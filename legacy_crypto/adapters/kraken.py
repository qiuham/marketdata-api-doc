#!/usr/bin/env python3
"""
Kraken 适配器（2026-11 改版后的 Mintlify 文档站 https://docs.kraken.com/）

旧站 /api/docs/... 的地址现在都跳到新站，例如
/api/docs/fix-api/nos-fix -> /exchange/api-reference/unified-fix/nos。
新站和 Deribit 一样是 Mintlify：每页加 .md 就是原始 Markdown。
页面清单从 sitemap.xml 取，按配置的前缀筛选。取页和存页沿用 Deribit 适配器。
"""
import re
from typing import Any, Dict, List
from urllib.parse import urlparse

from loguru import logger as log

from .base import register_adapter
from .deribit import DeribitAdapter
from ..utils.http import fetch_text

_LOC_RE = re.compile(r'<loc>\s*([^<\s]+)\s*</loc>')


@register_adapter('kraken')
class KrakenAdapter(DeribitAdapter):
    """Kraken Mintlify 文档适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        crawler = self.config.get('crawler', {})
        self.sitemap_url = crawler.get('sitemap_url', 'https://docs.kraken.com/sitemap.xml')
        self.include_prefixes = crawler.get('include_prefixes', [])
        self.exclude_prefixes = crawler.get('exclude_prefixes', [])

    def discover_pages(self) -> List[str]:
        text = fetch_text(self.sitemap_url, accept='application/xml')
        if not text:
            raise RuntimeError(f"无法读取 sitemap: {self.sitemap_url}")
        pages: List[str] = []
        for url in _LOC_RE.findall(text):
            if urlparse(url).netloc != self.host:
                continue
            path = urlparse(url).path.strip('/')
            if not path:
                continue
            if self.include_prefixes and not any(path.startswith(p) for p in self.include_prefixes):
                continue
            if any(path.startswith(p) for p in self.exclude_prefixes):
                continue
            url = url.rstrip('/')
            if url not in pages:
                pages.append(url)
        if len(pages) > self.max_pages:
            log.warning(f"发现页面超过上限 {self.max_pages}，已截断")
            pages = pages[:self.max_pages]
        log.success(f"Kraken 共发现 {len(pages)} 个页面")
        return pages

    def _detect_api_type(self, url: str) -> str:
        path = urlparse(url).path.strip('/')
        if 'websocket' in path or '/unified-ws' in path:
            return 'WebSocket'
        if 'fix' in path or '/drop-copy' in path:
            return 'FIX'
        if '/sbe' in path:
            return 'SBE'
        if path.startswith('api-reference') or '/api-reference/' in path:
            return 'REST'
        return 'Guide'
