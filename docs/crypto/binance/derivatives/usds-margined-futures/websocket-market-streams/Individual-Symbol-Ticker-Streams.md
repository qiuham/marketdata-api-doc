---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:48:04.643736
---

# Individual Symbol Ticker Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-description "Direct link to Stream Description")

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name "Direct link to Stream Name")

`<symbol>@ticker`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#update-speed "Direct link to Update Speed")

**2000ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e": "24hrTicker",  // Event type  
      "E": 123456789,     // Event time  
      "s": "BTCUSDT",     // Symbol  
      "p": "0.0015",      // Price change  
      "P": "250.00",      // Price change percent  
      "w": "0.0018",      // Weighted average price  
      "c": "0.0025",      // Last price  
      "Q": "10",          // Last quantity  
      "o": "0.0010",      // Open price  
      "h": "0.0025",      // High price  
      "l": "0.0010",      // Low price  
      "v": "10000",       // Total traded base asset volume  
      "q": "18",          // Total traded quote asset volume  
      "O": 0,             // Statistics open time  
      "C": 86400000,      // Statistics close time  
      "F": 0,             // First trade ID  
      "L": 18150,         // Last trade Id  
      "n": 18151          // Total number of trades  
    }

---

# 按Symbol的完整Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时完整ticker信息

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name "Stream Name的直接链接")

`<symbol>@ticker`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#更新速度 "更新速度的直接链接")

**2000ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "24hrTicker",  // 事件类型  
      "E": 123456789,     // 事件时间  
      "s": "BNBUSDT",      // 交易对  
      "p": "0.0015",      // 24小时价格变化  
      "P": "250.00",      // 24小时价格变化(百分比)  
      "w": "0.0018",      // 平均价格  
      "c": "0.0025",      // 最新成交价格  
      "Q": "10",          // 最新成交价格上的成交量  
      "o": "0.0010",      // 24小时内第一比成交的价格  
      "h": "0.0025",      // 24小时内最高成交价  
      "l": "0.0010",      // 24小时内最低成交价  
      "v": "10000",       // 24小时内成交量  
      "q": "18",          // 24小时内成交额  
      "O": 0,             // 统计开始时间  
      "C": 86400000,      // 统计关闭时间  
      "F": 0,             // 24小时内第一笔成交交易ID  
      "L": 18150,         // 24小时内最后一笔成交交易ID  
      "n": 18151          // 24小时内成交数  
    }