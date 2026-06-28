---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/fetch-withdraw-address
api_type: REST
updated_at: 2026-05-27 18:59:32.788600
---

# One click arrival deposit apply (for expired address deposit) (USER_DATA)

## API Description[​](/docs/wallet/capital/one-click-arrival-deposite-apply#api-description "Direct link to API Description")

Apply deposit credit for expired address (One click arrival)

## HTTP Request[​](/docs/wallet/capital/one-click-arrival-deposite-apply#http-request "Direct link to HTTP Request")

POST `/sapi/v1/capital/deposit/credit-apply`

## Request Weight(IP)[​](/docs/wallet/capital/one-click-arrival-deposite-apply#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/capital/one-click-arrival-deposite-apply#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
depositId| LONG| NO| Deposit record Id, priority use  
txId| STRING| NO| Deposit txId, used when depositId is not specified  
subAccountId| LONG| NO| Sub-accountId of Cloud user  
subUserId| LONG| NO| Sub-userId of parent user  
  
>   * Params need to be in the POST body
> 


## Response Example[​](/docs/wallet/capital/one-click-arrival-deposite-apply#response-example "Direct link to Response Example")
    
    
    {  
        "code": "000000",  
        "message": "success",  
        "data": true,  
        "success": true  
    }

---

# 一键上账(充值到过期地址)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/capital/one-click-arrival-deposite-apply#接口描述 "接口描述的直接链接")

申请充值到过期地址的一键上账.

## HTTP请求[​](/docs/zh-CN/wallet/capital/one-click-arrival-deposite-apply#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/capital/deposit/credit-apply`

## 请求权重(IP)[​](/docs/zh-CN/wallet/capital/one-click-arrival-deposite-apply#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/capital/one-click-arrival-deposite-apply#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
depositId| LONG| NO| 充值记录Id，优先使用  
txId| STRING| NO| 充值txId，当depositId没指定时使用  
subAccountId| LONG| NO| Cloud的子账户ID  
subUserId| LONG| NO| 母账户的子账户userId  
  
>   * 参数应在POST BODY
> 


## 响应示例[​](/docs/zh-CN/wallet/capital/one-click-arrival-deposite-apply#响应示例 "响应示例的直接链接")
    
    
    {  
        "code": "000000",  
        "message": "success",  
        "data": true,  
        "success": true  
    }