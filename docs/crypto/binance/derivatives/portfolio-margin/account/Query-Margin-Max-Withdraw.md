---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw
api_type: Account
updated_at: 2026-01-15T23:45:10.778030
---

# Query Margin Max Withdraw(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#api-description "Direct link to API Description")

Query Margin Max Withdraw

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/maxWithdraw`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#response-example "Direct link to Response Example")
    
    
    {   
      "amount": "60"  
    }

---

# 查询账户最大可转出额度(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#接口描述 "接口描述的直接链接")

查询账户最大可转出额度

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/maxWithdraw`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
recvWindow| LONG| NO| 赋值不能超过 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#响应示例 "响应示例的直接链接")
    
    
    {   
      "amount": "60"   
    }