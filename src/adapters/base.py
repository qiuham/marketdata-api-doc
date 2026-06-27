#!/usr/bin/env python3
"""Adapter base classes for document sources."""
from __future__ import annotations

import shutil
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Type

from src.utils.markdown import MarkdownProcessor
from src.utils.path_generator import safe_child_path, slugify_title


@dataclass
class DocumentPage:
    title: str
    content: str
    metadata: dict[str, Any]
    relative_path: str = ""
    source_url: str = ""
    source_file: str = ""


_ADAPTER_REGISTRY: dict[str, Type["ProductAdapter"]] = {}


def register_adapter(name: str):
    def decorator(cls: Type["ProductAdapter"]) -> Type["ProductAdapter"]:
        _ADAPTER_REGISTRY[name] = cls
        return cls
    return decorator


def get_adapter(config: dict[str, Any]) -> "ProductAdapter":
    adapter_name = config.get("adapter") or config.get("id")
    if adapter_name not in _ADAPTER_REGISTRY:
        available = ", ".join(sorted(_ADAPTER_REGISTRY)) or "none"
        raise NotImplementedError(f"Adapter not registered: {adapter_name}. Available: {available}")
    return _ADAPTER_REGISTRY[str(adapter_name)](config)


class ProductAdapter(ABC):
    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.product_id = str(config.get("id", ""))
        self.markdown = MarkdownProcessor()

    @abstractmethod
    def discover(self) -> list[Any]:
        """Return source document descriptors or URLs."""
        raise NotImplementedError

    @abstractmethod
    def extract(self, source: Any) -> DocumentPage:
        """Extract one source into a normalized Markdown page."""
        raise NotImplementedError

    def crawl(self, project_root: str | Path, limit: int | None = None) -> list[Path]:
        project_root = Path(project_root).resolve()
        output_dir = self.output_dir(project_root)
        if self.config.get("output", {}).get("clean_before_crawl", False):
            self._clean_output_dir(project_root, output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        sources = self.discover()
        if limit is not None:
            sources = sources[:limit]

        written: list[Path] = []
        used_paths: set[str] = set()
        for source in sources:
            page = self.extract(source)
            relative_path = page.relative_path or f"{slugify_title(page.title)}.md"
            relative_path = self._dedupe(relative_path, used_paths)
            used_paths.add(relative_path)
            target = safe_child_path(output_dir, relative_path)
            target.parent.mkdir(parents=True, exist_ok=True)
            metadata = dict(page.metadata)
            if page.source_url and not metadata.get("source_url"):
                metadata["source_url"] = page.source_url
            if page.source_file and not metadata.get("source_file"):
                metadata["source_file"] = page.source_file
            target.write_text(self.markdown.create_document(page.title, page.content, metadata), encoding="utf-8")
            written.append(target)
        return written

    def output_dir(self, project_root: str | Path) -> Path:
        return safe_child_path(project_root, self.config.get("output", {}).get("docs_dir", f"docs/{self.product_id}"))

    def metadata_defaults(self) -> dict[str, Any]:
        provider = self.config.get("provider", {}) if isinstance(self.config.get("provider"), dict) else {}
        defaults = dict(self.config.get("metadata_defaults", {}))
        defaults.update({
            "scope": self.config.get("scope", self.config.get("market", "")),
            "asset_class": self.config.get("asset_class", ""),
            "domain": self.config.get("domain", ""),
            "provider": provider.get("id", ""),
            "provider_name": provider.get("display_name", ""),
            "product": self.config.get("product", ""),
            "product_id": self.product_id,
        })
        return defaults

    def _clean_output_dir(self, project_root: Path, output_dir: Path) -> None:
        docs_root = (project_root / "docs").resolve()
        output_dir = output_dir.resolve()
        if output_dir.exists():
            if docs_root not in output_dir.parents:
                raise ValueError(f"Refuse to clean non-docs output directory: {output_dir}")
            shutil.rmtree(output_dir)

    def _dedupe(self, relative_path: str, used_paths: set[str]) -> str:
        if relative_path not in used_paths:
            return relative_path
        path = Path(relative_path)
        parent = "" if str(path.parent) == "." else f"{path.parent}/"
        for counter in range(2, 10000):
            candidate = f"{parent}{path.stem}-{counter}{path.suffix or '.md'}"
            if candidate not in used_paths:
                return candidate
        raise ValueError(f"Unable to dedupe path: {relative_path}")
