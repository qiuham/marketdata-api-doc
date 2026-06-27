---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:45.200796
---

# Individual Symbol Ticker Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-description "Direct link to Stream Description")

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name "Direct link to Stream Name")

`<symbol>@ticker`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#update-speed "Direct link to Update Speed")

**500ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"24hrTicker",				// Event type  
      "E":1591268262453,			// Event time  
      "s":"BTCUSD_200626",			// Symbol  
      "ps":"BTCUSD",				// Pair  
      "p":"-43.4",					// Price change  
      "P":"-0.452",					// Price change percent  
      "w":"0.00147974",				// Weighted average price  
      "c":"9548.5",					// Last price  
      "Q":"2",						// Last quantity  
      "o":"9591.9",					// Open price  
      "h":"10000.0",				// High price  
      "l":"7000.0",					// Low price  
      "v":"487850",					// Total traded volume  
      "q":"32968676323.46222700",	// Total traded base asset volume  
      "O":1591181820000,			// Statistics open time  
      "C":1591268262442,			// Statistics close time  
      "F":512014,					// First trade ID  
      "L":615289,					// Last trade Id  
      "n":103272					// Total number of trades  
    }

---

# 按Symbol的完整Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时完整ticker信息.

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name "Stream Name的直接链接")

`<symbol>@ticker`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#更新速度 "更新速度的直接链接")

**500ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"24hrTicker",				// 事件类型  
      "E":1591268262453,			// 事件时间  
      "s":"BTCUSD_200626",			// 交易对  
      "ps":"BTCUSD",				// 标的交易对  
      "p":"-43.4",					// 24小时价格变化  
      "P":"-0.452",					// 24小时价格变化(百分比)  
      "w":"0.00147974",				// 24小时平均价格  
      "c":"9548.5",					// 最新成交价格  
      "Q":"2",						// 最新成交价格上的成交量  
      "o":"9591.9",					// 24小时前第一笔成交价格  
      "h":"10000.0",				// 24小时内最高成交价  
      "l":"7000.0",					// 24小时内最低成交价  
      "v":"487850",					// 24小时成交量  
      "q":"32968676323.46222700",	// 24小时成交额(标的数量)  
      "O":1591181820000,			// 统计开始时间  
      "C":1591268262442,			// 统计关闭时间  
      "F":512014,					// 24小时内第一笔成交交易ID  
      "L":615289,					// 24小时内最后一笔成交交易ID  
      "n":103272					// 24小时内成交数  
    }