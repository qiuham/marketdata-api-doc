---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker
api_type: Market Data
updated_at: 2026-01-15T23:39:24.222201
---

# Symbol Price Ticker

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#api-description "Direct link to API Description")

Latest price for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#http-request "Direct link to HTTP Request")

GET `/dapi/v1/ticker/price`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#request-weight "Direct link to Request Weight")

**1** for a single symbol, **2** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
  
>   * Symbol and pair cannot be sent together
>   * If a pair is sent,tickers for all symbols of the pair will be returned
>   * If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#response-example "Direct link to Response Example")
    
    
    [  
    	{  
      		"symbol": "BTCUSD_200626",	  
      		"ps": "9647.8",  			// pair   
      		"price": "9647.8",		  
      		"time": 1591257246176    
    	}  
    ]

---

# 最新价格

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#接口描述 "接口描述的直接链接")

返回最近价格

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/ticker/price`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#请求权重 "请求权重的直接链接")

  * 单交易对**1** ，不传交易对**2**



## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
pair| STRING| NO| 标的交易对  
  
>   * symbol 和 pair 不接受同时发送
>   * 发送 pair的,返回pair对应所有正在交易的symbol数据
>   * symbol,pair 都没有发送的,返回所有symbol数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
      		"symbol": "BTCUSD_200626",	// 交易对  
      		"ps": "BTCUSD",  			// 标的交易对  
      		"price": "9647.8",			// 价格  
      		"time": 1591257246176  		// 时间  
    	}  
    ]