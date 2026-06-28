---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents
api_type: Market Data
updated_at: 2026-01-15T23:46:49.847210
---

# Query Index Price Constituents

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#api-description "Direct link to API Description")

Query index price constituents

**Note** :

> Prices from constituents of TradFi perps will be hiden and displayed as -1.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#http-request "Direct link to HTTP Request")

GET `/fapi/v1/constituents`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#request-weight "Direct link to Request Weight")

**2**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#response-example "Direct link to Response Example")
    
    
    {  
        "symbol": "BTCUSDT",  
        "time": 1745401553408,  
        "constituents": [  
            {  
                "exchange": "binance",  
                "symbol": "BTCUSDT",  
                "price": "94057.03000000",  
                "weight": "0.51282051"  
            },  
            {  
                "exchange": "coinbase",  
                "symbol": "BTC-USDT",  
                "price": "94140.58000000",  
                "weight": "0.15384615"  
            },  
            {  
                "exchange": "gateio",  
                "symbol": "BTC_USDT",  
                "price": "94060.10000000",  
                "weight": "0.02564103"  
            },  
            {  
                "exchange": "kucoin",  
                "symbol": "BTC-USDT",  
                "price": "94096.70000000",  
                "weight": "0.07692308"  
            },  
            {  
                "exchange": "mxc",  
                "symbol": "BTCUSDT",  
                "price": "94057.02000000",  
                "weight": "0.07692308"  
            },  
            {  
                "exchange": "bitget",  
                "symbol": "BTCUSDT",  
                "price": "94064.03000000",  
                "weight": "0.07692308"  
            },  
            {  
                "exchange": "bybit",  
                "symbol": "BTCUSDT",  
                "price": "94067.90000000",  
                "weight": "0.07692308"  
            }  
        ]  
    }

---

# 查询指数价格成分

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#接口描述 "接口描述的直接链接")

查询指数价格成分

**注意：** 传统金融合约的成分价格将被隐藏，并统一显示为 -1。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/constituents`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#请求权重 "请求权重的直接链接")

**2**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents#响应示例 "响应示例的直接链接")
    
    
    {  
        "symbol": "BTCUSDT",  
        "time": 1745401553408,  
        "constituents": [  
            {  
                "exchange": "binance",  
                "symbol": "BTCUSDT",  
                "price": "94057.03000000",  
                "weight": "0.51282051"  
            },  
            {  
                "exchange": "coinbase",  
                "symbol": "BTC-USDT",  
                "price": "94140.58000000",  
                "weight": "0.15384615"  
            },  
            {  
                "exchange": "gateio",  
                "symbol": "BTC_USDT",  
                "price": "94060.10000000",  
                "weight": "0.02564103"  
            },  
            {  
                "exchange": "kucoin",  
                "symbol": "BTC-USDT",  
                "price": "94096.70000000",  
                "weight": "0.07692308"  
            },  
            {  
                "exchange": "mxc",  
                "symbol": "BTCUSDT",  
                "price": "94057.02000000",  
                "weight": "0.07692308"  
            },  
            {  
                "exchange": "bitget",  
                "symbol": "BTCUSDT",  
                "price": "94064.03000000",  
                "weight": "0.07692308"  
            },  
            {  
                "exchange": "bybit",  
                "symbol": "BTCUSDT",  
                "price": "94067.90000000",  
                "weight": "0.07692308"  
            }  
        ]  
    }