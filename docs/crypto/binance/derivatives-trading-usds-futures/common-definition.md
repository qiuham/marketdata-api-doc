---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-usds-futures/common-definition
api_type: REST
updated_at: 2026-11-13 20:27:32.660112
---

# Public Endpoints Info

## Terminology

  * `base asset` refers to the asset that is the `quantity` of a symbol.
  * `quote asset` refers to the asset that is the `price` of a symbol.



## ENUM definitions

**Symbol type:**

  * FUTURE



**Contract type (contractType):**

  * PERPETUAL
  * CURRENT_MONTH
  * NEXT_MONTH
  * CURRENT_QUARTER
  * NEXT_QUARTER
  * PERPETUAL_DELIVERING



**Contract status (contractStatus, status):**

  * PENDING_TRADING
  * TRADING
  * PRE_DELIVERING
  * DELIVERING
  * DELIVERED
  * PRE_SETTLE
  * SETTLING
  * CLOSE
  * TRADING_HALT
  * TRADING_CANCEL_ONLY



**Order status (status):**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * REJECTED
  * EXPIRED
  * EXPIRED_IN_MATCH



**Order types (orderTypes, type):**

  * LIMIT
  * MARKET
  * STOP
  * STOP_MARKET
  * TAKE_PROFIT
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**Order side (side):**

  * BUY
  * SELL



**Position side (positionSide):**

  * BOTH
  * LONG
  * SHORT



**Time in force (timeInForce):**

  * GTC - Good Till Cancel(GTC order valitidy is 1 year from placement)
  * IOC - Immediate or Cancel
  * FOK - Fill or Kill
  * GTX - Good Till Crossing (Post Only)
  * GTD - Good Till Date
  * RPI - Retail Price Improvement(RPI order is post only and only be matched with the order from APP or Web)



**Working Type (workingType)**

  * MARK_PRICE
  * CONTRACT_PRICE



**Response Type (newOrderRespType)**

  * ACK
  * RESULT



**Kline/Candlestick chart intervals:**

s -> seconds; m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

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



**STP MODE (selfTradePreventionMode):**

  * EXPIRE_TAKER
  * EXPIRE_BOTH
  * EXPIRE_MAKER



**Price Match (priceMatch)**

  * NONE (No price match)
  * OPPONENT (counterparty best price)
  * OPPONENT_5 (the 5th best price from the counterparty)
  * OPPONENT_10 (the 10th best price from the counterparty)
  * OPPONENT_20 (the 20th best price from the counterparty)
  * QUEUE (the best price on the same side of the order book)
  * QUEUE_5 (the 5th best price on the same side of the order book)
  * QUEUE_10 (the 10th best price on the same side of the order book)
  * QUEUE_20 (the 20th best price on the same side of the order book)



**Rate limiters (rateLimitType)**

> REQUEST_WEIGHT
    
    
    Code
    
      {
      	"rateLimitType": "REQUEST_WEIGHT",
      	"interval": "MINUTE",
      	"intervalNum": 1,
      	"limit": 2400
      }

> ORDERS
    
    
    Code
    
      {
      	"rateLimitType": "ORDERS",
      	"interval": "MINUTE",
      	"intervalNum": 1,
      	"limit": 1200
       }

  * REQUEST_WEIGHT

  * ORDERS




**Rate limit intervals (interval)**

  * MINUTE



# Filters

Filters define trading rules on a symbol or an exchange.

## Symbol filters

### PRICE_FILTER

> **/exchangeInfo format:**
    
    
    Code
    
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
  * (`price`-`minPrice`) % `tickSize` == 0



### LOT_SIZE

> **/exchangeInfo format:**
    
    
    Code
    
      {
        "filterType": "LOT_SIZE",
        "minQty": "0.00100000",
        "maxQty": "100000.00000000",
        "stepSize": "0.00100000"
      }

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity` allowed.
  * `maxQty` defines the maximum `quantity` allowed.
  * `stepSize` defines the intervals that a `quantity` can be increased/decreased by.



In order to pass the `lot size`, the following must be true for `quantity`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * (`quantity`-`minQty`) % `stepSize` == 0



### MARKET_LOT_SIZE

> **/exchangeInfo format:**
    
    
    Code
    
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
  * (`quantity`-`minQty`) % `stepSize` == 0



### MAX_NUM_ORDERS

> **/exchangeInfo format:**
    
    
    Code
    
      {
        "filterType": "MAX_NUM_ORDERS",
        "limit": 200
      }

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol.

Note that both "algo" orders and normal orders are counted for this filter.

### MAX_NUM_ALGO_ORDERS

> **/exchangeInfo format:**
    
    
    Code
    
      {
        "filterType": "MAX_NUM_ALGO_ORDERS",
        "limit": 100
      }

The `MAX_NUM_ALGO_ORDERS ` filter defines the maximum number of all kinds of algo orders an account is allowed to have open on a symbol.

The algo orders include `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, and `TRAILING_STOP_MARKET` orders.

