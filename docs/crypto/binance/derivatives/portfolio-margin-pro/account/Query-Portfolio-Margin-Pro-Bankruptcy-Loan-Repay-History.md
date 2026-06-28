---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History
api_type: Account
updated_at: 2026-01-15T23:44:13.009660
---

# Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#api-description "Direct link to API Description")

Query repay history of pmloan for portfolio margin pro.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/pmloan-history`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#request-weightip "Direct link to Request Weight\(IP\)")

**500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * `startTime` and `endTime` cannot be longer than 360 days
  * If `startTime` and `endTime` not sent, return records of the last 30 days by default.
  * If `startTime`is sent and `endTime` is not sent, return records of [startTime, startTime+30d].
  * If `startTime` is not sent and `endTime` is sent, return records of [endTime-30d, endTime].



## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#response-example "Direct link to Response Example")
    
    
    {  
      "total": 3,  
      "rows": [  
        {  
          "asset": "USDT",  
          "amount": "404.80294503",  
          "repayTime": 1731336427804  
        },  
        {  
          "asset": "USDT",  
          "amount": "4620.41204574",  
          "repayTime": 1726125090016  
        }  
      ]  
    }

---

# 查询经典统一账户专业版穿仓借贷偿还历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#接口描述 "接口描述的直接链接")

查询统一账户专业版穿仓借贷偿还历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/pmloan-history`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#请求权重ip "请求权重\(IP\)的直接链接")

**500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
size| LONG| NO| 返回的结果集数量 默认值:10 最大值:100  
current| LONG| NO| 默认值：1  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * `startTime` 和 `endTime` 间隔不能超过 360天
  * 如果 `startTime` 和 `endTime` 没有传, 默认返回最近30天的记录
  * 如果传了 `startTime` 但没有传 `endTime`, 返回记录 [startTime, startTime+30d].
  * 如果没传 `startTime` 但传了`endTime`, 返回记录[endTime-30d, endTime].



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#响应示例 "响应示例的直接链接")
    
    
    {  
      "total": 3,  
      "rows": [  
        {  
          "asset": "USDT",  
          "amount": "404.80294503",  
          "repayTime": 1731336427804  
        },  
        {  
          "asset": "USDT",  
          "amount": "4620.41204574",  
          "repayTime": 1726125090016  
        }  
      ]  
    }