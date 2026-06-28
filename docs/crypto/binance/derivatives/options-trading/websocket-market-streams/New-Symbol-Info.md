---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info
api_type: WebSocket
updated_at: 2026-01-15T23:43:52.884455
---

# New Symbol Info

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#stream-description "Direct link to Stream Description")

New symbol listing stream.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#url-path "Direct link to URL PATH")

`/market`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#stream-name "Direct link to Stream Name")

`!optionSymbol`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#update-speed "Direct link to Update Speed")

**50ms**  

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#response-example "Direct link to Response Example")
    
    
    {  
        "e":"optionSymbol",             // Event Type  
        "E":1669356423908,              // Event Time  
        "s":"BTC-250926-140000-C",      // Symbol  
        "ps":"BTCUSDT",                 // Underlying index of the contract  
        "qa":"USDT",                    // Quotation asset  
        "d":"CALL",                     // Option type  
        "sp":"21000",                   // Strike price  
        "dt":4133404800000,             // Delivery date time  
        "u":1,                          // unit, the quantity of the underlying asset represented by a single contract.  
        "ot":1569398400000,             // onboard date time  
        "cs":"TRADING"                  // Contract status   
    }

---

# 新增交易对信息推送

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#数据流描述 "数据流描述的直接链接")

新增交易对推送。

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#url-path "URL PATH的直接链接")

`/market`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#stream-name "Stream Name的直接链接")

`!optionSymbol`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#更新速度 "更新速度的直接链接")

**50ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"optionSymbol",             // 事件类型     
        "E":1669356423908,              // 事件时间    
        "s":"BTC-250926-140000-C",      // 交易对  
        "ps":"BTCUSDT",                 // 标的资产   
        "qa":"USDT",                    // 计价资产    
        "d":"CALL",                     // 期权类型  
        "sp":"21000",                   // 行权价格  
        "dt":4133404800000,             // 行权时间   
        "u":1,                          // 一张合约代表的标的数量  
        "ot":1569398400000,             // 上币时间  
        "cs":"TRADING"                  // 合约状态  
    }