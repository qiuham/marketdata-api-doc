---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:45.264730
---

# Kline/Candlestick Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-description "Direct link to Stream Description")

The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).

**Kline/Candlestick chart intervals:** m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

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



## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-name "Direct link to Stream Name")

`<symbol>@kline_<interval>`

e.g. "btcusd_200626@kline_1m"

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#update-speed "Direct link to Update Speed")

**250ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"kline",				// Event type  
      "E":1591261542539,		// Event time  
      "s":"BTCUSD_200626",		// Symbol  
      "k":{  
        "t":1591261500000,		// Kline start time  
        "T":1591261559999,		// Kline close time  
        "s":"BTCUSD_200626",	// Symbol  
        "i":"1m",				// Interval  
        "f":606400,				// First trade ID  
        "L":606430,				// Last trade ID  
        "o":"9638.9",			// Open price  
        "c":"9639.8",			// Close price  
        "h":"9639.8",			// High price  
        "l":"9638.6",			// Low price  
        "v":"156",				// volume  
        "n":31,					// Number of trades  
        "x":false,				// Is this kline closed?  
        "q":"1.61836886",		// Base asset volume  
        "V":"73",				// Taker buy volume  
        "Q":"0.75731156",		// Taker buy base asset volume  
        "B":"0"					// Ignore  
      }  
    }

---

# K线

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#数据流描述 "数据流描述的直接链接")

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。

**订阅Kline需要提供间隔参数,最短为分钟线,最长为月线。支持以下间隔:**

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



## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#stream-name "Stream Name的直接链接")

`<symbol>@kline_<interval>`

例如: btcusd_200626@kline_1m

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#更新速度 "更新速度的直接链接")

**250ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"kline",				// 事件类型  
      "E":1591261542539,		// 事件时间  
      "s":"BTCUSD_200626",		// 交易对  
      "k":{  
        "t":1591261500000,		// 这根K线的起始时间  
        "T":1591261559999,		// 这根K线的结束时间  
        "s":"BTCUSD_200626",	// 交易对  
        "i":"1m",				// K线间隔  
        "f":606400,				// 这根K线期间第一笔成交ID  
        "L":606430,				// 这根K线期间末一笔成交ID  
        "o":"9638.9",			// 这根K线期间第一笔成交价  
        "c":"9639.8",			// 这根K线期间末一笔成交价  
        "h":"9639.8",			// 这根K线期间最高成交价  
        "l":"9638.6",			// 这根K线期间最低成交价  
        "v":"156",				// 这根K线期间成交量  
        "n":31,					// 这根K线期间成交笔数  
        "x":false,				// 这根K线是否完结(是否已经开始下一根K线)  
        "q":"1.61836886",		// 这根K线期间成交额(标的数量)  
        "V":"73",				// 主动买入的成交量  
        "Q":"0.75731156",		// 主动买入的成交额(标的数量)  
        "B":"0"					// 忽略此参数  
      }  
    }