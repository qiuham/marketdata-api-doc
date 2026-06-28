---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order
api_type: Trading
updated_at: 2026-01-15T23:45:48.810366
---

# Query Current UM Open Conditional Order(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#api-description "Direct link to API Description")

Query Current UM Open Conditional Order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/conditional/openOrder`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
strategyId| LONG| NO|   
newClientStrategyId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `strategyId` or `newClientStrategyId` must be sent.
>   * If the queried order has been `CANCELED`, `TRIGGERED`或`EXPIRED`, the error message "Order does not exist" will be returned.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#response-example "Direct link to Response Example")
    
    
    {              
        "newClientStrategyId": "abc",   
        "strategyId":123445,  
        "strategyStatus":"NEW",  
        "strategyType": "TRAILING_STOP_MARKET",      
        "origQty": "0.40",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",                // please ignore when order type is TRAILING_STOP_MARKET  
        "symbol": "BTCUSDT",   
        "bookTime": 1566818724710,              // order time   
        "updateTime": 1566818724722,  
        "timeInForce": "GTC",  
        "activatePrice": "9020",            // activation price, only return with TRAILING_STOP_MARKET order  
        "priceRate": "0.3",               // callback rate, only return with TRAILING_STOP_MARKET order   
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"                 
    }

---

# 查询UM当前条件挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#接口描述 "接口描述的直接链接")

查询UM当前条件挂单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/conditional/openOrder`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
strategyId| LONG| NO|   
newClientStrategyId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意:

>   * `strategyId` 与 `newClientStrategyId` 中的一个为必填参数.
>   * 如果查询的条件单已经为`CANCELED`， `TRIGGERED`或`EXPIRED`，会报错"Order does not exist"
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#响应示例 "响应示例的直接链接")
    
    
    {              
        "newClientStrategyId": "abc",   
        "strategyId":123445,  
        "strategyStatus":"NEW",  
        "strategyType": "TRAILING_STOP_MARKET",                                  
        "origQty": "0.40",                        
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",                 
        "symbol": "BTCUSDT",  
        "bookTime": 1566818724710,       //条件单下单时间          
        "updateTime": 1566818724722,  
        "timeInForce": "GTC",  
        "activatePrice": "9020",             
        "priceRate": "0.3",  
        "selfTradePreventionMode": "NONE",  
        "goodTillDate": 0,  
        "priceMatch": "NONE"                       
    }