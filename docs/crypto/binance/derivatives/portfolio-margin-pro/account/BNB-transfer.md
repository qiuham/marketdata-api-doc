---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/BNB-transfer
api_type: Account
updated_at: 2026-01-15T23:43:58.630435
---

# BNB transfer(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#api-description "Direct link to API Description")

BNB transfer can be between Margin Account and USDM Account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/bnb-transfer`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#request-weightip "Direct link to Request Weight\(IP\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
amount| DECIMAL| YES|   
transferSide| STRING| YES| "TO_UM","FROM_UM"  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You can only use this function 2 times per 10 minutes in a rolling manner
> 


## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#response-example "Direct link to Response Example")
    
    
    {  
         "tranId": 100000001  
    }

---

# BNB划转(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#接口描述 "接口描述的直接链接")

BNB在杠杆账户和USD-M期货账户划转

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/bnb-transfer`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#请求权重ip "请求权重\(IP\)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
amount| DECIMAL| YES|   
transferSide| STRING| YES| "TO_UM","FROM_UM"  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 本接口每10分钟仅可以调用2次
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#响应示例 "响应示例的直接链接")
    
    
    {  
         "tranId": 100000001  
    }