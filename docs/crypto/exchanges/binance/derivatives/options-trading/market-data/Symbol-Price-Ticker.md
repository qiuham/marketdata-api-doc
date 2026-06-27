---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker
api_type: Market Data
updated_at: 2026-01-15T23:41:26.048983
---

# Index Price

## API Description[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#api-description "Direct link to API Description")

Get spot index price for option underlying.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#http-request "Direct link to HTTP Request")

GET `/eapi/v1/index`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| YES| Spot pair（Option contract underlying asset, e.g BTCUSDT)  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#response-example "Direct link to Response Example")
    
    
    {  
       "time": 1656647305000,  
       "indexPrice": "105917.75" // Current index price  
    }

---

# 标的指数价格

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Symbol-Price-Ticker#接口描述 "接口描述的直接链接")

返回指数价格

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Symbol-Price-Ticker#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/index`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Symbol-Price-Ticker#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Symbol-Price-Ticker#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlying| STRING| YES| 现货交易对如BTCUSDT  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Symbol-Price-Ticker#响应示例 "响应示例的直接链接")
    
    
    {  
       "time": 1656647305000,  
       "indexPrice": "105917.75" // 指数价格  
    }