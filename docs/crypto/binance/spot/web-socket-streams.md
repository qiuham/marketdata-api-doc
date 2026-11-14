---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/web-socket-streams
api_type: WebSocket
updated_at: 2026-11-13 20:27:24.531271
---

# General WebSocket Streams information

## General WSS information

  * The base endpoint is: **wss://stream.binance.com:9443** or **wss://stream.binance.com:443**.
  * Streams can be accessed either in a single raw stream or in a combined stream.
  * Raw streams are accessed at **/ws/ <streamName>**
  * Combined streams are accessed at **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
  * Combined stream events are wrapped as follows: **{"stream":" <streamName>","data":<rawPayload>}**
  * All symbols for streams are **lowercase**
  * A single connection to **stream.binance.com** is only valid for 24 hours; expect to be disconnected at the 24 hour mark.
  * A [`serverShutdown`](/en/docs/products/spot/web-socket-streams#server-shutdown) event will be sent when the server is about to shutdown, resulting in disconnection. Please establish a new connection as soon as possible to prevent interruption.
  * The WebSocket server will send a `ping frame` every 20 seconds.
    * If the WebSocket server does not receive a `pong frame` back from the connection within a minute the connection will be disconnected.
    * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
    * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
  * The base endpoint **wss://data-stream.binance.vision** can be subscribed to receive **only** market data messages.  User data stream is **NOT** available from this URL.
  * All time and timestamp related fields are **milliseconds by default**. To receive the information in microseconds, please add the parameter `timeUnit=MICROSECOND or timeUnit=microsecond` in the URL.
    * For example: `/stream?streams=btcusdt@trade&timeUnit=MICROSECOND`
  * If your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.
  * [All Market Mini Tickers Stream](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker) and [All Market Rolling Window Statistics Streams](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-market-rolling-window-ticker) events may contain non-ASCII characters encoded in UTF-8.



## WebSocket Limits

  * WebSocket connections have a limit of 5 incoming messages per second. A message is considered:
    * A PING frame
    * A PONG frame
    * A JSON controlled message (e.g. subscribe, unsubscribe)
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of 1024 streams.
  * There is a limit of **300 connections per attempt every 5 minutes per IP**.



## Server Shutdown

`serverShutdown` event is sent when the server is about to shut down.

  * `raw` stream:


    
    
    Code
    
    {
      "e": "serverShutdown", // Event type
      "E": 1770123456789,    // Event time
      "T": 1770124000000     // Upcoming shutdown time
    }

  * `combined` stream:


    
    
    Code
    
    {
      "stream": "!serverShutdown",
      "data": {
        "e": "serverShutdown", // Event type
        "E": 1770123456789,    // Event time
        "T": 1770124000000     // Upcoming shutdown time
      }
    }

The `T` field indicates when the WebSocket session will be shut down.

Please establish a new connection as soon as possible to prevent interruption.

## Live Subscribing/Unsubscribing to streams

  * The following data can be sent through the WebSocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
  * The `id` is used as an identifier to uniquely identify the messages going back and forth. The following formats are accepted:
    * 64-bit signed integer
    * alphanumeric strings; max length 36
    * `null`
  * In the response, if the `result` received is `null` this means the request sent was a success for non-query requests (e.g. Subscribing/Unsubscribing).



### Subscribe to a stream

  * Request
        
        Code
        
        {
            "method": "SUBSCRIBE",
            "params": ["btcusdt@aggTrade", "btcusdt@depth"],
            "id": 1
        }

  * Response
        
        Code
        
        {
            "result": null,
            "id": 1
        }




### Unsubscribe to a stream

  * Request
        
        Code
        
        {
            "method": "UNSUBSCRIBE",
            "params": ["btcusdt@depth"],
            "id": 312
        }

  * Response
        
        Code
        
        {
            "result": null,
            "id": 312
        }




### Listing Subscriptions

  * Request
        
        Code
        
        {
            "method": "LIST_SUBSCRIPTIONS",
            "id": 3
        }

  * Response
        
        Code
        
        {
            "result": ["btcusdt@aggTrade"],
            "id": 3
        }




### Setting Properties

Currently, the only property that can be set is whether `combined` stream payloads are enabled or not. The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true` when connecting using `/stream/`.

  * Request
        
        Code
        
        {
            "method": "SET_PROPERTY",
            "params": ["combined", true],
            "id": 5
        }

  * Response
        
        Code
        
        {
            "result": null,
            "id": 5
        }




### Retrieving Properties

  * Request
        
        Code
        
        {
            "method": "GET_PROPERTY",
            "params": ["combined"],
            "id": 2
        }

  * Response
        
        Code
        
        {
            "result": true, // Indicates that combined is set to true.
            "id": 2
        }




### Error Messages

Error Message| Description  
---|---  
{"code": 0, "msg": "Unknown property","id": %s}| Parameter used in the `SET_PROPERTY` or `GET_PROPERTY` was invalid  
{"code": 1, "msg": "Invalid value type: expected Boolean"}| Value should only be `true` or `false`  
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name provided was invalid  
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| Parameter `id` had to be provided or the value provided in the `id` parameter is an unsupported type  
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"}| Possible typo in the provided method or provided method was neither of the expected values  
{"code": 2, "msg": "Invalid request: too many parameters"}| Unnecessary parameters provided in the data  
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name was not provided  
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"}| `method` was not provided in the data  
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}| JSON data sent has incorrect syntax.  
  
## How to manage a local order book correctly

  1. Open a WebSocket connection to `wss://stream.binance.com:9443/ws/bnbbtc@depth`.
  2. Buffer the events received from the stream. Note the `U` of the first event you received.
  3. Get a depth snapshot from `https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=5000`.
  4. If the `lastUpdateId` from the snapshot is strictly less than the `U` from step 2, go back to step 3.
  5. In the buffered events, discard any event where `u` is <= `lastUpdateId` of the snapshot. The first buffered event should now have `lastUpdateId` within its `[U;u]` range.
  6. Set your local order book to the snapshot. Its update ID is `lastUpdateId`.
  7. Apply the update procedure below to all buffered events, and then to all subsequent events received.



To apply an event to your local order book, follow this update procedure:

  1. Decide whether the update event can be applied:
     * If the event last update ID (`u`) is less than the update ID of your local order book, ignore the event.
     * If the event first update ID (`U`) is greater than the update ID of your local order book + 1, you have missed some events.  Discard your local order book and restart the process from the beginning.
     * Normally, `U` of the next event is equal to `u + 1` of the previous event.
  2. For each price level in bids (`b`) and asks (`a`), set the new quantity in the order book:
     * If the price level does not exist in the order book, insert it with new quantity.
     * If the quantity is zero, remove the price level from the order book.
  3. Set the order book update ID to the last update ID (`u`) in the processed event.



Since depth snapshots retrieved from the API have a limit on the number of price levels (5000 on each side maximum), you won't learn the quantities for the levels outside of the initial snapshot unless they change.  So be careful when using the information for those levels, since they might not reflect the full view of the order book.  However, for most use cases, seeing 5000 levels on each side is enough to understand the market and trade effectively.

Was this page helpful?

Last modified on November 12, 2026

[WebSocket API](/en/docs/products/spot/web-socket-api)[FIX API](/en/docs/products/spot/fix-api)

---

# 通用 WebSocket 流信息

## 基本信息

  * 本篇所列出的所有wss接口的baseurl为: **wss://stream.binance.com:9443** 或者 **wss://stream.binance.com:443**
  * 所有stream均可以直接访问，或者作为组合streams的一部分。
  * 直接访问时URL格式为 **/ws/ <streamName>**
  * 组合streams的URL格式为 **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
  * 订阅组合streams时，事件payload会以这样的格式封装 **{"stream":" <streamName>","data":<rawPayload>}**
  * stream名称中所有交易对均为**小写**
  * 每个到**stream.binance.com** 的链接有效期不超过24小时，请妥善处理断线重连。
  * 当服务器即将关闭时，系统将发送 [`serverShutdown`](/zh-CN/docs/products/spot/web-socket-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 事件，并导致连接断开。请尽快建立新连接，以防止中断。
  * WebSocket 服务器**每20秒** 发送 PING 消息。
    * 如果 WebSocket 服务器没有在一分钟之内收到PONG 消息应答，连接会被断开。
    * 当客户收到PING消息，必须尽快回复PONG消息，同时payload需要和PING消息一致。
    * 服务器允许未经请求的PONG消息，但这不会保证连接不断开。**对于这些PONG 消息，建议payload为空。**
  * **wss://data-stream.binance.vision** 可以用来订阅仅有市场信息的数据流。账户信息**无法** 从此URL获得。
  * 所有时间和时间戳相关字段均以**毫秒为默认单位** 。 要以微秒为单位接收信息，请在 URL 中添加参数 `timeUnit=MICROSECOND` 或 `timeUnit=microsecond`。
    * 例如： `/stream?streams=btcusdt@trade&timeUnit=MICROSECOND`
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么数据流事件中可能包含以 UTF-8 编码的非 ASCII 字符。
  * [全市场所有 Symbol 的精简 Ticker](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker) 和 [全市场滚动窗口统计](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-market-rolling-window-ticker) 事件可能包含以 UTF-8 编码的非 ASCII 字符。



## WebSocket 连接限制

  * WebSocket服务器每秒最多接受5个消息。消息包括:
    * PING帧
    * PONG帧
    * JSON格式的消息, 比如订阅, 断开订阅.
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅1024个Streams。
  * 每IP地址、每5分钟最多可以发送300次连接请求。



## 服务器关闭

`serverShutdown` 事件在服务器即将关闭时发送。

  * `raw` 数据流：


    
    
    Code
    
    {
      "e": "serverShutdown", // 事件类型
      "E": 1770123456789,    // 事件时间
      "T": 1770124000000     // 即将关闭时间
    }

  * `combined` 数据流：


    
    
    Code
    
    {
      "stream": "!serverShutdown",
      "data": {
        "e": "serverShutdown", // 事件类型
        "E": 1770123456789,    // 事件时间
        "T": 1770124000000     // 即将关闭时间
      }
    }

`T` 字段表示 WebSocket 会话的关闭时间。

请尽快建立新的连接以避免中断。

## 实时订阅/取消数据流

  * 以下数据可以通过 WebSocket 发送以实现订阅或取消订阅数据流。示例如下.
  * 请求中的`id`被用作唯一标识来区分来回传递的消息。以下格式被接受:
    * 64位有符号整数
    * 字母数字字符串；最大长度36
    * `null`
  * 如果相应内容中的`result` 为 `null`，表示请求发送成功。



### 订阅一个信息流

  * 请求
        
        Code
        
        {
          "method": "SUBSCRIBE",
          "params": [
            "btcusdt@aggTrade",
            "btcusdt@depth"
          ],
          "id": 1
        }

  * 响应
        
        Code
        
        {
          "result": null,
          "id": 1
        }




### 取消订阅一个信息流

  * 请求
        
        Code
        
        {
          "method": "UNSUBSCRIBE",
          "params": [
            "btcusdt@depth"
          ],
          "id": 312
        }

  * 响应
        
        Code
        
        {
          "result": null,
          "id": 312
        }




### 已订阅信息流

  * 请求
        
        Code
        
        {
          "method": "LIST_SUBSCRIPTIONS",
          "id": 3
        }

  * 响应
        
        Code
        
        {
          "result": [
            "btcusdt@aggTrade"
          ],
          "id": 3
        }




### 设定属性

当前，唯一可以设置的属性是设置是否启用`combined`("组合")信息流。当使用`/ws/`("原始信息流")进行连接时，combined属性设置为`false`，而使用 `/stream/`进行连接时则将属性设置为`true`。

  * 请求
        
        Code
        
        {
          "method": "SET_PROPERTY",
          "params": [
            "combined",
            true
          ],
          "id": 5
        }

  * 响应
        
        Code
        
        {
          "result": null,
          "id": 5
        }




### 检索属性

  * 请求
        
        Code
        
        {
          "method": "GET_PROPERTY",
          "params": [
            "combined"
          ],
          "id": 2
        }

  * 响应
        
        Code
        
        {
          "result": true, // Indicates that combined is set to true.
          "id": 2
        }




### 错误信息

错误信息| 描述  
---|---  
{"code": 0, "msg": "Unknown property","id": %s}| `SET_PROPERTY` 或 `GET_PROPERTY`中应用的参数无效  
{"code": 1, "msg": "Invalid value type: expected Boolean"}| 仅接受`true`或`false`  
{"code": 2, "msg": "Invalid request: property name must be a string"}| 提供的属性名无效  
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| 参数`id`未提供或`id`值是无效类型  
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"}| 错字提醒，或提供的值不是预期类型  
{"code": 2, "msg": "Invalid request: too many parameters"}| 数据中提供了不必要参数  
{"code": 2, "msg": "Invalid request: property name must be a string"}| 未提供属性名  
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"}| 数据未提供`method`  
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}| JSON 语法有误.  
  
## 如何正确在本地维护一个order book副本

  1. 打开与 `wss://stream.binance.com:9443/ws/bnbbtc@depth` 的 WebSocket 连接。
  2. 开始缓存收到的event。请记录您收到的第一个event的 `U`值。
  3. 访问 `https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=5000` 获取深度快照。
  4. 如果快照中的 `lastUpdateId` 小于等于步骤 2 中的 `U` 值，请返回步骤 3。
  5. 在收到的event中，丢弃快照中 `u` <= `lastUpdateId` 的所有event。现在第一个event的 `lastUpdateId` 应该在 `[U;u]` 范围以内。
  6. 将本地order book设置为快照。它的更新ID 为 `lastUpdateId`。
  7. 更新所有缓存的event，以及后续的所有event。



要将一个event应用于您的本地order book，请遵循以下更新过程：

  1. 判断是否需要处理event：
     * 如果event的最后一次更新ID（`u`）小于本地order book的更新ID，忽略该event。
     * 如果event的首次更新ID（`U`）大于本地order book的更新ID加1，说明你错过了一些events。请丢弃您的本地order book并从头开始重新同步。
     * 通常，下一event的`U`等于上一event的`u + 1`。
  2. 对买价（`b`）和卖价（`a`）中的每个价位，设置order book中的新数量：
     * 如果该价位在order book中不存在，则插入该价位及其数量。
     * 如果数量为零，则从order book中删除此价位。
  3. 将order book的更新ID设置为已处理event的最后一次更新ID（`u`）。



由于从 API 检索的深度快照对价位的数量有限制（每侧最多 5000 个），因此除非它们发生变化，否则您将无法了解初始快照之外的价位数量。 因此，在使用这些级别的信息时要小心，因为它们可能无法反映订单簿的完整视图。 但是，对于大多数场景，可以每侧看到 5000 个价位就足以了解市场并进行有效交易。

此页面是否有帮助？

Last modified on November 12, 2026

[WebSocket API](/zh-CN/docs/products/spot/web-socket-api)[FIX API](/zh-CN/docs/products/spot/fix-api)