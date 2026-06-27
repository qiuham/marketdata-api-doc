---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders
api_type: Trading
updated_at: 2026-05-27 18:57:48.533157
---

# Query Margin Account's All Orders (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Query-Margin-Account-All-Orders#api-description "Direct link to API Description")

Query Margin Account's All Orders

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Account-All-Orders#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/allOrders`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Account-All-Orders#request-weight "Direct link to Request Weight")

**200(IP)**

## Request Limit[​](/docs/margin_trading/trade/Query-Margin-Account-All-Orders#request-limit "Direct link to Request Limit")

**60times/min per IP**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Account-All-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 500.  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * If orderId is set, it will get orders >= that orderId. Otherwise the orders within 24 hours are returned.
  * For some historical orders cummulativeQuoteQty will be < 0, meaning the data is not available at this time.
  * Less than 24 hours between startTime and endTime.



## Response Example[​](/docs/margin_trading/trade/Query-Margin-Account-All-Orders#response-example "Direct link to Response Example")
    
    
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
              "isIsolated": false,  
              "time": 1565769338806,  
              "timeInForce": "GTC",  
              "type": "TAKE_PROFIT_LIMIT",  
              "selfTradePreventionMode": "NONE",  
              "updateTime": 1565769342148  
          },  
          {  
              "clientOrderId": "gXYtqhcEAs2Rn9SUD9nRKx",  
              "cummulativeQuoteQty": "0.00000000",  
              "executedQty": "0.00000000",  
              "icebergQty": "1.00000000",  
              "isWorking": true,  
              "orderId": 41296,  
              "origQty": "6.65000000",  
              "price": "0.18000000",  
              "side": "SELL",  
              "status": "CANCELED",  
              "stopPrice": "0.00000000",  
              "symbol": "BNBBTC",  
              "isIsolated": false,  
              "time": 1565769348687,  
              "timeInForce": "GTC",  
              "type": "LIMIT",  
              "selfTradePreventionMode": "NONE",  
              "updateTime": 1565769352226  
          }  
    ]

---

# 查询杠杆账户的所有订单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-Orders#接口描述 "接口描述的直接链接")

查询杠杆账户的所有订单

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-Orders#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/allOrders`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-Orders#请求权重 "请求权重的直接链接")

**200(IP)**

## 访问限制[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-Orders#访问限制 "访问限制的直接链接")

**60次/分钟/IP**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认 500;最大500.  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 如果设置 orderId , 获取订单 >= orderId ， 否则返回24小时内的订单历史。
  * 一些历史订单的 cummulativeQuoteQty < 0, 是指当前数据不存在。
  * startTime和endTime的时间间隔不可超过24小时



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-Orders#响应示例 "响应示例的直接链接")
    
    
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
              "isIsolated": false,       // 是否是逐仓symbol交易   
              "time": 1565769338806,  
              "timeInForce": "GTC",  
              "type": "TAKE_PROFIT_LIMIT",  
              "selfTradePreventionMode": "NONE",  
              "updateTime": 1565769342148  
          },  
          {  
              "clientOrderId": "gXYtqhcEAs2Rn9SUD9nRKx",  
              "cummulativeQuoteQty": "0.00000000",  
              "executedQty": "0.00000000",  
              "icebergQty": "1.00000000",  
              "isWorking": true,  
              "orderId": 41296,  
              "origQty": "6.65000000",  
              "price": "0.18000000",  
              "side": "SELL",  
              "status": "CANCELED",  
              "stopPrice": "0.00000000",  
              "symbol": "BNBBTC",  
              "isIsolated": false,       // 是否是逐仓symbol交易   
              "time": 1565769348687,  
              "timeInForce": "GTC",  
              "type": "LIMIT",  
              "selfTradePreventionMode": "NONE",  
              "updateTime": 1565769352226  
          }  
      
    ]