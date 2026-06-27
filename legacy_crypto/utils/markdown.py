#!/usr/bin/env python3
"""
Markdown 处理工具
"""
import html2text
import yaml
from typing import Dict, Any
from datetime import datetime


class MarkdownProcessor:
    """Markdown 转换和处理"""

    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        self.converter.ignore_images = False
        self.converter.ignore_emphasis = False
        self.converter.body_width = 0
        # 表格处理
        self.converter.bypass_tables = False  # 转换表格为 Markdown
        self.converter.use_automatic_links = True

    def html_to_markdown(self, html: str) -> str:
        """HTML 转 Markdown"""
        return self.converter.handle(html)

    def generate_frontmatter(self, metadata: Dict[str, Any]) -> str:
        """生成文档前置信息"""
        yaml_body = yaml.safe_dump(
            metadata,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False
        ).strip()
        return f"---\n{yaml_body}\n---"

    def create_document(
        self,
        title: str,
        content: str,
        metadata: Dict[str, Any]
    ) -> str:
        """创建完整的Markdown文档"""
        # 添加更新时间
        if 'updated_at' not in metadata:
            metadata['updated_at'] = datetime.now()

        frontmatter = self.generate_frontmatter(metadata)

        # 移除 content 中的第一个 h1 标题（避免重复）
        import re
        content_lines = content.split('\n')
        result_lines = []
        found_first_h1 = False

        for line in content_lines:
            # 如果是第一个 h1 标题行，跳过
            if not found_first_h1 and re.match(r'^#\s+', line):
                found_first_h1 = True
                continue
            result_lines.append(line)

        content = '\n'.join(result_lines).strip()

        return f"{frontmatter}\n\n# {title}\n\n{content}"


def sanitize_filename(name: str, max_length: int = 100) -> str:
    """清理文件名"""
    import re

    # 移除特殊字符
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # 空格转连字符
    name = re.sub(r'\s+', '-', name)
    # 移除多余的连字符
    name = re.sub(r'-+', '-', name)
    # 转小写
    name = name.lower().strip('-')
    # 限制长度
    return name[:max_length]
