#!/usr/bin/env python3
"""Crawl a docs site through its llms.txt index (GitBook, Mintlify, ...).

Such sites list every page in /llms.txt and serve each page as Markdown at `<page>.md`, so no
browser is needed. Nested indexes (links to other `.txt` files on the same host) are followed.
Optional machine-readable specs (OpenAPI / AsyncAPI `.json` / `.yaml`) are stored as a fenced
code block so they stay searchable next to the prose pages.

Config (`source` in config/products/<id>.yaml):

    source:
      type: llms_txt
      llms_txt: https://docs.example.com/llms.txt   # or, when llms.txt is only a short guide:
      sitemap: https://docs.example.com/sitemap.xml # every <loc> is a page; "<page>.md" is fetched
      base_url: https://docs.example.com/          # file paths are relative to this
      include_prefixes: ["for-developers/"]        # optional; paths relative to base_url
      exclude_prefixes: []                         # optional
      include_specs: true                          # optional; also keep .json/.yaml specs
      concurrency: 4
      max_failure_ratio: 0.02                      # more failures than this -> keep old docs
"""
from __future__ import annotations

import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from urllib.parse import urljoin, urlparse

from src.adapters.base import DocumentPage, ProductAdapter, register_adapter

USER_AGENT = "marketdata-api-doc-crawler/1.0"
SPEC_SUFFIXES = (".json", ".yaml", ".yml")
LINK = re.compile(r"\]\(([^)\s]+)\)")
LOC = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")
# GitBook / Mintlify insert a quoted note pointing back at llms.txt near the top; it is not part of the page.
QUOTE_BLOCK = re.compile(r"(?:^>[^\n]*\n?)+", re.M)


def strip_index_note(body: str) -> str:
    for block in QUOTE_BLOCK.finditer(body[:2000]):
        if "llms.txt" in block.group(0):
            return (body[:block.start()] + body[block.end():]).strip()
    return body.strip()


def fetch(url: str, timeout: int = 30, retries: int = 3) -> str:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise
            last = exc
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
        time.sleep(1 + attempt * 2)
    raise RuntimeError(f"fetch failed after {retries} tries: {url}: {last}")


def normalize(url: str, base: str) -> str:
    url = re.sub(r"^(https?):/(?!/)", r"\1://", url)  # "https:/host" typos in some indexes
    return urljoin(base, url).split("#")[0]


