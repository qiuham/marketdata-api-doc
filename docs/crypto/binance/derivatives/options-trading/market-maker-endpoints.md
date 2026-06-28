---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-endpoints
api_type: Market Data
updated_at: 2026-01-15T23:41:52.413045
---

# Get Market Maker Protection Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints#api-description "Direct link to API Description")

Get config for MMP.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints#http-request "Direct link to HTTP Request")

GET `/eapi/v1/mmp (HMAC SHA256)`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| TRUE| underlying, e.g BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints#response-example "Direct link to Response Example")
    
    
    {  
        "underlyingId": 2,  
        "underlying": "BTCUSDT",  
        "windowTimeInMilliseconds": 3000,  
        "frozenTimeInMilliseconds": 300000,  
        "qtyLimit": "2",  
        "deltaLimit": "2.3",  
        "lastTriggerTime": 0  
    }

---

# 获取MMP规则

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints#接口描述 "接口描述的直接链接")

获取MMP参数

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/mmpSet`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlying| STRING| YES| 标的资产如BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| NO|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints#响应示例 "响应示例的直接链接")
    
    
    {  
        "underlyingId": 2,  
        "underlying": "BTCUSDT",  
        "windowTimeInMilliseconds": 3000,  
        "frozenTimeInMilliseconds": 300000,  
        "qtyLimit": "2",  
        "deltaLimit": "2.3",  
        "lastTriggerTime": 0  
      
    }