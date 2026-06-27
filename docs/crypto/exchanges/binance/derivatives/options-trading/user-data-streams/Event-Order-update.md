---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams/Event-Order-update
api_type: REST
updated_at: 2026-01-15T23:43:23.943523
---

# Event: Order update

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#event-description "Direct link to Event Description")

When new order created, order status changed will push such event. event type is `ORDER_TRADE_UPDATE`.

**Side**

  * BUY
  * SELL



**Order Type**

  * LIMIT



**Execution Type**

  * NEW
  * CANCELED
  * EXPIRED
  * TRADE



**Order Status**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED



**Time in force**

  * GTC
  * IOC
  * FOK
  * GTX



## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#event-name "Direct link to Event Name")

`ORDER_TRADE_UPDATE`

## Update Speed[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#response-example "Direct link to Response Example")
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",             // Event Type  
      "E":1568879465651,                    // Event Time  
      "T":1568879465650,                    // Transaction Time  
      "o":{                                  
        "s":"BTCUSDT",                      // Symbol  
        "c":"TEST",                         // Client Order Id  
          // special client order id:  
          // starts with "autoclose-": liquidation order  
          // "adl_autoclose": ADL auto close order  
        "S":"SELL",                          // Side  
        "o":"TRAILING_STOP_MARKET",          // Order Type  
        "f":"GTC",                           // Time in Force  
        "q":"0.001",                         // Original Quantity  
        "p":"0",                             // Original Price  
        "ap":"0",                            // Average Price  
        "x":"NEW",                           // Execution Type  
        "X":"NEW",                           // Order Status  
        "i":8886774,                         // Order Id  
        "l":"0",                             // Order Last Filled Quantity  
        "z":"0",                             // Order Filled Accumulated Quantity  
        "L":"0",                             // Last Filled Price  
        "N":"USDT",                          // Commission Asset  
        "n":"0",                             // Commission, negative means fee charge  
        "T":1568879465650,                   // Order Trade Time  
        "t":0,                               // Trade Id  
        "b":"0",                             // Bids qty  
        "a":"9.91",                          // Ask qty  
        "m":false,                           // Is this trade the maker side?  
        "R":false,                           // Is this reduce only  
        "ot":"TRAILING_STOP_MARKET",         // Original Order Type  
        "rp":"0",                            // Realized Profit of the trade  
      }  
    }

---

# 订单/交易 更新推送

## 事件描述[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Order-update#事件描述 "事件描述的直接链接")

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件,事件类型统一为 `ORDER_TRADE_UPDATE`

**订单方向**

  * BUY 买入
  * SELL 卖出



**订单类型**

  * LIMIT 限价单



**本次事件的具体执行类型**

  * NEW
  * CANCELED 已撤
  * EXPIRED 订单失效
  * TRADE 交易



**订单状态**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED



**有效方式:**

  * GTC
  * IOC
  * FOK
  * GTX



**强平和ADL:**

  * 若用户因保证金不足发生强平： 
    * `c`为"autoclose-XXX"，`X`为"NEW"
  * 若用户保证金充足但被 ADL: 
    * `c`为“adl_autoclose”，`X`为“NEW”



## URL PATH[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Order-update#url-path "URL PATH的直接链接")

`/private`

## 事件类型[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Order-update#事件类型 "事件类型的直接链接")

`ORDER_TRADE_UPDATE`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Order-update#更新速度 "更新速度的直接链接")

**50ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Order-update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",             // 事件类型  
      "E":1568879465651,                    // 事件时间  
      "T":1568879465650,                    // 交易时间  
      "o":{                                  
        "s":"BTCUSDT",                      // 交易对  
        "c":"TEST",                         // 客户端自定订单ID  
          // 特殊的自定义订单ID:  
          // "autoclose-"开头的字符串: 系统强平订单  
          // "adl_autoclose": ADL自动减仓订单  
        "S":"SELL",                          // 方向  
        "o":"TRAILING_STOP_MARKET",          // 订单类型  
        "f":"GTC",                           // 有效方式  
        "q":"0.001",                         // 订单原始数量  
        "p":"0",                             // 订单原始价格  
        "ap":"0",                            // 订单平均价格  
        "x":"NEW",                           // 本次事件的具体执行类型  
        "X":"NEW",                           // 订单的当前状态  
        "i":8886774,                         // 订单ID  
        "l":"0",                             // 订单末次成交量  
        "z":"0",                             // 订单累计已成交量  
        "L":"0",                             // 订单末次成交价格  
        "N":"USDT",                          // 手续费资产  
        "n":"0",                             // 手续费，负数代表手续费收取  
        "T":1568879465650,                   // 交易时间  
        "t":0,                               // 交易id  
        "b":"0",                             // 买单总数量  
        "a":"9.91",                          // 卖单总数量  
        "m":false,                           // 该成交是作为挂单成交  
        "R":false,                           // 是否是只减仓单  
        "ot":"TRAILING_STOP_MARKET",         // 原始订单类型  
        "rp":"0",                            // 该交易实现盈亏  
      }  
    }