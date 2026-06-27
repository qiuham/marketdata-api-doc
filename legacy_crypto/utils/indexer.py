#!/usr/bin/env python3
"""No-op legacy indexer.

Legacy crypto adapters call their own indexer after crawling. In this repository
we generate product indexes with src.utils.indexer instead, so this class only
preserves the old adapter interface.
"""


class DocumentIndexer:
    def __init__(self, docs_dir: str):
        self.docs_dir = docs_dir

    def generate_index(self, index_dir: str) -> str:
        return ""

    def scan_documents(self):
        return []

    def generate_structure(self):
        return {"total": 0, "documents": []}
