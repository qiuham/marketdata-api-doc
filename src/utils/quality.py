#!/usr/bin/env python3
"""Sanity checks for crawled docs: catch broken crawls before they are committed.

Two failure shapes seen in practice:
- empty pages (`# Untitled`, no body): the page never loaded;
- the same body saved under several file names: a multi-tab crawler read the wrong tab.
"""
from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from pathlib import Path

MIN_BODY = 40
MAX_EMPTY_RATIO = 0.05
MAX_DUPLICATE_RATIO = 0.02
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def check_docs_dir(docs_dir: Path) -> list[str]:
    """Return problems found in one product's docs directory (empty list = looks fine)."""
    files = sorted(docs_dir.glob("**/*.md")) if docs_dir.exists() else []
    if not files:
        return [f"{docs_dir}: no documents"]
    untitled: list[str] = []
    empty = 0
    by_body: dict[str, list[str]] = defaultdict(list)
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        body = FRONTMATTER.sub("", text, count=1)
        if re.search(r"^# Untitled\s*$", body, re.M):
            untitled.append(str(path))
        content = re.sub(r"^# .*$", "", body, count=1, flags=re.M).strip()
        if len(content) < MIN_BODY:
            empty += 1
            continue
        by_body[hashlib.sha256(content.encode()).hexdigest()].append(str(path))

    problems: list[str] = []
    total = len(files)
    if untitled:
        problems.append(f"{docs_dir}: {len(untitled)} pages titled 'Untitled', e.g. {untitled[0]}")
    if empty / total > MAX_EMPTY_RATIO:
        problems.append(f"{docs_dir}: {empty}/{total} pages are empty")
    duplicated = [group for group in by_body.values() if len(group) > 1]
    duplicated_files = sum(len(group) for group in duplicated)
    if duplicated_files / total > MAX_DUPLICATE_RATIO:
        problems.append(
            f"{docs_dir}: {duplicated_files}/{total} files share a body with another file "
            f"({len(duplicated)} groups), e.g. {duplicated[0][:3]}"
        )
    return problems
