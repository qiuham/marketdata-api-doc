---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-sbe-market-data
anchor_id: order-book-trading-sbe-market-data
api_type: API
updated_at: 2026-06-28 19:37:24.490320
---

# SBE Market Data

### Overview

OKX supports Simple Binary Encoding (SBE) for data returned from the following WebSocket channels:

  * [WS / Trades channel](/docs-v5/en/#order-book-trading-market-data-ws-trades-channel): `trades`
  * [WS / Order book channel](/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel): `bbo-tbt` and `books-l2-tbt`

### XML Schema

The SBE XML schema is now available for download:

[ __Download XML Schema](/docs-v5/log_en/xml/okx_sbe_1_0.xml)

### General Information

  * The `bbo-tbt` channel is **available to users of any trading fee tier** but requires login. The `trades` and `books-l2-tbt` channels are restricted to users with a trading fee tier of **VIP4** or above in the live trading environment. Other users will receive error code 64003. In the demo trading environment, these channels require **VIP1** or above.  

  * SBE channels will use a new WebSocket URL.  
Live trading: `wss://ws.okx.com:8443/ws/v5/public-sbe`  
Demo trading: `wss://wspap.okx.com:8443/ws/v5/public-sbe`   

  * Both JSON and SBE format data will be available on the same connection, distinguishable by WebSocket frame type. opcode `1` indicates JSON, while opcode `2` indicates SBE.  

  * Prices and quantities will be encoded as exponential decimals, using a signed integer mantissa and signed exponent. For example, a mantissa of 123456 and a exponent of -4 represents 12.3456 (actual value = mantissa * 10 ^ exponent).  

  * The SBE protocol will use `instIdCode` , an integer will be provided by [Get instruments](/docs-v5/en/#public-data-rest-api-get-instruments) to represent trading instruments. Users must map `instIdCode` to `instId`, noting that `instIdCode` will change if a trading symbol is relisted, but `instIdCode` will remains unchanged when `instId` is renamed.  

  * `tsUs` and `outTime` come from different servers, so their relative order is not guaranteed.
  * `tsUs` is in microseconds format but only accurate to milliseconds. The microseconds-format timestamp is obtained by appending 000 to the millisecond timestamp. For example, if the millisecond timestamp is 1726233600001, the related microseconds-format timestamp (tsUs) will be 1726233600001000.

### Integration Information

  * To log in, transmit your API key and signature in the WebSocket connection header.  

    * The connection requests must contain the following headers:  

      * `OK-ACCESS-KEY` The API key as a String.  

      * `OK-ACCESS-SIGN` The Base64-encoded signature.  

      * `OK-ACCESS-TIMESTAMP` Unix Epoch time in seconds. e.g : `1751335333`  

      * `OK-ACCESS-PASSPHRASE` The passphrase you specified when creating the API key.  

    * The `OK-ACCESS-SIGN` header is generated as follows:  

      * Create a pre-hash string of timestamp + method + requestPath  

      * Prepare the SecretKey.  

      * Sign the pre-hash string with the SecretKey using the HMAC SHA256.  

      * Encode the signature in the Base64 format. Example: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/users/self/verify', SecretKey))  

      * Example of timestamp: const timestamp = '' + Date.now() / 1,000, e.g. 1704876947  

      * Method: always 'GET'.  

      * RequestPath : always '/users/self/verify'  

    * The response HTTP code of `101` indicates the successful login.  

    * The response HTTP code `401`, along with an error message in the response body, indicates a failed login. The error message will be in JSON fromat.  

    
    
    Login error message example
    {
        "msg": "Invalid apiKey",
        "code": "60005",
        "connId":"24a2aea3"
    }
    

  * Subscription request must be sent in JSON format. The response will also be in JSON format, and can be identified by opcode `1`.  

    * The protocol is similar to existing JSON-formatted subscription requests/response.  

    * The difference is that `instIdCode` should be used instead of instId.  

    
    
    Subscription request example
    {
        "op": "subscribe",
        "args": [
            {
                "channel": "trades",
                "instIdCode": 211874
            }
        ]
    }
    
    Subscription response example
    {
        "event": "subscribe",
        "arg": {
            "channel": "trades",
            "instIdCode": 211874
        },
        "connId": "accb8e21"
    }
    

  * The notice event is supported in JSON format: 

    
    
    Notice event example
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  * The WebSocket server will send a ping frame with opcode `9` every 20 seconds after receiving a pong frame.  

    * If the WebSocket server does not receive a pong frame back from the connection within 60 secondes, the connection will be disconnected.  

    * Upon receiving a ping, you must respond with a pong frame using opcode `10`, along with a copy of the ping‘s payload as soon as possible (payload will be a random numerical text like 11446744073709551615).  

    * Unsolicited pong frames are permitted but will not prevent disconnection. It is advisable that the payload for these pong frames be empty.  

  * For `trades` `bbo-tbt` and `books-l2-tbt` channels, data will be returned in binary format and can be identified by opcode `2`, distinguishable by template ID. Key differences compared to existing JSON-formatted connections include:  

    * For the `trades` channel, the `seqId` will be returned.  

    * For the `bbo-tbt` channel, it usually provides real-time data, but under system overload, data loss can occur, varying by different connection.  

    * For the `books-l2-tbt`:  

      * When prices and quantities decimals change, a exponent update (template ID: 1002) will occur with previous sequence ID and sequence ID, identifiable by template ID. This must be processed to maintain the sequence ID consistence.  

      * The checksum will no longer be included.  

      * There will be no initial order book snapshot after subscription. Instead, OKX will provide a REST API endpoint that returns SBE binary data for the initial 400 levels snapshot. This endpoint will buffer requests and return data only when a new snapshot is generated, approximately every 500 ms.  

  * The relationship between the channel and event is not one-to-one. The books-l2-tbt contains two types of events. The mapping is outlined below.

Channel | XML Template ID and message name  
---|---  
bbo-tbt | 1000: BboTbtChannelEvent  
books-l2-tbt | 1001: BooksL2TbtChannelEvent  
1002: BooksL2TbtExponentUpdateEvent  
books-l2-tbt-elp   
(It is not enabled) | 1003: BooksL2TbtElpChannelEvent  
1004: BooksL2TbtElpExponentUpdateEvent  
trades | 1005: TradesChannelEvent  
  
  * How to manage a local order book correctly

    1. Open a SBE WebSocket connection and subscribe to `books-l2-tbt`.
    2. Buffer the events received from the stream. Record the prevSeqId of the first event you received.   
Note: For template ID 1002, the event is an exponent update, containing only exponent update information without ask or bid data. For template ID 1001, the data includes both asks and bids.
    3. Get a depth snapshot from `/books-sbe`, e.g. `https://openapi.okx.com/api/v5/market/books-sbe?instIdCode=12345&source=0`
    4. If the `seqId` from the snapshot is strictly less than the `prevSeqId` from step 2, go back to step 3.
    5. In the buffered events, discard any event where stream `seqId` is <= snapshot `seqId` of the snapshot. 
    6. The first buffered event should satisfy the condition: stream `prevSeqId` <= snapshot `seqId` < stream `seqId`.
    7. Set your local order book to the snapshot. Its sequence ID is snapshot `seqId`.
    8. Apply the update procedure below to all buffered events, and then to all subsequent events received. 
       * If the template ID is 1002 (BooksL2TbtExponentUpdateEvent), only update the exponents without bid and ask data. If the template ID is 1001 (BooksL2TbtChannelEvent), follow the process outlined below.
       * For each price level in bids and asks, set the new quantity in the order book: 
         * If the price level does not exist in the order book, insert it with new quantity.
         * If the quantity is zero, remove the price level from the order book.
       * Set the order book sequence ID to the latest sequence ID (`seqId`) in the processed event.   
Note: Not all snapshot `seqId` will appear in the `books-l2-tbt` channels.
  * Sequence ID  

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `instIdCode` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.  

Exceptions:  
1\. If there are no updates to the depth for an extended period(Around 60 seconds), for the channel that always updates snapshot data, OKX will send the latest snapshot, for the channel that has incremental data, OKX will send a message with numInGroup: 0 to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`.  
2\. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

  1. Incremental message 1 (normal update): prevSeqId = 10, seqId = 15
  2. Incremental message 2 (no update): prevSeqId = 15, seqId = 15
  3. Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3
  4. Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

### SBE Order book

It is a public endpoint, returning SBE binary data for the initial 400 levels snapshot. This endpoint will buffer requests and return data only when a new snapshot is generated, approximately every 500 ms.  
  

Note: If the request fails, the error message will be provided in JSON format.  
  

For the HTTP request header, it doesn't need to be set to `application/sbe`; however, the response header will be `Content-Type`: `application/sbe` if the request is successful, and `Content-Type`: `application/json` if the request fails.

#### Rate Limit: 10 requests per 10 seconds

#### Rate limit rule: IP + instIdCode

#### HTTP Request

`GET /api/v5/market/books-sbe`

> Request Example
    
    
    GET /api/v5/market/books-sbe?instIdCode=12345&source=0
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instIdCode | Integer | Yes | Instruement ID code  
source | Integer | Yes | The source of order book.  
`0`: normal  
  
> Response Example
    
    
    Error message example
    
    Response header: 
    Content-Type: application/json
    
    Response body:
    {
        "code": "51000",
        "msg": "Parameter instIdCode error",
        "data": []
    }
    

#### Response Parameters

Please refer to the `SnapshotDepthResponseEvent` with ID `1006` in the XML schema.

### New error code

Error Code | HTTP Status | Error Message  
---|---|---  
60034 | 401 | Only users who are {0} and above in trading fee tier are allowed to use this URL.  
  
### Upgrade

  * In general, only compatible upgrades are made, such as adding a new field. In these cases, the XML schema ID remains unchanged, while the schema version is incremented.
  * If a breaking change is needed, a new XML schema with a new schema ID will be released at least 1–2 months in advance. Before the end of the transition period, you’ll need to support both the old and new schemas, based on their schema ID and version.

---

# SBE 行情数据

### 概述

以下 WebSocket 频道返回的数据支持简单二进制编码（SBE）：

  * [WS / 交易频道](/docs-v5/zh/#order-book-trading-market-data-ws-trades-channel)：`trades`
  * [WS / 深度频道](/docs-v5/zh/#order-book-trading-market-data-ws-order-book-channel)：`bbo-tbt` 和 `books-l2-tbt`

### XML Schema

SBE XML schema 已经发布：

[ __下载 XML Schema](/docs-v5/log_zh/xml/okx_sbe_1_0.xml)

### 基本信息

  * `bbo-tbt` 频道**无用户等级限制** ，但需登录后方可订阅；`trades` 与 `books-l2-tbt` 频道在实盘环境仅对交易费等级 **VIP4 及以上** 用户开放，其他用户接入将收到错误码64003。在模拟盘环境仅对交易费等级 **VIP1** 及以上 用户开放。  

  * SBE 频道将使用新的 WebSocket URL。  
实盘交易：`wss://ws.okx.com:8443/ws/v5/public-sbe`  
模拟盘交易：`wss://wspap.okx.com:8443/ws/v5/public-sbe`   

  * 同一个连接上会同时存在 JSON 和 SBE 格式的数据，可以通过 WebSocket 帧类型区分。opcode `1` 表示 JSON，opcode `2` 表示 SBE。  

  * 价格和数量将会使用尾数和指数来表示。例如，尾数为 123456，指数为 -4，表示 12.3456（实际值 = 尾数 * 10 ^ 指数）。  

  * [获取交易产品基础信息](/docs-v5/zh/#public-data-rest-api-get-instruments) 接口会新增整数类型的 `instIdCode` 字段，SBE 协议将会使用该字段代表交易产品，用户需要将 `instIdCode` 映射为 `instId`. 请注意 `instIdCode` 在交易产品重新上币时会发生改变，然而，`instIdCode` 在 `instId` 重命名时保持不变。  

  * `tsUs` 和 `outTime` 来自不同的服务，因此它们的相对顺序无法保证。
  * `tsUs` 是微秒格式时间戳，但是仅精确到毫秒。毫秒时间加上 `000` 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (tsUs) 为 1726233600001000。

### 接入信息

  * 需在 WebSocket 连接请求头中添加 API key 和 签名进行登录：  

    * 连接请求必须包含以下内容：  

      * `OK-ACCESS-KEY`：API 密钥，字符串格式。  

      * `OK-ACCESS-SIGN`：Base64 编码的签名。  

      * `OK-ACCESS-TIMESTAMP`：Unix Epoch 时间（秒），例如：`1751335333`。  

      * `OK-ACCESS-PASSPHRASE`：创建 API 密钥时指定的 Passphrase。  

    * `OK-ACCESS-SIGN` 头的生成方式如下：  

      * 准备签名前字符串：`timestamp + method + requestPath`  

      * 准备 SecretKey。  

      * 使用 HMAC SHA256 算法对签名前字符串进行签名。  

      * 将签名编码为 Base64 格式。例如：sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp + 'GET' + '/users/self/verify', SecretKey))  

      * `timestamp` 示例：const timestamp = '' + Date.now() / 1,000，例如 `1704876947`。  

      * `method`：始终为 'GET'。  

      * `requestPath`：始终为 '/users/self/verify'。  

    * HTTP 响应状态码 `101` 表示登录成功。  

    * HTTP 响应状态代码 `401` 表示登录失败，响应体中会包含报错消息，报错消息采用 JSON 格式。  

    
    
    登录报错示例：
    {
        "msg": "Invalid apiKey",
        "code": "60005"
        "connId":"24a2aea3"
    }
    

  * 订阅请求必须以 JSON 格式发送，响应也将采用 JSON 格式，可通过 opcode `1`识别是否为 JSON 格式的消息。  

    * 协议类似于现有的 JSON 格式订阅请求/响应。  

    * 区别在于应该使用 `instIdCode` 而非 instId。  

    
    
    订阅请求示例
    {
        "op": "subscribe",
        "args": [
            {
                "channel": "trades",
                "instIdCode": 211874
            }
        ]
    }
    
    订阅响应示例
    {
        "event": "subscribe",
        "arg": {
            "channel": "trades",
            "instIdCode": 211874
        },
        "connId": "accb8e21"
    }
    

  * 通知事件支持 JSON 格式：

    
    
    通知事件示例
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  * 服务端在收到 pong 帧 20 秒后会发送一次操作码为 `9` 的 ping 帧。  

    * 如果 WebSocket 服务器在 60 秒内未收到 pong 帧，连接将自动断开。  

    * 收到 ping 帧后，需尽快以 opcode `10` 的 pong 帧响应，并复制 ping 帧的 `payload`（`payload`为随机数字文本，如 11446744073709551615）。  

    * 允许发送未经请求的 pong 帧，但无法阻止断开连接。建议这些 pong 帧的 `payload` 为空。  

  * 对于 `trades`、`bbo-tbt` 和 `books-l2-tbt` 频道，数据将以 SBE 二进制格式返回，可以通过 opcode `2` 识别，通过 template ID 区分频道。与现有的 JSON 格式连接相比，主要区别包括：  

    * 对于 `trades` 频道，返回 `seqId`。  

    * 对于 `bbo-tbt` 频道，提供实时数据，但在系统超载时可能会发生数据丢失，不同连接的数据可能会不一样。  

    * 对于 `books-l2-tbt`：  

      * 当价格和数量的小数位发生变化时，会推送指数更新消息（template ID: 1002），包含上一个推送的序列号和当前推送的序列号，可以通过 template ID 进行识别。为了保持序列号一致性，必须处理指数更新消息。  

      * 将不再返回 `checksum`。  

      * 订阅后不再推送初始快照数据。但是，欧易 将提供 REST API 接口：获取产品 SBE 深度，返回 SBE 二进制格式的 400 档快照数据。该接口约每 500 毫秒更新一次，收到请求后不会立刻返回，而是会待服务端缓存数据更新后立即返回最新数据。  

  * 频道与事件的关系不是一一对应的。books-l2-tbt 包含两种类型的事件。映射关系如下所示。

频道 | XML Template ID 和 message name  
---|---  
bbo-tbt | 1000: BboTbtChannelEvent  
books-l2-tbt | 1001: BooksL2TbtChannelEvent  
1002: BooksL2TbtExponentUpdateEvent  
books-l2-tbt-elp   
（未启用） | 1003: BooksL2TbtElpChannelEvent  
1004: BooksL2TbtElpExponentUpdateEvent  
trades | 1005: TradesChannelEvent  
  
  * 如何正确管理本地订单簿

    1. 打开 SBE WebSocket 连接并订阅 `books-l2-tbt` 频道。
    2. 缓存从频道中接收的事件。记录您接收到的第一个事件的 `prevSeqId`。  
注意：对于 template ID 1002 是指数更新事件，仅包含指数更新信息，不包含买入和卖出数据。对于模板ID 1001，会包含买入和卖出数据。
    3. 从 `/books-sbe` 获取深度快照，例如 `https://openapi.okx.com/api/v5/market/books-sbe?instIdCode=12345&source=0`
    4. 如果快照的 `seqId` 小于步骤 2 中的 `prevSeqId`，请返回步骤 3。
    5. 在缓存的事件中，丢弃事件 `seqId` <= 快照 `seqId` 的任何事件。
    6. 对于缓存中的第一个事件，满足该条件： `seqId`： 事件`prevSeqId` <= 快照 `seqId` < 事件 `seqId`。
    7. 将您的本地订单簿设置为本地快照。它的序列号就是快照 `seqId`。
    8. 对所有缓存的事件，使用下面的流程处理，同样适用于所有后续接收的事件。 
       * 如果 template ID 为 1002（BooksL2TbtExponentUpdateEvent），则仅更新指数，不包含买入和卖出数据。如果 template ID 为 1001（BooksL2TbtChannelEvent），则按照以下流程处理。
       * 对于 bids 和 asks 中的每组价格数据，在订单簿中更新数量： 
         * 如果价格数据在订单簿中不存在，则插入新数量。
         * 如果数量为零，则从订单簿中删除价格数据。
       * 将订单簿序列号设置为最新的序列号(`seqId`)。  
注意：不是所有快照 seqId 都会出现在 `books-l2-tbt` 频道中。
  * 序列号

`seqId`是交易所行情的一个序号。如果用户通过多个websocket连接同一频道，收到的序列号会是相同的。每个`instIdCode`对应一套。用户可以使用在增量推送频道的`prevSeqId`和`seqId`来构建消息序列。这将允许用户检测数据包丢失和消息的排序。正常场景下`seqId`的值大于`prevSeqId`。新消息中的`prevSeqId`与上一条消息的`seqId`匹配。最小序列号值为0，除了快照消息的`prevSeqId`为-1。  

异常情况：  
1\. 如果一段时间内（约 60 秒）没有深度更新，对于定量推送频道，OKX 会推送最近的一条更新，对于增量推送频道，OKX将发一条 numInGroup: 0 的消息以通知用户连接是正常的。推送的`seqId`跟上一条信息的一样，`prevSeqId`等于`seqId`。  
2\. 序列号可能由于维护而重置，在这种情况下，用户将收到一条`seqId`小于`prevSeqId`的增量消息。随后的消息将遵循常规的排序规则。

##### 示例

  1. 增量推送1（正常更新）：`prevSeqId = 10`，`seqId = 15`
  2. 增量推送2（无更新）：`prevSeqId = 15`，`seqId = 15`
  3. 增量推送3（序列重置）：`prevSeqId = 15`，`seqId = 3`
  4. 增量推送4（正常更新）：`prevSeqId = 3`，`seqId = 5`

### SBE 订单簿

这是一个公共接口，返回初始 400 档快照的 SBE 二进制数据。该接口约每 500 毫秒更新一次，收到请求后不会立刻返回，而是会待服务端缓存数据更新后立即返回最新数据。  
  

注意：如果请求失败，错误消息的格式将会是 JSON。  
  

对于 HTTP 请求头，不需要设置为 `application/sbe`；但是，如果请求成功，响应头为 `Content-Type`: `application/sbe`，如果请求失败，则为 `Content-Type`: `application/json`。

#### 限速：10 次/10 秒

#### 限速规则：IP + instIdCode

#### HTTP 请求

`GET /api/v5/market/books-sbe`

> 请求示例
    
    
    GET /api/v5/market/books-sbe?instIdCode=12345&source=0
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instIdCode | Integer | 是 | 产品 ID 唯一标识码。  
source | Integer | 是 | 订单簿的来源。  
`0`: 普通  
  
> 返回示例
    
    
    错误消息示例
    
    返回头：
    Content-Type: application/json
    
    返回 body：
    {
        "code": "51000",
        "msg": "Parameter instIdCode error",
        "data": []
    }
    

#### 返回参数

请参考 XML schema 中 ID 为 `1006` 的 `SnapshotDepthResponseEvent`。

### 新增错误码

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
60034 | 401 | 该频道仅支持手续费等级为 {0} 及以上的用户订阅使用  
  
### 升级

  * 通常情况下，升级是兼容的（例如新增一个字段）。这种情况下，XML schema ID 不会变化，但 schema version 会增加。
  * 如果涉及不兼容的变更，则会至少提前 1–2 个月发布新的 XML schema（使用新的 schema ID）。在过渡期结束前，你需要做好同时使用新旧 XML schema 处理数据的准备（基于他们的 schema ID 和 version）。