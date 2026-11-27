---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/postman/collections
api_type: Guide
updated_at: 2026-11-27 18:27:40.973116
---

# Postman Collections

Binance maintains an official set of **Postman collections and environments** to help you explore
and test Binance **REST APIs** across products.

For source code, collections, environments, and updates, see the
[binance-api-postman](https://github.com/binance/binance-api-postman) repository on GitHub.

## What’s included

- Postman **Collections** for Binance REST endpoints
- Postman **Environments** (JSON) for configuring base URLs and credentials

> These collections are focused on **REST** usage. WebSocket APIs and WebSocket Streams are
> typically not covered by Postman collections.

## Quick start

1. Download (or clone) the `binance-api-postman` repository.
2. In Postman, click **Import** and select the repository’s **root folder**.
3. Choose which **collections** and **environments** you want to import.
4. In Postman → **Environments**, open the environment you’ll use and set your API credentials in
   the **Current Value** column.
5. Select that environment from the environment dropdown before sending requests.

## Authentication and environments

Many endpoints require authentication and signing. The repository provides environment files so you
can:

- Switch between environments (for example, production vs testnet) by selecting a different Postman
  environment
- Store your API key/secret in Postman environment variables (use **Current Value** so you don’t
  accidentally export secrets)

## Safety practices

When using Postman collections with real credentials, Binance recommends these safety measures:

- Only use collections from trusted sources (this repo is the official one)
- Review the environment JSON before using it
- Avoid enabling withdrawal permissions on API keys
- Delete API keys when you finish testing

---

# Postman 集合

Binance 维护一套官方 **Postman 集合与环境配置**，帮助您探索和测试各产品的 Binance **REST API**。

如需查看源代码、集合文件、环境配置及更新说明，请访问 GitHub 上的
[binance-api-postman](https://github.com/binance/binance-api-postman) 仓库。

## 内容概览

- 适用于 Binance REST 接口的 Postman **集合**
- 用于配置基础 URL 和凭证的 Postman **环境**（JSON 格式）

> 这些集合专注于 **REST** 使用场景。WebSocket
> API 和 WebSocket 数据流通常不在 Postman 集合的覆盖范围内。

## 快速开始

1. 下载（或克隆）`binance-api-postman` 仓库。
2. 在 Postman 中点击 **Import**，选择仓库的**根目录**。
3. 选择您需要导入的**集合**和**环境**。
4. 在 Postman → **Environments** 中，打开您将使用的环境，在 **Current Value**
   列中填入您的 API 凭证。
5. 发送请求前，从环境下拉菜单中选择对应的环境。

## 身份验证与环境配置

许多接口需要身份验证和请求签名。仓库提供的环境文件支持以下操作：

- 通过切换 Postman 环境（例如正式环境与测试网）来切换不同的请求目标
- 将 API Key/Secret 存储在 Postman 环境变量中（请使用 **Current Value**，避免意外导出密钥）

## 安全注意事项

在 Postman 集合中使用真实凭证时，Binance 建议遵循以下安全措施：

- 仅使用来自可信来源的集合（本仓库为官方来源）
- 使用前请审查环境 JSON 文件的内容
- 避免为 API 密钥开启提币权限
- 测试完成后及时删除 API 密钥