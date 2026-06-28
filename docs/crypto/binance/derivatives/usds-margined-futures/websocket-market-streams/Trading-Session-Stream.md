---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:48:08.260904
---

# Trading Session Stream

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#stream-description "Direct link to Stream Description")

Trading session information for the underlying assets of TradFi Perpetual contracts—covering the U.S. equity market and the commodity market—is updated every second. Trading session information for different underlying markets is pushed in separate messages. Session types for the equity market include "PRE_MARKET", "REGULAR", "AFTER_MARKET", "OVERNIGHT", and "NO_TRADING". Session types for the commodity market include "REGULAR" and "NO_TRADING".

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#stream-name "Direct link to Stream Name")

`tradingSession`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#update-speed "Direct link to Update Speed")

**1s**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#response-example "Direct link to Response Example")
    
    
      {  
        "e": "EquityUpdate",  	// Event type, can also be CommodityUpdate  
        "E": 1765244143062,     // Event time  
        "t": 1765242000000,   	// Session start time  
        "T": 1765270800000,		  // Session end time  
        "S": "OVERNIGHT"        // Session type  
      }

---

# 当前交易时段

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#数据流描述 "数据流描述的直接链接")

每秒返回统金融合约标的资产（美股市场及大宗商品市场）的当前交易时段信息。不同标的市场的交易时段信息由不同消息推送。美股市场的交易时段包括 "PRE_MARKET"、"REGULAR"、"AFTER_MARKET"、"OVERNIGHT" 及 "NO_TRADING"；大宗商品市场的交易时段包括 "REGULAR" 和 "NO_TRADING"。

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#stream-name "Stream Name的直接链接")

`tradingSession`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#更新速度 "更新速度的直接链接")

**1s**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#响应示例 "响应示例的直接链接")
    
    
      {  
        "e": "EquityUpdate",  	// 事件类型, 也可以是CommodityUpdate  
        "E": 1765244143062,     // 事件时间  
        "t": 1765242000000,   	// 交易时段开始时间  
        "T": 1765270800000,		  // 交易时段结束时间  
        "S": "OVERNIGHT"        // 交易时段类型  
      }