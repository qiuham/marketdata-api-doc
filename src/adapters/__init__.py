#!/usr/bin/env python3
"""Import adapters so registration decorators run."""
from src.adapters.base import DocumentPage, ProductAdapter, get_adapter, register_adapter
from src.adapters import crypto_legacy  # noqa: F401
from src.adapters import llms_txt  # noqa: F401

__all__ = ["DocumentPage", "ProductAdapter", "get_adapter", "register_adapter"]
