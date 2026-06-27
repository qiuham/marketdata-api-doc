---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order
api_type: WebSocket
updated_at: 2026-01-15T23:39:57.069407
---

# Cancel Order (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#api-description "Direct link to API Description")

Cancel an active order.

## Method[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#method "Direct link to Method")

`order.cancel`

## Request[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#request "Direct link to Request")
    
    
    {  
      "id": "a8627ea5-8b9f-452f-90ae-4136f2b442e2",  
      "method": "order.cancel",  
      "params": {  
        "apiKey": "",  
        "orderId": 333245211,  
        "symbol": "BTCUSD_PERP",  
        "timestamp": 1728416090517,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#response-example "Direct link to Response Example")
    
    
    {  
        "id": "a8627ea5-8b9f-452f-90ae-4136f2b442e2",  
        "status": 200,  
        "result": {  
            "orderId": 333245211,  
            "symbol": "BTCUSD_PERP",  
            "pair": "BTCUSD",  
            "status": "CANCELED",  
            "clientOrderId": "5SztZiGFAxgAqw4J9EN9fA",  
            "price": "51000",  
            "avgPrice": "0.00",  
            "origQty": "1",  
            "executedQty": "0",  
            "cumQty": "0",  
            "cumBase": "0",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "reduceOnly": false,  
            "closePosition": false,  
            "side": "BUY",  
            "positionSide": "BOTH",  
            "stopPrice": "0",  
            "workingType": "CONTRACT_PRICE",  
            "priceProtect": false,  
            "origType": "LIMIT",  
            "updateTime": 1728416138285  
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

# 撤销订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#接口描述 "接口描述的直接链接")

撤销订单

## 方式[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#方式 "方式的直接链接")

`order.cancel`

## 请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#请求 "请求的直接链接")
    
    
    {  
      "id": "a8627ea5-8b9f-452f-90ae-4136f2b442e2",  
      "method": "order.cancel",  
      "params": {  
        "apiKey": "",  
        "orderId": 333245211,  
        "symbol": "BTCUSD_PERP",  
        "timestamp": 1728416090517,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 与 `origClientOrderId` 必须至少发送一个
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "id": "a8627ea5-8b9f-452f-90ae-4136f2b442e2",  
        "status": 200,  
        "result": {  
            "orderId": 333245211,  
            "symbol": "BTCUSD_PERP",  
            "pair": "BTCUSD",  
            "status": "CANCELED",  
            "clientOrderId": "5SztZiGFAxgAqw4J9EN9fA",  
            "price": "51000",  
            "avgPrice": "0.00",  
            "origQty": "1",  
            "executedQty": "0",  
            "cumQty": "0",  
            "cumBase": "0",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "reduceOnly": false,  
            "closePosition": false,  
            "side": "BUY",  
            "positionSide": "BOTH",  
            "stopPrice": "0",  
            "workingType": "CONTRACT_PRICE",  
            "priceProtect": false,  
            "origType": "LIMIT",  
            "updateTime": 1728416138285  
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