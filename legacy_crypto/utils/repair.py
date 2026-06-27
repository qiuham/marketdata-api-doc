#!/usr/bin/env python3
"""
修复工具：处理 Untitled 和错误页面
"""
import os
import re
from pathlib import Path
from typing import List, Tuple
from loguru import logger as log


class DocumentRepair:
    """文档修复工具"""

    def __init__(self, docs_dir: str):
        self.docs_dir = Path(docs_dir)

    def find_untitled_pages(self) -> List[Tuple[str, str]]:
        """
        查找所有标题为 Untitled 的页面
        返回: [(文件路径, 源URL), ...]
        """
        untitled_pages = []

        for md_file in self.docs_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 检查是否有 "# Untitled"
                if re.search(r'^# Untitled\s*$', content, re.MULTILINE):
                    # 提取 source_url
                    url_match = re.search(r'source_url:\s*(.+)', content)
                    if url_match:
                        source_url = url_match.group(1).strip()
                        untitled_pages.append((str(md_file), source_url))

            except Exception as e:
                log.warning(f"读取文件失败: {md_file} - {e}")

        return untitled_pages

    def find_empty_content_pages(self) -> List[Tuple[str, str]]:
        """
        查找内容为空或过短的页面
        返回: [(文件路径, 源URL), ...]
        """
        empty_pages = []

        for md_file in self.docs_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 分离 frontmatter 和正文
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    body = parts[2].strip()

                    # 如果正文太短（少于 50 个字符）
                    if len(body) < 50:
                        url_match = re.search(r'source_url:\s*(.+)', frontmatter)
                        if url_match:
                            source_url = url_match.group(1).strip()
                            empty_pages.append((str(md_file), source_url))

            except Exception as e:
                log.warning(f"读取文件失败: {md_file} - {e}")

        return empty_pages

    def find_wrong_content_pages(self) -> List[Tuple[str, str]]:
        """
        查找内容不匹配的页面（URL 和内容不一致）
        检测方法：URL 中的关键词不在内容中
        """
        wrong_pages = []

        for md_file in self.docs_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 提取 source_url
                url_match = re.search(r'source_url:\s*(.+)', content)
                if not url_match:
                    continue

                source_url = url_match.group(1).strip()

                # 从 URL 提取页面名称
                url_parts = source_url.rstrip('/').split('/')
                page_slug = url_parts[-1] if url_parts else ''

                # 将 slug 转成关键词（去掉连字符）
                keywords = page_slug.replace('-', ' ').lower().split()

                # 检查内容中是否包含关键词（至少一半）
                content_lower = content.lower()
                matches = sum(1 for kw in keywords if kw in content_lower)

                if keywords and matches < len(keywords) / 2:
                    wrong_pages.append((str(md_file), source_url))

            except Exception as e:
                log.warning(f"读取文件失败: {md_file} - {e}")

        return wrong_pages

    def get_all_problem_pages(self) -> List[Tuple[str, str]]:
        """获取所有有问题的页面（去重）"""
        all_problems = set()

        # Untitled 页面
        untitled = self.find_untitled_pages()
        log.info(f"发现 {len(untitled)} 个 Untitled 页面")
        all_problems.update(untitled)

        # 空内容页面
        empty = self.find_empty_content_pages()
        log.info(f"发现 {len(empty)} 个空内容页面")
        all_problems.update(empty)

        # 内容不匹配页面
        wrong = self.find_wrong_content_pages()
        log.info(f"发现 {len(wrong)} 个内容可能不匹配的页面")
        all_problems.update(wrong)

        return list(all_problems)

    def delete_problem_pages(self, pages: List[Tuple[str, str]]) -> int:
        """删除有问题的页面"""
        deleted = 0
        for file_path, _ in pages:
            try:
                os.remove(file_path)
                deleted += 1
                log.debug(f"删除: {file_path}")
            except Exception as e:
                log.warning(f"删除失败: {file_path} - {e}")

        log.info(f"已删除 {deleted} 个文件")
        return deleted

    def extract_urls(self, pages: List[Tuple[str, str]]) -> List[str]:
        """从页面列表中提取 URL"""
        return [url for _, url in pages]


def repair_exchange_docs(exchange_name: str):
    """修复指定交易所的文档"""
    from pathlib import Path

    project_root = Path(__file__).parent.parent.parent
    docs_dir = project_root / "docs" / exchange_name

    if not docs_dir.exists():
        log.error(f"文档目录不存在: {docs_dir}")
        return

    log.info(f"开始检查 {exchange_name} 文档...")

    repair = DocumentRepair(str(docs_dir))

    # 查找所有问题页面
    problem_pages = repair.get_all_problem_pages()

    if not problem_pages:
        log.success("未发现问题页面！")
        return

    log.warning(f"共发现 {len(problem_pages)} 个问题页面")

    # 提取 URL 列表
    urls = repair.extract_urls(problem_pages)

    # 保存到文件供后续使用
    output_file = project_root / "temp" / f"{exchange_name}_problem_urls.txt"
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {exchange_name} 问题页面 URL 列表\n")
        f.write(f"# 总计: {len(urls)} 个\n\n")
        for url in urls:
            f.write(f"{url}\n")

    log.success(f"URL 列表已保存: {output_file}")
    log.info("稍后可使用这些 URL 重新爬取")

    return urls


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("用法: python repair.py <exchange_name>")
        sys.exit(1)

    exchange = sys.argv[1]
    repair_exchange_docs(exchange)
