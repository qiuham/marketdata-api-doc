#!/usr/bin/env python3
"""
交易所适配器基类
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Type
from dataclasses import dataclass


@dataclass
class DocumentPage:
    """文档页面数据结构"""
    url: str
    title: str
    content: str  # Markdown 格式
    metadata: Dict[str, Any]
    raw_html: str = ""


# Adapter注册表
_ADAPTER_REGISTRY: Dict[str, Type['ExchangeAdapter']] = {}


def register_adapter(name: str):
    """装饰器：注册adapter到全局注册表

    使用方式:
        @register_adapter('binance')
        class BinanceAdapter(ExchangeAdapter):
            pass
    """
    def decorator(cls: Type['ExchangeAdapter']) -> Type['ExchangeAdapter']:
        _ADAPTER_REGISTRY[name] = cls
        return cls
    return decorator


def get_adapter(config: dict) -> 'ExchangeAdapter':
    """根据配置动态获取adapter实例

    Args:
        config: 配置字典（必须包含'name'字段）

    Returns:
        ExchangeAdapter实例

    Raises:
        NotImplementedError: 当name对应的adapter未注册时
    """
    name = config['name']
    if name not in _ADAPTER_REGISTRY:
        available = ', '.join(_ADAPTER_REGISTRY.keys())
        raise NotImplementedError(
            f"暂不支持: {name}\n"
            f"可用的交易所: {available}"
        )
    return _ADAPTER_REGISTRY[name](config)


class ExchangeAdapter(ABC):
    """交易所适配器抽象基类"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.name = config['name']

    @abstractmethod
    def crawl(self, concurrency: int = 1, limit: int = None, languages: List[str] = None):
        """
        执行完整的爬取流程（每个适配器实现自己的逻辑）

        Args:
            concurrency: 并发数
            limit: 每个入口限制爬取的页面数（None表示不限制）
            languages: 指定爬取的语言列表（None表示爬取所有语言）
        """
        pass

    @abstractmethod
    def discover_pages(self) -> List[str]:
        """
        发现所有文档页面URL

        Returns:
            List[str]: 所有页面的URL列表
        """
        pass

    @abstractmethod
    def extract_content(self, url: str) -> DocumentPage:
        """
        提取指定页面的内容

        Args:
            url: 页面URL

        Returns:
            DocumentPage: 提取的页面内容
        """
        pass

    def get_exchange_name(self) -> str:
        """返回交易所名称"""
        return self.name

    def get_output_path(self, product_name: str = None) -> str:
        """
        获取输出路径

        Args:
            product_name: 产品名称（用于多产品模式）

        Returns:
            str: 输出目录路径
        """
        base_dir = self.config.get('output', {}).get('base_dir', 'docs')
        exchange_dir = self.config.get('output', {}).get('dir_name', self.name)

        if product_name:
            # 将产品名转换为安全的目录名
            import re
            safe_name = re.sub(r'[^\w\-]', '_', product_name.lower())
            safe_name = re.sub(r'_+', '_', safe_name).strip('_')
            return f"{base_dir}/{exchange_dir}/{safe_name}"
        else:
            return f"{base_dir}/{exchange_dir}"
