---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER
api_type: WebSocket
updated_at: 2026-01-15T23:43:38.688206
---

# 24-hour TICKER

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#stream-description "Direct link to Stream Description")

24hr ticker info for all symbols. Only symbols whose ticker info changed will be sent.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#stream-name "Direct link to Stream Name")

`<symbol>@optionTicker` or `<underlying>@optionTicker@<expiretionDate>` e.g: btcusdt@optionTicker@251230

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#response-example "Direct link to Response Example")
    
    
    {  
        "e": "24hrTicker",          // Event type  
        "E": 1764080707933,         // Event time  
        "s": "ETH-251226-3000-C",   // Symbol  
        "p": "0.0000",              // Price change  
        "P": "0.00",                // Price change percent  
        "w": "200.0000",            // Weighted average price  
        "c": "200.0000",            // Last price  
        "Q": "1.0000",              // Last quantity  
        "o": "200.0000",            // Open price  
        "h": "200.0000",            // High price  
        "l": "200.0000",            // Low price  
        "v": "9.0000",              // Trading volume(in contracts)  
        "q": "1800.0000",           // trade amount(in quote asset)   
        "O": 1764051060000,         // Statistics open time  
        "C": 1764080707933,         // Statistics close time  
        "F": 1,                     // First trade ID  
        "L": 22,                    // Last trade Id  
        "n": 9                      // Total number of trade  
    }

---

# 按交易对的Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时ticker信息.

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#url-path "URL PATH的直接链接")

`/public`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#stream-name "Stream Name的直接链接")

`<symbol>@optionTicker` 或 `<underlying>@optionTicker@<expiretionDate>` 如btcusdt@optionTicker@251230

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#更新速度 "更新速度的直接链接")

**1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#响应示例 "响应示例的直接链接")
    
    
    {  
        "e": "24hrTicker",          // 事件类型  
        "E": 1764080707933,         // 事件时间  
        "s": "ETH-251226-3000-C",   // 交易对  
        "p":"20",                   // 价格变化                   
        "P": "0.00",                // 价格变化百分比  
        "w": "200.0000",            // 平均价格  
        "c": "200.0000",            // 最新价  
        "Q": "1.0000",              // 最新成交价格上的成交量  
        "o": "200.0000",            // 开盘价  
        "h": "200.0000",            // 最高价  
        "l": "200.0000",            // 最低价  
        "v": "9.0000",              // 成交量张数  
        "q": "1800.0000",           // 成交金额  
        "O": 1764051060000,         // 统计开始时间  
        "C": 1764080707933,         // 统计结束时间  
        "F": 1,                     // 24小时内第一笔成交交易ID  
        "L": 22,                    // 24小时内最后一笔成交交易ID  
        "n": 9                      // 24小时内成交数  
    }