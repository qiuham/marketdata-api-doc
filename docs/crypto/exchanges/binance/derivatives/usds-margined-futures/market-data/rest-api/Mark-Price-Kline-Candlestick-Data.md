---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data
api_type: Market Data
updated_at: 2026-01-15T23:46:53.438453
---

# Mark Price Kline/Candlestick Data

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#api-description "Direct link to API Description")

Kline/candlestick bars for the mark price of a symbol. Klines are uniquely identified by their open time.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#http-request "Direct link to HTTP Request")

GET `/fapi/v1/markPriceKlines`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#request-weight "Direct link to Request Weight")

based on parameter `LIMIT`

LIMIT| weight  
---|---  
[1,100)| 1  
[100, 500)| 2  
[500, 1000]| 5  
> 1000| 10  
  
## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
interval| ENUM| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 1500.  
  
>   * If startTime and endTime are not sent, the most recent klines are returned.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#response-example "Direct link to Response Example")
    
    
    [  
      [  
        1591256460000,     		// Open time  
        "9653.29201333",    	// Open  
        "9654.56401333",     	// High  
        "9653.07367333",     	// Low  
        "9653.07367333",     	// Close (or latest price)  
        "0	", 					// Ignore  
        1591256519999,      	// Close time  
        "0",    				// Ignore  
        60,                	 	// Ignore  
        "0",    				// Ignore  
        "0",      			 	// Ignore  
        "0" 					// Ignore  
      ]  
    ]

---

# 标记价格K线数据

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#接口描述 "接口描述的直接链接")

每根K线的开盘时间可视为唯一ID

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/markPriceKlines`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#请求权重 "请求权重的直接链接")

取决于请求中的LIMIT参数

LIMIT参数| 权重  
---|---  
[1,100)| 1  
[100, 500)| 2  
[500, 1000]| 5  
> 1000| 10  
  
## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
interval| ENUM| YES| 时间间隔  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:500 最大值:1500  
  
>   * 缺省返回最近的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data#响应示例 "响应示例的直接链接")
    
    
    [  
      [  
        1591256400000,      	// 开盘时间  
        "9653.69440000",    	// 开盘价  
        "9653.69640000",     	// 最高价  
        "9651.38600000",     	// 最低价  
        "9651.55200000",     	// 收盘价(当前K线未结束的即为最新价)  
        "0	", 					// 请忽略  
        1591256459999,      	// 收盘时间  
        "0",    				// 请忽略  
        60,                		// 请忽略  
        "0",    				// 请忽略  
        "0",      				// 请忽略  
        "0" 					// 请忽略  
      ]  
    ]