---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call
api_type: REST
updated_at: 2026-01-15T23:47:45.785256
---

# Event: Margin Call

## Event Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call#event-description "Direct link to Event Description")

  * When the user's position risk ratio is too high, this stream will be pushed.
  * This message is only used as risk guidance information and is not recommended for investment strategies.
  * In the case of a highly volatile market, there may be the possibility that the user's position has been liquidated at the same time when this stream is pushed out.



## Event Name[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call#event-name "Direct link to Event Name")

`MARGIN_CALL`

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call#response-example "Direct link to Response Example")
    
    
    {  
        "e":"MARGIN_CALL",    	// Event Type  
        "E":1587727187525,		// Event Time  
        "cw":"3.16812045",		// Cross Wallet Balance. Only pushed with crossed position margin call  
        "p":[					// Position(s) of Margin Call  
          {  
            "s":"ETHUSDT",		// Symbol  
            "ps":"LONG",		// Position Side  
            "pa":"1.327",		// Position Amount  
            "mt":"CROSSED",		// Margin Type  
            "iw":"0",			// Isolated Wallet (if isolated position)  
            "mp":"187.17127",	// Mark Price  
            "up":"-1.166074",	// Unrealized PnL  
            "mm":"1.614445"		// Maintenance Margin Required  
          }  
        ]  
    }

---

# 追加保证金通知

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call#事件描述 "事件描述的直接链接")

  * 当用户持仓风险过高，会推送此消息。
  * 此消息仅作为风险指导信息，不建议用于投资策略。
  * 在大波动市场行情下，不排除此消息发出的同时用户仓位已被强平的可能。



## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call#事件类型 "事件类型的直接链接")

`MARGIN_CALL`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Margin-Call#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"MARGIN_CALL",    	// 事件类型  
        "E":1587727187525,		// 事件时间  
        "cw":"3.16812045",		// 除去逐仓仓位保证金的钱包余额, 仅在全仓 margin call 情况下推送此字段  
        "p":[					// 涉及持仓  
          {  
            "s":"ETHUSDT",		// symbol  
            "ps":"LONG",		// 持仓方向  
            "pa":"1.327",		// 仓位  
            "mt":"CROSSED",		// 保证金模式  
            "iw":"0",			// 若为逐仓，仓位保证金  
            "mp":"187.17127",	// 标记价格  
            "up":"-1.166074",	// 未实现盈亏  
            "mm":"1.614445"		// 持仓需要的维持保证金  
          }  
        ]  
    }