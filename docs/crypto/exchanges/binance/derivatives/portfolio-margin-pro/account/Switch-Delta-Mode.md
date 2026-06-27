---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode
api_type: Account
updated_at: 2026-01-15T23:44:20.376945
---

# Switch Delta Mode(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#api-description "Direct link to API Description")

Switch the Delta mode for existing PM PRO / PM RETAIL accounts.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/delta-mode`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#request-weightip "Direct link to Request Weight\(IP\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
deltaEnabled| STRING| YES| `true` to enable Delta mode; `false` to disable Delta mode  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#response-example "Direct link to Response Example")
    
    
    {  
        "msg": "success"  
    }

---

# 切换账户Delta模式(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#接口描述 "接口描述的直接链接")

切换当前 PM PRO / PM RETAIL账户Delta 模式

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/delta-mode `

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#请求权重ip "请求权重\(IP\)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
deltaEnabled| STRING| YES| `true`为开启Delta模式; `false`代表关闭Delta模式  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#响应示例 "响应示例的直接链接")
    
    
    {  
        "msg": "success"  
    }