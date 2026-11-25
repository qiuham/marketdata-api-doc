---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/intro
api_type: WebSocket
updated_at: 2026-11-25 19:01:29.362964
---

# Websocket API

### Overview

WebSocket is a new HTML5 protocol that achieves full-duplex data transmission between the client and server, allowing data to be transferred effectively in both directions. A connection between the client and server can be established with just one handshake. The server will then be able to push data to the client according to preset rules. Its advantages include:

- The WebSocket request header size for data transmission between client and server is only 2 bytes.
- Either the client or server can initiate data transmission.
- There's no need to repeatedly create and delete TCP connections, saving resources on bandwidth and server.

It is strongly recommended that developers use WebSocket API to obtain market information and transaction depth.

| Domain	| WebSocket API | Recommended to use |
|:---|:---|:---|
| Websocket Domain | wss://ws.bitget.com/v2/ws/public  | Main Domain, Public channel        |
| Websocket Domain | wss://ws.bitget.com/v2/ws/private | Main Domain, Private channel       |

### Connect

**Connection instructions**:

**Connection limit**: 300 connection requests/IP/5min, Max 100 connections/IP

**Subscription limit**: 240 subscription requests/Hour/connection, Max 1000 channel subscription/connection

To keep the connection stable and effective, it is recommended to:

1. Users set a 30 seconds timer to a send string "ping", and expect a string "pong" as response. If no string "pong" received, please reconnect
2. Websocket server will disconnect the connection if there is no string "ping" received for 2 min
3. Messages sent by the client (`ping`, `login`, `subscribe`, `unsubscribe`) are rate limited. See **Message rate limits** below. The IP which is repeatedly disconnected may be blocked by the server
4. We highly recommend you to subscribe **less than 50 channels in one connection**. The connections with less channel subscriptions will be more stable.

**Message rate limits**

Limits are calculated per WebSocket connection, and separately for each message type:

| Message type | Interval | Max messages per interval | When exceeded |
|:---|:---|:---|:---|
| `ping` | 5 seconds | 10 | Connection closed |
| `login` | 5 seconds | 2 | Excess messages discarded |
| `subscribe` | 5 seconds | 50 | Excess messages discarded |
| `unsubscribe` | 5 seconds | 50 | Excess messages discarded |

When the `ping` limit is exceeded, the server returns error code `30007` (`request over limit,connection close`) and closes the connection. The client needs to reconnect.

### Login

