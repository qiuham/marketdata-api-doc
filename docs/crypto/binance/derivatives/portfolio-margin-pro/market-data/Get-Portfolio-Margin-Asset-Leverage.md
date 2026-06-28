---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage
api_type: Market Data
updated_at: 2026-01-15T23:44:25.692770
---

# Get Portfolio Margin Asset Leverage(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#api-description "Direct link to API Description")

Get Portfolio Margin Asset Leverage

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/margin-asset-leverage`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#request-weightip "Direct link to Request Weight\(IP\)")

**50**

## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#response-example "Direct link to Response Example")
    
    
    [  
       {  
           "asset": "USDC",  
           "leverage": 10  
       },  
       {  
           "asset": "USDT",  
           "leverage": 10  
       }  
    ]

---

# 查询统一账户资产支持杠杆倍数(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#接口描述 "接口描述的直接链接")

查询统一账户资产支持杠杆倍数

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/margin-asset-leverage`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#请求权重ip "请求权重\(IP\)的直接链接")

**50**

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#响应示例 "响应示例的直接链接")
    
    
    [  
       {  
           "asset": "USDC",  
           "leverage": 10  
       },  
       {  
           "asset": "USDT",  
           "leverage": 10  
       }  
    ]