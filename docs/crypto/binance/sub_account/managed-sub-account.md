---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account
api_type: Account
updated_at: 2026-06-30 19:12:30.703627
---

# Deposit Assets Into The Managed Sub-account (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account#api-description "Direct link to API Description")

Deposit Assets Into The Managed Sub-account

## HTTP Request[​](/docs/sub_account/managed-sub-account#http-request "Direct link to HTTP Request")

POST `/sapi/v1/managed-subaccount/deposit`

## Request Weight(IP)[​](/docs/sub_account/managed-sub-account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/managed-sub-account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
toEmail| STRING| YES|   
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to enable `Enable Spot & Margin Trading` option for the api key which requests this endpoint
> 


## Response Example[​](/docs/sub_account/managed-sub-account#response-example "Direct link to Response Example")
    
    
    {  
       "tranId":66157362489  
    }

---

# 投资人账户为托管子账户充值资产 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account#接口描述 "接口描述的直接链接")

投资人账户为托管子账户充值资产(适用投资人母账户)

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/managed-subaccount/deposit`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/managed-sub-account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
toEmail| STRING| YES|   
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您需要开通API Key`允许现货和杠杆交易`权限
> 


## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account#响应示例 "响应示例的直接链接")
    
    
    {  
        "tranId":66157362489  
    }