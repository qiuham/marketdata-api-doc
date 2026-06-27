---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:38.588175
---

# Diff. Book Depth Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Bids and asks, pushed every 250 milliseconds, 500 milliseconds, or 100 milliseconds

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth` OR `<symbol>@depth@500ms` OR `<symbol>@depth@100ms`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**250ms** or **500ms** or **100ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e": "depthUpdate",			// Event type  
      "E": 1591270260907,			// Event time  
      "T": 1591270260891,			// Transction time  
      "s": "BTCUSD_200626",			// Symbol  
      "ps": "BTCUSD",				// Pair  
      "U": 17285681,				// First update ID in event  
      "u": 17285702,				// Final update ID in event  
      "pu": 17285675,				// Final update Id in last stream(ie `u` in last stream)  
      "b": [						// Bids to be updated  
        [  
          "9517.6",					// Price level to be updated  
          "10"						// Quantity  
        ]  
      ],  
      "a": [						// Asks to be updated  
        [  
          "9518.5",					// Price level to be updated  
          "45"						// Quantity  
        ]  
      ]  
    }

---

# 增量深度信息stream

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#数据流描述 "数据流描述的直接链接")

orderbook的变化部分，推送间隔250毫秒，500毫秒，100毫秒(如有刷新)

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-name "Stream Name的直接链接")

`<symbol>@depth` OR `<symbol>@depth@500ms` OR `<symbol>@depth@100ms`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#更新速度 "更新速度的直接链接")

**250ms** 或 **500ms** 或 **100ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "depthUpdate",			// 事件类型  
      "E": 1591270260907,			// 事件时间  
      "T": 1591270260891,			// 撮合时间  
      "s": "BTCUSD_200626",			// 交易对  
      "ps": "BTCUSD",				// 标的交易对  
      "U": 17285681,				// 从上次推送至今新增的第一个 update Id  
      "u": 17285702,				// 从上次推送至今新增的最后一个 update Id  
      "pu": 17285675,				// 上次推送的最后一个update Id(即上条消息的‘u’)  
      "b": [						// 变动的买单深度  
        [  
          "9517.6",					// 价格  
          "10"						// 数量  
        ]  
      ],  
      "a": [						// 变动的卖单深度  
        [  
          "9518.5",					// 价格  
          "45"						// 数量  
        ]  
      ]  
    }