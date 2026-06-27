---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order
api_type: WebSocket
updated_at: 2026-01-15T23:40:04.123777
---

# Query Order (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#api-description "Direct link to API Description")

Check an order's status.

  * These orders will not be found: 
    * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
    * order create time + 90 days < current time



## Method[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#method "Direct link to Method")

`order.status`

## Request[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#request "Direct link to Request")
    
    
    {  
        "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
        "method": "order.status",  
        "params": {  
            "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
            "orderId": 328999071,  
            "symbol": "BTCUSD_PERP",  
            "timestamp": 1703441060152,  
            "signature": "ba48184fc38a71d03d2b5435bd67c1206e3191e989fe99bda1bc643a880dfdbf"  
        }  
    }  
    

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `orderId` or `origClientOrderId` must be sent.
>   * `orderId` is self-increment for each specific `symbol`
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#response-example "Direct link to Response Example")
    
    
    {  
        "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
        "status": 200,  
        "result": {  
            "orderId": 328999071,  
            "symbol": "BTCUSD_PERP",  
            "pair": "BTCUSD",  
            "status": "NEW",  
            "clientOrderId": "ArY8Ng1rln0s9x3fclmAHy",  
            "price": "58000",  
            "avgPrice": "0.00",  
            "origQty": "1",  
            "executedQty": "0",  
            "cumBase": "0",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "reduceOnly": false,  
            "closePosition": false,  
            "side": "BUY",  
            "positionSide": "LONG",  
            "stopPrice": "0",  
            "workingType": "CONTRACT_PRICE",  
            "priceProtect": false,  
            "origType": "LIMIT",  
            "selfTradePreventionMode": "EXPIRE_TAKER",  
            "time": 1733740063619,  
            "updateTime": 1733740063619,  
            "priceMatch": "NONE"  
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

# 查询订单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#接口描述 "接口描述的直接链接")

查询订单状态

  * 请注意，如果订单满足如下条件，不会被查询到： 
    * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
    * 订单创建时间 + 90天 < 当前时间



## 方式[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#方式 "方式的直接链接")

`order.status`

## 请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#请求 "请求的直接链接")
    
    
    {  
        "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
        "method": "order.status",  
        "params": {  
            "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
            "orderId": 328999071,  
            "symbol": "BTCUSD_PERP",  
            "timestamp": 1703441060152,  
            "signature": "ba48184fc38a71d03d2b5435bd67c1206e3191e989fe99bda1bc643a880dfdbf"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意:

>   * 至少需要发送 `orderId` 与 `origClientOrderId`中的一个
>   * `orderId`在`symbol`维度是自增的
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
        "status": 200,  
        "result": {  
            "orderId": 328999071,  
            "symbol": "BTCUSD_PERP",  
            "pair": "BTCUSD",  
            "status": "NEW",  
            "clientOrderId": "ArY8Ng1rln0s9x3fclmAHy",  
            "price": "58000",  
            "avgPrice": "0.00",  
            "origQty": "1",  
            "executedQty": "0",  
            "cumBase": "0",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "reduceOnly": false,  
            "closePosition": false,  
            "side": "BUY",  
            "positionSide": "LONG",  
            "stopPrice": "0",  
            "workingType": "CONTRACT_PRICE",  
            "priceProtect": false,  
            "origType": "LIMIT",  
            "selfTradePreventionMode": "EXPIRE_TAKER",  
            "time": 1733740063619,  
            "updateTime": 1733740063619,  
            "priceMatch": "NONE"  
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