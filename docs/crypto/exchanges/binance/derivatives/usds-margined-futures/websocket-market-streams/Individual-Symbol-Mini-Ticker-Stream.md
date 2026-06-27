---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:48:01.051813
---

# Individual Symbol Mini Ticker Stream

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-description "Direct link to Stream Description")

24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-name "Direct link to Stream Name")

`<symbol>@miniTicker`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#update-speed "Direct link to Update Speed")

**2s**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#response-example "Direct link to Response Example")
    
    
      {  
        "e": "24hrMiniTicker",  // Event type  
        "E": 123456789,         // Event time  
        "s": "BTCUSDT",         // Symbol  
        "c": "0.0025",          // Close price  
        "o": "0.0010",          // Open price  
        "h": "0.0025",          // High price  
        "l": "0.0010",          // Low price  
        "v": "10000",           // Total traded base asset volume  
        "q": "18"               // Total traded quote asset volume  
      }

---

# 按交易对的精简Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时精简ticker信息.

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-name "Stream Name的直接链接")

`<symbol>@miniTicker`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#更新速度 "更新速度的直接链接")

**2s**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#响应示例 "响应示例的直接链接")
    
    
      {  
        "e": "24hrMiniTicker",  // 事件类型  
        "E": 123456789,         // 事件时间(毫秒)  
        "s": "BNBUSDT",          // 交易对  
        "c": "0.0025",          // 最新成交价格  
        "o": "0.0010",          // 24小时前开始第一笔成交价格  
        "h": "0.0025",          // 24小时内最高成交价  
        "l": "0.0010",          // 24小时内最低成交价  
        "v": "10000",           // 成交量  
        "q": "18"               // 成交额  
      }