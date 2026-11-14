---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/margin-trading/listen-token-data-stream
api_type: REST
updated_at: 2026-11-13 20:28:35.147623
---

# Listen Token User Data Stream

> This is the recommended successor to the deprecated listen-key-based User Data Stream on `wss://stream.binance.com:9443`. It uses a short-lived **listen token** and a WebSocket API subscription method, and offers lower latency. See the [Change Log](/en/docs/products/margin-trading/change-log) for the deprecation announcement.

## Connect

  * The base REST endpoint is: **<https://api.binance.com>**
  * `POST /sapi/v1/userListenToken` creates a new user data stream and returns a `listenToken`.
    * Request weight (UID): **1**
    * `expirationTime = current time + validity`. Default and maximum validity are both **24 hours**.
    * `isIsolated` (BOOLEAN): `true` means isolated margin (then `symbol` is required); default is cross margin.
    * To extend a subscription, call `POST /sapi/v1/userListenToken` again **before** the current subscription expires, obtain a new `listenToken`, then call `userDataStream.subscribe.listenToken` again with the new token. The subscription extends seamlessly to the new `expirationTime`.
  * The base WebSocket API endpoint is: **`wss://ws-api.binance.com:443/ws-api/v3`**
    * testnet: `wss://ws-api.testnet.binance.vision/ws-api/v3`
  * Subscribe via the WebSocket API method **`userDataStream.subscribe.listenToken`** with the param `listenToken` (string, required).
    * Request weight: **2**
    * Non-authenticated sessions are allowed to use this feature.
    * An invalid `listenToken` returns error **-1209**.
  * If a subscription is not extended before its token expires, it expires and an [`eventStreamTerminated`](/en/docs/products/margin-trading/listen-token-data-stream#event-event-stream-terminated) event is sent. No further events will be pushed after that until a new token is created and a new subscription is opened.



* * *

## HTTP Request — POST /sapi/v1/userListenToken

### Request

Name| Type| Required| Description  
---|---|---|---  
`symbol`| STRING| CONDITIONAL| Trading pair symbol; required when `isIsolated` is `true`, e.g. `BNBUSDT`.  
`isIsolated`| BOOLEAN| NO| Whether it is isolated margin; `true` means isolated; default is cross margin.  
`validity`| LONG| NO| Validity in milliseconds; default 24 hours, maximum 24 hours.  
  
### Response Example
    
    
    Code
    
    {
      "token": "6xXxePXwZRjVSHKhzUCCGnmN3fkvMTXru+pYJS8RwijXk9Vcyr3rkwfVOTcP2OkONqciYA",
      "expirationTime": 1758792204196
    }

* * *

## WebSocket API Method — userDataStream.subscribe.listenToken

Subscribe to the user data stream using the `listenToken` obtained from `POST /sapi/v1/userListenToken`.

### Request Example
    
    
    Code
    
    {
      "id": "f3a8f7a29f2e54df796db582f3d",
      "method": "userDataStream.subscribe.listenToken",
      "params": {
        "listenToken": "5DbylArkmImhyHkpG6s9tbiFy5uAMTFwzx9vwsFjDv9dC3GkKxSuoTCj0HvcJC0WYi8fA"
      }
    }

### Response Example
    
    
    Code
    
    {
      "id": "f3a8f7a29f2e54df796db582f3d",
      "status": 200,
      "result": {
        "subscriptionId": 0,
        "expirationTime": 1749094553955907
      }
    }

* * *

## Event: Event Stream Terminated

### Description

This event is sent when the subscription expires because it was not extended before the `listenToken`'s `expirationTime`. No more events will be sent after this until a new `listenToken` is created and a new subscription is opened.

### Event Name

`eventStreamTerminated`

### Payload
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "eventStreamTerminated",
        "E": 1759089357377
      }
    }

Was this page helpful?

Last modified on November 12, 2026

[(deprecated) Trade Data Stream](/en/docs/products/margin-trading/trade-data-stream)[Public API Definitions](/en/docs/products/margin-trading/common-definition)

---

# Listen Token 用户数据流