### PERCENT_PRICE

> **/exchangeInfo format:**
    
    
    Code
    
      {
        "filterType": "PERCENT_PRICE",
        "multiplierUp": "1.1500",
        "multiplierDown": "0.8500",
        "multiplierDecimal": 4
      }

The `PERCENT_PRICE` filter defines valid range for a price based on the mark price.

In order to pass the `percent price`, the following must be true for `price`:

  * BUY: `price` <= `markPrice` * `multiplierUp`
  * SELL: `price` >= `markPrice` * `multiplierDown`



### MIN_NOTIONAL

> **/exchangeInfo format:**
    
    
    Code
    
      {
        "filterType": "MIN_NOTIONAL",
        "notional": "5.0"
      }

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the `price` * `quantity`. Since `MARKET` orders have no price, the mark price is used.

Was this page helpful?

Last modified on November 12, 2026

[User Data Streams](/en/docs/products/derivatives-trading-usds-futures/user-data-streams)[Error Codes](/en/docs/products/derivatives-trading-usds-futures/error-code)

---

# 公开API参数

## 术语解释

  * `base asset` 指一个交易对的交易对象，即写在靠前部分的资产名
  * `quote asset` 指一个交易对的定价资产，即写在靠后部分资产名



## 枚举定义

**交易对类型:**

  * FUTURE 期货



**合约类型 (contractType):**

  * PERPETUAL 永续合约
  * CURRENT_MONTH 当月交割合约
  * NEXT_MONTH 次月交割合约
  * CURRENT_QUARTER 当季交割合约
  * NEXT_QUARTER 次季交割合约
  * PERPETUAL_DELIVERING 交割结算中合约



**合约状态 (contractStatus, status):**

  * PENDING_TRADING 待上市
  * TRADING 交易中
  * PRE_DELIVERING 预交割
  * DELIVERING 交割中
  * DELIVERED 已交割
  * PRE_SETTLE 预结算
  * SETTLING 结算中
  * CLOSE 已下架
  * TRADING_HALT 交易暂停
  * TRADING_CANCEL_ONLY 只挂单



**订单状态 (status):**

  * NEW 新建订单
  * PARTIALLY_FILLED 部分成交
  * FILLED 全部成交
  * CANCELED 已撤销
  * REJECTED 订单被拒绝
  * EXPIRED 订单过期(根据timeInForce参数规则)
  * EXPIRED_IN_MATCH 订单被STP过期



**订单种类 (orderTypes, type):**

  * LIMIT 限价单
  * MARKET 市价单
  * STOP 止损限价单
  * STOP_MARKET 止损市价单
  * TAKE_PROFIT 止盈限价单
  * TAKE_PROFIT_MARKET 止盈市价单
  * TRAILING_STOP_MARKET 跟踪止损单



**订单方向 (side):**

  * BUY 买入
  * SELL 卖出



**持仓方向:**

  * BOTH 单一持仓方向
  * LONG 多头(双向持仓下)
  * SHORT 空头(双向持仓下)



**有效方式 (timeInForce):**

  * GTC - Good Till Cancel 成交为止（下单后仅有1年有效期，1年后自动取消）
  * IOC - Immediate or Cancel 无法立即成交(吃单)的部分就撤销
  * FOK - Fill or Kill 无法全部立即成交就撤销
  * GTX - Good Till Crossing 无法成为挂单方就撤销
  * GTD - Good Till Date 在特定时间之前有效，到期自动撤销
  * RPI - Retail Price Improvement（仅与来自APP或者网页端的订单成交，且为Post Only）



**条件价格触发类型 (workingType)**

  * MARK_PRICE
  * CONTRACT_PRICE



**响应类型 (newOrderRespType)**

  * ACK
  * RESULT



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



**防止自成交模式:**

  * EXPIRE_TAKER
  * EXPIRE_BOTH
  * EXPIRE_MAKER



**盘口价下单模式:**

  * OPPONENT (盘口对手价)
  * OPPONENT_5 (盘口对手5档价)
  * OPPONENT_10 (盘口对手10档价)
  * OPPONENT_20
  * QUEUE (盘口同向价)
  * QUEUE_5 (盘口同向排队5档价)
  * QUEUE_10 (盘口同向排队10档价)
  * QUEUE_20 (盘口同向排队20档价)



