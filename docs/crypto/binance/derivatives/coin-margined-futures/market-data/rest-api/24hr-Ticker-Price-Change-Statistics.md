---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics
api_type: Market Data
updated_at: 2026-01-15T23:37:57.898080
---

# 24hr Ticker Price Change Statistics

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#api-description "Direct link to API Description")

24 hour rolling window price change statistics.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#http-request "Direct link to HTTP Request")

GET `/dapi/v1/ticker/24hr`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-weight "Direct link to Request Weight")

**1** for a single symbol, **40** when the symbol parameter is omitted **Careful** when accessing this with no symbol.

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
  
>   * Symbol and pair cannot be sent together
>   * If a pair is sent,tickers for all symbols of the pair will be returned
>   * If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_200925",  
    	  	"pair": "BTCUSD",  
    	  	"priceChange": "136.6",  
    	  	"priceChangePercent": "1.436",  
    	  	"weightedAvgPrice": "9547.3",  
    	  	"lastPrice": "9651.6",  
    	  	"lastQty": "1",  
    	  	"openPrice": "9515.0",  
    	  	"highPrice": "9687.0",  
    	  	"lowPrice": "9499.5",  
    	  	"volume": "494109",  
    	  	"baseVolume": "5192.94797687",  
    	  	"openTime": 1591170300000,  
    	  	"closeTime": 1591256718418,  
    	  	"firstId": 600507, // First tradeId  
    	  	"lastId": 697803,  // Last tradeId  
    	  	"count": 97297    // Trade count  	  
      	}  
    ]

---

# 24hr价格变动情况

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#接口描述 "接口描述的直接链接")

请注意,不携带symbol参数会返回全部交易对数据,不仅数据庞大,而且权重极高

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/ticker/24hr`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#请求权重 "请求权重的直接链接")

带symbol为**1** ，不带为**40**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
pair| STRING| NO| 标的交易对  
  
>   * symbol 和 pair 不接受同时发送
>   * 发送 pair的,返回pair对应所有正在交易的symbol数据
>   * symbol,pair 都没有发送的,返回所有symbol数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_200925",  
    	  	"pair": "BTCUSD",  
    	  	"priceChange": "136.6",				//24小时价格变动  
    	  	"priceChangePercent": "1.436", 	//24小时价格变动百分比  
    	  	"weightedAvgPrice": "9547.3",		//24小时加权平均价  
    	  	"lastPrice": "9651.6",				//最近一次成交价  
    	  	"lastQty": "1",						//最近一次成交量  
    	  	"openPrice": "9515.0",				//24小时内第一次成交的价格  
    	  	"highPrice": "9687.0",				//24小时最高价  
    	  	"lowPrice": "9499.5",				//24小时最低价  
    	  	"volume": "494109",					//24小时成交量  
    	  	"baseVolume": "5192.94797687",	//24小时成交额(标的数量)  
    	  	"openTime": 1591170300000,			//24小时内,第一笔交易的发生时间  
    	  	"closeTime": 1591256718418,		//24小时内,最后一笔交易的发生时间  
    	  	"firstId": 600507, 					// 首笔成交id  
    	  	"lastId": 697803,  					// 末笔成交id  
    	  	"count": 97297    					// 成交笔数 	  
      	}  
    ]