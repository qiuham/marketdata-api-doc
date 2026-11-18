#!/usr/bin/env python3
"""
Bitget 适配器（2026 年的新文档站 https://www.bitget.com/docs/，Zudoku 搭的）

旧地址 /api-doc/... 都跳到这里。站点没有 llms.txt、sitemap，侧边栏在浏览器里才生成，
但不用开浏览器，全部 HTTP 取：
1. 页面清单：任一文档页的 HTML 引用一个 entry.client-*.js，里面有全部路由表：
   - 文档页 "/docs/uta/..."、"/docs/classic/..."：每页加 .md 就是原始 Markdown；
     中文页在 "/zh-CN/docs/..."。英文在前、中文在后，合成一篇双语文档（照币安的做法）。
   - API 参考 "/docs/catalog/<名字>"：每个一份 OpenAPI 规格，编在一个 JS 模块里
     （docs-static/assets/docs-catalog-...en.json-*.js，中文是 ...zh-CN.json-*.js）。
     页面上的 schema.json 下载地址是 404，所以读 JS 模块里的对象字面量（不执行 JS），
     英文、中文各转一遍 Markdown，合成一篇。
2. 统一账户（UTA，/docs/uta/）和经典账户（classic，/docs/classic/）是两套接口，都收。
"""
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Tuple

from loguru import logger as log

from .base import DocumentPage, ExchangeAdapter, register_adapter
from ..utils.http import fetch_text, looks_like_html, strip_llm_preamble
from ..utils.js_literal import parse_module_export
from ..utils.markdown import MarkdownProcessor
from ..utils.openapi_md import OpenApiRenderer
from ..utils.path_generator import safe_output_path

_ENTRY_RE = re.compile(r'src="(/docs-static/assets/entry\.client-[^"]+\.js)"')
# 文档页路由："/docs/uta/quick-start":()=>N(()=>import(`./quick-start-xxxx.js`)
_DOC_ROUTE_RE = re.compile(r'"(/docs/[A-Za-z0-9_./-]+)":\(\)=>\w+\(\(\)=>import\(')
# 规格模块："/data/.../processed/<文件>":()=>N(()=>import(`./<资源>`)
_SPEC_MODULE_RE = re.compile(r'"/[^"]*/processed/([^"/]+)":\(\)=>\w+\(\(\)=>import\(`\./([^`]+)`\)')
# API 参考：{type:`file`,input:[{... input:`/data/.../<文件>` ...}],path:`/docs/catalog/<名字>`
_API_RE = re.compile(r'\{type:`file`,input:\[\{(.*?)\}\],path:`(/(?:zh-CN/)?docs/catalog/[^`]+)`')


