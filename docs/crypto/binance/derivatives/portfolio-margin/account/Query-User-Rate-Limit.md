---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit
api_type: Account
updated_at: 2026-01-15T23:45:14.673167
---

# Query User Rate Limit (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#api-description "Direct link to API Description")

Query User Rate Limit

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#http-request "Direct link to HTTP Request")

GET `/papi/v1/rateLimit/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#response-example "Direct link to Response Example")
    
    
    [  
      {  
            "rateLimitType": "ORDERS",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 1200  
        }  
    ]

---

# 查询用户下单限频 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Rate-Limit#接口描述 "接口描述的直接链接")

查询用户下单限频

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Rate-Limit#http请求 "HTTP请求的直接链接")

GET `/papi/v1/rateLimit/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Rate-Limit#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Rate-Limit#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Rate-Limit#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
            "rateLimitType": "ORDERS",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 1200  
        }  
    ]