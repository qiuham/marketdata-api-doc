---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/risk-data-stream/Event-Liability-Update
api_type: REST
updated_at: 2026-05-27 18:57:03.894244
---

# Payload: Margin Call

## Event Description[​](/docs/margin_trading/risk-data-stream/Event-Margin-Call#event-description "Direct link to Event Description")

Margin call trigger the event

## Event Name[​](/docs/margin_trading/risk-data-stream/Event-Margin-Call#event-name "Direct link to Event Name")

`MARGIN_LEVEL_STATUS_CHANGE`

## Response Example[​](/docs/margin_trading/risk-data-stream/Event-Margin-Call#response-example "Direct link to Response Example")
    
    
    {  
       "e": "MARGIN_LEVEL_STATUS_CHANGE", // Event Type  
       "E": 1701949763462, // Event Time  
       "l": "1.1", // margin level  
       "s": "MARGIN_CALL" // margin call status  
    }

---

# Margin Call事件

## 事件描述[​](/docs/zh-CN/margin_trading/risk-data-stream/Event-Margin-Call#事件描述 "事件描述的直接链接")

在用户 margin 账户发生 margin call 事件时,会推送此事件

## 事件类型[​](/docs/zh-CN/margin_trading/risk-data-stream/Event-Margin-Call#事件类型 "事件类型的直接��链接")

`MARGIN_LEVEL_STATUS_CHANGE`

## 响应示例[​](/docs/zh-CN/margin_trading/risk-data-stream/Event-Margin-Call#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "MARGIN_LEVEL_STATUS_CHANGE", // 事件类型  
      "E": 1701949763462, // 事件时间  
      "l": "1.1", // 杠杆账户风险率  
      "s": "MARGIN_CALL" // 杠杆账户状态为Margin Call  
    }