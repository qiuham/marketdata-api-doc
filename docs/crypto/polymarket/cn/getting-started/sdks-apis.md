---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/cn/getting-started/sdks-apis'
updated_at: 2026-11-13
---

# SDK 与 API

> 选择与 Polymarket 集成的方式。

选择最适合应用的接口。使用 SDK 可获得统一、带类型的集成；需要更底层的控制时，也可以直接使用 API。

> [card] [TypeScript SDK](https://docs.polymarket.com/cn/getting-started/typescript.md)
>
> 使用 `@polymarket/client` 构建服务、机器人、脚本和应用。

> [card] [Python SDK](https://docs.polymarket.com/cn/getting-started/python.md)
>
> 使用 `polymarket-client` 构建服务、笔记本、脚本和数据工作流。

> [card] [API](https://docs.polymarket.com/cn/getting-started/api.md)
>
> 直接使用 Polymarket REST API 和 WebSocket 数据流构建集成。

> [!NOTE]
>
> 统一的 Rust SDK 正在开发中。目前请参阅 [Rust
> 迁移指南](https://docs.polymarket.com/cn/migrate/clob-sdk-to-unified-sdk.md#安装-rust-sdk)。

## 选项对比

| | TypeScript SDK | Python SDK | API |
| - | - | - | - |
| 最适合 | Node.js 应用、机器人和服务 | 服务、脚本和笔记本 | 不受支持的运行时和底层控制 |
| 数据模型 | 带类型的模型 | 带类型的模型 | 原始 JSON |
| Polymarket 产品面 | 一个客户端接口 | 一个客户端接口 | 各服务使用不同 API |
| 身份验证与签名 | SDK 辅助方法选择支持的路径 | SDK 辅助方法选择支持的路径 | 选择并实现匹配的路径 |
| 分页 | 统一的分页器 | 统一的分页器 | 因 API 而异 |
| 实时数据 | SDK 订阅 | SDK 订阅 | 分别连接各 WebSocket 产品面 |

## 现有集成

已经在使用较早版本的 Polymarket SDK？请按照 [SDK 迁移指南](https://docs.polymarket.com/cn/migrate/clob-sdk-to-unified-sdk.md)更新集成。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
