---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount
api_type: Account
updated_at: 2026-01-15T23:44:12.882107
---

# Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#api-description "Direct link to API Description")

Query Portfolio Margin Pro Bankruptcy Loan Amount

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/pmLoan`

## Request Weight(UID)[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#request-weightuid "Direct link to Request Weight\(UID\)")

**500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If there’s no classic portfolio margin bankruptcy loan, the amount would be 0
> 


## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#response-example "Direct link to Response Example")
    
    
    {  
       "asset": "BUSD",     
       "amount":  "579.45", // portfolio margin bankruptcy loan amount in BUSD  
    }

---

# 查询统一账户专业版穿仓借贷金额 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#接口描述 "接口描述的直接链接")

查询统一账户专业版穿仓借贷金额

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/pmLoan`

## 请求权重(UID)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#请求权重uid "请求权重\(UID\)的直接链接")

**500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果不存在统一账户专业版穿仓负债，amount显示为0
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#响应示例 "响应示例的直接链接")
    
    
    {  
       "asset": "BUSD",     
       "amount":  "579.45", // 统一账户用户强平穿仓负债，单位为BUSD  
    }