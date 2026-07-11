---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket
anchor_id: overview-websocket
api_type: WebSocket
updated_at: 2026-07-11 19:11:55.488398
---

# WebSocket

### Overview

WebSocket is a new HTML5 protocol that achieves full-duplex data transmission between the client and server, allowing data to be transferred effectively in both directions. A connection between the client and server can be established with just one handshake. The server will then be able to push data to the client according to preset rules. Its advantages include:

  * The WebSocket request header size for data transmission between client and server is only 2 bytes.
  * Either the client or server can initiate data transmission.
  * There's no need to repeatedly create and delete TCP connections, saving resources on bandwidth and server.

We recommend developers use WebSocket API to retrieve market data and order book depth. 

### Connect

**Connection limit** : 3 requests per second (based on IP)

When subscribing to a public channel, use the address of the public service. When subscribing to a private channel, use the address of the private service

**Request limit** : 

The total number of 'subscribe'/'unsubscribe'/'login' requests per connection is limited to 480 times per hour.

If there’s a network problem, the system will automatically disable the connection. 

The connection will break automatically if the subscription is not established or data has not been pushed for more than 30 seconds. 

To keep the connection stable: 

1\. Set a timer of N seconds whenever a response message is received, where N is less than 30. 

2\. If the timer is triggered, which means that no new message is received within N seconds, send the String 'ping'. 

3\. Expect a 'pong' as a response. If the response message is not received within N seconds, please raise an error or reconnect. 

### Connection count limit

The limit will be set at 30 WebSocket connections per specific WebSocket channel per sub-account. Each WebSocket connection is identified by the unique `connId`.

  

