---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay
api_type: REST
updated_at: 2026-06-28 18:56:11.129007
---

# Public API Definitions

## Terminology[​](/docs/institutional_loan/common-definition#terminology "Direct link to Terminology")

These terms will be used throughout the documentation, so it is recommended especially for new users to read to help their understanding of the API.

  * `base asset` refers to the asset that is the `quantity` of a symbol. For the symbol BTCUSDT, BTC would be the `base asset.`
  * `quote asset` refers to the asset that is the `price` of a symbol. For the symbol BTCUSDT, USDT would be the `quote asset`.



## ENUM definitions[​](/docs/institutional_loan/common-definition#enum-definitions "Direct link to ENUM definitions")

**Symbol status (status):**

  * `PRE_TRADING`
  * `TRADING`
  * `POST_TRADING`
  * `END_OF_DAY`
  * `HALT`
  * `AUCTION_MATCH`
  * `BREAK`



**Account and Symbol Permissions (permissions):**

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



**Order status (status):**

Status| Description  
---|---  
`NEW`| The order has been accepted by the engine.  
`PARTIALLY_FILLED`| A part of the order has been filled.  
`FILLED`| The order has been completed.  
`CANCELED`| The order has been canceled by the user.  
`PENDING_CANCEL`| Currently unused  
`REJECTED`| The order was not accepted by the engine and not processed.  
`EXPIRED`| The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill) or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance)  
`EXPIRED_IN_MATCH`| The order was canceled by the exchange due to STP trigger. (e.g. an order with `EXPIRE_TAKER` will match with existing orders on the book with the same account or same `tradeGroupId`)  
  
**OCO Status (listStatusType):**

Status| Description  
---|---  
`RESPONSE`| This is used when the ListStatus is responding to a failed action. (E.g. Orderlist placement or cancellation)  
`EXEC_STARTED`| The order list has been placed or there is an update to the order list status.  
`ALL_DONE`| The order list has finished executing and thus no longer active.  
  
**OCO Order Status (listOrderStatus):**

Status| Description  
---|---  
`EXECUTING`| Either an order list has been placed or there is an update to the status of the list.  
`ALL_DONE`| An order list has completed execution and thus no longer active.  
`REJECT`| The List Status is responding to a failed action either during order placement or order canceled.)  
  
**ContingencyType**

  * `OCO`



**AllocationType**

  * `SOR`



**WorkingFloor**

  * `EXCHANGE`
  * `SOR`



**Order types (orderTypes, type):**

  * `LIMIT`
  * `MARKET`
  * `STOP_LOSS`
  * `STOP_LOSS_LIMIT`
  * `TAKE_PROFIT`
  * `TAKE_PROFIT_LIMIT`
  * `LIMIT_MAKER`



**Order Response Type (newOrderRespType):**

  * `ACK`
  * `RESULT`
  * `FULL`



**Order side (side):**

  * BUY
  * SELL



**Time in force (timeInForce):**

This sets how long an order will be active before expiration.

Status| Description  
---|---  
`GTC`| Good Til Canceled   
  
An order will be on the book unless the order is canceled.  
`IOC`| Immediate Or Cancel   
  
An order will try to fill the order as much as it can before the order expires.  
`FOK`| Fill or Kill   
  
An order will expire if the full order cannot be filled upon execution.  
  
**Kline/Candlestick chart intervals:**

s-> seconds; m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

  * 1s
  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



**Rate limiters (rateLimitType)**

> REQUEST_WEIGHT
    
    
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 6000  
        }  
    

> ORDERS
    
    
        {  
          "rateLimitType": "ORDERS",  
          "interval": "SECOND",  
          "intervalNum": 10,  
          "limit": 100  
        },  
        {  
          "rateLimitType": "ORDERS",  
          "interval": "DAY",  
          "intervalNum": 1,  
          "limit": 200000  
        }  
    

> RAW_REQUESTS
    
    
        {  
          "rateLimitType": "RAW_REQUESTS",  
          "interval": "MINUTE",  
          "intervalNum": 5,  
          "limit": 5000  
        }  
    

  * REQUEST_WEIGHT

  * ORDERS

  * RAW_REQUESTS




