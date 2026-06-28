---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order
api_type: Trading
updated_at: 2026-01-15T23:45:52.553145
---

# Query Margin Account Order (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#api-description "Direct link to API Description")

Query Margin Account Order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/order`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#weight "Direct link to Weight")

**10**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
**Notes:**

  * Either `orderId` or `origClientOrderId` must be sent.
  * For some historical orders cummulativeQuoteQty will be < 0, meaning the data is not available at this time.



## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#response "Direct link to Response:")
    
    
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
       "time": 1562133008725,  
       "timeInForce": "GTC",  
       "type": "LIMIT",  
       "updateTime": 1562133008725，  
       "accountId": 152950866,  
       "selfTradePreventionMode": "EXPIRE_TAKER",  
       "preventedMatchId": null,  
       "preventedQuantity": null  
    }

---

# 查询杠杆账户订单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#接口描述 "接口描述的直接链接")

查询杠杆账户订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
**注意:**

  * 必须发送 `orderId` 或 `origClientOrderId` 其中一个。
  * 一些历史订单的 cummulativeQuoteQty < 0, 是指当前数据不存在。



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Order#响应示例 "响应示例的直接链接")
    
    
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
       "time": 1562133008725,  
       "timeInForce": "GTC",  
       "type": "LIMIT",  
       "updateTime": 1562133008725，  
       "accountId": 152950866,  
       "selfTradePreventionMode": "EXPIRE_TAKER",  
       "preventedMatchId": null,  
       "preventedQuantity": null  
    }