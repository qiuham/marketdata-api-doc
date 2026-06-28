---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order
api_type: Trading
updated_at: 2026-01-15T23:47:27.101880
---

# Query Algo Order (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#api-description "Direct link to API Description")

Check an algo order's status.

  * These orders will not be found: 
    * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
    * order create time + 90 days < current time



## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#http-request "Direct link to HTTP Request")

GET `/fapi/v1/algoOrder`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
algoId| LONG| NO|   
clientAlgoId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `algoId` or `clientAlgoId` must be sent.
>   * `algoId` is self-increment for each specific `symbol`
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#response-example "Direct link to Response Example")
    
    
    {  
       "algoId": 2146760,  
       "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
       "algoType": "CONDITIONAL",  
       "orderType": "TAKE_PROFIT",  
       "symbol": "BNBUSDT",  
       "side": "SELL",  
       "positionSide": "BOTH",  
       "timeInForce": "GTC",  
       "quantity": "0.01",  
       "algoStatus": "CANCELED",  
       "actualOrderId": "",  
       "actualPrice": "0.00000",  
       "triggerPrice": "750.000",  
       "price": "750.000",  
       "icebergQuantity": null,  
       "tpTriggerPrice": "0.000",  
       "tpPrice": "0.000",  
       "slTriggerPrice": "0.000",  
       "slPrice": "0.000",  
       "tpOrderType": "",  
       "selfTradePreventionMode": "EXPIRE_MAKER",  
       "workingType": "CONTRACT_PRICE",  
       "priceMatch": "NONE",  
       "closePosition": false,  
       "priceProtect": false,  
       "reduceOnly": false,  
       "createTime": 1750485492076,  
       "updateTime": 1750514545091,  
       "triggerTime": 0,  
       "goodTillDate": 0  
    }

---

# 查询条件订单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#接口描述 "接口描述的直接链接")

查询条件订单状态

  * 请注意，如果订单满足如下条件，不会被查询到： 
    * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
    * 订单创建时间 + 90天 < 当前时间



## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/algoOrder`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
algoId| LONG| NO| 系统订单号  
clientAlgoId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意:

>   * 至少需要发送 `algoId` 与 `clientAlgoId`中的一个
>   * `algoId`在`symbol`维度是自增的
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#响应示例 "响应示例的直接链接")
    
    
    {  
       "algoId": 2146760,  
       "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
       "algoType": "CONDITIONAL",  
       "orderType": "TAKE_PROFIT",  
       "symbol": "BNBUSDT",  
       "side": "SELL",  
       "positionSide": "BOTH",  
       "timeInForce": "GTC",  
       "quantity": "0.01",  
       "algoStatus": "CANCELED",  
       "actualOrderId": "",  
       "actualPrice": "0.00000",  
       "triggerPrice": "750.000",  
       "price": "750.000",  
       "icebergQuantity": null,  
       "tpTriggerPrice": "0.000",  
       "tpPrice": "0.000",  
       "slTriggerPrice": "0.000",  
       "slPrice": "0.000",  
       "tpOrderType": "",  
       "selfTradePreventionMode": "EXPIRE_MAKER",  
       "workingType": "CONTRACT_PRICE",  
       "priceMatch": "NONE",  
       "closePosition": false,  
       "priceProtect": false,  
       "reduceOnly": false,  
       "createTime": 1750485492076,  
       "updateTime": 1750514545091,  
       "triggerTime": 0,  
       "goodTillDate": 0  
    }