**Rate limit intervals (interval)**

  * SECOND
  * MINUTE
  * DAY



**Prefix definition of the parameter "clientOrderId"**

  * S05_xxxxx: The order triggered by delisted token. See delist announcement as detail information.
  * qs_xxxxx : The order trigerred by force liquidation.



* * *

# Filters

Filters define trading rules on a symbol or an exchange. Filters come in two forms: `symbol filters` and `exchange filters`.

## Symbol Filters[​](/docs/institutional_loan/common-definition#symbol-filters "Direct link to Symbol Filters")

### PRICE_FILTER[​](/docs/institutional_loan/common-definition#price_filter "Direct link to PRICE_FILTER")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "PRICE_FILTER",  
        "minPrice": "0.00000100",  
        "maxPrice": "100000.00000000",  
        "tickSize": "0.00000100"  
      }  
    

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

  * `minPrice` defines the minimum `price`/`stopPrice` allowed; disabled on `minPrice` == 0.
  * `maxPrice` defines the maximum `price`/`stopPrice` allowed; disabled on `maxPrice` == 0.
  * `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by; disabled on `tickSize` == 0.



Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

  * `price` >= `minPrice`
  * `price` <= `maxPrice`
  * `price` % `tickSize` == 0



### PERCENT_PRICE[​](/docs/institutional_loan/common-definition#percent_price "Direct link to PERCENT_PRICE")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "PERCENT_PRICE",  
        "multiplierUp": "1.3000",  
        "multiplierDown": "0.7000",  
        "avgPriceMins": 5  
      }  
    

The `PERCENT_PRICE` filter defines the valid range for the price based on the average of the previous trades. `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

In order to pass the `percent price`, the following must be true for `price`:

  * `price` <= `weightedAveragePrice` * `multiplierUp`
  * `price` >= `weightedAveragePrice` * `multiplierDown`



### PERCENT_PRICE_BY_SIDE[​](/docs/institutional_loan/common-definition#percent_price_by_side "Direct link to PERCENT_PRICE_BY_SIDE")

> **ExchangeInfo format:**
    
    
        {  
              "filterType": "PERCENT_PRICE_BY_SIDE",  
              "bidMultiplierUp": "1.2",  
              "bidMultiplierDown": "0.2",  
              "askMultiplierUp": "5",  
              "askMultiplierDown": "0.8",  
              "avgPriceMins": 1  
        }  
    

The `PERCENT_PRICE_BY_SIDE` filter defines the valid range for the price based on the average of the previous trades.  
  
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.   
  


There is a different range depending on whether the order is placed on the `BUY` side or the `SELL` side.

Buy orders will succeed on this filter if:

  * `Order price` <= `weightedAveragePrice` * `bidMultiplierUp`
  * `Order price` >= `weightedAveragePrice` * `bidMultiplierDown`



Sell orders will succeed on this filter if:

  * `Order Price` <= `weightedAveragePrice` * `askMultiplierUp`
  * `Order Price` >= `weightedAveragePrice` * `askMultiplierDown`



### LOT_SIZE[​](/docs/institutional_loan/common-definition#lot_size "Direct link to LOT_SIZE")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
      }  
    

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity`/`icebergQty` allowed.
  * `maxQty` defines the maximum `quantity`/`icebergQty` allowed.
  * `stepSize` defines the intervals that a `quantity`/`icebergQty` can be increased/decreased by.



In order to pass the `lot size`, the following must be true for `quantity`/`icebergQty`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



### MIN_NOTIONAL[​](/docs/institutional_loan/common-definition#min_notional "Direct link to MIN_NOTIONAL")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "MIN_NOTIONAL",  
        "minNotional": "0.00100000",  
        "applyToMarket": true,  
        "avgPriceMins": 5  
      }  
    

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the `price` * `quantity`. If the order is an Algo order (e.g. `STOP_LOSS_LIMIT`), then the notional value of the `stopPrice` * `quantity` will also be evaluated. If the order is an Iceberg Order, then the notional value of the `price` * `icebergQty` will also be evaluated. `applyToMarket` determines whether or not the `MIN_NOTIONAL` filter will also be applied to `MARKET` orders. Since `MARKET` orders have no price, the average price is used over the last `avgPriceMins` minutes. `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

