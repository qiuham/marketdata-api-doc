---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:40.444762
---

# Query All Current UM Open Orders(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#api-description "Direct link to API Description")

Get all open orders on a symbol.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/openOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If the symbol is not sent, orders for all symbols will be returned in an array.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#response-example "Direct link to Response Example")
    
    
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
        "updateTime": 1579276756075，       // update time   
        "selfTradePreventionMode": "NONE", //self trading preventation mode  
        "goodTillDate": 0,  
        "priceMatch": "NONE"    
      }  
    ]

---

# 查看当前全部UM挂单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#接口描述 "接口描述的直接链接")

查看当前全部UM挂单，请小心使用不带symbol参数的调用

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#请求权重 "请求权重的直接链接")

带symbol **1** \- 不带 **40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 不带`symbol`参数，会返回所有交易对的挂单
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#响应示例 "响应示例的直接链接")
    
    
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