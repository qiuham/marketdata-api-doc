#!/usr/bin/env python3
"""MarketData API docs command line entrypoint."""
from __future__ import annotations

import argparse
import subprocess
import sys
import traceback
from pathlib import Path

from src.utils.config import load_product_configs, safe_id
from src.utils.indexer import DocumentIndexer
from src.utils.quality import check_docs_dir
from src.utils.readme_updater import ReadmeUpdater
from src.adapters import get_adapter

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _find_product(product_id: str) -> dict:
    product_id = safe_id(product_id, "product id")
    products = load_product_configs(PROJECT_ROOT)
    match = next((product for product in products if product.get("id") == product_id), None)
    if not match:
        raise SystemExit(f"Unknown product: {product_id}")
    return match


def cmd_crawl(args: argparse.Namespace) -> int:
    indexer = DocumentIndexer(PROJECT_ROOT)
    products = load_product_configs(PROJECT_ROOT) if args.all else [_find_product(args.product)]
    total_written = 0
    failed: list[str] = []
    for product in products:
        product_id = product.get("id")
        try:
            adapter = get_adapter(product)
            written = adapter.crawl(PROJECT_ROOT, limit=args.limit)
        except Exception as exc:  # noqa: BLE001 - one broken source must not stop the others
            # Keep this product's existing docs; report it and move on to the next product.
            failed.append(product_id)
            traceback.print_exc()
            print(f"::error title=Crawl failed: {product_id}::{type(exc).__name__}: {exc}")
            continue
        problems = check_docs_dir(PROJECT_ROOT / product.get("output", {}).get("docs_dir", ""))
        if problems:
            # A crawl that produced empty or cross-wired pages must not replace good docs.
            _restore_product(product)
            failed.append(product_id)
            for problem in problems:
                print(f"::error title=Bad crawl: {product_id}::{problem}")
            continue
        data = indexer.generate_product_index(product)
        total_written += len(written)
        print(f"Crawled {product_id}: {len(written)} files, indexed {data['total']} docs")
    indexer.generate_catalog()
    ReadmeUpdater(PROJECT_ROOT).update()
    print(f"Done: {len(products) - len(failed)}/{len(products)} products, {total_written} files")
    if failed:
        print(f"Failed products (existing docs kept): {', '.join(failed)}")
    # Fail the run only when nothing could be crawled, so the other products still get committed.
    return 1 if failed and len(failed) == len(products) else 0


def _restore_product(product: dict) -> None:
    """Put a product's docs and index back to the last commit (drop this run's output)."""
    output = product.get("output", {})
    paths = [p for p in (output.get("docs_dir"), output.get("index_file")) if p]
    tracked = subprocess.run(["git", "ls-files", "--", *paths], cwd=PROJECT_ROOT,
                             capture_output=True, text=True, check=True).stdout.strip()
    if tracked:
        subprocess.run(["git", "checkout", "HEAD", "--", *paths], cwd=PROJECT_ROOT, check=True)
    subprocess.run(["git", "clean", "-fdq", "--", *paths], cwd=PROJECT_ROOT, check=True)
    print(f"Restored {product.get('id')} docs to the last commit")


def cmd_list(_: argparse.Namespace) -> int:
    products = load_product_configs(PROJECT_ROOT)
    if not products:
        print("No products configured.")
        return 0
    print("PRODUCT ID          SCOPE  ASSET      DOMAIN     PROVIDER      STATUS")
    print("-" * 78)
    for product in products:
        provider = product.get("provider", {}) if isinstance(product.get("provider"), dict) else {}
        print(
            f"{product.get('id', ''):<19} "
            f"{product.get('scope', product.get('market', '')):<6} "
            f"{product.get('asset_class', ''):<10} "
            f"{product.get('domain', ''):<10} "
            f"{provider.get('id', ''):<13} "
            f"{product.get('status', '')}"
        )
    return 0


def cmd_index(args: argparse.Namespace) -> int:
    indexer = DocumentIndexer(PROJECT_ROOT)
    products = load_product_configs(PROJECT_ROOT)
    if args.all:
        indexes = indexer.generate_all()
        print(f"Generated {len(indexes)} product indexes and index/catalog.json")
        return 0

    product_id = safe_id(args.product, "product id")
    match = next((product for product in products if product.get("id") == product_id), None)
    if not match:
        raise SystemExit(f"Unknown product: {product_id}")
    data = indexer.generate_product_index(match)
    indexer.generate_catalog()
    print(f"Generated {match.get('output', {}).get('index_file')} ({data['total']} docs)")
    return 0


def cmd_readme(_: argparse.Namespace) -> int:
    path = ReadmeUpdater(PROJECT_ROOT).update()
    print(f"Updated {Path(path).relative_to(PROJECT_ROOT)}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    products = load_product_configs(PROJECT_ROOT)
    errors: list[str] = []
    warnings: list[str] = []
    for product in products:
        output = product.get("output", {})
        docs_dir = PROJECT_ROOT / output.get("docs_dir", "")
        index_file = PROJECT_ROOT / output.get("index_file", "")
        if not docs_dir.exists():
            errors.append(f"Missing docs_dir for {product.get('id')}: {docs_dir.relative_to(PROJECT_ROOT)}")
        if not index_file.exists():
            errors.append(f"Missing index_file for {product.get('id')}: {index_file.relative_to(PROJECT_ROOT)}")
        if docs_dir.exists():
            # Bad crawls are already blocked at crawl time; old bad docs only warn unless --strict,
            # so one source that cannot be re-crawled does not block every other product's update.
            (errors if args.strict else warnings).extend(check_docs_dir(docs_dir))
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(products)} products configured and indexed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage multi-market API docs")
    sub = parser.add_subparsers(dest="command", required=True)

    crawl_parser = sub.add_parser("crawl", help="Crawl product docs")
    crawl_parser.add_argument("--all", action="store_true", help="Crawl all products")
    crawl_parser.add_argument("--product", "-p", help="Crawl one product")
    crawl_parser.add_argument("--limit", "-l", type=int, help="Limit number of documents per product")
    crawl_parser.set_defaults(func=cmd_crawl)

    list_parser = sub.add_parser("list", help="List configured products")
    list_parser.set_defaults(func=cmd_list)

    index_parser = sub.add_parser("index", help="Generate JSON indexes")
    index_parser.add_argument("--all", action="store_true", help="Generate all product indexes")
    index_parser.add_argument("--product", "-p", help="Generate one product index")
    index_parser.set_defaults(func=cmd_index)

    readme_parser = sub.add_parser("readme", help="Refresh generated README sections")
    readme_parser.set_defaults(func=cmd_readme)

    validate_parser = sub.add_parser("validate", help="Validate configs, docs dirs, and indexes")
    validate_parser.add_argument("--strict", action="store_true", help="Treat doc quality problems as errors")
    validate_parser.set_defaults(func=cmd_validate)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command in {"crawl", "index"} and not args.all and not args.product:
        parser.error(f"{args.command} requires --all or --product/-p")
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
