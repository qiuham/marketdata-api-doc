---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:23.930738
---

# Websocket Market Streams

* There are two connection methods for Websocket：

    * Base Url: **wss://dstream.binance.com**
    * Streams can be access either in a single raw stream or a combined stream
    * Raw streams are accessed at **/ws/ <streamName>**
    * Combined streams are accessed at **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
    * Example:
    * `wss://dstream.binance.com/ws/bnbusdt@aggTrade`
    * `wss://dstream.binance.com/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice`
  * Combined stream events are wrapped as follows: **{"stream":" <streamName>","data":<rawPayload>}**

  * All symbols for streams are **lowercase**

  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark

  * The websocket server will send a `ping frame` every 3 minutes. If the websocket server does not receive a `pong frame` back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited `pong frames` are allowed(Client can send `pong frames` with frequency higher than 10 minutes).

  * WebSocket connections have a limit of 10 incoming messages per second.

  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.

  * A single connection can listen to a maximum of **1024** streams.

  * Considering the possible data latency from RESTful endpoints during an extremely volatile market, it is highly recommended to get the order status, position, etc from the Websocket user data stream.

---

# 市场数据连接

* 本篇所列出的所有wss接口，共有如下两种连接方式：

    * 连接方式：
    * Base Url：**wss://dstream.binance.com**
    * 订阅单一stream格式为 **/ws/ <streamName>**
    * 组合streams的URL格式为 **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
    * 连接样例：
    * `wss://dstream.binance.com/ws/bnbusdt@aggTrade`
    * `wss://dstream.binance.com/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice`
  * 订阅组合streams时，事件payload会以这样的格式封装 **{"stream":" <streamName>","data":<rawPayload>}**

  * stream名称中所有交易对均为**小写** 。

  * 每个链接有效期不超过24小时，请妥善处理断线重连。

  * 服务端每3分钟会发送ping帧，客户端应当在10分钟内回复pong帧，否则服务端会主动断开链接。允许客户端发送不成对的pong帧(即客户端可以以高于10分钟每次的频率发送pong帧保持链接)。

  * Websocket服务器每秒最多接受10个订阅消息。

  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。

  * 单个连接最多可以订阅 **1024** 个Streams。