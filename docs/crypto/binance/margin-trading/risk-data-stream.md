---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/margin-trading/risk-data-stream
api_type: REST
updated_at: 2026-11-13 20:28:35.174527
---

# Risk Data Stream

## Connect

  * Margin websocket only support Cross Margin Accounts
  * The base API endpoint is: **<https://api.binance.com>**
  * A User Data Stream `listenKey` is valid for 60 minutes after creation.
  * Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes.
  * Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
  * Doing a `POST` on an account with an active `listenKey` will return the currently active `listenKey` and extend its validity for 60 minutes.
  * A `listenKey` is a stream.
  * Users can listen to multiple streams.
  * The base websocket endpoint is: **wss://margin-stream.binance.com**
  * User Data Streams are accessed at **/ws/ <listenKey>** or **/stream?streams= <listenKey>**
  * A single connection to **stream.binance.com** is only valid for 24 hours; expect to be disconnected at the 24 hour mark



* * *

## Event: Margin Call

### Description

Margin call trigger the event

### Event Name

`MARGIN_LEVEL_STATUS_CHANGE`

### Payload

> **Schema:** [`marginLevelStatusChange`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#marginlevelstatuschange)

Loading schema...

* * *

## Event: Liability Update

### Description

Liability update during the following:

  * Borrowing
  * Repayment
  * Interest Calculation



### Event Name

`USER_LIABILITY_CHANGE`

### Payload

> **Schema:** [`userLiabilityChange`](/en/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#userliabilitychange)

Loading schema...

Was this page helpful?

Last modified on November 12, 2026

[Change Log](/en/docs/products/margin-trading/change-log)[(deprecated) Trade Data Stream](/en/docs/products/margin-trading/trade-data-stream)

---

# 风险数据流

## 连接

  * 以下文档目前仅支持全仓杠杆账户
  * 本篇所列出 API 接口的 base URL : **<https://api.binance.com>**
  * 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟。
  * 可以通过 `PUT` 一个 `listenKey` 延长60分钟有效期。
  * 可以通过 `DELETE` 一个 `listenKey` 立即关闭当前数据流，并使该 `listenKey` 无效。
  * 在具有有效 `listenKey` 的帐户上执行`POST`将返回当前有效的 `listenKey` 并将其有效期延长60分钟。
  * 一个`listenKey`就是一个数据流。
  * 用户可以侦听/订阅数个数据流。
  * websocket 接口的 base URL: **wss://margin-stream.binance.com**
  * 订阅账户数据流的 stream 名称为 **/ws/ <listenKey>** 或 **/stream?streams= <listenKey>**
  * 每个链接有效期不超过24小时，请妥善处理断线重连。



* * *

## Margin Call事件

### 事件描述

在用户 margin 账户发生 margin call 事件时，会推送此事件

### 事件类型

`MARGIN_LEVEL_STATUS_CHANGE`

### Payload

> **Schema:** [`marginLevelStatusChange`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#marginlevelstatuschange)

Loading schema...

* * *

## 负债变化事件

### 事件描述

当下列情形发生时，会推送此事件:

  * 借款
  * 计息
  * 还款



### 事件类型

`USER_LIABILITY_CHANGE`

### Payload

> **Schema:** [`userLiabilityChange`](/zh-CN/docs/catalog/core-trading-margin-trading/api/ws-streams/~schemas#userliabilitychange)

Loading schema...

此页面是否有帮助？

Last modified on November 12, 2026

[更新日志](/zh-CN/docs/products/margin-trading/change-log)[（已弃用）交易数据流](/zh-CN/docs/products/margin-trading/trade-data-stream)