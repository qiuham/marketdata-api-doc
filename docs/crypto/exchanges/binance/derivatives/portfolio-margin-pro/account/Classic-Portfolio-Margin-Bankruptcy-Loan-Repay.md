---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay
api_type: Account
updated_at: 2026-01-15T23:43:58.756890
---

# Portfolio Margin Pro Bankruptcy Loan Repay

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#api-description "Direct link to API Description")

Repay Portfolio Margin Pro Bankruptcy Loan

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/repay`

## Request Weight(UID)[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
from| STRING| NO| SPOT or MARGIN，default SPOT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * Please note that the API Key has enabled Spot & Margin Trading permissions to access this endpoint.



## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#response-example "Direct link to Response Example")
    
    
    {  
        "tranId": 58203331886213504  
    }

---

# 偿还统一账户专业版穿仓负债

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#接口描述 "接口描述的直接链接")

偿还统一账户专业版穿仓负债

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/repay`

## 请求权重(UID)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
from| STRING| NO| SPOT或MARGIN，默认SPOT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#响应示例 "响应示例的直接链接")
    
    
    {  
        "tranId": 58203331886213504  
    }