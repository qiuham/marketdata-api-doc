---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:40.507680
---

# Query All Margin Account Orders (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#api-description "Direct link to API Description")

Query All Margin Account Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/allOrders`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#weight "Direct link to Weight")

**100**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 500.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
**Notes:**

  * If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
  * For some historical orders cummulativeQuoteQty will be < 0, meaning the data is not available at this time.



## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#response "Direct link to Response:")
    
    
    [  
          {  
              "clientOrderId": "D2KDy4DIeS56PvkM13f8cP",  
              "cummulativeQuoteQty": "0.00000000",  
              "executedQty": "0.00000000",  
              "icebergQty": "0.00000000",  
              "isWorking": false,  
              "orderId": 41295,  
              "origQty": "5.31000000",  
              "price": "0.22500000",  
              "side": "SELL",  
              "status": "CANCELED",  
              "stopPrice": "0.18000000",  
              "symbol": "BNBBTC",  
              "time": 1565769338806,  
              "timeInForce": "GTC",  
              "type": "TAKE_PROFIT_LIMIT",  
              "updateTime": 1565769342148，  
              "accountId": 152950866,  
              "selfTradePreventionMode": "EXPIRE_TAKER",  
              "preventedMatchId": null,  
              "preventedQuantity": null  
          }  
    ]

---

# 查询杠杆账户的所有订单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#接口描述 "接口描述的直接链接")

查询杠杆账户的所有订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#请求权重 "请求权重的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认 500;最大500.  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
**注意:**

  * 如果设置 `orderId` , 获取订单 >= `orderId`， 否则返回近期订单历史。
  * 一些历史订单的 cummulativeQuoteQty < 0, 是指当前数据不存在。



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
          {  
              "clientOrderId": "D2KDy4DIeS56PvkM13f8cP",  
              "cummulativeQuoteQty": "0.00000000",  
              "executedQty": "0.00000000",  
              "icebergQty": "0.00000000",  
              "isWorking": false,  
              "orderId": 41295,  
              "origQty": "5.31000000",  
              "price": "0.22500000",  
              "side": "SELL",  
              "status": "CANCELED",  
              "stopPrice": "0.18000000",  
              "symbol": "BNBBTC",  
              "time": 1565769338806,  
              "timeInForce": "GTC",  
              "type": "TAKE_PROFIT_LIMIT",  
              "updateTime": 1565769342148，  
              "accountId": 152950866,  
              "selfTradePreventionMode": "EXPIRE_TAKER",  
              "preventedMatchId": null,  
              "preventedQuantity": null  
          }  
    ]