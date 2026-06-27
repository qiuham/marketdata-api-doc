---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:48:04.772516
---

# Liquidation Order Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#stream-description "Direct link to Stream Description")

The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#stream-name "Direct link to Stream Name")

   `<symbol>@forceOrder`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#update-speed "Direct link to Update Speed")

1000ms

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#response-example "Direct link to Response Example")
    
    
    {  
      
    	"e":"forceOrder",                   // Event Type  
    	"E":1568014460893,                  // Event Time  
    	"o":{  
    	  
    		"s":"BTCUSDT",                   // Symbol  
    		"S":"SELL",                      // Side  
    		"o":"LIMIT",                     // Order Type  
    		"f":"IOC",                       // Time in Force  
    		"q":"0.014",                     // Original Quantity  
    		"p":"9910",                      // Price  
    		"ap":"9910",                     // Average Price  
    		"X":"FILLED",                    // Order Status  
    		"l":"0.014",                     // Order Last Filled Quantity  
    		"z":"0.014",                     // Order Filled Accumulated Quantity  
    		"T":1568014460893,          	 // Order Trade Time  
    	  
    	}  
      
    }

---

# 强平订单

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#数据流描述 "数据流描述的直接链接")

推送特定`symbol`的强平订单快照信息。 1000ms内至多仅推送一条最近的强平订单作为快照

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#stream-name "Stream Name的直接链接")

   `<symbol>@forceOrder`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#更新速度 "更新速度的��直接链接")

**1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      
    	"e":"forceOrder",                   // 事件类型  
    	"E":1568014460893,                  // 事件时间  
    	"o":{  
    		"s":"BTCUSDT",                   // 交易对  
    		"S":"SELL",                      // 订单方向  
    		"o":"LIMIT",                     // 订单类型  
    		"f":"IOC",                       // 有效方式  
    		"q":"0.014",                     // 订单数量  
    		"p":"9910",                      // 订单价格  
    		"ap":"9910",                     // 平均价格  
    		"X":"FILLED",                    // 订单状态  
    		"l":"0.014",                     // 订单最近成交量  
    		"z":"0.014",                     // 订单累计成交量  
    		"T":1568014460893,          	 // 交易时间  
    	}  
    }