### NOTIONAL[​](/docs/institutional_loan/common-definition#notional "Direct link to NOTIONAL")

> **ExchangeInfo format:**
    
    
    {  
       "filterType": "NOTIONAL",  
       "minNotional": "10.00000000",  
       "applyMinToMarket": false,  
       "maxNotional": "10000.00000000",  
       "applyMaxToMarket": false,  
       "avgPriceMins": 5  
    }  
    

The `NOTIONAL` filter defines the acceptable notional range allowed for an order on a symbol.   
  
  
  
`applyMinToMarket` determines whether the `minNotional` will be applied to `MARKET` orders.   
  
`applyMaxToMarket` determines whether the `maxNotional` will be applied to `MARKET` orders.

In order to pass this filter, the notional (`price * quantity`) has to pass the following conditions:

  * `price * quantity` <= `maxNotional`
  * `price * quantity` >= `minNotional`



For `MARKET` orders, the average price used over the last `avgPriceMins` minutes will be used for calculation.   
  
If the `avgPriceMins` is 0, then the last price will be used.

### ICEBERG_PARTS[​](/docs/institutional_loan/common-definition#iceberg_parts "Direct link to ICEBERG_PARTS")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "ICEBERG_PARTS",  
        "limit": 10  
      }  
    

The `ICEBERG_PARTS` filter defines the maximum parts an iceberg order can have. The number of `ICEBERG_PARTS` is defined as `CEIL(qty / icebergQty)`.

### MARKET_LOT_SIZE[​](/docs/institutional_loan/common-definition#market_lot_size "Direct link to MARKET_LOT_SIZE")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "MARKET_LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
      }  
    

The `MARKET_LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for `MARKET` orders on a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity` allowed.
  * `maxQty` defines the maximum `quantity` allowed.
  * `stepSize` defines the intervals that a `quantity` can be increased/decreased by.



In order to pass the `market lot size`, the following must be true for `quantity`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



### MAX_NUM_ORDERS[​](/docs/institutional_loan/common-definition#max_num_orders "Direct link to MAX_NUM_ORDERS")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "MAX_NUM_ORDERS",  
        "maxNumOrders": 25  
      }  
    

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol. Note that both "algo" orders and normal orders are counted for this filter.

### MAX_NUM_ALGO_ORDERS[​](/docs/institutional_loan/common-definition#max_num_algo_orders "Direct link to MAX_NUM_ALGO_ORDERS")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 5  
      }  
    

The `MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol. "Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

### MAX_NUM_ICEBERG_ORDERS[​](/docs/institutional_loan/common-definition#max_num_iceberg_orders "Direct link to MAX_NUM_ICEBERG_ORDERS")

The `MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of `ICEBERG` orders an account is allowed to have open on a symbol. An `ICEBERG` order is any order where the `icebergQty` is > 0.

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "MAX_NUM_ICEBERG_ORDERS",  
        "maxNumIcebergOrders": 5  
      }  
    

### MAX_POSITION[​](/docs/institutional_loan/common-definition#max_position "Direct link to MAX_POSITION")

The `MAX_POSITION` filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

  1. free balance of the base asset
  2. locked balance of the base asset
  3. sum of the qty of all open BUY orders



`BUY` orders will be rejected if the account's position is greater than the maximum position allowed.

If an order's `quantity` can cause the position to overflow, this will also fail the `MAX_POSITION` filter.

> **ExchangeInfo format:**
    
    
    {  
      "filterType":"MAX_POSITION",  
      "maxPosition":"10.00000000"  
    }  
    

### TRAILING_DELTA[​](/docs/institutional_loan/common-definition#trailing_delta "Direct link to TRAILING_DELTA")

> **ExchangeInfo format:**
    
    
        {  
              "filterType": "TRAILING_DELTA",  
              "minTrailingAboveDelta": 10,  
              "maxTrailingAboveDelta": 2000,  
              "minTrailingBelowDelta": 10,  
              "maxTrailingBelowDelta": 2000  
       }  
    

