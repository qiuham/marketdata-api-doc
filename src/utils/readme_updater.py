#!/usr/bin/env python3
"""README generated-section updater."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from src.utils.config import load_product_configs


class ReadmeUpdater:
    def __init__(self, project_root: str | Path):
        self.project_root = Path(project_root).resolve()
        self.readme_path = self.project_root / "README.md"

    def update(self) -> str:
        content = self.readme_path.read_text(encoding="utf-8")
        products = load_product_configs(self.project_root)
        content = self._replace_section(content, "覆盖范围", self._coverage_section(products))
        content = self._replace_section(content, "项目结构", self._structure_section(products))
        self.readme_path.write_text(content, encoding="utf-8")
        return str(self.readme_path)

    def _coverage_section(self, products: list[dict[str, Any]]) -> str:
        lines = [
            "> 此表由 `src/utils/readme_updater.py` 根据 `config/products/*.yaml` 和 `index/**/*.json` 自动生成。",
            "",
            "| 范围 | 资产 | 业务域 | 提供方 | 产品 | 状态 | 文档数量 | 最后更新 |",
            "|------|------|--------|--------|------|------|----------|----------|",
        ]
        for product in products:
            index_data = self._load_index(product)
            output = product.get("output", {})
            docs_dir = output.get("docs_dir", "")
            provider = product.get("provider", {}) if isinstance(product.get("provider"), dict) else {}
            status = self._status_icon(str(product.get("status", "")))
            total = index_data.get("total", "-") if index_data else "-"
            updated_at = index_data.get("updated_at", "-") if index_data else "-"
            display_name = product.get("display_name", product.get("id", ""))
            product_link = f"[{display_name}](./{docs_dir}/)" if docs_dir else str(display_name)
            lines.append(
                f"| {product.get('scope', product.get('market', ''))} | {product.get('asset_class', '')} | "
                f"{product.get('domain', '')} | {provider.get('display_name', provider.get('id', ''))} | "
                f"{product_link} | {status} | {total} | {updated_at or '-'} |"
            )
        return "\n".join(lines)

    def _structure_section(self, products: list[dict[str, Any]]) -> str:
        lines = [
            "> 此结构由 `src/utils/readme_updater.py` 根据当前仓库文件自动生成。",
            "",
            "```",
            "marketdata-api-doc/",
        ]
        workflows = self._list_files(self.project_root / ".github" / "workflows", "*.yml")
        if workflows:
            lines.extend(["├── .github/", "│   └── workflows/        # GitHub Actions"])
            self._append_tree(lines, workflows, "│       ")

        lines.extend(["├── config/", "│   ├── scopes/           # cn / us / crypto 等顶层范围"])
        self._append_tree(lines, self._list_files(self.project_root / "config" / "scopes", "*.yaml"), "│   │   ")
        lines.append("│   └── products/         # 接入产品配置")
        self._append_tree(lines, self._list_files(self.project_root / "config" / "products", "*.yaml"), "│       ")

        lines.append("├── docs/                 # Markdown 文档")
        self._append_docs_tree(lines, products)

        lines.append("├── index/                # JSON 索引（供 AI 读取）")
        self._append_index_tree(lines)

        lines.extend(["├── src/", "│   ├── adapters/         # 采集/导入适配器"])
        self._append_tree(lines, self._ordered_py_files(self.project_root / "src" / "adapters"), "│   │   ")
        lines.append("│   ├── utils/            # 浏览器、Markdown、索引、路径、README 工具")
        self._append_tree(lines, self._ordered_py_files(self.project_root / "src" / "utils"), "│   │   ")
        lines.append("│   └── main.py")
        if (self.project_root / "requirements.txt").exists():
            lines.append("├── requirements.txt")
        lines.extend(["└── README.md", "```"])
        return "\n".join(lines)

    def _append_docs_tree(self, lines: list[str], products: list[dict[str, Any]]) -> None:
        grouped: dict[str, dict[str, dict[str, dict[str, list[dict[str, Any]]]]]] = {}
        for product in products:
            scope = str(product.get("scope", product.get("market", "unknown")))
            asset = str(product.get("asset_class", "unknown"))
            domain = str(product.get("domain", "unknown"))
            provider = product.get("provider", {}) if isinstance(product.get("provider"), dict) else {}
            provider_id = str(provider.get("id", "unknown"))
            grouped.setdefault(scope, {}).setdefault(asset, {}).setdefault(domain, {}).setdefault(provider_id, []).append(product)

        for scope in sorted(grouped):
            lines.append(f"│   ├── {scope}/")
            for asset in sorted(grouped[scope]):
                lines.append(f"│   │   ├── {asset}/")
                for domain in sorted(grouped[scope][asset]):
                    lines.append(f"│   │   │   ├── {domain}/")
                    for provider_id in sorted(grouped[scope][asset][domain]):
                        lines.append(f"│   │   │   │   ├── {provider_id}/")
                        products_for_provider = grouped[scope][asset][domain][provider_id]
                        for index, product in enumerate(products_for_provider):
                            connector = "└──" if index == len(products_for_provider) - 1 else "├──"
                            index_data = self._load_index(product)
                            total = index_data.get("total", "-") if index_data else "-"
                            lines.append(
                                f"│   │   │   │       {connector} {product.get('product', product.get('id'))}/".ljust(52)
                                + f"# {total} Markdown docs"
                            )
        for extra in ["us", "crypto"]:
            if extra not in grouped and (self.project_root / "docs" / extra).exists():
                lines.append(f"│   ├── {extra}/")

    def _append_index_tree(self, lines: list[str]) -> None:
        index_root = self.project_root / "index"
        if not index_root.exists():
            return
        entries = []
        if (index_root / "catalog.json").exists():
            entries.append("catalog.json")
        for path in sorted(index_root.glob("**/*.json")):
            if path.name == "catalog.json":
                continue
            entries.append(str(path.relative_to(index_root)))
        self._append_tree(lines, entries, "│   ")

    def _load_index(self, product: dict[str, Any]) -> dict[str, Any]:
        index_file = self.project_root / product.get("output", {}).get("index_file", "")
        if not index_file.exists():
            return {}
        try:
            return json.loads(index_file.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def _status_icon(self, status: str) -> str:
        return {
            "active": "✅",
            "scaffold": "🧱",
            "planned": "🔜",
            "deprecated": "⚠️",
        }.get(status, status or "-")

    def _replace_section(self, content: str, heading: str, body: str) -> str:
        pattern = rf"(## {re.escape(heading)}\n\n)(.*?)(?=\n\n## |\Z)"
        return re.sub(pattern, lambda match: f"{match.group(1)}{body}", content, flags=re.DOTALL)

    def _list_files(self, directory: Path, pattern: str) -> list[str]:
        if not directory.exists():
            return []
        return sorted(path.name for path in directory.glob(pattern) if path.is_file())

    def _ordered_py_files(self, directory: Path) -> list[str]:
        priority = {"__init__.py": 0, "base.py": 1}
        return sorted(self._list_files(directory, "*.py"), key=lambda name: (priority.get(name, 2), name))

    def _append_tree(self, lines: list[str], entries: list[str], prefix: str) -> None:
        for index, entry in enumerate(entries):
            connector = "└──" if index == len(entries) - 1 else "├──"
            lines.append(f"{prefix}{connector} {entry}")
