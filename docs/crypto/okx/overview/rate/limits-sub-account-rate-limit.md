---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rate-limits-sub-account-rate-limit
anchor_id: overview-rate-limits-sub-account-rate-limit
api_type: API
updated_at: 2026-07-10 19:30:06.812109
---

# Sub-account rate limit

At the sub-account level, we allow a maximum of 1000 order requests per 2 seconds. Only new order requests and amendment order requests will be counted towards this limit. The limit encompasses all requests from the endpoints below. For batch order requests consisting of multiple orders, each order will be counted individually. Error code 50061 is returned when the sub-account rate limit is exceeded. The existing rate limit rule per instrument ID remains unchanged and the existing rate limit and sub-account rate limit will operate in parallel. If clients require a higher rate limit, clients can trade via multiple sub-accounts.

  * [POST / Place order](/docs-v5/en/#order-book-trading-trade-post-place-order)
  * [POST / Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders)
  * [POST / Amend order](/docs-v5/en/#order-book-trading-trade-post-amend-order)
  * [POST / Amend multiple orders](/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders)

  * [WS / Place order](/docs-v5/en/#order-book-trading-trade-ws-place-order)

  * [WS / Place multiple orders](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders)

  * [WS / Amend order](/docs-v5/en/#order-book-trading-trade-ws-amend-order)

  * [WS / Amend multiple orders](/docs-v5/en/#order-book-trading-trade-ws-amend-multiple-orders)

---

# 子账户限速

子账户维度，每2秒最多允许1000个订单相关请求。仅有新订单及修改订单请求会被计入此限制。此限制涵盖以下所列的所有接口。对于包含多个订单的批量请求，每个订单将被单独计数。如果请求频率超过限制，系统会返回50061错误码。产品ID维度的限速规则保持不变，现有的限速规则与新增的子账户维度限速将并行运行。若用户需要更高的速率限制，可以通过多个子账户进行交易。

  * [POST / 下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)
  * [POST / 批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)
  * [POST / 修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-order)
  * [POST / 批量修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-multiple-orders)

  * [WS / 下单](/docs-v5/zh/#order-book-trading-trade-ws-place-order)

  * [WS / 批量下单](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)

  * [WS / 改单](/docs-v5/zh/#order-book-trading-trade-ws-amend-order)

  * [WS / 批量改单](/docs-v5/zh/#order-book-trading-trade-ws-amend-multiple-orders)