---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status
api_type: Account
updated_at: 2026-01-15T23:44:12.742649
---

# Get Delta Mode Status(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#api-description "Direct link to API Description")

Query the Delta mode status of current account.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/delta-mode`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#request-weightip "Direct link to Request Weight\(IP\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#response-example "Direct link to Response Example")
    
    
    {  
        "deltaEnabled": false  
    }

---

# 查询账户Delta模式状态 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#接口描述 "接口描述的直接链接")

查询账户Delta模式状态

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/delta-mode`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#请求权重ip "请求权重\(IP\)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#响应示例 "响应示例的直接链接")
    
    
    {  
        "deltaEnabled": false  
    }