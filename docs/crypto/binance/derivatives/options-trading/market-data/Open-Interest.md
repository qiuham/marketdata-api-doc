---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Open-Interest
api_type: Market Data
updated_at: 2026-01-15T23:41:10.088533
---

# Open Interest

## API Description[​](/docs/derivatives/options-trading/market-data/Open-Interest#api-description "Direct link to API Description")

Get open interest for specific underlying asset on specific expiration date.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Open-Interest#http-request "Direct link to HTTP Request")

GET `/eapi/v1/openInterest`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Open-Interest#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Open-Interest#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlyingAsset| STRING| YES| underlying asset, e.g ETH/BTC  
expiration| STRING| YES| expiration date, e.g 221225  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Open-Interest#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "ETH-221119-1175-P",  
            "sumOpenInterest": "4.01",  
            "sumOpenInterestUsd": "4880.2985615624",  
            "timestamp": "1668754020000"  
        }  
    ]

---

# 合约持仓量

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Open-Interest#接口描述 "接口描述的直接链接")

获取期权持仓量。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Open-Interest#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/openInterest`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Open-Interest#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Open-Interest#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlyingAsset| STRING| YES| 标的资产，如ETH或BTC  
expiration| STRING| YES| 到期日，如221225  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Open-Interest#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "ETH-221119-1175-P",  
            "sumOpenInterest": "4.01",  
            "sumOpenInterestUsd": "4880.2985615624",  
            "timestamp": "1668754020000"  
        }  
    ]