---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Fund-Auto-collection
api_type: Account
updated_at: 2026-01-15T23:44:46.442778
---

# Fund Auto-collection(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/Fund-Auto-collection#api-description "Direct link to API Description")

Fund collection for Portfolio Margin

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Fund-Auto-collection#http-request "Direct link to HTTP Request")

`POST /papi/v1/auto-collection`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/account/Fund-Auto-collection#request-weightip "Direct link to Request Weight\(IP\)")

**750**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Fund-Auto-collection#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * The BNB would not be collected from UM-PM account to the Portfolio Margin account.
>   * You can only use this function 500 times per hour in a rolling manner.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Fund-Auto-collection#response-example "Direct link to Response Example")
    
    
    {  
        "msg": "success"  
    }

---

# 统一账户资金归集(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#接口描述 "接口描述的直接链接")

资金归集到统一账户钱包

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#http请求 "HTTP请求的直接链接")

POST `/papi/v1/auto-collection`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#请求权重 "请求权重的直接链接")

**750**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
>   * BNB资产不会归集
>   * 滚动每小时仅能调用500次
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#响应示例 "响应示例的直接链接")
    
    
    {  
        "msg": "success"  
    }