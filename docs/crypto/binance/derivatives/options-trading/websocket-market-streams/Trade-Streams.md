---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:43:58.506420
---

# Trade Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#stream-description "Direct link to Stream Description")

The Trade Streams push raw trade information for specific symbol or underlying asset. E.g.[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#stream-name "Direct link to Stream Name")

`<symbol>@optionTrade` or `<underlying>@optionTrade`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#response-example "Direct link to Response Example")
    
    
    {  
        "e": "trade",                  // event type     
        "E": 1762856064204,            // event time     
        "T": 1762856064203,            // trade completed time      
        "s": "BTC-251123-126000-C",    // Option trading symbol      
        "t": 4,                        // trade ID     
        "p": "1300.000",               // price  
        "q": "0.1000",                 // quantity, always positive  
        "X": "MARKET",                 // trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade	  
        "S": "BUY",                    // direction     
        "m": false                     // Is the buyer the market maker?  
    }

---

# 最新交易

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Trade-Streams#数据流描述 "数据流描述的直接链接")

交易流推出特定交易对或特定标的资产的最新成交信息。如[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Trade-Streams#url-path "URL PATH的直接链接")

`/public`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Trade-Streams#stream-name "Stream Name的直接链接")

`<symbol>@optionTrade` or `<underlying>@optionTrade`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Trade-Streams#更新速度 "更新速度的直接链接")

**50ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Trade-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
        "e": "trade",                  // 事件类型    
        "E": 1762856064204,            // 事件时间     
        "T": 1762856064203,            // trade completed time      
        "s": "BTC-251123-126000-C",    // 交易对    
        "t": 4,                        // 交易ID     
        "p": "1300.000",               // 交易价格     
        "q": "0.1000",                 // 交易数量     
        "X": "MARKET",                 // 交易类型，"MARKET" 代表订单薄交易, "BLOCK"代表大宗交易  
        "S": "BUY",                    // 方向     
        "m": false                     // 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。  
    }