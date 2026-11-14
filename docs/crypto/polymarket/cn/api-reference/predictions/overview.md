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
source_url: 'https://docs.polymarket.com/cn/api-reference/predictions/overview'
updated_at: 2026-11-13
---

# 概览

> 了解用于构建 Polymarket 预测市场集成的 API。

## API

Polymarket 预测市场由多个 API 组成，每个 API 负责集成中的不同部分。

> [card] Gamma API
>
> **`https://gamma-api.polymarket.com`**
>
> 发现事件和市场，并获取使用它们所需的元数据。

> [card] CLOB API
>
> **`https://clob.polymarket.com`**
>
> 读取实时市场状态，然后下单和管理订单。

> [card] [Data API](https://data-api.polymarket.com/v2/docs)
>
> **`https://data-api.polymarket.com`**
>
> 在发现市场和交易后，了解账户与市场活动。v2 现已提供，
> 支持游标分页与统一的响应结构。

> [card] Relayer API
>
> **`https://relayer-v2.polymarket.com`**
>
> 提交受支持的钱包交易，而无需账户持有用于支付 Gas 的 POL。

> [card] WebSocket API
>
> **实时数据流**
>
> 通过市场、账户、体育和 RFQ 事件持续更新集成。

> [card] Bridge API
>
> **`https://bridge.polymarket.com`**
>
> 使用受支持的资产向 Polymarket 充值或从中提现。

## 集成前须知

> [card] [速率限制](https://docs.polymarket.com/cn/api-reference/rate-limits.md)
>
> 查看各服务和端点的请求限制。

> [card] [地区限制](https://docs.polymarket.com/cn/api-reference/geoblock.md)
>
> 查看哪些地区可以下单。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
