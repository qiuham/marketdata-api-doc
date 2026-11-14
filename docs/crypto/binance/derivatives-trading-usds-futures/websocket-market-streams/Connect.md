---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Connect
api_type: WebSocket
updated_at: 2026-11-13 20:27:35.366747
---

# Websocket Market Streams

* The connection method for Websocket is：
    * Base Url: **wss://fstream.binance.com**
    * Three routed endpoints are available based on data type:
      * **Public** (high-frequency public market data): `wss://fstream.binance.com/public`
      * **Market** (regular market data): `wss://fstream.binance.com/market`
      * **Private** (user data): `wss://fstream.binance.com/private`
    * Two access modes are supported:
      * `ws` mode: streams are composed in the URL path — **/ws/ <streamName>**
      * `stream` mode: streams are passed via query parameters — **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
    * Examples:
      * `wss://fstream.binance.com/market/ws/bnbusdt@aggTrade`
      * `wss://fstream.binance.com/public/ws/bnbusdt@depth/ethusdt@depth`
      * `wss://fstream.binance.com/market/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice`



> **Important:** Connections that do not include a routed path (`/public`, `/market`, or `/private`) will only receive data from the **Public** endpoint. Streams belonging to `/market` or `/private` will not push data on unrouted connections. For example, `wss://fstream.binance.com/ws/btcusdt@depth` will continue to work (since `@depth` belongs to `/public`), but `wss://fstream.binance.com/ws/btcusdt@markPrice` will not (since `@markPrice` belongs to `/market`). See [Important WebSocket Change Notice](/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Important-WebSocket-Change-Notice) for the full stream-to-endpoint mapping and migration details.

  * Combined stream events are wrapped as follows: **{"stream":" <streamName>","data":<rawPayload>}**
  * All symbols for streams are **lowercase**
  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark
  * The websocket server will send a `ping frame` every 3 minutes. If the websocket server does not receive a `pong frame` back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited `pong frames` are allowed(the client can send pong frames at a frequency higher than every 15 minutes to maintain the connection).
  * WebSocket connections have a limit of 10 incoming messages per second.
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of **1024** streams.
  * Considering the possible data latency from RESTful endpoints during an extremely volatile market, it is highly recommended to get the order status, position, etc from the Websocket user data stream.



Was this page helpful?

Last modified on November 12, 2026

[Error Codes](/en/docs/products/derivatives-trading-usds-futures/error-code)[How to manage a local order book correctly](/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly)

---

# 市场数据连接

* 本篇所列出的所有wss接口需用下列方式连接：
    * Base Url：**wss://fstream.binance.com**
    * 三个分流入口，按数据类型分别接入：
      * **Public** （高频公共行情/盘口数据）：`wss://fstream.binance.com/public`
      * **Market** （常规公共市场数据）：`wss://fstream.binance.com/market`
      * **Private** （用户私有数据）：`wss://fstream.binance.com/private`
    * 支持两种访问模式：
      * `ws` 模式：通过 URL path 拼接订阅流 — **/ws/ <streamName>**
      * `stream` 模式：通过 query 参数传入 — **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
    * 连接样例：
      * `wss://fstream.binance.com/market/ws/bnbusdt@aggTrade`
      * `wss://fstream.binance.com/public/ws/bnbusdt@depth/ethusdt@depth`
      * `wss://fstream.binance.com/market/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice`



> **重要提示：** 如果连接 URL 中未指定分流路径（`/public`、`/market` 或 `/private`），则该连接将仅能接收 **Public** 类别的数据。属于 `/market` 或 `/private` 类别的 stream 将不会推送数据。例如，`wss://fstream.binance.com/ws/btcusdt@depth` 仍可正常接收（因为 `@depth` 属于 `/public`），但 `wss://fstream.binance.com/ws/btcusdt@markPrice` 将无法接收（因为 `@markPrice` 属于 `/market`）。各 stream 与入口的完整映射关系及迁移说明，请参考 [WebSocket Base URL 迁移公告](/zh-CN/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Important-WebSocket-Change-Notice)。

  * 订阅组合streams时，事件payload会以这样的格式封装 **{"stream":" <streamName<","data":<rawPayload>}**
  * stream名称中所有交易对均为**小写** 。
  * 每个链接有效期不超过24小时，请妥善处理断线重连。
  * 服务端每3分钟会发送ping帧，客户端应当在10分钟内回复pong帧，否则服务端会主动断开链接。允许客户端发送不成对的pong帧(即客户端可以以高于15分钟每次的频率发送pong帧保持链接)。
  * Websocket服务器每秒最多接受10个订阅消息。
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅 **1024** 个Streams。



此页面是否有帮助？

Last modified on November 12, 2026

[错误代码](/zh-CN/docs/products/derivatives-trading-usds-futures/error-code)[如何正确在本地维护一个 orderbook 副本](/zh-CN/docs/products/derivatives-trading-usds-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly)