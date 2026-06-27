---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow
api_type: Account
updated_at: 2026-01-15T23:45:06.354382
---

# Margin Max Borrow(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#api-description "Direct link to API Description")

Query margin max borrow

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/maxBorrowable`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#response-example "Direct link to Response Example")
    
    
    {  
      "amount": "1.69248805", // account's currently max borrowable amount with sufficient system availability  
      "borrowLimit": "60" // max borrowable amount limited by the account level  
    }

---

# 查询账户最大可借贷额度 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#接口描述 "接口描述的直接链接")

查询账户最大可借贷额度

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/maxBorrowable`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO| 赋值不能超过 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#响应示例 "响应示例的直接链接")
    
    
    {  
      "amount": "1.69248805", // 系统可借充足情况下用户账户当前最大可借额度  
      "borrowLimit": "60" // 平台限制的用户当前等级可以借的额度  
    }