---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update
api_type: REST
updated_at: 2026-01-15T23:47:41.736945
---

# Event: Algo Order Update

## Event Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update#event-description "Direct link to Event Description")

When new algo order created, order status changed will push such event. event type is `ALGO_UPDATE`.

**Algo Status**

  * `NEW`: This status indicates that the conditional order was successfully placed into the Algo Service but has not yet been triggered.
  * `CANCELED`: This status signifies that the conditional order has been canceled.
  * `TRIGGERING`: This status suggests that the order has met the triggering condition and has been forwarded to the matching engine.
  * `TRIGGERED`: This status means that the order has been successfully placed into the matching engine.
  * `FINISHED`: This status shows that the triggered conditional order has been filled or canceled in the matching engine.
  * `REJECTED`: This status signifies that the conditional order has been denied by the matching engine, such as in scenarios of margin check failures.
  * `EXPIRED`: This status denotes that the conditional order has been canceled by the system. An example would be when a user places a GTE_GTC Time-In-Force conditional order but then closes all positions on that symbol, resulting in system-led cancellation of the conditional order.



## Event Name[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update#event-name "Direct link to Event Name")

`ALGO_UPDATE`

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e":"ALGO_UPDATE",  // Event Type  
      "T":1750515742297,  // Event Time  
      "E":1750515742303,  // Transaction Time  
      "o":{  
        "caid":"Q5xaq5EGKgXXa0fD7fs0Ip",  // Client Algo Id  
        "aid":2148719,  // Algo Id  
        "at":"CONDITIONAL",  // Algo Type  
        "o":"TAKE_PROFIT",  //Order Type  
        "s":"BNBUSDT",  //Symbol  
        "S":"SELL",  //Side  
        "ps":"BOTH",  //Position Side  
        "f":"GTC",  //Time in force  
        "q":"0.01",  //quantity  
        "X":"CANCELED",  //Algo status  
        "ai":"",  // order id  
        "ap": "0.00000", // avg fill price in matching engine, only display when order is triggered and placed in matching engine  
        "aq": "0.00000", // execuated quantity in matching engine, only display when order is triggered and placed in matching engine  
        "act": "0", // actual order type in matching engine, only display when order is triggered and placed in matching engine  
        "tp":"750",  //Trigger price  
        "p":"750", //Order Price  
        "V":"EXPIRE_MAKER",  //STP mode  
        "wt":"CONTRACT_PRICE", //Working type  
        "pm":"NONE",  // Price match mode  
        "cp":false,  //If Close-All  
        "pP":false, //If price protection is turned on  
        "R":false,  // Is this reduce only  
        "tt":0,  //Trigger time  
        "gtd":0,  // good till time for GTD time in force  
        "rm": "Reduce Only reject"  // algo order failed reason  
      }  
    }

---

# 条件订单交易更新推送

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update#事件描述 "事件描述的直接链接")

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件 事件类型统一为 `ALGO_UPDATE`

**本次事件的具体执行类型**

  * NEW：该状态表示条件订单已提交，但尚未触发。
  * CANCELED：该状态表示条件订单已被取消。
  * TRIGGERING：该状态表示条件订单已满足触发条件，且已被转发至撮合引擎。
  * TRIGGERED：该状态表示条件订单已成功触发并成功进入撮合引擎。
  * FINISHED：该状态表示触发的条件订单已在撮合引擎中被成交或取消。
  * REJECTED：该状态表示条件订单被撮合引擎拒绝，例如保证金检查失败等情况。
  * EXPIRED：该状态表示条件订单被系统取消。例如，用户下了一个GTE_GTC时效条件订单，但随后关闭了该标的的所有持仓，系统因此取消了该条件订单。



## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update#事件类型 "事件类型的直接链接")

`ALGO_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"ALGO_UPDATE",  // 事件类型  
      "T":1750515742297,  // 事件时间  
      "E":1750515742303,  // 撮合时间  
      "o":{  
        "caid":"Q5xaq5EGKgXXa0fD7fs0Ip",  // 客户端自定条件订单ID  
        "aid":2148719,  // 条件单 Id  
        "at":"CONDITIONAL",  // 条件单类型  
        "o":"TAKE_PROFIT",  //订单类型  
        "s":"BNBUSDT",  //交易对  
        "S":"SELL",  //订单方向  
        "ps":"BOTH",  //持仓方向  
        "f":"GTC",  //有效方式  
        "q":"0.01",  //订单数量  
        "X":"CANCELED",  //条件单状态  
        "ai":"",  // 触发后普通订单 id  
        "ap": "0.00000", // 触发后在撮合引擎中实际订单的平均成交价格，仅在订单被触发并进入撮合引擎时显示  
        "aq": "0.00000", // 触发后在撮合引擎中实际订单已成交数量，仅当订单被触发并进入撮合引擎时显示  
        "act": "0", // 触发后在撮合引擎中实际的订单类型，仅当订单被触发并进入撮合引擎时显示  
        "tp":"750",  //条件单触发价格  
        "p":"750", //订单价格  
        "V":"EXPIRE_MAKER",  //自成交防止模式  
        "wt":"CONTRACT_PRICE", //触发价类型  
        "pm":"NONE",  // 价格匹配模式  
        "cp":false,  //是否为触发平仓单; 仅在条件订单情况下会推送此字段  
        "pP":false, //是否开启条件单触发保护  
        "R":false,  // 是否是只减仓单  
        "tt":0,  //触发时间  
        "gtd":0,       // TIF为GTD的订单自动取消时间  
        "rm": "Reduce Only reject"  // 条件单失败原因  
    }