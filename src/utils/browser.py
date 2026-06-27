#!/usr/bin/env python3
"""agent-browser wrapper utilities.

This is adapted from the earlier crypto-api-docs project so crawlers can share
one browser automation interface across XTP, XTP Pro, crypto, and future sources.
"""
from __future__ import annotations

import json
import subprocess
import time
from typing import Any


class BrowserManager:
    """Small wrapper around the agent-browser CLI."""

    def __init__(self, session_name: str):
        self.session = session_name

    def _run_command(self, cmd: list[str], timeout: int = 30) -> subprocess.CompletedProcess[str]:
        full_cmd = ["agent-browser", "--session", self.session] + cmd
        try:
            return subprocess.run(full_cmd, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired as exc:
            return subprocess.CompletedProcess(
                full_cmd,
                returncode=124,
                stdout=exc.stdout or "",
                stderr=exc.stderr or f"Command timed out after {timeout}s",
            )

    def open(self, url: str, wait: float = 3) -> bool:
        result = self._run_command(["open", url], timeout=30)
        if result.returncode == 0:
            time.sleep(wait)
            return True
        return False

    def eval_js(self, js_code: str, return_json: bool = True, timeout: int = 30) -> Any | None:
        cmd = ["eval", js_code]
        if return_json:
            cmd.append("--json")
        result = self._run_command(cmd, timeout=timeout)
        if result.returncode != 0:
            return None
        if not return_json:
            return result.stdout
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            return None
        if data.get("success"):
            return data.get("data", {}).get("result")
        return None

    def set_headers(self, headers: dict[str, str]) -> bool:
        result = self._run_command(["set", "headers", json.dumps(headers, ensure_ascii=False)], timeout=10)
        return result.returncode == 0

    def get_links(self, selector: str, filter_func: str | None = None) -> list[str]:
        selector_js = json.dumps(selector)
        js = f"""
        Array.from(document.querySelectorAll({selector_js}))
            .map(a => a.href)
            .filter(href => href && {filter_func if filter_func else "true"})
        """
        result = self.eval_js(js)
        return result if isinstance(result, list) else []

    def extract_content(self, selector: str) -> str | None:
        selector_js = json.dumps(selector)
        js = f"""
        (function() {{
            const element = document.querySelector({selector_js});
            return element ? element.innerHTML : null;
        }})()
        """
        result = self.eval_js(js)
        return result if isinstance(result, str) else None

    def count_elements(self, selector: str) -> int:
        selector_js = json.dumps(selector)
        result = self.eval_js(f"document.querySelectorAll({selector_js}).length")
        return int(result) if result is not None else 0

    def click_all(self, selector: str) -> int:
        selector_js = json.dumps(selector)
        js = f"""
        const elements = document.querySelectorAll({selector_js});
        let clicked = 0;
        elements.forEach(el => {{
            try {{
                el.click();
                clicked++;
            }} catch(e) {{}}
        }});
        clicked;
        """
        result = self.eval_js(js)
        return int(result) if result is not None else 0

    def wait_for_element(self, selector: str = "main", timeout: int = 30) -> bool:
        result = self._run_command(["wait", selector], timeout=timeout)
        return result.returncode == 0

    def tab_new(self) -> bool:
        return self._run_command(["tab", "new"], timeout=10).returncode == 0

    def tab_switch(self, index: int) -> bool:
        return self._run_command(["tab", str(index)], timeout=10).returncode == 0

    def tab_list(self) -> list[dict[str, Any]]:
        result = self._run_command(["tab", "list"], timeout=10)
        tabs = []
        for line in result.stdout.strip().split("\n"):
            if "[" not in line or "]" not in line:
                continue
            tabs.append({
                "active": line.strip().startswith("->") or line.strip().startswith("→"),
                "index": int(line.split("[")[1].split("]")[0]),
            })
        return tabs

    def tab_close(self, index: int | None = None) -> bool:
        cmd = ["tab", "close"]
        if index is not None:
            cmd.append(str(index))
        return self._run_command(cmd, timeout=10).returncode == 0

    def open_tabs_batch(self, count: int) -> None:
        for _ in range(count):
            self.tab_new()

    def load_urls_batch(self, urls: list[str], start_tab: int = 0) -> None:
        for offset, url in enumerate(urls):
            self.tab_switch(start_tab + offset)
            self.open(url, wait=0)

    def close_tabs_batch(self, start: int, count: int) -> None:
        for _ in range(count):
            self.tab_close(start)
