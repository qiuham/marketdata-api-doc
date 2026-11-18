#!/usr/bin/env python3
"""
Binance 适配器（2026-11 改版后的新文档站 https://developers.binance.com/en/docs）

新站分两部分，取法不同：
1. 文档页（/en/docs/products/...、/en/docs/sdks-tools/... 等）：
   /en/docs/llms.txt 列出全部文档页，每页加 .md 就是原始 Markdown，直接 HTTP 取，不用浏览器。
   中文页把 /en/ 换成 /zh-CN/。英文在前、中文在后，合成一篇双语文档。
2. API 参考（/en/docs/catalog/<产品>/api/<rest-api|ws-api|ws-streams>）：
   每个 API 一份 OpenAPI schema.yaml，英文、中文都在里面。schema 和目录页有 AWS WAF 验证，
   只能在浏览器里取：浏览器打开目录页拿到全部 API，再打开每个 API 页，找到 schema.yaml 的链接，
   用页面里的 fetch 取回文本，转成一篇 Markdown。
   例如现货行情推送频道列表（trade、aggTrade、depth 等）在
   catalog/core-trading-spot-trading/api/ws-streams.md。

旧站地址（/docs/binance-spot-api-docs/... 等）现在都跳到新站，旧文档目录整个不再使用。
"""
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Tuple

import yaml
from loguru import logger as log

from .base import DocumentPage, ExchangeAdapter, register_adapter
from ..utils.browser import BrowserManager
from ..utils.http import fetch_text, looks_like_html, strip_llm_preamble
from ..utils.markdown import MarkdownProcessor
from ..utils.openapi_md import OpenApiRenderer
from ..utils.path_generator import safe_output_path, url_to_filepath

_DOC_LINK_RE = re.compile(r'^- \[[^\]]*\]\((/[^)\s]+\.md)\)', re.MULTILINE)
_API_PATH_RE = re.compile(r'/docs/catalog/[^/#?]+/api/[^/#?]+$')