The `TRAILING_DELTA` filter defines the minimum and maximum value for the parameter `trailingDelta`.

In order for a trailing stop order to pass this filter, the following must be true:

For `STOP_LOSS BUY`, `STOP_LOSS_LIMIT_BUY`,`TAKE_PROFIT SELL` and `TAKE_PROFIT_LIMIT SELL` orders:

  * `trailingDelta` >= `minTrailingAboveDelta`
  * `trailingDelta` <= `maxTrailingAboveDelta`



For `STOP_LOSS SELL`, `STOP_LOSS_LIMIT SELL`, `TAKE_PROFIT BUY`, and `TAKE_PROFIT_LIMIT BUY` orders:

  * `trailingDelta` >= `minTrailingBelowDelta`
  * `trailingDelta` <= `maxTrailingBelowDelta`



## Exchange Filters[​](/docs/institutional_loan/common-definition#exchange-filters "Direct link to Exchange Filters")

### EXCHANGE_MAX_NUM_ORDERS[​](/docs/institutional_loan/common-definition#exchange_max_num_orders "Direct link to EXCHANGE_MAX_NUM_ORDERS")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "EXCHANGE_MAX_NUM_ORDERS",  
        "maxNumOrders": 1000  
      }  
    

The `EXCHANGE_MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on the exchange. Note that both "algo" orders and normal orders are counted for this filter.

### EXCHANGE_MAX_NUM_ALGO_ORDERS[​](/docs/institutional_loan/common-definition#exchange_max_num_algo_orders "Direct link to EXCHANGE_MAX_NUM_ALGO_ORDERS")

> **ExchangeInfo format:**
    
    
      {  
        "filterType": "EXCHANGE_MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 200  
      }  
    

The `EXCHANGE_MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on the exchange. "Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

### EXCHANGE_MAX_NUM_ICEBERG_ORDERS[​](/docs/institutional_loan/common-definition#exchange_max_num_iceberg_orders "Direct link to EXCHANGE_MAX_NUM_ICEBERG_ORDERS")

