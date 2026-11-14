---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin/common-definition
api_type: REST
updated_at: 2026-11-13 20:28:10.141068
---

# Public API Definitions

## Terminology

  * `baseasseet` refers to the asset that is the `quantity` of a symbol.
  * `quoteAsset` refers to the asset that is the `price` of a symbol.
  * `Margin` refers to `Cross Margin`
  * `UM` refers to `USD-M Futures`
  * `CM` refers to `Coin-M Futures`



## ENUM definitions

**Order side (side)**

  * BUY
  * SELL



**Position side for Futures (positionSide)**

  * BOTH
  * LONG
  * SHORT



**Time in force (timeInForce)**

  * GTC - Good Till Cancel
  * IOC - Immediate or Cancel
  * FOK - Fill or Kill
  * GTX - Good Till Crossing (Post Only)



**Stop-Limit Time in force (stopLimitTimeInForce)**

  * GTC - Good Till Cancel
  * IOC - Immediate or Cancel
  * FOK - Fill or Kill



**Side Effect Type (sideEffectType)**

  * NO_SIDE_EFFECT
  * MARGIN_BUY
  * AUTO_REPAY



**Price Match (priceMatch)**

  * NONE: no price match
  * OPPONENT: counterparty best price
  * OPPONENT_5: counterparty 5th best price
  * OPPONENT_10: counterparty 10th best price
  * OPPONENT_20: counterparty 20th best price
  * QUEUE: the best price on the same side of the order book
  * QUEUE_5: the 5th best price on the same side of the order book
  * QUEUE_10: the 10th best price on the same side of the order book
  * QUEUE_20: the 20th best price on the same side of the order book



**Self-Trade Prevention mode (selfTradePreventionMode)**

  * NONE: No Self-Trade Prevention
  * EXPIRE_TAKER: expire taker order when STP trigger
  * EXPIRE_BOTH: expire taker and maker order when STP trigger
  * EXPIRE_MAKER: expire maker order when STP trigger



**Response Type (newOrderRespType)**

  * ACK
  * RESULT



**Order types (type)**

  * LIMIT
  * MARKET



**Conditional Order types (strategyType)**

  * STOP
  * STOP_MARKET
  * LIMIT_MAKER
  * TAKE_PROFIT
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**Working Type for Futures Conditional Orders (workingType)**

  * MARK_PRICE



**Order status (status)**

  * NEW
  * CANCELED
  * REJECTED
  * PARTIALLY_FILLED
  * FILLED
  * EXPIRED
  * EXPIRED_IN_MATCH



**Conditional Order status (strategyStatus)**

  * NEW
  * CANCELED
  * TRIGGERED - conditional order is triggered
  * FINISHED - triggered order is filled
  * EXPIRED



**Futures Contract type (contractType):**

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



**Rate limiters (rateLimitType)**

  * REQUEST_WEIGHT
  * ORDERS



> **REQUEST_WEIGHT**
    
    
    Code
    
      {
        "rateLimitType": "REQUEST_WEIGHT",
        "interval": "MINUTE",
        "intervalNum": 1,
        "limit": 2400
      }

> **ORDERS**
    
    
    Code
    
      {
        "rateLimitType": "ORDERS",
        "interval": "MINUTE",
        "intervalNum": 1,
        "limit": 1200
       }

**Rate limit intervals (interval)**

  * MINUTE



# Filters

Filters define trading rules on a symbol or an exchange.

## Symbol filters

### PRICE_FILTER

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

  * `minPrice` defines the minimum `price`/`stopPrice` allowed; disabled on `minPrice` == 0.
  * `maxPrice` defines the maximum `price`/`stopPrice` allowed; disabled on `maxPrice` == 0.
  * `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by; disabled on `tickSize` == 0.



Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

  * sell order `price` >= `minPrice`
  * buy order `price` <= `maxPrice`
  * (`price`-`minPrice`) % `tickSize` == 0



> **ExchangeInfo format:**
    
    
    Code
    
    {
        "filterType": "PRICE_FILTER",
        "minPrice": "0.00000100",
        "maxPrice": "100000.00000000",
        "tickSize": "0.00000100"
    }

### LOT_SIZE

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity` allowed.
  * `maxQty` defines the maximum `quantity` allowed.
  * `stepSize` defines the intervals that a `quantity` can be increased/decreased by.



In order to pass the `lot size`, the following must be true for `quantity`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * (`quantity`-`minQty`) % `stepSize` == 0



> **/exchangeInfo format:**
    
    
    Code
    
    {
        "filterType": "LOT_SIZE",
        "minQty": "0.00100000",
        "maxQty": "100000.00000000",
        "stepSize": "0.00100000"
    }

### PERCENT_PRICE

