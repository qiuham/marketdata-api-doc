---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status
api_type: Account
updated_at: 2026-01-15T23:44:46.589936
---

# Get Auto-repay-futures Status(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#api-description "Direct link to API Description")

Query Auto-repay-futures Status

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#http-request "Direct link to HTTP Request")

GET `/papi/v1/repay-futures-switch`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#request-weightip "Direct link to Request Weight\(IP\)")

**30**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#response-example "Direct link to Response Example")
    
    
    {  
        "autoRepay": true  //  "true" for turn on the auto-repay futures; "false" for turn off the auto-repay futures   
    }

---

# 查询自动清还合约负余额模式(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#接口描述 "接口描述的直接链接")

查询自动清还合约负余额模式

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#http请求 "HTTP请求的直接链接")

GET `/papi/v1/repay-futures-switch`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#请求权重ip "请求权重\(IP\)的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#响应示例 "响应示例的直接链接")
    
    
    {  
        "autoRepay": true  //  `true`代表自动清还合约负余额; `false`代表关闭自动清还合约负余额  
    }