---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/algo/change-log
api_type: REST
updated_at: 2026-11-13 20:28:43.484382
---

# Change Log

## 2026-10-09

  * New endpoint for Spot Algo:
    * `POST /sapi/v1/algo/spot/newOrderVp` to support placing a new Volume Participation (VP) order



* * *

## 2026-08-25

### REST API

  * Added `clientAlgoId` as an optional parameter to cancel an algo order by client-defined ID. Either `algoId` or `clientAlgoId` must now be sent:
    * `DELETE /sapi/v1/algo/futures/order`
    * `DELETE /sapi/v1/algo/spot/order`



* * *

## 2025-12-26

### Time-sensitive Notice

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/en/docs/products/algo/error-code#-1022-invalid_signature). Please review and update your signing logic accordingly.



### REST API

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/en/docs/products/algo/general-info#signed-endpoint-examples-for-post-apiv3order).



* * *

## 2023-04-18

  * New endpoints for Spot Algo：
    * `POST /sapi/v1/algo/spot/newOrderTwap` to support new order
    * `DELETE /sapi/v1/algo/spot/order` to support cancel Algo order
    * `GET /sapi/v1/algo/spot/openOrders` to support query Algo open orders
    * `GET /sapi/v1/algo/spot/historicalOrders` to support query Algo historical orders
    * `GET /sapi/v1/algo/spot/subOrders` to support query Algo sub orders for a specified algoId



* * *

## 2022-04-27

  * New endpoint for Futures Algo：
    * `POST /sapi/v1/algo/futures/newOrderTwap` to support Twap new order



FAQ: [Time-Weighted Average Price(Twap) Introduction](https://www.binance.com/en/support/faq/093927599fd54fd48857237f6ebec0b0)

* * *

## 2022-04-13

  * New endpoints for Futures Algo：
    * `POST /sapi/v1/algo/futures/newOrderVp` to support VP new order
    * `DELETE /sapi/v1/algo/futures/order` to support cancel Algo order
    * `GET /sapi/v1/algo/futures/openOrders` to support query Algo open orders
    * `GET /sapi/v1/algo/futures/historicalOrders` to support query Algo historical orders
    * `GET /sapi/v1/algo/futures/subOrders` to support query Algo sub orders for a specified algoId



FAQ: [Volume Participation(VP) Introduction](https://www.binance.com/en/support/faq/b0b94dcc8eb64c2585763b8747b60702)

Was this page helpful?

Last modified on November 12, 2026

[Introduction](/en/docs/products/algo/Introduction)[General Info](/en/docs/products/algo/general-info)

---

# 更新日志

## 2026-10-09

  * 现货策略新增接口：
    * `POST /sapi/v1/algo/spot/newOrderVp` 支持发送成交量份额参与（VP）下单



* * *

## 2026-08-25

### REST API

  * 新增可选参数 `clientAlgoId`，支持通过用户自定义策略订单 ID 取消订单。现在必须发送 `algoId` 或 `clientAlgoId` 其中一个：
    * `DELETE /sapi/v1/algo/futures/order`
    * `DELETE /sapi/v1/algo/spot/order`



* * *

## 2025-12-26

### 时效性通知

  * **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** 调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/zh-CN/docs/products/algo/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。



### REST API

  * 更新了 REST API 文档中有关于 [签名请求示例](/zh-CN/docs/products/algo/general-info#post-apiv3order-%E7%9A%84%E7%AD%BE%E5%90%8D%E7%A4%BA%E4%BE%8B) 的部分。



* * *

## 2023-04-18

  * 新增现货策略交易接口：
    * `POST /sapi/v1/algo/spot/newOrderTwap` 以支持现货策略下单
    * `DELETE /sapi/v1/algo/spot/order` 以支持现货策略委托撤单
    * `GET /sapi/v1/algo/spot/openOrders` 以支持查询现货策略当前委托
    * `GET /sapi/v1/algo/spot/historicalOrders` 以支持查询现货策略历史订单
    * `GET /sapi/v1/algo/spot/subOrders` 以支持查询现货策略子订单



* * *

## 2022-04-27

  * 新增合约策略交易接口：
    * `POST /sapi/v1/algo/futures/newOrderTwap` 以支持合约 Twap 策略下单



FAQ: [时间加权平均价格策略(Twap) 介绍](https://www.binance.com/cn/support/faq/093927599fd54fd48857237f6ebec0b0)

* * *

## 2022-04-13

  * 新增合约策略交易接口：
    * `POST /sapi/v1/algo/futures/newOrderVp` 以支持合约 vp 策略下单
    * `DELETE /sapi/v1/algo/futures/order` 以支持合约策略委托撤单
    * `GET /sapi/v1/algo/futures/openOrders` 以支持查询合约策略当前委托
    * `GET /sapi/v1/algo/futures/historicalOrders` 以支持查询合约策略历史订单
    * `GET /sapi/v1/algo/futures/subOrders` 以支持查询合约策略子订单



FAQ: [成交量份额参与算法(VP) 介绍](https://www.binance.com/cn/support/faq/b0b94dcc8eb64c2585763b8747b60702)

此页面是否有帮助？

Last modified on November 12, 2026

[概述](/zh-CN/docs/products/algo/Introduction)[基本信息](/zh-CN/docs/products/algo/general-info)