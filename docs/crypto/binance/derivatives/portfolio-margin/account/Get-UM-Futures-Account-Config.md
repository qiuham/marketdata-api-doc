---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config
api_type: Account
updated_at: 2026-01-15T23:44:58.734947
---

# UM Futures Account Configuration(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#api-description "Direct link to API Description")

Query UM Futures account configuration

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/accountConfig`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#response-example "Direct link to Response Example")
    
    
    {     
        "feeTier": 0,               // account commission tier   
        "canTrade": true,           // if can trade  
        "canDeposit": true,         // if can transfer in asset  
        "canWithdraw": true,        // if can transfer out asset  
        "dualSidePosition": true,  
        "updateTime": 1724416653850,            // reserved property, please ignore   
        "multiAssetsMargin": false,  
        "tradeGroupId": -1  
    }

---

# 账户配置(USER_DATA)

查询UM账户配置

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/accountConfig`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#响应示例 "响应示例的直接链接")
    
    
    {     
        "feeTier": 0,               // 费率等级  
        "canTrade": true,           // 是否可以交易  
        "canDeposit": true,         // 是否可以存款  
        "canWithdraw": true,        // 是否可以提现  
        "dualSidePosition": true,  
        "updateTime": 1724416653850,            // 忽略  
        "multiAssetsMargin": false,  
        "tradeGroupId": -1  
    }