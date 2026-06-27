#!/usr/bin/env python3
"""Safe path generation helpers adapted from crypto-api-docs."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse

_UNSAFE_PATH_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_MULTI_DASHES = re.compile(r"-+")
_WHITESPACE = re.compile(r"\s+")


def sanitize_path_component(value: object, fallback: str = "untitled") -> str:
    component = unquote(str(value or "")).strip()
    component = _UNSAFE_PATH_CHARS.sub("-", component)
    component = _WHITESPACE.sub("-", component)
    component = _MULTI_DASHES.sub("-", component)
    component = component.strip("-. ")
    if not component or component in {".", ".."}:
        return fallback
    return component


def safe_child_path(base_dir: str | Path, relative_path: str | Path) -> Path:
    base = Path(base_dir).resolve()
    target = (base / relative_path).resolve()
    if target != base and base not in target.parents:
        raise ValueError(f"Path escapes base directory: {relative_path}")
    return target


def safe_output_path(output_dir: str | Path, relative_path: str | Path) -> str:
    return str(safe_child_path(output_dir, relative_path))


def url_to_filepath(url: str, base_prefix: Optional[str] = None) -> str:
    path = urlparse(url).path
    if base_prefix:
        prefix_path = urlparse(base_prefix).path
        if path.startswith(prefix_path):
            path = path[len(prefix_path):]
    parts = [
        sanitize_path_component(part)
        for part in path.split("/")
        if part and part not in {".", ".."}
    ]
    filepath = "/".join(parts) or "index"
    if not filepath.endswith(".md"):
        filepath += ".md"
    return filepath


def anchor_to_filepath(anchor_id: str, separator: str = "-", max_depth: int = 3) -> str:
    if not anchor_id:
        return "index.md"
    parts = [
        sanitize_path_component(part)
        for part in anchor_id.split(separator)
        if part and part not in {".", ".."}
    ]
    if not parts:
        return "index.md"
    if len(parts) == 1:
        return f"{parts[0]}.md"
    if len(parts) <= max_depth:
        dirs = parts[:-1]
        filename = parts[-1]
    else:
        dirs = parts[: max_depth - 1]
        filename = separator.join(parts[max_depth - 1 :])
    return f"{'/'.join(dirs)}/{filename}.md" if dirs else f"{filename}.md"


def slugify(value: str, max_length: int = 80) -> str:
    return slugify_title(value, max_length=max_length)


def slugify_title(title: str, max_length: int = 50) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s\-\u4e00-\u9fff]", "", slug)
    slug = re.sub(r"[\s\-]+", "-", slug).strip("-")
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip("-")
    return slug or "untitled"


def is_hash_anchor(anchor_id: str) -> bool:
    return bool(re.match(r"^[a-f0-9]{10}$", anchor_id))


def deduplicate_filepath(filepath: str, existing_files: set[str]) -> str:
    if filepath not in existing_files:
        return filepath
    path = Path(filepath)
    stem = path.stem
    suffix = path.suffix or ".md"
    parent = str(path.parent)
    for counter in range(2, 10000):
        candidate_name = f"{stem}-{counter}{suffix}"
        candidate = candidate_name if parent == "." else f"{parent}/{candidate_name}"
        if candidate not in existing_files:
            return candidate
    raise ValueError(f"Unable to deduplicate path: {filepath}")
