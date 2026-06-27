---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:43:45.888696
---

# Index Price Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#stream-description "Direct link to Stream Description")

Underlying(e.g ETHUSDT) index stream.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#url-path "Direct link to URL PATH")

`/market`

**Stream Name:**  
`!index@arr`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "e":"indexPrice",  
            "E":1763092572229,  
            "s":"ETHUSDT",  
            "p":"3224.51976744"  
        },  
        {  
            "e": "indexPrice",     // event type  
            "E": 1763092572229,    // time  
            "s": "BTCUSDT",        // underlying symbol  
            "p": "99102.32326087"  // index price  
        }  
    ]

---

# 指数价格

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#数据流描述 "数据流描述的直接链接")

标的资产指数价格(如ETHUSDT).

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#url-path "URL PATH��的直接链接")

`/market`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#stream-name "Stream Name的直接链接")

`!index@arr`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#更新速度 "更新速度的直接链接")

**1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "e":"indexPrice",  
            "E":1763092572229,  
            "s":"ETHUSDT",  
            "p":"3224.51976744"  
        },  
        {  
            "e": "indexPrice",     // event type  
            "E": 1763092572229,    // time  
            "s": "BTCUSDT",        // underlying symbol  
            "p": "99102.32326087"  // index price  
        }  
    ]