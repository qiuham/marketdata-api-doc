#!/usr/bin/env python3
"""Content checks: does each page's body belong to its source_url?

Two signals, both cheap and tolerant:

1. Duplicate body: several files with different source_url but the same body. This is what a
   crawler that reads the wrong browser tab (or a stale page) produces.
2. Title vs URL: the page's first H1 shares no word with the last URL segment (or the #anchor).
   Only checked when the title has Latin letters; Chinese-only titles are skipped.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

_LANG_SEGMENTS = {"en", "zh", "zh-cn", "zh_cn", "zh-hans", "cn", "ja", "ko", "en-us"}
_STOPWORDS = {
    "a", "an", "and", "the", "of", "for", "to", "in", "on", "by", "with", "or", "via",
    "api", "apis", "doc", "docs", "md", "html", "index", "v1", "v2", "v3", "v4", "v5",
    "get", "post", "put", "delete", "new", "is", "my", "all",
}
# Page names that say nothing about the content; for these the parent URL segment is used too.
_GENERIC = {"introduction", "intro", "overview", "reference", "home", "readme", "ws", "rest", "http"}


@dataclass
class PageIssue:
    path: Path
    source_url: str
    title: str
    reason: str


def _split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    meta: dict[str, str] = {}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end < 0:
        return meta, text
    for line in text[3:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip("'\"")
    return meta, text[end + 4:]


def _first_h1(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _url_key(url: str) -> str:
    parts = urlsplit(url)
    if parts.fragment:
        return unquote(parts.fragment)
    segments = [unquote(s) for s in parts.path.split("/") if s]
    while segments and segments[-1].lower() in _LANG_SEGMENTS:
        segments.pop()
    if not segments:
        return ""
    key = segments[-1]
    if len(segments) > 1 and _tokens(key) <= _GENERIC:
        key = f"{segments[-2]} {key}"
    return key


def _tokens(text: str) -> set[str]:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)  # camelCase -> camel Case
    words = re.split(r"[^A-Za-z0-9]+", text.lower())
    out = set()
    for word in words:
        if len(word) < 2 or word in _STOPWORDS:
            continue
        word = "websocket" if word == "ws" else word
        out.add(word[:-1] if len(word) > 3 and word.endswith("s") else word)
    return out


def _squash(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def title_matches_url(title: str, url: str) -> bool:
    """True when the title and the URL page name plausibly name the same page."""
    if not re.search(r"[A-Za-z]", title):
        return True  # non-Latin title: cannot compare, do not flag
    key = _url_key(url)
    if not key:
        return True
    title_tokens, key_tokens = _tokens(title), _tokens(key)
    if not title_tokens or not key_tokens:
        return True
    if title_tokens & key_tokens:
        return True
    # Acronyms such as "er-fix" for "Execution Report".
    initials = "".join(w[0] for w in re.split(r"[^A-Za-z0-9]+", title.lower()) if w)
    if any(len(k) >= 2 and k in initials for k in key_tokens):
        return True
    # Prefix match catches abbreviations such as "auth" / "Authentication".
    for t in title_tokens:
        for k in key_tokens:
            if min(len(t), len(k)) >= 3 and (t.startswith(k) or k.startswith(t)):
                return True
    a, b = _squash(title), _squash(key)
    return bool(a and b and (a in b or b in a))


def _body_fingerprint(body: str) -> str:
    # Only the first language block: bilingual files append other languages after "\n---\n".
    primary = body.split("\n---\n", 1)[0]
    normalized = re.sub(r"\s+", " ", primary).strip()
    if len(normalized) < 200:
        return ""  # too short to be a meaningful duplicate (stubs, redirects)
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()


def check_docs(docs_dir: Path) -> list[PageIssue]:
    issues: list[PageIssue] = []
    by_body: dict[str, list[tuple[Path, str, str]]] = {}
    for path in sorted(docs_dir.rglob("*.md")):
        if path.name == "README.md" and path.parent == docs_dir:
            continue
        meta, body = _split_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        url = meta.get("source_url", "")
        if not url:
            continue
        title = _first_h1(body)
        fp = _body_fingerprint(body)
        if fp:
            by_body.setdefault(fp, []).append((path, url, title))
        if title and not title_matches_url(title, url):
            issues.append(PageIssue(path, url, title, "标题和 URL 对不上"))

    flagged = {i.path for i in issues}
    for group in by_body.values():
        urls = {_strip_lang(u) for _, u, _ in group}
        if len(urls) < 2:
            continue
        for path, url, title in group:
            if path not in flagged:
                issues.append(PageIssue(path, url, title, f"正文和另外 {len(group) - 1} 页相同"))
                flagged.add(path)
    issues.sort(key=lambda i: str(i.path))
    return issues


def _strip_lang(url: str) -> str:
    parts = urlsplit(url)
    segments = [s for s in parts.path.split("/") if s.lower() not in _LANG_SEGMENTS]
    return f"{parts.netloc}/{'/'.join(segments)}#{parts.fragment}"
