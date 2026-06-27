#!/usr/bin/env python3
"""
OKX 适配器（单页应用SPA格式）
"""
import re
from typing import List, Dict, Any
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage, register_adapter
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


@register_adapter('okx')
class OKXAdapter(ExchangeAdapter):
    """OKX 单页应用适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def discover_pages(self) -> List[str]:
        """发现所有文档段落（通过锚点链接）"""
        start_url = self.config['crawler']['start_urls'][0]

        if not self.browser.open(start_url, wait=5):  # 增加等待时间
            raise Exception(f"无法打开页面: {start_url}")

        # 等待内容加载
        import time
        from urllib.parse import urlparse
        time.sleep(2)

        # 提取当前页面的base路径，用于过滤跨页面链接
        base_path = urlparse(start_url).path.rstrip('#')

        # 尝试多种方式提取链接
        # 方式1：侧边栏链接
        js1 = '''
        Array.from(document.querySelectorAll('a'))
            .filter(a => a.href && a.href.includes('#'))
            .map(a => a.href)
        '''

        links = self.browser.eval_js(js1)

        if not links:
            # 方式2：提取所有包含锚点的href
            js2 = '''
            Array.from(document.querySelectorAll('[href*="#"]'))
                .map(el => el.href)
                .filter(href => href && href.includes('/docs-v5/') && href.includes('#'))
            '''
            links = self.browser.eval_js(js2)

        if not links:
            log.warning("未找到任何锚点链接")
            return []

        # 去重
        unique_links = list(dict.fromkeys(links))

        # 过滤条件：
        # 1. 不以 # 结尾（没有具体锚点）
        # 2. 必须在同一个页面上（base路径相同）
        filtered_links = []
        cross_page_count = 0
        for link in unique_links:
            if link.endswith('#'):
                continue

            # 检查是否是同一页面的锚点
            link_path = urlparse(link).path
            if link_path == base_path or link_path + '/' == base_path or link_path == base_path + '/':
                filtered_links.append(link)
            else:
                cross_page_count += 1

        if cross_page_count > 0:
            log.info(f"过滤掉 {cross_page_count} 个跨页面链接")

        log.info(f"发现 {len(filtered_links)} 个段落（同页面）")

        return filtered_links

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取锚点对应的内容段落"""

        # 打开页面（SPA只需打开一次）
        if not skip_open:
            self.browser.open(url, wait=2)

        # 提取锚点ID
        anchor_match = re.search(r'#(.+)$', url)
        if not anchor_match:
            raise Exception(f"URL不包含锚点: {url}")

        anchor_id = anchor_match.group(1)
        import json
        anchor_id_js = json.dumps(anchor_id)

        # 提取该锚点对应的标题
        title_js = f'''
        (() => {{
            const elem = document.getElementById({anchor_id_js});
            if (!elem) return null;

            // 查找标题
            const heading = elem.tagName.match(/^H[1-6]$/) ? elem : elem.querySelector('h1, h2, h3, h4, h5, h6');
            return heading ? heading.textContent.trim() : null;
        }})()
        '''
        title = self.browser.eval_js(title_js) or anchor_id

        # 提取该段落的内容（从锚点元素到下一个同级标题之间的内容）
        js_extract = f'''
        (() => {{
            const anchor = document.getElementById({anchor_id_js});
            if (!anchor) return '';

            // 创建容器收集内容
            const container = document.createElement('div');

            // 从锚点元素开始往下遍历
            let current = anchor;
            const anchorLevel = parseInt(anchor.tagName?.match(/H([1-6])/)?.[1] || '2');

            while (current) {{
                current = current.nextElementSibling;
                if (!current) break;

                // 遇到同级或更高级别的标题就停止
                const match = current.tagName?.match(/H([1-6])/);
                if (match && parseInt(match[1]) <= anchorLevel) {{
                    break;
                }}

                container.appendChild(current.cloneNode(true));
            }}

            // 清理UI元素
            const selectors = [
                'nav', 'button', 'svg',
                '[class*="copy"]', '[class*="navigation"]'
            ];
            selectors.forEach(sel => {{
                container.querySelectorAll(sel).forEach(el => el.remove());
            }});

            return container.innerHTML;
        }})()
        '''

        html_content = self.browser.eval_js(js_extract)

        # 转换为Markdown
        markdown = self.md_processor.html_to_markdown(html_content or '')

        # 清理
        markdown = self._clean_markdown(markdown)

        # 提取元数据
        metadata = {
            'exchange': self.name,
            'source_url': url,
            'anchor_id': anchor_id,
            'api_type': self._detect_api_type(url, title)
        }

        return DocumentPage(
            url=url,
            title=title,
            content=markdown,
            metadata=metadata,
            raw_html=html_content
        )

    def save_page(self, page: DocumentPage, output_path: str):
        """保存页面到文件"""
        import os

        # 创建完整文档
        doc_content = self.md_processor.create_document(
            title=page.title,
            content=page.content,
            metadata=page.metadata
        )

        # 确保目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        return output_path

    def _clean_markdown(self, markdown: str) -> str:
        """清理Markdown内容"""
        import re

        # 移除常见的UI元素文本
        ui_patterns = [
            r'copyCopy.*?\n',
            r'\[Previous.*?\]\(.*?\)',
            r'\[Next.*?\]\(.*?\)',
        ]

        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        # 清理多余的空行
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown.strip()

    def _detect_api_type(self, url: str, title: str) -> str:
        """检测API类型"""
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'ws' in url_lower or 'websocket' in title_lower:
            return 'WebSocket'
        elif 'rest' in url_lower or 'rest' in title_lower:
            return 'REST'
        else:
            return 'API'

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """执行完整的OKX多语言多入口SPA爬取流程"""
        import os
        from pathlib import Path
        from urllib.parse import urlparse

        lang_configs = self.config['crawler']['languages']

        # 过滤指定的语言
        if languages:
            lang_configs = [lc for lc in lang_configs if lc['lang'] in languages]
            if not lang_configs:
                log.error(f"配置中未找到指定语言: {languages}")
                return

        log.info(f"开始多语言爬取，共 {len(lang_configs)} 种语言")

        # 遍历每个语言
        for lang_idx, lang_config in enumerate(lang_configs, 1):
            lang = lang_config['lang']
            start_urls = lang_config['start_urls']

            log.info(f"\n{'='*60}")
            log.info(f"[{lang_idx}/{len(lang_configs)}] 开始爬取语言: {lang.upper()}")
            log.info(f"{'='*60}")

            if not start_urls:
                log.warning(f"语言 {lang} 未定义 start_urls，跳过")
                continue

            log.success(f"发现 {len(start_urls)} 个入口")

            # 对每个入口分别爬取
            for entry_idx, start_url in enumerate(start_urls, 1):
                # 提取页面标识（用于日志显示）
                page_identifier = urlparse(start_url).path.strip('/').split('/')[-1]

                log.info(f"\n{'-'*50}")
                log.info(f"[{entry_idx}/{len(start_urls)}] 开始爬取: {page_identifier}")
                log.info(f"入口: {start_url}")
                log.info(f"{'-'*50}")

                # 发现该页面的所有段落（会自动过滤跨页面链接）
                log.info(f"发现 {page_identifier} 的段落...")

                # 临时保存当前start_url，让discover_pages使用
                original_urls = self.config['crawler'].get('start_urls')
                self.config['crawler']['start_urls'] = [start_url]

                urls = self.discover_pages()

                # 恢复原始配置
                if original_urls:
                    self.config['crawler']['start_urls'] = original_urls
                else:
                    self.config['crawler'].pop('start_urls', None)

                if not urls:
                    log.warning(f"{page_identifier} 未发现任何段落")
                    continue

                log.success(f"{page_identifier} 发现 {len(urls)} 个段落")

                # 限制爬取数量
                if limit and limit > 0:
                    urls = urls[:limit]
                    log.warning(f"限制模式：只爬取前 {len(urls)} 个段落")

                # 为该语言创建临时输出目录
                import tempfile
                temp_base = tempfile.gettempdir()
                output_dir = f"{temp_base}/crypto-api-docs/{self.name}/{lang}"
                os.makedirs(output_dir, exist_ok=True)

                # 提取内容（SPA所有内容在一个页面，顺序爬取）
                log.info(f"开始提取 {page_identifier} 内容...")
                success_count = 0
                for i, url in enumerate(urls, 1):
                    try:
                        # SPA只需在第一次打开页面
                        skip_open = (i > 1)
                        page = self.extract_content(url, skip_open=skip_open)

                        # 生成文件路径：将锚点ID转换为目录结构
                        from ..utils.path_generator import anchor_to_filepath, is_hash_anchor, safe_output_path, slugify_title
                        anchor_id = page.metadata.get('anchor_id', str(i))

                        # 如果锚点是哈希格式，使用标题生成文件名
                        if is_hash_anchor(anchor_id):
                            filepath = f"{slugify_title(page.title)}.md"
                        else:
                            filepath = anchor_to_filepath(anchor_id)

                        output_path = safe_output_path(output_dir, filepath)

                        # 确保子目录存在
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)

                        self.save_page(page, output_path)
                        log.success(f"[{i}/{len(urls)}] {page.title}")
                        success_count += 1
                    except Exception as e:
                        log.error(f"[{i}/{len(urls)}] {url} - {e}")

                log.success(f"{page_identifier} 完成! 成功: {success_count}/{len(urls)}")

        # 全部完成
        log.info("\n" + "="*60)
        log.info("所有语言爬取完成")

        # 如果爬取了多种语言，合并成双语文件
        if len(lang_configs) > 1:
            log.info("开始合并双语文件...")
            import tempfile
            temp_base = f"{tempfile.gettempdir()}/crypto-api-docs/{self.name}"
            final_output_dir = self.get_output_path()
            merged_count = self._merge_bilingual_files(temp_base, final_output_dir, [lc['lang'] for lc in lang_configs])
            log.success(f"合并完成：{merged_count} 个文件")

            # 删除临时文件
            log.info("清理临时文件...")
            if os.path.exists(temp_base):
                from ..utils.path_generator import safe_rmtree
                safe_rmtree(temp_base, [os.path.join(tempfile.gettempdir(), "crypto-api-docs")])
            log.success("临时文件已删除")

        # 生成索引
        log.info("生成索引...")
        from ..utils.indexer import DocumentIndexer
        project_root = Path(__file__).parent.parent.parent
        index_dir = project_root / "index"

        # 为整个 okx 目录生成索引
        base_output_dir = self.get_output_path()
        indexer = DocumentIndexer(base_output_dir)
        index_path = indexer.generate_index(str(index_dir))
        log.success(f"索引已生成: {index_path}")

        # 更新主 README
        log.info("更新 README...")
        from ..utils.readme_updater import ReadmeUpdater
        updater = ReadmeUpdater(str(project_root))
        readme_path = updater.update_exchange_table()
        log.success(f"README 已更新: {readme_path}")

    def _remove_trailing_separator(self, content: str) -> str:
        """移除内容末尾的 markdown 分隔线"""
        import re
        return re.sub(r'\n+(\*\s*\*\s*\*|---)\s*$', '', content.rstrip())

    def _merge_bilingual_files(self, temp_dir: str, output_dir: str, languages: List[str]) -> int:
        """合并多语言文件为双语文件

        Args:
            temp_dir: 临时目录，如 /tmp/crypto-api-docs/okx
            output_dir: 最终输出目录，如 docs/okx
            languages: 语言列表，如 ['en', 'zh']

        Returns:
            合并的文件数量
        """
        import os
        import glob
        from ..utils.path_generator import safe_output_path

        if len(languages) < 2:
            return 0

        # 假设第一种语言是主语言（英文）
        primary_lang = languages[0]
        primary_dir = os.path.join(temp_dir, primary_lang)

        if not os.path.exists(primary_dir):
            log.warning(f"主语言目录不存在: {primary_dir}")
            return 0

        # 遍历主语言的所有文件
        pattern = os.path.join(primary_dir, '**', '*.md')
        primary_files = glob.glob(pattern, recursive=True)
        merged_count = 0

        for primary_file in primary_files:
            # 获取相对路径（相对于语言目录）
            rel_path = os.path.relpath(primary_file, primary_dir)

            # 读取主语言内容
            with open(primary_file, 'r', encoding='utf-8') as f:
                primary_content = f.read()

            # 收集其他语言的内容
            other_contents = []
            for lang in languages[1:]:
                lang_file = os.path.join(temp_dir, lang, rel_path)
                if os.path.exists(lang_file):
                    with open(lang_file, 'r', encoding='utf-8') as f:
                        other_contents.append((lang, f.read()))

            # 如果有其他语言的内容，合并
            if other_contents:
                # 构建合并后的内容
                # 先移除英文内容末尾的 markdown 分隔线（如果有）
                primary_content = self._remove_trailing_separator(primary_content)
                merged_content = primary_content

                for lang, content in other_contents:
                    # 移除次要语言内容中的 metadata（YAML front matter）
                    lines = content.split('\n')
                    if lines and lines[0].strip() == '---':
                        # 找到第二个 ---
                        end_idx = 1
                        for i in range(1, len(lines)):
                            if lines[i].strip() == '---':
                                end_idx = i + 1
                                break
                        # 跳过 metadata，保留后面的内容
                        content = '\n'.join(lines[end_idx:]).strip()

                    # 移除内容末尾的分隔线
                    content = self._remove_trailing_separator(content)

                    # 添加分隔符和次要语言内容
                    merged_content += f"\n\n---\n\n"
                    merged_content += content

                # 写入合并后的文件到最终目录
                output_file = safe_output_path(output_dir, rel_path)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(merged_content)

                merged_count += 1

        return merged_count
