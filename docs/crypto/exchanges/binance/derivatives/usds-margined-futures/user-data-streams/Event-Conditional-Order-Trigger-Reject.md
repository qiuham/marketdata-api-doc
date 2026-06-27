---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject
api_type: REST
updated_at: 2026-01-15T23:47:41.873444
---

# Event: Conditional_Order_Trigger_Reject

## Event Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#event-description "Direct link to Event Description")

`CONDITIONAL_ORDER_TRIGGER_REJECT` update when a triggered TP/SL order got rejected.

## Event Name[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#event-name "Direct link to Event Name")

`CONDITIONAL_ORDER_TRIGGER_REJECT`

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#response-example "Direct link to Response Example")
    
    
    {  
        "e":"CONDITIONAL_ORDER_TRIGGER_REJECT",      // Event Type  
        "E":1685517224945,      // Event Time  
        "T":1685517224955,      // me message send Time  
        "or":{  
          "s":"ETHUSDT",      // Symbol     
          "i":155618472834,      // orderId  
          "r":"Due to the order could not be filled immediately, the FOK order has been rejected. The order will not be recorded in the order history",      // reject reason  
         }  
    }

---

# 条件订单(TP/SL)触发后拒绝更新推送

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#事件描述 "事件描述的直接链接")

`CONDITIONAL_ORDER_TRIGGER_REJECT` 在止盈止损单触发后被拒绝时推送

## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#事件类型 "事件类型的直接链接")

`CONDITIONAL_ORDER_TRIGGER_REJECT`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"CONDITIONAL_ORDER_TRIGGER_REJECT",      // 事件类型  
        "E":1685517224945,      // 事件时间  
        "T":1685517224955,      // 撮合时间  
        "or":{  
          "s":"ETHUSDT",      // 交易对  
          "i":155618472834,      // 订单号  
          "r":"Due to the order could not be filled immediately, the FOK order has been rejected. The order will not be recorded in the order history",      // 拒绝原因  
         }  
    }