The WebSocket channels subject to this limitation are as follows:

  1. [Orders channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel)
  2. [Account channel](/docs-v5/en/#trading-account-websocket-account-channel)
  3. [Positions channel](/docs-v5/en/#trading-account-websocket-positions-channel)
  4. [Balance and positions channel](/docs-v5/en/#trading-account-websocket-balance-and-position-channel)
  5. [Position risk warning channel](/docs-v5/en/#trading-account-websocket-position-risk-warning)
  6. [Account greeks channel](/docs-v5/en/#trading-account-websocket-account-greeks-channel)

If users subscribe to the same channel through the same WebSocket connection through multiple arguments, for example, by using `{"channel": "orders", "instType": "ANY"}` and `{"channel": "orders", "instType": "SWAP"}`, it will be counted once only. If users subscribe to the listed channels (such as orders and accounts) using either the same or different connections, it will not affect the counting, as these are considered as two different channels. The system calculates the number of WebSocket connections per channel.

  

The platform will send the number of active connections to clients through the `channel-conn-count` event message **to new channel subscriptions**.

> Connection count update
    
    
    {
        "event":"channel-conn-count",
        "channel":"orders",
        "connCount": "2",
        "connId":"abcd1234"
    }
    
    

  

When the limit is breached, generally the latest connection that sends the subscription request will be rejected. Client will receive the usual subscription acknowledgement followed by the `channel-conn-count-error` from the connection that the subscription has been terminated. In exceptional circumstances the platform may unsubscribe existing connections.

> Connection limit error
    
    
    {
        "event": "channel-conn-count-error",
        "channel": "orders",
        "connCount": "30",
        "connId":"a4d3ae55"
    }
    
    

  

Order operations through WebSocket, including place, amend and cancel orders, are not impacted through this change.

### Login

> Request Example
    
    
    {
      "op": "login",
      "args": [
        {
          "apiKey": "******",
          "passphrase": "******",
          "timestamp": "1538054050",
          "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs="
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
op | String | Yes | Operation  
`login`  
args | Array of objects | Yes | List of account to login  
> apiKey | String | Yes | API Key  
> passphrase | String | Yes | API Key password  
> timestamp | String | Yes | Unix Epoch time, the unit is seconds  
> sign | String | Yes | Signature string  
  
> Successful Response Example
    
    
    {
      "event": "login",
      "code": "0",
      "msg": "",
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "event": "error",
      "code": "60009",
      "msg": "Login failed.",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
event | String | Yes | Operation  
`login`  
`error`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
**apiKey** : Unique identification for invoking API. Requires user to apply one manually.

**passphrase** : API Key password

**timestamp** : the Unix Epoch time, the unit is seconds, e.g. 1704876947

**sign** : signature string, the signature algorithm is as follows:

First concatenate `timestamp`, `method`, `requestPath`, strings, then use HMAC SHA256 method to encrypt the concatenated string with SecretKey, and then perform Base64 encoding.

**secretKey** : The security key generated when the user applies for API key, e.g. `22582BD0CFF14C41EDBF1AB98506286D`

**Example of timestamp** : const timestamp = '' + Date.now() / 1,000

**Among sign example** : sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+'/users/self/verify', secretKey))

**method** : always 'GET'.

**requestPath** : always '/users/self/verify'

The request will expire 30 seconds after the timestamp. If your server time differs from the API server time, we recommended using the REST API to query the API server time and then set the timestamp. 

### Subscribe

**Subscription Instructions**

> Request format description
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": ["<SubscriptionTopic>"]
    }
    

WebSocket channels are divided into two categories: `public` and `private` channels.

`Public channels` \-- No authentication is required, include tickers channel, K-Line channel, limit price channel, order book channel, and mark price channel etc.

`Private channels` \-- including account channel, order channel, and position channel, etc -- require log in.

Users can choose to subscribe to one or more channels, and the total length of multiple channels cannot exceed 64 KB.

Below is an example of subscription parameters. The requirement of subscription parameters for each channel is different. For details please refer to the specification of each channels.

> Request Example
    
    
    {
        "id": "1512",
        "op":"subscribe",
        "args":[
            {
                "channel":"tickers",
                "instId":"BTC-USDT"
            }
        ]
    }
    

**Request parameters**

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "accb8e21"
    }
    

**Return parameters**

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
### Unsubscribe

Unsubscribe from one or more channels.

> Request format description
    
    
    {
      "op": "unsubscribe",
      "args": ["< SubscriptionTopic> "]
    }
    

> Request Example
    
    
    {
      "op": "unsubscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    

**Request parameters**

Parameter | Type | Required | Description  
---|---|---|---  
op | String | Yes | Operation  
`unsubscribe`  
args | Array of objects | Yes | List of channels to unsubscribe from  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "event": "unsubscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "d0b44253"
    }
    

**Response parameters**

Parameter | Type | Required | Description  
---|---|---|---  
event | String | Yes | Event  
`unsubscribe`  
`error`  
arg | Object | No | Unsubscribed channel  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
  
### Notification

WebSocket has introduced a new message type (event = `notice`).   
  

Client will receive the information in the following scenarios:

  * Websocket disconnect for service upgrade  

60 seconds prior to the upgrade of the WebSocket service, the notification message will be sent to users indicating that the connection will soon be disconnected. Users are encouraged to establish a new connection to prevent any disruptions caused by disconnection.

> Response Example
    
    
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  
  
The feature is supported by WebSocket Public (/ws/v5/public) and Private (/ws/v5/private) for now.

---

# WebSocket

### 概述 

WebSocket是HTML5一种新的协议（Protocol）。它实现了用户端与服务器全双工通信， 使得数据可以快速地双向传播。通过一次简单的握手就可以建立用户端和服务器连接， 服务器根据业务规则可以主动推送信息给用户端。其优点如下：

  * 用户端和服务器进行数据传输时，请求头信息比较小，大概2个字节。
  * 用户端和服务器皆可以主动地发送数据给对方。
  * 不需要多次创建TCP请求和销毁，节约宽带和服务器的资源。

强烈建议开发者使用WebSocket API获取市场行情和买卖深度等信息。 

### 连接 

**连接限制** ：3 次/秒 (基于IP)

当订阅公有频道时，使用公有服务的地址；当订阅私有频道时，使用私有服务的地址

**请求限制** ：

每个连接 对于 `订阅`/`取消订阅`/`登录` 请求的总次数限制为 480 次/小时

如果出现网络问题，系统会自动断开连接

如果连接成功后30s未订阅或订阅后30s内服务器未向用户推送数据，系统会自动断开连接

为了保持连接有效且稳定，建议您进行以下操作：

1\. 每次接收到消息后，用户设置一个定时器，定时N秒，N 小于30。

2\. 如果定时器被触发（N 秒内没有收到新消息），发送字符串 'ping'。

3\. 期待一个文字字符串'pong'作为回应。如果在 N秒内未收到，请发出错误或重新连接。

### 连接限制 

子账户维度，订阅每个 WebSocket 频道的最大连接数为 30 个。每个 WebSocket 连接都由唯一的 connId 标识。

  

受此限制的 WebSocket 频道如下：

  1. [订单频道](/docs-v5/zh/#order-book-trading-trade-ws-order-channel)
  2. [账户频道](/docs-v5/zh/#trading-account-websocket-account-channel)
  3. [持仓频道](/docs-v5/zh/#trading-account-websocket-positions-channel)
  4. [账户余额和持仓频道](/docs-v5/zh/#trading-account-websocket-balance-and-position-channel)
  5. [爆仓风险预警推送频道](/docs-v5/zh/#trading-account-websocket-position-risk-warning)
  6. [账户greeks频道](/docs-v5/zh/#trading-account-websocket-account-greeks-channel)

若用户通过不同的请求参数在同一个 WebSocket 连接下订阅同一个频道，如使用 `{"channel": "orders", "instType": "ANY"}` 和 `{"channel": "orders", "instType": "SWAP"}`，只算为一次连接。若用户使用相同或不同的 WebSocket 连接订阅上述频道，如订单频道和账户频道。在该两个频道之间，计数不会累计，因为它们被视作不同的频道。简言之，系统计算每个频道对应的 WebSocket 连接数量。

  

新链接订阅频道时，平台将对该订阅返回`channel-conn-count`的消息同步链接数量。

> 链接数量更新
    
    
    {
        "event":"channel-conn-count",
        "channel":"orders",
        "connCount": "2",
        "connId":"abcd1234"
    }
    
    

  

当超出限制时，一般最新订阅的链接会收到拒绝。用户会先收到平时的订阅成功信息然后收到`channel-conn-count-error`消息，代表平台终止了这个链接的订阅。在异常场景下平台会终止已订阅的现有链接。

> 链接数量限制报错
    
    
    {
        "event": "channel-conn-count-error",
        "channel": "orders",
        "connCount": "30",
        "connId":"a4d3ae55"
    }
    
    

  

通过 WebSocket 进行的订单操作，例如下单、修改和取消订单，不会受到此改动影响。

### 登录 

> 请求示例
    
    
    {
     "op": "login",
     "args":
      [
         {
           "apiKey": "******",
           "passphrase": "******",
           "timestamp": "1538054050",
           "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs=" 
          }
       ]
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`login`  
args | Array of objectss | 是 | 账户列表  
> apiKey | String | 是 | APIKey  
> passphrase | String | 是 | APIKey 的密码  
> timestamp | String | 是 | 时间戳，Unix Epoch时间，单位是秒  
> sign | String | 是 | 签名字符串  
  
> 全部成功返回示例
    
    
    {
      "event": "login",
      "code": "0",
      "msg": "",
      "connId": "a4d3ae55"
    }
    

> 全部失败返回示例
    
    
    {
      "event": "error",
      "code": "60009",
      "msg": "Login failed.",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 操作，`login` `error`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
**apiKey** :调用API的唯一标识。需要用户手动设置一个 **passphrase** :APIKey的密码 **timestamp** :Unix Epoch 时间戳，单位为秒，如 1704876947 **sign** :签名字符串，签名算法如下：

先将`timestamp` 、 `method` 、`requestPath` 进行字符串拼接，再使用HMAC SHA256方法将拼接后的字符串和SecretKey加密，然后进行Base64编码

**SecretKey:** 用户申请APIKey时所生成的安全密钥，如：22582BD0CFF14C41EDBF1AB98506286D

**其中 timestamp 示例** :const timestamp = '' + Date.now() / 1,000

**其中 sign 示例** : sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))

**method** 总是 'GET'

**requestPath** 总是 '/users/self/verify'

请求在时间戳之后30秒会失效，如果您的服务器时间和API服务器时间有偏差，推荐使用 REST API查询API服务器的时间，然后设置时间戳 

### 订阅 

**订阅说明**

> 请求格式说明
    
    
    {
        "op": "subscribe",
        "args": ["<SubscriptionTopic>"]
    }
    

WebSocket 频道分成两类： `公共频道` 和 `私有频道`

`公共频道`无需登录，包括行情频道，K线频道，交易数据频道，资金费率频道，限价范围频道，深度数据频道，标记价格频道等。

`私有频道`需登录，包括用户账户频道，用户交易频道，用户持仓频道等。

用户可以选择订阅一个或者多个频道，多个频道总长度不能超过 64 KB。

以下是一个请求参数的例子。每一个频道的请求参数的要求都不一样。请根据每一个频道的需求来订阅频道。

> 请求示例
    
    
    {
        "op":"subscribe",
        "args":[
            {
                "channel":"tickers",
                "instId":"BTC-USDT"
            }
        ]
    }
    
    

**请求参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`subscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币   
`MARGIN`：币币杠杆  
`SWAP`：永续  
`FUTURES`：交割  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 返回示例 
    
    
    {
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "accb8e21"
    }
    

**返回参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 事件，`subscribe` `error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续  
`FUTURES`：交割  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
### 取消订阅 

可以取消一个或者多个频道

> 请求格式说明
    
    
    {
        "op": "unsubscribe",
        "args": ["< SubscriptionTopic > "]
    }
    

> 请求示例
    
    
    {
      "op": "unsubscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    

**请求参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`unsubscribe`  
args | Array of objects | 是 | 取消订阅的频道列表  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 返回示例
    
    
    {
        "event": "unsubscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "d0b44253"
    }
    

**返回参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 事件，`unsubscribe` `error`  
arg | Object | 否 | 取消订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
### 通知 

WebSocket有一种消息类型(event=`notice`)。   
  

用户会在如下场景收到此类信息：

  * Websocket服务升级断线

在推送服务升级前60秒会推送信息，告知用户WebSocket服务即将升级。用户可以重新建立新的连接避免由于断线造成的影响。

> 返回示例
    
    
    {
        "event": "notice",
        "code": "64008",
        "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
        "connId": "a4d3ae55"
    }
    

  
  
目前支持WebSocket公共频道(/ws/v5/public)和私有频道(/ws/v5/private)。