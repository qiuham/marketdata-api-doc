---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data
api_type: Market Data
updated_at: 2026-01-15T23:46:45.943807
---

# Continuous Contract Kline/Candlestick Data

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#api-description "Direct link to API Description")

Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#http-request "Direct link to HTTP Request")

GET `/fapi/v1/continuousKlines`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#request-weight "Direct link to Request Weight")

based on parameter `LIMIT`

LIMIT| weight  
---|---  
[1,100)| 1  
[100, 500)| 2  
[500, 1000]| 5  
> 1000| 10  
  
## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
pair| STRING| YES|   
contractType| ENUM| YES|   
interval| ENUM| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1500.  
  
>   * If startTime and endTime are not sent, the most recent klines are returned.
> 


>   * Contract type: 
>     * PERPETUAL
>     * CURRENT_QUARTER
>     * NEXT_QUARTER
>     * TRADIFI_PERPETUAL
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#response-example "Direct link to Response Example")
    
    
    [  
      [  
        1607444700000,      	// Open time  
        "18879.99",       	 	// Open  
        "18900.00",       	 	// High  
        "18878.98",       	 	// Low  
        "18896.13",      	 	// Close (or latest price)  
        "492.363", 			 	// Volume  
        1607444759999,       	// Close time  
        "9302145.66080",    	// Quote asset volume  
        1874,             		// Number of trades  
        "385.983",    			// Taker buy volume  
        "7292402.33267",      	// Taker buy quote asset volume  
        "0" 					// Ignore.  
      ]  
    ]

---

# 连续合约K线数据

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#接口描述 "接口描述的直接链接")

每根K线的开盘时间可视为唯一ID

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/continuousKlines`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#请求权重 "请求权重的直接链接")

取决于请求中的LIMIT参数

LIMIT参数| 权重  
---|---  
[1,100)| 1  
[100, 500)| 2  
[500, 1000]| 5  
> 1000| 10  
  
## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
pair| STRING| YES| 标的交易对  
contractType| ENUM| YES| 合约类型  
interval| ENUM| YES| 时间间隔  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:500 最大值:1500  
  
  * 缺省返回最近的数据

  * 合约类型:

    * PERPETUAL 永续合约
    * CURRENT_QUARTER 当季交割合约
    * NEXT_QUARTER 次季交割合约
    * TRADIFI_PERPETUAL 传统金融合约



## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Continuous-Contract-Kline-Candlestick-Data#响应示例 "响应示例的直接链接")
    
    
    [  
      [  
        1607444700000,    	// 开盘时间  
        "18879.99",       	// 开盘价  
        "18900.00",       	// 最高价  
        "18878.98",       	// 最低价  
        "18896.13",       	// 收盘价(当前K线未结束的即为最新价)  
        "492.363",  		// 成交量  
        1607444759999,   	// 收盘时间  
        "9302145.66080",    // 成交额  
        1874,               // 成交笔数  
        "385.983",    		// 主动买入成交量  
        "7292402.33267",    // 主动买入成交额  
        "0" 				// 请忽略该参数  
      ]  
    ]