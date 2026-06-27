#!/usr/bin/env python3
"""
Adapter模块初始化
导入所有adapter以触发装饰器注册
"""

# 导入base以便外部可以使用get_adapter
from .base import get_adapter, register_adapter, ExchangeAdapter, DocumentPage

# 导入所有adapter以触发@register_adapter装饰器
from . import binance
from . import bybit
from . import hyperliquid
from . import okx
from . import kraken
from . import coinbase
from . import gateio

__all__ = ['get_adapter', 'register_adapter', 'ExchangeAdapter', 'DocumentPage']
