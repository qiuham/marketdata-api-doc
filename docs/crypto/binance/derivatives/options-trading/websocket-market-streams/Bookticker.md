---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Bookticker
api_type: WebSocket
updated_at: 2026-01-15T23:43:45.681961
---

# Individual Symbol Book Ticker Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#stream-description "Direct link to Stream Description")

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#stream-name "Direct link to Stream Name")

`<symbol>@bookTicker`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#update-speed "Direct link to Update Speed")

**Real-Time**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#response-example "Direct link to Response Example")
    
    
    {  
            "e": "bookTicker",             // event type  
            "u": 2472,                     // order book updateId  
            "s": "BTC-251226-110000-C",    // symbol  
            "b": "5000.000",               // best bid price  
            "B": "0.2000",                 // bid bid quantity  
            "a": "5100.000",               // best ask price  
            "A": "0.1000",                 // best ask quantity  
            "T": 1763041762942,            // transaction time  
            "E": 1763041762942             // event time  
    }

---

# 按Symbol的最优挂单信息

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Bookticker#数据流描述 "数据流描述的直接链接")

实时推送指定交易对最优挂单信息.

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Bookticker#url-path "URL PATH的直接链接")

`/public`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Bookticker#stream-name "Stream Name的直接链接")

`<symbol>@bookTicker`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Bookticker#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Bookticker#响应示例 "响应示例的直接链接")
    
    
    {  
            "e": "bookTicker",           // 事件类型  
            "u": 2472,                   // 更新ID  
            "s": "BTC-251226-110000-C",  // 交易对  
            "b": "5000.000",             // 买单最优挂单价格  
            "B": "0.2000",               // 买单最优挂单数量  
            "a": "5100.000",             // 卖单最优挂单价格  
            "A": "0.1000",               // 卖单最优挂单数量  
            "T": 1763041762942,          // 撮合时间  
            "E": 1763041762942           // 事件推送时间  
    }