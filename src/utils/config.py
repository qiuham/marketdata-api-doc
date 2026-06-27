#!/usr/bin/env python3
"""Configuration loading helpers."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

_SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


def safe_id(value: str, label: str = "id") -> str:
    value = (value or "").strip().lower()
    if not _SAFE_ID.fullmatch(value):
        raise ValueError(f"Invalid {label}: {value!r}")
    return value


def load_config(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    data = load_yaml_text(text)
    if not isinstance(data, dict):
        raise ValueError(f"Config must be a mapping: {path}")
    return data


def load_yaml_text(text: str) -> Any:
    """Load YAML with PyYAML when present, otherwise use a tiny subset parser.

    The fallback intentionally supports only the simple mapping/list syntax used by
    this repository's scaffold configs and frontmatter.
    """
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        return _load_simple_yaml(text)
    return yaml.safe_load(text) or {}


def dump_json(path: str | Path, data: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def iter_product_configs(project_root: str | Path) -> list[Path]:
    config_dir = Path(project_root) / "config" / "products"
    if not config_dir.exists():
        return []
    return sorted(config_dir.glob("*.yaml"))


def load_product_configs(project_root: str | Path) -> list[dict[str, Any]]:
    products = []
    for path in iter_product_configs(project_root):
        data = load_config(path)
        data.setdefault("id", path.stem)
        safe_id(str(data["id"]), "product id")
        products.append(data)
    return sorted(products, key=lambda item: (item.get("priority", 9999), item.get("id", "")))


def _load_simple_yaml(text: str) -> Any:
    root: Any = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    pending: list[tuple[int, dict[str, Any], str]] = []

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        line = raw_line.rstrip()
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        while pending and indent <= pending[-1][0]:
            pending.pop()
        while stack and indent <= stack[-1][0]:
            stack.pop()

        if content.startswith("- "):
            value_text = content[2:].strip()
            parent = stack[-1][1]
            if not isinstance(parent, list):
                if pending:
                    _, owner, key = pending.pop()
                    new_list: list[Any] = []
                    owner[key] = new_list
                    stack.append((indent - 1, new_list))
                    parent = new_list
                else:
                    raise ValueError("List item without list parent")
            parent.append(_parse_scalar(value_text))
            continue

        if ":" not in content:
            raise ValueError(f"Unsupported YAML line: {raw_line}")

        key, value_text = content.split(":", 1)
        key = key.strip()
        value_text = value_text.strip()
        parent = stack[-1][1]
        if not isinstance(parent, dict):
            raise ValueError(f"Mapping item under non-mapping: {raw_line}")

        if value_text == "":
            child: dict[str, Any] = {}
            parent[key] = child
            pending.append((indent, parent, key))
            stack.append((indent, child))
        else:
            parent[key] = _parse_scalar(value_text)

    return root


def _parse_scalar(value: str) -> Any:
    if value in {"''", '""'}:
        return ""
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1]
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if lowered in {"null", "none", "~"}:
        return None
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            pass
    return value
