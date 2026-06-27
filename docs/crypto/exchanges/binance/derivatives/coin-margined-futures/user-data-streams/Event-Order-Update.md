---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update
api_type: REST
updated_at: 2026-01-15T23:40:11.235299
---

# Event: Order Update

## Event Description[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update#event-description "Direct link to Event Description")

When new order created, modified, order status changed will push such event. event type is `ORDER_TRADE_UPDATE`.

**Side**

  * BUY
  * SELL



**Position side:**

  * BOTH
  * LONG
  * SHORT



**Order Type**

  * MARKET
  * LIMIT
  * STOP
  * TAKE_PROFIT
  * LIQUIDATION



**Execution Type**

  * NEW
  * CANCELED
  * CALCULATED - Liquidation Execution
  * EXPIRED
  * TRADE
  * AMENDMENT - Order Modified



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

    * `c` shows as "autoclose-XXX"，`X` shows as "NEW"
  * If user has enough margin balance but gets ADL:

    * `c` shows as “adl_autoclose”，`X` shows as “NEW”



**Expiry Reason**

  * `0`: None, the default value
  * `1`: Order has expired to prevent users from inadvertently trading against themselves
  * `2`: IOC order could not be filled completely, remaining quantity is canceled
  * `3`: IOC order could not be filled completely to prevent users from inadvertently trading against themselves, remaining quantity is canceled
  * `4`: Order has been canceled, as it's knocked out by another higher priority RO (market) order or reversed positions would be opened
  * `5`: Order has expired when the account was liquidated
  * `6`: Order has expired as GTE condition unsatisfied
  * `7`: Order has been canceled as the symbol is delisted
  * `8`: The initial order has expired after the stop order is triggered
  * `9`: Market order could not be filled completely, remaining quantity is canceled
  * `10`: FOK order could not be filled completely, the order is canceled
  * `11`: Order has been canceled, as it's failed Post-only check.



## Event Name[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update#event-name "Direct link to Event Name")

`ORDER_TRADE_UPDATE`

## Response Example[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",		  // Event Type  
      "E":1591274595442,		       	// Event Time  
      "T":1591274595442,		       	// Transaction Time  
      "i":"SfsR",					          // Account Alias  
      "o":{								  
        "s":"BTCUSD_200925",		    // Symbol  
        "c":"TEST",					        // Client Order Id  
          // special client order id:  
          // starts with "autoclose-": liquidation order  
          // "adl_autoclose": ADL auto close order  
          // "delivery_autoclose-": settlement order for delisting or delivery  
        "S":"SELL",					        // Side  
        "o":"TRAILING_STOP_MARKET",	// Order Type  
        "f":"GTC",				         	// Time in Force  
        "q":"2",				            // Original Quantity  
        "p":"0",					          // Original Price  
        "ap":"0",					          // Average Price  
        "sp":"9103.1",		       		// Stop Price. Please ignore with TRAILING_STOP_MARKET order  
        "x":"NEW",				         	// Execution Type  
        "X":"NEW",				         	// Order Status  
        "i":8888888,		         		// Order Id  
        "l":"0",				           	// Order Last Filled Quantity  
        "z":"0",					          // Order Filled Accumulated Quantity  
        "L":"0",					          // Last Filled Price  
        "ma": "BTC", 				        // Margin Asset  
        "N":"BTC",            		  // Commission Asset of the trade, will not push if no commission  
        "n":"0",               	    // Commission of the trade, will not push if no commission  
        "T":1591274595442,			    // Order Trade Time  
        "t":0,			        	      // Trade Id  
        "rp": "0",					        // Realized Profit of the trade  
        "b":"0",			    	        // Bid quantity of base asset  
        "a":"0",					          // Ask quantity of base asset  
        "m":false,					        // Is this trade the maker side?  
        "R":false,					        // Is this reduce only  
        "wt":"CONTRACT_PRICE", 		  // Stop Price Working Type  
        "ot":"TRAILING_STOP_MARKET",// Original Order Type  
        "ps":"LONG",				        // Position Side  
        "cp":false,					        // If Close-All, pushed with conditional order  
        "AP":"9476.8",				      // Activation Price, only puhed with TRAILING_STOP_MARKET order  
        "cr":"5.0",					        // Callback Rate, only puhed with TRAILING_STOP_MARKET order  
        "pP": false,				        // If conditional order trigger is protected  
        "V":"EXPIRE_TAKER",         // STP mode  
        "pm":"OPPONENT",            // Price match mode  
        "er":"0"                    // Expiry Reason  
      }  
    }

