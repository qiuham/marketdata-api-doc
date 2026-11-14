---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/sbe-market-data-streams
api_type: Market Data
updated_at: 2026-11-13 20:24:41.725583
---

# SBE Market Data Streams

## General Information

  * The base endpoint is **stream-sbe.binance.com** or **stream-sbe.binance.com:9443**.
  * To retrieve market data in JSON format, please refer to [this page](/en/docs/products/spot/web-socket-streams).
  * SBE schema used for decoding the streams can be found [here](/en/docs/products/spot/sbe/schemas/stream_1_0.xml).
  * All symbols in stream names are **lowercase**.
  * You can subscribe to a single stream at **/ws/ <streamName>**.
  * You can subscribe to multiple streams at **/stream?streams= <streamName1>/<streamName2>/<streamName3>**.
  * A single connection to **stream-sbe.binance.com** is **only valid for 24 hours** ; expect to be disconnected at the 24 hour mark.
  * A [`serverShutdown`](/en/docs/products/spot/sbe-market-data-streams#server-shutdown) event will be sent when the server is about to shutdown, resulting in disconnection. Please establish a new connection as soon as possible to prevent interruption.
  * All time and timestamp fields are in **microseconds**.
  * **An API Key is necessary for access**.
    * Only Ed25519 keys are allowed.
    * Please put your API Key in the `X-MBX-APIKEY` header when opening the connection. Timestamp and signature are not necessary.
    * No extra API key permissions are necessary to access public market data. Symbol whitelist also does not affect access to SBE Market Data Streams.
    * However, if you use an IP whitelist for the API key, only specified IP addresses are allowed to use the API key.
  * The server sends a `ping frame` every 20 seconds.
    * If the server does not receive a `pong frame` back from you within a minute, the connection will be closed.
    * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
    * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
  * [Live Subscribing and Unsubscribing](/en/docs/products/spot/web-socket-streams#live-subscribingunsubscribing-to-streams) is also supported.
    * You must send subscription requests in JSON in WebSocket text frames. You will receive subscription responses in JSON in WebSocket text frames.
    * You will receive [`serverShutdown`](/en/docs/products/spot/sbe-market-data-streams#server-shutdown) events in JSON in WebSocket text frames.
    * You will receive market data events in SBE in WebSocket binary frames.
  * If your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.



## WebSocket Limits

  * WebSocket connections have a rate limit of **5 requests per second**.
    * Only messages from your client are considered:
      * `PING frame`
      * `PONG frame`
      * `Text frame` with JSON control request
    * Events pushed by the server are not rate-limited.
    * Connections that go beyond the limit will be closed. Repeatedly disconnected IP addresses may be banned.
  * A single connection can listen to a maximum of 1024 streams.
  * There is a limit of **300 connection attempts every 5 minutes per IP address**.



## Server Shutdown

`serverShutdown` event is sent when the server is about to shut down.

Note that this message will be in JSON.
    
    
    Code
    
    {
      "e": "serverShutdown", // Event type
      "E": 1770123456789,    // Event time
      "T": 1770124000000     // Upcoming shutdown time
    }

The `T` field indicates when the WebSocket session will be shut down.

Please establish a new connection as soon as possible to prevent interruption.

## Available Streams

### Trades Streams

Raw trade information, pushed in real-time.

**SBE Message Name:** `TradesStreamEvent`

**Stream Name** : <symbol>@trade

**Update Speed** : Real time

### Best Bid/Ask Streams

The best bid and ask price and quantity, pushed in real-time when the order book changes.

Best bid/ask streams in SBE are the equivalent of bookTicker streams in JSON, except they support auto-culling, and also include the `eventTime` field.

**SBE Message Name:** `BestBidAskStreamEvent`

**Stream Name** : <symbol>@bestBidAsk

**Update Speed** : Real time

SBE best bid/ask streams use **auto-culling** : when the system is under high load, it may drop outdated events instead of queuing all events and delivering them with a delay.

For example, if a best bid/ask event is generated at time T2 when there is still an undelivered event queued at time T1 (where T1 < T2), the event for T1 is dropped, and the system will deliver only the event for T2. This is done on a per-symbol basis.

### Diff. Depth Streams

Incremental updates to the order book, pushed at regular intervals. Use this stream to maintain a local order book.

[How to manage a local order book.](/en/docs/products/spot/web-socket-streams#how-to-manage-a-local-order-book-correctly)

**SBE Message Name:** `DepthDiffStreamEvent`

**Stream Name** : <symbol>@depth

**Update Speed:** 20ms

### Partial Book Depth Streams

Snapshots of the top 20 levels of the order book, pushed at regular intervals.

**SBE Message Name:** `DepthSnapshotStreamEvent`

**Stream Name** : <symbol>@depth20

**Update Speed:** 50ms

Was this page helpful?

Last modified on November 12, 2026

[FIX API](/en/docs/products/spot/fix-api)[SBE Schemas](/en/docs/products/spot/sbe/schemas/introduction)

---

# SBE 市场数据流

## WSS 基本信息

  * 基本访问地址是 **stream-sbe.binance.com** 或 **stream-sbe.binance.com:9443** 。
  * 要以 JSON 格式检索市场数据，请参阅 [此页面](/zh-CN/docs/products/spot/web-socket-streams)。
  * 可以在[此处](/zh-CN/docs/products/spot/sbe/schemas/stream_1_0.xml)找到用于对数据流进行解码的 SBE 模式。
  * stream 名称中所有交易对均为**小写** 。
  * 订阅单个streams时，可用的URL格式示例： **/ws/ <streamName>**。
  * 订阅组合streams时，可用的URL格式示例： **/stream?streams= <streamName1>/<streamName2>/<streamName3>**。
  * 每个到**stream-sbe.binance.com** 的链接有效期不超过24小时，请妥善处理断线重连。
  * 当服务器即将关闭时，系统将发送 [`serverShutdown`](/zh-CN/docs/products/spot/sbe-market-data-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 事件，并导致连接断开。请尽快建立新连接，以防止中断。
  * 所有时间和时间戳相关的字段均以 **微秒** 为单位。
  * **需要 API Key 身份验证。**
    * 只允许使用 Ed25519 密钥。
    * 打开连接时，请将您的 API Key 放在 `X-MBX-APIKEY` 标头中。时间戳和签名不是必需的。
    * 无需额外的 API 密钥权限即可访问公开市场数据。交易对白名单也不会影响对 SBE 市场数据流的访问。
    * 但是，如果 API 密钥使用 IP 白名单，则仅允许指定的 IP 地址使用 API 密钥。
  * WebSocket 服务器会**每20秒** 发送 PING 帧。
    * 如果websocket 服务器没有在一分钟之内收到 PONG 帧响应，连接会被断开。
    * 当客户收到 PING 帧，必须尽快回复 PONG 帧，同时 payload 需要和 PING 帧一致。
    * 服务器允许未经请求的 PONG 帧，但这不会保证连接不断开。**对于这种类型的 PONG 帧，建议设置其 payload 为空。**
  * [支持实时订阅和取消订阅](/zh-CN/docs/products/spot/web-socket-streams#%E5%AE%9E%E6%97%B6%E8%AE%A2%E9%98%85%E5%8F%96%E6%B6%88%E6%95%B0%E6%8D%AE%E6%B5%81)。
    * 您必须以 JSON 格式通过 WebSocket text 帧发送订阅请求；订阅响应也将以 JSON 格式通过 WebSocket text 帧返回。
    * [`serverShutdown`](/zh-CN/docs/products/spot/sbe-market-data-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 事件将以 JSON 格式通过 WebSocket text 帧发送。
    * 市场数据事件将以 SBE 格式通过 WebSocket 二进制帧发送。
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么数据流事件中可能包含以 UTF-8 编码的非 ASCII 字符。



## WebSocket 连接限制

  * WebSocket服务器**每秒最多接受5个消息** 。
    * 消息包括:
      * PING 帧
      * PONG 帧
      * Text 帧JSON格式的控制请求
    * 由服务器推送的事件不受速率限制。
    * 如果用户发送的消息数超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅1024个 Streams。
  * 每个IP地址的请求限制为 **每5分钟最多可以发送300次连接请求** 。



## 服务器关闭

当服务器即将关闭时，会发送 `serverShutdown` 事件。

请注意，此消息将以 JSON 格式发送。
    
    
    Code
    
    {
      "e": "serverShutdown", // 事件类型
      "E": 1770123456789,    // 事件时间
      "T": 1770124000000     // 即将关闭时间
    }

`T` 字段表示 WebSocket 会话的关闭时间。

请尽快建立新连接，以防中断。

## 可供用户使用的 Stream

### 逐笔交易

实时推送的原始交易信息

**SBE 消息名称:** `TradesStreamEvent`

**Stream 名称** : <symbol>@trade

**更新速度:** 实时

### 最优挂单信息

当订单簿发生变化时，会实时推送最优买入价和卖出价和数量。

**SBE 消息名称:** `BestBidAskStreamEvent`

**Stream 名称** : <symbol>@bestBidAsk

**更新速度** : 实时

SBE 最优挂单信息使用 **自动剔除（auto-culling）** ：当系统负载较高时，可能会丢弃过时的事件，而不是将所有事件排队并延迟发送。

例如，如果在时间 T2 生成了一个最优买/卖报价事件，而此时仍有一个未发送的事件排队在时间 T1（且 T1 < T2），则会丢弃时间 T1 的事件，系统只会发送时间 T2 的事件。此操作是基于每个交易对分别进行的。

### 增量深度信息

定期推送订单簿的增量更新。使用此流来维护本地订单簿。

[如何管理本地订单簿。](/zh-CN/docs/products/spot/web-socket-streams#%E5%A6%82%E4%BD%95%E6%AD%A3%E7%A1%AE%E5%9C%A8%E6%9C%AC%E5%9C%B0%E7%BB%B4%E6%8A%A4%E4%B8%80%E4%B8%AAorder-book%E5%89%AF%E6%9C%AC)

**SBE 消息名称:** `DepthDiffStreamEvent`

**Stream 名称** : <symbol>@depth

**更新速度:** 20ms

### 有限档深度信息

订单簿前 20 档的快照，定期推送。

**SBE 消息名称:** `DepthSnapshotStreamEvent`

**Stream 名称** : <symbol>@depth20

**更新速度:** 50ms

此页面是否有帮助？

Last modified on November 12, 2026

[FIX API](/zh-CN/docs/products/spot/fix-api)[SBE Schemas](/zh-CN/docs/products/spot/sbe/schemas/introduction)