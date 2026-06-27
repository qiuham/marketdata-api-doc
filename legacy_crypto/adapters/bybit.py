#!/usr/bin/env python3
"""
Bybit 适配器（Docusaurus 格式）
"""
import os
import time
import re
from typing import List, Dict, Any
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage, register_adapter
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


@register_adapter('bybit')
class BybitAdapter(ExchangeAdapter):
    """Bybit Docusaurus 适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def discover_pages(self) -> List[str]:
        """发现当前页面的所有文档页面"""

        # 获取当前页面URL
        current_url_js = 'window.location.href'
        current_url = self.browser.eval_js(current_url_js)

        if not current_url:
            log.error("无法获取当前页面URL")
            return []

        # Bybit URL格式:
        # 英文: https://bybit-exchange.github.io/docs/v5/...
        # 中文: https://bybit-exchange.github.io/docs/zh-TW/v5/...

        # 提取产品路径前缀（到 v5/ 为止）
        match = re.match(r'(https://[^/]+/docs/(?:[^/]+/)?v5/)', current_url)
        if not match:
            log.warning(f"无法从URL提取产品路径: {current_url}")
            product_prefix = None
        else:
            product_prefix = match.group(1)
            log.info(f"产品路径前缀: {product_prefix}")

        # 展开所有折叠菜单 (使用aria-expanded属性定位)
        max_iterations = 20
        prev_clicked = None

        for i in range(max_iterations):
            # 点击所有未展开的折叠菜单，使用更简单的选择器
            js_expand = '''
            (function() {
                const collapsed = document.querySelectorAll('.menu__list-item--collapsed .menu__link--sublist');
                let clicked = 0;
                collapsed.forEach(link => {
                    if (link && link.getAttribute('aria-expanded') === 'false') {
                        try {
                            link.click();
                            clicked++;
                        } catch(e) {}
                    }
                });
                return clicked;
            })()
            '''

            clicked = self.browser.eval_js(js_expand) or 0

            if clicked == 0:
                log.info("所有菜单已展开")
                break

            log.info(f"[轮次 {i+1}] 折叠菜单: {clicked} 个")
            # 不需要sleep，Python/Browser往返时React会完成渲染

            # 如果连续2轮都是同样数量，说明无法继续展开，退出
            if prev_clicked is not None and clicked == prev_clicked:
                # 这些通常是顶层分类菜单（href="#"），不影响爬取
                log.info(f"检测到 {clicked} 个顶层菜单项无法展开（通常是分类菜单），已获取所有可用链接")
                break
            prev_clicked = clicked

        # 提取所有侧边栏链接
        sidebar_selector = self.config['crawler']['selectors']['sidebar_links']
        js_extract = f'''
        (function() {{
            const links = document.querySelectorAll('{sidebar_selector}');
            return Array.from(links).map(a => a.href);
        }})()
        '''

        all_links = self.browser.eval_js(js_extract) or []

        if not all_links:
            return []

        # 过滤：只保留同一产品的链接
        filtered_links = []
        for link in all_links:
            if product_prefix and link.startswith(product_prefix):
                filtered_links.append(link)
            elif not product_prefix:
                filtered_links.append(link)

        # 去重并排序
        unique_links = list(set(filtered_links))
        unique_links.sort()

        log.info(f"过滤前: {len(all_links)} 个链接，过滤后: {len(unique_links)} 个链接")
        log.info(f"发现 {len(unique_links)} 个唯一页面（去重后）")

        return unique_links

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面内容"""

        # 打开页面（并发模式下已打开则跳过）
        if not skip_open:
            self.browser.open(url, wait=2)

        # 提取标题
        title_js = 'document.querySelector("h1")?.textContent?.trim() || document.title'
        title = self.browser.eval_js(title_js) or "Untitled"

        # 提取主内容
        content_selector = self.config['crawler']['selectors']['main_content']
        js_extract = f'''
        (function() {{
            const main = document.querySelector('{content_selector}');
            if (!main) return '';

            // 克隆节点避免修改原始DOM
            const clone = main.cloneNode(true);

            // 移除不需要的元素
            const selectors = [
                'nav',  // 所有导航
                '.theme-doc-breadcrumbs',  // 面包屑
                '.breadcrumbs',  // 面包屑
                '[class*="toc"]',  // 目录
                '[class*="TOC"]',  // 目录
                '.table-of-contents',  // 目录
                '[class*="pagination"]',  // 分页
                'button',  // 按钮
                '[class*="copy"]',  // 复制按钮
                'svg',  // SVG图标
                '.hash-link'  // hash 链接
            ];

            selectors.forEach(sel => {{
                clone.querySelectorAll(sel).forEach(el => el.remove());
            }});

            return clone.innerHTML;
        }})()
        '''

        html_content = self.browser.eval_js(js_extract) or ""

        if not html_content:
            log.warning(f"未提取到内容: {url}")

        # 转换为 Markdown
        markdown = self.md_processor.html_to_markdown(html_content)

        # 确定API类型（从URL路径推断）
        api_type = self._infer_api_type(url)

        # 构建元数据
        metadata = {
            'exchange': self.name,
            'source_url': url,
            'api_type': api_type
        }

        return DocumentPage(
            url=url,
            title=title,
            content=markdown,
            metadata=metadata,
            raw_html=html_content
        )

    def _infer_api_type(self, url: str) -> str:
        """从URL推断API类型"""
        if '/market/' in url:
            return 'Market Data'
        elif '/trade/' in url or '/order/' in url:
            return 'Trading'
        elif '/account/' in url:
            return 'Account'
        elif '/position/' in url:
            return 'Position'
        elif '/websocket/' in url:
            return 'WebSocket'
        else:
            return 'REST'

    def save_page(self, page: DocumentPage, output_path: str):
        """保存页面到文件"""
        # 创建完整文档
        doc_content = self.md_processor.create_document(
            title=page.title,
            content=page.content,
            metadata=page.metadata
        )

        # 确保目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """执行完整的爬取流程（多语言支持）"""
        import os
        import tempfile
        from pathlib import Path

        log.info(f"开始爬取: {self.name} (并发: {concurrency})")

        if limit:
            log.warning(f"限制模式：每个入口最多爬取 {limit} 页")

        # 获取语言配置
        lang_configs = self.config['crawler'].get('languages', [])

        # 如果用户指定了语言，过滤
        if languages:
            lang_configs = [lc for lc in lang_configs if lc['lang'] in languages]

        if not lang_configs:
            log.error("没有可用的语言配置")
            return

        log.info(f"开始多语言爬取，共 {len(lang_configs)} 种语言")

        # 遍历每种语言
        for lang_idx, lang_config in enumerate(lang_configs, 1):
            lang = lang_config['lang']
            start_urls = lang_config['start_urls']

            log.info("\n" + "="*60)
            log.info(f"[{lang_idx}/{len(lang_configs)}] 开始爬取语言: {lang.upper()}")
            log.info("="*60)

            if not start_urls:
                log.warning(f"{lang} 没有配置 start_urls")
                continue

            # Bybit 只有一个入口
            entry_url = start_urls[0]
            log.info(f"入口: {entry_url}")

            # 打开入口页面
            if not self.browser.open(entry_url, wait=3):
                log.error(f"无法打开入口页面: {entry_url}")
                continue

            # 发现页面
            log.info("发现页面...")
            urls = self.discover_pages()

            if not urls:
                log.warning("未发现任何页面")
                continue

            log.success(f"发现 {len(urls)} 个页面")

            # 限制爬取数量
            if limit and limit > 0:
                urls = urls[:limit]
                log.warning(f"限制模式：只爬取前 {len(urls)} 页")

            # 为该语言创建临时输出目录
            temp_base = tempfile.gettempdir()
            output_dir = f"{temp_base}/crypto-api-docs/{self.name}/{lang}"
            os.makedirs(output_dir, exist_ok=True)

            # 提取内容
            log.info("开始提取内容...")

            if concurrency == 1:
                success_count = self._crawl_sequential(urls, output_dir)
            else:
                success_count = self._crawl_concurrent(urls, output_dir, concurrency)

            log.success(f"完成! 成功: {success_count}/{len(urls)}")

        # 全部完成后，合并双语文件
        log.info("\n" + "="*60)
        log.info("所有语言爬取完成")

        # 如果爬取了多种语言，合并成双语文件
        if len(lang_configs) > 1:
            log.info("开始合并双语文件...")
            temp_base = f"{tempfile.gettempdir()}/crypto-api-docs/{self.name}"
            base_output_dir = self.get_output_path()
            merged_count = self._merge_bilingual_files(temp_base, base_output_dir, [lc['lang'] for lc in lang_configs])
            log.success(f"合并完成：{merged_count} 个文件")

            # 清理临时文件
            log.info("清理临时文件...")
            if os.path.exists(temp_base):
                from ..utils.path_generator import safe_rmtree
                safe_rmtree(temp_base, [os.path.join(tempfile.gettempdir(), "crypto-api-docs")])
                log.success("临时文件已删除")
        else:
            # 单语言，直接移动文件
            temp_lang_dir = f"{tempfile.gettempdir()}/crypto-api-docs/{self.name}/{lang_configs[0]['lang']}"
            base_output_dir = self.get_output_path()
            if os.path.exists(temp_lang_dir):
                import shutil
                if os.path.exists(base_output_dir):
                    from ..utils.path_generator import safe_rmtree
                    project_root = Path(__file__).parent.parent.parent
                    docs_root = project_root / self.config.get('output', {}).get('base_dir', 'docs')
                    target_output_dir = Path(base_output_dir)
                    if not target_output_dir.is_absolute():
                        target_output_dir = project_root / target_output_dir
                    safe_rmtree(str(target_output_dir), [docs_root])
                shutil.move(temp_lang_dir, base_output_dir)
                log.success(f"文件已移动到: {base_output_dir}")

        # 生成索引
        log.info("生成索引...")
        from ..utils.indexer import DocumentIndexer
        project_root = Path(__file__).parent.parent.parent
        index_dir = project_root / "index"
        indexer = DocumentIndexer(self.get_output_path())
        index_path = indexer.generate_index(str(index_dir))
        log.success(f"索引已生成: {index_path}")

        # 更新主 README
        log.info("更新 README...")
        from ..utils.readme_updater import ReadmeUpdater
        updater = ReadmeUpdater(str(project_root))
        readme_path = updater.update_exchange_table()
        log.success(f"README 已更新: {readme_path}")

    def _crawl_sequential(self, urls: List[str], output_dir: str) -> int:
        """顺序爬取"""
        import re
        from ..utils.path_generator import safe_output_path, url_to_filepath

        # 获取产品前缀用于生成文件名（动态提取，包含语言代码）
        if urls:
            current_url = self.browser.eval_js('window.location.href')
            match = re.match(r'(https://[^/]+/docs/(?:[^/]+/)?[^/]+/)', current_url) if current_url else None
            product_prefix = match.group(1) if match else "https://bybit-exchange.github.io/docs/"
        else:
            product_prefix = "https://bybit-exchange.github.io/docs/"

        success_count = 0
        for i, url in enumerate(urls, 1):
            try:
                page = self.extract_content(url)
                filepath = url_to_filepath(url, product_prefix)
                output_path = safe_output_path(output_dir, filepath)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.save_page(page, output_path)
                log.success(f"[{i}/{len(urls)}] {page.title}")
                success_count += 1
            except Exception as e:
                log.error(f"[{i}/{len(urls)}] {url} - {e}")

        return success_count

    def _crawl_concurrent(self, urls: List[str], output_dir: str, concurrency: int) -> int:
        """多标签并发爬取（与 Binance 相同的实现）"""
        import re
        from ..utils.path_generator import safe_output_path, url_to_filepath

        browser = self.browser
        total = len(urls)
        success_count = 0

        # 获取产品前缀用于生成文件名（动态提取，包含语言代码）
        # 英文: https://bybit-exchange.github.io/docs/v5/... -> https://bybit-exchange.github.io/docs/v5/
        # 中文: https://bybit-exchange.github.io/docs/zh-TW/v5/... -> https://bybit-exchange.github.io/docs/zh-TW/v5/
        if urls:
            current_url = browser.eval_js('window.location.href')
            # 匹配 /docs/ 后面的可选语言代码 + 产品路径
            match = re.match(r'(https://[^/]+/docs/(?:[^/]+/)?[^/]+/)', current_url) if current_url else None
            product_prefix = match.group(1) if match else "https://bybit-exchange.github.io/docs/"
        else:
            product_prefix = "https://bybit-exchange.github.io/docs/"

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
                    if not browser.wait_for_element('article', timeout=30):
                        log.warning(f"[{idx}/{total}] 页面加载超时，尝试继续")

                    filepath = url_to_filepath(url, product_prefix)
                    output_path = safe_output_path(output_dir, filepath)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    page = self.extract_content(url, skip_open=True)
                    self.save_page(page, output_path)

                    log.success(f"[{idx}/{total}] {page.title}")
                    success_count += 1
                except Exception as e:
                    log.error(f"[{idx}/{total}] {url} - {e}")

        return success_count

    def _remove_trailing_separator(self, content: str) -> str:
        """移除内容末尾的 markdown 分隔线"""
        import re
        return re.sub(r'\n+(\*\s*\*\s*\*|---)\s*$', '', content.rstrip())

    def _merge_bilingual_files(self, temp_dir: str, output_dir: str, languages: List[str]) -> int:
        """合并多语言文件为双语文件"""
        import os
        import glob
        from ..utils.path_generator import safe_output_path

        if len(languages) < 2:
            return 0

        # 假设第一种语言是主语言
        primary_lang = languages[0]
        primary_dir = os.path.join(temp_dir, primary_lang)

        if not os.path.exists(primary_dir):
            log.warning(f"主语言目录不存在: {primary_dir}")
            return 0

        # 遍历主语言的所有文件
        pattern = os.path.join(primary_dir, '**', '*.md')
        primary_files = glob.glob(pattern, recursive=True)
        merged_count = 0

        for primary_file in primary_files:
            # 获取相对路径
            rel_path = os.path.relpath(primary_file, primary_dir)

            # 读取主语言内容
            with open(primary_file, 'r', encoding='utf-8') as f:
                primary_content = f.read()

            # 收集其他语言的内容
            other_contents = []
            for lang in languages[1:]:
                lang_file = os.path.join(temp_dir, lang, rel_path)
                if os.path.exists(lang_file):
                    with open(lang_file, 'r', encoding='utf-8') as f:
                        other_contents.append((lang, f.read()))

            # 如果有其他语言的内容，合并
            if other_contents:
                # 移除主语言内容末尾的分隔线
                primary_content = self._remove_trailing_separator(primary_content)
                merged_content = primary_content

                for lang, content in other_contents:
                    # 移除次要语言内容中的 metadata（YAML front matter）
                    lines = content.split('\n')
                    if lines and lines[0].strip() == '---':
                        # 找到第二个 ---
                        end_idx = 1
                        for i in range(1, len(lines)):
                            if lines[i].strip() == '---':
                                end_idx = i + 1
                                break
                        # 跳过 metadata
                        content = '\n'.join(lines[end_idx:]).strip()

                    # 移除内容末尾的分隔线
                    content = self._remove_trailing_separator(content)

                    # 添加分隔符和次要语言内容
                    merged_content += f"\n\n---\n\n"
                    merged_content += content

                # 写入合并后的文件到最终目录
                output_file = safe_output_path(output_dir, rel_path)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(merged_content)

                merged_count += 1
            else:
                # 没有其他语言，直接复制主语言文件
                output_file = safe_output_path(output_dir, rel_path)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                import shutil
                shutil.copy2(primary_file, output_file)
                merged_count += 1

        return merged_count
