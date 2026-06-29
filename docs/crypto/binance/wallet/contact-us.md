---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/contact-us
api_type: REST
updated_at: 2026-06-29 19:12:09.109089
---

# Get symbols delist schedule for spot (MARKET_DATA)

## API Description[​](/docs/wallet/others/delist-schedule#api-description "Direct link to API Description")

Get symbols delist schedule for spot

## HTTP Request[​](/docs/wallet/others/delist-schedule#http-request "Direct link to HTTP Request")

GET `/sapi/v1/spot/delist-schedule`

## Request Weight(IP)[​](/docs/wallet/others/delist-schedule#request-weightip "Direct link to Request Weight\(IP\)")

**100**

## Request Parameters[​](/docs/wallet/others/delist-schedule#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/others/delist-schedule#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "delistTime": 1686161202000,  
            "symbols": ["ADAUSDT", "BNBUSDT"]  
        },  
        {  
            "delistTime": 1686222232000,  
            "symbols": ["ETHUSDT"]  
        }  
    ]

---

# 查询现货币对的下架计划

## 接口描述[​](/docs/zh-CN/wallet/others/delist-schedule#接口描述 "接口描述的直接链接")

查询现货币对的下架计划

## HTTP请求[​](/docs/zh-CN/wallet/others/delist-schedule#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/spot/delist-schedule`

## 请求权重(IP)[​](/docs/zh-CN/wallet/others/delist-schedule#请求权重ip "请求权重\(IP\)的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/wallet/others/delist-schedule#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/others/delist-schedule#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "delistTime": 1686161202000,  
            "symbols": ["ADAUSDT", "BNBUSDT"]  
        },  
        {  
            "delistTime": 1686222232000,  
            "symbols": ["ETHUSDT"]  
        }  
    ]