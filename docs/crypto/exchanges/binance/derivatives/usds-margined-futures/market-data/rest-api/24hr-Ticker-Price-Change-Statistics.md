---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics
api_type: Market Data
updated_at: 2026-01-15T23:46:42.609755
---

# 24hr Ticker Price Change Statistics

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#api-description "Direct link to API Description")

24 hour rolling window price change statistics.  
**Careful** when accessing this with no symbol.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#http-request "Direct link to HTTP Request")

GET `/fapi/v1/ticker/24hr`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-weight "Direct link to Request Weight")

**1** for a single symbol;  
**40** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * If the symbol is not sent, tickers for all symbols will be returned in an array.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#response-example "Direct link to Response Example")

> **Response:**
    
    
    {  
      "symbol": "BTCUSDT",  
      "priceChange": "-94.99999800",  
      "priceChangePercent": "-95.960",  
      "weightedAvgPrice": "0.29628482",  
      "lastPrice": "4.00000200",  
      "lastQty": "200.00000000",  
      "openPrice": "99.00000000",  
      "highPrice": "100.00000000",  
      "lowPrice": "0.10000000",  
      "volume": "8913.30000000",  
      "quoteVolume": "15.30000000",  
      "openTime": 1499783499040,  
      "closeTime": 1499869899040,  
      "firstId": 28385,   // First tradeId  
      "lastId": 28460,    // Last tradeId  
      "count": 76         // Trade count  
    }  
    

> OR
    
    
    [  
    	{  
      		"symbol": "BTCUSDT",  
      		"priceChange": "-94.99999800",  
      		"priceChangePercent": "-95.960",  
      		"weightedAvgPrice": "0.29628482",  
      		"lastPrice": "4.00000200",  
      		"lastQty": "200.00000000",  
      		"openPrice": "99.00000000",  
      		"highPrice": "100.00000000",  
      		"lowPrice": "0.10000000",  
      		"volume": "8913.30000000",  
      		"quoteVolume": "15.30000000",  
      		"openTime": 1499783499040,  
      		"closeTime": 1499869899040,  
      		"firstId": 28385,   // First tradeId  
      		"lastId": 28460,    // Last tradeId  
      		"count": 76         // Trade count  
    	}  
    ]

---

# 24hr价格变动情况

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#接口描述 "接口描述的直接链接")

请注意，不携带symbol参数会返回全部交易对数据，不仅数据庞大，而且权重极高

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/ticker/24hr`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#请求权重 "请求权重的直接链接")

带symbol为**1** , 不带为**40**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#响应示例 "响应示例的直接链接")
    
    
    {  
      "symbol": "BTCUSDT",  
      "priceChange": "-94.99999800",    //24小时价格变动  
      "priceChangePercent": "-95.960",  //24小时价格变动百分比  
      "weightedAvgPrice": "0.29628482", //加权平均价  
      "lastPrice": "4.00000200",        //最近一次成交价  
      "lastQty": "200.00000000",        //最近一次成交额  
      "openPrice": "99.00000000",       //24小时内第一次成交的价格  
      "highPrice": "100.00000000",      //24小时最高价  
      "lowPrice": "0.10000000",         //24小时最低价  
      "volume": "8913.30000000",        //24小时成交量  
      "quoteVolume": "15.30000000",     //24小时成交额  
      "openTime": 1499783499040,        //24小时内，第一笔交易的发生时间  
      "closeTime": 1499869899040,       //24小时内，最后一笔交易的发生时间  
      "firstId": 28385,   // 首笔成交id  
      "lastId": 28460,    // 末笔成交id  
      "count": 76         // 成交笔数  
    }  
    

> 或(当不发送交易对信息)
    
    
    [  
    	{  
      		"symbol": "BTCUSDT",  
      		"priceChange": "-94.99999800",    //24小时价格变动  
      		"priceChangePercent": "-95.960",  //24小时价格变动百分比  
      		"weightedAvgPrice": "0.29628482", //加权平均价  
      		"lastPrice": "4.00000200",        //最近一次成交价  
      		"lastQty": "200.00000000",        //最近一次成交额  
      		"openPrice": "99.00000000",       //24小时内第一次成交的价格  
      		"highPrice": "100.00000000",      //24小时最高价  
      		"lowPrice": "0.10000000",         //24小时最低价  
      		"volume": "8913.30000000",        //24小时成交量  
      		"quoteVolume": "15.30000000",     //24小时成交额  
      		"openTime": 1499783499040,        //24小时内，第一笔交易的发生时间  
      		"closeTime": 1499869899040,       //24小时内，最后一笔交易的发生时间  
      		"firstId": 28385,   // 首笔成交id  
      		"lastId": 28460,    // 末笔成交id  
      		"count": 76         // 成交笔数  
        }  
    ]