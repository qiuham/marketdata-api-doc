---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:24.004840
---

# Aggregate Trade Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-description "Direct link to Stream Description")

The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-name "Direct link to Stream Name")

`<symbol>@aggTrade`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#update-speed "Direct link to Update Speed")

**100ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"aggTrade",		// Event type  
      "E":1591261134288,	// Event time  
      "a":424951,			// Aggregate trade ID  
      "s":"BTCUSD_200626",	// Symbol  
      "p":"9643.5",			// Price  
      "q":"2",				// Quantity  
      "f":606073,			// First trade ID  
      "l":606073,			// Last trade ID  
      "T":1591261134199,	// Trade time  
      "m":false				// Is the buyer the market maker?  
    }

---

# 归集交易

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#数据流描述 "数据流描述的直接链接")

同一价格、同一方向、同一时间(100ms计算)的trade会被聚合为一条.推送间隔100毫秒。

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-name "Stream Name的直接链接")

`<symbol>@aggTrade`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#更新速度 "更新速度的直接链接")

**100ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"aggTrade",		// 事件类型  
      "E":1591261134288,	// 事件时间  
      "a":424951,				// 归集成交ID  
      "s":"BTCUSD_200626",	// 交易对  
      "p":"9643.5",			// 成交价格  
      "q":"2",				// 成交量  
      "f":606073,				// 被归集的首个交易ID  
      "l":606073,				// 被归集的末次交易ID  
      "T":1591261134199,	// 成交时间  
      "m":false				// 买方是否是做市方。如true,则此次成交是一个主动卖出单,否则是一个主动买入单。  
    }