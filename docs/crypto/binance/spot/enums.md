---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/enums
api_type: REST
updated_at: 2026-11-13 20:24:32.484579
---

# ENUM Definitions

This will apply for both REST API and WebSocket API.

## Symbol status (status)

  * `TRADING`
  * `END_OF_DAY`
  * `HALT`
  * `BREAK`
  * `CANCEL_ONLY`



## Account and Symbol Permissions (permissions)

  * `SPOT`
  * `MARGIN`
  * `LEVERAGED`
  * `TRD_GRP_002`
  * `TRD_GRP_003`
  * `TRD_GRP_004`
  * `TRD_GRP_005`
  * `TRD_GRP_006`
  * `TRD_GRP_007`
  * `TRD_GRP_008`
  * `TRD_GRP_009`
  * `TRD_GRP_010`
  * `TRD_GRP_011`
  * `TRD_GRP_012`
  * `TRD_GRP_013`
  * `TRD_GRP_014`
  * `TRD_GRP_015`
  * `TRD_GRP_016`
  * `TRD_GRP_017`
  * `TRD_GRP_018`
  * `TRD_GRP_019`
  * `TRD_GRP_020`
  * `TRD_GRP_021`
  * `TRD_GRP_022`
  * `TRD_GRP_023`
  * `TRD_GRP_024`
  * `TRD_GRP_025`



## Order status (status)

Status| Description  
---|---  
`NEW`| The order has been accepted by the engine.  
`PENDING_NEW`| The order is in a pending phase until the working order of an order list has been fully filled.  
`PARTIALLY_FILLED`| A part of the order has been filled.  
`FILLED`| The order has been completed.  
`CANCELED`| The order has been canceled by the user.  
`PENDING_CANCEL`| Currently unused  
`REJECTED`| The order was not accepted by the engine and not processed.  
`EXPIRED`| The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill)  or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance)  
`EXPIRED_IN_MATCH`| The order was expired by the exchange due to STP. (e.g. an order with `EXPIRE_TAKER` will match with existing orders on the book with the same account or same `tradeGroupId`)  
  
## Order List Status (listStatusType)

Status| Description  
---|---  
`RESPONSE`| This is used when the ListStatus is responding to a failed action. (E.g. order list placement or cancellation)  
`EXEC_STARTED`| The order list has been placed or there is an update to the order list status.  
`UPDATED`| The clientOrderId of an order in the order list has been changed.  
`ALL_DONE`| The order list has finished executing and thus is no longer active.  
  
## Order List Order Status (listOrderStatus)

Status| Description  
---|---  
`EXECUTING`| Either an order list has been placed or there is an update to the status of the list.  
`ALL_DONE`| An order list has completed execution and thus no longer active.  
`REJECT`| The List Status is responding to a failed action either during order placement or order canceled.  
  
## ContingencyType

  * `OCO`
  * `OTO`



## AllocationType

  * `SOR`



## Order types (orderTypes, type)

  * `LIMIT`
  * `MARKET`
  * `STOP_LOSS`
  * `STOP_LOSS_LIMIT`
  * `TAKE_PROFIT`
  * `TAKE_PROFIT_LIMIT`
  * `LIMIT_MAKER`



## Order Response Type (newOrderRespType)

  * `ACK`
  * `RESULT`
  * `FULL`



## Working Floor

  * `EXCHANGE`
  * `SOR`



## Order side (side)

  * `BUY`
  * `SELL`



## Time in force (timeInForce)

This sets how long an order will be active before expiration.

Status| Description  
---|---  
`GTC`| Good Til Canceled  An order will be on the book unless the order is canceled.  
`IOC`| Immediate Or Cancel  An order will try to fill the order as much as it can before the order expires.  
`FOK`| Fill or Kill  An order will expire if the full order cannot be filled upon execution.  
  
