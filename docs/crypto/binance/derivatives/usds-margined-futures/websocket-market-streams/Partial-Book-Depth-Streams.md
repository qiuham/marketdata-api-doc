---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:48:08.201202
---

# Partial Book Depth Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Top **< levels>** bids and asks, Valid **< levels>** are 5, 10, or 20.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth<levels>` OR `<symbol>@depth<levels>@500ms` OR `<symbol>@depth<levels>@100ms`.

**Note** :

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**250ms** , **500ms** or **100ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e": "depthUpdate", // Event type  
      "E": 1571889248277, // Event time  
      "T": 1571889248276, // Transaction time  
      "s": "BTCUSDT",  
      "U": 390497796,     // First update ID in event  
      "u": 390497878,     // Final update ID in event  
      "pu": 390497794,    // Final update Id in last stream(ie `u` in last stream)  
      "b": [              // Bids to be updated  
        [  
          "7403.89",      // Price Level to be updated  
          "0.002"         // Quantity  
        ],  
        [  
          "7403.90",  
          "3.906"  
        ],  
        [  
          "7404.00",  
          "1.428"  
        ],  
        [  
          "7404.85",  
          "5.239"  
        ],  
        [  
          "7405.43",  
          "2.562"  
        ]  
      ],  
      "a": [              // Asks to be updated  
        [  
          "7405.96",      // Price level to be  
          "3.340"         // Quantity  
        ],  
        [  
          "7406.63",  
          "4.525"  
        ],  
        [  
          "7407.08",  
          "2.475"  
        ],  
        [  
          "7407.15",  
          "4.800"  
        ],  
        [  
          "7407.20",  
          "0.175"  
        ]  
      ]  
    }

---

# 有限档深度信息

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#数据流描述 "数据流描述的直接链接")

推送有限档深度信息。levels表示几档买卖单信息, 可选 5/10/20档

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Stream Name的直接链接")

`<symbol>@depth<levels>` 或 `<symbol>@depth<levels>@500ms` 或 `<symbol>@depth<levels>@100ms`.

**注意：** 响应消息不包含RPI订单，其不可见。

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#更新速度 "更新速度的直接链接")

**250ms** 或 **500ms** 或 **100ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "depthUpdate", 			// 事件类型  
      "E": 1571889248277, 			// 事件时间  
      "T": 1571889248276, 			// 交易时间  
      "s": "BTCUSDT",  
      "U": 390497796,           // 从上次推送至今新增的第一个 update Id  
      "u": 390497878,           // 从上次推送至今新增的最后一个 update Id  
      "pu": 390497794,          // 上次推送的最后一个update Id(即上条消息的‘u’)  
      "b": [             				// 买方  
        [  
          "7403.89",  	  			// 价格  
          "0.002"     		  		// 数量  
        ],  
        [  
          "7403.90",  
          "3.906"  
        ],  
        [  
          "7404.00",  
          "1.428"  
        ],  
        [  
          "7404.85",  
          "5.239"  
        ],  
        [  
          "7405.43",  
          "2.562"  
        ]  
      ],  
      "a": [          				// 卖方  
        [  
          "7405.96",  				// 价格  
          "3.340"     				// 数量  
        ],  
        [  
          "7406.63",  
          "4.525"  
        ],  
        [  
          "7407.08",  
          "2.475"  
        ],  
        [  
          "7407.15",  
          "4.800"  
        ],  
        [  
          "7407.20",  
          "0.175"  
        ]  
      ]  
    }