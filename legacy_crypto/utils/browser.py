#!/usr/bin/env python3
"""
agent-browser 封装工具
"""
import os
import subprocess
import json
import time
from typing import List, Dict, Any, Optional


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/140.0.0.0 Safari/537.36"
)


class BrowserManager:
    """agent-browser 管理器"""

    def __init__(self, session_name: str):
        self.session = session_name

    def _run_command(self, cmd: List[str], timeout: int = 30) -> subprocess.CompletedProcess:
        """执行 agent-browser 命令"""
        full_cmd = ['agent-browser', '--session', self.session] + cmd
        # 默认的 HeadlessChrome 标识会被 Gate 的 Akamai 防火墙拒绝（Access Denied），换成普通桌面 Chrome。
        # 只在浏览器启动时生效；环境变量里已经设了就用设的。
        env = dict(os.environ)
        env.setdefault('AGENT_BROWSER_USER_AGENT', DEFAULT_USER_AGENT)
        try:
            return subprocess.run(
                full_cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                env=env,
            )
        except subprocess.TimeoutExpired as e:
            return subprocess.CompletedProcess(
                full_cmd,
                returncode=124,
                stdout=e.stdout or "",
                stderr=e.stderr or f"Command timed out after {timeout}s"
            )

    def open(self, url: str, wait: int = 3) -> bool:
        """打开URL"""
        for attempt in range(3):  # 第一次打开要先启动浏览器，偶尔超时；失败再试两次
            result = self._run_command(['open', url], timeout=45)
            if result.returncode == 0:
                time.sleep(wait)
                return True
            time.sleep(2 + attempt * 3)
        return False

    def eval_js(self, js_code: str, return_json: bool = True, timeout: int = 30) -> Optional[Any]:
        """执行JavaScript代码"""
        cmd = ['eval', js_code]
        if return_json:
            cmd.append('--json')

        result = self._run_command(cmd, timeout=timeout)

        if result.returncode != 0:
            return None

        if return_json:
            try:
                data = json.loads(result.stdout)
                if data.get('success'):
                    return data.get('data', {}).get('result')
            except json.JSONDecodeError:
                return None
        else:
            return result.stdout

        return None

    def get_links(self, selector: str, filter_func: Optional[str] = None) -> List[str]:
        """获取所有匹配选择器的链接"""
        selector_js = json.dumps(selector)
        js = f'''
        Array.from(document.querySelectorAll({selector_js}))
            .map(a => a.href)
            .filter(href => href && {filter_func if filter_func else "true"})
        '''

        result = self.eval_js(js)
        return result if result else []

    def extract_content(self, selector: str) -> Optional[str]:
        """提取HTML内容"""
        selector_js = json.dumps(selector)
        js = f'''
        (function() {{
            const element = document.querySelector({selector_js});
            return element ? element.innerHTML : null;
        }})()
        '''

        return self.eval_js(js)

    def count_elements(self, selector: str) -> int:
        """统计元素数量"""
        selector_js = json.dumps(selector)
        js = f'document.querySelectorAll({selector_js}).length'
        result = self.eval_js(js)
        return result if result is not None else 0

    def click_all(self, selector: str) -> int:
        """点击所有匹配的元素"""
        selector_js = json.dumps(selector)
        js = f'''
        const elements = document.querySelectorAll({selector_js});
        let clicked = 0;
        elements.forEach(el => {{
            try {{
                el.click();
                clicked++;
            }} catch(e) {{}}
        }});
        clicked;
        '''

        result = self.eval_js(js)
        return result if result is not None else 0

    def tab_new(self) -> bool:
        """打开新标签页"""
        result = self._run_command(['tab', 'new'], timeout=10)
        return result.returncode == 0

    def tab_switch(self, index: int) -> bool:
        """切换到第 index 个标签页（从 0 数）。

        agent-browser 的标签页编号是 t1、t2 这种，关掉的编号不再复用，所以按位置查出编号再切。
        切不过去就抛异常：静默失败会让几个网址都在同一个标签页里打开，内容存进错的文件。
        """
        tabs = self.tab_list()
        for _ in range(3):  # 标签页加载中时列表偶尔暂时变短，等一下再查
            if index < len(tabs):
                break
            time.sleep(1)
            tabs = self.tab_list()
        if index >= len(tabs):
            self.ensure_tabs(index + 1)  # 真的少了就补开
            tabs = self.tab_list()
        if index >= len(tabs):
            raise RuntimeError(f"标签页不存在: 第 {index} 个（共 {len(tabs)} 个）")
        result = self._run_command(['tab', tabs[index]['id']], timeout=10)
        if result.returncode != 0:
            raise RuntimeError(f"切换标签页失败: {tabs[index]['id']} {result.stderr.strip()}")
        return True

    def tab_list(self) -> List[Dict[str, Any]]:
        """列出所有标签页，按打开顺序：[{index, id, active, url}]"""
        for attempt in range(3):  # 浏览器忙时偶尔超过 10 秒，重试
            result = self._run_command(['tab', 'list', '--json'], timeout=30)
            try:
                data = json.loads(result.stdout)
                break
            except json.JSONDecodeError:
                time.sleep(2)
        else:
            raise RuntimeError(f"读不了标签页列表: {result.stdout[:200]} {result.stderr[:200]}")
        tabs = [t for t in (data.get('data') or {}).get('tabs', []) if t.get('type', 'page') == 'page']
        return [{'index': i, 'id': t['tabId'], 'active': t.get('active', False), 'url': t.get('url', '')}
                for i, t in enumerate(tabs)]

    def current_url(self) -> str:
        """当前标签页的网址"""
        return self.eval_js('window.location.href') or ''

    @staticmethod
    def same_page(a: str, b: str) -> bool:
        """两个网址是不是同一页（不看 #锚点、末尾斜杠）"""
        norm = lambda u: (u or '').split('#')[0].rstrip('/')
        return norm(a) == norm(b)

    def ensure_page(self, url: str, selector: str, timeout: int = 30) -> None:
        """确认当前标签页就是 url 这一页并且加载完了；不是就在本标签页重开一次，还不是就抛异常。

        用在多标签页并发爬取里：存盘前核对，防止把别的页存进这个文件。带 #锚点的网址（同一页的不同章节）
        只核对锚点前的部分。
        """
        for attempt in range(2):
            if attempt == 1:
                self.open(url, wait=2)
            if not self.wait_for_element(selector, timeout=timeout):
                continue
            if self.same_page(self.current_url(), url):
                return
        raise RuntimeError(f"页面不对: 要 {url}，实际 {self.current_url()}")

    def tab_close(self, index: int = None) -> bool:
        """关闭标签页（不指定则关闭当前）"""
        cmd = ['tab', 'close']
        if index is not None:
            cmd.append(str(index))
        result = self._run_command(cmd, timeout=10)
        return result.returncode == 0

    def ensure_tabs(self, count: int):
        """标签页不够 count 个就补开"""
        for _ in range(count - len(self.tab_list())):
            self.tab_new()

    def open_tabs_batch(self, count: int):
        """批量创建N个空白标签"""
        for i in range(count):
            self.tab_new()

    def load_urls_batch(self, urls: List[str], start_tab: int = 0):
        """批量在标签页中加载URLs（并行加载）"""
        for i, url in enumerate(urls):
            self.tab_switch(start_tab + i)
            # 打开失败不在这里停：取内容前 ensure_page 会核对、重开
            self.open(url, wait=0)

    def close_tabs_batch(self, start: int, count: int):
        """批量关闭标签（从start开始关闭count个）"""
        for i in range(count):
            self.tab_close(start)

    def wait_for_element(self, selector: str = 'main', timeout: int = 30) -> bool:
        """等待元素出现"""
        try:
            result = self._run_command(['wait', selector], timeout=timeout)
            return result.returncode == 0
        except Exception:
            return False
