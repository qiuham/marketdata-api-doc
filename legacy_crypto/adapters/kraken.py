#!/usr/bin/env python3
"""
Kraken 适配器（Docusaurus 格式）
"""
import os
import re
import time
import html as html_lib
from typing import List, Dict, Any, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage, register_adapter
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


class KrakenBadPageError(RuntimeError):
    """页面命中 Cloudflare/验证页等坏页时抛出，避免覆盖已有好内容。"""


@register_adapter('kraken')
class KrakenAdapter(ExchangeAdapter):
    """Kraken Docusaurus 适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def discover_pages(self) -> List[str]:
        """从 Kraken API 首页顶部导航发现启用菜单，再收集各菜单侧边栏页面。"""
        import json

        crawler_config = self.config.get('crawler', {})
        home_url = crawler_config.get('home_url', 'https://docs.kraken.com/api/')
        scope_prefix = crawler_config.get('scope_prefix', 'https://docs.kraken.com/api/docs/').rstrip('/')
        nav_items = crawler_config.get('nav_items', [])

        if not nav_items:
            log.error("未配置 nav_items")
            return []

        # 先打开稳定首页，从顶部导航拿当前真实入口；如果没拿到则回退到配置 URL。
        if not self.browser.open(home_url, wait=5):
            log.error(f"无法打开 Kraken API 首页: {home_url}")
            return []

        nav_links = self.browser.eval_js(r'''
        (function() {
            const links = Array.from(document.querySelectorAll('nav a, a[href*="/api/docs/"]'))
                .map(a => ({
                    text: (a.textContent || '').trim().replace(/\s+/g, ' '),
                    href: (a.href || '').split('#')[0].replace(/\/$/, '')
                }))
                .filter(item => item.href && item.href.startsWith('https://docs.kraken.com/api/docs/'));
            return Array.from(new Map(links.map(item => [item.href, item])).values());
        })()
        ''') or []

        seeds = []
        for item in nav_items:
            label = item.get('label', '')
            fallback_url = self._normalize_url(item.get('url', ''))
            label_lower = label.lower()

            matched = None
            for link in nav_links:
                href = self._normalize_url(link.get('href', ''))
                text = (link.get('text') or '').lower()
                if href == fallback_url or (label_lower and label_lower in text):
                    matched = href
                    break

            seed_url = matched or fallback_url
            if seed_url:
                if matched:
                    log.info(f"顶部菜单: {label} -> {seed_url}")
                else:
                    log.warning(f"首页未匹配到菜单 {label}，使用配置 URL: {seed_url}")
                seeds.append(seed_url)

        all_links = set()
        for i, seed_url in enumerate(dict.fromkeys(seeds), 1):
            log.info(f"[{i}/{len(seeds)}] 发现菜单页面: {seed_url}")
            if not self.browser.open(seed_url, wait=4):
                log.warning(f"无法打开菜单入口: {seed_url}")
                continue

            menu_links = self._collect_sidebar_links(scope_prefix)
            menu_links.add(seed_url)
            log.success(f"{seed_url} -> {len(menu_links)} 个页面")
            all_links.update(menu_links)

        unique_links = sorted(all_links)
        log.success(f"Kraken 启用菜单共发现 {len(unique_links)} 个唯一页面")
        return unique_links

    def _normalize_url(self, url: str) -> str:
        """规范化 URL，去掉 hash 和尾部斜杠。"""
        return (url or '').split('#')[0].rstrip('/')

    def _collect_sidebar_links(self, scope_prefix: str) -> set:
        """展开当前 Docusaurus 侧边栏，并收集当前菜单下的文档链接。"""
        import json

        selector = self.config['crawler']['selectors'].get('sidebar_links', '.menu__link')
        selector_json = json.dumps(selector)
        scope_prefix_json = json.dumps(scope_prefix)

        collected = set()
        last_count = -1
        stable_rounds = 0

        for _ in range(20):
            js = f'''
            (function() {{
                let clicked = 0;
                document.querySelectorAll('.menu__list-item--collapsed').forEach(item => {{
                    let btn = item.querySelector('button.menu__caret') || item.querySelector('a[role="button"]');
                    if (btn) {{
                        try {{
                            btn.click();
                            clicked++;
                        }} catch(e) {{}}
                    }}
                }});

                document.querySelectorAll('aside, nav, [role="navigation"]').forEach(el => {{
                    try {{
                        if (el.scrollHeight > el.clientHeight) el.scrollTop = el.scrollHeight;
                    }} catch(e) {{}}
                }});

                const scopePrefix = {scope_prefix_json};
                const links = Array.from(document.querySelectorAll({selector_json}))
                    .map(a => (a.href || '').split('#')[0].replace(/\\/$/, ''))
                    .filter(href => href && href.startsWith(scopePrefix))
                    .filter(href => href.indexOf('/category/') === -1);

                return {{clicked, links: Array.from(new Set(links)).sort()}};
            }})()
            '''

            result = self.browser.eval_js(js) or {}
            for link in result.get('links') or []:
                collected.add(link)

            if len(collected) == last_count:
                stable_rounds += 1
            else:
                stable_rounds = 0
            last_count = len(collected)

            if stable_rounds >= 2:
                break

            time.sleep(0.2)

        return collected

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面内容（包括所有语言的代码示例）"""

        # 打开页面（增加等待时间避免 Cloudflare 验证）
        if not skip_open:
            self.browser.open(url, wait=5)

        # 提取标题
        title_js = '''
        (function() {
            const article = document.querySelector('article');
            if (article) {
                const h1 = article.querySelector('h1');
                if (h1) return h1.textContent.trim();
            }
            const anyH1 = document.querySelector('h1');
            if (anyH1) return anyH1.textContent.trim();
            return document.title.split('|')[0].trim();
        })()
        '''
        title = self.browser.eval_js(title_js) or "Untitled"

        body_text = self.browser.eval_js("document.body ? document.body.innerText : ''") or ""
        if self._is_bad_page(title=title, html=body_text):
            log.warning(f"检测到坏页/验证页，尝试静态 HTML 回退: {url}")
            static_page = self._fetch_static_page(url)
            if static_page:
                return static_page
            raise KrakenBadPageError(f"检测到坏页/验证页，已跳过保存: {url}")

        # 提取基础内容
        content_selector = self.config['crawler']['selectors']['main_content']
        js_extract_base = f'''
        (function() {{
            const main = document.querySelector('{content_selector}');
            if (!main) return null;

            const clone = main.cloneNode(true);

            // 清理不需要的元素
            const selectors = [
                'nav', 'header', 'footer', 'button',
                '[class*="copy"]', 'svg'
            ];

            selectors.forEach(sel => {{
                clone.querySelectorAll(sel).forEach(el => el.remove());
            }});

            // 显示所有隐藏的 tabpanel（如 response examples）
            clone.querySelectorAll('[role="tabpanel"][hidden]').forEach(panel => {{
                panel.removeAttribute('hidden');
                panel.style.display = 'block';
            }});

            return clone.innerHTML;
        }})()
        '''

        base_html = self.browser.eval_js(js_extract_base)

        if not base_html:
            log.warning(f"无法从浏览器提取内容，尝试静态 HTML 回退: {url}")
            static_page = self._fetch_static_page(url)
            if static_page:
                return static_page
            log.warning(f"无法提取内容: {url}")
            return DocumentPage(
                url=url,
                title=title,
                content="",
                metadata={},
                raw_html=""
            )

        # 转换基础内容为 Markdown（只提取默认显示的内容，不点击其他 tab）
        markdown = self.md_processor.html_to_markdown(base_html)
        markdown = self._clean_markdown(markdown)

        if self._is_bad_page(title=title, html=base_html, markdown=markdown):
            log.warning(f"浏览器内容疑似坏页，尝试静态 HTML 回退: {url}")
            static_page = self._fetch_static_page(url)
            if static_page:
                return static_page
            raise KrakenBadPageError(f"检测到坏页/验证页，已跳过保存: {url}")

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
            raw_html=base_html
        )

    def save_page(self, page: DocumentPage, output_path: str):
        """保存页面到文件"""
        if self._is_bad_page(
            title=page.title,
            html=page.raw_html,
            markdown=page.content
        ):
            raise KrakenBadPageError(f"拒绝保存坏页: {page.url}")

        processor = MarkdownProcessor()

        doc_content = processor.create_document(
            title=page.title,
            content=page.content,
            metadata=page.metadata
        )

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        return output_path

    def _fetch_static_page(self, url: str) -> Optional[DocumentPage]:
        """Docusaurus SSR 静态 HTML 回退；不用用户 Cookie，失败则返回 None。"""
        request_url = url if url.endswith('/') else f"{url}/"
        normalized_url = self._normalize_url(url)
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
            ),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        try:
            req = Request(request_url, headers=headers)
            with urlopen(req, timeout=30) as response:
                charset = response.headers.get_content_charset() or 'utf-8'
                html = response.read().decode(charset, errors='replace')
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            log.warning(f"静态 HTML 回退失败: {url} - {exc}")
            return None

        return self._page_from_static_html(normalized_url, html)

    def _page_from_static_html(self, url: str, html: str) -> Optional[DocumentPage]:
        """从 Docusaurus 静态 HTML 中提取正文。"""
        if not html or self._is_bad_page(html=html):
            log.warning(f"静态 HTML 也是坏页，跳过: {url}")
            return None

        article_html = self._extract_doc_html(html)
        if not article_html:
            log.warning(f"静态 HTML 未找到正文: {url}")
            return None

        title = self._extract_title(article_html, html)
        markdown = self.md_processor.html_to_markdown(article_html)
        markdown = self._clean_markdown(markdown)

        if not markdown or self._is_bad_page(title=title, html=article_html, markdown=markdown):
            log.warning(f"静态 HTML 正文疑似坏页，跳过: {url}")
            return None

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
            raw_html=article_html
        )

    def _extract_doc_html(self, html: str) -> str:
        """提取 Docusaurus 文档正文容器 HTML。"""
        match = re.search(
            r'<div\b(?=[^>]*\btheme-doc-markdown\b)(?=[^>]*\bmarkdown\b)[^>]*>',
            html,
            flags=re.IGNORECASE
        )
        if match:
            return self._extract_balanced_tag(html, match.start(), 'div')

        match = re.search(r'<article\b[^>]*>', html, flags=re.IGNORECASE)
        if match:
            return self._extract_balanced_tag(html, match.start(), 'article')

        return ""

    def _extract_balanced_tag(self, html: str, start: int, tag_name: str) -> str:
        """从 start 处按同名标签配平，返回完整元素 HTML。"""
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

    def _extract_title(self, article_html: str, full_html: str) -> str:
        """从正文或 HTML title 中提取页面标题。"""
        for pattern in [
            r'<h1\b[^>]*>(.*?)</h1>',
            r'<title\b[^>]*>(.*?)</title>',
        ]:
            source = article_html if 'h1' in pattern else full_html
            match = re.search(pattern, source, flags=re.IGNORECASE | re.DOTALL)
            if match:
                title = re.sub(r'<[^>]+>', '', match.group(1))
                title = html_lib.unescape(title).strip()
                if '|' in title:
                    title = title.split('|', 1)[0].strip()
                if title:
                    return title

        return "Untitled"

    def _is_bad_page(self, title: str = "", html: str = "", markdown: str = "") -> bool:
        """识别 Cloudflare/验证页，避免把挑战页写成文档。"""
        title_text = re.sub(r'\s+', ' ', title or '').strip().lower()
        if title_text in {'one more step', 'just a moment...', 'attention required!'}:
            return True

        text = "\n".join(part for part in [title or "", html or "", markdown or ""] if part).lower()
        challenge_markers = [
            'one more step',
            'needs to review the security of your connection',
            'checking if the site connection is secure',
            'enable javascript and cookies to continue',
            'why do i have to complete a captcha',
            'verify you are human',
            'cf-chl',
            'cf_chl',
            'cf-turnstile',
            'challenge-platform',
            'cloudflare ray id',
        ]

        return any(marker in text for marker in challenge_markers)

    def _clean_markdown(self, markdown: str) -> str:
        """清理Markdown内容"""
        markdown = markdown.replace('\u200b', '')

        # 移除常见的UI元素文本
        ui_patterns = [
            r'copy.*?\n',
            r'\[Previous.*?\]\(.*?\)',
            r'\[Next.*?\]\(.*?\)',
            r'Last updated.*?\n'
        ]

        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        # 清理混乱的 Authorization 元数据信息
        # 匹配：#### Authorization: API-Key 开头，后面跟着多行 **name:**... 的内容
        markdown = re.sub(
            r'####\s+Authorization:\s+API-Key\s+\*\*name:\*\*.*?(?=\n\s*\*\s+curl|\n\s*##|\Z)',
            '',
            markdown,
            flags=re.DOTALL | re.MULTILINE
        )

        # 修复 POST/GET/PUT/DELETE + URL 的格式
        # 例如：POST \n    \n    ## https://api.kraken.com/...
        # 转换为：POST `https://api.kraken.com/...`
        markdown = re.sub(
            r'(POST|GET|PUT|DELETE|PATCH)\s*\n\s+##\s+(https?://[^\s]+)',
            r'**\1** `\2`',
            markdown,
            flags=re.IGNORECASE
        )

        # 修复 WebSocket URL 格式
        # 例如：REQUEST \n    \n    ## wss://ws-auth.kraken.com/v2
        markdown = re.sub(
            r'REQUEST\s*\n\s+##\s+(wss?://[^\s]+)',
            r'**WebSocket Endpoint:** `\1`',
            markdown,
            flags=re.IGNORECASE
        )

        # 修复剩余的 URL 被错误转换为标题的问题
        markdown = re.sub(
            r'^\s*##\s+((?:wss?|https?)://[^\s]+)\s*$',
            r'**Endpoint:** `\1`',
            markdown,
            flags=re.MULTILINE
        )

        # 修复 URL 后面紧跟的方法名
        # 例如：add_orderAuthentication Required -> **Method:** `add_order` (Authentication Required)
        markdown = re.sub(
            r'^\s*([a-z_]+)Authentication Required\s*$',
            r'**Method:** `\1` (Authentication Required)',
            markdown,
            flags=re.MULTILINE
        )

        # 移除列表项前的缩进（4个空格），避免被识别为代码块
        # 处理各种列表格式：* •, *, -, +, 数字列表等
        markdown = re.sub(
            r'^(\s{4,})(\*\s+[•\-\+]?|\-\s+|\+\s+|\d+\.\s+)',
            r'\2',
            markdown,
            flags=re.MULTILINE
        )

        # 也移除纯粹的 4 空格缩进（在列表上下文中）
        # 但保留代码块内的缩进
        lines = markdown.split('\n')
        result_lines = []
        in_code_block = False
        prev_was_list = False

        for line in lines:
            # 检测代码块标记
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                result_lines.append(line)
                prev_was_list = False
                continue

            # 在代码块内，保持原样
            if in_code_block:
                result_lines.append(line)
                continue

            # 检测是否是列表项
            is_list = bool(re.match(r'^\s{0,3}[\*\-\+]\s+', line))

            # 如果当前行或上一行是列表项，并且当前行有 4+ 空格缩进
            # 则移除缩进（但保留相对缩进结构）
            if (is_list or prev_was_list) and line.startswith('    '):
                # 移除 4 个空格
                result_lines.append(line[4:])
            else:
                result_lines.append(line)

            prev_was_list = is_list

        markdown = '\n'.join(result_lines)

        # 优化参数格式（保持列表，不转表格）
        markdown = self._format_parameters(markdown)

        # 标记 Example 部分（在代码块前添加标题）
        markdown = re.sub(
            r'(\n)(```(?:json|javascript)?)\n',
            r'\1#### Example\n\n\2\n',
            markdown
        )

        # 清理多余的空行
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown.strip()

    def _format_parameters(self, markdown: str) -> str:
        """格式化参数列表（保持原始列表格式，恢复层级结构）"""
        lines = markdown.split('\n')
        result = []
        i = 0
        indent_level = 0  # 当前缩进级别
        last_was_object = False  # 上一个参数是否是 object/array 类型

        while i < len(lines):
            line = lines[i]

            # 检测参数的格式：**param_name** type required/conditional
            # 改进格式为：**param_name** `type` *required/conditional*
            param_match = re.match(r'^\*\*([a-z_]+)\*\*\s+(.+)$', line.strip())
            if param_match:
                name = param_match.group(1)
                rest = param_match.group(2).strip()

                # 尝试分离 required/conditional（可能紧跟着 type，也可能有空格）
                required = None
                type_str = rest

                # 匹配末尾的 required 或 conditional
                if rest.endswith('required'):
                    required = 'required'
                    type_str = rest[:-8].strip()  # 移除 'required'
                elif rest.endswith('conditional'):
                    required = 'conditional'
                    type_str = rest[:-11].strip()  # 移除 'conditional'

                # 检查类型是否是 object 或 array
                is_object_or_array = 'object' in type_str.lower() or 'array' in type_str.lower()

                # 如果上一个参数是 object/array，当前参数应该缩进
                if last_was_object:
                    indent_level += 1
                    last_was_object = False

                # 如果当前参数不是子属性的开始（检测一些标志），减少缩进
                # 比如遇到 method, params, result 等顶层字段
                if name in ['method', 'params', 'result', 'error', 'success', 'req_id', 'time_in', 'time_out']:
                    indent_level = 0

                # 格式化为更清晰的样式，使用更明显的缩进和符号
                if indent_level > 0:
                    # 子参数：使用 4 空格缩进 + └─ 符号
                    indent = '    ' * indent_level
                    prefix = '↳ '  # 或者用 '└─ '
                else:
                    indent = ''
                    prefix = ''

                if required:
                    result.append(f'{indent}{prefix}**{name}** `{type_str}` *{required}*')
                else:
                    result.append(f'{indent}{prefix}**{name}** `{type_str}`')

                # 如果当前参数是 object/array，下一个参数应该缩进
                if is_object_or_array:
                    last_was_object = True
                else:
                    last_was_object = False

                i += 1
                continue

            # 遇到标题、代码块等，重置缩进
            if line.strip().startswith('#') or line.strip().startswith('```'):
                indent_level = 0
                last_was_object = False

            # 保持其他行不变
            result.append(line)
            i += 1

        return '\n'.join(result)

    def _detect_api_type(self, url: str, title: str) -> str:
        """检测API类型"""
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'websocket' in title_lower or 'ws' in url_lower:
            return 'WebSocket'
        elif 'nft' in url_lower or 'nft' in title_lower:
            return 'NFT'
        elif 'market' in url_lower or 'market' in title_lower:
            return 'Market Data'
        elif 'etp' in url_lower:
            return 'ETP'
        elif 'guide' in url_lower or 'intro' in url_lower:
            return 'Guide'
        else:
            return 'REST'

    def _extract_category(self, url: str) -> str:
        """从URL提取类别名

        例如:
        https://docs.kraken.com/api/docs/rest-api/... -> rest-api
        https://docs.kraken.com/api/docs/websocket-v2/... -> websocket-v2
        """
        match = re.search(r'/api/docs/([^/]+)', url)
        if match:
            return match.group(1)

        log.warning(f"无法从URL提取类别: {url}")
        return 'default'

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """执行完整的Kraken爬取流程"""
        from pathlib import Path

        log.info("开始从 Kraken API 首页发现启用菜单页面")
        all_pages = self.discover_pages()

        if not all_pages:
            log.error("未发现任何页面")
            return

        # 限制爬取数量（全局）
        if limit and limit > 0:
            all_pages = all_pages[:limit]
            log.warning(f"限制模式：只爬取前 {len(all_pages)} 页")

        log.info(f"\n{'='*60}")
        log.success(f"总共发现 {len(all_pages)} 个唯一页面")
        log.info(f"{'='*60}\n")

        # 提取内容
        log.info("开始提取内容...")
        output_dir = self.get_output_path()

        if concurrency == 1:
            success_count = self._crawl_sequential(all_pages, output_dir)
        else:
            success_count = self._crawl_concurrent(all_pages, output_dir, concurrency)

        log.success(f"完成! 成功: {success_count}/{len(all_pages)}")

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

    def _crawl_sequential(self, urls, output_dir):
        """顺序爬取（Kraken 需要较慢速度避免 Cloudflare 验证）"""
        import time
        from ..utils.path_generator import safe_output_path, url_to_filepath

        # 获取基础前缀用于生成文件名
        # https://docs.kraken.com/api/docs/xxx/... -> https://docs.kraken.com/api/docs/
        base_prefix = "https://docs.kraken.com/api/docs/"

        success_count = 0
        for i, url in enumerate(urls, 1):
            try:
                filename = url_to_filepath(url, base_prefix)
                output_path = safe_output_path(output_dir, filename)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                page = self.extract_content(url)
                self.save_page(page, output_path)
                log.success(f"[{i}/{len(urls)}] {page.title}")
                success_count += 1

                # 增加延迟避免触发 Cloudflare 保护
                if i < len(urls):
                    time.sleep(1)
            except Exception as e:
                log.error(f"[{i}/{len(urls)}] {url} - {e}")

        return success_count

    def _crawl_concurrent(self, urls, output_dir, concurrency):
        """多标签并发爬取"""
        from ..utils.path_generator import safe_output_path, url_to_filepath

        browser = self.browser
        total = len(urls)
        success_count = 0

        # 获取基础前缀用于生成文件名
        base_prefix = "https://docs.kraken.com/api/docs/"

        # 已有tab 0，再创建N-1个新标签
        num_tabs = min(concurrency, total)
        browser.open_tabs_batch(num_tabs - 1)

        for batch_start in range(0, total, num_tabs):
            batch_urls = urls[batch_start:batch_start + num_tabs]

            # 1. 批量加载URLs
            browser.load_urls_batch(batch_urls, start_tab=0)

            # 2. 顺序提取内容
            for i, url in enumerate(batch_urls):
                idx = batch_start + i + 1
                try:
                    browser.tab_switch(i)

                    # 等待页面加载完成
                    if not browser.wait_for_element('main', timeout=30):
                        log.warning(f"[{idx}/{total}] 页面加载超时，尝试继续")

                    filename = url_to_filepath(url, base_prefix)
                    output_path = safe_output_path(output_dir, filename)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)

                    page = self.extract_content(url, skip_open=True)
                    self.save_page(page, output_path)

                    log.success(f"[{idx}/{total}] {page.title}")
                    success_count += 1
                except Exception as e:
                    log.error(f"[{idx}/{total}] {url} - {e}")

        return success_count