**apiKey**: Unique identification for invoking API. Requires user to [apply](https://www.bitget.com/account/newapi) one manually.

**passphrase**: APIKey password

**timestamp**: Unix timestamp in milliseconds, which will expire in 30 seconds.

**secretKey**: The security key generated when the user applies for APIKey, e.g. : 22582BD0CFF14C41EDBF1AB98506286D

```javascript title="Example of timestamp"
const timestamp ='' + Date.now()
```

```javascript title="Sign example
sign=CryptoJS.enc.Base64.Stringify(CryptoJS.HmacSHA256(timestamp +'GET'+'/user/verify', secretKey))
```

**method**: always 'GET'.

**requestPath** : always '/user/verify'

**sign**: signature string, the signature algorithm is as follows:

First concatenate `timestamp`, `method`, `requestPath`, then use HMAC SHA256 method to encrypt the concatenated string with SecretKey, and then perform Base64 encoding.

The request will expire 30 seconds after the timestamp. If your server time differs from the API server time, we recommended using the REST API to query the <a href="https://www.bitget.com/zh-CN/docs/classic/common/public/Get-Server-Time">API server time</a> and then compare the timestamp.

#### Steps to generate the final signature

***HMAC***

Step 1. concat the content

```java
Long timestamp = System.currentTimeMillis() / 1000;
        String content = timestamp +"GET"+"/user/verify";
```

Step 1. Use the private key secretkey to encrypt the string to be signed with hmac sha256

```java
String hash = hmac_sha256(content, secretkey);
```

The final step is to base64 encode the hash

```java
String sign = base64.encode(hash);
```

***RSA***

- RSA sample code

Step 1. Use the RSA privateKey **privateKey** to encrypt the string to be signed with SHA-256

Step 2. Base64 encoding for Signature.

If login fails, it will automatically disconnect

```json title="Request Format Description"
{
  "op":"login",
  "args":[
    {
      "apiKey":"<api_key>",
      "passphrase":"<passphrase>",
      "timestamp":"<timestamp>",
      "sign":"<sign>"
    }
  ]
}
```

```json title="Request Example"
{
  "op":"login",
  "args":[
    {
      "apiKey":"xx_xxx",
      "passphrase":"xxx",
      "timestamp":"1538054050",
      "sign":"8RCOqCJAhhEh4PWcZB/96QojLDqMAg4qNynIixFzS3E="
    }
  ]
}
```

```json title="Successful Response Example"
{
  "event":"login",
  "code":"0",
  "msg":""
}
```

```json title="Failure Response Example"
{
  "event":"error",
  "code":"30005",
  "msg":"error"
}
```

### Subscribe

**Subscription Instructions**

```json title="Request Format Description"
{
    "op": "subscribe",
    "args": ["<SubscriptionTopic>"]
}
```

WebSocket channel: Public channel

No login required. Public channels include market ticker, candlestick, trade data, depth data, etc.

`instId`: should be either `symbol` or `default`

Users can choose to subscribe to one or more channels, and the total length of multiple channels cannot exceed 4096 bytes at a time.

```json title="Request Example"
{
    "op":"subscribe",
    "args":[
        {
            "instType":"SPOT",
            "channel":"ticker",
            "instId":"BTCUSDT"
        },
        {
            "instType":"SPOT",
            "channel":"candle5m",
            "instId":"BTCUSDT"
        }
    ]
}
```

**Request Parameters**

|Parameter	|Type	|Required	|Description|
|:---|:---|:---|:---|
|op	|String	|Yes	|Operation, `subscribe`|
|args	|Array	|Yes	|List of subscribe channels|
| > instType	|String	|No	|Instrument Type |
| > channel	|String	|Yes|	Channel name|
| > instId	|String	|No	|Instrument ID|

```json title="Example Response"
{
 "event": "subscribe",
  "arg": {
   "instType":"SPOT",
   "channel":"ticker", 
   "instId":"BTCUSDT" 
 }
}
```

**Return Parameters**

|Parameter	|Type	|Required	|Description|
|:---|:---|:---|:---|
|event	|String	|Yes	|Event, subscribe error|
|arg	|Object	|No	|Subscribed channel|
|> instType	|String	|No	|Instrument Type MC：Perpetual contract public channel|
|> channel	|String	|Yes|	Channel name|
|> instId	|String	|No	|Instrument ID|
|code	|String	|No	|Error code|
|msg	|String	|No	|Error message|

### Unsubscribe

Unsubscribe from one or more channels.

```json title="Request Format Description"
{
    "op": "unsubscribe",
    "args": ["< SubscriptionTopic>"]
}
```

```json title="Request Example"
{
    "op":"unsubscribe",
    "args":[
        {
            "instType":"SPOT",
            "channel":"ticker",
            "instId":"BTCUSDT"
        },
        {
            "instType":"SPOT",
            "channel":"candle1m",
            "instId":"BTCUSDT"
        }
    ]
}
```

**Request Parameters**

|Parameter	|Type	|Required	|Description|
|:---|:---|:---|:---|
| op	|String	|Yes	|Operation, unsubscribe|
| args	|Array	|Yes	|List of channels to unsubscribe from|
| > instType	|String	|Yes	|Instrument Type MC：Perpetual contract public channel|
| > channel	|String	|Yes	|Channel name|
| > instId	|String	|Yes	|Instrument ID|

```json title="Example Response"
{
  "op":"unsubscribe",
  "args":[
    {
      "instType":"USDT-FUTURES",
      "channel":"ticker",
      "instId":"BTCUSDT"
    },
    {
      "instType":"USDT-FUTURES",
      "channel":"candle1m",
      "instId":"BTCUSDT"
    }
  ]
}
```

**Return Parameters**

|Parameter	|Type	|Required	|Description|
|:---|:---|:---|:---|
| event	|String	|Yes	|Event, unsubscribe error|
| arg	|Object	|Yes	|Unsubscribed channel|
| > instType	|String	|Yes|	Instrument Type|
| > channel	|String	|Yes	|Channel name|
| > instId	|String	|Yes	|Instrument ID|
| code	|String	|No	|Error Code|
| msg	|String |No	|Error Message|

---

# Websocket

<h3 id="overview">概述</h3>
WebSocket是HTML5一种新的协议(Protocol)。它实现了客户端与服务器全双工通信， 使得数据可以快速地双向传播。通过一次简单的握手就 可以建立客户端和服务器连接， 服务器根据业务规则可以主动推送信息给客户端。其优点如下：

- 客户端和服务器进行数据传输时，请求头信息比较小，大概2个字节。
- 客户端和服务器皆可以主动地发送数据给对方。
- 不需要多次创建TCP请求和销毁，节约宽带和服务器的资源。

- 强烈建议开发者使用WebSocket API获取市场行情和买卖深度等信息。

| 域名	| WebSocket API | 建议使用 |
|:---|:---|:---|
| 公共频道 | wss://ws.bitget.com/v2/ws/public  | 主域名， 公共频道       |
| 私有频道 | wss://ws.bitget.com/v2/ws/private | 主域名， 私有频道       |

<h3 id="connect">连接</h3>
**连接说明**：

**连接限制**：300次连接请求/IP/5分钟，单个IP最多可以创建100个连接

**订阅限制**：240次/小时/连接，单个连接最多可以订阅1000个频道

为了保持连接有效且稳定，建议您进行以下操作：

1. 用户设置一个定时器，每30秒发送字符串"ping", 并期待一个字符串"pong"作为回应。如果未收到字符串"pong"响应，请重新连接
2. 如果2分钟内服务端没收到"ping"，会自动断开连接
3. 客户端发送的消息（`ping`、`login`、`subscribe`、`unsubscribe`）受频率限制，详见下方**消息限频规则**。反复被断开连接的IP有可能被服务器屏蔽
4. 为了保持连接的稳定性，强烈建议**单个连接不要订阅超过50个频道**。订阅频道数越少的连接，稳定性会更高。

**消息限频规则**

以下限制按每个 WebSocket 连接、各消息类型分别计算：

| 消息类型 | 统计间隔 | 间隔内允许的最大次数 | 超限处理 |
|:---|:---|:---|:---|
| `ping` | 5 秒 | 10 次 | 断开连接 |
| `login` | 5 秒 | 2 次 | 丢弃超限消息 |
| `subscribe` | 5 秒 | 50 次 | 丢弃超限消息 |
| `unsubscribe` | 5 秒 | 50 次 | 丢弃超限消息 |

`ping` 超过限制时，服务器将返回错误码 `30007`（`request over limit,connection close`，请求超过限制，连接关闭）并断开连接，客户端需要重新连接。

<h3 id="login">登录</h3>
**api_key**:用于调用API的用户身份唯一标示，需要用户[申请](https://www.bitget.com/zh-CN/account/newapi)

**passphrase**:API Key 的密码,如果没有口令的话传入空字符串("")即可

**timestamp**: Unix 毫秒时间戳 ，时间戳30秒后会过期

**sign**:为签名字符串，签名规则参照如下:

Message即(待签名字符串)为： timestamp+method+requestPath

其中timestamp示例:

`const timestamp = '' + Date.now()`

method一律默认为'GET'

requestPath 一律默认为 `/user/verify`

请求在时间戳之后30秒会失效，如果您的服务器时间和API服务器时间有偏差，推荐使用 REST API查询 <a href="https://www.bitget.com/zh-CN/docs/classic/common/public/Get-Server-Time">服务器时间</a>，然后设置时间戳

签名方式说明参考API概述里的验证部分

<h4 id="steps-to-generate-the-final-signature">生成最终签名的步骤</h4>
##### HMAC

第1步，将待签名字符串使用私钥secretkey进行hmac sha256加密

```java
Signature = hmac_sha256(secretkey, Message)
```

第2步，对于Signature进行base64编码

```java
Signature = base64.encode(Signature)
```

##### RSA

- RSA示例代码

第一步，使用RSA私钥privateKey对待签名字符串进行SHA-256签名。

第二步，对生成的签名字符串进行编码为 base64 string，得到签名字符串进行接口请求。

如果登录失败会自动断开链接

```json title="请求格式说明"
{
  "op":"login",
  "args":[
    {
      "apiKey":"<api_key>",
      "passphrase":"<passphrase>",
      "timestamp":"<timestamp>",
      "sign":"<sign>"
    }
  ]
}	
```

```json title="请求示例"
{
  "op":"login",
  "args":[
    {
      "apiKey":"xx_xxx",
      "passphrase":"12345678",
      "timestamp":"1538054050",
      "sign":"8RCOqCJAhhEh4PWcZB/96QojLDqMAg4qNynIixFzS3E="
    }
  ]
}
```

```json title="成功返回示例"
{
  "event":"login",
  "code":"0",
  "msg":""
}
```

```json title="失败返回示例"
{
  "event":"error",
  "code":"30005",
  "msg":"login fail"
}
```

<h3 id="subscribe">订阅</h3>
**订阅说明**

```json title="请求格式说明"
{
  "op":"subscribe",
  "args":[
    "<SubscriptionTopic> "
  ]
}
```

WebSocket 频道： 公共频道

公共频道无需登录，包括行情频道，K线频道，交易数据频道，深度数据频道等。

`instId` 取值参考 `symbol` 或 `default`

用户可以选择订阅一个或者多个频道，一次订阅多个频道总长度不能超过4096个字节。

```json title="请求示例"
{
  "op":"subscribe",
  "args":[
    {
      "instType":"USDT-FUTURES",
      "channel":"ticker",
      "instId":"BTCUSDT"
    },
    {
      "instType":"USDT-FUTURES",
      "channel":"candle1m",
      "instId":"BTCUSDT"
    }
  ]
}
```

**请求参数**

|参数	|类型	|是否必须	|描述|
|:---|:---|:---|:---|
|op	|String	|是	|操作，`subscribe`|
|args	|Array	|是	|请求订阅的频道列表|
|> instType	|String	|否	|产品类型 MC：公共频道|
|> channel	|String	|是	|频道名|
|> instId	|String	|否	|产品ID或产品名称|

```json title = "返回示例"
{
  "event":"subscribe",
  "arg":{
    "instType":"USDT-FUTURES",
    "channel":"ticker",
    "instId":"BTCUSDT"
  }
}
```

**返回参数**

|参数	|类型	|是否必须	|描述|
|:---|:---|:---|:---|
|event	|String	|是	|事件，`subscribe`|
|arg	|Object	|否	|订阅的频道|
|> instType	|String	|否	|产品类型|
|> channel	|String	|是	|频道名|
|> instId	|String	|否	|产品ID|
|code	|String	|否	|错误码|
|msg	|String	|否	|错误消息|

<h3 id="unsubscribe">取消订阅</h3>
可以取消一个或者多个频道

```json title="请求格式说明"
{
  "op":"unsubscribe",
  "args":[
    "< SubscriptionTopic > "
  ]
}
```

```json title="请求示例"
{
  "op":"unsubscribe",
  "args":[
    {
      "instType":"USDT-FUTURES",
      "channel":"ticker",
      "instId":"BTCUSDT"
    },
    {
      "instType":"USDT-FUTURES",
      "channel":"candle1D",
      "instId":"BTCUSDT"
    }
  ]
}
```

**请求参数**

|参数	|类型	|是否必须	|描述|
|:---|:---|:---|:---|
|op	|String	|是	|操作，`unsubscribe`|
|args	|Array	|是	|取消订阅的频道列表|
|> instType	|String	|是	|产品类型 MC：公共频道|
|> channel	|String	|是	|频道名|
|> instId	|String	|是	|产品ID|

```json title="返回示例"
{
  "event":"unsubscribe",
  "arg":{
    "instType":"USDT-FUTURES",
    "channel":"ticker",
    "instId":"BTCUSDT"
  }
}
```