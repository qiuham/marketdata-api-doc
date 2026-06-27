#!/usr/bin/env python3
"""
Hyperliquid 适配器（GitBook格式）
"""
import time
from typing import List, Dict, Any
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage, register_adapter
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


@register_adapter('hyperliquid')
class HyperliquidAdapter(ExchangeAdapter):
    """Hyperliquid GitBook 适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def discover_pages(self) -> List[str]:
        """递归发现 For Developers 下的所有文档页面"""
        import json
        from urllib.parse import urlparse

        start_urls = self.config['crawler']['start_urls']
        start_url = start_urls[0] if start_urls else None

        if not start_url:
            raise Exception("配置文件中未定义 start_urls")

        scope_prefixes = self.config.get('crawler', {}).get('scope_prefixes')
        if not scope_prefixes:
            parsed = urlparse(start_url)
            marker = '/for-developers/'
            if marker in parsed.path:
                scope_path = parsed.path[:parsed.path.index(marker) + len(marker)]
                scope_prefixes = [f"{parsed.scheme}://{parsed.netloc}{scope_path}"]
            else:
                scope_prefixes = [start_url.rstrip('/') + '/']

        normalized_prefixes = [prefix.rstrip('/') for prefix in scope_prefixes]
        scope_prefixes_json = json.dumps(normalized_prefixes)
        max_pages = self.config.get('crawler', {}).get('max_discovery_pages', 500)

        def normalize_url(url: str) -> str:
            return (url or '').split('#')[0].rstrip('/')

        def in_scope(url: str) -> bool:
            return any(url == prefix or url.startswith(prefix + '/') for prefix in normalized_prefixes)

        def collect_current_page_links() -> List[str]:
            """展开当前 GitBook 页面并收集范围内链接。"""
            collected = set()
            last_count = -1
            stable_rounds = 0

            for _ in range(12):
                js = f'''
        (function() {{
            const scopePrefixes = {scope_prefixes_json};
            let clicked = 0;

            [
                'button[aria-expanded="false"]',
                '[role="button"][aria-expanded="false"]',
                'summary:not([open])'
            ].forEach(selector => {{
                document.querySelectorAll(selector).forEach(el => {{
                    try {{
                        el.click();
                        clicked++;
                    }} catch(e) {{}}
                }});
            }});

            document.querySelectorAll('aside, nav, [role="navigation"]').forEach(el => {{
                try {{
                    if (el.scrollHeight > el.clientHeight) el.scrollTop = el.scrollHeight;
                }} catch(e) {{}}
            }});
            try {{ window.scrollTo(0, document.body.scrollHeight); }} catch(e) {{}}

            const links = Array.from(document.querySelectorAll('a'))
                .map(a => (a.href || '').split('#')[0].replace(/\\/$/, ''))
                .filter(href => href && !href.endsWith('#'))
                .filter(href => !href.includes('/~/'))
                .filter(href => scopePrefixes.some(prefix => href === prefix || href.startsWith(prefix + '/')));
            return {{ clicked, links: Array.from(new Set(links)).sort() }};
        }})()
                '''

                result = self.browser.eval_js(js) or {}
                links = result.get('links') or []
                collected.update(links)

                if len(collected) == last_count:
                    stable_rounds += 1
                else:
                    stable_rounds = 0
                last_count = len(collected)

                if stable_rounds >= 2:
                    break
                time.sleep(0.2)

            return sorted(collected)

        discovered = set()
        processed = set()
        queue = [normalize_url(url) for url in start_urls]

        while queue and len(discovered) < max_pages:
            current_url = normalize_url(queue.pop(0))
            if not current_url or current_url in processed or not in_scope(current_url):
                continue

            processed.add(current_url)
            discovered.add(current_url)

            if not self.browser.open(current_url, wait=3):
                log.warning(f"无法打开页面，跳过发现子链接: {current_url}")
                continue

            links = collect_current_page_links()
            log.info(f"发现链接: {current_url} -> {len(links)} 个")

            for link in links:
                link = normalize_url(link)
                if link and in_scope(link) and link not in discovered:
                    discovered.add(link)
                    if link not in processed and link not in queue:
                        queue.append(link)

        if len(discovered) >= max_pages:
            log.warning(f"达到最大页面发现数量: {max_pages}")

        unique_links = sorted(discovered)

        return unique_links

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面内容"""

        # 打开页面（并发模式下已打开则跳过）
        if not skip_open:
            self.browser.open(url, wait=2)  # 减少到 2 秒

        # 提取标题
        title_js = 'document.querySelector("h1")?.textContent?.trim() || document.title'
        title = self.browser.eval_js(title_js) or "Untitled"

        # GitBook特殊处理：提取页面正文，排除导航和UI元素
        js_extract = r'''
        (function() {
            const main = document.querySelector('main, article, [role="main"]');
            if (!main) return null;

            // 克隆节点避免修改原始DOM
            const clone = main.cloneNode(true);

            // 1. 转换 role="table" 为真正的 <table>
            clone.querySelectorAll('[role="table"]').forEach(divTable => {
                const table = document.createElement('table');

                divTable.querySelectorAll('[role="rowgroup"]').forEach((rowGroup, idx) => {
                    const section = idx === 0 ? document.createElement('thead') : document.createElement('tbody');

                    rowGroup.querySelectorAll('[role="row"]').forEach(divRow => {
                        const tr = document.createElement('tr');

                        divRow.querySelectorAll('[role="columnheader"], [role="cell"]').forEach(divCell => {
                            const cell = divCell.getAttribute('role') === 'columnheader'
                                ? document.createElement('th')
                                : document.createElement('td');
                            cell.innerHTML = divCell.innerHTML;
                            tr.appendChild(cell);
                        });

                        section.appendChild(tr);
                    });

                    table.appendChild(section);
                });

                divTable.replaceWith(table);
            });

            // 2. 清理标题中的 "hashtag" 文本
            clone.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(heading => {
                // 移除包含 "hashtag" 的子元素
                heading.querySelectorAll('.hash, [class*="hash"]').forEach(el => el.remove());
                // 清理文本
                heading.textContent = heading.textContent.replace(/^hashtag\s*/i, '').trim();
            });

            // 3. 移除不需要的元素
            const selectors = [
                'nav', 'header', 'footer',
                '.page-api-block:first-child',  // 面包屑
                'button',  // 所有按钮
                '[class*="copy"]',  // 复制按钮
                'svg'  // SVG图标
            ];

            selectors.forEach(sel => {
                clone.querySelectorAll(sel).forEach(el => el.remove());
            });

            return clone.innerHTML;
        })()
        '''

        html_content = self.browser.eval_js(js_extract)

        if not html_content:
            log.warning("无法提取内容")
            return DocumentPage(
                url=url,
                title=title,
                content="",
                metadata={},
                raw_html=""
            )

        # 转换为 Markdown
        markdown = self.md_processor.html_to_markdown(html_content)

        # 后处理：清理多余文本
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
        from ..utils.markdown import MarkdownProcessor, sanitize_filename

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
            r'copyCopy.*?\n',
            r'chevron-right',
            r'chevron-left',
            r'chevron-down',
            r'chevron-up',
            r'arrow-up-right',
            r'arrow-down',
            r'\[Previous.*?\]\(.*?\)',
            r'\[Next.*?\]\(.*?\)',
            r'Last updated.*?\n'
        ]

        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        # 清理空的标题标记（只有 # 但没有文本）
        markdown = re.sub(r'^(#{1,6})\s*$', '', markdown, flags=re.MULTILINE)

        # 清理多余的空行
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown.strip()

    def _detect_api_type(self, url: str, title: str) -> str:
        """检测API类型"""
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'websocket' in title_lower:
            return 'WebSocket'
        else:
            return 'REST'

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """执行完整的Hyperliquid单入口爬取流程"""
        import os
        from pathlib import Path

        log.info("获取爬取入口...")

        # 从配置读取 start_urls（hyperliquid只有一个）
        start_urls = self.config['crawler']['start_urls']

        if not start_urls:
            log.error("配置文件中未定义 start_urls")
            return

        start_url = start_urls[0]  # 取第一个
        log.success(f"入口: {start_url}")

        # 发现所有页面
        log.info("发现页面...")
        urls = self.discover_pages()

        if not urls:
            log.error("未发现任何页面")
            return

        log.success(f"发现 {len(urls)} 个页面")

        # 限制爬取数量
        if limit and limit > 0:
            urls = urls[:limit]
            log.warning(f"限制模式：只爬取前 {len(urls)} 页")

        # 初始化输出目录
        output_dir = self.get_output_path()
        os.makedirs(output_dir, exist_ok=True)

        # 提取内容（hyperliquid暂不支持并发，因为没有实现）
        log.info("开始提取内容...")
        from ..utils.path_generator import safe_output_path, url_to_filepath

        # 获取基础URL前缀
        base_prefix = "https://hyperliquid.gitbook.io/hyperliquid-docs/"

        success_count = 0
        for i, url in enumerate(urls, 1):
            try:
                page = self.extract_content(url)
                # 使用URL路径生成目录结构
                filepath = url_to_filepath(url, base_prefix)
                output_path = safe_output_path(output_dir, filepath)
                # 确保子目录存在
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.save_page(page, output_path)
                log.success(f"[{i}/{len(urls)}] {page.title}")
                success_count += 1
            except Exception as e:
                log.error(f"[{i}/{len(urls)}] {url} - {e}")

        log.success(f"完成! 成功: {success_count}/{len(urls)}")
        log.info(f"保存在: {output_dir}")

        # 生成索引
        log.info("生成索引...")
        from ..utils.indexer import DocumentIndexer
        project_root = Path(__file__).parent.parent.parent
        index_dir = project_root / "index"
        indexer = DocumentIndexer(output_dir)
        index_path = indexer.generate_index(str(index_dir))
        log.success(f"索引已生成: {index_path}")

        # 更新主 README
        log.info("更新 README...")
        from ..utils.readme_updater import ReadmeUpdater
        updater = ReadmeUpdater(str(project_root))
        readme_path = updater.update_exchange_table()
        log.success(f"README 已更新: {readme_path}")
