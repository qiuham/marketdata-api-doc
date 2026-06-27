---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update
api_type: Trading
updated_at: 2026-01-15T23:46:04.556132
---

# Event: Conditional Order Trade Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update#event-description "Direct link to Event Description")

When new order created, order status changed will push such event. event type is `CONDITIONAL_ORDER_TRADE_UPDATE`.

**Side**

  * BUY
  * SELL



**Conditional Order Type**

  * STOP
  * TAKE_PROFIT
  * STOP_MARKET
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**Execution Type**

  * NEW
  * CANCELED
  * CALCULATED - Liquidation Execution
  * EXPIRED
  * TRADE



**Order Status**

  * NEW
  * CANCELED
  * EXPIRED
  * TRIGGERED
  * FINISHED



**Time in force**

  * GTC
  * IOC
  * FOK
  * GTX



## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update#event-name "Direct link to Event Name")

`CONDITIONAL_ORDER_TRADE_UPDATE`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update#response-example "Direct link to Response Example")
    
    
    {  
        "e": "CONDITIONAL_ORDER_TRADE_UPDATE", // Event Type  
        "T": 1669262908216,                    // Transaction Time  
        "E": 1669262908218,                    // Event Time  
        "fs": "UM",                            // Event business unit  
        "so": {               
                "s": "BTCUSDT",                // Symbol  
                "c":"TEST",                    // Strategy Client Order Id  
                "si": 176057039,               // Strategy ID  
                "S":"SELL",                    // Side  
                "st": "TRAILING_STOP_MARKET",  // Strategy Type  
                "f":"GTC",                     // Time in Force  
                "q":"0.001",                   //Quantity  
                "p":"0",                       //Price  
                "sp":"7103.04",                // Stop Price. Please ignore with TRAILING_STOP_MARKET order  
                "os":"NEW",                    // Strategy Order Status  
                "T":1568879465650,             // Order book Time  
                "ut": 1669262908216,           // Order update Time   
                "R":false,                     // Is this reduce only  
                "wt":"MARK_PRICE",             // Stop Price Working Type  
                "ps":"LONG",                   // Position Side  
                "cp":false,                    // If Close-All, pushed with conditional order  
                "AP":"7476.89",                // Activation Price, only pushed with TRAILING_STOP_MARKET order  
                "cr":"5.0",                    // Callback Rate, only puhed with TRAILING_STOP_MARKET order  
                "i":8886774,                   // Order Id  
                "V":"EXPIRE_TAKER",         // STP mode  
                "gtd":0  
            }  
    }

---

# 合约条件订单/交易更新推送

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update#事件描述 "事件描述的直接链接")

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件 事件类型统一为 `CONDITIONAL_ORDER_TRADE_UPDATE`

**订单方向**

  * BUY 买入
  * SELL 卖出



**条件订单类型**

  * STOP
  * TAKE_PROFIT
  * STOP_MARKET
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**本次事件的具体执行类型**

  * NEW
  * CANCELED 已撤
  * CALCULATED 订单 ADL 或爆仓
  * EXPIRED 订单失效
  * TRADE 交易



**订单状态**

  * NEW
  * CANCELED
  * EXPIRED
  * TRIGGERED
  * FINISHED



**有效方式:**

  * GTC
  * IOC
  * FOK
  * GTX



## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update#事件类型 "事件类型的直接链接")

`CONDITIONAL_ORDER_TRADE_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Conditional-Order-Trade-Update#响应示例 "响应示例的直接链接")
    
    
    {  
        "e": "CONDITIONAL_ORDER_TRADE_UPDATE", // 时间类型  
        "T": 1669262908216,                    // 交易时间  
        "E": 1669262908218,                    // 事件时间  
        "fs": "UM",                            // 业务线  
        "so": {               
                "s": "BTCUSDT",                // 交易对  
                "c":"TEST",                    // 用户自定义策略Id  
                "si": 176057039,               // 策略Id  
                "S":"SELL",                    // 方向  
                "st": "TRAILING_STOP_MARKET",  // 策略类型  
                "f":"GTC",                     // 生效时间  
                "q":"0.001",                   // 数量  
                "p":"0",                       // 价格  
                "sp":"7103.04",                // TPSL触发价  
                "os":"NEW",                    // 策略订单状态  
                "T":1568879465650,             // 订单  
                "ut": 1669262908216,           // Order update Time   
                "R":false,                     // 仅减仓  
                "wt":"MARK_PRICE",             // TPSL触发价格类型  
                "ps":"LONG",                   // 仓位方向  
                "cp":false,                    // 是否为触发平仓单; 仅在条件订单情况下会推送此字段  
                "AP":"7476.89",                // 追踪止损激活价格, 仅在追踪止损单时会推送此字段  
                "cr":"5.0",                    // 追踪止损回调比例, 仅在追踪止损单时会推送此字段  
                "i":8886774,                   // 订单Id  
                "V":"EXPIRE_TAKER",         // STP mode  
                "gtd":0  
            }  
    }