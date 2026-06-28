---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:51.712666
---

# Partial Book Depth Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Top **< levels>** bids and asks, Valid **< levels>** are 5, 10, or 20.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth<levels>` OR `<symbol>@depth<levels>@500ms` OR `<symbol>@depth<levels>@100ms`.

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**250ms** , **500ms** or **100ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"depthUpdate",		// Event type  
      "E":1591269996801,		// Event time  
      "T":1591269996646,		// Transaction time  
      "s":"BTCUSD_200626",		// Symbol  
      "ps":"BTCUSD",			// Pair  
      "U":17276694,  
      "u":17276701,  
      "pu":17276678,  
      "b":[						// Bids to be updated  
        [  
          "9523.0",				// Price Level  
          "5"					// Quantity  
        ],  
        [  
          "9522.8",  
          "8"  
        ],  
        [  
          "9522.6",  
          "2"  
        ],  
        [  
          "9522.4",  
          "1"  
        ],  
        [  
          "9522.0",  
          "5"  
        ]  
      ],  
      "a":[						// Asks to be updated  
        [  
          "9524.6",				// Price level to be  
          "2"					// Quantity  
        ],  
        [  
          "9524.7",  
          "3"  
        ],  
        [  
          "9524.9",  
          "16"  
        ],  
        [  
          "9525.1",  
          "10"  
        ],  
        [  
          "9525.3",  
          "6"  
        ]  
      ]  
    }

---

# 有限档深度信息

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#数据流描述 "数据流描述的直接链接")

推送有限档深度信息。levels表示几档买卖单信息, 可选 5/10/20档

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Stream Name的直接链接")

`<symbol>@depth<levels>` 或 `<symbol>@depth<levels>@500ms` 或 `<symbol>@depth<levels>@100ms`.

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#更新速度 "更新速度的直接链接")

**250ms** 或 **500ms** 或 **100ms**

## Response Example[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams#response-example "Response Example的直接链接")
    
    
    {  
      "e":"depthUpdate",		// 事件类型  
      "E":1591269996801,		// 事件时间  
      "T":1591269996646,		// 撮合时间  
      "s":"BTCUSD_200626",		// 交易对  
      "ps":"BTCUSD",			// 标的交易对  
      "U":17276694,  
      "u":17276701,  
      "pu":17276678,  
      "b":[						// 买方  
        [  
          "9523.0",				// 价格  
          "5"					// 数量  
        ],  
        [  
          "9522.8",  
          "8"  
        ],  
        [  
          "9522.6",  
          "2"  
        ],  
        [  
          "9522.4",  
          "1"  
        ],  
        [  
          "9522.0",  
          "5"  
        ]  
      ],  
      "a":[						// 卖方  
        [  
          "9524.6",				// 价格  
          "2"					// 数量  
        ],  
        [  
          "9524.7",  
          "3"  
        ],  
        [  
          "9524.9",  
          "16"  
        ],  
        [  
          "9525.1",  
          "10"  
        ],  
        [  
          "9525.3",  
          "6"  
        ]  
      ]  
    }