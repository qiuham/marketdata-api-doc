---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection
api_type: Account
updated_at: 2026-01-15T23:44:05.077377
---

# Fund Auto-collection(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#api-description "Direct link to API Description")

Transfers all assets from Futures Account to Margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/auto-collection`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#request-weightip "Direct link to Request Weight\(IP\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * The BNB would not be collected from UM-PM account to the Portfolio Margin account.
>   * You can only use this function 500 times per hour in a rolling manner.
> 


## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#response-example "Direct link to Response Example")
    
    
    {  
        "msg": "success"  
    }

---

# 资金归集(USER_DATA)

账户资金归集，将除BNB外资产从合约账户划转到杠杆账户

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/auto-collection`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#请求权重ip "请求权重\(IP\)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 本接口不会划转BNB资产
>   * 本接口每小时仅能被调用500次（滚动计算）
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Auto-collection#响应示例 "响应示例的直接链接")
    
    
    {  
        "msg": "success"  
    }