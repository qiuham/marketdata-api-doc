---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order
api_type: WebSocket
updated_at: 2026-01-15T23:47:34.941407
---

# Cancel Order (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#api-description "Direct link to API Description")

Cancel an active order.

## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#method "Direct link to Method")

`order.cancel`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#request "Direct link to Request")
    
    
    {  
       	"id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "method": "order.cancel",   
        "params": {   
          "apiKey": "HsOehcfih8ZRxnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGOGQj1lGdTjR",   
          "orderId": 283194212,   
          "symbol": "BTCUSDT",   
          "timestamp": 1703439070722,   
          "signature": "b09c49815b4e3f1f6098cd9fbe26a933a9af79803deaaaae03c29f719c08a8a8"   
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#response-example "Direct link to Response Example")
    
    
    {  
      "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
      "status": 200,  
      "result": {  
        "clientOrderId": "myOrder1",  
        "cumQty": "0",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 283194212,  
        "origQty": "11",  
        "origType": "TRAILING_STOP_MARKET",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "CANCELED",  
        "stopPrice": "9300",                  
        "closePosition": false,    
        "symbol": "BTCUSDT",  
        "timeInForce": "GTC",  
        "type": "TRAILING_STOP_MARKET",  
        "activatePrice": "9020",              
        "priceRate": "0.3",                  
        "updateTime": 1571110484038,  
        "workingType": "CONTRACT_PRICE",  
        "priceProtect": false,             
        "priceMatch": "NONE",                
        "selfTradePreventionMode": "NONE",  
        "goodTillDate": 0                   
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 1  
        }  
      ]  
    }

---

# 撤销订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#接口描述 "接口描述的直接链接")

撤销订单

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#方式 "方式的直接链接")

`order.cancel`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#请求 "请求的直接链接")
    
    
    {  
       	"id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "method": "order.cancel",   
        "params": {   
          "apiKey": "HsOehcfih8ZRxnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGOGQj1lGdTjR",   
          "orderId": 283194212,  
          "symbol": "BTCUSDT",   
          "timestamp": 1703439070722,   
          "signature": "b09c49815b4e3f1f6098cd9fbe26a933a9af79803deaaaae03c29f719c08a8a8"   
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 与 `origClientOrderId` 必须至少发送一个
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
      "status": 200,  
      "result": {  
        "clientOrderId": "myOrder1",  
        "cumQty": "0",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 283194212,  
        "origQty": "11",  
        "origType": "TRAILING_STOP_MARKET",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "CANCELED",  
        "stopPrice": "9300",                  
        "closePosition": false,    
        "symbol": "BTCUSDT",  
        "timeInForce": "GTC",  
        "type": "TRAILING_STOP_MARKET",  
        "activatePrice": "9020",              
        "priceRate": "0.3",                  
        "updateTime": 1571110484038,  
        "workingType": "CONTRACT_PRICE",  
        "priceProtect": false,             
        "priceMatch": "NONE",                
        "selfTradePreventionMode": "NONE",  
        "goodTillDate": 0                   
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 1  
        }  
      ]  
    }