**限制种类 (rateLimitType)**

> REQUEST_WEIGHT
    
    
    Code
    
      {
      	"rateLimitType": "REQUEST_WEIGHT",
      	"interval": "MINUTE",
      	"intervalNum": 1,
      	"limit": 2400
      }

> ORDERS
    
    
    Code
    
      {
      	"rateLimitType": "ORDERS",
      	"interval": "MINUTE",
      	"intervalNum": 1,
      	"limit": 1200
       }

  * REQUESTS_WEIGHT 单位时间请求权重之和上限

  * ORDERS 单位时间下单(撤单)次数上限




**限制间隔**

  * MINUTE



# 过滤器

过滤器，即Filter，定义了一系列交易规则。共有两类，分别是针对交易对的过滤器`symbol filters`，和针对整个交易所的过滤器`exchange filters`(暂不支持)

## 交易对过滤器

#### PRICE_FILTER 价格过滤器

> **/exchangeInfo 响应中的格式:**
    
    
    Code
    
      {
        "filterType": "PRICE_FILTER",
        "minPrice": "0.00000100",
        "maxPrice": "100000.00000000",
        "tickSize": "0.00000100"
      }

价格过滤器用于检测order订单中price参数的合法性

  * `minPrice` 定义了 `price`/`stopPrice` 允许的最小值
  * `maxPrice` 定义了 `price`/`stopPrice` 允许的最大值。
  * `tickSize` 定义了 `price`/`stopPrice` 的步进间隔，即price必须等于minPrice+(tickSize的整数倍) 以上每一项均可为0，为0时代表这一项不再做限制。



逻辑伪代码如下：

  * `price` >= `minPrice`
  * `price` <= `maxPrice`
  * (`price`-`minPrice`) % `tickSize` == 0



### LOT_SIZE 订单尺寸

> */exchangeInfo 响应中的格式:**
    
    
    Code
    
      {
        "filterType": "LOT_SIZE",
        "minQty": "0.00100000",
        "maxQty": "100000.00000000",
        "stepSize": "0.00100000"
      }

lots是拍卖术语，这个过滤器对订单中的`quantity`也就是数量参数进行合法性检查。包含三个部分：

  * `minQty` 表示 `quantity` 允许的最小值.
  * `maxQty` 表示 `quantity` 允许的最大值
  * `stepSize` 表示 `quantity`允许的步进值。



逻辑伪代码如下：

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * (`quantity`-`minQty`) % `stepSize` == 0



### MARKET_LOT_SIZE 市价订单尺寸

参考LOT_SIZE，区别仅在于对市价单还是限价单生效

### MAX_NUM_ORDERS 最多订单数

> **/exchangeInfo 响应中的格式:**
    
    
    Code
    
      {
        "filterType": "MAX_NUM_ORDERS",
        "limit": 200
      }

定义了某个交易对最多允许的挂单数量(不包括已关闭的订单)

普通订单与条件订单均计算在内

### MAX_NUM_ALGO_ORDERS 最多条件订单数

> **/exchangeInfo format:**
    
    
    Code
    
      {
        "filterType": "MAX_NUM_ALGO_ORDERS",
        "limit": 100
      }

定义了某个交易对最多允许的条件订单的挂单数量(不包括已关闭的订单)。

条件订单目前包括`STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, 和 `TRAILING_STOP_MARKET`

### PERCENT_PRICE 价格振幅过滤器

> **/exchangeInfo 响应中的格式:**
    
    
    Code
    
      {
        "filterType": "PERCENT_PRICE",
        "multiplierUp": "1.1500",
        "multiplierDown": "0.8500",
        "multiplierDecimal": 4
      }

`PERCENT_PRICE` 定义了基于标记价格计算的挂单价格的可接受区间.

挂单价格必须同时满足以下条件：

  * 买单: `price` <= `markPrice` * `multiplierUp`
  * 卖单: `price` >= `markPrice` * `multiplierDown`



### MIN_NOTIONAL 最小名义价值

> **/exchangeInfo 响应中的格式:**
    
    
    Code
    
      {
        "filterType": "MIN_NOTIONAL",
        "notional": "5.0"
      }

MIN_NOTIONAL过滤器定义了交易对订单所允许的最小名义价值(成交额)。订单的名义价值是`价格`*`数量`。由于`MARKET`订单没有价格，因此会使用 mark price 计算。

此页面是否有帮助？

Last modified on November 12, 2026

[账户信息流](/zh-CN/docs/products/derivatives-trading-usds-futures/user-data-streams)[错误代码](/zh-CN/docs/products/derivatives-trading-usds-futures/error-code)