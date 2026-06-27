#!/usr/bin/env python3
"""
文件路径生成工具
用于将URL、锚点ID等转换为规范的文件目录结构
"""
import re
from pathlib import Path
from urllib.parse import unquote, urlparse
from typing import Optional


_UNSAFE_PATH_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_MULTI_DASHES = re.compile(r'-+')
_WHITESPACE = re.compile(r'\s+')


def sanitize_path_component(value: object, fallback: str = "untitled") -> str:
    """清理单个路径片段，避免绝对路径/路径穿越/非法文件名。"""
    component = unquote(str(value or "")).strip()
    component = _UNSAFE_PATH_CHARS.sub("-", component)
    component = _WHITESPACE.sub("-", component)
    component = _MULTI_DASHES.sub("-", component)
    component = component.strip("-. ")

    if not component or component in {".", ".."}:
        return fallback

    return component


def safe_output_path(output_dir: str, relative_path: str) -> str:
    """把相对路径限制在输出目录内，防止写出目标目录。"""
    base_dir = Path(output_dir).resolve()
    target_path = (base_dir / relative_path).resolve()

    if target_path != base_dir and base_dir not in target_path.parents:
        raise ValueError(f"输出路径越界: {relative_path}")

    return str(target_path)


def safe_rmtree(target_dir: str, allowed_roots: list) -> None:
    """只允许删除指定根目录下的子目录，避免配置错误误删。"""
    import shutil

    target_path = Path(target_dir).resolve()
    allowed = [Path(root).resolve() for root in allowed_roots]

    if not any(target_path != root and root in target_path.parents for root in allowed):
        raise ValueError(f"拒绝删除非授权目录: {target_dir}")

    shutil.rmtree(target_path)


def url_to_filepath(url: str, base_prefix: Optional[str] = None) -> str:
    """从URL生成文件路径（保留目录结构）

    Args:
        url: 页面URL
        base_prefix: 基础前缀URL，会从路径中移除

    Returns:
        文件路径，例如: testnet/rest-api/endpoints.md

    Examples:
        >>> url_to_filepath(
        ...     "https://example.com/docs/zh-CN/product/testnet/rest-api/endpoints",
        ...     "https://example.com/docs/zh-CN/product/"
        ... )
        'testnet/rest-api/endpoints.md'

        >>> url_to_filepath("https://example.com/api/websocket/info")
        'api/websocket/info.md'
    """
    path = urlparse(url).path

    # 移除基础前缀
    if base_prefix:
        prefix_path = urlparse(base_prefix).path
        if path.startswith(prefix_path):
            path = path[len(prefix_path):]

    # 清理每个路径片段，避免远端链接构造 ../../ 等路径穿越
    parts = [
        sanitize_path_component(part)
        for part in path.split('/')
        if part and part not in {'.', '..'}
    ]
    path = '/'.join(parts)

    # 处理空路径
    if not path:
        return "index.md"

    # 确保有.md后缀
    if not path.endswith('.md'):
        path += '.md'

    return path


def anchor_to_filepath(anchor_id: str, separator: str = '-', max_depth: int = 3) -> str:
    """从锚点ID生成目录层级路径

    策略：将短横线分隔的ID转换为目录层级，最后一段作为文件名

    Args:
        anchor_id: 锚点ID，例如 "overview-api-resources-and-support-tutorials"
        separator: 分隔符，默认是短横线
        max_depth: 最大目录深度，超过的部分会合并到最后

    Returns:
        文件路径，例如: overview/api-resources-and-support/tutorials.md

    Examples:
        >>> anchor_to_filepath("overview-api-resources-and-support-tutorials")
        'overview/api-resources-and-support/tutorials.md'

        >>> anchor_to_filepath("overview")
        'overview.md'

        >>> anchor_to_filepath("rest-api-trade-order-post", max_depth=2)
        'rest-api/trade-order-post.md'
    """
    if not anchor_id:
        return "index.md"

    # 分割成段并清理，避免锚点中携带路径穿越字符
    parts = [
        sanitize_path_component(part)
        for part in anchor_id.split(separator)
        if part and part not in {'.', '..'}
    ]

    if not parts:
        return "index.md"

    # 只有一段：直接作为文件名
    if len(parts) == 1:
        return f"{parts[0]}.md"

    # 多段：转换为目录结构
    # 策略：最后一段是文件名，前面的是目录
    if len(parts) <= max_depth:
        # 不超过最大深度：正常分层
        dirs = parts[:-1]
        filename = parts[-1]
    else:
        # 超过最大深度：前max_depth-1个作为目录，剩余的合并为文件名
        dirs = parts[:max_depth-1]
        filename = separator.join(parts[max_depth-1:])

    # 组合路径
    if dirs:
        return f"{'/'.join(dirs)}/{filename}.md"
    else:
        return f"{filename}.md"


def slugify_title(title: str, max_length: int = 50) -> str:
    """将标题转换为安全的文件名slug

    Args:
        title: 原始标题
        max_length: 最大长度

    Returns:
        安全的文件名slug

    Examples:
        >>> slugify_title("REST API - Trade Order (POST)")
        'rest-api-trade-order-post'

        >>> slugify_title("WebSocket 用户数据流")
        'websocket-用户数据流'
    """
    import re

    # 转小写
    slug = title.lower()

    # 移除特殊字符，保留字母、数字、短横线、下划线、中文
    slug = re.sub(r'[^\w\s\-\u4e00-\u9fff]', '', slug)

    # 多个空格/短横线合并为一个短横线
    slug = re.sub(r'[\s\-]+', '-', slug)

    # 移除首尾的短横线
    slug = slug.strip('-')

    # 限制长度
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip('-')

    return slug or 'untitled'


def is_hash_anchor(anchor_id: str) -> bool:
    """检测锚点ID是否是哈希格式（无语义的随机字符串）

    Args:
        anchor_id: 锚点ID

    Returns:
        是否是哈希格式

    Examples:
        >>> is_hash_anchor("b122f813d5")
        True

        >>> is_hash_anchor("overview-api-resources")
        False
    """
    import re
    # 10位纯字母数字，没有短横线 → 视为哈希
    return bool(re.match(r'^[a-f0-9]{10}$', anchor_id))


def deduplicate_filepath(filepath: str, existing_files: set) -> str:
    """为重复的文件路径添加序号

    Args:
        filepath: 原始文件路径
        existing_files: 已存在的文件路径集合

    Returns:
        去重后的文件路径

    Examples:
        >>> deduplicate_filepath("api/order.md", {"api/order.md"})
        'api/order-2.md'

        >>> deduplicate_filepath("api/order.md", {"api/order.md", "api/order-2.md"})
        'api/order-3.md'
    """
    if filepath not in existing_files:
        return filepath

    # 分离路径和扩展名
    import os
    base, ext = os.path.splitext(filepath)

    # 尝试添加序号
    counter = 2
    while True:
        new_filepath = f"{base}-{counter}{ext}"
        if new_filepath not in existing_files:
            return new_filepath
        counter += 1
