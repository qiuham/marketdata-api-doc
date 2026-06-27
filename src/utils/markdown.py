#!/usr/bin/env python3
"""Markdown conversion and frontmatter helpers.

The API mirrors the crypto-api-docs MarkdownProcessor, with a small fallback so
metadata-only commands can still run before optional crawler dependencies are installed.
"""
from __future__ import annotations

import re
from datetime import date
from html import unescape
from typing import Any


class MarkdownProcessor:
    """Convert extracted HTML into Markdown and wrap it with frontmatter."""

    def __init__(self):
        try:
            import html2text  # type: ignore
        except ModuleNotFoundError:
            self.converter = None
        else:
            self.converter = html2text.HTML2Text()
            self.converter.ignore_links = False
            self.converter.ignore_images = False
            self.converter.ignore_emphasis = False
            self.converter.body_width = 0
            self.converter.bypass_tables = False
            self.converter.use_automatic_links = True

    def html_to_markdown(self, html: str) -> str:
        if self.converter is not None:
            return self.converter.handle(html)
        return simple_html_to_markdown(html)

    def generate_frontmatter(self, metadata: dict[str, Any]) -> str:
        return generate_frontmatter(metadata)

    def create_document(self, title: str, content: str, metadata: dict[str, Any]) -> str:
        return create_document(title, content, metadata)


def simple_html_to_markdown(html: str) -> str:
    """Tiny best-effort fallback used only when html2text is not installed."""
    text = html
    text = re.sub(r"<\s*h1[^>]*>(.*?)<\s*/\s*h1\s*>", r"# \1\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<\s*h2[^>]*>(.*?)<\s*/\s*h2\s*>", r"## \1\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<\s*h3[^>]*>(.*?)<\s*/\s*h3\s*>", r"### \1\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<\s*br\s*/?\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<\s*/\s*p\s*>", "\n\n", text, flags=re.I)
    text = re.sub(r"<\s*/\s*(li|tr)\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def generate_frontmatter(metadata: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in metadata.items():
        lines.append(f"{key}: {_format_yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines)


def create_document(title: str, body: str, metadata: dict[str, Any]) -> str:
    metadata = dict(metadata)
    metadata.setdefault("updated_at", date.today().isoformat())

    body = _remove_first_h1(body).strip()
    return f"{generate_frontmatter(metadata)}\n\n# {title}\n\n{body}\n"


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    from src.utils.config import load_yaml_text

    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    metadata = load_yaml_text(parts[1]) or {}
    if not isinstance(metadata, dict):
        metadata = {}
    return metadata, parts[2].lstrip("\n")


def first_heading(markdown_body: str, fallback: str) -> str:
    for line in markdown_body.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def sanitize_filename(name: str, max_length: int = 100) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "-", name)
    name = re.sub(r"-+", "-", name)
    return name.lower().strip("-")[:max_length] or "untitled"


def _remove_first_h1(content: str) -> str:
    lines = content.split("\n")
    result = []
    found_first_h1 = False
    for line in lines:
        if not found_first_h1 and re.match(r"^#\s+", line):
            found_first_h1 = True
            continue
        result.append(line)
    return "\n".join(result)


def _format_yaml_scalar(value: Any) -> str:
    if value is None:
        return "''"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or any(ch in text for ch in [":", "#", "'", '"', "\n"]):
        return repr(text)
    return text
