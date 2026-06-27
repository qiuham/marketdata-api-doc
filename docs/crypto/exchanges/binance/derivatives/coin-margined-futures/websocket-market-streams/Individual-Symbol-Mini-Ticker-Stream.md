---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:40:45.134387
---

# Individual Symbol Mini Ticker Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-description "Direct link to Stream Description")

24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-name "Direct link to Stream Name")

`<symbol>@miniTicker`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#update-speed "Direct link to Update Speed")

**500ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#response-example "Direct link to Response Example")
    
    
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

---

# 按Symbol的精简Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时精简ticker信息.

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-name "Stream Name的直接链接")

`<symbol>@miniTicker`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#更新速度 "更新速度的直接链接")

**500ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#响应示例 "响应示例的直接链接")
    
    
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