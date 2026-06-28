---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:44.471897
---

# Query All UM Conditional Orders(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#api-description "Direct link to API Description")

Query All UM Conditional Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/conditional/allOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
strategyId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * These orders will not be found: 
>     * order strategyStatus is `CANCELED` or `EXPIRED`, **AND**
>     * order has NO filled trade, **AND**
>     * created time + 7 days < current time
>   * The query time period must be less than 7 days( default as the recent 7 days).
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "newClientStrategyId": "abc",   
        "strategyId":123445,  
        "strategyStatus":"TRIGGERED",  
        "strategyType": "TRAILING_STOP_MARKET",    
        "origQty": "0.40",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",                // please ignore when order type is TRAILING_STOP_MARKET  
        "symbol": "BTCUSDT",   
        "orderId":12132343435,     //Normal orderID after trigger if appliable, only have when the strategy is triggered  
        "status": "NEW",             //Normal order status after trigger if appliable, only have when the strategy is triggered        
        "bookTime": 1566818724710,              // order time   
        "updateTime": 1566818724722,  
        "triggerTime": 1566818724750,    
        "timeInForce": "GTC",  
        "type": "MARKET",     //Normal order type after trigger if appliable  
        "activatePrice": "9020",            // activation price, only return with TRAILING_STOP_MARKET order  
        "priceRate": "0.3",                // callback rate, only return with TRAILING_STOP_MARKET order  
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"    
      }  
    ]

---

# 查询UM所有条件订单(包括历史订单)(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#接口描述 "接口描述的直接链接")

查询UM所有条件订单(包括历史订单)

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/conditional/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#请求权重 "请求权重的直接链接")

带symbol **1** ; 不带**40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
strategyId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 请注意，如果订单满足如下条件，不会被查询到： 
>     * 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且
>     * 订单没有任何的成交记录, 并且
>     * 订单生成时间 + 3 天 < 当前时间
>   * 查询时间范围最大不得超过 7 天(默认查询最近 7 天内的数据).
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "newClientStrategyId": "abc",   
        "strategyId":123445,  
        "strategyStatus":"TRIGGERED",  
        "strategyType": "TRAILING_STOP_MARKET",    
        "origQty": "0.40",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",                  
        "symbol": "BTCUSDT",   
        "orderId":12132343435,  //条件单触发后普通单id，当条件单被触发后才有     
        "status": "NEW",      //条件单触发后普通单状态, 当条件单被触发后才有         
        "bookTime": 1566818724710,      //条件单下单时间          
        "updateTime": 1566818724722,  
        "triggerTime": 1566818724750,    
        "timeInForce": "GTC",  
        "type": "MARKET",    //条件单触发后普通订单类型  
        "activatePrice": "9020",              
        "priceRate": "0.3",  
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"     
      }  
    ]