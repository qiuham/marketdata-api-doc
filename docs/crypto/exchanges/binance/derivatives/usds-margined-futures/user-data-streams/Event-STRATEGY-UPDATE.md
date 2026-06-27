---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE
api_type: REST
updated_at: 2026-01-15T23:47:45.930753
---

# Event: STRATEGY_UPDATE

## Event Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE#event-description "Direct link to Event Description")

`STRATEGY_UPDATE` update when a strategy is created/cancelled/expired, ...etc.

**Strategy Status**

  * NEW
  * WORKING
  * CANCELLED
  * EXPIRED



**opCode**

  * 8001: The strategy params have been updated
  * 8002: User cancelled the strategy
  * 8003: User manually placed or cancelled an order
  * 8004: The stop limit of this order reached
  * 8005: User position liquidated
  * 8006: Max open order limit reached
  * 8007: New grid order
  * 8008: Margin not enough
  * 8009: Price out of bounds
  * 8010: Market is closed or paused
  * 8011: Close position failed, unable to fill
  * 8012: Exceeded the maximum allowable notional value at current leverage
  * 8013: Grid expired due to incomplete KYC verification or access from a restricted jurisdiction
  * 8014: Violated Futures Trading Quantitative Rules. Strategy stopped
  * 8015: User position empty or liquidated



## Event Name[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE#event-name "Direct link to Event Name")

`STRATEGY_UPDATE`

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE#response-example "Direct link to Response Example")
    
    
    {  
    	"e": "STRATEGY_UPDATE", // Event Type  
    	"T": 1669261797627, // Transaction Time  
    	"E": 1669261797628, // Event Time  
    	"su": {  
    			"si": 176054594, // Strategy ID  
    			"st": "GRID", // Strategy Type  
    			"ss": "NEW", // Strategy Status  
    			"s": "BTCUSDT", // Symbol  
    			"ut": 1669261797627, // Update Time  
    			"c": 8007 // opCode  
    		}  
    }

---

# 策略交易更新推送

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE#事件描述 "事件描述的直接链接")

`STRATEGY_UPDATE` 在策略交易创建、取消、失效等等时候更新。

**策略状态**

  * NEW
  * WORKING
  * CANCELLED
  * EXPIRED



**opCode**

  * 8001: 策略参数更改
  * 8002: 用户取消策略
  * 8003: 用户手动新增或取消订单
  * 8004: 达到 stop limit
  * 8005: 用户仓位爆仓
  * 8006: 已达最大可挂单数量
  * 8007: 新增网格策略
  * 8008: 保证金不足
  * 8009: 价格超出范围
  * 8010: 市场非交易状态
  * 8011: 关仓失败，平仓单无法成交
  * 8012: 超过最大可交易名目金额
  * 8013: 不符合网格交易身份
  * 8014: 不符合 Futures Trading Quantitative Rules，策略终止
  * 8015: 无仓位或是仓位已经爆仓



## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE#事件类型 "事件类型的直接链接")

`STRATEGY_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-STRATEGY-UPDATE#响应示例 "响应示例的直接链接")
    
    
    {  
    	"e": "STRATEGY_UPDATE", // 事件类型  
    	"T": 1669261797627, // 撮合时间  
    	"E": 1669261797628, // 事件时间  
    	"su": {  
    			"si": 176054594, // 策略 ID  
    			"st": "GRID", // 策略类型  
    			"ss": "NEW", // 策略状态  
    			"s": "BTCUSDT", // 交易对  
    			"ut": 1669261797627, // 更新时间  
    			"c": 8007 // opCode  
    		}  
    }