The `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of iceberg orders an account is allowed to have open on the exchange.

> **ExchangeInfo format:**
    
    
    {  
      "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",  
      "maxNumIcebergOrders": 10000  
    }

---

# 公开 API 参数

## 术语[​](/docs/zh-CN/institutional_loan/common-definition#术语 "术语的直接链接")

这里的术语适用于全部文档，建议特别是新手熟读，也便于理解。

  * `base asset` 指一个交易对的交易对象，即写在靠前部分的资产名, 比如`BTCUSDT`, `BTC`是`base asset`。
  * `quote asset` 指一个交易对的定价资产，即写在靠后部分的资产名, 比如`BTCUSDT`, `USDT`是`quote asset`。



## 枚举定义[​](/docs/zh-CN/institutional_loan/common-definition#枚举定义 "枚举定义的直接链接")

**交易对状态 (状态 status):**

  * `PRE_TRADING` 交易前
  * `TRADING` 交易中
  * `POST_TRADING` 交易后
  * `END_OF_DAY`
  * `HALT`
  * `AUCTION_MATCH`
  * `BREAK`



**交易对类型:**

  * `SPOT` 现货
  * `MARGIN` 杠杆
  * `LEVERAGED` 杠杆代币
  * `TRD_GRP_002` 交易组 002
  * `TRD_GRP_003` 交易组 003
  * `TRD_GRP_004` 交易组 004
  * `TRD_GRP_005` 交易组 005
  * `TRD_GRP_006` 交易组 006
  * `TRD_GRP_007` 交易组 007
  * `TRD_GRP_008` 交易组 008
  * `TRD_GRP_009` 交易组 009
  * `TRD_GRP_010` 交易组 010
  * `TRD_GRP_011` 交易组 011
  * `TRD_GRP_012` 交易组 012
  * `TRD_GRP_013` 交易组 013
  * `TRD_GRP_014` 交易组 014



**订单状态 (状态 status):**

状态| 描述  
---|---  
`NEW`| 订单被交易引擎接  
`PARTIALLY_FILLED`| 部分订单被成交  
`FILLED`| 订单完全成交  
`CANCELED`| 用户撤销了订单  
`PENDING_CANCEL`| 撤销中（目前并未使用）  
`REJECTED`| 订单没有被交易引擎接受，也没被处理  
`EXPIRED`| 订单被交易引擎取消，比如：  
  
LIMIT FOK 订单没有成交  
  
市价单没有完全成交  
  
强平期间被取消的订单  
  
交易所维护期间被取消的订单  
`EXPIRED_IN_MATCH`| 表示订单由于 STP 触发而过期 （e.g. 带有 `EXPIRE_TAKER` 的订单与订单簿上属于同账户或同 `tradeGroupId` 的订单撮合）  
  
**OCO 状态 (状态类型集 listStatusType):**

状态| 描述  
---|---  
`RESPONSE`| 当ListStatus响应失败的操作时使用。 (订单完成或取消订单)  
`EXEC_STARTED`| 当已经下单或者订单有更新时  
`ALL_DONE`| 当订单执行结束或者不在激活状态  
  
**OCO 订单状态 (订单状态集 listOrderStatus):**

状态| 描述  
---|---  
`EXECUTING`| 当已经下单或者订单有更新时  
`ALL_DONE`| 当订单执行结束或者不在激活状态  
`REJECT`| 当订单状态响应失败(订单完成或取消订单)  
  
**指定订单的类型**

  * `OCO` 选择性委托订单



**分配类型 (allocationtype, type):**

  * `SOR` 智能订单路由



**工作平台**

  * `EXCHANGE` \- 常规交易
  * `SOR` \- 智能订单路由



**订单类型 (orderTypes, type):**

  * `LIMIT` 限价单
  * `MARKET` 市价单
  * `STOP_LOSS` 止损单
  * `STOP_LOSS_LIMIT` 限价止损单
  * `TAKE_PROFIT` 止盈单
  * `TAKE_PROFIT_LIMIT` 限价止盈单
  * `LIMIT_MAKER` 限价只挂单



**订单返回类型 (newOrderRespType):**

  * `ACK`
  * `RESULT`
  * `FULL`



**订单方向 (方向 side):**

  * `BUY` 买入
  * `SELL` 卖出



**有效方式 (timeInForce):**

这里定义了订单多久能够失效

状态| 描述  
---|---  
`GTC`| 成交为止   
  
订单会一直有效，直到被成交或者取消。  
`IOC`| 无法立即成交的部分就撤销   
  
订单在失效前会尽量多的成交。  
`FOK`| 无法全部立即成交就撤销   
  
如果无法全部成交，订单会失效。  
  
**K线间隔:**

s -> 秒; m -> 分钟; h -> 小时; d -> 天; w -> 周; M -> 月

  * 1s
  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



**限制种类 (rateLimitType)**

> REQUEST_WEIGHT
    
    
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 6000  
        }  
    

> ORDERS
    
    
        {  
          "rateLimitType": "ORDERS",  
          "interval": "SECOND",  
          "intervalNum": 10,  
          "limit": 100  
        },  
        {  
          "rateLimitType": "ORDERS",  
          "interval": "DAY",  
          "intervalNum": 1,  
          "limit": 200000  
        }  
    

> RAW_REQUESTS
    
    
        {  
          "rateLimitType": "RAW_REQUESTS",  
          "interval": "MINUTE",  
          "intervalNum": 5,  
          "limit": 5000  
        }  
    

  * REQUEST_WEIGHT 单位时间请求权重之和上限

  * ORDERS 单位时间下单次数限制

  * RAW_REQUESTS 单位时间请求次数上限




**限制间隔 (interval)**

  * SECOND 秒
  * MINUTE 分
  * DAY 天



# 过滤器

过滤器，即Filter，定义了一系列交易规则。 共有两类，分别是针对交易对的过滤器`symbol filters`，和针对整个交易所的过滤器 `exchange filters`

## 交易对过滤器[​](/docs/zh-CN/institutional_loan/common-definition#交易对过滤器 "交易对过滤器的直接链接")

### PRICE_FILTER 价格过滤器[​](/docs/zh-CN/institutional_loan/common-definition#price_filter-价格过滤器 "PRICE_FILTER 价格过滤器的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "PRICE_FILTER",  
        "minPrice": "0.00000100",  
        "maxPrice": "100000.00000000",  
        "tickSize": "0.00000100"  
      }  
    

`价格过滤器` 用于检测订单中 `price` 参数的合法性。包含以下三个部分:

  * `minPrice` 定义了 `price`/`stopPrice` 允许的最小值。
  * `maxPrice` 定义了 `price`/`stopPrice` 允许的最大值。
  * `tickSize` 定义了 `price`/`stopPrice` 的步进间隔，即price必须等于minPrice+(tickSize的整数倍)



以上每一项均可为0，为0时代表这一项不再做限制。

逻辑伪代码如下:

  * `price` >= `minPrice`
  * `price` <= `maxPrice`
  * `price` % `tickSize` == 0



### PERCENT_PRICE 价格振幅过滤器[​](/docs/zh-CN/institutional_loan/common-definition#percent_price-价格振幅过滤器 "PERCENT_PRICE 价格振幅过滤器的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "PERCENT_PRICE",  
        "multiplierUp": "5",  
        "multiplierDown": "0.2",  
        "avgPriceMins": 5  
      }  
    

`PERCENT_PRICE`过滤器基于先前交易的平均值来定义价格的有效范围。  
`avgPriceMins`是计算平均价格的分钟数。 0表示使用最后的价格。

为了通过"价格百分比"，"价格"必须符合以下条件：

  * `price` <=`weightedAveragePrice` *`multiplierUp`
  * `price`> =`weightedAveragePrice` *`multiplierDown`



### PERCENT_PRICE_BY_SIDE 基于买卖方向的价格振幅过滤器[​](/docs/zh-CN/institutional_loan/common-definition#percent_price_by_side-基于买卖方向的价格振幅过滤器 "PERCENT_PRICE_BY_SIDE 基于买卖方向的价格振幅过滤器的直接链接")

> **ExchangeInfo format:**
    
    
        {  
              "filterType": "PERCENT_PRICE_BY_SIDE",  
              "bidMultiplierUp": "1.2",  
              "bidMultiplierDown": "0.2",  
              "askMultiplierUp": "5",  
              "askMultiplierDown": "0.8",  
              "avgPriceMins": 1  
        }  
    

`PERCENT_PRICE_BY_SIDE` 过滤器定义了基于交易对平均价格的合法价格范围. 取决于`BUY`或者`SELL`, 价格范围可能有所不同.  
  
`avgPriceMins` 是用来计算平均价格的分钟数. 0 表示用最新价(last price).  
  


买向订单需要满足:

  * `Order price` <= `weightedAveragePrice` * `bidMultiplierUp`
  * `Order price` >= `weightedAveragePrice` * `bidMultiplierDown`



卖向订单需要满足:

  * `Order Price` <= `weightedAveragePrice` * `askMultiplierUp`
  * `Order Price` >= `weightedAveragePrice` * `askMultiplierDown`



### LOT_SIZE 订单尺寸[​](/docs/zh-CN/institutional_loan/common-definition#lot_size-订单尺寸 "LOT_SIZE 订单尺寸的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
      }  
    

Lots是拍卖术语，`LOT_SIZE` 过滤器对订单中的 `quantity` 也就是数量参数进行合法性检查。包含三个部分:

  * `minQty` 表示 `quantity`/`icebergQty` 允许的最小值。
  * `maxQty` 表示 `quantity`/`icebergQty` 允许的最大值。
  * `stepSize` 表示 `quantity`/`icebergQty` 允许的步进值。



逻辑伪代码如下:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



### MIN_NOTIONAL 最小名义价值(成交额)[​](/docs/zh-CN/institutional_loan/common-definition#min_notional-最小名义价值成交额 "MIN_NOTIONAL 最小名义价值\(成交额\)的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "MIN_NOTIONAL",  
        "minNotional": "0.00100000",  
        "applyToMarket": true,  
        "avgPriceMins": 5  
      }  
    

MIN_NOTIONAL过滤器定义了交易对订单所允许的最小名义价值(成交额)。 订单的名义价值是`价格`*`数量`。 如果是高级订单(比如止盈止损订单`STOP_LOSS_LIMIT`)，名义价值会按照`stopPrice` * `quantity`来计算。 如果是冰山订单，名义价值会按照`price` * `icebergQty`来计算。 `applyToMarket`确定 `MIN_NOTIONAL`过滤器是否也将应用于`MARKET`订单。  
由于`MARKET`订单没有价格，因此会在最后`avgPriceMins`分钟内使用平均价格。  
`avgPriceMins`是计算平均价格的分钟数。 0表示使用最后的价格。

### NOTIONAL 名义价值[​](/docs/zh-CN/institutional_loan/common-definition#notional-名义价值 "NOTIONAL 名义价值的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
    {  
       "filterType": "NOTIONAL",  
       "minNotional": "10.00000000",  
       "applyMinToMarket": false,  
       "maxNotional": "10000.00000000",  
       "applyMaxToMarket": false,  
       "avgPriceMins": 5  
    }  
    

名义价值过滤器(`NOTIONAL`)定义了订单在一个交易对上可以下单的名义价值区间.  
  
  
  
`applyMinToMarket` 定义了 `minNotional` 是否适用于市价单(`MARKET`)   
  
`applyMaxToMarket` 定义了 `maxNotional` 是否适用于市价单(`MARKET`).

要通过此过滤器, 订单的名义价值 (单价 x 数量, `price * quantity`) 需要满足如下条件:

  * `price * quantity` <= `maxNotional`
  * `price * quantity` >= `minNotional`



对于市价单(`MARKET`), 用于计算的价格采用的是在 `avgPriceMins` 定义的时间之内的平均价.  
  
如果 `avgPriceMins` 为 0, 则采用最新的价格.

### ICEBERG_PARTS 冰山订单拆分数[​](/docs/zh-CN/institutional_loan/common-definition#iceberg_parts-冰山订单拆分数 "ICEBERG_PARTS 冰山订单拆分数的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "ICEBERG_PARTS",  
        "limit": 10  
      }  
    

`ICEBERG_PARTS` 代表冰山订单最多可以拆分成多少个小订单。  
计算方法为 `向上取整(qty / icebergQty)`。

### MARKET_LOT_SIZE 市价订单尺寸[​](/docs/zh-CN/institutional_loan/common-definition#market_lot_size-市价订单尺寸 "MARKET_LOT_SIZE 市价订单尺寸的直接链接")

> * **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "MARKET_LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
      }  
    

`MARKET_LOT_SIZE`过滤器为交易对上的`MARKET`订单定义了`数量`(即拍卖中的"手数")规则。 共有3部分：

  * `minQty`定义了允许的最小`quantity`。
  * `maxQty`定义了允许的最大数量。
  * `stepSize`定义了可以增加/减少数量的间隔。



为了通过`market lot size`，`quantity`必须满足以下条件：

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



### MAX_NUM_ORDERS 最多订单数[​](/docs/zh-CN/institutional_loan/common-definition#max_num_orders-最多订单数 "MAX_NUM_ORDERS 最多订单数的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "MAX_NUM_ORDERS",  
        "maxNumOrders": 25  
      }  
    

定义了某个交易对最多允许的挂单数量(不包括已关闭的订单)  
普通订单与条件订单均计算在内

### MAX_NUM_ALGO_ORDERS 最多条件单数[​](/docs/zh-CN/institutional_loan/common-definition#max_num_algo_orders-最多条件单数 "MAX_NUM_ALGO_ORDERS 最多条件单数的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 5  
      }  
    

`MAX_NUM_ALGO_ORDERS`过滤器定义允许账户在交易对上开设的"algo"订单的最大数量。  
"Algo"订单是`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`和`TAKE_PROFIT_LIMIT`止盈止损单。

### MAX_NUM_ICEBERG_ORDERS 最多冰山单数[​](/docs/zh-CN/institutional_loan/common-definition#max_num_iceberg_orders-最多冰山单数 "MAX_NUM_ICEBERG_ORDERS 最多冰山单数的直接链接")

`MAX_NUM_ICEBERG_ORDERS`过滤器定义了允许在交易对上开设账户的`ICEBERG`订单的最大数量。  
`ICEBERG`订单是icebergQty大于0的任何订单。.

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "MAX_NUM_ICEBERG_ORDERS",  
        "maxNumIcebergOrders": 5  
      }  
    

### MAX_POSITION 过滤器[​](/docs/zh-CN/institutional_loan/common-definition#max_position-过滤器 "MAX_POSITION 过滤器的直接链接")

这个过滤器定义账户允许的基于`base asset`的最大仓位。一个用户的仓位可以定义为如下资产的总和:

  1. `base asset`的可用余额
  2. `base asset`的锁定余额
  3. 所有处于open的买单的数量总和



如果用户的仓位大于最大的允许仓位，买单会被拒绝。

如果一个订单的数量(`quantity`) 可能导致持有仓位溢出, 会触发过滤器 `MAX_POSITION`.

> **/exchangeInfo 响应中的格式:**
    
    
    {  
      "filterType": "MAX_POSITION",  
      "maxPosition": "10.00000000"  
    }  
    

### TRAILING_DELTA[​](/docs/zh-CN/institutional_loan/common-definition#trailing_delta "TRAILING_DELTA的直接链接")

> **ExchangeInfo format:**
    
    
        {  
              "filterType": "TRAILING_DELTA",  
              "minTrailingAboveDelta": 10,  
              "maxTrailingAboveDelta": 2000,  
              "minTrailingBelowDelta": 10,  
              "maxTrailingBelowDelta": 2000  
       }  
    

此过滤器定义了参数`trailingDelta`的最大和最小值.

下追踪止损订单, 需要满足条件:

对于 `STOP_LOSS BUY`, `STOP_LOSS_LIMIT_BUY`, `TAKE_PROFIT SELL` 和 `TAKE_PROFIT_LIMIT SELL` 订单:

  * `trailingDelta` >= `minTrailingAboveDelta`
  * `trailingDelta` <= `maxTrailingAboveDelta`



对于 `STOP_LOSS SELL`, `STOP_LOSS_LIMIT SELL`, `TAKE_PROFIT BUY`, 和 `TAKE_PROFIT_LIMIT BUY` 订单:

  * `trailingDelta` >= `minTrailingBelowDelta`
  * `trailingDelta` <= `maxTrailingBelowDelta`



## 交易所级别过滤器[​](/docs/zh-CN/institutional_loan/common-definition#交易所级别过滤器 "交易所级别过滤器的直接链接")

### EXCHANGE_MAX_NUM_ORDERS 最多订单数[​](/docs/zh-CN/institutional_loan/common-definition#exchange_max_num_orders-最多订单数 "EXCHANGE_MAX_NUM_ORDERS 最多订单数的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "EXCHANGE_MAX_NUM_ORDERS",  
        "maxNumOrders": 1000  
      }  
    

`EXCHANGE_MAX_NUM_ORDERS`过滤器定义了允许在交易对上开设账户的最大订单数。  
请注意，此过滤器同时计算"algo"订单和常规订单。

### EXCHANGE_MAX_ALGO_ORDERS 交易最大ALGO订单数[​](/docs/zh-CN/institutional_loan/common-definition#exchange_max_algo_orders-交易最大algo订单数 "EXCHANGE_MAX_ALGO_ORDERS 交易最大ALGO订单数的直�接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "EXCHANGE_MAX_ALGO_ORDERS",  
        "maxNumAlgoOrders": 200  
      }  
    

`EXCHANGE_MAX_ALGO_ORDERS`过滤器定义了允许在交易上开设账户的"algo"订单的最大数量。  
"Algo"订单是`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`和`TAKE_PROFIT_LIMIT`订单。

### EXCHANGE_MAX_NUM_ICEBERG_ORDERS 冰山订单的最大订单数[​](/docs/zh-CN/institutional_loan/common-definition#exchange_max_num_iceberg_orders--冰山订单的最大订单数 "EXCHANGE_MAX_NUM_ICEBERG_ORDERS  冰山订单的最大订单数的直接链接")

此过滤器定义了允许账号持有的最大冰山订单数量.

> **/exchangeInfo 响应中的格式:**
    
    
    {  
      "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",  
      "maxNumIcebergOrders": 10000  
    }