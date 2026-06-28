---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data
api_type: Market Data
updated_at: 2026-01-15T23:44:25.569455
---

# Query Portfolio Margin Asset Index Price (MARKET_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data#api-description "Direct link to API Description")

Query Portfolio Margin Asset Index Price

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/asset-index-price`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data#request-weightip "Direct link to Request Weight\(IP\)")

**1** if send asset or **50** if not send asset

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/market-data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data#response-example "Direct link to Response Example")
    
    
    [  
       {  
           "asset": "BTC",  
           "assetIndexPrice": "28251.9136906",  // in USD  
           "time": 1683518338121  
       }  
    ]

---

# 查询统一账户资产价格指数(MARKET_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#接口描述 "接口描述的直接链接")

查询统一账户资产价格指数

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/asset-index-price`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#请求权重ip "请求权重\(IP\)的直接链接")

传asset为**1** 或不传asset**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#响应示例 "响应示例的直接链接")
    
    
    [  
       {  
           "asset": "BTC",  
           "assetIndexPrice": "28251.9136906",  //USD价格指数  
           "time": 1683518338121  
       }  
    ]