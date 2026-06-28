---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Open-Orders
api_type: Trading
updated_at: 2026-05-27 18:57:52.912574
---

# Query Margin Account's Open Orders (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Query-Margin-Account-Open-Orders#api-description "Direct link to API Description")

Query Margin Account's Open Orders

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Account-Open-Orders#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/openOrders`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Account-Open-Orders#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Account-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * If the symbol is not sent, orders for all symbols will be returned in an array.
  * When all symbols are returned, the number of requests counted against the rate limiter is equal to the number of symbols currently trading on the exchange.
  * If isIsolated ="TRUE", symbol must be sent.



## Response Example[​](/docs/margin_trading/trade/Query-Margin-Account-Open-Orders#response-example "Direct link to Response Example")
    
    
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
           "isIsolated": true,  
           "time": 1562040170089,  
           "timeInForce": "GTC",  
           "type": "LIMIT",  
           "selfTradePreventionMode": "NONE",  
           "updateTime": 1562040170089  
    	}  
    ]

---

# 查询杠杆账户挂单记录 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-Orders#接口描述 "接口描述的直接链接")

查询杠杆账户挂单记录

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-Orders#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/openOrders`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-Orders#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 如未发送symbol，返回所有 symbols 订单记录。
  * 当返回所有symbols时，针对限速器计数的请求数量等于当前在交易所交易的symbols数量。
  * 如果 isIsolated = "TRUE", symbol 为必填



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-Orders#响应示例 "响应示例的直接链接")
    
    
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
           "isIsolated": true,       // 是否是逐仓symbol交易  
           "time": 1562040170089,  
           "timeInForce": "GTC",  
           "type": "LIMIT",  
           "selfTradePreventionMode": "NONE",  
           "updateTime": 1562040170089  
    	}  
    ]