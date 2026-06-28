---
exchange: binance
source_url: https://developers.binance.com/docs/convert/trade/Order-Status
api_type: Trading
updated_at: 2026-06-28 18:55:45.764083
---

# Query limit open orders (USER_DATA)

## API Description[​](/docs/convert/trade/Query-Order#api-description "Direct link to API Description")

Request a quote for the requested token pairs

## HTTP Request[​](/docs/convert/trade/Query-Order#http-request "Direct link to HTTP Request")

GET `/sapi/v1/convert/limit/queryOpenOrders`

## Request Weight[​](/docs/convert/trade/Query-Order#request-weight "Direct link to Request Weight")

**3000(UID)**

## Request Parameters[​](/docs/convert/trade/Query-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/convert/trade/Query-Order#response-example "Direct link to Response Example")
    
    
    {  
        "list": [  
            {  
                "quoteId": "18sdf87kh9df",   
                "orderId": 1150901289839,   
                "orderStatus": "SUCCESS",   
                "fromAsset": "BNB",   
                "fromAmount": "10",   
                "toAsset": "USDT",   
                "toAmount": "2317.89",   
                "ratio": "231.789",   
                "inverseRatio": "0.00431427",   
                "createTime": 1614089498000,  
               "expiredTimestamp": 1614099498000  
            }  
        ]  
    }

---

# 查询闪兑限价单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/convert/trade/Query-Order#接口描述 "接口描述的直接链接")

查询闪兑限价单

## HTTP请求[​](/docs/zh-CN/convert/trade/Query-Order#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/convert/limit/queryOpenOrders`

## 请求权重[​](/docs/zh-CN/convert/trade/Query-Order#请求权重 "请求权重的直接链接")

**3000(UID)**

## 请求参数[​](/docs/zh-CN/convert/trade/Query-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 该值不大于60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/convert/trade/Query-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "list": [  
            {  
                "quoteId": "18sdf87kh9df",   
                "orderId": 1150901289839,   
                "orderStatus": "SUCCESS",   
                "fromAsset": "BNB",   
                "fromAmount": "10",   
                "toAsset": "USDT",   
                "toAmount": "2317.89",   
                "ratio": "231.789",   
                "inverseRatio": "0.00431427",   
                "createTime": 1614089498000,  
               "expiredTimestamp": 1614099498000  
            }  
        ]  
    }