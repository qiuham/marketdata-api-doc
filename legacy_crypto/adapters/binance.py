#!/usr/bin/env python3
"""
Binance 适配器（Docusaurus 格式）
"""
import time
from typing import List, Dict, Any
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage, register_adapter
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


@register_adapter('binance')
class BinanceAdapter(ExchangeAdapter):
    """Binance Docusaurus 适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def discover_pages(self) -> List[str]:
        """发现当前页面的所有文档页面（使用当前已打开的页面）"""

        # 获取当前页面URL，用于过滤相关页面
        current_url_js = 'window.location.href'
        current_url = self.browser.eval_js(current_url_js)

        if not current_url:
            log.error("无法获取当前页面URL")
            return []

        # 从URL提取产品路径前缀（用于过滤）
        # 英文: https://developers.binance.com/docs/derivatives/... -> https://.../docs/derivatives/
        # 中文: https://developers.binance.com/docs/zh-CN/derivatives/... -> https://.../docs/zh-CN/derivatives/
        import re
        # 匹配到第二或第三个斜杠后的部分
        match = re.match(r'(https://[^/]+/docs/(?:[^/]+/)?[^/]+/)', current_url)
        if not match:
            log.warning(f"无法从URL提取产品路径: {current_url}")
            product_prefix = None
        else:
            product_prefix = match.group(1)
            log.info(f"产品路径前缀: {product_prefix}")

        # 展开所有折叠菜单（在Python中循环，让React有时间渲染）
        collapsed_selector = self.config['crawler']['selectors']['collapsed_menu']
        max_iterations = 50  # 防止死循环

        for i in range(max_iterations):
            # 统计折叠菜单数量
            count = self.browser.count_elements(collapsed_selector)
            if count == 0:
                log.info("所有菜单已展开")
                break

            if i < 3 or i % 5 == 0:  # 只显示前3次和每5次
                log.info(f"[轮次 {i+1}] 折叠菜单: {count} 个")

            # 点击折叠菜单里的 a[role="button"]
            js_expand = '''
            const collapsedItems = document.querySelectorAll('.menu__list-item--collapsed');
            let expanded = 0;

            collapsedItems.forEach(item => {
                const link = item.querySelector('a[role="button"]');
                if (link) {
                    try {
                        link.click();
                        expanded++;
                    } catch(e) {}
                }
            });

            expanded;
            '''

            clicked = self.browser.eval_js(js_expand)
            if not clicked or clicked == 0:
                break

            # 不需要 sleep，Python/Browser往返间React会完成渲染

        # 提取所有文档链接
        doc_link_selector = self.config['crawler']['selectors']['doc_link']
        js = f'''
        Array.from(document.querySelectorAll('{doc_link_selector}'))
            .map(a => a.href)
            .filter(href => href && !href.endsWith('#'))
        '''

        links = self.browser.eval_js(js)

        if not links:
            return []

        # 如果有产品前缀，过滤只保留当前产品的页面
        if product_prefix:
            filtered_links = [link for link in links if link.startswith(product_prefix)]
            log.info(f"过滤前: {len(links)} 个链接，过滤后: {len(filtered_links)} 个链接")
            links = filtered_links

        # 去重并排序
        unique_links = list(set(links))
        unique_links.sort()

        log.info(f"发现 {len(unique_links)} 个唯一页面（去重后）")
        return unique_links

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面内容"""

        # 打开页面
        if not skip_open:
            self.browser.open(url, wait=2)

        # 提取标题（在 article 内查找第一个 h1）
        title_js = '''
        (function() {
            // 优先从 article 内查找 h1
            const article = document.querySelector('main article');
            if (article) {
                const h1 = article.querySelector('h1');
                if (h1) return h1.textContent.trim();
            }

            // 其次查找页面任意 h1
            const anyH1 = document.querySelector('h1');
            if (anyH1) return anyH1.textContent.trim();

            // 最后用 document.title，去掉后缀
            return document.title.split('|')[0].trim();
        })()
        '''
        title = self.browser.eval_js(title_js) or "Untitled"

        # 提取主内容
        content_selector = self.config['crawler']['selectors']['main_content']
        js_extract = f'''
        (function() {{
            const main = document.querySelector('{content_selector}');
            if (!main) return null;

            // 克隆节点
            const clone = main.cloneNode(true);

            // 清理不需要的元素
            const selectors = [
                'nav', 'header', 'footer', 'button',
                '[class*="copy"]', 'svg'
            ];

            selectors.forEach(sel => {{
                clone.querySelectorAll(sel).forEach(el => el.remove());
            }});

            return clone.innerHTML;
        }})()
        '''

        html_content = self.browser.eval_js(js_extract)

        if not html_content:
            log.warning(f"无法提取内容: {url}")
            return DocumentPage(
                url=url,
                title=title,
                content="",
                metadata={},
                raw_html=""
            )

        # 转换为 Markdown
        markdown = self.md_processor.html_to_markdown(html_content)
        markdown = self._clean_markdown(markdown)

        # 提取元数据
        metadata = {
            'exchange': self.name,
            'source_url': url,
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
        from ..utils.markdown import MarkdownProcessor

        processor = MarkdownProcessor()

        # 创建完整文档
        doc_content = processor.create_document(
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
            r'copyCopy.*?\\n',
            r'\\[Previous.*?\\]\\(.*?\\)',
            r'\\[Next.*?\\]\\(.*?\\)',
            r'Last updated.*?\\n'
        ]

        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        # 清理多余的空行
        markdown = re.sub(r'\\n{3,}', '\\n\\n', markdown)

        return markdown.strip()

    def _remove_first_h1(self, markdown: str) -> str:
        """移除第一个 h1 标题"""
        import re

        # 匹配第一个 h1（行首的 # ）
        pattern = r'^# .+?$'
        markdown = re.sub(pattern, '', markdown, count=1, flags=re.MULTILINE)

        # 清理开头的空行
        return markdown.lstrip()

    def _detect_api_type(self, url: str, title: str) -> str:
        """检测API类型"""
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'websocket' in title_lower or 'ws' in url_lower:
            return 'WebSocket'
        elif 'market' in url_lower or '行情' in title_lower:
            return 'Market Data'
        elif 'trade' in url_lower or '交易' in title_lower:
            return 'Trading'
        elif 'account' in url_lower or '账户' in title_lower:
            return 'Account'
        else:
            return 'REST'

    def _extract_product_dir(self, url: str) -> str:
        """从URL提取产品目录名

        例如:
        英文: https://.../docs/binance-spot-api-docs/... -> binance-spot-api-docs
        中文: https://.../docs/zh-CN/binance-spot-api-docs/... -> binance-spot-api-docs
        """
        import re
        # 先尝试匹配 /docs/{lang}/{product}/ 格式（中文）
        match = re.search(r'/docs/(zh-CN|en|zh|ja|ko)/([^/]+)', url)
        if match:
            return match.group(2)

        # 再尝试匹配 /docs/{product}/ 格式（英文）
        match = re.search(r'/docs/([^/]+)/', url)
        if match:
            return match.group(1)

        log.warning(f"无法从URL提取产品目录名: {url}")
        return 'default'

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """执行完整的Binance多语言多入口爬取流程"""
        import os
        from pathlib import Path

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

            # 临时替换配置的 start_urls
            original_urls = self.config['crawler'].get('start_urls')
            self.config['crawler']['start_urls'] = start_urls

            # 对每个入口分别爬取
            for i, entry_url in enumerate(start_urls, 1):
                product_dir = self._extract_product_dir(entry_url)

                log.info(f"\n{'-'*50}")
                log.info(f"[{i}/{len(start_urls)}] 开始爬取: {product_dir}")
                log.info(f"{'-'*50}")

                # 打开入口页面
                if not self.browser.open(entry_url, wait=3):
                    log.error(f"无法打开入口页面: {entry_url}")
                    continue

                # 发现该入口的所有页面
                log.info(f"发现 {product_dir} 的页面...")
                urls = self.discover_pages()

                if not urls:
                    log.warning(f"{product_dir} 未发现任何页面")
                    continue

                log.success(f"{product_dir} 发现 {len(urls)} 个页面")

                # 限制爬取数量
                if limit and limit > 0:
                    urls = urls[:limit]
                    log.warning(f"限制模式：只爬取前 {len(urls)} 页")

                # 为该产品和语言创建临时输出目录
                import tempfile
                temp_base = tempfile.gettempdir()
                output_dir = f"{temp_base}/crypto-api-docs/{self.name}/{lang}/{product_dir}"
                os.makedirs(output_dir, exist_ok=True)

                # 提取内容
                log.info(f"开始提取 {product_dir} 内容...")

                if concurrency == 1:
                    success_count = self._crawl_sequential(urls, output_dir)
                else:
                    success_count = self._crawl_concurrent(urls, output_dir, concurrency)

                log.success(f"{product_dir} 完成! 成功: {success_count}/{len(urls)}")

            # 恢复原始配置
            if original_urls:
                self.config['crawler']['start_urls'] = original_urls
            else:
                self.config['crawler'].pop('start_urls', None)

        # 全部完成后，合并双语文件
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

        # 为整个 binance 目录生成索引
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
            temp_dir: 临时目录，如 /tmp/crypto-api-docs/binance
            output_dir: 最终输出目录，如 docs/binance
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

    def _crawl_sequential(self, urls, output_dir):
        """顺序爬取"""
        import re
        import os
        from ..utils.path_generator import safe_output_path, url_to_filepath

        # 获取产品前缀用于生成文件名
        # 英文: https://.../docs/derivatives/... -> https://.../docs/derivatives/
        # 中文: https://.../docs/zh-CN/derivatives/... -> https://.../docs/zh-CN/derivatives/
        if urls and hasattr(self, 'browser'):
            current_url = self.browser.eval_js('window.location.href')
            match = re.match(r'(https://[^/]+/docs/(?:[^/]+/)?[^/]+/)', current_url) if current_url else None
            product_prefix = match.group(1) if match else None
        else:
            product_prefix = None

        success_count = 0
        for i, url in enumerate(urls, 1):
            try:
                filename = url_to_filepath(url, product_prefix)
                output_path = safe_output_path(output_dir, filename)
                # 确保子目录存在
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                page = self.extract_content(url)
                self.save_page(page, output_path)
                log.success(f"[{i}/{len(urls)}] {page.title}")
                success_count += 1
            except Exception as e:
                log.error(f"[{i}/{len(urls)}] {url} - {e}")
        return success_count

    def _crawl_concurrent(self, urls, output_dir, concurrency):
        """多标签并发爬取"""
        import re
        import os
        from ..utils.path_generator import safe_output_path, url_to_filepath

        browser = self.browser
        total = len(urls)
        success_count = 0

        # 获取产品前缀用于生成文件名
        # 英文: https://.../docs/derivatives/... -> https://.../docs/derivatives/
        # 中文: https://.../docs/zh-CN/derivatives/... -> https://.../docs/zh-CN/derivatives/
        if urls:
            current_url = browser.eval_js('window.location.href')
            match = re.match(r'(https://[^/]+/docs/(?:[^/]+/)?[^/]+/)', current_url) if current_url else None
            product_prefix = match.group(1) if match else None
        else:
            product_prefix = None

        # 已有tab 0，再创建N-1个新标签
        num_tabs = min(concurrency, total)
        browser.open_tabs_batch(num_tabs - 1)

        for batch_start in range(0, total, num_tabs):
            batch_urls = urls[batch_start:batch_start + num_tabs]

            # 1. 批量加载URLs
            browser.load_urls_batch(batch_urls, start_tab=0)

            # 2. 顺序提取内容
            for i, url in enumerate(batch_urls):
                idx = batch_start + i + 1
                try:
                    browser.tab_switch(i)

                    # 等待页面加载完成
                    if not browser.wait_for_element('main', timeout=30):
                        log.warning(f"[{idx}/{total}] 页面加载超时，尝试继续")

                    filename = url_to_filepath(url, product_prefix)
                    output_path = safe_output_path(output_dir, filename)
                    # 确保子目录存在
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    page = self.extract_content(url, skip_open=True)
                    self.save_page(page, output_path)

                    log.success(f"[{idx}/{total}] {page.title}")
                    success_count += 1
                except Exception as e:
                    log.error(f"[{idx}/{total}] {url} - {e}")

        return success_count
