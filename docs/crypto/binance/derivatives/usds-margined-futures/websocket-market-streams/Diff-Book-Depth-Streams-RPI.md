---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI
api_type: WebSocket
updated_at: 2026-01-15T23:48:00.869728
---

# RPI Diff. Book Depth Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#stream-description "Direct link to Stream Description")

Bids and asks including RPI orders, pushed every 500 milliseconds

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#stream-name "Direct link to Stream Name")

`<symbol>@rpiDepth@500ms`

**Note** :

> RPI(Retail Price Improvement) orders are included and aggreated in the response message. When the quantity of a price level to be updated is equal to 0, it means either all quotations for this price have been filled/canceled, or the quantity of crossed RPI orders for this price are hidden

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#update-speed "Direct link to Update Speed")

**500ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#response-example "Direct link to Response Example")
    
    
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

# RPI增量深度信息

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#数据流描述 "数据流描述的直接链接")

orderbook 的变化部分，包含RPI订单，推送间隔 500 毫秒

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#stream-name "Stream Name的直接链接")

`<symbol>@rpiDepth@500ms`

**注意：** 响应消息包含RPI订单数量。如果增量数据的推送出现数量=0时，这意味着该价位的订单全部成交或者全部撤销，亦或该价位的RPI订单因价格交叉而隐藏

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#更新速度 "更新速度的直接链接")

**500ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#响应示例 "响应示例的直接链接")
    
    
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