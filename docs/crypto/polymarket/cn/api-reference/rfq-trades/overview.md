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
source_url: 'https://docs.polymarket.com/cn/api-reference/rfq-trades/overview'
updated_at: 2026-11-13
---

# 概览

> 了解 RFQ 交易合作伙伴 API，用于结算在你的平台上撮合的交易。

## API

RFQ 交易合作伙伴 API 用于结算你的平台在 Polymarket 之外撮合的交易：请求通过 HTTP 发送，交易状态通过 WebSocket 推送。仅限受邀访问：请参阅[机构概览](https://docs.polymarket.com/partners/overview.md)，了解适用对象以及申请访问的方式。

> [card] HTTP API
>
> `https://external-rfq-partner.polymarket.com`
>
> 验证、准备、提交和查询 RFQ 交易。

> [card] WebSocket API
>
> `wss://external-rfq-partner.polymarket.com/v1/ws/rfq-trades`
>
> 推送你的交易的状态变化。

测试环境的 Base URL 会在接入时提供，并附带该环境的测试 API 密钥。

## 集成前须知

> [card] [身份验证](https://docs.polymarket.com/cn/api-reference/rfq-trades/authentication.md)
>
> 使用你的合作伙伴 API 密钥签署每个请求。

> [card] [交易流程](https://docs.polymarket.com/partners/rfq-trades.md)
>
> 查找市场，然后验证、签名、提交并跟踪交易。

> [card] [错误](https://docs.polymarket.com/partners/rfq-trades.md#errors)
>
> 了解错误响应格式和所有拒绝原因。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
