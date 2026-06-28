---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:40:32.052427
---

# All Market Liquidation Order Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#stream-description "Direct link to Stream Description")

The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#stream-name "Direct link to Stream Name")

`!forceOrder@arr`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#response-example "Direct link to Response Example")
    
    
    {  
    	"e":"forceOrder",                   // Event Type  
    	"E": 1591154240950,					// Event Time  
    	"o":{  
    		"s":"BTCUSD_200925", 		// Symbol  
    		"ps": "BTCUSD",					// Pair  
    		"S":"SELL",						// Side  
    		"o":"LIMIT",					// Order Type  
    		"f":"IOC",						// Time in Force  
    		"q":"1",						// Original Quantity  
    		"p":"9425.5",					// Price  
    		"ap":"9496.5",					// Average Price  
    		"X":"FILLED",					// Order Status  
    		"l":"1",						// Order Last Filled Quantity  
    		"z":"1",						// Order Filled Accumulated Quantity  
    		"T": 1591154240949,				// Order Trade Time  
    	  
    	}  
    }

---

# 全市场强平订单

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#数据流描述 "数据流描述的直接链接")

推送全市场强平订单快照信息 每个symbol，1000ms内至多仅推送一条最近的强平订单作为快照

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#stream-name "Stream Name的直接链接")

`!forceOrder@arr`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
    	"e":"forceOrder",             		// 事件类型  
    	"E": 1591154240950,					// 事件时间  
    	"o":{  
    		"s":"BTCUSD_200925", 			// 交易对  
    		"ps": "BTCUSD",					// 标的交易对  
    		"S":"SELL",						// 订单方向  
    		"o":"LIMIT",					// 订单类型  
    		"f":"IOC",						// 有效方式  
    		"q":"1",						// 订单数量  
    		"p":"9425.5",					// 订单价格  
    		"ap":"9496.5",					// 平均价格  
    		"X":"FILLED",					// 订单状态  
    		"l":"1",						// 订单最近成交量  
    		"z":"1",						// 订单累计成交量  
    		"T": 1591154240949,				// 交易时间  
    	}  
    }