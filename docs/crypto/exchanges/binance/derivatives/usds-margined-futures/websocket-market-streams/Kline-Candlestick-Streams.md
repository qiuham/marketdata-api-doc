---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:48:04.711918
---

# Kline/Candlestick Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-description "Direct link to Stream Description")

The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).

**Kline/Candlestick chart intervals:**

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-name "Direct link to Stream Name")

`<symbol>@kline_<interval>`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#update-speed "Direct link to Update Speed")

**250ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e": "kline",     // Event type  
      "E": 1638747660000,   // Event time  
      "s": "BTCUSDT",    // Symbol  
      "k": {  
        "t": 1638747660000, // Kline start time  
        "T": 1638747719999, // Kline close time  
        "s": "BTCUSDT",  // Symbol  
        "i": "1m",      // Interval  
        "f": 100,       // First trade ID  
        "L": 200,       // Last trade ID  
        "o": "0.0010",  // Open price  
        "c": "0.0020",  // Close price  
        "h": "0.0025",  // High price  
        "l": "0.0015",  // Low price  
        "v": "1000",    // Base asset volume  
        "n": 100,       // Number of trades  
        "x": false,     // Is this kline closed?  
        "q": "1.0000",  // Quote asset volume  
        "V": "500",     // Taker buy base asset volume  
        "Q": "0.500",   // Taker buy quote asset volume  
        "B": "123456"   // Ignore  
      }  
    }

---

# K线

## Stream Description[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-description "Stream Description的直接链接")

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。推送间隔250毫秒(如有刷新)

**订阅 Kline 需要提供间隔参数，最短为分钟线，最长为月线。支持以下间隔:**

m -> 分钟; h -> 小时; d -> 天; w -> 周; M -> 月

  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-name "Stream Name的直接链接")

`<symbol>@kline_<interval>`

## Update Speed[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#update-speed "Update Speed的直接链接")

**250ms**

## Response Example[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#response-example "Response Example的直接链接")
    
    
    {  
      "e": "kline",     // 事件类型  
      "E": 123456789,   // 事件时间  
      "s": "BNBUSDT",    // 交易对  
      "k": {  
        "t": 123400000, // 这根K线的起始时间  
        "T": 123460000, // 这根K线的结束时间  
        "s": "BNBUSDT",  // 交易对  
        "i": "1m",      // K线间隔  
        "f": 100,       // 这根K线期间第一笔成交ID  
        "L": 200,       // 这根K线期间末一笔成交ID  
        "o": "0.0010",  // 这根K线期间第一笔成交价  
        "c": "0.0020",  // 这根K线期间末一笔成交价  
        "h": "0.0025",  // 这根K线期间最高成交价  
        "l": "0.0015",  // 这根K线期间最低成交价  
        "v": "1000",    // 这根K线期间成交量  
        "n": 100,       // 这根K线期间成交笔数  
        "x": false,     // 这根K线是否完结(是否已经开始下一根K线)  
        "q": "1.0000",  // 这根K线期间成交额  
        "V": "500",     // 主动买入的成交量  
        "Q": "0.500",   // 主动买入的成交额  
        "B": "123456"   // 忽略此参数  
      }  
    }