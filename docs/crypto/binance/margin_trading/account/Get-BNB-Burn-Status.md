---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Get-BNB-Burn-Status
api_type: Account
updated_at: 2026-06-29 19:09:07.122535
---

# Get BNB Burn Status (USER_DATA)

## API Description[​](/docs/margin_trading/account/Get-BNB-Burn-Status#api-description "Direct link to API Description")

Get BNB Burn Status

## HTTP Request[​](/docs/margin_trading/account/Get-BNB-Burn-Status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/bnbBurn`

## Request Weight[​](/docs/margin_trading/account/Get-BNB-Burn-Status#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/account/Get-BNB-Burn-Status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Get-BNB-Burn-Status#response-example "Direct link to Response Example")
    
    
    {  
       "spotBNBBurn":true,  
       "interestBNBBurn": false     
    }

---

# 获取BNB抵扣开关状态 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Get-BNB-Burn-Status#接口描述 "接口描述的直接链接")

获取BNB抵扣开关状态

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Get-BNB-Burn-Status#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/bnbBurn`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Get-BNB-Burn-Status#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Get-BNB-Burn-Status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Get-BNB-Burn-Status#响应示例 "响应示例的直接链接")
    
    
    {  
       "spotBNBBurn":true,  
       "interestBNBBurn": false     
    }