## Rate limiters (rateLimitType)

  * REQUEST_WEIGHT


    
    
    Code
    
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 6000
    }

  * ORDERS


    
    
    Code
    
    {
      "rateLimitType": "ORDERS",
      "interval": "SECOND",
      "intervalNum": 1,
      "limit": 10
    }

  * RAW_REQUESTS


    
    
    Code
    
    {
      "rateLimitType": "RAW_REQUESTS",
      "interval": "MINUTE",
      "intervalNum": 5,
      "limit": 61000
    }

## Rate limit intervals (interval)

  * SECOND
  * MINUTE
  * DAY



## STP Modes

Read [Self Trade Prevention (STP) FAQ](/en/docs/products/spot/faqs/stp_faq) to learn more.

  * `NONE`
  * `EXPIRE_MAKER`
  * `EXPIRE_TAKER`
  * `EXPIRE_BOTH`
  * `DECREMENT`
  * `TRANSFER`



## Execution types:

Status| Description  
---|---  
`NEW`| The order has been accepted into the engine.  
`CANCELED`| The order has been canceled by the user.  
`REPLACED`| The order has been amended.  
`REJECTED`| The order has been rejected and was not processed (e.g. Cancel Replace Orders wherein the new order placement is rejected but the request to cancel request succeeds.)  
`TRADE`| Part of the order or all of the order's quantity has filled.  
`EXPIRED`| The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill) or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance).  
`TRADE_PREVENTION`| The order has expired due to STP.  
  
## Execution Rules

  * `PRICE_RANGE`



## Expiry Reasons

Expiry Reason (`eR`)| Explanation  
---|---  
`NONE`| The order has not expired.  
`REJECTED`| A contingent order or an order that was part of an OTO was rejected by the matching engine when trying to place it on the order book. Common reasons are lack of funds and rejection by filters.  
`EXCHANGE_CANCELED`| The order was canceled by Binance.  
`OCO_TRIGGER`| An order that was part of an OCO pair was canceled because the other order of the pair started working or the entire OCO expired.  
`OTO_PHASE_ONE_EXPIRED`| The working order of the order list expired, thus expiring the entire order list.  
`UNFILLED_IOC_QUANTITY_EXPIRED`| The IOC order was not fully filled and thus expired.  
`UNFILLED_FOK_ORDER_EXPIRED`| The FOK order was not fully filled and thus expired.  
`INSUFFICIENT_LIQUIDITY`| There were not enough orders in the order book to match with this order.  
`EXECUTION_RULE_PRICE_RANGE_EXCEEDED`| The order attempted to trade at a price that would not meet the Price Range Execution Rule.  
`INSUFFICIENT_QUOTE_NOTIONAL_LIMIT`| The order's `quoteNotionalLimit` prevented the remaining quantity from executing or resting, so it expired. See [Quote Notional Limit](/en/docs/products/spot/faqs/quoteNotionalLimit).  
`EXHAUSTED`| The order was amended down to its filled quantity or less, so it expired.  
  
Was this page helpful?

Last modified on November 12, 2026

[Filters](/en/docs/products/spot/filters)[Errors](/en/docs/products/spot/errors)

---

# 枚举定义

这将适用于 REST API 和 WebSocket API。

## 交易对的状态（status）

  * `TRADING` \- 正常交易中
  * `END_OF_DAY` \- 收盘
  * `HALT` \- 交易终止(该交易对已下线)
  * `BREAK` \- 交易暂停
  * `CANCEL_ONLY` \- 仅可撤单



