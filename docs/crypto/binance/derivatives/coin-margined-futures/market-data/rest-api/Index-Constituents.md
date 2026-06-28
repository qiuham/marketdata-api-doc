---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents
api_type: Market Data
updated_at: 2026-01-15T23:38:10.532604
---

# Query Index Price Constituents

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#api-description "Direct link to API Description")

Query index price constituents

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#http-request "Direct link to HTTP Request")

GET `/dapi/v1/constituents`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#response-example "Direct link to Response Example")
    
    
    {  
        "symbol": "BTCUSD",  
        "time": 1697422647853,  
        "constituents": [  
            {  
                "exchange": "bitstamp",  
                "symbol": "btcusd"  
            },  
            {  
                "exchange": "coinbase",  
                "symbol": "BTC-USD"  
            },  
            {  
                "exchange": "kraken",  
                "symbol": "XBT/USD"  
            },  
            {  
                "exchange": "binance_cross",  
                "symbol": "BTCUSDC*index(USDCUSD)"  
            }  
        ]  
    }

---

# 查询指数价格成分

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#接口描述 "接口描述的直接链接")

查询指数价格成分

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/constituents`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#响应示例 "响应示例的直接链接")
    
    
    {  
        "symbol": "BTCUSD",  
        "time": 1697422647853,  
        "constituents": [  
            {  
                "exchange": "bitstamp",  
                "symbol": "btcusd"  
            },  
            {  
                "exchange": "coinbase",  
                "symbol": "BTC-USD"  
            },  
            {  
                "exchange": "kraken",  
                "symbol": "XBT/USD"  
            },  
            {  
                "exchange": "binance_cross",  
                "symbol": "BTCUSDC*index(USDCUSD)"  
            }  
        ]  
    }