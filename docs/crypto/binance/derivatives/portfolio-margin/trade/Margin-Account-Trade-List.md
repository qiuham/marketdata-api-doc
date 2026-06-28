---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List
api_type: Trading
updated_at: 2026-01-15T23:45:33.464283
---

# Margin Account Trade List (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#api-description "Direct link to API Description")

Margin Account Trade List

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/myTrades`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#weight "Direct link to Weight")

**5**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
**Notes:**

  * If `fromId` is set, it will get trades >= that `fromId`. Otherwise most recent trades are returned.
  * Less than 24 hours between `startTime` and `endTime`.



## Response:[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#response "Direct link to Response:")
    
    
    [  
        {  
            "commission": "0.00006000",  
            "commissionAsset": "BTC",  
            "id": 34,  
            "isBestMatch": true,  
            "isBuyer": false,  
            "isMaker": false,  
            "orderId": 39324,  
            "price": "0.02000000",  
            "qty": "3.00000000",  
            "symbol": "BNBBTC",  
            "time": 1561973357171  
        }  
    ]

---

# 查询杠杆账户交易历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#接口描述 "接口描述的直接链接")

查询杠杆账户交易历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/myTrades`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| 获取TradeId，默认获取近期交易历史。  
limit| INT| NO| 默认 500; 最大 1000.  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
**注意:**

  * 如果设置 `fromId` , 获取订单 id >= `fromId`， 否则返回近期订单历史。
  * `startTime` 和 `endTime`的间隔需要小于24小时。



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "commission": "0.00006000",  
            "commissionAsset": "BTC",  
            "id": 34,  
            "isBestMatch": true,  
            "isBuyer": false,  
            "isMaker": false,  
            "orderId": 39324,  
            "price": "0.02000000",  
            "qty": "3.00000000",  
            "symbol": "BNBBTC",  
            "time": 1561973357171  
        }  
    ]