## 账户与交易对权限（permissions）

  * `SPOT` \- 现货
  * `MARGIN` \- 杠杆
  * `LEVERAGED` \- 杠杆代币
  * `TRD_GRP_002` \- 交易组 002
  * `TRD_GRP_003` \- 交易组 003
  * `TRD_GRP_004` \- 交易组 004
  * `TRD_GRP_005` \- 交易组 005
  * `TRD_GRP_006` \- 交易组 006
  * `TRD_GRP_007` \- 交易组 007
  * `TRD_GRP_008` \- 交易组 008
  * `TRD_GRP_009` \- 交易组 009
  * `TRD_GRP_010` \- 交易组 010
  * `TRD_GRP_011` \- 交易组 011
  * `TRD_GRP_012` \- 交易组 012
  * `TRD_GRP_013` \- 交易组 013
  * `TRD_GRP_014` \- 交易组 014
  * `TRD_GRP_015` \- 交易组 015
  * `TRD_GRP_016` \- 交易组 016
  * `TRD_GRP_017` \- 交易组 017
  * `TRD_GRP_018` \- 交易组 018
  * `TRD_GRP_019` \- 交易组 019
  * `TRD_GRP_020` \- 交易组 020
  * `TRD_GRP_021` \- 交易组 021
  * `TRD_GRP_022` \- 交易组 022
  * `TRD_GRP_023` \- 交易组 023
  * `TRD_GRP_024` \- 交易组 024
  * `TRD_GRP_025` \- 交易组 025



## 订单状态（status）

状态| 描述  
---|---  
`NEW`| 该订单被交易引擎接受。  
`PENDING_NEW`| 该订单处于待处理 (`PENDING`) 阶段，直到其所属订单列表（order list） 中的 `working order` 完全成交。  
`PARTIALLY_FILLED`| 部分订单已被成交。  
`FILLED`| 订单已完全成交。  
`CANCELED`| 用户撤销了订单。  
`PENDING_CANCEL`| 撤销中(目前并未使用)  
`REJECTED`| 订单没有被交易引擎接受，也没被处理。  
`EXPIRED`| 该订单根据订单类型的规则被取消（例如，没有成交的 LIMIT FOK 订单, LIMIT IOC 或部分成交的 MARKET 订单）或者被交易引擎取消（例如，在强平期间被取消的订单，在交易所维护期间被取消的订单）  
`EXPIRED_IN_MATCH`| 表示订单由于 STP 而过期。（例如，带有 `EXPIRE_TAKER` 的订单与账簿上同属相同帐户或相同 `tradeGroupId` 的现有订单匹配）  
  
## 订单列表（order list）状态 （状态类型集 listStatusType）

状态| 描述  
---|---  
`RESPONSE`| 在 ListStatus 用于响应失败的操作时会被使用。（例如，下订单列表或取消订单列表）  
`EXEC_STARTED`| 订单列表已被下达或订单列表状态有更新。  
`UPDATED`| 订单列表里的某个订单的 clientOrderId 被改变。  
`ALL_DONE`| 订单列表执行结束，因此不再处于活动状态。  
  
## 订单列表（order list）中的订单状态 （订单状态集 listOrderStatus）

状态| 描述  
---|---  
`EXECUTING`| 订单列表已被下达或订单列表状态有更新。  
`ALL_DONE`| 订单列表执行结束，因此不再处于活动状态。  
`REJECT`| 在 ListStatus 用于响应在下单阶段或取消订单列表期间的失败操作时会被使用，  
  
## 订单列表的类型

  * `OCO`
  * `OTO`



## 分配类型

  * `SOR`



## 订单类型（orderTypes, type）

  * `LIMIT` \- 限价单
  * `MARKET` \- 市价单
  * `STOP_LOSS` \- 止损单
  * `STOP_LOSS_LIMIT` \- 限价止损单
  * `TAKE_PROFIT` \- 止盈单
  * `TAKE_PROFIT_LIMIT` \- 限价止盈单
  * `LIMIT_MAKER` \- 限价做市单



## 订单返回类型 （newOrderRespType）

  * `ACK`
  * `RESULT`
  * `FULL`



## 工作平台

  * `EXCHANGE` \- 常规交易
  * `SOR` \- 智能订单路由



## 订单方向 (side)

  * `BUY` \- 买入
  * `SELL` \- 卖出



## 生效时间 （timeInForce）

这里定义了订单在失效前的有效时间。

