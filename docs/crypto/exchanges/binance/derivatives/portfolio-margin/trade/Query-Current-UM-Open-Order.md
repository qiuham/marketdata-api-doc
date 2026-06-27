---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order
api_type: Trading
updated_at: 2026-01-15T23:45:48.877974
---

# Query Current UM Open Order(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#api-description "Direct link to API Description")

Query current UM open order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/openOrder`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Notes:

>   * Either `orderId` or `origClientOrderId` must be sent.
>   * If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#response-example "Direct link to Response Example")
    
    
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
        "updateTime": 1579276756075，  
        "selfTradePreventionMode": "NONE",   
        "goodTillDate": 0,  
        "priceMatch": "NONE"              
    }

---

# 查询当前UM挂单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#接口描述 "接口描述的直接链接")

查询当前UM挂单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/openOrder`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
注意:

>   * `orderId` 或 `origClientOrderId` 必须至少发送一个
>   * 查询的订单如果已经成交或取消，将返回报错 "Order does not exist"
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#响应示例 "响应示例的直接链接")
    
    
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
        "updateTime": 1579276756075，  
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"          
    }