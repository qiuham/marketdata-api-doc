---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE
api_type: REST
updated_at: 2026-01-15T23:40:11.107833
---

# Event: GRID_UPDATE

## Event Description[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE#event-description "Direct link to Event Description")

`GRID_UPDATE` update when a sub order of a grid is filled or partially filled.

**Strategy Status**

  * NEW
  * WORKING
  * CANCELLED
  * EXPIRED



## Event Name[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE#event-name "Direct link to Event Name")

`GRID_UPDATE`

## Response Example[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE#response-example "Direct link to Response Example")
    
    
    {  
    	"e": "GRID_UPDATE", // Event Type  
    	"T": 1669262908216, // Transaction Time  
    	"E": 1669262908218, // Event Time  
    	"gu": {   
    			"si": 176057039, // Strategy ID  
    			"st": "GRID", // Strategy Type  
    			"ss": "WORKING", // Strategy Status  
    			"s": "BTCUSDT", // Symbol  
    			"r": "-0.00300716", // Realized PNL  
    			"up": "16720", // Unmatched Average Price  
    			"uq": "-0.001", // Unmatched Qty  
    			"uf": "-0.00300716", // Unmatched Fee  
    			"mp": "0.0", // Matched PNL  
    			"ut": 1669262908197 // Update Time  
    	}  
    }

---

# 网格更新推送

## 事件描述[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE#事件描述 "事件描述的直接链接")

`GRID_UPDATE` 在网格子订单有部份或是完全成交时更新。

**策略状态**

  * NEW
  * WORKING
  * CANCELLED
  * EXPIRED



## 事件类型[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE#事件类型 "事件类型的直接链接")

`GRID_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-GRID-UPDATE#响应示例 "响应示例的直接链接")
    
    
    {  
    	"e": "GRID_UPDATE", // 事件类型  
    	"T": 1669262908216, // 撮合时间  
    	"E": 1669262908218, // 事件时间  
    	"gu": {   
    			"si": 176057039, // 策略 ID  
    			"st": "GRID", // 策略类型  
    			"ss": "WORKING", // 策略状态  
    			"s": "BTCUSDT", // 交易对  
    			"r": "-0.00300716", // 已实现 PNL  
    			"up": "16720", // 未配对均价  
    			"uq": "-0.001", // 未配对数量  
    			"uf": "-0.00300716", // 未配对手续费  
    			"mp": "0.0", // 已配对 PNL  
    			"ut": 1669262908197 // 更新时间  
    	}  
    }