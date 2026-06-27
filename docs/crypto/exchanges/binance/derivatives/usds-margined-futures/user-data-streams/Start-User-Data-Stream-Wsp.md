---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp
api_type: WebSocket
updated_at: 2026-01-15T23:47:49.489519
---

# Start User Data Stream (USER_STREAM)

## API Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#api-description "Direct link to API Description")

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

## Method[​](/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#method "Direct link to Method")

`userDataStream.start`

## Request[​](/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#request "Direct link to Request")
    
    
    {  
      "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
      "method": "userDataStream.start",  
      "params": {  
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"  
      }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
apiKey| STRING| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#response-example "Direct link to Response Example")
    
    
    {  
      "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
      "status": 200,  
      "result": {  
        "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"  
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

# Websocket API生成listenKey (USER_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#接口描述 "接口描述的直接链接")

创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#方式 "方式的直接链接")

`userDataStream.start`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求 "请求的直接链接")
    
    
    {  
      "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
      "method": "userDataStream.start",  
      "params": {  
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"  
      }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
apiKey| STRING| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
      "status": 200,  
      "result": {  
        "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"  
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