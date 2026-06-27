---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History
api_type: Account
updated_at: 2026-01-15T23:44:12.945711
---

# Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#api-description "Direct link to API Description")

Query interest history of negative balance for portfolio margin.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/interest-history`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#request-weightip "Direct link to Request Weight\(IP\)")

**50**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "USDT",      
            "interest": "24.4440",               //interest amount  
            "interestAccruedTime": 1670227200000,  
            "interestRate": "0.0001164",         //daily interest rate  
            "principal": "210000"  
        }   
    ]

---

# 查询经典统一账户专业版期货负余额收息历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#接口描述 "接口描述的直接链接")

查询统一账户专业版期货负余额收息历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/interest-history`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#请求权重ip "请求权重\(IP\)的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
size| LONG| NO| 返回的结果集数量 默认值:10 最大值:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "USDT",      
            "interest": "24.4440",               //利息金额  
            "interestAccruedTime": 1670227200000,  
            "interestRate": "0.0001164",         //日利率   
            "principal": "210000"  
        }   
    ]