---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:48:00.992256
---

# Individual Symbol Book Ticker Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#stream-description "Direct link to Stream Description")

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#stream-name "Direct link to Stream Name")

`<symbol>@bookTicker`

**Note** :

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#update-speed "Direct link to Update Speed")

**Real-time**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"bookTicker",			// event type  
      "u":400900217,     		// order book updateId  
      "E": 1568014460893,  		// event time  
      "T": 1568014460891,  		// transaction time  
      "s":"BNBUSDT",     		// symbol  
      "b":"25.35190000", 		// best bid price  
      "B":"31.21000000", 		// best bid qty  
      "a":"25.36520000", 		// best ask price  
      "A":"40.66000000"  		// best ask qty  
    }

---

# 按Symbol的最优挂单信息

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#数据流描述 "数据流描述的直接链接")

实时推送指定交易对最优挂单信息

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#stream-name "Stream Name的直接链接")

`<symbol>@bookTicker`

**注意：** 响应消息不包含RPI订单，其不可见。

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"bookTicker",		// 事件类型  
      "u":400900217,     	// 更新ID  
      "E": 1568014460893,	// 事件推送时间  
      "T": 1568014460891,	// 撮合时间  
      "s":"BNBUSDT",     	// 交易对  
      "b":"25.35190000", 	// 买单最优挂单价格  
      "B":"31.21000000", 	// 买单最优挂单数量  
      "a":"25.36520000", 	// 卖单最优挂单价格  
      "A":"40.66000000"  	// 卖单最优挂单数量  
    }