---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rate-limits-trading-related-apis
anchor_id: overview-rate-limits-trading-related-apis
api_type: API
updated_at: 2026-07-11 19:12:00.742377
---

# Trading-related APIs

For Trading-related APIs (place order, cancel order, and amend order) the following conditions apply:

  * Rate limits are shared across the REST and WebSocket channels. 

  * Rate limits for placing orders, amending orders, and cancelling orders are independent from each other. 

  * Rate limits are defined on the Instrument ID level (except Options)

  * Rate limits for Options are defined based on the Instrument Family level. Refer to the [Get instruments](/docs-v5/en/#public-data-rest-api-get-instruments) endpoint to view Instrument Family information.

  * Rate limits for a multiple order endpoint and a single order endpoint are also independent, with the exception being when there is only one order sent to a multiple order endpoint, the order will be counted as a single order and adopt the single order rate limit.

---

# 交易相关API

对于与交易相关的 API（下订单、取消订单和修改订单），以下条件适用：

  * 限速在 REST 和 WebSocket 通道之间共享。

  * 下单、修改订单、取消订单的限速相互独立。

  * 限速在 Instrument ID 级别定义（期权除外）

  * 期权的限速是根据 Instrument Family 级别定义的。 请参阅 [获取交易产品基础信息](/docs-v5/zh/#public-data-rest-api-get-instruments) 接口以查看交易品种信息。

  * 批量订单接口和单订单接口的限速也是独立的，除了只有一个订单发送到批量订单接口时，该订单将被视为一个订单并采用单订单限速。