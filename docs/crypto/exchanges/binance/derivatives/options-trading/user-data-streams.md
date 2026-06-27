---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams
api_type: REST
updated_at: 2026-01-15T23:43:04.968964
---

# Connect

* The base API endpoint is: **<https://eapi.binance.com>**
  * A User Data Stream `listenKey` is valid for 60 minutes after creation.
  * Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes.
  * Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.
  * Doing a `POST` on an account with an active `listenKey` will return the currently active `listenKey` and extend its validity for 60 minutes.
  * Connection method for Websocket： 
    * Base Url: **wss://fstream.binance.com/private/**
    * User Data Streams are accessed at **/ws/ <listenKey>**
    * Example: `wss://fstream.binance.com/private/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark

---

# 连接

* 本篇所列出REST接口的baseurl **<https://eapi.binance.com>**

  * 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟

  * 可以通过`PUT`一个`listenKey`延长60分钟有效期

  * 可以通过`DELETE`一个 `listenKey` 立即关闭当前数据流，并使该`listenKey` 无效

  * 在具有有效`listenKey`的帐户上执行`POST`将返回当前有效的`listenKey`并将其有效期延长60分钟

  * websocket接口的连接方式如下：

    * Base Url: **wss://fstream.binance.com/private/**
    * 订阅账户数据流的stream名称为 **/ws/ <listenKey>**
    * 连接样例：
    * `wss://fstream.binance.com/private/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
  * 每个链接有效期不超过24小时，请妥善处理断线重连。

  * 考虑到剧烈行情下, RESTful接口可能存在查询延迟，我们强烈建议您优先从Websocket user data stream推送的消息来获取订单，仓位等信息。