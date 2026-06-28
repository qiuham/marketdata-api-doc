---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams
api_type: WebSocket
updated_at: 2026-01-15T23:43:38.627304
---

# Connect

* The baseurl of the websocket interface is: **wss://fstream.binance.com/public/ ** or **/ **wss://fstream.binance.com/market/**

  * Streams can be access either in a single raw stream or a combined stream

  * Raw streams are accessed at **/ws/ <streamName>**

  * Combined streams are accessed at **/stream?streams= <streamName1>/<streamName2>/<streamName3>**

  * Example:

    * `wss://fstream.binance.com/public/ws/btc-210630-9000-p@ticker`
    * `wss://fstream.binance.com/market/stream?streams=btc-210630-9000-p@markPriceoptionMarkPrice`
  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark

  * The websocket server will send a `ping frame` every 5 minutes. If the websocket server does not receive a `pong frame` back from the connection within a 15 minute period, the connection will be disconnected. Unsolicited `pong frames` are allowed.

  * WebSocket connections have a limit of 10 incoming messages per second.

  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.

  * A single connection can listen to a maximum of **200** streams.

  * Considering the possible data latency from RESTful endpoints during an extremely volatile market, it is highly recommended to get the order status, position, etc from the Websocket user data stream.

  * Combined stream events are wrapped as follows: **{"stream":" <streamName>","data":<rawPayload>}**

  * All symbols for streams are **lowercase**

  * A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark

  * The websocket server will send a `ping frame` every 5 minutes. If the websocket server does not receive a `pong frame` back from the connection within a 15 minute period, the connection will be disconnected. Unsolicited `pong frames` are allowed.

  * WebSocket connections have a limit of 10 incoming messages per second.

  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.

  * A single connection can listen to a maximum of **200** streams.

  * Considering the possible data latency from RESTful endpoints during an extremely volatile market, it is highly recommended to get the order status, position, etc from the Websocket user data stream.

---

# 连接

* Base Url：**wss://fstream.binance.com/public/** or **wss://fstream.binance.com/market/**

  * 订阅单一stream格式为 **/ws/ <streamName>**

  * 组合streams的URL格式为 **/stream?streams= <streamName1>/<streamName2>/<streamName3>**

  * 连接样例：

    * `wss://fstream.binance.com/public/ws/btc-210630-9000-p@ticker`
    * `wss://fstream.binance.com/market/stream?streams=btc-210630-9000-p@markPriceoptionMarkPrice`
  * 订阅组合streams时，事件payload会以这样的格式封装 **{"stream":" <streamName>","data":<rawPayload>}**

  * 订阅stream的交易对需要**小写**

  * 每个链接有效期不超过24小时，请妥善处理断线重连。

  * 服务端每5分钟会发送ping帧，客户端应当在15分钟内回复pong帧，否则服务端会主动断开链接。允许客户端发送不成对的pong帧(即客户端可以以高于15分钟每次的频率发送pong帧保持链接)。

  * Websocket服务器每秒最多接受10个订阅消息。

  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。

  * 单个连接最多可以订阅 **200** 个Streams。