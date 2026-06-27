---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams/Start-User-Data-Stream
api_type: REST
updated_at: 2026-01-15T23:43:38.560534
---

# Start User Data Stream (USER_STREAM)

## API Description[​](/docs/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#api-description "Direct link to API Description")

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

## HTTP Request[​](/docs/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#http-request "Direct link to HTTP Request")

POST `/eapi/v1/listenKey`

## Request Weight[​](/docs/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#response-example "Direct link to Response Example")
    
    
    {  
      "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1",  
      "expiration": 1762855900452  
    }

---

# 生成listenKey (USER_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#接口描述 "接口描述的直接链接")

创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#http请求 "HTTP请求的直接链接")

POST `/eapi/v1/listenKey`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#请求参数 "请求参数的直接链接")

None

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Start-User-Data-Stream#响应示例 "响应示例的直接链接")
    
    
    {  
      "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"  
    }