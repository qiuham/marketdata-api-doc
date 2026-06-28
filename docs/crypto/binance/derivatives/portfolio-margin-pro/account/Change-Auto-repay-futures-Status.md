---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status
api_type: Account
updated_at: 2026-01-15T23:43:58.694679
---

# Change Auto-repay-futures Status(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#api-description "Direct link to API Description")

Change Auto-repay-futures Status

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/repay-futures-switch`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#request-weightip "Direct link to Request Weight\(IP\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
autoRepay| STRING| YES| Default: `true`; `false` for turn off the auto-repay futures negative balance function  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#response-example "Direct link to Response Example")
    
    
    {  
        "msg": "success"  
    }

---

# 更改自动清还合约负余额模式(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#接口描述 "接口描述的直接链接")

更改自动支付合约负余额模式

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/repay-futures-switch `

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#请求权重ip "请求权重\(IP\)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
autoRepay| STRING| YES| 默认为`true`; `false`代表关闭自动清还合约负余额  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Change-Auto-repay-futures-Status#响应示例 "响应示例的直接链接")
    
    
    {  
        "msg": "success"  
    }