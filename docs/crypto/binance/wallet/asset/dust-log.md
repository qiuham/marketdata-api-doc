---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/dust-log
api_type: REST
updated_at: 2026-05-27 18:59:09.960616
---

# Funding Wallet (USER_DATA)

## API Description[​](/docs/wallet/asset/funding-wallet#api-description "Direct link to API Description")

Query Funding Wallet

## HTTP Request[​](/docs/wallet/asset/funding-wallet#http-request "Direct link to HTTP Request")

POST `/sapi/v1/asset/get-funding-asset`

## Request Weight(IP)[​](/docs/wallet/asset/funding-wallet#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset/funding-wallet#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
needBtcValuation| STRING| NO| true or false  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card, Stock Token
> 


## Response Example[​](/docs/wallet/asset/funding-wallet#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "USDT",  
            "free": "1",                     // avalible balance  
            "locked": "0",                   // locked asset  
            "freeze": "0",                   // freeze asset  
            "withdrawing": "0",  
            "btcValuation": "0.00000091"  
        }  
    ]

---

# 查询资金账户(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/funding-wallet#接口描述 "接口描述的直接链接")

查询资金账户(USER_DATA)

## HTTP请求[​](/docs/zh-CN/wallet/asset/funding-wallet#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/asset/get-funding-asset`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/funding-wallet#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset/funding-wallet#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
needBtcValuation| STRING| NO| true or false  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 目前仅支持查询以下业务资产：Binance Pay, Binance Card, Binance Gift Card, Stock Token
> 


## 响应示例[​](/docs/zh-CN/wallet/asset/funding-wallet#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "USDT",  
            "free": "1",                     // 可用余额  
            "locked": "0",                   // 锁定资金  
            "freeze": "0",                   // 冻结资金  
            "withdrawing": "0",              // 提币  
            "btcValuation": "0.00000091"     // btc估值  
        }  
    ]