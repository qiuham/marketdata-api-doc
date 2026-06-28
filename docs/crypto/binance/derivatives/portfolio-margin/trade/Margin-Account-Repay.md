---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay
api_type: Trading
updated_at: 2026-01-15T23:45:29.249466
---

# Margin Account Repay(MARGIN)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#api-description "Direct link to API Description")

Repay for a margin loan.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#http-request "Direct link to HTTP Request")

POST `/papi/v1/repayLoan`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#request-weight "Direct link to Request Weight")

**100**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#response-example "Direct link to Response Example")
    
    
    {  
        //transaction id  
        "tranId": 100000001  
    }

---

# 杠杆账户归还借贷(MARGIN)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay#接口描述 "接口描述的直接链接")

获取杠杆账户归还借贷

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay#http请求 "HTTP请求的直接链接")

POST `/papi/v1/repayLoan`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay#请求权重 "请求权重的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO| 赋值不能超过`60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay#响应示例 "响应示例的直接链接")
    
    
    {  
        "tranId": 100000001     //transaction id  
    }