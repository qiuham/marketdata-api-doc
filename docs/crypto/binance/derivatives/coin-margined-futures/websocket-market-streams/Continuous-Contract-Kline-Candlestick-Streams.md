---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:32.244292
---

# Continuous Contract Kline/Candlestick Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#stream-description "Direct link to Stream Description")

Kline update every second

**Contract type:**

  * perpetual
  * current_quarter
  * next_quarter



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



**Stream Name:**  
`<pair>_<contractType>@continuousKline_<interval>`

e.g. "btcusd_next_quarter@continuousKline_1m"

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#update-speed "Direct link to Update Speed")

**250ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"continuous_kline",	// Event type  
      "E":1591261542539,		// Event time  
      "ps":"BTCUSD",			// Pair  
      "ct":"NEXT_QUARTER"		// Contract type  
      "k":{  
        "t":1591261500000,		// Kline start time  
        "T":1591261559999,		// Kline close time  
        "i":"1m",				// Interval  
        "f":606400,				// First update ID  
        "L":606430,				// Last update ID  
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

# 连续合约K线

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#数据流描述 "数据流描述的直接链接")

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。

**合约类型:**

  * perpetual 永续合约
  * current_quarter 当季交割合约
  * next_quarter 次季交割合约



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



## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#stream-name "Stream Name的直接链接")

`<pair>_<contractType>@continuousKline_<interval>`

例如: "btcusd_next_quarter@continuousKline_1m"

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#更新速度 "更新速度的直接链接")

**250ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"continuous_kline",	// 事件类型  
      "E":1591261542539,		// 事件时间  
      "ps":"BTCUSD",			// 标的交易对  
      "ct":"NEXT_QUARTER",		// 合约类型   
      "k":{  
        "t":1591261500000,		// 这根K线的起始时间  
        "T":1591261559999,		// 这根K线的结束时间  
        "i":"1m",				// K线间隔  
        "f":606400,				// 这根K线期间第一个UpdateId  
        "L":606430,				// 这根K线期间末一笔UpdateId  
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