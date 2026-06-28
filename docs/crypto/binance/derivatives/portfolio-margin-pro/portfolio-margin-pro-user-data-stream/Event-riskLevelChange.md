---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange
api_type: REST
updated_at: 2026-01-15T23:44:31.789600
---

# Event: riskLevelChange

## Event Description[​](/docs/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange#event-description "Direct link to Event Description")

  * When the user's position risk ratio is too high, this stream will be pushed.
  * This message is only used as risk guidance information and is not recommended for investment strategies.
  * `RISK_LEVEL_CHANGE`includes following types：`MARGIN_CALL`, `REDUCE_ONLY`, `FORCE_LIQUIDATION`
  * In the case of a highly volatile market, there may be the possibility that the user's position has been liquidated at the same time when this stream is pushed out.



## Event Name[​](/docs/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange#event-name "Direct link to Event Name")

`RISK_LEVEL_CHANGE`

## Response Example[​](/docs/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange#response-example "Direct link to Response Example")
    
    
    {  
        "e":"riskLevelChange",      // Event Type  
        "E":1587727187525,      // Event Time  
        "u":"1.99999999",      // uniMMR level  
        "s":"MARGIN_CALL",        //MARGIN_CALL, REDUCE_ONLY, FORCE_LIQUIDATION   
        "eq":"30.23416728",      // account equity in USD value  
        "ae":"30.23416728",      // actual equity without collateral rate in USD value  
        "m":"15.11708371"      // total maintenance margin in USD value   
    }

---

# 账户风险状态变动

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange#事件描述 "事件描述的直接链接")

  * 当用户持仓风险过高，会推送此消息。
  * 此消息仅作为风险指导信息，不建议用于投资策略。
  * `RISK_LEVEL_CHANGE`包含如下事件：`MARGIN_CALL`, `REDUCE_ONLY`, `FORCE_LIQUIDATION`
  * 在大波动市场行情下,不排除此消息发出的同时用户仓位已被强平的可能。



## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange#事件类型 "事件类型的直接链接")

`RISK_LEVEL_CHANGE`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream/Event-riskLevelChange#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"riskLevelChange",  // 事件类型  
        "E":1587727187525,      // 事件时间  
        "u":"1.99999999",       // uniMMR  
        "s":"MARGIN_CALL",      //MARGIN_CALL, REDUCE_ONLY, FORCE_LIQUIDATION  
        "eq":"30.23416728",     // 账号美元保证金  
        "ae":"30.23416728",     // actual equity without collateral rate in USD value  
        "m":"15.11708371"       // 美元计价维持保证金  
    }