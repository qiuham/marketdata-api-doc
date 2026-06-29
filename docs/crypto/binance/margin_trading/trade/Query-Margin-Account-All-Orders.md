---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders
api_type: Trading
updated_at: 2026-06-29 19:10:32.279429
---

# Query Margin Account's Order (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Query-Margin-Account-Order#api-description "Direct link to API Description")

Query Margin Account's Order

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Account-Order#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/order`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Account-Order#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Account-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * Either orderId or origClientOrderId must be sent.
  * For some historical orders cummulativeQuoteQty will be < 0, meaning the data is not available at this time.



## Response Example[​](/docs/margin_trading/trade/Query-Margin-Account-Order#response-example "Direct link to Response Example")
    
    
    {  
       "clientOrderId": "ZwfQzuDIGpceVhKW5DvCmO",  
       "cummulativeQuoteQty": "0.00000000",  
       "executedQty": "0.00000000",  
       "icebergQty": "0.00000000",  
       "isWorking": true,  
       "orderId": 213205622,  
       "origQty": "0.30000000",  
       "price": "0.00493630",  
       "side": "SELL",  
       "status": "NEW",  
       "stopPrice": "0.00000000",  
       "symbol": "BNBBTC",  
       "isIsolated": true,  
       "time": 1562133008725,  
       "timeInForce": "GTC",  
       "type": "LIMIT",  
       "selfTradePreventionMode": "NONE",  
       "updateTime": 1562133008725  
    }

---

# 查询杠杆账户订单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Order#接口描述 "接口描述的直接链接")

查询杠杆账户订单

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Order#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/order`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Order#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 必须发送 orderId 或 origClientOrderId 其中一个。
  * 一些历史订单的 cummulativeQuoteQty < 0, 是指当前数据不存在。



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Order#响应示例 "响应示例的直接链接")
    
    
    {  
       "clientOrderId": "ZwfQzuDIGpceVhKW5DvCmO",  
       "cummulativeQuoteQty": "0.00000000",  
       "executedQty": "0.00000000",  
       "icebergQty": "0.00000000",  
       "isWorking": true,  
       "orderId": 213205622,  
       "origQty": "0.30000000",  
       "price": "0.00493630",  
       "side": "SELL",  
       "status": "NEW",  
       "stopPrice": "0.00000000",  
       "symbol": "BNBBTC",  
       "isIsolated": true,  
       "time": 1562133008725,  
       "timeInForce": "GTC",  
       "type": "LIMIT",  
       "selfTradePreventionMode": "NONE",  
       "updateTime": 1562133008725  
    }