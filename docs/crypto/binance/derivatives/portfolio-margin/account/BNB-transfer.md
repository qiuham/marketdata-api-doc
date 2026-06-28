---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/BNB-transfer
api_type: Account
updated_at: 2026-01-15T23:44:31.984506
---

# BNB transfer (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#api-description "Direct link to API Description")

Transfer BNB in and out of UM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#http-request "Direct link to HTTP Request")

POST `/papi/v1/bnb-transfer`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#request-weightip "Direct link to Request Weight\(IP\)")

**750**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
amount| DECIMAL| YES|   
transferSide| STRING| YES| "TO_UM","FROM_UM"  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * The endpoint can only be called 10 times per 10 minutes in a rolling manner
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#response-example "Direct link to Response Example")
    
    
    {  
        "tranId": 100000001       //transaction id  
    }

---

# BNB划转(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/BNB-transfer#接口描述 "接口描述的直接链接")

从PM钱包划转BNB到UM钱包

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/BNB-transfer#http请求 "HTTP请求的直接链接")

POST `/papi/v1/bnb-transfer`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin/account/BNB-transfer#请求权重ip "请求权重\(IP\)的直接链接")

**750**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/BNB-transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
amount| DECIMAL| YES|   
transferSide| STRING| YES| "TO_UM","FROM_UM"  
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
>   * 本接口每10分钟只能调用10次（时间滚动计算）
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/BNB-transfer#响应示例 "响应示例的直接链接")
    
    
    {  
        //transaction id  
        "tranId": 100000001  
    }