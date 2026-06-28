---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order
api_type: Trading
updated_at: 2026-01-15T23:45:48.748146
---

# Query Current Margin Open Order (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#api-description "Direct link to API Description")

Query Current Margin Open Order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/openOrders`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#weight "Direct link to Weight")

**5**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
**Notes:**

  * If the `symbol` is not sent, orders for all symbols will be returned in an array.
  * When all symbols are returned, the number of requests counted against the rate limiter is equal to the number of symbols currently trading on the exchange.



## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#response "Direct link to Response:")
    
    
    [  
       {  
           "clientOrderId": "qhcZw71gAkCCTv0t0k8LUK",  
           "cummulativeQuoteQty": "0.00000000",  
           "executedQty": "0.00000000",  
           "icebergQty": "0.00000000",  
           "isWorking": true,  
           "orderId": 211842552,  
           "origQty": "0.30000000",  
           "price": "0.00475010",  
           "side": "SELL",  
           "status": "NEW",  
           "stopPrice": "0.00000000",  
           "symbol": "BNBBTC",  
           "time": 1562040170089,  
           "timeInForce": "GTC",  
           "type": "LIMIT",  
           "updateTime": 1562040170089，  
           "accountId": 152950866,  
           "selfTradePreventionMode": "EXPIRE_TAKER",  
           "preventedMatchId": null,  
           "preventedQuantity": null  
        }  
    ]

---

# 查询杠杆账户挂单记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#接口描述 "接口描述的直接链接")

查询杠杆账户挂单记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
**注意:**

  * 如未发送`symbol`，返回所有 symbols 订单记录。
  * 当返回所有symbols时，针对限速器计数的请求数量等于当前在交易所交易的symbols数量。



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order#响应示例 "响应示例的直接链接")
    
    
    [  
       {  
           "clientOrderId": "qhcZw71gAkCCTv0t0k8LUK",  
           "cummulativeQuoteQty": "0.00000000",  
           "executedQty": "0.00000000",  
           "icebergQty": "0.00000000",  
           "isWorking": true,  
           "orderId": 211842552,  
           "origQty": "0.30000000",  
           "price": "0.00475010",  
           "side": "SELL",  
           "status": "NEW",  
           "stopPrice": "0.00000000",  
           "symbol": "BNBBTC",  
           "time": 1562040170089,  
           "timeInForce": "GTC",  
           "type": "LIMIT",  
           "updateTime": 1562040170089，  
           "accountId": 152950866,  
           "selfTradePreventionMode": "EXPIRE_TAKER",  
           "preventedMatchId": null,  
           "preventedQuantity": null  
        }  
    ]