---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:47:52.349150
---

# Aggregate Trade Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-description "Direct link to Stream Description")

The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds. Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-name "Direct link to Stream Name")

`<symbol>@aggTrade`

**Note** :

> Retail Price Improvement(RPI) orders are aggregated into field `q` and without special tags to be distinguished.

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#update-speed "Direct link to Update Speed")

**100ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e": "aggTrade",  // Event type  
      "E": 123456789,   // Event time  
      "s": "BTCUSDT",   // Symbol  
      "a": 5933014,		  // Aggregate trade ID  
      "p": "0.001",     // Price  
      "q": "100",       // Quantity with all the market trades  
      "nq": "100",      // Normal quantity without the trades involving RPI orders  
      "f": 100,         // First trade ID  
      "l": 105,         // Last trade ID  
      "T": 123456785,   // Trade time  
      "m": true,        // Is the buyer the market maker?  
    }

---

# 归集交易

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#数据流描述 "数据流描述的直接链接")

同一价格、同一方向、同一时间(100ms计算)的trade会被聚合为一条.

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-name "Stream Name的直接链接")

`<symbol>@aggTrade`

**注意：** 响应消息字段`q`聚合RPI订单数据，但无任何特殊标签区别。

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#更新速度 "更新速度的直接链接")

**100ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "aggTrade",  // 事件类型  
      "E": 123456789,   // 事件时间  
      "s": "BNBUSDT",   // 交易对  
      "a": 5933014,		  // 归集成交 ID  
      "p": "0.001",     // 成交价格  
      "q": "100",       // 成交量，包含RPI订单数据  
      "nq": "100",      // 普通订单成交量，不包含RPI订单数据  
      "f": 100,         // 被归集的首个交易ID  
      "l": 105,         // 被归集的末次交易ID  
      "T": 123456785,   // 成交时间  
      "m": true         // 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。  
    }