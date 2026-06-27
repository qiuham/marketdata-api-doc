---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp
api_type: WebSocket
updated_at: 2026-01-15T23:40:17.247262
---

# Keepalive User Data Stream (USER_STREAM)

## API Description[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#api-description "Direct link to API Description")

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

## Method[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#method "Direct link to Method")

`userDataStream.ping`

## Request[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#request "Direct link to Request")
    
    
    {  
      "id": "815d5fce-0880-4287-a567-80badf004c74",  
      "method": "userDataStream.ping",  
      "params": {  
        "apiKey": "vmPUZE6mv9SD5VNHk9HlWFsOr9aLE2zvsw0MuIgwCIPy8atIco14y7Ju91duEh8A"  
       }  
    }  
    

## Request Weight[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory|  Description  
---|---|---|---  
`apiKey`| STRING| NO| Required if session is not authenticated via `session.logon`  
  
## Response Example[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#response-example "Direct link to Response Example")
    
    
    {  
      "id": "815d5fce-0880-4287-a567-80badf004c74",  
      "status": 200,  
      "result": {  
        "listenKey": "3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg"  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 2  
        }  
      ]  
    }

---

# Websocket API延长listenKey有效期(USER_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#接口描述 "接口描述的直接链接")

有效期延长至本次调用后60分钟

## 方式[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#方式 "方式的直接链接")

`userDataStream.ping`

## 请求[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#请求 "请求的直接链接")
    
    
    {  
      "id": "815d5fce-0880-4287-a567-80badf004c74",  
      "method": "userDataStream.ping",  
      "params": {  
        "apiKey": "vmPUZE6mv9SD5VNHk9HlWFsOr9aLE2zvsw0MuIgwCIPy8atIco14y7Ju91duEh8A"  
       }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需|  描述  
---|---|---|---  
`apiKey`| STRING| NO| 如果未通过 session.logon 对会话进行身份验证，则为必需  
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "815d5fce-0880-4287-a567-80badf004c74",  
      "status": 200,  
      "result": {  
        "listenKey": "3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg"  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 2  
        }  
      ]  
    }