---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market
api_type: WebSocket
updated_at: 2026-01-15T23:48:08.070890
---

# Mark Price Stream for All market

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#stream-description "Direct link to Stream Description")

Mark price and funding rate for all symbols pushed every 3 seconds or every second.

**Note** :

> TradFi symbols will be pushed through a seperate message.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#stream-name "Direct link to Stream Name")

`!markPrice@arr` or `!markPrice@arr@1s`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#update-speed "Direct link to Update Speed")

**3000ms** or **1000ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#response-example "Direct link to Response Example")
    
    
    [   
      {  
        "e": "markPriceUpdate",  	// Event type  
        "E": 1562305380000,      	// Event time  
        "s": "BTCUSDT",          	// Symbol  
        "p": "11185.87786614",   	// Mark price  
        "i": "11784.62659091"		// Index price  
        "P": "11784.25641265",		// Estimated Settle Price, only useful in the last hour before the settlement starts  
        "r": "0.00030000",       	// Funding rate  
        "T": 1562306400000       	// Next funding time  
      }  
    ]

---

# 全市场最新标记价格

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#数据流描述 "数据流描述的直接链接")

全市场最新标记价格

**注意：** 传统金融合约将通过单独的消息推送。

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#stream-name "Stream Name的直接链接")

`!markPrice@arr` 或 `!markPrice@arr@1s`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#更新速度 "更新速度的直接链接")

**3000ms** 或 **1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "e": "markPriceUpdate",  	// 事件类型  
        "E": 1562305380000,      	// 事件时间  
        "s": "BTCUSDT",          	// 交易对  
        "p": "11185.87786614",   	// 标记价格  
        "i": "11784.62659091"		// 现货指数价格  
        "P": "11784.25641265",		// 预估结算价,仅在结算前最后一小时有参考价值  
        "r": "0.00030000",       	// 资金费率  
        "T": 1562306400000       	// 下个资金时间  
      }  
    ]