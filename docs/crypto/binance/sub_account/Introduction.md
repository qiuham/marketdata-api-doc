---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/Introduction
api_type: Account
updated_at: 2026-05-27 19:01:53.925922
---

# Enable Futures for Sub-account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management/Enable-Futures-for-Sub-account#api-description "Direct link to API Description")

Enable Futures for Sub-account for Master Account

## HTTP Request[​](/docs/sub_account/account-management/Enable-Futures-for-Sub-account#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/futures/enable`

## Request Weight(IP)[​](/docs/sub_account/account-management/Enable-Futures-for-Sub-account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/account-management/Enable-Futures-for-Sub-account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/account-management/Enable-Futures-for-Sub-account#email-address)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/account-management/Enable-Futures-for-Sub-account#response-example "Direct link to Response Example")
    
    
    {  
      
        "email":"123@test.com",  
        "isFuturesEnabled": true  // true or false  
      
    }

---

# 为子账户开通Futures (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management/Enable-Futures-for-Sub-account#接口描述 "接口描述的直接链接")

为子账户开通Futures(适用主账户)

## HTTP请求[​](/docs/zh-CN/sub_account/account-management/Enable-Futures-for-Sub-account#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/futures/enable`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/account-management/Enable-Futures-for-Sub-account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/account-management/Enable-Futures-for-Sub-account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/account-management/Enable-Futures-for-Sub-account#request-email-address)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/account-management/Enable-Futures-for-Sub-account#响应示例 "响应示例的直接链接")
    
    
    {  
      
        "email":"123@test.com",  
        "isFuturesEnabled": true  // true or false  
      
    }