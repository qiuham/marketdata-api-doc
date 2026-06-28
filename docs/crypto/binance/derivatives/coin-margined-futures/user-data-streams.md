---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams
api_type: REST
updated_at: 2026-01-15T23:40:04.186944
---

# User Data Streams Connect

* The base API endpoint is: **<https://dapi.binance.com>**

  * A User Data Stream `listenKey` is valid for 60 minutes after creation.

  * Doing a `PUT` on a `listenKey` will extend its validity for 60 minutes, if response `-1125` error "This listenKey does not exist." Please use `POST /dapi/v1/listenKey` to recreate `listenKey`.

  * Doing a `DELETE` on a `listenKey` will close the stream and invalidate the `listenKey`.

  * Doing a `POST` on an account with an active `listenKey` will return the currently active `listenKey` and extend its validity for 60 minutes.

  * There are two connection methods for Websocket：

    * Base Url 1: **wss://dstream.binance.com**

    * User Data Streams are accessed at **/ws/ <listenKey>**

    * Example: `wss://dstream.binance.com/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`

    * Base Url 2: **wss://dstream-auth.binance.com**

    * User Data Streams are accessed at **/ws/ <listenKey>?listenKey=<validateListenKey>**

    * **< validateListenKey> must be a valid listenKey when you establish a connection**

    * Example:

    * `wss://dstream-auth.binance.com/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh？listenKey=XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`

  * For one connection(one user data), the user data stream payloads can guaranteed to be in order during heavy periods; **Strongly recommend you order your updates using E**

  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark

---

# 账户信息流连接

* 本篇所列出REST接口的baseurl **<https://dapi.binance.com>**

  * 用于订阅账户数据的 `listenKey` 从创建时刻起有效期为60分钟

  * 可以通过`PUT`一个`listenKey`延长60分钟有效期，如收到`-1125`报错提示此`listenKey`不存在，建议重新使用`POST /dapi/v1/listenKey`生成`listenKey`

  * 可以通过`DELETE`一个 `listenKey` 立即关闭当前数据流，并使该`listenKey` 无效

  * 在具有有效`listenKey`的帐户上执行`POST`将返回当前有效的`listenKey`并将其有效期延长60分钟

  * 本篇所列出的websocket接口，共有如下两种连接方式：

    * 连接方式一：

    * Base Url: **wss://dstream.binance.com**

    * 订阅账户数据流的stream名称为 **/ws/` <listenKey>`**

    * 连接样例：

    * `wss://dstream.binance.com/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`

    * 连接方式二：

    * Base Url: **wss://dstream-auth.binance.com**

    * 订阅账户数据流的stream名称为 **/ws/` <listenKey>`?listenKey=<validateListenKey>**

    * **< validateListenKey>在建立连接时，必须为一个有效的listenKey**

    * 连接样例：

    * `wss://dstream-auth.binance.com/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh？listenKey=XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`

  * 每个链接有效期不超过24小时，请妥善处理断线重连。

  * 单一账户，单一连接的推送数据流消息可以保证时间序; **强烈建议您使用 E 字段进行排序**

  * 考虑到剧烈行情下, RESTful接口可能存在查询延迟，我们强烈建议您优先从Websocket user data stream推送的消息来获取订单，仓位等信息。