---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config
api_type: Market Data
updated_at: 2026-01-15T23:42:11.262080
---

# Reset Market Maker Protection Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#api-description "Direct link to API Description")

Reset MMP, start MMP order again.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#http-request "Direct link to HTTP Request")

POST `/eapi/v1/mmpReset`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| TRUE| underlying, e.g BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#response-example "Direct link to Response Example")
    
    
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

# 重置MMP状态

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#接口描述 "接口描述的直接链接")

MMP冻结后重置MMP，重新开启MMP下单

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#http请求 "HTTP请求的直接链接")

POST `/eapi/v1/mmpReset`

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlying| STRING| YES| 标的资产如BTCUSDT  
recvWindow| LONG| NO|   
timestamp| LONG| NO|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#响应示例 "响应示例的直接链接")
    
    
    {  
        "underlyingId": 2,  
        "underlying": "BTCUSDT",  
        "windowTimeInMilliseconds": 3000,  
        "frozenTimeInMilliseconds": 300000,  
        "qtyLimit": "2",  
        "deltaLimit": "2.3",  
        "lastTriggerTime": 0  
      
    }