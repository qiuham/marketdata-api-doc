#!/usr/bin/env python3
"""
Gate.io developer docs adapter.
"""
import os
import re
import time
import itertools
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List
from urllib.parse import urlparse

from loguru import logger as log

from .base import DocumentPage, ExchangeAdapter, register_adapter
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


class PageNotFound(Exception):
    """网站上没有这一页（404）"""


@register_adapter('gateio')
class GateioAdapter(ExchangeAdapter):
    """Gate.io 文档适配器（浏览器渲染，侧边栏全量发现）"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()
        crawler_config = self.config.get('crawler', {})
        self.allowed_languages = set(crawler_config.get('allowed_languages', ['zh_CN', 'en']))
        self.base_prefix = crawler_config.get('base_prefix', 'https://www.gate.com/docs/developers/')

    def discover_pages(self) -> List[str]:
        """从中英文入口、顶部产品菜单和侧边栏发现所有 Gate developer 文档页。"""
        start_urls = [self._normalize_url(url) for url in self.config['crawler']['start_urls']]
        max_pages = self.config.get('crawler', {}).get('max_discovery_pages', 500)

        discovered = set()

        for start_url in start_urls:
            if not self.browser.open(start_url, wait=4):
                log.warning(f"无法打开入口: {start_url}")
                continue

            entry_links = self._collect_page_links(click_top_nav=True)
            log.info(f"入口发现: {start_url} -> {len(entry_links)} 个链接")
            discovered.update(entry_links)
            discovered.add(start_url)

        if len(discovered) >= max_pages:
            log.warning(f"达到最大页面发现数量: {max_pages}")

        # 中英文页一一对应，但侧边栏不一定都链到（例如 announcements/ws/en 只有中文侧边栏链到中文版）。
        # 找到一种语言就补上另一种；补出来的网站上可能没有，爬的时候遇到 404 就跳过。
        self.mirror_only = set()
        for url in list(discovered):
            for a, b in (('/en', '/zh_CN'), ('/zh_CN', '/en')):
                if url.endswith(a) or f'{a}/' in url:
                    twin = url[:-len(a)] + b if url.endswith(a) else url.replace(f'{a}/', f'{b}/', 1)
                    if twin not in discovered:
                        discovered.add(twin)
                        self.mirror_only.add(twin)

        pages = sorted(url for url in discovered if self._in_scope(url))[:max_pages]
        log.success(f"Gate.io 共发现 {len(pages)} 个页面（其中按另一语言补的 {len(self.mirror_only)} 个）")
        return pages

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面正文。"""
        url = self._normalize_url(url)
        if not skip_open:
            self.browser.open(url, wait=2)

        if self._is_bad_current_page():
            raise RuntimeError(f"检测到坏页/拒绝访问页: {url}")

        title = self.browser.eval_js(r'''
        (function() {
            const h1 = document.querySelector('main h1, .content__default h1');
            if (h1) return h1.textContent.replace(/^#\s*/, '').trim();
            return document.title.split('|')[0].trim();
        })()
        ''') or "Untitled"

        selector = self.config.get('crawler', {}).get('selectors', {}).get(
            'main_content',
            'main .content__default, main'
        )
        html = self.browser.eval_js(f'''
        (function() {{
            const main = document.querySelector({selector!r});
            if (!main) return null;
            const clone = main.cloneNode(true);

            clone.querySelectorAll('nav, header, footer, button, svg, .header-anchor, .pageHeader, .sidebar, .menu').forEach(el => el.remove());
            clone.querySelectorAll('a').forEach(a => {{
                if ((a.textContent || '').trim() === '#') a.remove();
            }});
            return clone.innerHTML;
        }})()
        ''')

        if not html:
            raise RuntimeError(f"未找到正文: {url}")

        markdown = self.md_processor.html_to_markdown(html)
        markdown = self._clean_markdown(markdown)

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
            raw_html=html
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
        """执行 Gate.io 爬取流程。"""
        from pathlib import Path
        from ..utils.indexer import DocumentIndexer
        from ..utils.path_generator import safe_output_path, url_to_filepath
        from ..utils.readme_updater import ReadmeUpdater

        if languages:
            self.allowed_languages = set(languages)

        urls = self.discover_pages()
        if not urls:
            log.error("未发现任何 Gate.io 页面")
            return

        if limit and limit > 0:
            urls = urls[:limit]
            log.warning(f"限制模式：只爬取前 {len(urls)} 页")

        output_dir = self.get_output_path()
        os.makedirs(output_dir, exist_ok=True)
        self.written = set()  # 这次写到的文件
        self.skipped = set()  # 按另一语言补出来、网站上没有的页

        success_count = 0
        if concurrency <= 1:
            for i, url in enumerate(urls, 1):
                if self._crawl_one(i, len(urls), url, output_dir):
                    success_count += 1
                time.sleep(0.2)
        else:
            workers = min(concurrency, len(urls))
            log.info(f"使用 {workers} 个浏览器 session 并发提取 Gate.io 页面")

            local = threading.local()
            counter = itertools.count(1)
            counter_lock = threading.Lock()

            def get_worker_adapter() -> 'GateioAdapter':
                if not hasattr(local, 'adapter'):
                    with counter_lock:
                        worker_id = next(counter)
                    adapter = GateioAdapter(self.config)
                    adapter.written = self.written  # 共用同一个集合（set.add 线程安全）
                    adapter.skipped = self.skipped
                    adapter.mirror_only = self.mirror_only
                    adapter.browser = BrowserManager(f"{self.name}-crawler-w{worker_id}")
                    local.adapter = adapter
                return local.adapter

            def run_one(item):
                i, url = item
                return get_worker_adapter()._crawl_one(i, len(urls), url, output_dir)

            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = [executor.submit(run_one, item) for item in enumerate(urls, 1)]
                for future in as_completed(futures):
                    if future.result():
                        success_count += 1

        log.success(f"完成! 成功: {success_count}/{len(urls)}")
        if success_count < len(urls) * 0.9:
            # 一页没抓到也报“成功”的话，旧文件会被当成新结果。抛出去由主程序把这一家退回上一次提交。
            raise RuntimeError(f"Gate.io 只成功 {success_count}/{len(urls)} 页")
        if not limit:
            # 网站删掉或改名的页不能一直留在库里；网站上还在、只是这次没抓成功的页保留旧文件
            expected = {os.path.abspath(safe_output_path(output_dir, url_to_filepath(u, self.base_prefix)))
                        for u in urls if u not in self.skipped}
            for path in Path(output_dir).rglob('*.md'):
                if os.path.abspath(path) not in expected:
                    path.unlink()
                    log.info(f"删除旧页: {path}")

        project_root = Path(__file__).parent.parent.parent
        indexer = DocumentIndexer(output_dir)
        index_path = indexer.generate_index(str(project_root / "index"))
        log.success(f"索引已生成: {index_path}")

        updater = ReadmeUpdater(str(project_root))
        readme_path = updater.update_exchange_table()
        log.success(f"README 已更新: {readme_path}")

    def _crawl_one(self, index: int, total: int, url: str, output_dir: str) -> bool:
        from ..utils.path_generator import safe_output_path, url_to_filepath

        last_exc = None
        for attempt in range(3):  # Akamai 偶尔给一次拒绝页，隔几秒再试
            try:
                page = self.extract_content(url)
                filepath = url_to_filepath(url, self.base_prefix)
                output_path = safe_output_path(output_dir, filepath)
                self.save_page(page, output_path)
                self.written.add(os.path.abspath(output_path))
                log.success(f"[{index}/{total}] {page.title}")
                return True
            except PageNotFound:
                if url in getattr(self, 'mirror_only', set()):
                    self.skipped.add(url)
                    log.info(f"[{index}/{total}] 另一语言没有这一页，跳过: {url}")
                    return True
                last_exc = RuntimeError("404 Not Found")
                break
            except Exception as exc:
                last_exc = exc
                time.sleep(5 * (attempt + 1))
        log.error(f"[{index}/{total}] {url} - {last_exc}")
        return False

    def _collect_page_links(self, click_top_nav: bool = False) -> List[str]:
        """收集当前页面侧边栏链接；必要时点击顶部产品菜单展开 REST/WS 入口。"""
        links = set(self._eval_link_collection() or [])

        if click_top_nav:
            nav_names = self.browser.eval_js(r'''
            Array.from(document.querySelectorAll('.pageNav .navItem'))
                .map(el => el.getAttribute('data-name'))
                .filter(Boolean)
            ''') or []

            for name in nav_names:
                if name == '🔥 Agent':
                    continue

                selector = f'.pageNav .navItem[data-name="{name}"]'
                self.browser._run_command(['click', selector], timeout=10)
                time.sleep(0.5)
                links.update(self._eval_link_collection() or [])

        return sorted(self._normalize_url(link) for link in links if self._in_scope(link))

    def _eval_link_collection(self) -> List[str]:
        return self.browser.eval_js(r'''
        (function() {
            const selectors = [
                '.sidebar a[href]',
                'a.sidebar-link[href]',
                'a.category__link[href]',
                '.pageHeader a[href]',
                '.pageHeader__toolbar a[href]'
            ].join(',');

            const links = Array.from(document.querySelectorAll(selectors))
                .map(a => a.href || '')
                .filter(Boolean)
                .map(href => href.split('#')[0].replace(/\/$/, ''))
                .filter(href => href.startsWith('https://www.gate.com/docs/developers/'));

            return Array.from(new Set(links)).sort();
        })()
        ''') or []

    def _is_bad_current_page(self) -> bool:
        title = (self.browser.eval_js("document.title") or "").lower()
        if 'access denied' in title:
            return True
        if title.startswith('404'):
            raise PageNotFound()
        text = self.browser.eval_js("document.body ? document.body.innerText : ''") or ""
        if len(text) >= 2000:
            # 真正的拒绝页只有两百多字；长的接口文档正文里本来就可能出现 "access denied"（错误码说明）
            return False
        low = text.lower()
        bad_markers = [
            'access denied',
            "you don't have permission",
            'one more step',
            'enable javascript and cookies',
            'cloudflare ray id',
        ]
        return any(marker in low for marker in bad_markers)

    def _clean_markdown(self, markdown: str) -> str:
        markdown = markdown.replace('\u200b', '')
        markdown = re.sub(r'\(opens new window\)', '', markdown, flags=re.IGNORECASE)
        markdown = re.sub(r'^\s*#\s*$', '', markdown, flags=re.MULTILINE)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        return markdown.strip()

    def _detect_api_type(self, url: str, title: str) -> str:
        value = f"{url} {title}".lower()
        if '/ws/' in value or 'websocket' in value:
            return 'WebSocket'
        if any(part in value for part in ['/spot', '/futures', '/delivery', '/options', '/tradfi', '/alpha', '/crossex']):
            return 'Trading'
        if any(part in value for part in ['/wallet', '/withdrawal', '/account', '/subaccount', '/unified']):
            return 'Account'
        if any(part in value for part in ['/earn', '/rebate', '/loan']):
            return 'Earn'
        return 'REST'

    def _normalize_url(self, url: str) -> str:
        return (url or '').split('#')[0].rstrip('/')

    def _in_scope(self, url: str) -> bool:
        normalized = self._normalize_url(url)
        parsed = urlparse(normalized)
        if parsed.scheme != 'https' or parsed.netloc != 'www.gate.com':
            return False
        if not parsed.path.startswith('/docs/developers/'):
            return False
        if self._is_asset_path(parsed.path):
            return False

        parts = [part for part in parsed.path.split('/') if part]
        return any(lang in parts for lang in self.allowed_languages)

    def _is_asset_path(self, path: str) -> bool:
        return path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.ico', '.pdf'))
