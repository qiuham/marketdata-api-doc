---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate
api_type: Market Data
updated_at: 2026-01-15T23:44:25.632216
---

# Portfolio Margin Collateral Rate(MARKET_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#api-description "Direct link to API Description")

Portfolio Margin Collateral Rate

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/collateralRate`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#request-weightip "Direct link to Request Weight\(IP\)")

**50**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#response-example "Direct link to Response Example")
    
    
    [  
       {  
           "asset": "USDC",  
           "collateralRate": "1.0000"  
       },  
       {  
           "asset": "BUSD",  
           "collateralRate": "1.0000"  
       },  
    ]

---

# 统一账户资产质押率(MARKET_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#接口描述 "接口描述的直接链接")

统一账户资产质押率

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/collateralRate`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#请求权重ip "请求权重\(IP\)的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#请求参数 "请求参数的直接链接")

None

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#响应示例 "响应示例的直接链接")
    
    
    [  
       {  
           "asset": "USDC",  
           "collateralRate": "1.0000" //质押率  
       },  
       {  
           "asset": "BUSD",  
           "collateralRate": "1.0000"  
       },  
    ]