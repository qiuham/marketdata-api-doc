---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition
api_type: REST
updated_at: 2026-05-27 18:55:31.845511
---

# Public Endpoints Info

## Terminology[​](/docs/derivatives/coin-margined-futures/common-definition#terminology "Direct link to Terminology")

  * `symbol` refers to the symbol name of a contract symbol
  * `pair` refers to the underlying symbol of a contracrt symbol
  * `base asset` refers to the asset that is the `quantity` of a symbol.
  * `quote asset` refers to the asset that is the `price` of a symbol.
  * `margin asset` refers to the asset that is the `margin` of a symbol



## ENUM definitions[​](/docs/derivatives/coin-margined-futures/common-definition#enum-definitions "Direct link to ENUM definitions")

**Symbol type:**

  * DELIVERY_CONTRACT
  * PERPETUAL_CONTRACT



**Contract type (contractType):**

  * PERPETUAL
  * CURRENT_QUARTER
  * NEXT_QUARTER
  * CURRENT_QUARTER_DELIVERING // Invalid type, only used for DELIVERING status
  * NEXT_QUARTER_DELIVERING // Invalid type, only used for DELIVERING status
  * PERPETUAL_DELIVERING



**Contract status (contractStatus, status):**

  * PENDING_TRADING
  * TRADING
  * PRE_DELIVERING
  * DELIVERING
  * DELIVERED



**Order status (status):**

  * NEW
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED



**Order types (type):**

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

  * GTC - Good Till Cancel
  * IOC - Immediate or Cancel
  * FOK - Fill or Kill
  * GTX - Good Till Crossing (Post Only)



**Working Type (workingType)**

  * MARK_PRICE
  * CONTRACT_PRICE



**New Order Response Type (newOrderRespType)**

  * ACK
  * RESULT



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



**Kline/Candlestick chart intervals:**

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

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

## Symbol filters[​](/docs/derivatives/coin-margined-futures/common-definition#symbol-filters "Direct link to Symbol filters")

### PRICE_FILTER[​](/docs/derivatives/coin-margined-futures/common-definition#price_filter "Direct link to PRICE_FILTER")

> **/exchangeInfo format:**
    
    
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



### LOT_SIZE[​](/docs/derivatives/coin-margined-futures/common-definition#lot_size "Direct link to LOT_SIZE")

> **/exchangeInfo format:**
    
    
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



### MARKET_LOT_SIZE[​](/docs/derivatives/coin-margined-futures/common-definition#market_lot_size "Direct link to MARKET_LOT_SIZE")

> **/exchangeInfo format:**
    
    
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



### MAX_NUM_ORDERS[​](/docs/derivatives/coin-margined-futures/common-definition#max_num_orders "Direct link to MAX_NUM_ORDERS")

> **/exchangeInfo format:**
    
    
      {  
        "filterType": "MAX_NUM_ORDERS",  
        "limit": 200  
      }  
    

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol.

Note that both "algo" orders and normal orders are counted for this filter.

### PERCENT_PRICE[​](/docs/derivatives/coin-margined-futures/common-definition#percent_price "Direct link to PERCENT_PRICE")

> **/exchangeInfo format:**
    
    
      {  
        "filterType": "PERCENT_PRICE",  
        "multiplierUp": "1.0500",  
        "multiplierDown": "0.9500",  
        "multiplierDecimal": 4  
      }  
    

The `PERCENT_PRICE` filter defines valid range for a price based on the mark price.

In order to pass the `percent price`, the following must be true for `price`:

  * BUY: `price` <= `markPrice` * `multiplierUp`
  * SELL: `price` >= `markPrice` * `multiplierDown`

---

# 公开API参数

## 术语解释[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#术语解释 "术语解释的直接链接")

  * `symbol` 指合约交易对名称
  * `pair` 指合约交易对的标的物交易对
  * `base asset` 指合约交易对的交易对象,即标的物交易对交易对象
  * `quote asset` 指合约交易对的定价资产,即标的物交易对的定价资产
  * `margin asset` 指合约交易对使用的保证金资产



## 枚举定义[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#枚举定义 "枚举定义的直接链接")

**交易对类型:**

  * DELIVERY_CONTRACT 交割合约
  * PERPETUAL_CONTRACT 永续合约



**合约类型 (contractType):**

  * PERPETUAL 永续合约
  * CURRENT_QUARTER 当季合约
  * NEXT_QUARTER 次季合约
  * CURRENT_QUARTER_DELIVERING 交割中的无效类型
  * NEXT_QUARTER_DELIVERING 交割中的无效类型
  * PERPETUAL DELIVERING 交割結算中合約



**合约状态 (contractStatus, status):**

  * PENDING_TRADING 待上市
  * TRADING 交易中
  * PRE_DELIVERING 预结算
  * DELIVERING 交割中
  * DELIVERED 已交割



**订单状态 (status):**

  * NEW 新建订单
  * PARTIALLY_FILLED 部分成交
  * FILLED 全部成交
  * CANCELED 已撤销
  * EXPIRED 订单过期(根据timeInForce参数规则)



