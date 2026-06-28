---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:37.002359
---

# Query All CM Orders (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#api-description "Direct link to API Description")

Get all account CM orders; active, canceled, or filled.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/allOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **40** with pair

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
pair| STRING| NO|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 50; max 100.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `symbol` or `pair` must be sent.
>   * If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
>   * These orders will not be found: 
>     * order status is `CANCELED` or `EXPIRED`, **AND**
>     * order has NO filled trade, **AND**
>     * created time + 3 days < current time
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "avgPrice": "0.0",  
        "clientOrderId": "abc",  
        "cumBase": "0",  
        "executedQty": "0",  
        "orderId": 1917641,  
        "origQty": "0.40",  
        "origType": "LIMIT",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "time": 1579276756075,              // order time  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075       // update time  
      }  
    ]

---

# 查询所有CM订单(包括历史订单)(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Orders#接口描述 "接口描述的直接链接")

查询所有CM订单(包括历史订单)

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Orders#请求权重 "请求权重的直接链接")

传symbol **20** ，传pairs **40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
pair| STRING| NO|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 返回的结果集数量 默认值:50 最大值:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `symbol` 或 `pair` 必须传一个,不能同时传
>   * 请注意，如果订单满足如下条件，不会被查询到： 
>     * 订单的最终状态为 `CANCELED` 或 `EXPIRED`, **AND**
>     * 订单没有任何的成交记录，并且
>     * 订单生成时间 + 3天 < 当前时间
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "avgPrice": "0.0",  
        "clientOrderId": "abc",  
        "cumBase": "0",  
        "executedQty": "0",  
        "orderId": 1917641,  
        "origQty": "0.40",  
        "origType": "LIMIT",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "time": 1579276756075,              // order time  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075       // update time  
      }  
    ]