The `PERCENT_PRICE` filter defines valid range for a price based on the mark price in Futures and on the average of the previous trades in Cross Margin. For Cross Margin `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

In order to pass the `percent price`, the following must be true for `price`:

  * Futures
    * BUY: `price` <= `markPrice` * `multiplierUp`
    * SELL: `price` >= `markPrice` * `multiplierDown`
  * Cross Margin
    * BUY: `price` <= `weightedAveragePrice` * `multiplierUp`
    * SELL: `price` >= `weightedAveragePrice` * `multiplierDown`



### MIN_NOTIONAL

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the `price` * `quantity`. Since `MARKET` orders have no price, the `mark price` is used in Futures and the average price is used over the last `avgPriceMins` for Cross Margin. `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

### MARKET_LOT_SIZE

The `MARKET_LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for `MARKET` orders on a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity` allowed.
  * `maxQty` defines the maximum `quantity` allowed.
  * `stepSize` defines the intervals that a `quantity` can be increased/decreased by.



In order to pass the `market lot size`, the following must be true for `quantity`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * (`quantity`-`minQty`) % `stepSize` == 0



> **/exchangeInfo format:**
    
    
    Code
    
    {
      "filterType": "MARKET_LOT_SIZE",
      "minQty": "0.00100000",
      "maxQty": "100000.00000000",
      "stepSize": "0.00100000"
    }

### MAX_NUM_ORDERS

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol. Note that both "algo" orders and normal orders are counted for this filter.

> **/exchangeInfo format:**
    
    
    Code
    
    {
      "filterType": "MAX_NUM_ORDERS",
      "limit": 200
    }

### MAX_NUM_ALGO_ORDERS

The `MAX_NUM_ALGO_ORDERS` filter defines the maximum number of all kinds of algo orders an account is allowed to have open on a symbol. The algo orders include `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, and `TRAILING_STOP_MARKET` orders.

> **/exchangeInfo format:**
    
    
    Code
    
    {
      "filterType": "MAX_NUM_ALGO_ORDERS",
      "limit": 100
    }

Was this page helpful?

Last modified on November 12, 2026

[Error Codes](/en/docs/products/derivatives-trading-portfolio-margin/error-code)[Introduction](/en/docs/products/derivatives-trading-portfolio-margin-pro/Introduction)

---

# 公开API参数

## 术语解释

  * `base asset` 指一个交易对的交易对象，即写在靠前部分的资产名
  * `quote asset` 指一个交易对的定价资产，即写在靠后部分资产名
  * `Margin` 指全仓杠杆
  * `UM` 指U本位合约`USD-M Futures`
  * `CM` 指币本位合约`Coin-M Futures`



## 枚举定义

**订单方向 (side):**

  * BUY 买入
  * SELL 卖出



**合约持仓方向:**

  * BOTH 单一持仓方向
  * LONG 多头(双向持仓下)
  * SHORT 空头(双向持仓下)



**有效方式 (timeInForce):**

  * GTC - Good Till Cancel 成交为止
  * IOC - Immediate or Cancel 无法立即成交(吃单)的部分就撤销
  * FOK - Fill or Kill 无法全部立即成交就撤销
  * GTX - Good Till Crossing 无法成为挂单方就撤销



**响应类型 (newOrderRespType)**

  * ACK
  * RESULT



**订单种类 (orderTypes, type):**

  * LIMIT
  * MAERKET



**条件订单类型（type）:**

  * STOP
  * STOP_MARKET
  * LIMIT_MAKER
  * TAKE_PROFIT
  * TAKE_PROFIT_MARKET
  * TRAILING_STOP_MARKET



**合约条件单价格触发类型 (workingType)**

  * MARK_PRICE 标记价格



**条件单状态 (strategyStatus)**

  * NEW
  * CANCELED
  * TRIGGERED - 条件单被触发
  * FINISHED - 触发单完全成交
  * EXPIRED



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



**订单状态 (status):**

  * NEW 新建订单
  * PARTIALLY_FILLED 部分成交
  * FILLED 全部成交
  * CANCELED 已撤销
  * REJECTED 订单被拒绝
  * EXPIRED 订单过期(根据timeInForce参数规则)
  * EXPIRED_IN_MATCH 订单在撮合过程中被过期(例如STP自成交预防触发)



**限制种类 (rateLimitType)**

> REQUEST_权重
    
    
    Code
    
      {
      	"rateLimitType": "REQUEST_权重",
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

  * REQUESTS_权重 单位时间请求权重之和上限

  * ORDERS 单位时间下单(撤单)次数上限




**限制间隔**

  * MINUTE



# 过滤器

过滤器，即Filter，定义了一系列交易规则。共有两类，分别是针对交易对的过滤器`symbol filters`，和针对整个交易所的过滤器`exchange filters`(暂不支持)

## 交易对过滤器

### PRICE_FILTER 价格过滤器

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
        "notioanl": "5.0"
      }

MIN_NOTIONAL过滤器定义了交易对订单所允许的最小名义价值(成交额)。订单的名义价值是`价格`*`数量`。由于`MARKET`订单没有价格，因此会使用 mark price 计算。

此页面是否有帮助？

Last modified on November 12, 2026

[错误代码](/zh-CN/docs/products/derivatives-trading-portfolio-margin/error-code)[概述](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/Introduction)