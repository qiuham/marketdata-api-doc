---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:43:53.006098
---

# Partial Book Depth Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Top **< levels>** bids and asks, Valid levels are **< levels>** are 5, 10, 20.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth<level>@100ms` or `<symbol>@depth<level>@500ms`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**100ms** or **500ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#response-example "Direct link to Response Example")
    
    
    {  
        "e": "depthUpdate",            // event type   
        "E": 1762866729459,            // event time  
        "T": 1762866729358,            // transaction time   
        "s": "BTC-251123-126000-C",    // Option symbol    
        "U": 465,                      // First update ID in event  
        "u": 465,                      // Final update ID in event  
        "pu": 464,                     // Final update Id in last stream(ie `u` in last stream)  
        "b": [                         // Buy order     
            [  
                "1100.000",            // Price  
                "0.6000"               // quantity  
            ]          
        ],  
        "a": [                         // Sell order     
            [  
                "1300.000",  
                "0.6000"  
            ]  
        ]  
    }

---

# 有限档深度信息

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#数据流描述 "数据流描述的直接链接")

推送有限档深度信息。levels表示几档买卖单信息, 可选5/10/20档

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#url-path "URL PATH的直接链接")

`/public`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Stream Name的直接链接")

`<symbol>@depth<level>@100ms`或`<symbol>@depth<level>@500ms`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#更新速度 "更新速度的直接链接")

**100ms** 或 **500ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
        "e": "depthUpdate",            // 时间类型  
        "E": 1762866729459,            // 事件时间  
        "T": 1762866729358,            // 撮合时间  
        "s": "BTC-251123-126000-C",    // 交易对  
        "U": 465,                      // 从上次推送至今新增的第一个 update Id  
        "u": 465,                      // 从上次推送至今新增的第一个 update Id  
        "pu": 464,                     // 上次推送的最后一个update Id(即上条消息的‘u’)  
        "b": [                         // 买方  
            [  
                "1100.000",  
                "0.6000"  
            ]          
        ],  
        "a": [                         // 卖方  
            [  
                "1300.000",  
                "0.6000"  
            ]  
        ]  
    }