状态| 描述  
---|---  
`GTC`| 成交为止  订单会一直有效，直到被成交或者取消。  
`IOC`| 无法立即成交的部分就撤销  订单在失效前会尽量多的成交。  
`FOK`| 无法全部立即成交就撤销  如果无法全部成交，订单会失效。  
  
## 速率限制种类（rateLimitType）

  * REQUEST_WEIGHT - 单位时间请求权重之和上限


    
    
    Code
    
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 6000
    }

  * ORDERS - 单位时间下单次数上限


    
    
    Code
    
    {
      "rateLimitType": "ORDERS",
      "interval": "SECOND",
      "intervalNum": 1,
      "limit": 10
    }

  * RAW_REQUESTS - 单位时间请求次数上限


    
    
    Code
    
    {
      "rateLimitType": "RAW_REQUESTS",
      "interval": "MINUTE",
      "intervalNum": 5,
      "limit": 61000
    }

## 速率限制间隔 （interval）

  * SECOND
  * MINUTE
  * DAY



## STP 模式

请参阅 [自我交易预防 (Self Trade Prevention - STP) 常见问题](/zh-CN/docs/products/spot/faqs/stp_faq)。

  * `NONE`
  * `EXPIRE_MAKER`
  * `EXPIRE_TAKER`
  * `EXPIRE_BOTH`
  * `DECREMENT`
  * `TRANSFER`



## 可能的执行类型:

状态| 描述  
---|---  
`NEW`| 新订单已被引擎接受。  
`CANCELED`| 订单被用户取消。  
`REPLACED`| 订单已被修改。  
`REJECTED`| 新订单被拒绝 （e.g. 在撤消挂单再下单时，其中新订单被拒绝但撤消挂单请求成功）。  
`TRADE`| 订单有新成交。  
`EXPIRED`| 订单已根据 Time In Force 参数的规则取消（e.g. 没有成交的 LIMIT FOK 订单或部分成交的 LIMIT IOC 订单）或者被交易所取消（e.g. 强平或维护期间取消的订单）。  
`TRADE_PREVENTION`| 订单因 STP 触发而过期。  
  
## 执行规则

  * `PRICE_RANGE`



## 过期原因

过期原因 (`eR`)| 说明  
---|---  
`NONE`| 订单未过期。  
`REJECTED`| 当尝试将条件单或OTO（One-Triggers-the-Other）订单放入订单簿时，被撮合引擎拒绝。常见原因包括资金不足和过滤器拒绝。  
`EXCHANGE_CANCELED`| 订单被币安取消。  
`OCO_TRIGGER`| OCO（One-Cancels-the-Other）订单对中的一个订单被取消，因为其另一个订单开始生效或整个OCO订单对过期。  
`OTO_PHASE_ONE_EXPIRED`| 订单列表中的生效订单过期，导致整个订单列表过期。  
`UNFILLED_IOC_QUANTITY_EXPIRED`| IOC（立即成交或取消）订单未完全成交，因此过期。  
`UNFILLED_FOK_ORDER_EXPIRED`| FOK（全部成交或取消）订单未完全成交，因此过期。  
`INSUFFICIENT_LIQUIDITY`| 订单簿中没有足够的订单与该订单匹配。  
`EXECUTION_RULE_PRICE_RANGE_EXCEEDED`| 订单尝试以不符合价格区间执行规则的价格进行交易。  
`INSUFFICIENT_QUOTE_NOTIONAL_LIMIT`| 订单的 `quoteNotionalLimit` 导致剩余数量无法成交或挂单，因此订单过期。参见 [报价资产名义价值上限](/zh-CN/docs/products/spot/faqs/quoteNotionalLimit)。  
`EXHAUSTED`| 订单数量被减少至等于或低于已成交数量，因此过期。  
  
此页面是否有帮助？

Last modified on November 12, 2026

[过滤器](/zh-CN/docs/products/spot/filters)[错误代码](/zh-CN/docs/products/spot/errors)