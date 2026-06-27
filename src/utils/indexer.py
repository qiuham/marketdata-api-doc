#!/usr/bin/env python3
"""Product-level and catalog index generation."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from src.utils.config import dump_json, load_product_configs
from src.utils.markdown import first_heading, split_frontmatter
from src.utils.path_generator import safe_child_path


class DocumentIndexer:
    def __init__(self, project_root: str | Path):
        self.project_root = Path(project_root).resolve()

    def generate_product_index(self, product: dict[str, Any]) -> dict[str, Any]:
        product_id = str(product["id"])
        output = product.get("output", {})
        docs_dir = safe_child_path(self.project_root, output.get("docs_dir", f"docs/{product_id}"))
        index_file = safe_child_path(self.project_root, output.get("index_file", f"index/{product_id}.json"))

        docs = self.scan_documents(docs_dir)
        latest_update = max((str(doc.get("updated_at", "")) for doc in docs), default="")
        grouped: dict[str, list[dict[str, Any]]] = {}
        for doc in docs:
            grouped.setdefault(str(doc.get("api_type") or "other"), []).append(doc)

        provider = product.get("provider", {}) if isinstance(product.get("provider"), dict) else {}
        index_data = {
            "product_id": product_id,
            "display_name": product.get("display_name", product_id),
            "scope": product.get("scope", product.get("market", "")),
            "asset_class": product.get("asset_class", ""),
            "domain": product.get("domain", ""),
            "provider": provider.get("id", ""),
            "provider_name": provider.get("display_name", provider.get("id", "")),
            "product": product.get("product", ""),
            "status": product.get("status", ""),
            "docs_dir": str(docs_dir.relative_to(self.project_root)),
            "total": len(docs),
            "updated_at": latest_update,
            "documents_by_type": grouped,
            "all_documents": sorted(docs, key=lambda item: (str(item.get("api_type", "")), str(item.get("title", "")))),
        }
        dump_json(index_file, index_data)
        return index_data

    def generate_all(self) -> list[dict[str, Any]]:
        products = load_product_configs(self.project_root)
        indexes = [self.generate_product_index(product) for product in products]
        self.generate_catalog(indexes)
        return indexes

    def generate_catalog(self, product_indexes: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        if product_indexes is None:
            product_indexes = []
            for product in load_product_configs(self.project_root):
                index_file = safe_child_path(self.project_root, product.get("output", {}).get("index_file", f"index/{product['id']}.json"))
                if index_file.exists():
                    import json
                    product_indexes.append(json.loads(index_file.read_text(encoding="utf-8")))
        catalog = {
            "total_products": len(product_indexes),
            "total_documents": sum(int(item.get("total", 0)) for item in product_indexes),
            "scopes": sorted({str(item.get("scope", "")) for item in product_indexes if item.get("scope")}),
            "asset_classes": sorted({str(item.get("asset_class", "")) for item in product_indexes if item.get("asset_class")}),
            "products": sorted(product_indexes, key=lambda item: str(item.get("product_id", ""))),
        }
        dump_json(self.project_root / "index" / "catalog.json", catalog)
        return catalog

    def scan_documents(self, docs_dir: Path) -> list[dict[str, Any]]:
        if not docs_dir.exists():
            return []
        documents = []
        for md_file in sorted(docs_dir.glob("**/*.md")):
            metadata, body = split_frontmatter(md_file.read_text(encoding="utf-8"))
            if not metadata:
                continue
            rel_path = md_file.relative_to(self.project_root)
            title = first_heading(body, md_file.stem.replace("-", " ").title())
            documents.append({
                "id": metadata.get("id", md_file.stem),
                "title": title,
                "path": str(rel_path),
                "filename": md_file.name,
                "api_type": metadata.get("api_type", "other"),
                "source_type": metadata.get("source_type", ""),
                "source_url": metadata.get("source_url", ""),
                "doc_category": metadata.get("doc_category", ""),
                "version": metadata.get("version", ""),
                "updated_at": str(metadata.get("updated_at", "")),
            })
        return documents
