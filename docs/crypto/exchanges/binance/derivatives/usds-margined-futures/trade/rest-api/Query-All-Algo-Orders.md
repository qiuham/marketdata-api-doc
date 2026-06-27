---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders
api_type: Trading
updated_at: 2026-01-15T23:47:31.442778
---

# Query All Algo Orders (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#api-description "Direct link to API Description")

Get all algo orders; active, CANCELED, TRIGGERED or FINISHED .

  * These orders will not be found: 
    * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
    * order create time + 90 days < current time



## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#http-request "Direct link to HTTP Request")

GET `/fapi/v1/allAlgoOrders`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
algoId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| NO|   
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**Notes:**

>   * If `algoId` is set, it will get orders >= that `algoId`. Otherwise most recent orders are returned.
>   * The query time period must be less then 7 days( default as the recent 7 days).
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#response-example "Direct link to Response Example")
    
    
    [  
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
    ]

---

# 查询所有条件订单(包括历史订单) (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#接口描述 "接口描述的直接链接")

查询所有条件订单(包括历史订单)

  * 请注意，如果订单满足如下条件，不会被查询到： 
    * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
    * 订单创建时间 + 90天 < 当前时间



## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/allAlgoOrders`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
algoId| LONG| NO| 只返回此orderID及之后的订单，缺省返回最近的订单  
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| NO|   
limit| INT| NO| 返回的结果集数量 默认值:500 最大值:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 查询时间范围最大不得超过7天
>   * 默认查询最近7天内的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
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
    ]