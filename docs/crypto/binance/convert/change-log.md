---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/convert/change-log
api_type: REST
updated_at: 2026-11-13 20:31:13.989875
---

# Change Log

## 2025-12-26

### Time-sensitive Notice

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/en/docs/products/convert/error-code#-1022-invalid_signature). Please review and update your signing logic accordingly.



### REST API

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/en/docs/products/convert/general-info#signed-endpoint-examples-for-post-apiv3order).



* * *

## 2024-01-24

  * New Endpoints for Convert:
    * `POST /sapi/v1/convert/limit/placeOrder`: Place convert limit order
    * `POST /sapi/v1/convert/limit/cancelOrder`: Cancel convert limit order
    * `GET /sapi/v1/convert/limit/queryOpenOrders`: Query convert limit open orders



* * *

## 2022-11-22

  * New endpoints for Convert:
    * `GET /sapi/v1/convert/exchangeInfo`: Query for all convertible token pairs and the tokens’ respective upper/lower limits
    * `GET /sapi/v1/convert/assetInfo`: Query for supported asset’s precision information
    * `POST /sapi/v1/convert/getQuote`: Request a quote for the requested token pairs
    * `POST /sapi/v1/convert/acceptQuote`: Accept the offered quote by quote ID.
    * `GET /sapi/v1/convert/orderStatus`: Query order status by order ID.



* * *

## 2022-08-18

  * Update endpoint for Convert:
    * `GET /sapi/v1/convert/tradeFlow`: Update weight from Weight(IP) 3000 to Weight(UID) 3000.



* * *

## 2022-07-01

  * Update endpoint for Convert:
    * `GET /sapi/v1/convert/tradeFlow`: Update weight from 3000 to 100.



* * *

## 2021-11-30

  * New endpoint for Convert:
    * `GET /sapi/v1/convert/tradeFlow` to support user query convert trade history records



Was this page helpful?

Last modified on November 12, 2026

[Introduction](/en/docs/products/convert/Introduction)[General Info](/en/docs/products/convert/general-info)

---

# 更新日志

## 2025-12-26

### 时效性通知

  * **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** 调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/zh-CN/docs/products/convert/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。



### REST API

  * 更新了 REST API 文档中有关于 [签名请求示例](/zh-CN/docs/products/convert/general-info#post-apiv3order-%E7%9A%84%E7%AD%BE%E5%90%8D%E7%A4%BA%E4%BE%8B) 的部分。



* * *

## 2024-01-24

  * 新增闪兑接口:
    * `POST /sapi/v1/convert/limit/placeOrder`：创建闪兑限价单
    * `POST /sapi/v1/convert/limit/cancelOrder`：取消闪兑限价单
    * `GET /sapi/v1/convert/limit/queryOpenOrders`：查询闪兑限价单



* * *

## 2022-11-22

  * 新增闪兑接口：
    * `GET /sapi/v1/convert/exchangeInfo`: 查询可交易的币对的信息，以及它们分别所支持交易金额的上下限。
    * `GET /sapi/v1/convert/assetInfo`: 查询每个可交易币种的精度信息。
    * `POST /sapi/v1/convert/getQuote`: 对所需的币对发送获取报价请求。
    * `POST /sapi/v1/convert/acceptQuote`: 通过 quote ID 来接受报价。
    * `GET /sapi/v1/convert/orderStatus`: 通过 order ID 来查询订单状态。



* * *

## 2022-08-18

  * 更新闪兑接口：
    * `GET /sapi/v1/convert/tradeFlow`: 权重自 Weight(IP) 3000 改至 Weight(UID) 3000。



* * *

## 2022-07-01

  * 更新闪兑接口：
    * `GET /sapi/v1/convert/tradeFlow`：权重自 3000 改至 100。



* * *

## 2021-11-30

  * 新增闪兑接口:
    * 新增接口 `GET /sapi/v1/convert/tradeFlow` 以支持用户查询闪兑交易历史记录



此页面是否有帮助？

Last modified on November 12, 2026

[概述](/zh-CN/docs/products/convert/Introduction)[基本信息](/zh-CN/docs/products/convert/general-info)