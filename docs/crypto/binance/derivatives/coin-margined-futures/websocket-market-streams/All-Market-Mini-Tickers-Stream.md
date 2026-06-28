---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:40:32.118645
---

# All Market Mini Tickers Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#stream-description "Direct link to Stream Description")

24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#stream-name "Direct link to Stream Name")

`!miniTicker@arr`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#response-example "Direct link to Response Example")
    
    
    [    
    	{  
    	  "e":"24hrMiniTicker",			// Event type  
    	  "E":1591267704450,			// Event time  
    	  "s":"BTCUSD_200626",			// Symbol  
    	  "ps":"BTCUSD",				// Pair  
    	  "c":"9561.7",					// Close price  
    	  "o":"9580.9",					// Open price  
    	  "h":"10000.0",				// High price  
    	  "l":"7000.0",					// Low price  
    	  "v":"487476",					// Total traded volume  
    	  "q":"33264343847.22378500"	// Total traded base asset volume  
    	}  
    ]

---

# 全市场的精简Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#数据流描述 "数据流描述的直接链接")

所有symbol24小时精简ticker信息.需要注意的是,只有发生变化的ticker更新才会被推送。

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#stream-name "Stream Name的直接链接")

`!miniTicker@arr`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#更新速度 "更新速度的直接链接")

**1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#响应示例 "响应示例的直接链接")
    
    
    [    
    	{  
    	  "e":"24hrMiniTicker",			// 事件类型  
    	  "E":1591267704450,			// 事件时间  
    	  "s":"BTCUSD_200626",			// 交易对  
    	  "ps":"BTCUSD",				// 标的交易对  
    	  "c":"9561.7",					// 最新成交价格  
    	  "o":"9580.9",					// 24小时前开始第一笔成交价格  
    	  "h":"10000.0",				// 24小时内最高成交价  
    	  "l":"7000.0",					// 24小时内最低成交价  
    	  "v":"487476",					// 24小时成交量  
    	  "q":"33264343847.22378500"	// 24小时成交额(标的数量)  
    	}  
    ]