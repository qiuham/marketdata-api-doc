---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2
api_type: Market Data
updated_at: 2026-01-15T23:47:00.417511
---

# Symbol Price Ticker V2

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#api-description "Direct link to API Description")

Latest price for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#http-request "Direct link to HTTP Request")

GET `/fapi/v2/ticker/price`

**Weight:**

**1** for a single symbol;  
**2** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * If the symbol is not sent, prices for all symbols will be returned in an array.
>   * The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#response-example "Direct link to Response Example")
    
    
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

# 最新价格V2

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#接口描述 "接口描述的直接链接")

返回最近价格

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#http请求 "HTTP请求的直接链接")

GET `/fapi/v2/ticker/price`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#请求权重 "请求权重的直接链接")

单交易对**1** ，无交易对**2**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
>   * 该接口返回头中的`X-MBX-USED-WEIGHT-1M`参数不准确，可以忽略
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2#响应示例 "响应示例的直接链接")

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