**订单种类 (type):**

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



**持仓方向 (positionSide):**

  * BOTH 单一持仓方向
  * LONG 多头(双向持仓下)
  * SHORT 空头(双向持仓下)



**有效方式 (timeInForce):**

  * GTC - Good Till Cancel 成交为止
  * IOC - Immediate or Cancel 无法立即成交(吃单)的部分就撤销
  * FOK - Fill or Kill 无法全部立即成交就撤销
  * GTX - Good Till Crossing 无法成为挂单方就撤销



**条件价格触发类型 (workingType)**

  * MARK_PRICE
  * CONTRACT_PRICE



**响应类型 (newOrderRespType)**

  * ACK
  * RESULT



**价格匹配类型 (priceMatch)**

  * NONE: 设置价格匹配
  * OPPONENT: 盘口对手价
  * OPPONENT_5: 盘口对手5档价
  * OPPONENT_10: 盘口对手10档价
  * OPPONENT_20: 盘口对手20档价
  * QUEUE: 盘口同向价
  * QUEUE_5: 盘口同向排队5档价
  * QUEUE_10: 盘口同向排队10档价
  * QUEUE_20: 盘口同向排队20档价



**自成交保护类型（selfTradePreventionMode）**

  * NONE: 不设置自成交保护
  * EXPIRE_TAKER: 自成交过期 taker 订单
  * EXPIRE_MAKER: 自成交过期 maker 订单
  * EXPIRE_BOTH: 自成交过期 taker 和 maker 订单



**K线间隔:**

m -> 分钟; h -> 小时; d -> 天; w -> 周; M -> 月

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
      	"interval": "MINUTE",  
      	"intervalNum": 1,  
      	"limit": 1200  
       }  
    

  * REQUESTS_WEIGHT 单位时间请求权重之和上限

  * ORDERS 单位时间下单(撤单)次数上限




**限制间隔**

  * MINUTE



# 过滤器

过滤器,即Filter,定义了一系列交易规则。 共有两类,分别是针对交易对的过滤器`symbol filters`,和针对整个交易所的过滤器`exchange filters`(暂不支持)

## 交易对过滤器[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#交易对过滤器 "交易对过滤器的直接链接")

### PRICE_FILTER 价格过滤器[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#price_filter-价格过滤器 "PRICE_FILTER 价格过滤器的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "PRICE_FILTER",  
        "minPrice": "0.00000100",  
        "maxPrice": "100000.00000000",  
        "tickSize": "0.00000100"  
      }  
    

价格过滤器用于检测order订单中price参数的合法性

  * `minPrice` 定义了 `price`/`stopPrice` 允许的最小值
  * `maxPrice` 定义了 `price`/`stopPrice` 允许的最大值。
  * `tickSize` 定义了 `price`/`stopPrice` 的步进间隔,即price必须等于minPrice+(tickSize的整数倍) 以上每一项均可为0,为0时代表这一项不再做限制。



逻辑伪代码如下：

  * `price` >= `minPrice`
  * `price` <= `maxPrice`
  * (`price`-`minPrice`) % `tickSize` == 0



### LOT_SIZE 订单尺寸[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#lot_size-订单尺寸 "LOT_SIZE 订单尺寸的直接链接")

> _/exchangeInfo 响应中的格式:_ *
    
    
      {  
        "filterType": "LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
      }  
    

lots是拍卖术语,这个过滤器对订单中的`quantity`也就是数量参数进行合法性检查。包含三个部分：

  * `minQty` 表示 `quantity` 允许的最小值.
  * `maxQty` 表示 `quantity` 允许的最大值
  * `stepSize` 表示 `quantity`允许的步进值。



逻辑伪代码如下：

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * (`quantity`-`minQty`) % `stepSize` == 0



### MARKET_LOT_SIZE 市价订单尺寸[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#market_lot_size-市价订单尺寸 "MARKET_LOT_SIZE 市价订单尺寸的直接链接")

参考LOT_SIZE,区别仅在于对市价单还是限价单生效

### MAX_NUM_ORDERS 最多订单数[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#max_num_orders-最多订单数 "MAX_NUM_ORDERS 最多订单数的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "MAX_NUM_ORDERS",  
        "limit": 200  
      }  
    

定义了某个交易对最多允许的挂单数量(不包括已关闭的订单)

普通订单与条件订单均计算在内

### PERCENT_PRICE 价格振幅过滤器[​](/docs/zh-CN/derivatives/coin-margined-futures/common-definition#percent_price-价格振幅过滤器 "PERCENT_PRICE 价格振幅过滤器的直接链接")

> **/exchangeInfo 响应中的格式:**
    
    
      {  
        "filterType": "PERCENT_PRICE",  
        "multiplierUp": "1.0500",  
        "multiplierDown": "0.9500",  
        "multiplierDecimal": 4  
      }  
    

`PERCENT_PRICE` 定义了基于标记价格计算的挂单价格的可接受区间.

挂单价格必须同时满足以下条件：

  * 买单: `price` <= `markPrice` * `multiplierUp`
  * 卖单: `price` >= `markPrice` * `multiplierDown`