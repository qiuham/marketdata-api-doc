#!/usr/bin/env python3
"""
agent-browser 封装工具
"""
import subprocess
import json
import time
from typing import List, Dict, Any, Optional


class BrowserManager:
    """agent-browser 管理器"""

    def __init__(self, session_name: str):
        self.session = session_name

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
        """切换到指定标签页"""
        result = self._run_command(['tab', str(index)], timeout=10)
        return result.returncode == 0

    def tab_list(self) -> List[Dict[str, Any]]:
        """列出所有标签页"""
        result = self._run_command(['tab', 'list'], timeout=10)
        # 解析输出，格式：→ [0] Title - URL
        tabs = []
        for line in result.stdout.strip().split('\n'):
            if '[' in line and ']' in line:
                tabs.append({
                    'active': line.strip().startswith('→'),
                    'index': int(line.split('[')[1].split(']')[0]),
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

    def load_urls_batch(self, urls: List[str], start_tab: int = 0):
        """批量在标签页中加载URLs（并行加载）"""
        for i, url in enumerate(urls):
            self.tab_switch(start_tab + i)
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
