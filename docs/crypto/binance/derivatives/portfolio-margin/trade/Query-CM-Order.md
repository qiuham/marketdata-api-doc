---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Order
api_type: Trading
updated_at: 2026-01-15T23:45:44.854549
---

# Query CM Order(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#api-description "Direct link to API Description")

Check an CM order's status.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `orderId` or `origClientOrderId` must be sent.
>   * These orders will not be found: 
>     * order status is `CANCELED` or `EXPIRED`, **AND**
>     * order has NO filled trade, **AND**
>     * created time + 3 days < current time
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#response-example "Direct link to Response Example")
    
    
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
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "positionSide": "SHORT",  
        "time": 1579276756075,             // order time  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075        // update time  
    }

---

# 查询CM订单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Order#接口描述 "接口描述的直接链接")

查询CM订单状态

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意:

>   * `orderId` 或 `origClientOrderId` 必须至少发送一个
>   * 请注意，如果订单满足如下条件，不会被查询到： 
>     * 订单的最终状态为 `CANCELED` 或 `EXPIRED`, **AND**
>     * 订单没有任何的成交记录，并且
>     * 订单生成时间 + 3天 < 当前时间
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Order#响应示例 "响应示例的直接链接")
    
    
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
        "status": "NEW",  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "positionSide": "SHORT",  
        "time": 1579276756075,               
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "updateTime": 1579276756075          
    }