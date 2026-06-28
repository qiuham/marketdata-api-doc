---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:44.587506
---

# Query All UM Orders(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders#api-description "Direct link to API Description")

Get all account UM orders; active, canceled, or filled.

  * These orders will not be found: 
    * order status is `CANCELED` or `EXPIRED`, **AND**
    * order has NO filled trade, **AND**
    * created time + 3 days < current time



## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/allOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
>   * The query time period must be less then 7 days( default as the recent 7 days).
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "avgPrice": "0.00000",  
        "clientOrderId": "abc",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 1917641,  
        "origQty": "0.40",  
        "origType": "LIMIT",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSDT",  
        "time": 1579276756075,              // order time  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075,        // update time    
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"   
      }  
    ]

---

# 查询所有UM订单(包括历史订单)(USER_DATA)

## API Description[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Orders#api-description "API Description的直接链接")

查询所有UM订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Orders#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 或 `origClientOrderId` 必须至少发送一个
>   * 请注意，如果订单满足如下条件，不会被查询到： 
>     * 订单的最终状态为 `CANCELED` 或 `EXPIRED`，并且
>     * 订单没有任何的成交记录，并且
>     * 订单生成时间 + 3天 < 当前时间
>   * 查询时间范围最大不得超过7天
>   * 默认查询最近7天内的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "avgPrice": "0.00000",  
        "clientOrderId": "abc",  
        "cumQuote": "0",  
        "executedQty": "0",  
        "orderId": 1917641,  
        "origQty": "0.40",  
        "origType": "LIMIT",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSDT",  
        "time": 1579276756075,                
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075，  
        "selfTradePreventionMode": "NONE",   
        "goodTillDate": 0,  
        "priceMatch": "NONE"           
      }  
    ]