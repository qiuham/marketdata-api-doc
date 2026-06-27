---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker
api_type: Market Data
updated_at: 2026-01-15T23:47:00.354034
---

# Symbol Price Ticker(Deprecated)

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#api-description "Direct link to API Description")

Latest price for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#http-request "Direct link to HTTP Request")

GET `/fapi/v1/ticker/price`

**Weight:**

**1** for a single symbol;  
**2** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * If the symbol is not sent, prices for all symbols will be returned in an array.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#response-example "Direct link to Response Example")
    
    
    {  
      "symbol": "BTCUSDT",  
      "price": "6000.01",  
      "time": 1589437530011   // Transaction time  
    }  
    

> OR
    
    
    [  
    	{  
      		"symbol": "BTCUSDT",  
      		"price": "6000.01",  
      		"time": 1589437530011  
    	}  
    ]

---

# 最新价格

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#接口描述 "接口描述的直接链接")

返回最近价格

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/ticker/price`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#请求权重 "请求权重的直接链接")

单交易对**1** ，无交易对**2**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    {  
      "symbol": "LTCBTC",		// 交易对  
      "price": "4.00000200",		// 价格  
      "time": 1589437530011   // 撮合引擎时间  
    }  
    

> 或(当不发送symbol)
    
    
    [  
    	{  
      		"symbol": "BTCUSDT",	// 交易对  
      		"price": "6000.01",		// 价格  
      		"time": 1589437530011   // 撮合引擎时间  
    	}  
    ]