---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest
api_type: Market Data
updated_at: 2026-01-15T23:38:29.612003
---

# Open Interest

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#api-description "Direct link to API Description")

Get present open interest of a specific symbol.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#http-request "Direct link to HTTP Request")

GET `/dapi/v1/openInterest`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#response-example "Direct link to Response Example")
    
    
    {  
    	"symbol": "BTCUSD_200626",  
    	"pair": "BTCUSD",  
    	"openInterest": "15004",  
    	"contractType": "CURRENT_QUARTER",  
    	"time": 1591261042378  
    }

---

# 获取未平仓合约数

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#接口描述 "接口描述的直接链接")

合约持仓量

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/openInterest`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#响应示例 "响应示例的直接链接")
    
    
    {  
    	"symbol": "BTCUSD_200626",  
    	"pair": "BTCUSD",  
    	"openInterest": "15004",  
    	"contractType": "CURRENT_QUARTER",  
    	"time": 1591261042378  
    }