> 本篇为基于 `wss://stream.binance.com:9443` 的 listenKey 用户数据流的推荐替代方案，使用有效期较短的 **listen token** 与 WebSocket API 订阅方法，延迟更低。弃用公告请参见 [变更日志](/zh-CN/docs/products/margin-trading/change-log)。

## 连接

  * REST 接口的 base URL：**<https://api.binance.com>**
  * `POST /sapi/v1/userListenToken` 创建一个新的用户数据流并返回一个 `listenToken`。
    * 请求权重 (UID)：**1**
    * `expirationTime = 当前时间 + validity`。默认与最大有效期均为 **24 小时** 。
    * `isIsolated`（BOOLEAN）：`true` 表示逐仓（此时 `symbol` 必填），默认为全仓。
    * 如需延长订阅，请在当前订阅过期**之前** 再次调用 `POST /sapi/v1/userListenToken`，获取新的 `listenToken`，然后用新 token 再次调用 `userDataStream.subscribe.listenToken`，订阅将无缝延长至新的 `expirationTime`。
  * WebSocket API 的 base URL：**`wss://ws-api.binance.com:443/ws-api/v3`**
    * testnet：`wss://ws-api.testnet.binance.vision/ws-api/v3`
  * 通过 WebSocket API 方法 **`userDataStream.subscribe.listenToken`** 订阅，参数 `listenToken`（字符串，必填）。
    * 请求权重：**2**
    * 允许在非鉴权会话中使用此功能。
    * `listenToken` 无效时返回错误码 **-1209** 。
  * 若订阅未在 token 过期前延长，订阅将失效并推送 [`eventStreamTerminated`](/zh-CN/docs/products/margin-trading/listen-token-data-stream#%E4%BA%8B%E4%BB%B6%E4%BA%8B%E4%BB%B6%E6%B5%81%E7%BB%88%E6%AD%A2) 事件；此后不会再推送任何事件，直到创建新 token 并重新订阅。



* * *

## HTTP 请求 — POST /sapi/v1/userListenToken

### 请求参数

名称| 类型| 是否必填| 描述  
---|---|---|---  
`symbol`| STRING| 条件必填| 交易对符号；当 `isIsolated` 为 `true` 时必填，例如 `BNBUSDT`。  
`isIsolated`| BOOLEAN| 否| 是否逐仓；`true` 为逐仓，默认为全仓。  
`validity`| LONG| 否| 有效期，单位毫秒；默认 24 小时，最大 24 小时。  
  
### 响应示例
    
    
    Code
    
    {
      "token": "6xXxePXwZRjVSHKhzUCCGnmN3fkvMTXru+pYJS8RwijXk9Vcyr3rkwfVOTcP2OkONqciYA",
      "expirationTime": 1758792204196
    }

* * *

## WebSocket API 方法 — userDataStream.subscribe.listenToken

使用从 `POST /sapi/v1/userListenToken` 获取的 `listenToken` 订阅用户数据流。

### 请求示例
    
    
    Code
    
    {
      "id": "f3a8f7a29f2e54df796db582f3d",
      "method": "userDataStream.subscribe.listenToken",
      "params": {
        "listenToken": "5DbylArkmImhyHkpG6s9tbiFy5uAMTFwzx9vwsFjDv9dC3GkKxSuoTCj0HvcJC0WYi8fA"
      }
    }

### 响应示例
    
    
    Code
    
    {
      "id": "f3a8f7a29f2e54df796db582f3d",
      "status": 200,
      "result": {
        "subscriptionId": 0,
        "expirationTime": 1749094553955907
      }
    }

* * *

## 事件：事件流终止

### 描述

当订阅因未在 `listenToken` 的 `expirationTime` 之前续期而到期时，会推送此事件。此后不会再推送任何事件，直到创建新的 `listenToken` 并重新订阅。

### 事件名称

`eventStreamTerminated`

### 负载
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "eventStreamTerminated",
        "E": 1759089357377
      }
    }

此页面是否有帮助？

Last modified on November 12, 2026

[（已弃用）交易数据流](/zh-CN/docs/products/margin-trading/trade-data-stream)[公开 API 参数](/zh-CN/docs/products/margin-trading/common-definition)