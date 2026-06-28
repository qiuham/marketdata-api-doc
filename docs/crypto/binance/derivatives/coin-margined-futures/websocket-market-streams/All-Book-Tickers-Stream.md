---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:40:24.070914
---

# All Book Tickers Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#stream-description "Direct link to Stream Description")

Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#stream-name "Direct link to Stream Name")

`!bookTicker`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#update-speed "Direct link to Update Speed")

`Real-time`

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#response-example "Direct link to Response Example")
    
    
    {  
      "e":"bookTicker",         // Event type  
      "u":17242169,             // Order book update Id  
      "s":"BTCUSD_200626",      // Symbol  
      "ps":"BTCUSD",            // Pair  
      "b":"9548.1",             // Best bid price  
      "B":"52",                 // Best bid qty  
      "a":"9548.5",             // Best ask price  
      "A":"11",                 // Best ask qty  
      "T":1591268628155,        // Transaction time  
      "E":1591268628166         // Event time  
    }

---

# 全市场最优挂单信息

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#数据流描述 "数据流描述的直接链接")

实时推送所有交易对交易对最优挂单信息

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#stream-name "Stream Name的直接链接")

`!bookTicker`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"bookTicker",         // 事件类型  
      "u":17242169,             // 更新ID  
      "s":"BTCUSD_200626",      // 交易对  
      "ps":"BTCUSD",                 // 标的交易对  
      "b":"9548.1",             // 买单最优挂单价格  
      "B":"52",                 // 买单最优挂单数量  
      "a":"9548.5",             // 卖单最优挂单价格  
      "A":"11",                 // 卖单最优挂单数量  
      "T":1591268628155,        // 撮合时间  
      "E":1591268628166         // 事件时间  
    }