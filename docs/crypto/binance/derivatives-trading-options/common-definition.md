---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-options/common-definition
api_type: REST
updated_at: 2026-11-13 20:27:57.289760
---

# Public Endpoints Info

## Terminology

  * `symbol` refers to the symbol name of a options contract symbol
  * `underlying` refers to the underlying symbol of a options contract symbol
  * `quoteAsset` refers to the asset that is the price of a symbol.
  * `settleAsset` refers to the settlement asset when options are exercised



## ENUM definitions

**Options contract type**

  * CALL
  * PUT



**Order side (side)**

  * BUY
  * SELL



**Position side (positionSide)**

  * LONG
  * SHORT



**Time in force (timeInForce)**

  * GTC - Good Till Cancel
  * IOC - Immediate or Cancel
  * FOK - Fill or Kill
  * GTX - Post only



**Response Type (newOrderRespType)**

  * ACK
  * RESULT



**Order types (type)**

  * LIMIT



**Order status (status)**

  * NEW
  * REJECTED
  * PARTIALLY_FILLED
  * FILLED
  * CANCELED
  * EXPIRED
  * EXPIRED_IN_MATCH



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



**STP MODE (selfTradePreventionMode):**

  * EXPIRE_TAKER
  * EXPIRE_BOTH
  * EXPIRE_MAKER



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
      "minPrice": "793.112",
      "maxPrice": "1189.668",
      "tickSize": "5.000"
    }

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

  * `minPrice` defines the minimum `price` allowed; disabled on `minPrice` == 0.
  * `maxPrice` defines the maximum `price` allowed; disabled on `maxPrice` == 0.
  * `tickSize` defines the intervals that a `price` can be increased/decreased by; disabled on `tickSize` == 0.



Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

  * sell order `price` >= `minPrice`
  * buy order `price` <= `maxPrice`
  * (`price`-`minPrice`) % `tickSize` == 0



### LOT_SIZE

> **/exchangeInfo format:**
    
    
    Code
    
    {
      "filterType": "LOT_SIZE",
      "minQty": "0.0001",
      "maxQty": "1000",
      "stepSize": "0.0100"
    }

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity` allowed.
  * `maxQty` defines the maximum `quantity` allowed.
  * `stepSize` defines the intervals that a `quantity` can be increased/decreased by.



In order to pass the `lot size`, the following must be true for `quantity`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * (`quantity`-`minQty`) % `stepSize` == 0



Was this page helpful?

Last modified on November 12, 2026

[User Data Streams](/en/docs/products/derivatives-trading-options/user-data-streams)[Error Codes](/en/docs/products/derivatives-trading-options/error-code)

---

# 公开API参数

## 术语解释

  * `symbol` 指期权合约的合约交易对名
  * `underlying` 指期权合约标的资产的交易对名
  * `quote asset` 指一个期权交易对的定价资产
  * `settleAsset` 指期权行权时的结算资产



## 枚举定义

**期权方向 (side):**

  * CALL 看涨期权
  * PUT 看跌期权



**订单方向 (side):**

  * BUY 买入
  * SELL 卖出



**持仓方向:**

  * LONG 多头
  * SHORT 空头



**有效方式 (timeInForce):**

  * GTC - Good Till Cancel 成交为止
  * IOC - Immediate or Cancel 无法立即成交(吃单)的部分就撤销
  * FOK - Fill or Kill 无法全部立即成交就撤销
  * GTX - 仅做maker



**响应类型 (newOrderRespType)**

  * ACK
  * RESULT



**订单状态 (order status):**

  * NEW 撮合收到的新建订单
  * REJECTED 订单被拒绝
  * PARTIALLY_FILLED 部分成交
  * FILLED 全部成交
  * CANCELED 已撤销
  * EXPIRED 系统撤销
  * EXPIRED_IN_MATCH 订单被STP过期



**订单种类 (orderTypes, type):**

  * LIMIT 限价单



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



**防止自成交模式 (selfTradePreventionMode):**

  * EXPIRE_TAKER
  * EXPIRE_BOTH
  * EXPIRE_MAKER



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

  * `minPrice` 定义了 `price` 允许的最小值
  * `maxPrice` 定义了 `price` 允许的最大值。
  * `tickSize` 定义了 `price` 的步进间隔，即price必须等于minPrice+(tickSize的整数倍) 以上每一项均可为0，为0时代表这一项不再做限制。



逻辑伪代码如下：

  * 卖单`price` >= `minPrice`
  * 买单`price` <= `maxPrice`
  * (`price`-`minPrice`) % `tickSize` == 0



### LOT_SIZE 订单尺寸

> */exchangeInfo 响应中的格式:**
    
    
    Code
    
      {
        "filterType": "LOT_SIZE",
        "minQty": "0.0100000",
        "maxQty": "1000.00000000",
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



此页面是否有帮助？

Last modified on November 12, 2026

[账户信息流](/zh-CN/docs/products/derivatives-trading-options/user-data-streams)[错误代码](/zh-CN/docs/products/derivatives-trading-options/error-code)