---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:48:00.804225
---

# Diff. Book Depth Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Bids and asks, pushed every 250 milliseconds, 500 milliseconds, 100 milliseconds (if existing)

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth` OR `<symbol>@depth@500ms` OR `<symbol>@depth@100ms`

**Note** :

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**250ms** , **500ms** , **100ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e": "depthUpdate", // Event type  
      "E": 123456789,     // Event time  
      "T": 123456788,     // Transaction time   
      "s": "BTCUSDT",     // Symbol  
      "U": 157,           // First update ID in event  
      "u": 160,           // Final update ID in event  
      "pu": 149,          // Final update Id in last stream(ie `u` in last stream)  
      "b": [              // Bids to be updated  
        [  
          "0.0024",       // Price level to be updated  
          "10"            // Quantity  
        ]  
      ],  
      "a": [              // Asks to be updated  
        [  
          "0.0026",       // Price level to be updated  
          "100"          // Quantity  
        ]  
      ]  
    }

---

# 增量深度信息

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#数据流描述 "数据流描述的直接链接")

orderbook 的变化部分，推送间隔 250 毫秒,500 毫秒，100 毫秒(如有刷新)

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-name "Stream Name的直接链接")

` <symbol>@depth` OR `<symbol>@depth@500ms` OR `<symbol>@depth@100ms`

**注意：** 响应消息不包含RPI订单，其不可见。

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#更新速度 "更新速度的直接链接")

**250ms** 或 **500ms** 或 **100ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "depthUpdate", 	// 事件类型  
      "E": 123456789,     	// 事件时间  
      "T": 123456788,     	// 撮合时间  
      "s": "BNBUSDT",      	// 交易对  
      "U": 157,           	// 从上次推送至今新增的第一个 update Id  
      "u": 160,           	// 从上次推送至今新增的最后一个 update Id  
      "pu": 149,          	// 上次推送的最后一个update Id(即上条消息的‘u’)  
      "b": [              	// 变动的买单深度  
        [  
          "0.0024",       	// 价格  
          "10"           	// 数量  
        ]  
      ],  
      "a": [              	// 变动的卖单深度  
        [  
          "0.0026",       	// 价格  
          "100"          	// 数量  
        ]  
      ]  
    }