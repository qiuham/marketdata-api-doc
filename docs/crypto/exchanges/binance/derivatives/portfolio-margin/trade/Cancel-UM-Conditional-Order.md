---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order
api_type: Trading
updated_at: 2026-01-15T23:45:25.372754
---

# Cancel UM Conditional Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#api-description "Direct link to API Description")

Cancel UM Conditional Order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#http-request "Direct link to HTTP Request")

DELETE `/papi/v1/um/conditional/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
strategyId| LONG| NO|   
newClientStrategyId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `strategyId` or `newClientStrategyId` must be sent.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#response-example "Direct link to Response Example")
    
    
    {  
        "newClientStrategyId": "myOrder1",  
        "strategyId":123445,  
        "strategyStatus":"CANCELED",  
        "strategyType": "TRAILING_STOP_MARKET",    
        "origQty": "11",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",                // please ignore when order type is TRAILING_STOP_MARKET  
        "symbol": "BTCUSDT",  
        "timeInForce": "GTC",  
        "activatePrice": "9020",            // activation price, only return with TRAILING_STOP_MARKET order  
        "priceRate": "0.3",                 // callback rate, only return with TRAILING_STOP_MARKET order  
        "bookTime": 1566818724710,  
        "updateTime": 1566818724722,  
        "workingType":"CONTRACT_PRICE",  
        "priceProtect": false,  
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"        
    }

---

# 取消UM条件订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#接口描述 "接口描述的直接链接")

取消UM条件订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/um/conditional/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
strategyId| LONG| NO|   
newClientStrategyId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `strategyId` 与 `newClientStrategyId` 之一必须发送
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "newClientStrategyId": "myOrder1",  
        "strategyId":123445,  
        "strategyStatus":"CANCELED",  
        "strategyType": "TRAILING_STOP_MARKET",    
        "origQty": "11",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",                  
        "symbol": "BTCUSDT",  
        "timeInForce": "GTC",  
        "activatePrice": "9020",              
        "priceRate": "0.3",                  
        "bookTime": 1566818724710, //条件单下单时间    
        "updateTime": 1566818724722,  
        "workingType":"CONTRACT_PRICE",  
        "priceProtect": false,  
        "selfTradePreventionMode": "NONE",   
        "goodTillDate": 0,  
        "priceMatch": "NONE"     
    }