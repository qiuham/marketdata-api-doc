#!/usr/bin/env python3
"""
agent-browser 封装工具
"""
import subprocess
import json
import time
from typing import List, Dict, Any, Optional
from urllib.parse import unquote, urlsplit


def same_page(a: str, b: str) -> bool:
    """两个 URL 是否指同一页（忽略 #锚点、末尾斜杠、大小写的域名）"""
    def norm(u: str) -> tuple:
        p = urlsplit(u or '')
        return (p.netloc.lower(), unquote(p.path).rstrip('/'), p.query)
    return norm(a) == norm(b)


class BrowserManager:
    """agent-browser 管理器"""

    def __init__(self, session_name: str):
        self.session = session_name
        # 标签的稳定编号，按创建顺序。新版 agent-browser 只认 t1、t2 这类编号，不认 0、1、2。
        self._tab_ids: List[str] = []

    def _run_command(self, cmd: List[str], timeout: int = 30) -> subprocess.CompletedProcess:
        """执行 agent-browser 命令"""
        full_cmd = ['agent-browser', '--session', self.session] + cmd
        try:
            return subprocess.run(
                full_cmd,
                capture_output=True,
                text=True,
                timeout=timeout
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
        result = self._run_command(['open', url], timeout=30)
        if result.returncode == 0:
            time.sleep(wait)
            return True
        return False

    def eval_js(self, js_code: str, return_json: bool = True) -> Optional[Any]:
        """执行JavaScript代码"""
        cmd = ['eval', js_code]
        if return_json:
            cmd.append('--json')

        result = self._run_command(cmd, timeout=30)

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
        """切换到第 index 个标签页（从 0 数，按创建顺序）"""
        if index >= len(self._tab_ids):
            self._tab_ids = [t['id'] for t in self.tab_list()]
        if index >= len(self._tab_ids):
            return False
        result = self._run_command(['tab', self._tab_ids[index]], timeout=10)
        return result.returncode == 0

    def tab_list(self) -> List[Dict[str, Any]]:
        """列出所有标签页"""
        result = self._run_command(['tab', 'list'], timeout=10)
        # 解析输出，旧版：→ [0] Title - URL；新版：→ [t1] Title - URL
        tabs = []
        for line in result.stdout.strip().split('\n'):
            if '[' in line and ']' in line:
                tab_id = line.split('[')[1].split(']')[0].strip()
                tabs.append({
                    'active': line.strip().startswith('→'),
                    'index': len(tabs),
                    'id': tab_id,
                })
        return tabs

    def tab_close(self, index: int = None) -> bool:
        """关闭标签页（不指定则关闭当前）"""
        cmd = ['tab', 'close']
        if index is not None:
            cmd.append(str(index))
        result = self._run_command(cmd, timeout=10)
        return result.returncode == 0

    def open_tabs_batch(self, count: int):
        """批量创建N个空白标签"""
        for i in range(count):
            self.tab_new()
        self._tab_ids = [t['id'] for t in self.tab_list()]

    def load_urls_batch(self, urls: List[str], start_tab: int = 0):
        """批量在标签页中加载URLs（并行加载）"""
        for i, url in enumerate(urls):
            if not self.tab_switch(start_tab + i):
                raise RuntimeError(f"切换到第 {start_tab + i} 个标签失败")
            self.open(url, wait=0)

    def close_tabs_batch(self, start: int, count: int):
        """批量关闭标签（从start开始关闭count个）"""
        for i in range(count):
            self.tab_close(start)
        self._tab_ids = []

    def current_url(self) -> str:
        return self.eval_js('window.location.href') or ''

    def ensure_page(self, url: str, ready_selector: str = 'main', timeout: int = 30) -> str:
        """确认当前标签显示的是 url 这一页，返回实际地址。

        并发抓取时，标签里可能还是上一批的旧页，或者标签没切过去。
        如果等到超时地址还对不上，就在当前标签重新打开 url；
        重开后地址仍不同，说明网站做了跳转，返回跳转后的地址。
        """
        ready_js = f'!!document.querySelector({json.dumps(ready_selector)})'
        deadline = time.time() + timeout
        while time.time() < deadline:
            if same_page(self.current_url(), url) and self.eval_js(ready_js):
                return self.current_url()
            time.sleep(0.5)
        if not self.open(url, wait=2):
            raise RuntimeError(f"打开页面失败: {url}")
        self.wait_for_element(ready_selector, timeout=timeout)
        actual = self.current_url()
        if not actual:
            raise RuntimeError(f"读不到当前页地址: {url}")
        return actual

    def wait_for_element(self, selector: str = 'main', timeout: int = 30) -> bool:
        """等待元素出现"""
        try:
            result = self._run_command(['wait', selector], timeout=timeout)
            return result.returncode == 0
        except Exception:
            return False
