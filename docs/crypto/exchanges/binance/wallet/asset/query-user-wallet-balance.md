---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/query-user-wallet-balance
api_type: REST
updated_at: 2026-05-27 18:59:19.528017
---

# Trade Fee (USER_DATA)

## API Description[​](/docs/wallet/asset/trade-fee#api-description "Direct link to API Description")

Fetch trade fee

## HTTP Request[​](/docs/wallet/asset/trade-fee#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/tradeFee`

## Request Weight(IP)[​](/docs/wallet/asset/trade-fee#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset/trade-fee#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/asset/trade-fee#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "ADABNB",  
            "makerCommission": "0.001",  
            "takerCommission": "0.001"  
        },  
        {  
            "symbol": "BNBBTC",  
            "makerCommission": "0.001",  
            "takerCommission": "0.001"  
        }  
    ]

---

# 交易手续费率查询(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/trade-fee#接口描述 "接口描述的直接链接")

交易手续费率查询

## HTTP请求[​](/docs/zh-CN/wallet/asset/trade-fee#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/tradeFee `

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/trade-fee#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset/trade-fee#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/trade-fee#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "ADABNB",  
            "makerCommission": "0.001",  
            "takerCommission": "0.001"  
        },  
        {  
            "symbol": "BNBBTC",  
            "makerCommission": "0.001",  
            "takerCommission": "0.001"  
        }  
    ]