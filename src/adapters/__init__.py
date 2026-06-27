#!/usr/bin/env python3
"""Import adapters so registration decorators run."""
from src.adapters.base import DocumentPage, ProductAdapter, get_adapter, register_adapter
from src.adapters import zhongtai_xtp, zhongtai_xtppro  # noqa: F401

__all__ = ["DocumentPage", "ProductAdapter", "get_adapter", "register_adapter"]
