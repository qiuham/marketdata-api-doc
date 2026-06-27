---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History
api_type: Trading
updated_at: 2026-01-15T23:45:44.711853
---

# Query CM Conditional Order History(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#api-description "Direct link to API Description")

Query CM Conditional Order History

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/conditional/orderHistory`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
strategyId| LONG| NO|   
newClientStrategyId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|    
  
**Notes:**

>   * Either `strategyId` or `newClientStrategyId` must be sent.
>   * `NEW` orders will not be found.
>   * These orders will not be found: 
>     * order status is `CANCELED` or `EXPIRED`, **AND**
>     * order has NO filled trade, **AND**
>     * created time + 7 days < current time
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#response-example "Direct link to Response Example")
    
    
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
        "symbol": "BTCUSD",   
        "orderId": 12123343534,    //Normal orderID after trigger if appliable，only have when the strategy is triggered   
        "status": "NEW",   //Normal order status after trigger if appliable, only have when the strategy is triggered  
        "bookTime": 1566818724710,              // order time   
        "updateTime": 1566818724722,  
        "triggerTime": 1566818724750,    
        "timeInForce": "GTC",  
        "type": "MARKET",     //Normal order type after trigger if appliable  
        "activatePrice": "9020",            // activation price, only return with TRAILING_STOP_MARKET order  
        "priceRate": "0.3"                // callback rate, only return with TRAILING_STOP_MARKET order    
        "workingType":"CONTRACT_PRICE",  
        "priceProtect": false,  
        "priceMatch": "NONE"      
    }

---

# 查询CM条件单历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#接口描述 "接口描述的直接链接")

查询CM条件单历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/conditional/orderHistory`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
strategyId| LONG| NO|   
newClientStrategyId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|    
  
**注意:**

>   * `strategyId` 与 `newClientStrategyId` 中的一个为必填参数.
>   * `NEW` 状态的条件订单不会返回
>   * 请注意，如果订单满足如下条件，不会被查询到： 
>     * 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且
>     * 订单没有任何的成交记录, 并且
>     * 订单生成时间 + 3天 < 当前时间
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History#响应示例 "响应示例的直接链接")
    
    
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
        "symbol": "BTCUSD",   
        "orderId": 12123343534,  //条件单触发后普通单id，当条件单被触发后才有  
        "status": "NEW",   //条件单触发后普通单状态, 当条件单被触发后才有  
        "bookTime": 1566818724710,   //条件单下单时间        
        "updateTime": 1566818724722,  
        "triggerTime": 1566818724750,    
        "timeInForce": "GTC",  
        "type": "MARKET",     //条件单触发后普通订单类型  
        "activatePrice": "9020",             
        "priceRate": "0.3",  
        "workingType":"CONTRACT_PRICE",  
        "priceProtect": false,  
        "priceMatch": "NONE"                     
    }