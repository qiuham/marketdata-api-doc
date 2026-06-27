#!/usr/bin/env python3
"""
Coinbase Advanced Trade API 适配器（Mintlify/Next 静态 HTML）
"""
import html as html_lib
import os
import re
from http.client import IncompleteRead
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from loguru import logger as log

from .base import DocumentPage, ExchangeAdapter, register_adapter
from ..utils.markdown import MarkdownProcessor


@register_adapter('coinbase')
class CoinbaseAdapter(ExchangeAdapter):
    """Coinbase Mintlify 文档适配器"""

    USER_AGENT = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/148.0.0.0 Safari/537.36'
    )

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.md_processor = MarkdownProcessor()
        crawler_config = self.config.get('crawler', {})
        self.scope_prefixes = [
            self._normalize_url(prefix)
            for prefix in crawler_config.get('scope_prefixes', [])
        ]
        self.base_prefix = crawler_config.get('base_prefix', 'https://docs.cdp.coinbase.com/')

    def discover_pages(self) -> List[str]:
        """从 Mintlify SSR HTML/序列化侧边栏中发现 Advanced Trade 页面。"""
        start_urls = [
            self._normalize_url(url)
            for url in self.config.get('crawler', {}).get('start_urls', [])
        ]
        max_pages = self.config.get('crawler', {}).get('max_discovery_pages', 300)

        discovered = set(start_urls)

        for start_url in start_urls:
            html = self._fetch_html(start_url)
            if not html:
                log.warning(f"无法读取入口: {start_url}")
                continue

            links = self._extract_scoped_links(html, start_url)
            log.info(f"入口发现: {start_url} -> {len(links)} 个链接")
            discovered.update(links)

        unique_links = sorted(link for link in discovered if self._in_scope(link))

        if len(unique_links) > max_pages:
            log.warning(f"发现页面超过上限 {max_pages}，已截断")
            unique_links = unique_links[:max_pages]

        log.success(f"Coinbase Advanced Trade 共发现 {len(unique_links)} 个页面")
        return unique_links

    def extract_content(self, url: str) -> DocumentPage:
        """提取页面内容。"""
        normalized_url = self._normalize_url(url)
        html = self._fetch_html(normalized_url)
        if not html:
            raise RuntimeError(f"无法读取页面: {normalized_url}")

        if self._is_bad_page(html):
            raise RuntimeError(f"检测到坏页/验证页: {normalized_url}")

        title = self._extract_title(html)
        content_html = self._extract_content_area(html)
        if not content_html:
            raise RuntimeError(f"未找到正文区域: {normalized_url}")

        cleaned_html = self._clean_html(content_html)
        markdown = self.md_processor.html_to_markdown(cleaned_html)
        markdown = self._clean_markdown(markdown)

        endpoint = self._extract_endpoint(markdown)
        if endpoint:
            markdown = self._remove_operation_card_noise(markdown)
        if endpoint and not markdown.startswith('**Endpoint:**'):
            markdown = f"**Endpoint:** `{endpoint}`\n\n{markdown}"

        metadata = {
            'exchange': self.name,
            'source_url': normalized_url,
            'api_type': self._detect_api_type(normalized_url, title)
        }

        return DocumentPage(
            url=normalized_url,
            title=title,
            content=markdown,
            metadata=metadata,
            raw_html=content_html
        )

    def save_page(self, page: DocumentPage, output_path: str):
        """保存页面到 Markdown。"""
        doc_content = self.md_processor.create_document(
            title=page.title,
            content=page.content,
            metadata=page.metadata
        )

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        return output_path

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """执行 Coinbase Advanced Trade 爬取流程。"""
        from pathlib import Path
        from ..utils.indexer import DocumentIndexer
        from ..utils.path_generator import safe_output_path, url_to_filepath
        from ..utils.readme_updater import ReadmeUpdater

        urls = self.discover_pages()
        if not urls:
            log.error("未发现任何 Coinbase 页面")
            return

        if limit and limit > 0:
            urls = urls[:limit]
            log.warning(f"限制模式：只爬取前 {len(urls)} 页")

        output_dir = self.get_output_path()
        os.makedirs(output_dir, exist_ok=True)

        base_prefix = self.config.get('crawler', {}).get('base_prefix', self.base_prefix)
        log.info(f"开始提取 Coinbase 内容，并发: {concurrency}")

        success_count = 0
        if concurrency <= 1:
            for i, url in enumerate(urls, 1):
                if self._crawl_one(i, len(urls), url, output_dir, base_prefix):
                    success_count += 1
        else:
            workers = min(concurrency, len(urls))
            with ThreadPoolExecutor(max_workers=workers) as executor:
                future_map = {
                    executor.submit(self._crawl_one, i, len(urls), url, output_dir, base_prefix): url
                    for i, url in enumerate(urls, 1)
                }
                for future in as_completed(future_map):
                    if future.result():
                        success_count += 1

        log.success(f"完成! 成功: {success_count}/{len(urls)}")

        project_root = Path(__file__).parent.parent.parent
        indexer = DocumentIndexer(output_dir)
        index_path = indexer.generate_index(str(project_root / "index"))
        log.success(f"索引已生成: {index_path}")

        updater = ReadmeUpdater(str(project_root))
        readme_path = updater.update_exchange_table()
        log.success(f"README 已更新: {readme_path}")

    def _crawl_one(self, index: int, total: int, url: str, output_dir: str, base_prefix: str) -> bool:
        from ..utils.path_generator import safe_output_path, url_to_filepath

        try:
            page = self.extract_content(url)
            filepath = url_to_filepath(url, base_prefix)
            output_path = safe_output_path(output_dir, filepath)
            self.save_page(page, output_path)
            log.success(f"[{index}/{total}] {page.title}")
            return True
        except Exception as exc:
            log.error(f"[{index}/{total}] {url} - {exc}")
            return False

    def _fetch_html(self, url: str) -> Optional[str]:
        """用普通 HTTP 获取 Mintlify SSR HTML。"""
        request_url = url if url.endswith('/') else url
        headers = {
            'User-Agent': self.USER_AGENT,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        last_error = None
        for attempt in range(1, 4):
            try:
                req = Request(request_url, headers=headers)
                with urlopen(req, timeout=30) as response:
                    charset = response.headers.get_content_charset() or 'utf-8'
                    try:
                        data = response.read()
                    except IncompleteRead as exc:
                        data = exc.partial
                        log.warning(f"响应提前结束，使用已读取内容: {url} ({len(data)} bytes)")
                    return data.decode(charset, errors='replace')
            except (HTTPError, URLError, TimeoutError, OSError) as exc:
                last_error = exc
                log.warning(f"请求失败({attempt}/3): {url} - {exc}")

        log.warning(f"请求最终失败: {url} - {last_error}")
        return None

    def _extract_scoped_links(self, html: str, base_url: str) -> List[str]:
        """从普通 href 和 Next/Mintlify 序列化 JSON 中提取范围内链接。"""
        hrefs = set()
        patterns = [
            r'href=(?:"|\\"|\')([^"\'\\]+)(?:"|\\"|\')',
            r'"href"\s*:\s*"([^"\\]+)"',
            r'\\"href\\"\s*:\s*\\"([^"\\]+)\\"',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, html):
                hrefs.add(html_lib.unescape(match.group(1)))

        links = set()
        for href in hrefs:
            if not href or href.startswith(('#', 'mailto:', 'javascript:')):
                continue

            url = self._normalize_url(urljoin(base_url, href))
            if self._in_scope(url) and not self._is_asset_url(url):
                links.add(url)

        return sorted(links)

    def _extract_content_area(self, html: str) -> str:
        """优先提取 Mintlify content-area，回退到 mdx-content。"""
        match = re.search(r'<div\b[^>]*id="content-area"[^>]*>', html, flags=re.IGNORECASE)
        if match:
            content = self._extract_balanced_tag(html, match.start(), 'div')
            if content:
                return content

        match = re.search(
            r'<div\b(?=[^>]*\bmdx-content\b)[^>]*>',
            html,
            flags=re.IGNORECASE
        )
        if match:
            return self._extract_balanced_tag(html, match.start(), 'div')

        return ""

    def _extract_balanced_tag(self, html: str, start: int, tag_name: str) -> str:
        pattern = re.compile(rf'<\s*(/?)\s*{re.escape(tag_name)}\b[^>]*?>', re.IGNORECASE)
        depth = 0

        for match in pattern.finditer(html, start):
            token = match.group(0)
            is_closing = bool(match.group(1))
            is_self_closing = token.rstrip().endswith('/>')

            if is_closing:
                depth -= 1
                if depth == 0:
                    return html[start:match.end()]
            elif not is_self_closing:
                depth += 1

        return ""

    def _clean_html(self, html: str) -> str:
        """移除脚本、按钮、图标等 UI 噪声。"""
        for tag in ['script', 'style', 'svg', 'button']:
            html = re.sub(
                rf'<{tag}\b[^>]*>.*?</{tag}>',
                '',
                html,
                flags=re.IGNORECASE | re.DOTALL
            )

        html = re.sub(
            r'<div\b[^>]*data-fade-overlay="true"[^>]*>.*?</div>',
            '',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
        html = re.sub(
            r'<div\b[^>]*id="page-context-menu"[^>]*>.*?</div>',
            '',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )

        return html

    def _clean_markdown(self, markdown: str) -> str:
        """清理 Mintlify UI 文案和空标题。"""
        markdown = markdown.replace('\u200b', '')
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        # Mintlify heading anchor 会被 html2text 拆成空标题 + 标题文本。
        markdown = re.sub(
            r'^(#{1,6})\s*\n+([^\n#][^\n]*)$',
            r'\1 \2',
            markdown,
            flags=re.MULTILINE
        )

        # 去掉 h1 前面的 eyebrow/category 文案，避免重复标题前多一行分类。
        first_h1 = re.search(r'^#\s+', markdown, flags=re.MULTILINE)
        if first_h1:
            markdown = markdown[first_h1.start():]

        ui_patterns = [
            r'Was this page helpful\?.*',
            r'\[.*?Previous\]\(.*?\)',
            r'\[.*?Next\]\(.*?\)',
            r'Copy page',
            r'Try it',
            r'More actions',
        ]
        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        markdown = re.sub(r'^\s*⌘[A-Za-z]\s*$', '', markdown, flags=re.MULTILINE)
        markdown = re.sub(r'^\s*Show child attributes\s*$', '', markdown, flags=re.MULTILINE)
        markdown = re.sub(r'^\s*Hide child attributes\s*$', '', markdown, flags=re.MULTILINE)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown.strip()

    def _extract_title(self, html: str) -> str:
        patterns = [
            r'<h1\b[^>]*id="page-title"[^>]*>(.*?)</h1>',
            r'<h1\b[^>]*>(.*?)</h1>',
            r'<title\b[^>]*>(.*?)</title>',
        ]

        for pattern in patterns:
            match = re.search(pattern, html, flags=re.IGNORECASE | re.DOTALL)
            if match:
                title = re.sub(r'<[^>]+>', '', match.group(1))
                title = html_lib.unescape(title).strip()
                if ' - Coinbase Developer Documentation' in title:
                    title = title.split(' - Coinbase Developer Documentation', 1)[0].strip()
                if title:
                    return title

        return "Untitled"

    def _extract_endpoint(self, markdown: str) -> Optional[str]:
        method_match = re.search(r'curl\s+--request\s+(GET|POST|PUT|DELETE|PATCH)', markdown)
        url_match = re.search(r'--url\s+(https://api\.coinbase\.com/[^\s\\]+)', markdown)
        if method_match and url_match:
            return f"{method_match.group(1)} {url_match.group(1)}"
        return None

    def _remove_operation_card_noise(self, markdown: str) -> str:
        """移除 Mintlify API operation 卡片拆散出来的 METHOD / path 片段。"""
        return re.sub(
            r'(?ms)\n\s*(GET|POST|PUT|DELETE|PATCH)\s*\n\s*/\s*\n\s*api\s*\n.*?(\n\s+curl\s+--request)',
            r'\2',
            markdown,
            count=1
        )

    def _detect_api_type(self, url: str, title: str) -> str:
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'websocket' in title_lower:
            return 'WebSocket'
        if '/api-reference/advanced-trade-api/rest-api/' in url_lower:
            if 'product' in url_lower or 'market' in title_lower:
                return 'Market Data'
            if 'order' in url_lower or 'convert' in url_lower:
                return 'Trading'
            if 'account' in url_lower or 'portfolio' in url_lower:
                return 'Account'
            return 'REST'
        if '/guides/' in url_lower or url_lower.endswith('/overview') or url_lower.endswith('/faq'):
            return 'Guide'
        if 'product' in url_lower or 'market' in title_lower:
            return 'Market Data'
        if 'order' in url_lower or 'trade' in title_lower:
            return 'Trading'
        if 'account' in url_lower or 'portfolio' in url_lower:
            return 'Account'
        return 'REST'

    def _normalize_url(self, url: str) -> str:
        return (url or '').split('#')[0].rstrip('/')

    def _in_scope(self, url: str) -> bool:
        return any(url == prefix or url.startswith(prefix.rstrip('/') + '/') for prefix in self.scope_prefixes)

    def _is_asset_url(self, url: str) -> bool:
        path = urlparse(url).path.lower()
        return path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.ico', '.yaml', '.yml'))

    def _is_bad_page(self, html: str) -> bool:
        text = (html or '').lower()
        markers = [
            'one more step',
            'enable javascript and cookies to continue',
            'checking if the site connection is secure',
            'cf-chl',
            'cloudflare ray id',
        ]
        return any(marker in text for marker in markers)
