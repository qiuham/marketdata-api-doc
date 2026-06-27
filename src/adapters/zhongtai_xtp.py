#!/usr/bin/env python3
"""Zhongtai XTP 3.0 document adapter."""
from __future__ import annotations

import json
import re
import urllib.request
from html import unescape
from typing import Any

from src.adapters.base import DocumentPage, ProductAdapter, register_adapter
from src.utils.path_generator import slugify_title

_MENU_SLUGS = {
    "XTP API简介": "overview",
    "XTP API 快速入门": "quickstart",
    "详细接口使用说明": "api-reference",
    "范例和教程": "examples",
    "使用建议": "guides",
    "其他帮助文档": "help",
}


@register_adapter("zhongtai_xtp")
class ZhongtaiXtpAdapter(ProductAdapter):
    def discover(self) -> list[dict[str, Any]]:
        source = self.config.get("source", {})
        data = self._get_json(source["menu_url"])
        roots = data.get("result") or []
        docs: list[dict[str, Any]] = []
        for menu in roots:
            self._collect_menu_docs(menu, docs)
        return docs

    def extract(self, source: dict[str, Any]) -> DocumentPage:
        cfg_source = self.config.get("source", {})
        doc_id = str(source["id"])
        content_url = cfg_source["content_url"].format(doc_id=doc_id)
        data = self._get_json(content_url)
        html = data.get("message") if data.get("success") else ""
        if not html or html == "操作成功！":
            html = source.get("html") or ""

        title = source.get("title") or source.get("name") or doc_id
        menu_name = source.get("menu_name", "")
        markdown = self._mixed_html_to_markdown(html)
        metadata = self.metadata_defaults()
        metadata.update({
            "id": f"{self.product_id}-{doc_id}",
            "title": title,
            "doc_id": doc_id,
            "doc_category": menu_name,
            "api_type": self._infer_api_type(title, menu_name),
            "source_url": content_url,
            "page_url": cfg_source.get("page_url", ""),
            "updated_at": self._format_time(source.get("update_time") or source.get("create_time") or ""),
        })
        relative_path = f"{_MENU_SLUGS.get(menu_name, slugify_title(menu_name))}/{slugify_title(title)}.md"
        return DocumentPage(title=title, content=markdown, metadata=metadata, relative_path=relative_path, source_url=content_url)

    def _mixed_html_to_markdown(self, html: str) -> str:
        """XTP 3.0 stores Markdown text with a few HTML heading/br tags."""
        text = html or ""
        for level in range(1, 7):
            pattern = rf"<h{level}[^>]*>(.*?)</h{level}>"
            text = re.sub(pattern, lambda m: f"{'#' * level} {self._strip_tags(m.group(1)).strip()}\n\n", text, flags=re.I | re.S)
        text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
        text = re.sub(r"</p>", "\n\n", text, flags=re.I)
        text = re.sub(r"<[^>]+>", "", text)
        text = unescape(text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{4,}", "\n\n\n", text)
        return text.strip() + "\n"

    def _strip_tags(self, text: str) -> str:
        return re.sub(r"<[^>]+>", "", text or "")

    def _collect_menu_docs(self, menu: dict[str, Any], docs: list[dict[str, Any]]) -> None:
        menu_name = menu.get("departName") or menu.get("name") or "docs"
        for doc in menu.get("docList") or []:
            docs.append({
                "id": str(doc.get("id", "")),
                "name": doc.get("name", ""),
                "title": doc.get("subName") or re.sub(r"\.md$", "", doc.get("name", "")),
                "menu_name": menu_name,
                "file_path": doc.get("filePath", ""),
                "html": doc.get("byx2", ""),
                "create_time": doc.get("createTime", ""),
                "update_time": doc.get("updateTime") or doc.get("createTime", ""),
            })
        for child in menu.get("children") or []:
            self._collect_menu_docs(child, docs)

    def _get_json(self, url: str) -> dict[str, Any]:
        source = self.config.get("source", {})
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": source.get("authorization", "bearernull"),
            "Referer": source.get("referer", source.get("page_url", "")),
            "User-Agent": "Mozilla/5.0 marketdata-api-doc crawler",
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))

    def _infer_api_type(self, title: str, menu_name: str) -> str:
        text = f"{title} {menu_name}".lower()
        if "错误" in text or "error" in text:
            return "error_code"
        if "版本" in text or "更新" in text:
            return "changelog"
        if "quickstart" in text or "快速" in text or "指南" in text:
            return "guide"
        if "quote" in text or "行情" in text or "逐笔" in text or "l2" in text:
            return "market_data"
        if "trader" in text or "交易" in text or "报单" in text or "订单" in text or "资金" in text:
            return "trade"
        if "详细接口" in menu_name or "api" in text:
            return "reference"
        return "guide"

    def _format_time(self, value: str) -> str:
        return value.split()[0] if value else ""