@register_adapter("llms_txt")
class LlmsTxtAdapter(ProductAdapter):
    """Product adapter for sites that publish llms.txt and per-page Markdown."""

    def __init__(self, config: dict[str, Any]):
        super().__init__(config)
        source = config.get("source", {})
        self.sitemap_url = source.get("sitemap")
        self.index_url = source.get("llms_txt") or self.sitemap_url
        if not self.index_url:
            raise ValueError(f"{self.product_id}: source needs llms_txt or sitemap")
        self.base_url = source.get("base_url") or self.index_url.rsplit("/", 1)[0] + "/"
        self.include = list(source.get("include_prefixes") or [])
        self.exclude = list(source.get("exclude_prefixes") or [])
        self.include_specs = bool(source.get("include_specs", False))
        self.concurrency = max(1, int(source.get("concurrency", 4)))
        self.max_failure_ratio = float(source.get("max_failure_ratio", 0.02))

    # ---- discovery -------------------------------------------------------------------------

    def _relative(self, url: str) -> str | None:
        """Path of url relative to base_url, or None when it is outside base_url."""
        if not url.startswith(self.base_url):
            return None
        return url[len(self.base_url):]

    def _wanted(self, rel: str) -> bool:
        if self.include and not any(rel.startswith(p) for p in self.include):
            return False
        return not any(rel.startswith(p) for p in self.exclude)

    def _discover_sitemap(self) -> list[str]:
        pages: dict[str, None] = {}
        queue, seen = [self.sitemap_url], set()
        while queue:
            sitemap = queue.pop(0)
            if sitemap in seen:
                continue
            seen.add(sitemap)
            for url in LOC.findall(fetch(sitemap)):
                if urlparse(url).path.endswith(".xml"):  # sitemap index -> child sitemaps
                    queue.append(url)
                    continue
                rel = self._relative(url)
                if rel is not None and self._wanted(rel):
                    pages[url.rstrip("/") + ".md"] = None
        if not pages:
            raise RuntimeError(f"{self.product_id}: sitemap listed no pages: {self.sitemap_url}")
        return list(pages)

    def discover(self) -> list[str]:
        if self.sitemap_url:
            return self._discover_sitemap()
        host = urlparse(self.index_url).netloc
        seen_index: set[str] = set()
        pages: dict[str, None] = {}  # ordered set
        queue = [self.index_url]
        while queue:
            index = queue.pop(0)
            if index in seen_index:
                continue
            seen_index.add(index)
            for raw in LINK.findall(fetch(index)):
                url = normalize(raw, index)
                path = urlparse(url).path
                if path.endswith(".txt") and urlparse(url).netloc == host:
                    queue.append(url)
                    continue
                is_page = path.endswith(".md")
                is_spec = self.include_specs and path.endswith(SPEC_SUFFIXES)
                if not (is_page or is_spec):
                    continue
                rel = self._relative(url)
                if is_spec and rel is None:
                    rel = f"_external/{urlparse(url).netloc}{path}"  # spec hosted elsewhere
                if rel is None or (not is_spec and not self._wanted(rel)):
                    continue
                pages[url] = None
        if not pages:
            raise RuntimeError(f"{self.product_id}: llms.txt listed no pages: {self.index_url}")
        return list(pages)

    # ---- extraction ------------------------------------------------------------------------

    def _relative_path(self, url: str) -> str:
        rel = self._relative(url)
        if rel is None:
            parsed = urlparse(url)
            rel = f"_external/{parsed.netloc}{parsed.path}"
        rel = rel.strip("/") or "index.md"
        if rel.endswith(SPEC_SUFFIXES):
            return f"_specs/{rel.replace('/', '__')}.md"
        return rel if rel.endswith(".md") else f"{rel}.md"

    def extract(self, source: str) -> DocumentPage:
        text = fetch(source)
        path = urlparse(source).path
        metadata = self.metadata_defaults()
        metadata["source_url"] = source if path.endswith(SPEC_SUFFIXES) else source.removesuffix(".md")
        if path.endswith(SPEC_SUFFIXES):
            lang = "json" if path.endswith(".json") else "yaml"
            title = path.rsplit("/", 1)[-1]
            metadata["api_type"] = "spec"
            body = f"Source: {source}\n\n```{lang}\n{text.rstrip()}\n```"
            return DocumentPage(title=title, content=body, metadata=metadata,
                                relative_path=self._relative_path(source), source_url=source)
        body = strip_index_note(text.lstrip("﻿"))
        match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
        title = match.group(1) if match else path.rsplit("/", 1)[-1].removesuffix(".md")
        if len(body) < 40:
            raise RuntimeError(f"page is empty: {source}")
        return DocumentPage(title=title, content=body, metadata=metadata,
                            relative_path=self._relative_path(source), source_url=source.removesuffix(".md"))

    def crawl(self, project_root, limit: int | None = None):
        sources = self.discover()
        if limit is not None:
            sources = sources[:limit]
        failures: list[str] = []

        def one(url: str) -> DocumentPage | None:
            try:
                return self.extract(url)
            except Exception as exc:  # noqa: BLE001 - counted and reported below
                failures.append(f"{url}: {exc}")
                return None

        with ThreadPoolExecutor(max_workers=self.concurrency) as pool:
            pages = [p for p in pool.map(one, sources) if p is not None]
        for line in failures:
            print(f"WARN {self.product_id}: {line}")
        if sources and len(failures) / len(sources) > self.max_failure_ratio:
            raise RuntimeError(f"{self.product_id}: {len(failures)}/{len(sources)} pages failed; keeping old docs")

        return self.write_pages(project_root, pages)
