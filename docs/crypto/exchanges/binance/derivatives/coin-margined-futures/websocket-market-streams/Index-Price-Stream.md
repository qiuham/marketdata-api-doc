---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:40:38.775368
---

# Index Price Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#stream-description "Direct link to Stream Description")

Index Price Stream

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#stream-name "Direct link to Stream Name")

`<pair>@indexPrice` OR `<pair>@indexPrice@1s`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#update-speed "Direct link to Update Speed")

**3000ms** OR **1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#response-example "Direct link to Response Example")
    
    
      {  
        "e": "indexPriceUpdate",  // Event type  
        "E": 1591261236000,       // Event time  
        "i": "BTCUSD",            // Pair  
        "p": "9636.57860000",     // Index Price  
      }

---

# 最新现货指数价格

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#数据流描述 "数据流描述的直接链接")

最新现货指数价格

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#stream-name "Stream Name的直接链接")

`<pair>@indexPrice` 或 `<pair>@indexPrice@1s`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#更新速度 "更新速度的直接链接")

**3000ms** 或 **1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#响应示例 "响应示例的直接链接")
    
    
      {  
        "e": "indexPriceUpdate",  // 事件类型  
        "E": 1591261236000,       // 事件时间  
        "i": "BTCUSD",            // 标的交易对  
        "p": "9636.57860000",   	// 指数价格  
      }