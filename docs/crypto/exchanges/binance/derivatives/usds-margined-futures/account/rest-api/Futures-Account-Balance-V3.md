---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3
api_type: Account
updated_at: 2026-01-15T23:46:14.246909
---

# Futures Account Balance V3 (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#api-description "Direct link to API Description")

Query account balance info

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#http-request "Direct link to HTTP Request")

GET `/fapi/v3/balance`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#response-example "Direct link to Response Example")
    
    
    [  
     {  
       "accountAlias": "SgsR",              // unique account code  
       "asset": "USDT",  	                // asset name  
       "balance": "122607.35137903",        // wallet balance  
       "crossWalletBalance": "23.72469206", // crossed wallet balance  
       "crossUnPnl": "0.00000000",           // unrealized profit of crossed positions  
       "availableBalance": "23.72469206",   // available balance  
       "maxWithdrawAmount": "23.72469206",  // maximum amount for transfer out  
       "marginAvailable": true,             // whether the asset can be used as margin in Multi-Assets mode  
       "updateTime": 1617939110373  
     }  
    ]

---

# 账户余额V3 (USER_DATA)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#http请求 "HTTP请求的直接链接")

GET `/fapi/v3/balance`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3#响应示例 "响应示例的直接链接")
    
    
    [  
     {  
       "accountAlias": "SgsR",              // 账户唯一识别码  
       "asset": "USDT",  	                // 资产  
       "balance": "122607.35137903",        // 总余额  
       "crossWalletBalance": "23.72469206", // 全仓余额  
       "crossUnPnl": "0.00000000",           // 全仓持仓未实现盈亏  
       "availableBalance": "23.72469206",   // 下单可用余额  
       "maxWithdrawAmount": "23.72469206",  // 最大可转出余额  
       "marginAvailable": true,            // 是否可用作联合保证金  
       "updateTime": 1617939110373  
     }  
    ]