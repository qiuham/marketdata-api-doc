---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info
api_type: Account
updated_at: 2026-01-15T23:44:05.330549
---

# Get Portfolio Margin Pro Account Balance(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#api-description "Direct link to API Description")

Query Portfolio Margin Pro account balance

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/balance`

## Request Weight[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#response-example "Direct link to Response Example")
    
    
      
    [  
        {  
            "asset": "BTC",    // asset name  
            "totalWalletBalance": "100",    // wallet balance =  cross margin free + cross margin locked + UM wallet balance + CM wallet balance  
            "crossMarginAsset": "100",    // crossMarginAsset = crossMarginFree + crossMarginLocked  
            "crossMarginBorrowed": "0",    // principal of cross margin  
            "crossMarginFree": "100",    // free asset of cross margin  
            "crossMarginInterest": "0",    // interest of cross margin  
            "crossMarginLocked": "0",  //lock asset of cross margin  
            "umWalletBalance": "0",    // wallet balance of um  
            "umUnrealizedPNL": "0",     // unrealized profit of um   
            "cmWalletBalance": "0",    // wallet balance of cm  
            "cmUnrealizedPNL": "0",    // unrealized profit of cm  
            "updateTime": 0,  
            "negativeBalance": "0",  
            "optionWalletBalance": "0",  //only for PM PRO SPAN  
            "optionEquity": "0"  //only for PM PRO SPAN  
        }  
    ]

---

# 查询统一账户专业版账户余额(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#接口描述 "接口描述的直接链接")

查询统一账户专业版账户余额

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/balance`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info#响应示例 "响应示例的直接链接")
    
    
      
    [  
        {  
            "asset": "USDT",    // 资产  
            "totalWalletBalance": "122607.35137903", // 钱包余额 =  全仓杠杆未锁定 + 全仓杠杆锁定 + u本位合约钱包余额 + 币本位合约钱包余额  
            "crossMarginAsset": "92.27530794", // 全仓资产 = 全仓杠杆未锁定 + 全仓杠杆锁定  
            "crossMarginBorrowed": "10.00000000", // 全仓杠杆借贷  
            "crossMarginFree": "100.00000000", // 全仓杠杆未锁定  
            "crossMarginInterest": "0.72469206", // 全仓杠杆利息  
            "crossMarginLocked": "3.00000000", //全仓杠杆锁定   
            "umWalletBalance": "0.00000000",  // u本位合约钱包余额  
            "umUnrealizedPNL": "23.72469206",     // u本位未实现盈亏  
            "cmWalletBalance": "23.72469206",       // 币本位合约钱包余额  
            "cmUnrealizedPNL": "",    // 币本位未实现盈亏  
            "updateTime": 1617939110373,  
            "negativeBalance": "0",  
            "optionWalletBalance": "0",  //仅适用于PM PRO SPAN  
            "optionEquity": "0"  //仅适用于PM PRO SPAN  
        }  
    ]