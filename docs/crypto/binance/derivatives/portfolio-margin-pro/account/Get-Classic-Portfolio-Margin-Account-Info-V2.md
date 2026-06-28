---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2
api_type: Account
updated_at: 2026-01-15T23:44:05.267259
---

# Get Portfolio Margin Pro SPAN Account Info(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#api-description "Direct link to API Description")

Get Portfolio Margin Pro SPAN Account Info (For Portfolio Margin Pro SPAN users only)

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#http-request "Direct link to HTTP Request")

GET `/sapi/v2/portfolio/account`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#request-weightip "Direct link to Request Weight\(IP\)")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#response-example "Direct link to Response Example")
    
    
    {  
            "uniMMR": "5167.92171923",          
            "accountEquity": "122607.35137903",  // Account equity, unit：USD  
            "actualEquity": "142607.35137903",   // Actual equity, unit：USD  
            "accountMaintMargin": "23.72469206", //Account maintenance margin, unit：USD  
            "riskUnitMMList":[  
                 {  
                     "asset": "BTC",  
                     "uniMaintainUsd": "23.72469206"  
                 }  
            ]  
            "marginMM": "0.00000000",   
            "otherMM": "0.00000000",   
            "accountStatus": "NORMAL",   // Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
            "accountType": "PM_3"     //PM_1 for classic PM, PM_2 for PM, PM_3 for PM Pro(SPAN)   
    }

---

# 查询统一账户专业版SPAN账户信息(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#接口描述 "接口描述的直接链接")

查询统一账户专业版SPAN账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/portfolio/account`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#请求权重ip "请求权重\(IP\)的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#响应示例 "响应示例的直接链接")
    
    
    {  
            "uniMMR": "5167.92171923",          
            "accountEquity": "122607.35137903",  // Account equity, unit：USD  
            "actualEquity": "142607.35137903",   // Actual equity, unit：USD  
            "accountMaintMargin": "23.72469206", //Account maintenance margin, unit：USD  
            "riskUnitMMList":[  
                 {  
                     "asset": "BTC",  
                     "uniMaintainUsd": "23.72469206"  
                 }  
            ]  
            "marginMM": "0.00000000",   
            "otherMM": "0.00000000",   
            "accountStatus": "NORMAL",   // Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
            "accountType": "PM_3"     //PM_1 for classic PM, PM_2 for PM, PM_3 for PM Pro(SPAN)   
    }