---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:40.375112
---

# Query All Current UM Open Conditional Orders(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#api-description "Direct link to API Description")

Get all open conditional orders on a symbol.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#http-request "Direct link to HTTP Request")

`GET /papi/v1/um/conditional/openOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted **Careful** when accessing this with no symbol.

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If the symbol is not sent, orders for all symbols will be returned in an array.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#response-example "Direct link to Response Example")
    
    
    [  
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
    ]

---

# 查看UM当前全部条件挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#接口描述 "接口描述的直接链接")

查看UM当前全部条件挂单。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/conditional/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#请求权重 "请求权重的直接链接")

带symbol **1** ; 不带**40** 请小心使用不带symbol参数的调用

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 不带symbol参数，会返回所有交易对的条件挂单
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
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
        "bookTime": 1566818724710,   //条件单下单时间               
        "updateTime": 1566818724722,  
        "timeInForce": "GTC",  
        "activatePrice": "9020",             
        "priceRate": "0.3",  
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"               
      }  
    ]