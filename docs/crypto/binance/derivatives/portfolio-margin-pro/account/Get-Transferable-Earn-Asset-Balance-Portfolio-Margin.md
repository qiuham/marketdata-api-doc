---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin
api_type: Account
updated_at: 2026-01-15T23:44:12.808312
---

# Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#api-description "Direct link to API Description")

Get transferable earn asset balance for all types of Portfolio Margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/earn-asset-balance`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-weightip "Direct link to Request Weight\(IP\)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES| `LDUSDT` only  
transferType| STRING| YES| `EARN_TO_FUTURE` /`FUTURE_TO_EARN`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#response-example "Direct link to Response Example")
    
    
    {  
        "asset": "LDUSDT",  
        "amount": "0.55"  
    }

---

# 查询统一账户LDUSDT可转金额(TRADE)

# Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA)

## API Description[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#api-description "API Description的直接链接")

Get transferable earn asset balance for all types of Portfolio Margin account

## HTTP Request[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#http-request "HTTP Request的直接链接")

GET `/sapi/v1/portfolio/earn-asset-balance`

## Request Weight(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-weightip "Request Weight\(IP\)的直接链接")

**1500**

## Request Parameters[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES| `LDUSDT` only  
transferType| STRING| YES| `EARN_TO_FUTURE` /`FUTURE_TO_EARN`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#response-example "Response Example的直接链接")
    
    
    {  
        "asset": "LDUSDT",  
        "amount": "0.55"  
    }