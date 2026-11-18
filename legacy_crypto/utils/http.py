#!/usr/bin/env python3
"""
简单的 HTTP 取文本工具：带浏览器 UA、最多试 5 次、429 限流时退避、404 不重试。
代理走标准环境变量（HTTPS_PROXY 等），由调用者在外面设好。
"""
import re
import time
from http.client import IncompleteRead
from typing import Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from loguru import logger as log

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/148.0.0.0 Safari/537.36'
)


def fetch_text(url: str, accept: str = 'text/plain', attempts: int = 5) -> Optional[str]:
    headers = {
        'User-Agent': USER_AGENT,
        'Accept': f'{accept},text/plain;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            with urlopen(Request(url, headers=headers), timeout=30) as response:
                if response.status != 200:
                    # 例如 AWS WAF 返回 202 + 空正文，表示要先过浏览器验证
                    last_error = f'HTTP {response.status}'
                    log.warning(f"请求失败({attempt}/{attempts}): {url} - {last_error}")
                    continue
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
            if exc.code == 429 and attempt < attempts:
                # 限流：按 Retry-After 等，没有就 5、10、20 秒递增
                retry_after = exc.headers.get('Retry-After') if exc.headers else None
                wait = int(retry_after) if retry_after and retry_after.isdigit() else 5 * 2 ** (attempt - 1)
                log.warning(f"限流，{wait} 秒后重试({attempt}/{attempts}): {url}")
                time.sleep(min(wait, 60))
                continue
            log.warning(f"请求失败({attempt}/{attempts}): {url} - {exc}")
        except (URLError, TimeoutError, OSError) as exc:
            last_error = exc
            log.warning(f"请求失败({attempt}/{attempts}): {url} - {exc}")
            time.sleep(2 * attempt)
    log.warning(f"请求最终失败: {url} - {last_error}")
    return None


def looks_like_html(text: str) -> bool:
    return text.lstrip()[:20].lower().startswith(('<!doctype', '<html'))


def strip_llm_preamble(text: str) -> str:
    """去掉 Mintlify 等站点在 .md 页首给 AI 看的“Documentation Index”提示块和自带 frontmatter。"""
    text = text.replace('\r\n', '\n')
    text = re.sub(r'\A\s*> ## Documentation Index\n(?:>.*\n)*\s*', '', text)
    text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.DOTALL)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()
