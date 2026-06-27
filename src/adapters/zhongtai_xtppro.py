#!/usr/bin/env python3
"""Zhongtai XTP Pro VitePress document adapter."""
from __future__ import annotations

import re
from typing import Any
from urllib.parse import quote, unquote, urlparse

from src.adapters.base import DocumentPage, ProductAdapter, register_adapter
from src.utils.browser import BrowserManager
from src.utils.path_generator import sanitize_path_component, slugify_title


@register_adapter("zhongtai_xtppro")
class ZhongtaiXtpProAdapter(ProductAdapter):
    def __init__(self, config: dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"crawl-{self.product_id}")

    def discover(self) -> list[str]:
        source = self.config.get("source", {})
        preload_url = source.get("preload_url") or source.get("home_url")
        if not self.browser.open(preload_url, wait=2):
            raise RuntimeError(f"Unable to open XTP Pro preload page: {preload_url}")
        self.browser.wait_for_element(source.get("content_selector", "main .vp-doc"), timeout=20)

        sidebar_links = self.browser.eval_js(
            """
            (() => {
                const site = window.__VP_SITE_DATA__ || {};
                const sidebar = site.themeConfig?.sidebar?.['/API4/'] || [];
                const links = [];
                const walk = (items) => (items || []).forEach(item => {
                    if (item.link) links.push(item.link);
                    if (item.items) walk(item.items);
                });
                walk(sidebar);
                return links;
            })()
            """
        ) or []
        routes = [self._sidebar_link_to_route(link) for link in sidebar_links]

        if not routes:
            asset_urls = self.browser.eval_js(
                """
                Array.from(document.querySelectorAll('link[href*="/xtp-pro/assets/"][href*=".md."]'))
                    .map(link => link.href)
                """
            ) or []
            routes = [self._asset_url_to_route(url) for url in asset_urls if self._asset_url_to_route(url)]

        seen = set()
        result = []
        for url in routes:
            if url and url not in seen:
                seen.add(url)
                result.append(url)
        return result

    def extract(self, source: str) -> DocumentPage:
        cfg_source = self.config.get("source", {})
        selector = cfg_source.get("content_selector", "main .vp-doc")
        if not self.browser.open(source, wait=1.5):
            raise RuntimeError(f"Unable to open XTP Pro page: {source}")
        self.browser.wait_for_element(selector, timeout=20)
        payload = self.browser.eval_js(
            f"""
            (() => {{
                const root = document.querySelector({selector!r});
                const titleEl = root?.querySelector('h1, h2, p strong') || document.querySelector('h1');
                return {{
                    title: (titleEl?.textContent || document.title || '').trim(),
                    html: root ? root.innerHTML : '',
                    updated: document.querySelector('time[datetime]')?.getAttribute('datetime')?.slice(0, 10) ||
                        document.querySelector('meta[name="last-updated"]')?.content || ''
                }};
            }})()
            """
        ) or {}
        title = payload.get("title") or self._title_from_url(source)
        html = payload.get("html") or ""
        markdown = self.markdown.html_to_markdown(html)
        metadata = self.metadata_defaults()
        metadata.update({
            "id": f"{self.product_id}-{slugify_title(title)}",
            "title": title,
            "api_type": self._infer_api_type(title, source),
            "source_url": source,
            "page_url": cfg_source.get("home_url", ""),
            "updated_at": payload.get("updated") or "",
        })
        return DocumentPage(title=title, content=markdown, metadata=metadata, relative_path=self._route_to_relative_path(source), source_url=source)

    def _sidebar_link_to_route(self, link: str) -> str:
        source = self.config.get("source", {})
        base_url = source.get("base_url", "https://xtp.zts.com.cn/xtp-pro/").rstrip("/") + "/"
        route = str(link or "").strip()
        if not route:
            return ""
        if route.startswith("/xtp-pro/"):
            route = route[len("/xtp-pro/") :]
        elif route.startswith("/"):
            route = route[1:]
        if route.endswith(".md"):
            route = route[:-3]
        if not route.endswith(".html"):
            route += ".html"
        encoded = "/".join(quote(part) for part in route.split("/"))
        return base_url + encoded

    def _asset_url_to_route(self, asset_url: str) -> str:
        parsed = urlparse(asset_url)
        asset_name = unquote(parsed.path.rsplit("/", 1)[-1])
        match = re.match(r"(.+)\.md\.[^.]+(?:\.lean)?\.js$", asset_name)
        if not match:
            return ""
        route_path = match.group(1).replace("_", "/") + ".html"
        encoded = "/".join(quote(part) for part in route_path.split("/"))
        return f"{parsed.scheme}://{parsed.netloc}/xtp-pro/{encoded}"

    def _route_to_relative_path(self, url: str) -> str:
        path = unquote(urlparse(url).path)
        prefix = "/xtp-pro/"
        if path.startswith(prefix):
            path = path[len(prefix):]
        if not path or path == "/":
            return "index.md"
        if path.endswith(".html"):
            path = path[:-5] + ".md"
        parts = [sanitize_path_component(part) for part in path.split("/") if part]
        return "/".join(parts) or "index.md"

    def _title_from_url(self, url: str) -> str:
        path = unquote(urlparse(url).path).rstrip("/")
        name = path.rsplit("/", 1)[-1].replace(".html", "") or "XTP Pro"
        return name

    def _infer_api_type(self, title: str, url: str) -> str:
        text = f"{title} {unquote(url)}".lower()
        if "错误" in text or "error" in text:
            return "error_code"
        if "quickstart" in text or "指南" in text or "常见问题" in text or "faq" in text:
            return "guide"
        if "变化" in text or "迁移" in text:
            return "migration"
        if "quote" in text or "行情" in text or "l2" in text:
            return "market_data"
        if "trader" in text or "交易" in text or "报单" in text or "订单" in text or "资金" in text:
            return "trade"
        if "api" in text or "接口" in text:
            return "reference"
        return "guide"
