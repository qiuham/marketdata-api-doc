---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin
api_type: Account
updated_at: 2026-01-15T23:44:20.437841
---

# Transfer LDUSDT/RWUSD for Portfolio Margin(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#api-description "Direct link to API Description")

Transfer LDUSDT/RWUSD as collateral for all types of Portfolio Margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/earn-asset-transfer`

## Request Weight(UID)[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#request-weightuid "Direct link to Request Weight\(UID\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES| `LDUSDT` and `RWUSD`  
transferType| STRING| YES| `EARN_TO_FUTURE` /`FUTURE_TO_EARN`  
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#response-example "Direct link to Response Example")
    
    
    {  
      "msg":"success"  
    }

---

# 统一账户转入LDUSDT/RWUSD资产(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#接口描述 "接口描述的直接链接")

LDUSDT/RWUSD转入，支持所有的统一账户类型

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/earn-asset-transfer`

## 请求权重(UID)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#请求权重uid "请求权重\(UID\)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES| 支持`LDUSDT` 和 `RWUSD`  
transferType| STRING| YES| `EARN_TO_FUTURE` /`FUTURE_TO_EARN`  
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#响应示例 "响应示例的直接链接")
    
    
    {  
      "msg":"success"  
    }