@register_adapter('bitget')
class BitgetAdapter(ExchangeAdapter):
    """Bitget 新文档站适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.md_processor = MarkdownProcessor()
        crawler = self.config.get('crawler', {})
        self.site = crawler.get('site', 'https://www.bitget.com').rstrip('/')
        self.entry_page = crawler.get('entry_page', '/docs/uta/Introduction')
        self.secondary_prefix = crawler.get('secondary_prefix', '/zh-CN')
        self.doc_sections = tuple(crawler.get('doc_sections', ['/docs/uta/', '/docs/classic/']))
        self.request_delay = float(crawler.get('request_delay', 0.3))
        self.entry_js = ''

    # ------------------------------------------------------------------
    # 发现页面
    # ------------------------------------------------------------------
    def _load_entry(self) -> str:
        html = fetch_text(self.site + self.entry_page, accept='text/html')
        match = _ENTRY_RE.search(html or '')
        if not match:
            raise RuntimeError(f"文档页里找不到 entry.client 脚本: {self.site + self.entry_page}")
        js = fetch_text(self.site + match.group(1), accept='application/javascript')
        if not js or len(js) < 100000:
            raise RuntimeError(f"读不到 entry.client 脚本: {match.group(1)}")
        return js

    def discover_pages(self) -> List[str]:
        """文档页的英文路径，例如 /docs/uta/websocket/public/Order-Book-Channel。"""
        pages = sorted({p for p in _DOC_ROUTE_RE.findall(self.entry_js) if p.startswith(self.doc_sections)})
        log.success(f"文档页 {len(pages)} 个")
        return pages

    def discover_apis(self) -> List[Tuple[str, str, str]]:
        """API 参考：[(英文路径, 英文规格资源, 中文规格资源)]，资源是 docs-static/assets 下的文件名。"""
        modules = dict(_SPEC_MODULE_RE.findall(self.entry_js))
        by_path: Dict[str, str] = {}
        for body, path in _API_RE.findall(self.entry_js):
            m = re.search(r'input:`[^`]*/([^`/]+)`', body)
            if m and m.group(1) in modules:
                by_path[path] = modules[m.group(1)]
        apis = []
        for path, asset in by_path.items():
            if path.startswith('/docs/'):
                apis.append((path, asset, by_path.get(self.secondary_prefix + path, '')))
        log.success(f"API 参考 {len(apis)} 个")
        return sorted(apis)

    # ------------------------------------------------------------------
    # 文档页
    # ------------------------------------------------------------------
    def _fetch_doc(self, path: str) -> Tuple[str, Optional[DocumentPage], str]:
        parts: List[str] = []
        title = ''
        for i, prefix in enumerate(['', self.secondary_prefix]):
            time.sleep(self.request_delay)
            text = fetch_text(f'{self.site}{prefix}{path}.md', accept='text/markdown')
            if not text or looks_like_html(text) or not text.strip():
                if i == 0:
                    return path, None, '读不到英文页'
                continue
            body = strip_llm_preamble(text)
            if i == 0:
                match = re.search(r'^#\s+(.+?)\s*$', body, flags=re.MULTILINE)
                title = match.group(1).strip() if match else path.rsplit('/', 1)[-1]
            parts.append(body.strip())
        url = f'{self.site}{path}'
        page = DocumentPage(
            url=url, title=title, content='\n\n---\n\n'.join(p for p in parts if p),
            metadata={'exchange': self.name, 'source_url': url, 'api_type': self._doc_api_type(path)},
        )
        return path, page, ''

    # ------------------------------------------------------------------
    # API 参考
    # ------------------------------------------------------------------
    def _load_spec(self, asset: str) -> Dict[str, Any]:
        time.sleep(self.request_delay)
        js = fetch_text(f'{self.site}/docs-static/assets/{asset}', accept='application/javascript')
        if not js:
            raise RuntimeError(f'取不到规格模块: {asset}')
        spec = parse_module_export(js, 'schema')
        if not isinstance(spec, dict) or 'paths' not in spec:
            raise RuntimeError(f'规格模块里没有 OpenAPI: {asset}')
        return spec

    def _fetch_api(self, item: Tuple[str, str, str]) -> Tuple[str, Optional[DocumentPage], str]:
        path, en_asset, zh_asset = item
        try:
            spec = self._load_spec(en_asset)
            title, body = OpenApiRenderer(spec).render()
            parts = [body]
            if zh_asset:
                _, zh_body = OpenApiRenderer(self._load_spec(zh_asset)).render()
                parts.append(zh_body)
        except Exception as exc:  # noqa: BLE001 - 一个 API 失败不影响其它
            return path, None, str(exc)
        url = f'{self.site}{path}'
        return path, DocumentPage(
            url=url, title=title, content='\n\n---\n\n'.join(parts),
            metadata={'exchange': self.name, 'source_url': url, 'api_type': 'REST'},
        ), ''

    # ------------------------------------------------------------------
    # 主流程
    # ------------------------------------------------------------------
    def extract_content(self, url: str) -> DocumentPage:
        raise NotImplementedError('Bitget 适配器在 crawl 里一次取完')

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        output_dir = self.get_output_path()
        os.makedirs(output_dir, exist_ok=True)
        self.entry_js = self._load_entry()

        jobs: List[Tuple[Any, Any]] = [(self._fetch_doc, p) for p in self.discover_pages()]
        jobs += [(self._fetch_api, a) for a in self.discover_apis()]
        if limit and limit > 0:
            jobs = jobs[:limit]

        failed: List[str] = []
        written: set = set()
        with ThreadPoolExecutor(max_workers=max(1, concurrency)) as pool:
            results = pool.map(lambda job: job[0](job[1]), jobs)
            for i, (path, page, error) in enumerate(results, 1):
                if page is None or len(page.content) < 40:
                    failed.append(f'{path}: {error or "正文过短"}')
                    log.error(f"[{i}/{len(jobs)}] {path} - {error or '正文过短'}")
                    continue
                rel = path[len('/docs/'):] + '.md'
                written.add(self._save(page, rel, output_dir))
        log.success(f"完成: {len(written)}/{len(jobs)}")
        for item in failed:
            log.warning(f"失败: {item}")
        if not written:
            raise RuntimeError("Bitget 一页也没抓到")
        if len(failed) > max(2, len(jobs) // 50):
            raise RuntimeError(f"Bitget 失败 {len(failed)}/{len(jobs)} 页，保留旧文档")
        if not limit:
            # 官网删掉的页：本次没写到的旧文件删掉
            for root, _, files in os.walk(output_dir):
                for f in files:
                    p = os.path.realpath(os.path.join(root, f))
                    if f.endswith('.md') and p not in written:
                        os.remove(p)
                        log.info(f"删除官网已没有的页: {os.path.relpath(p, output_dir)}")

    def _save(self, page: DocumentPage, rel: str, output_dir: str) -> str:
        path = safe_output_path(output_dir, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.md_processor.create_document(page.title, page.content, page.metadata))
        return os.path.realpath(path)

    @staticmethod
    def _doc_api_type(path: str) -> str:
        lower = path.lower()
        if '/changelog/' in lower:
            return 'Changelog'
        if '/sbe/' in lower:
            return 'SBE'
        if 'websocket' in lower:
            return 'WebSocket'
        if 'error-code' in lower:
            return 'Error Code'
        if 'rate-limit' in lower:
            return 'Rate Limit'
        return 'Guide'