@register_adapter('binance')
class BinanceAdapter(ExchangeAdapter):
    """Binance 新文档站适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.md_processor = MarkdownProcessor()
        crawler = self.config.get('crawler', {})
        self.site = crawler.get('site', 'https://developers.binance.com').rstrip('/')
        self.primary_prefix = crawler.get('primary_prefix', '/en/docs/')
        self.secondary_prefixes = crawler.get('secondary_prefixes', ['/zh-CN/docs/'])
        self.llms_index = crawler.get('llms_index', '/en/docs/llms.txt')
        self.catalog_url = crawler.get('catalog_url', '/en/docs/catalog')
        self.schema_version = crawler.get('schema_version', '1.0.0')
        # 每次请求前等这么多秒；太快会被限流（HTTP 429），而且会封一阵子
        self.request_delay = float(crawler.get('request_delay', 0.5))
        self.browser: Optional[BrowserManager] = None

    # ------------------------------------------------------------------
    # 文档页
    # ------------------------------------------------------------------
    def discover_pages(self) -> List[str]:
        """返回文档页的相对路径（相对 /en/docs/，不带 .md），例如 products/spot/web-socket-streams。"""
        text = fetch_text(self.site + self.llms_index)
        if not text:
            raise RuntimeError(f"无法读取文档索引: {self.site + self.llms_index}")
        # 只取 “## Documentation” 一节；“## API Reference” 一节只有接口摘要，没有链接
        doc_part = text.split('\n## API Reference', 1)[0]
        pages: List[str] = []
        for link in _DOC_LINK_RE.findall(doc_part):
            if not link.startswith(self.primary_prefix):
                continue
            rel = link[len(self.primary_prefix):-len('.md')]
            if rel and rel not in pages:
                pages.append(rel)
        log.success(f"文档页 {len(pages)} 个")
        return pages

    def _fetch_doc(self, rel: str) -> Tuple[str, Optional[DocumentPage], str]:
        parts: List[str] = []
        title = ''
        for i, prefix in enumerate([self.primary_prefix] + list(self.secondary_prefixes)):
            time.sleep(self.request_delay)
            text = fetch_text(f'{self.site}{prefix}{rel}.md', accept='text/markdown')
            if not text or looks_like_html(text):
                if i == 0:
                    return rel, None, '读不到英文页'
                continue
            body = strip_llm_preamble(text)
            if i == 0:
                match = re.search(r'^#\s+(.+?)\s*$', body, flags=re.MULTILINE)
                # 英文的一级标题留在正文里，写文件时 create_document 会去掉它、换成 title
                title = match.group(1).strip() if match else rel.rsplit('/', 1)[-1]
            parts.append(body.strip())
        url = f'{self.site}{self.primary_prefix}{rel}'
        page = DocumentPage(
            url=url, title=title, content='\n\n---\n\n'.join(p for p in parts if p),
            metadata={'exchange': self.name, 'source_url': url, 'api_type': self._doc_api_type(rel)},
        )
        return rel, page, ''

    # ------------------------------------------------------------------
    # API 参考
    # ------------------------------------------------------------------
    def discover_apis(self) -> List[str]:
        """返回 API 参考页地址，例如 https://.../en/docs/catalog/core-trading-spot-trading/api/ws-streams"""
        if not self.browser.open(self.site + self.catalog_url, wait=5):
            raise RuntimeError("无法打开 API 目录页")
        links = self.browser.eval_js(
            'Array.from(document.querySelectorAll("a[href]")).map(a => a.href.split("#")[0])') or []
        apis: List[str] = []
        for link in links:
            link = link.rstrip('/')
            if link.startswith(self.site) and _API_PATH_RE.search(link) and link not in apis:
                apis.append(link)
        log.success(f"API 参考 {len(apis)} 个")
        return apis

    def _fetch_api(self, api_url: str) -> DocumentPage:
        # 浏览器已经在本站页面上（过了 WAF 验证），直接用页面里的 fetch 取 schema。
        # 现在所有 API 都是 1.0.0 版；取不到时再打开 API 页找 “Download schema” 链接。
        schema_url = f'{api_url}/{self.schema_version}/schema.yaml'
        text = self._browser_fetch(schema_url)
        if not text:
            self.browser.open(api_url + '/~', wait=5)
            schema_url = self.browser.eval_js(
                '(document.querySelector("a[href$=\\"schema.yaml\\"]") || {}).href || ""') or ''
            text = self._browser_fetch(schema_url) if schema_url else None
        if not text:
            raise RuntimeError(f"取不到 schema: {api_url}")
        spec = yaml.safe_load(text)
        title, body = OpenApiRenderer(spec).render()
        product_type = spec.get('x-product-type') or api_url.rsplit('/', 1)[-1]
        api_type = {'rest-api': 'REST', 'ws-api': 'WebSocket API', 'ws-streams': 'WebSocket Streams'}.get(
            product_type, product_type)
        return DocumentPage(
            url=api_url, title=title, content=f'Schema: {schema_url}\n\n{body}',
            metadata={'exchange': self.name, 'source_url': api_url, 'api_type': api_type},
        )

    def _browser_fetch(self, url: str) -> Optional[str]:
        text = self.browser.eval_js(f'fetch({json.dumps(url)}).then(r => r.ok ? r.text() : "")')
        if not text or looks_like_html(text) or not text.lstrip().startswith('openapi'):
            return None
        return text

    # ------------------------------------------------------------------
    # 主流程
    # ------------------------------------------------------------------
    def extract_content(self, url: str) -> DocumentPage:
        if '/catalog/' in url:
            return self._fetch_api(url)
        _, page, error = self._fetch_doc(url)
        if page is None:
            raise RuntimeError(error)
        return page

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        output_dir = self.get_output_path()
        os.makedirs(output_dir, exist_ok=True)

        pages = self.discover_pages()
        if limit and limit > 0:
            pages = pages[:limit]
        failed: List[str] = []
        written = 0
        with ThreadPoolExecutor(max_workers=max(1, concurrency)) as pool:
            for i, (rel, page, error) in enumerate(pool.map(self._fetch_doc, pages), 1):
                if page is None or len(page.content) < 40:
                    failed.append(f'{rel}: {error or "正文过短"}')
                    log.error(f"[{i}/{len(pages)}] {rel} - {error or '正文过短'}")
                    continue
                self._save(page, f'{rel}.md', output_dir)
                written += 1
        log.success(f"文档页完成: {written}/{len(pages)}")

        self.browser = BrowserManager(f"{self.name}-crawler")
        apis = self.discover_apis()
        if limit and limit > 0:
            apis = apis[:limit]
        api_written = 0
        for i, api_url in enumerate(apis, 1):
            try:
                page = self._fetch_api(api_url)
            except Exception as exc:  # noqa: BLE001 - 一个 API 失败不影响其它
                failed.append(f'{api_url}: {exc}')
                log.error(f"[{i}/{len(apis)}] {api_url} - {exc}")
                continue
            rel = url_to_filepath(api_url, f'{self.site}{self.primary_prefix}')
            self._save(page, rel, output_dir)
            api_written += 1
            log.success(f"[{i}/{len(apis)}] {page.title}")
        log.success(f"API 参考完成: {api_written}/{len(apis)}")

        for item in failed:
            log.warning(f"失败: {item}")
        if written + api_written == 0:
            raise RuntimeError("Binance 一页也没抓到")

    def _save(self, page: DocumentPage, rel: str, output_dir: str) -> None:
        path = safe_output_path(output_dir, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.md_processor.create_document(page.title, page.content, page.metadata))

    @staticmethod
    def _doc_api_type(rel: str) -> str:
        lower = rel.lower()
        if 'websocket' in lower or 'web-socket' in lower or 'stream' in lower:
            return 'WebSocket'
        if '/fix' in lower:
            return 'FIX'
        if 'sbe' in lower:
            return 'SBE'
        if 'changelog' in lower or 'change-log' in lower:
            return 'Changelog'
        return 'Guide'
