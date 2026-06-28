---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account
api_type: Account
updated_at: 2026-01-15T23:44:31.859230
---

# Account Balance(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account#api-description "Direct link to API Description")

Query account balance

## HTTP Request[​](/docs/derivatives/portfolio-margin/account#http-request "Direct link to HTTP Request")

GET `/papi/v1/balance`

## Request Weight[​](/docs/derivatives/portfolio-margin/account#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "USDT",    // asset name  
            "totalWalletBalance": "122607.35137903", // wallet balance =  cross margin free + cross margin locked + UM wallet balance + CM wallet balance  
            "crossMarginAsset": "92.27530794", // crossMarginAsset = crossMarginFree + crossMarginLocked  
            "crossMarginBorrowed": "10.00000000", // principal of cross margin  
            "crossMarginFree": "100.00000000", // free asset of cross margin  
            "crossMarginInterest": "0.72469206", // interest of cross margin  
            "crossMarginLocked": "3.00000000", //lock asset of cross margin  
            "umWalletBalance": "0.00000000",  // wallet balance of um  
            "umUnrealizedPNL": "23.72469206",     // unrealized profit of um   
            "cmWalletBalance": "23.72469206",       // wallet balance of cm  
            "cmUnrealizedPNL": "",    // unrealized profit of cm  
            "updateTime": 1617939110373,  
            "negativeBalance": "0"  
        }  
    ]  
    

**OR (when asset sent)**
    
    
    {  
        "asset": "USDT",    // asset name  
        "totalWalletBalance": "122607.35137903", // wallet balance =  cross margin free + cross margin locked + UM wallet balance + CM wallet balance  
        "crossMarginBorrowed": "10.00000000", // principal of cross margin  
        "crossMarginFree": "100.00000000", // free asset of cross margin  
        "crossMarginInterest": "0.72469206", // interest of cross margin  
        "crossMarginLocked": "3.00000000", //lock asset of cross margin  
        "umWalletBalance": "0.00000000",  // wallet balance of um  
        "umUnrealizedPNL": "23.72469206",     // unrealized profit of um   
        "cmWalletBalance": "23.72469206",       // wallet balance of cm  
        "cmUnrealizedPNL": "",    // unrealized profit of cm  
        "updateTime": 1617939110373,  
        "negativeBalance": "0"  
    }  
    ```

---

# 查询账户余额(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account#接口描述 "接口描述的直接链接")

查询账户余额

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account#http请求 "HTTP请求的直接链接")

GET `/papi/v1/balance`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account#响应示例 "响应示例的直接链接")
    
    
      
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
            "negativeBalance": "0"  
        }  
    ]  
    

**或 (发送asset)**
    
    
    {  
        "asset": "USDT",      
        "totalWalletBalance": "122607.35137903",   
        "crossMarginBorrowed": "10.00000000",   
        "crossMarginFree": "100.00000000",   
        "crossMarginInterest": "0.72469206",   
        "crossMarginLocked": "3.00000000",  
        "umWalletBalance": "0.00000000",    
        "umUnrealizedPNL": "23.72469206",       
        "cmWalletBalance": "23.72469206",        
        "cmUnrealizedPNL": "",     
        "updateTime": 1617939110373,  
        "negativeBalance": "0"  
    }