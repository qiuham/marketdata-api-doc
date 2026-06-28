---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order
api_type: WebSocket
updated_at: 2026-01-15T23:47:34.877563
---

# Cancel Algo Order (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#api-description "Direct link to API Description")

Cancel an active algo order.

## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#method "Direct link to Method")

`algoOrder.cancel`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#request "Direct link to Request")
    
    
    {  
       	"id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "method": "algoOrder.cancel",   
        "params": {   
          "apiKey": "HsOehcfih8ZRxnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGOGQj1lGdTjR",   
          "algoId": 283194212,   
          "clientAlgoId": "DolwRKnQNjoc1E9Bbh03ER",  
          "timestamp": 1703439070722,   
          "signature": "b09c49815b4e3f1f6098cd9fbe26a933a9af79803deaaaae03c29f719c08a8a8"   
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
algoId| LONG| NO|   
clientAlgoId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `algoId` or `clientAlgoId` must be sent.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#response-example "Direct link to Response Example")
    
    
    {  
      "id": "unique-cancel-request-id-5678",  
      "status": 200,  
      "result": {  
        "algoId": 2000000002162519,  
        "clientAlgoId": "rDMG8WSde6LkyMNtk6s825",  
        "code": "200",  
        "msg": "success"  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 6  
        }  
      ]  
    }

---

# 条件单撤销订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#接口描述 "接口描述的直接链接")

撤销条件订单

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#方式 "方式的直接链接")

`algoOrder.cancel`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求 "请求的直接链接")
    
    
    {  
       	"id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "method": "algoOrder.cancel",   
        "params": {   
          "apiKey": "HsOehcfih8ZRxnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGOGQj1lGdTjR",   
          "algoId": 283194212,   
          "clientAlgoId": "DolwRKnQNjoc1E9Bbh03ER",  
          "timestamp": 1703439070722,   
          "signature": "b09c49815b4e3f1f6098cd9fbe26a933a9af79803deaaaae03c29f719c08a8a8"   
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
algoId| LONG| NO| 系统订单号  
clientAlgoId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `algoId` 与 `clientAlgoId` 必须至少发送一个
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "unique-cancel-request-id-5678",  
      "status": 200,  
      "result": {  
        "algoId": 2000000002162519,  
        "clientAlgoId": "rDMG8WSde6LkyMNtk6s825",  
        "code": "200",  
        "msg": "success"  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 6  
        }  
      ]  
    }