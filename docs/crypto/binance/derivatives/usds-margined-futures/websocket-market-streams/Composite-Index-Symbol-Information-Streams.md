---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:47:56.494872
---

# Composite Index Symbol Information Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#stream-description "Direct link to Stream Description")

Composite index information for index symbols pushed every second.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#stream-name "Direct link to Stream Name")

`<symbol>@compositeIndex`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#response-example "Direct link to Response Example")
    
    
    {  
      "e":"compositeIndex",		// Event type  
      "E":1602310596000,		// Event time  
      "s":"DEFIUSDT",			// Symbol  
      "p":"554.41604065",		// Price  
      "C":"baseAsset",  
      "c":[      				// Composition  
      	{  
      		"b":"BAL",			// Base asset  
      		"q":"USDT",         // Quote asset  
      		"w":"1.04884844",	// Weight in quantity  
      		"W":"0.01457800",   // Weight in percentage  
      		"i":"24.33521021"   // Index price  
      	},  
      	{  
      		"b":"BAND",  
      		"q":"USDT" ,  
      		"w":"3.53782729",  
      		"W":"0.03935200",  
      		"i":"7.26420084"  
        }  
      ]  
    }

---

# 综合指数交易对信息流

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#数据流描述 "数据流描述的直接链接")

获取交易对为综合指数的基础成分信息。 推送间隔1000毫秒(如有刷新)

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#stream-name "Stream Name的直接链接")

`<symbol>@compositeIndex`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#更新速度 "更新速度的直接链接")

**1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"compositeIndex",		// 事件类型  
      "E":1602310596000,		// 事件事件  
      "s":"DEFIUSDT",			// 交易对  
      "p":"554.41604065",		// 价格  
      "C":"baseAsset",  
      "c":[					// 成分信息  
      	{  
      		"b":"BAL",			// 基础资产  
      		"q":"USDT",         // 报价资产  
      		"w":"1.04884844",	// 权重(数量)  
      		"W":"0.01457800",   // 权重(比例)  
      		"i":"24.33521021"   // 指数价格  
      	},  
      	{  
      		"b":"BAND",  
      		"q":"USDT",          
      		"w":"3.53782729",  
      		"W":"0.03935200",  
      		"i":"7.26420084"  
        }  
      ]  
    }