#!/usr/bin/env python3
"""
Deribit API 适配器（Mintlify 多页站点，直接取每页的原始 Markdown）

Deribit 文档站 https://docs.deribit.com/ 提供：
- /_llms/production.txt 等索引文件，列出全部页面，并链接到下一级 /_llms/ 子索引；
- 每个页面的原始 Markdown（页面地址后加 .md），内含方法说明和完整的
  OpenAPI / AsyncAPI 片段（参数、返回字段）。
所以这里不用浏览器，也不用解析 HTML。
"""
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.client import IncompleteRead
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from loguru import logger as log

from .base import DocumentPage, ExchangeAdapter, register_adapter
from ..utils.markdown import MarkdownProcessor


@register_adapter('deribit')
class DeribitAdapter(ExchangeAdapter):
    """Deribit Mintlify 文档适配器"""

    USER_AGENT = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/148.0.0.0 Safari/537.36'
    )

    _LINK_RE = re.compile(r'\]\((https?://[^)\s]+|/[^)\s]+)\)')

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.md_processor = MarkdownProcessor()
        crawler_config = self.config.get('crawler', {})
        self.base_prefix = crawler_config.get('base_prefix', 'https://docs.deribit.com/')
        self.index_urls = crawler_config.get('index_urls', [])
        self.index_scope_prefix = crawler_config.get('index_scope_prefix', '')
        self.max_pages = crawler_config.get('max_discovery_pages', 1000)
        self.host = urlparse(self.base_prefix).netloc

    # ------------------------------------------------------------------
    # 发现页面
    # ------------------------------------------------------------------
    def discover_pages(self) -> List[str]:
        """递归读取 /_llms/ 索引，收集全部页面地址（不带 .md 后缀）。"""
        if not self.index_urls:
            raise RuntimeError("配置文件中未定义 crawler.index_urls")

        pages: List[str] = []
        seen_pages = set()
        seen_indexes = set()
        queue = list(self.index_urls)

        while queue:
            index_url = queue.pop(0)
            if index_url in seen_indexes:
                continue
            seen_indexes.add(index_url)

            text = self._fetch_text(index_url, accept='text/plain')
            if not text:
                log.warning(f"无法读取索引: {index_url}")
                continue

            found = 0
            for raw in self._LINK_RE.findall(text):
                link = urljoin(self.base_prefix, raw).split('#')[0]
                parsed = urlparse(link)
                if parsed.netloc != self.host:
                    continue
                if '/_llms/' in parsed.path and parsed.path.endswith('.txt'):
                    if not self.index_scope_prefix or link.startswith(self.index_scope_prefix):
                        queue.append(link)
                    continue
                if not parsed.path.endswith('.md'):
                    continue
                page_url = self._page_url(link)
                if page_url not in seen_pages:
                    seen_pages.add(page_url)
                    pages.append(page_url)
                    found += 1
            log.info(f"索引 {index_url} -> 新页面 {found} 个")

        if len(pages) > self.max_pages:
            log.warning(f"发现页面超过上限 {self.max_pages}，已截断")
            pages = pages[:self.max_pages]

        log.success(f"Deribit 共发现 {len(pages)} 个页面")
        return pages

    # ------------------------------------------------------------------
    # 提取内容
    # ------------------------------------------------------------------
    def extract_content(self, url: str) -> DocumentPage:
        md_url = self._markdown_url(url)
        text = self._fetch_text(md_url, accept='text/markdown')
        if not text:
            raise RuntimeError(f"无法读取页面: {md_url}")
        if text.lstrip().lower().startswith(('<!doctype', '<html')):
            raise RuntimeError(f"返回的是 HTML 而不是 Markdown: {md_url}")

        markdown = self._clean_markdown(text)
        title = self._extract_title(markdown, url)
        if len(markdown) < 80:
            raise RuntimeError(f"正文过短，疑似坏页: {md_url}")

        metadata = {
            'exchange': self.name,
            'source_url': url,
            'api_type': self._detect_api_type(url),
        }
        return DocumentPage(url=url, title=title, content=markdown, metadata=metadata)

    def save_page(self, page: DocumentPage, output_path: str):
        doc_content = self.md_processor.create_document(
            title=page.title,
            content=page.content,
            metadata=page.metadata,
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        return output_path

    # ------------------------------------------------------------------
    # 主流程
    # ------------------------------------------------------------------
    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        urls = self.discover_pages()
        if not urls:
            raise RuntimeError("未发现任何 Deribit 页面")

        if limit and limit > 0:
            urls = urls[:limit]
            log.warning(f"限制模式：只爬取前 {len(urls)} 页")

        output_dir = self.get_output_path()
        os.makedirs(output_dir, exist_ok=True)
        log.info(f"开始提取 Deribit 内容，并发: {concurrency}")

        total = len(urls)
        success_count = 0
        failed: List[str] = []
        if concurrency <= 1:
            for i, url in enumerate(urls, 1):
                if self._crawl_one(i, total, url, output_dir):
                    success_count += 1
                else:
                    failed.append(url)
        else:
            with ThreadPoolExecutor(max_workers=min(concurrency, total)) as executor:
                future_map = {
                    executor.submit(self._crawl_one, i, total, url, output_dir): url
                    for i, url in enumerate(urls, 1)
                }
                for future in as_completed(future_map):
                    if future.result():
                        success_count += 1
                    else:
                        failed.append(future_map[future])

        log.success(f"完成! 成功: {success_count}/{total}")
        for url in sorted(failed):
            log.warning(f"失败页面: {url}")

    def _crawl_one(self, index: int, total: int, url: str, output_dir: str) -> bool:
        from ..utils.path_generator import safe_output_path, url_to_filepath

        try:
            page = self.extract_content(url)
            output_path = safe_output_path(output_dir, url_to_filepath(url, self.base_prefix))
            self.save_page(page, output_path)
            log.success(f"[{index}/{total}] {page.title}")
            return True
        except Exception as exc:
            log.error(f"[{index}/{total}] {url} - {exc}")
            return False

    # ------------------------------------------------------------------
    # 工具函数
    # ------------------------------------------------------------------
    def _page_url(self, md_link: str) -> str:
        """https://docs.deribit.com/a/b.md -> https://docs.deribit.com/a/b；/index.md -> 根地址。"""
        url = md_link[:-3] if md_link.endswith('.md') else md_link
        if url.rstrip('/').endswith('/index') and urlparse(url).path.strip('/') == 'index':
            return self.base_prefix
        return url

    def _markdown_url(self, page_url: str) -> str:
        if page_url.rstrip('/') == self.base_prefix.rstrip('/'):
            return self.base_prefix.rstrip('/') + '/index.md'
        return page_url.rstrip('/') + '.md'

    def _fetch_text(self, url: str, accept: str) -> Optional[str]:
        headers = {
            'User-Agent': self.USER_AGENT,
            'Accept': f'{accept},text/plain;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        last_error = None
        for attempt in range(1, 4):
            try:
                with urlopen(Request(url, headers=headers), timeout=30) as response:
                    charset = response.headers.get_content_charset() or 'utf-8'
                    try:
                        data = response.read()
                    except IncompleteRead as exc:
                        data = exc.partial
                        log.warning(f"响应提前结束，使用已读取内容: {url} ({len(data)} bytes)")
                    return data.decode(charset, errors='replace')
            except HTTPError as exc:
                last_error = exc
                if exc.code == 404:
                    break
                log.warning(f"请求失败({attempt}/3): {url} - {exc}")
            except (URLError, TimeoutError, OSError) as exc:
                last_error = exc
                log.warning(f"请求失败({attempt}/3): {url} - {exc}")
        log.warning(f"请求最终失败: {url} - {last_error}")
        return None

    def _clean_markdown(self, text: str) -> str:
        text = text.replace('\r\n', '\n')
        # 去掉页首给 AI 看的“Documentation Index”提示块
        text = re.sub(
            r'\A\s*> ## Documentation Index\n(?:>.*\n)*\s*',
            '',
            text,
        )
        # 去掉页面自带的 YAML frontmatter（如果有）
        text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.DOTALL)
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        return text.strip()

    def _extract_title(self, markdown: str, url: str) -> str:
        match = re.search(r'^#\s+(.+?)\s*$', markdown, flags=re.MULTILINE)
        if match:
            return match.group(1).strip()
        path = urlparse(url).path.strip('/')
        return path.split('/')[-1] if path else 'Deribit API'

    def _detect_api_type(self, url: str) -> str:
        path = urlparse(url).path.strip('/')
        first = path.split('/')[0] if path else ''
        if first == 'api-reference':
            return 'JSON-RPC'
        if first == 'subscriptions':
            return 'WebSocket'
        if first == 'fix-api':
            return 'FIX'
        if first == 'starbase':
            return 'Starbase'
        if first == 'changelogs':
            return 'Changelog'
        return 'Guide'
