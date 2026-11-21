---
exchange: binance
source_url: https://developers.binance.com/en/docs/agent-native/llms-txt
api_type: Guide
updated_at: 2026-11-21 18:26:14.007286
---

# llms.txt

[llms.txt](https://llmstxt.org/) is a proposed standard for making website content accessible to
large language models. Similar to `robots.txt` for web crawlers, `llms.txt` tells AI tools what
documentation is available and how to access it.

## Files

Binance API Documentation provides two llms.txt files:

| File            | URL                                                                         | Description                                            |
| --------------- | --------------------------------------------------------------------------- | ------------------------------------------------------ |
| `llms.txt`      | <a href={`/en/docs/llms.txt`} target="\_blank">/docs/llms.txt</a>           | Summary — document titles, descriptions, and links     |
| `llms-full.txt` | <a href={`/en/docs/llms-full.txt`} target="\_blank">/docs/llms-full.txt</a> | Full content — complete documentation in a single file |

## Format

### llms.txt (Summary)

The summary file contains a structured list of all documentation pages with titles, descriptions,
and URLs:

```
# Binance API Documentation

> Comprehensive API documentation for Binance trading platform.

## Spot Trading

- [Changelog](/docs/spot-trading/1.changelog): Spot Trading API changelog
- [README](/docs/spot-trading/2.readme): Getting started with Spot Trading API
...

## Derivatives Trading

- [Change Log](/docs/derivatives/change-log): Derivatives API changelog
...
```

### llms-full.txt (Full Content)

The full file includes the complete markdown content of every documentation page, separated by
headers. This is useful for loading the entire documentation into an LLM's context window.

## Usage Examples

### Feed into any LLM

```bash
# Download and use as context
curl -s https://developers.binance.com/en/docs/llms.txt

# Full documentation for comprehensive context
curl -s https://developers.binance.com/en/docs/llms-full.txt
```

### Use with Claude

```
Please read https://developers.binance.com/en/docs/llms.txt and help me
understand how to place a futures order using the Binance API.
```

### Use in a Python script

```python
import requests

# Fetch the documentation index
response = requests.get("https://developers.binance.com/en/docs/llms.txt")
docs_index = response.text

# Feed into your LLM as context
messages = [
    {"role": "system", "content": f"Binance API docs:\n{docs_index}"},
    {"role": "user", "content": "How do I check my account balance?"}
]
```

### Use with LangChain

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://developers.binance.com/en/docs/llms-full.txt")
docs = loader.load()
```

## When to Use llms.txt vs Other Options

- **llms.txt** — You want to quickly give an LLM awareness of all available documentation, or load
  full docs into context
- **Agent REST API** — You need structured JSON data, filtered queries, or programmatic access
- **MCP Server** — You're using Claude Code, Cursor, or another MCP-compatible IDE

---

# llms.txt

[llms.txt](https://llmstxt.org/)
是一项拟议标准，旨在使网站内容对大语言模型更易于访问。与用于网络爬虫的 `robots.txt` 类似，`llms.txt`
告知 AI 工具有哪些文档可用以及如何访问这些文档。

## 文件

币安 API 文档提供两个 llms.txt 文件：

| 文件            | URL                                                                            | 描述                                |
| --------------- | ------------------------------------------------------------------------------ | ----------------------------------- |
| `llms.txt`      | <a href={`/zh-CN/docs/llms.txt`} target="\_blank">/docs/llms.txt</a>           | 摘要 — 文档标题、描述和链接         |
| `llms-full.txt` | <a href={`/zh-CN/docs/llms-full.txt`} target="\_blank">/docs/llms-full.txt</a> | 完整内容 — 所有文档汇集在一个文件中 |

## 格式

### llms.txt（摘要）

摘要文件包含所有文档页面的结构化列表，包括标题、描述和 URL：

```
# Binance API Documentation

> Comprehensive API documentation for Binance trading platform.

## Spot Trading

- [Changelog](/docs/spot-trading/1.changelog): Spot Trading API changelog
- [README](/docs/spot-trading/2.readme): Getting started with Spot Trading API
...

## Derivatives Trading

- [Change Log](/docs/derivatives/change-log): Derivatives API changelog
...
```

### llms-full.txt（完整内容）

完整文件包含每个文档页面的完整 Markdown 内容，以标题分隔。这对于将整个文档加载到大语言模型的上下文窗口中非常有用。

## 使用示例

### 输入到任意大语言模型

```bash
# 下载并用作上下文
curl -s https://developers.binance.com/zh-CN/docs/llms.txt

# 完整文档，用于全面的上下文
curl -s https://developers.binance.com/zh-CN/docs/llms-full.txt
```

### 与 Claude 配合使用

```
请阅读 https://developers.binance.com/zh-CN/docs/llms.txt，并帮助我了解
如何使用币安 API 下合约订单。
```

### 在 Python 脚本中使用

```python
import requests

# 获取文档索引
response = requests.get("https://developers.binance.com/zh-CN/docs/llms.txt")
docs_index = response.text

# 将其作为上下文输入到大语言模型
messages = [
    {"role": "system", "content": f"Binance API docs:\n{docs_index}"},
    {"role": "user", "content": "How do I check my account balance?"}
]
```

### 与 LangChain 配合使用

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://developers.binance.com/zh-CN/docs/llms-full.txt")
docs = loader.load()
```

## 何时使用 llms.txt 与其他选项

- **llms.txt** — 您希望快速让大语言模型了解所有可用文档，或将完整文档加载到上下文中
- **Agent REST API** — 您需要结构化的 JSON 数据、过滤查询或程序化访问
- **MCP Server** — 您正在使用 Claude Code、Cursor 或其他兼容 MCP 的 IDE