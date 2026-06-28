---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:40:51.584910
---

# Mark Price Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#stream-description "Direct link to Stream Description")

Mark price update stream

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#stream-name "Direct link to Stream Name")

`<symbol>@markPrice` OR `<symbol>@markPrice@1s`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#update-speed "Direct link to Update Speed")

**3000ms** OR **1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#response-example "Direct link to Response Example")
    
    
    {  
    	"e":"markPriceUpdate",	// Event type  
      	"E":1596095725000,		// Event time  
       	"s":"BTCUSD_201225",	// Symbol  
      	"p":"10934.62615417",	// Mark Price  
      	"P":"10962.17178236",	// Estimated Settle Price, only useful in the last hour before the settlement starts.  
    	"i":"10933.62615417",   // Index Price   
      	"r":"",					// funding rate for perpetual symbol, "" will be shown for delivery symbol  
      	"T":0					// next funding time for perpetual symbol, 0 will be shown for delivery symbol  
    }

---

# 最新MarkPrice

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#数据流描述 "数据流描述的直接链接")

最新MarkPrice推送

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#stream-name "Stream Name的直接链接")

`<symbol>@markPrice` 或 `<symbol>@markPrice@1s`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#更新速度 "更新速度的直接链接")

**3000ms** 或 **1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream#响应示例 "响应示例的直接链接")
    
    
    {  
    	"e":"markPriceUpdate",	// 事件类型  
        "E":1596095725000,		// 事件时间  
        "s":"BTCUSD_201225",	// 交易对  
        "p":"10934.62615417",	// 标记价格  
        "P":"10962.17178236",	// 预估结算价,仅在结算前最后一小时有参考价值  
        "i":"10933.62615417",   // 指数价格  
        "r":"",					// 资金费率，对非永续合约显示""  
        "T":0				    // 下个资金时间,对非永续合约显示0  
    }