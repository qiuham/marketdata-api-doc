---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:38.713022
---

# Index Kline/Candlestick Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#stream-description "Direct link to Stream Description")

Index Kline/Candlestick Streams

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



## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#stream-name "Direct link to Stream Name")

`<pair>@indexPriceKline_<interval>`

e.g. "btcusd@indexPriceKline_1m"

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#update-speed "Direct link to Update Speed")

**250ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"indexPrice_kline",		// Event Name  
      "E":1591267070033,			// Event Time  
      "ps":"BTCUSD",				// Pair  
      "k":{  
        "t":1591267020000,			// Kline start time  
        "T":1591267079999,			// Kline close time  
        "s":"0",					// ignore  
        "i":"1m",					// Interval  
        "f":1591267020000,			// ignore  
        "L":1591267070000,			// ignore  
        "o":"9542.21900000",		// Open price  
        "c":"9542.50440000",		// Close price  
        "h":"9542.71640000",		// High price  
        "l":"9542.21040000",		// Low price  
        "v":"0",					// ignore  
        "n":51,						// Number of basic data  
        "x":false,					// Is this kline closed?  
        "q":"0",					// ignore  
        "V":"0",					// ignore  
        "Q":"0",					// ignore  
        "B":"0"						// ignore  
      }  
    }

---

# 价格指数K线

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#数据流描述 "数据流描述的直接链接")

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



## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#stream-name "Stream Name的直接链接")

`<pair>@indexPriceKline_<interval>`

例如: btcusd@indexPriceKline_1m

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#更新速度 "更新速度的直接链接")

**250ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"indexPrice_kline",		// 事件类型  
      "E":1591267070033,			// 事件时间  
      "ps":"BTCUSD",				// 标的交易对  
      "k":{  
        "t":1591267020000,			// 这根K线的起始时间  
        "T":1591267079999,			// 这根K线的结束时间  
        "s":"0",					// 无意义字段  
        "i":"1m",					// K线间隔  
        "f":1591267020000,			// 无意义字段  
        "L":1591267070000,			// 无意义字段  
        "o":"9542.21900000",		// 这根K线期间第一笔成交价  
        "c":"9542.50440000",		// 这根K线期间末一笔成交价  
        "h":"9542.71640000",		// 这根K线期间最高成交价  
        "l":"9542.21040000",		// 这根K线期间最低成交价  
        "v":"0",					// 无意义字段  
        "n":51,						// 这根K线更新期间数据数量  
        "x":false,					// 这根K线是否完结(是否已经开始下一根K线)  
        "q":"0",					// 无意义字段  
        "V":"0",					// 无意义字段  
        "Q":"0",					// 无意义字段  
        "B":"0"						// 无意义字段  
      }  
    }