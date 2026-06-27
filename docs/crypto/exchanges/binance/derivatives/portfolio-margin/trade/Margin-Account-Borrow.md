---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow
api_type: Trading
updated_at: 2026-01-15T23:45:29.082130
---

# Margin Account Borrow(MARGIN)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#api-description "Direct link to API Description")

Apply for a margin loan.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#http-request "Direct link to HTTP Request")

POST `/papi/v1/marginLoan`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#request-weightip "Direct link to Request Weight\(IP\)")

**100**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#response-example "Direct link to Response Example")
    
    
    {  
        //transaction id  
        "tranId": 100000001  
    }

---

# 杠杆账户借贷(MARGIN)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#接口描述 "接口描述的直接链接")

申请借贷

## HTTP Request[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#http-request "HTTP Request的直接链接")

POST `/papi/v1/marginLoan`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#请求权重 "请求权重的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO| 赋值不能超过`60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#响应示例 "响应示例的直接链接")
    
    
    {  
        "tranId": 100000001 //transaction id  
    }