---

# 订单/交易更新推送

## 事件描述[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update#事件描述 "事件描述的直接链接")

当有新订单创建、修改、订单有新成交或者新的状态变化时会推送此类事件

**订单方向**

  * BUY 买入
  * SELL 卖出



**持仓方向:**

  * BOTH 单一持仓方向
  * LONG 多头(双向持仓下)
  * SHORT 空头(双向持仓下)



**订单类型**

  * MARKET 市价单
  * LIMIT 限价单
  * STOP 止损单
  * TAKE_PROFIT 止盈单



**本次事件的具体执行类型**

  * NEW
  * CANCELED 已撤
  * CALCULATED 强平单
  * EXPIRED 订单失效
  * TRADE 交易
  * AMENDMENT 订单修改



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



**强平和ADL:**

  * 若用户因保证金不足发生强平

    * `c`为"autoclose-XXX"，`X`为"NEW"
  * 若用户保证金充足但被ADL:

    * `c`为“adl_autoclose”，`X`为“NEW”



**过期原因**

  * `0`: 无，默认值
  * `1`: 自成交保护，订单被取消
  * `2`: IOC订单无法完全成交，订单被取消
  * `3`: IOC订单因自成交保护无法完全成交，订单被取消
  * `4`: 只减仓竞争过程中，低优先级的只减仓订单被取消
  * `5`: 账户强平过程中，订单被取消
  * `6`: 不满足GTE条件，订单被取消
  * `7`: Symbol下架，订单被取消
  * `8`: 止盈止损单触发后，初始订单被取消
  * `9`: 市价订单无法完全成交，订单被取消
  * `10`: FOK订单无法完全成交，订单被取消
  * `11`: 只做Maker订单会以Taker成交，订单被取消



## 事件类型[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update#事件类型 "事件类型的直接链接")

`ORDER_TRADE_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e":"ORDER_TRADE_UPDATE",		// 事件类型  
      "E":1568879465651,				  // 事件时间  
      "T":1568879465650,				  // 撮合时间  
      "i": "SfsR",							  // 账户唯一识别码 accountAlias  
      "o":{								  
        "s":"BTCUSD_200925",			// 交易对  
        "c":"TEST",						    // 客户端自定订单ID  
          // 特殊的自定义订单ID:  
          // "autoclose-"开头的字符串: 系统强平订单  
          // "delivery-"开头的字符串: 系统交割平仓单  
          // "delivery_autoclose-": 下架或交割的结算订单  
        "S":"SELL",						    // 订单方向  
        "o":"LIMIT",					    // 订单类型  
        "f":"GTC",						    // 有效方式  
        "q":"0.001",					    // 订单原始数量  
        "p":"9910",						    // 订单原始价格  
        "ap":"0",						      // 订单平均价格  
        "sp":"0",						      // 订单停止价格  
        "x":"NEW",						    // 本次事件的具体执行类型  
        "X":"NEW",						    // 订单的当前状态  
        "i":8886774,					    // 订单ID  
        "l":"0",						      // 订单末次成交量  
        "z":"0",						      // 订单累计已成交量  
        "L":"0",					        // 订单末次成交价格  
        "ma": "BTC", 					    // 保证金资产类型  
        "N": "BTC",               // 该成交手续费资产类型  
        "n": "0",                 // 该成交手续费数量  
        "T":1568879465650,				// 成交时间  
        "t":0,							      // 成交ID  
        "rp": "0",						    // 该成交已实现盈亏  
        "b":"0",						      // 买单净值  
        "a":"9.91",						    // 卖单净值  
        "m": false,					      // 该成交是作为挂单成交吗？  
        "R":false	,				        // 是否是只减仓单  
        "wt": "CONTRACT_PRICE",	  // 触发价类型  
        "ot": "LIMIT",					  // 原始订单类型  
        "ps":"LONG",						  // 持仓方向  
        "cp":false,						    // 是否为触发平仓单  
        "AP":"7476.89",					  // 追踪止损激活价格  
        "cr":"5.0",						    // 追踪止损回调比例  
        "pP": false						    // 是否开启条件单触发保护  
        "V":"EXPIRE_TAKER",       // 自成交防止模式  
        "pm":"OPPONENT",          // 价格匹配模式  
        "er":"0"                  // 过期原因  
      }  
    }