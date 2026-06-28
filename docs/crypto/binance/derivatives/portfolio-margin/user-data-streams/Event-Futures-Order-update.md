---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update
api_type: REST
updated_at: 2026-01-15T23:46:04.755264
---

# Event: Futures Order update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update#event-description "Direct link to Event Description")

When new order created, order status changed will push such event. event type is `ORDER_TRADE_UPDATE`.

**Side**

  * BUY
  * SELL



**Order Type**

  * MARKET
  * LIMIT
  * LIQUIDATION



**Execution Type**

  * NEW
  * CANCELED
  * CALCULATED - Liquidation Execution
  * EXPIRED
  * TRADE



**Order Status**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED
  * EXPIRED_IN_MATCH



**Time in force**

  * GTC
  * IOC
  * FOK
  * GTX



**Liquidation and ADL:**

  * If user gets liquidated due to insufficient margin balance: 
    * c shows as "autoclose-XXX"，X shows as "NEW"
  * If user has enough margin balance but gets ADL: 
    * c shows as “adl_autoclose”，X shows as “NEW”



## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update#event-name "Direct link to Event Name")

`ORDER_TRADE_UPDATE`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update#response-example "Direct link to Response Example")
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",     // Event Type    
      "fs": "UM",                   // Event business unit. 'UM' for USDS-M futures and 'CM' for COIN-M futures  
      "E":1568879465651,            // Event Time  
      "T":1568879465650,            // Transaction Time  
      "i":"",                   // Account Alias,ignore for UM  
      "o":{                              
        "s":"BTCUSDT",              // Symbol  
        "c":"TEST",                 // Client Order Id  
          // special client order id:  
          // starts with "autoclose-": liquidation order  
          // "adl_autoclose": ADL auto close order  
          // "settlement_autoclose-": settlement order for delisting or delivery  
        "S":"SELL",                 // Side  
        "o":"MARKET", // Order Type  
        "f":"GTC",                  // Time in Force  
        "q":"0.001",                // Original Quantity  
        "p":"0",                    // Original Price  
        "ap":"0",                   // Average Price  
        "sp":"7103.04",					    // Ignore  
        "x":"NEW",                  // Execution Type  
        "X":"NEW",                  // Order Status  
        "i":8886774,                // Order Id  
        "l":"0",                    // Order Last Filled Quantity  
        "z":"0",                    // Order Filled Accumulated Quantity  
        "L":"0",                    // Last Filled Price  
        "N":"USDT",             // Commission Asset, will not push if no commission  
        "n":"0",                // Commission, will not push if no commission  
        "T":1568879465650,          // Order Trade Time  
        "t":0,                      // Trade Id  
        "b":"0",                    // Bids Notional  
        "a":"9.91",                 // Ask Notional  
        "m":false,                  // Is this trade the maker side?  
        "R":false,                  // Is this reduce only  
        "ps":"LONG",                // Position Side  
        "rp":"0",                   // Realized Profit of the trade  
        "st":"C_TAKE_PROFIT",       // Strategy type, only pushed with conditional order triggered  
        "si":12893,                  // StrategyId,only pushed with conditional order triggered  
        "V":"EXPIRE_TAKER",         // STP mode  
        "gtd":0    
      }  
    }

---

# 合约订单/交易更新推送

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update#事件描述 "事件描述的直接链接")

当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件 事件类型统一为 `ORDER_TRADE_UPDATE`

**订单方向**

  * BUY 买入
  * SELL 卖出



**订单类型**

  * MARKET 市价单
  * LIMIT 限价单
  * STOP 止损单
  * TAKE_PROFIT 止盈单
  * LIQUIDATION 强平单



**本次事件的具体执行类型**

  * NEW
  * CANCELED 已撤
  * CALCULATED 订单 ADL 或爆仓
  * EXPIRED 订单失效
  * TRADE 交易



**订单状态**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED
  * EXPIRED_IN_MATCH



**有效方式:**

  * GTC
  * IOC
  * FOK
  * GTX



**强平和 ADL:**

  * 若用户因保证金不足发生强平： 
    * `c`为"autoclose-XXX"，`X`为"NEW"
  * 若用户保证金充足但被 ADL: 
    * `c`为“adl_autoclose”，`X`为“NEW”



## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update#事件类型 "事件类型的直接链接")

`ORDER_TRADE_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Futures-Order-update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",			// 事件类型  
      "E":1568879465651,				// 事件时间  
      "T":1568879465650,				// 撮合时间  
      "fs": "UM",                   // 事件业务线：'UM'代表U本位合约，'CM'代表币本位合约  
      "o":{								  
        "s":"BTCUSDT",					// 交易对  
        "c":"TEST",						// 客户端自定订单ID  
          // 特殊的自定义订单ID:  
          // "autoclose-"开头的字符串: 系统强平订单  
          // "adl_autoclose": ADL自动减仓订单  
          // "settlement_autoclose-": 下架或交割的结算订单  
        "S":"SELL",						// 订单方向  
        "o":"TRAILING_STOP_MARKET",	// 订单类型  
        "f":"GTC",						// 有效方式  
        "q":"0.001",					// 订单原始数量  
        "p":"0",						// 订单原始价格  
        "ap":"0",						// 订单平均价格  
        "sp":"7103.04",				// 忽略  
        "x":"NEW",						// 本次事件的具体执行类型  
        "X":"NEW",						// 订单的当前状态  
        "i":8886774,					// 订单ID  
        "l":"0",						// 订单末次成交量  
        "z":"0",						// 订单累计已成交量  
        "L":"0",						// 订单末次成交价格  
        "N": "USDT",           // 手续费资产类型  
        "n": "0",              // 手续费数量  
        "T":1568879465650,		 // 成交时间  
        "t":0,							   // 成交ID  
        "b":"0",						   // 买单净值  
        "a":"9.91",						 // 卖单净值  
        "m": false,					   // 该成交是作为挂单成交吗？  
        "R":false	,				     // 是否是只减仓单  
        "ps":"LONG"						 // 持仓方向  
        "rp":"0",					     // 该交易实现盈亏     
        "st":"C_TAKE_PROFIT",  // 策略单类型，仅在条件订单触发后会推送此字段  
        "si":12893,					   // 该交易实现盈亏，仅在条件订单触发后会推送此字段   
        "V":"EXPIRE_TAKER",         // STP mode  
        "gtd":0      
      }  
    }