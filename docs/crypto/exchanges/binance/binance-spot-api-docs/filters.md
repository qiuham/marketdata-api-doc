---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/filters
api_type: REST
updated_at: 2026-05-27 18:54:11.974614
---

# Filters

Filters define trading rules on a symbol or an exchange. Filters come in three forms: `symbol filters`, `exchange filters` and `asset filters`.

## Symbol filters[​](/docs/binance-spot-api-docs/filters#symbol-filters "Direct link to Symbol filters")

### PRICE_FILTER[​](/docs/binance-spot-api-docs/filters#price_filter "Direct link to PRICE_FILTER")

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

  * `minPrice` defines the minimum `price`/`stopPrice` allowed; disabled on `minPrice` == 0.
  * `maxPrice` defines the maximum `price`/`stopPrice` allowed; disabled on `maxPrice` == 0.
  * `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by; disabled on `tickSize` == 0.



Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

  * `price` >= `minPrice`
  * `price` <= `maxPrice`
  * `price` % `tickSize` == 0



**/exchangeInfo format:**
    
    
    {  
        "filterType": "PRICE_FILTER",  
        "minPrice": "0.00000100",  
        "maxPrice": "100000.00000000",  
        "tickSize": "0.00000100"  
    }  
    

### PERCENT_PRICE[​](/docs/binance-spot-api-docs/filters#percent_price "Direct link to PERCENT_PRICE")

The `PERCENT_PRICE` filter defines the valid range for an order `price` based on an `average of previous trade prices`.

  * When a non-null [reference price](/docs/binance-spot-api-docs/faqs/price_range_execution_rules) for the symbol exists, it is used in the filter evaluation.
  * When a non-null reference price for the symbol does not exist, then the volume weighted average price over the preceding `avgPriceMins` minutes is used in the filter evaluation. 
    * If `avgPriceMins` is 0, then the last price is used in the filter evaluation.



An order will pass this filter evaluation if:

  * `price` <= `average of previous trade prices` * `multiplierUp`
  * `price` >= `average of previous trade prices` * `multiplierDown`



**/exchangeInfo format:**
    
    
    {  
        "filterType": "PERCENT_PRICE",  
        "multiplierUp": "1.3000",  
        "multiplierDown": "0.7000",  
        "avgPriceMins": 5  
    }  
    

### PERCENT_PRICE_BY_SIDE[​](/docs/binance-spot-api-docs/filters#percent_price_by_side "Direct link to PERCENT_PRICE_BY_SIDE")

The `PERCENT_PRICE_BY_SIDE` filter defines the valid range for an order `price` based on an `average of previous trade prices`.

  * When a non-null [reference price](/docs/binance-spot-api-docs/faqs/price_range_execution_rules) for the symbol exists, it is used in the filter evaluation.
  * When a non-null reference price for the symbol does not exist, then the volume weighted average price over the preceding `avgPriceMins` minutes is used in the filter evaluation. 
    * If `avgPriceMins` is 0, then the last price is used in the filter evaluation.



There is a different range depending on whether an order is placed on the `BUY` side or the `SELL` side.

A `BUY` order will pass this filter evaluation if:

  * `price` <= `average of previous trade prices` * `bidMultiplierUp`
  * `price` >= `average of previous trade prices` * `bidMultiplierDown`



A `SELL` order will pass this filter evaluation if:

  * `price` <= `average of previous trade prices` * `askMultiplierUp`
  * `price` >= `average of previous trade prices` * `askMultiplierDown`



**/exchangeInfo format:**
    
    
    {  
        "filterType": "PERCENT_PRICE_BY_SIDE",  
        "bidMultiplierUp": "1.2",  
        "bidMultiplierDown": "0.2",  
        "askMultiplierUp": "5",  
        "askMultiplierDown": "0.8",  
        "avgPriceMins": 1  
    }  
    

### LOT_SIZE[​](/docs/binance-spot-api-docs/filters#lot_size "Direct link to LOT_SIZE")

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity`/`icebergQty` allowed.
  * `maxQty` defines the maximum `quantity`/`icebergQty` allowed.
  * `stepSize` defines the intervals that a `quantity`/`icebergQty` can be increased/decreased by.



In order to pass the `lot size`, the following must be true for `quantity`/`icebergQty`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



**/exchangeInfo format:**
    
    
    {  
        "filterType": "LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
    }  
    

### MIN_NOTIONAL[​](/docs/binance-spot-api-docs/filters#min_notional "Direct link to MIN_NOTIONAL")

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol.

  * An order's notional value is the `price` * `quantity`.
  * `applyToMarket` determines whether or not the `MIN_NOTIONAL` filter will also be applied to `MARKET` orders. 
    * Since `MARKET` orders have no `price`, an `average of previous trade prices` is used instead. 
      * When a non-null [reference price](/docs/binance-spot-api-docs/faqs/price_range_execution_rules) for the symbol exists, it is used as `price`.
      * When a non-null reference price for the symbol does not exist, then the volume weighted average price over the preceding `avgPriceMins` minutes is used as `price`. 
        * If `avgPriceMins` is 0, then the last price is used as `price`.



An order will pass this filter evaluation if:

  * `price` * `quantity` >= `minNotional`



**/exchangeInfo format:**
    
    
    {  
        "filterType": "MIN_NOTIONAL",  
        "minNotional": "0.00100000",  
        "applyToMarket": true,  
        "avgPriceMins": 5  
    }  
    

### NOTIONAL[​](/docs/binance-spot-api-docs/filters#notional "Direct link to NOTIONAL")

The `NOTIONAL` filter defines the acceptable notional range allowed for an order on a symbol.

  * `applyMinToMarket` determines whether `minNotional` will be applied to `MARKET` orders.
  * `applyMaxToMarket` determines whether `maxNotional` will be applied to `MARKET` orders. 
    * Since `MARKET` orders have no `price`, an `average of previous trade prices` is used instead. 
      * When a non-null [reference price](/docs/binance-spot-api-docs/faqs/price_range_execution_rules) for the symbol exists, it is used as `price`.
      * When a non-null reference price for the symbol does not exist, then the volume weighted average price over the preceding `avgPriceMins` minutes is used as `price`. 
        * If `avgPriceMins` is 0, then the last price is used as `price`.



An order will pass this filter evaluation if:

  * `price` * `quantity` <= `maxNotional`
  * `price` * `quantity` >= `minNotional`



**/exchangeInfo format:**
    
    
    {  
        "filterType": "NOTIONAL",  
        "minNotional": "10.00000000",  
        "applyMinToMarket": false,  
        "maxNotional": "10000.00000000",  
        "applyMaxToMarket": false,  
        "avgPriceMins": 5  
    }  
    

### ICEBERG_PARTS[​](/docs/binance-spot-api-docs/filters#iceberg_parts "Direct link to ICEBERG_PARTS")

The `ICEBERG_PARTS` filter defines the maximum parts an iceberg order can have. The number of `ICEBERG_PARTS` is defined as `CEIL(qty / icebergQty)`.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "ICEBERG_PARTS",  
        "limit": 10  
    }  
    

### MARKET_LOT_SIZE[​](/docs/binance-spot-api-docs/filters#market_lot_size "Direct link to MARKET_LOT_SIZE")

The `MARKET_LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for `MARKET` orders on a symbol. There are 3 parts:

  * `minQty` defines the minimum `quantity` allowed.
  * `maxQty` defines the maximum `quantity` allowed.
  * `stepSize` defines the intervals that a `quantity` can be increased/decreased by.



In order to pass the `market lot size`, the following must be true for `quantity`:

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



**/exchangeInfo format:**
    
    
    {  
        "filterType": "MARKET_LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
    }  
    

### MAX_NUM_ORDERS[​](/docs/binance-spot-api-docs/filters#max_num_orders "Direct link to MAX_NUM_ORDERS")

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol. Note that both "algo" orders and normal orders are counted for this filter.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ORDERS",  
        "maxNumOrders": 25  
    }  
    

### MAX_NUM_ALGO_ORDERS[​](/docs/binance-spot-api-docs/filters#max_num_algo_orders "Direct link to MAX_NUM_ALGO_ORDERS")

The `MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol. "Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 5  
    }  
    

### MAX_NUM_ICEBERG_ORDERS[​](/docs/binance-spot-api-docs/filters#max_num_iceberg_orders "Direct link to MAX_NUM_ICEBERG_ORDERS")

The `MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of `ICEBERG` orders an account is allowed to have open on a symbol. An `ICEBERG` order is any order where the `icebergQty` is > 0.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ICEBERG_ORDERS",  
        "maxNumIcebergOrders": 5  
    }  
    

### MAX_POSITION[​](/docs/binance-spot-api-docs/filters#max_position "Direct link to MAX_POSITION")

The `MAX_POSITION` filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

  1. free balance of the base asset
  2. locked balance of the base asset
  3. sum of the qty of all open BUY orders



`BUY` orders will be rejected if the account's position is greater than the maximum position allowed.

If an order's `quantity` can cause the position to overflow, this will also fail the `MAX_POSITION` filter.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_POSITION",  
        "maxPosition": "10.00000000"  
    }  
    

### TRAILING_DELTA[​](/docs/binance-spot-api-docs/filters#trailing_delta "Direct link to TRAILING_DELTA")

The `TRAILING_DELTA` filter defines the minimum and maximum value for the parameter [`trailingDelta`](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).

In order for a trailing stop order to pass this filter, the following must be true:

For `STOP_LOSS BUY`, `STOP_LOSS_LIMIT_BUY`,`TAKE_PROFIT SELL` and `TAKE_PROFIT_LIMIT SELL` orders:

  * `trailingDelta` >= `minTrailingAboveDelta`
  * `trailingDelta` <= `maxTrailingAboveDelta`



For `STOP_LOSS SELL`, `STOP_LOSS_LIMIT SELL`, `TAKE_PROFIT BUY`, and `TAKE_PROFIT_LIMIT BUY` orders:

  * `trailingDelta` >= `minTrailingBelowDelta`
  * `trailingDelta` <= `maxTrailingBelowDelta`



**/exchangeInfo format:**
    
    
    {  
        "filterType": "TRAILING_DELTA",  
        "minTrailingAboveDelta": 10,  
        "maxTrailingAboveDelta": 2000,  
        "minTrailingBelowDelta": 10,  
        "maxTrailingBelowDelta": 2000  
    }  
    

### MAX_NUM_ORDER_AMENDS[​](/docs/binance-spot-api-docs/filters#max_num_order_amends "Direct link to MAX_NUM_ORDER_AMENDS")

The `MAX_NUM_ORDER_AMENDS` filter defines the maximum number of times an order can be amended on the given symbol.

If there are too many order amendments made on a single order, you will receive the `-2038` error code.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ORDER_AMENDS",  
        "maxNumOrderAmends": 10  
    }  
    

### MAX_NUM_ORDER_LISTS[​](/docs/binance-spot-api-docs/filters#max_num_order_lists "Direct link to MAX_NUM_ORDER_LISTS")

The `MAX_NUM_ORDER_LISTS` filter defines the maximum number of open order lists an account can have on a symbol. Note that OTOCOs count as one order list.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ORDER_LISTS",  
        "maxNumOrderLists": 20  
    }  
    

## Exchange Filters[​](/docs/binance-spot-api-docs/filters#exchange-filters "Direct link to Exchange Filters")

### EXCHANGE_MAX_NUM_ORDERS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_orders "Direct link to EXCHANGE_MAX_NUM_ORDERS")

The `EXCHANGE_MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on the exchange. Note that both "algo" orders and normal orders are counted for this filter.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ORDERS",  
        "maxNumOrders": 1000  
    }  
    

### EXCHANGE_MAX_NUM_ALGO_ORDERS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_algo_orders "Direct link to EXCHANGE_MAX_NUM_ALGO_ORDERS")

The `EXCHANGE_MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on the exchange. "Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 200  
    }  
    

### EXCHANGE_MAX_NUM_ICEBERG_ORDERS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_iceberg_orders "Direct link to EXCHANGE_MAX_NUM_ICEBERG_ORDERS")

The `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of iceberg orders an account is allowed to have open on the exchange.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",  
        "maxNumIcebergOrders": 10000  
    }  
    

### EXCHANGE_MAX_NUM_ORDER_LISTS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_order_lists "Direct link to EXCHANGE_MAX_NUM_ORDER_LISTS")

The `EXCHANGE_MAX_NUM_ORDER_LISTS` filter defines the maximum number of order lists an account is allowed to have open on the exchange. Note that OTOCOs count as one order list.

**/exchangeInfo format:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ORDER_LISTS",  
        "maxNumOrderLists": 20  
    }  
    

## Asset Filters[​](/docs/binance-spot-api-docs/filters#asset-filters "Direct link to Asset Filters")

### MAX_ASSET[​](/docs/binance-spot-api-docs/filters#max_asset "Direct link to MAX_ASSET")

The `MAX_ASSET` filter defines the maximum quantity of an asset that an account is allowed to transact in a single order.

  * When the asset is a symbol's base asset, the limit applies to the order's quantity.
  * When the asset is a symbol's quote asset, the limit applies to the order's notional value.
  * For example, a MAX_ASSET filter for USDC applies to all symbols that have USDC as either a base or quote asset, such as: 
    * USDCBNB
    * BNBUSDC



**/myFilters format:**
    
    
    {  
        "filterType": "MAX_ASSET",  
        "asset": "USDC",  
        "limit": "42.00000000"  
    }

---

# 过滤器

过滤器，即Filter，定义了一系列交易规则。 共有三类，分别是针对交易对的过滤器 `symbol filters`，针对整个交易所的过滤器 `exchange filters` 和针对资产的过滤器 `asset filters`。

## 交易对过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#交易对过滤器 "交易对过滤器的直接链接")

### PRICE_FILTER 价格过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#price_filter-价格过滤器 "PRICE_FILTER 价格过滤器的直接链接")

价格过滤器用于检测order订单中price参数的合法性

  * `minPrice` 定义了 `price`/`stopPrice` 允许的最小值; `minPrice` == 0 的时候则失效。
  * `maxPrice` 定义了 `price`/`stopPrice` 允许的最大值; `maxPrice` == 0 的时候则失效。
  * `tickSize` 定义了 `price`/`stopPrice` 的步进间隔; `tickSize` == 0 的时候则失效。



以上每一项均可为0，为0时代表这一项不再做限制。

订单需满足以下条件，方可通过该过滤器校验：

  * `price` >= `minPrice`
  * `price` <= `maxPrice`
  * `price` % `tickSize` == 0



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "PRICE_FILTER",  
        "minPrice": "0.00000100",  
        "maxPrice": "100000.00000000",  
        "tickSize": "0.00000100"  
    }  
    

### PERCENT_PRICE 价格振幅过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#percent_price-价格振幅过滤器 "PERCENT_PRICE 价格振幅过滤器的直接链接")

`PERCENT_PRICE` 过滤器会根据`前序交易的平均成交价`来定义订单`价格`的有效范围。

  * 当该交易对存在非空的 [参考价格](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules) 时，过滤器校验将使用该参考价格。
  * 当该交易对不存在非空的参考价格时，过滤器校验将使用 `avgPriceMins` 分钟前的成交量加权平均价。 
    * 如果 `avgPriceMins` 为 0，那么过滤器校验将使用最新成交价。



订单需满足以下条件，方可通过该过滤器校验：

  * `price` <= `average of previous trade prices` * `multiplierUp`
  * `price` >= `average of previous trade prices` * `multiplierDown`



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "PERCENT_PRICE",  
        "multiplierUp": "1.3000",  
        "multiplierDown": "0.7000",  
        "avgPriceMins": 5  
    }  
    

#### PERCENT_PRICE_BY_SIDE[​](/docs/zh-CN/binance-spot-api-docs/filters#percent_price_by_side "PERCENT_PRICE_BY_SIDE的直接链接")

`PERCENT_PRICE_BY_SIDE` 过滤器会根据`前序交易的平均成交价`来定义订单`价格`的有效范围。

  * 当该交易对存在非空的 [参考价格](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules) 时，过滤器校验将使用该参考价格。
  * 当该交易对不存在非空的参考价格时，过滤器校验将使用 `avgPriceMins` 分钟前的成交量加权平均价。 
    * `avgPriceMins` 为 0，那么过滤器校验将使用最新成交价。



`买方`订单需满足以下条件，方可通过该过滤器校验：

  * `price` <= `average of previous trade prices` * `bidMultiplierUp`
  * `price` >= `average of previous trade prices` * `bidMultiplierDown`



`卖方`订单需满足以下条件，方可通过该过滤器校验：

  * `price` <= `average of previous trade prices` * `askMultiplierUp`
  * `price` >= `average of previous trade prices` * `askMultiplierDown`



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "PERCENT_PRICE_BY_SIDE",  
        "bidMultiplierUp": "1.2",  
        "bidMultiplierDown": "0.2",  
        "askMultiplierUp": "5",  
        "askMultiplierDown": "0.8",  
        "avgPriceMins": 1  
    }  
    

### LOT_SIZE 订单尺寸[​](/docs/zh-CN/binance-spot-api-docs/filters#lot_size-订单尺寸 "LOT_SIZE 订单尺寸的直接链接")

"lots" 是拍卖术语，这个过滤器对订单中的 `quantity` 也就是数量参数进行合法性检查。包含三个部分：

  * `minQty` 表示 `quantity`/`icebergQty` 允许的最小值.
  * `maxQty` 表示 `quantity`/`icebergQty` 允许的最大值
  * `stepSize` 表示 `quantity`/`icebergQty` 允许的步进值。



订单需满足以下条件，方可通过该过滤器校验：

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
    }  
    

### MIN_NOTIONAL 最小金额[​](/docs/zh-CN/binance-spot-api-docs/filters#min_notional-最小金额 "MIN_NOTIONAL 最小金额的直接链接")

`MIN_NOTIONAL` 过滤器定义了交易对订单所允许的最小名义价值(成交额)。

  * 订单的名义价值是 `价格` * `数量` 。
  * `applyToMarket` 确定 `MIN_NOTIONAL` 过滤器是否也将应用于 `MARKET` 订单。 
    * 由于 `MARKET` 订单没有`价格`，因此会使用`前序交易的平均成交价`。 
      * 当该交易对存在非空的 [参考价格](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules) 时，过滤器校验将使用该参考价格来作为`价格`。
      * 当该交易对不存在非空的参考价格时，过滤器校验将使用 `avgPriceMins` 分钟前的成交量加权平均价来作为`价格`。 
        * 如果 `avgPriceMins` 为 0，那么过滤器校验将使用最新成交价来作为`价格`。



订单需满足以下条件，方可通过该过滤器校验：

  * `price` * `quantity` >= `minNotional`



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "MIN_NOTIONAL",  
        "minNotional": "0.00100000",  
        "applyToMarket": true,  
        "avgPriceMins": 5  
    }  
    

### NOTIONAL 名义价值[​](/docs/zh-CN/binance-spot-api-docs/filters#notional-名义价值 "NOTIONAL 名义价值的直接链接")

名义价值过滤器(`NOTIONAL`)定义了订单在一个交易对上可以下单的名义价值区间。

  * `applyMinToMarket` 定义了 `minNotional` 是否适用于市价单(`MARKET`)。
  * `applyMaxToMarket` 定义了 `maxNotional` 是否适用于市价单(`MARKET`)。 
    * 由于 `MARKET` 订单没有`价格`，因此会使用`前序交易的平均成交价`。 
      * 当该交易对存在非空的 [参考价格](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules) 时，过滤器校验将使用该参考价格来作为`价格`。
      * 当该交易对不存在非空的参考价格时，过滤器校验将使用 `avgPriceMins` 分钟前的成交量加权平均价来作为`价格`。 
        * 如果 `avgPriceMins` 为 0，那么过滤器校验将使用最新成交价来作为`价格`。



订单需满足以下条件，方可通过该过滤器校验：

  * `price` * `quantity` <= `maxNotional`
  * `price` * `quantity` >= `minNotional`



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "NOTIONAL",  
        "minNotional": "10.00000000",  
        "applyMinToMarket": false,  
        "maxNotional": "10000.00000000",  
        "applyMaxToMarket": false,  
        "avgPriceMins": 5  
    }  
    

### ICEBERG_PARTS 冰山订单拆分数[​](/docs/zh-CN/binance-spot-api-docs/filters#iceberg_parts-冰山订单拆分数 "ICEBERG_PARTS 冰山订单拆分数的直接链接")

`ICEBERG_PARTS` 代表冰山订单最多可以拆分成多少个小订单。 计算方法为 `向上取整(qty / icebergQty)`.

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "ICEBERG_PARTS",  
        "limit": 10  
    }  
    

### MARKET_LOT_SIZE 市价订单尺寸[​](/docs/zh-CN/binance-spot-api-docs/filters#market_lot_size-市价订单尺寸 "MARKET_LOT_SIZE 市价订单尺寸的直接链接")

`MARKET_LOT_SIZE`过滤器为交易对上的`MARKET`订单定义了`数量`(即拍卖中的"手数")规则。 共有3部分：

  * `minQty`定义了允许的最小`quantity`。
  * `maxQty`定义了允许的最大数量。
  * `stepSize`定义了可以增加/减少数量的间隔。



为了通过 `market lot size`，`quantity` 必须满足以下条件：

  * `quantity` >= `minQty`
  * `quantity` <= `maxQty`
  * `quantity` % `stepSize` == 0



**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "MARKET_LOT_SIZE",  
        "minQty": "0.00100000",  
        "maxQty": "100000.00000000",  
        "stepSize": "0.00100000"  
    }  
    

### MAX_NUM_ORDERS 最多订单数[​](/docs/zh-CN/binance-spot-api-docs/filters#max_num_orders-最多订单数 "MAX_NUM_ORDERS 最多订单数的直接链接")

定义了某个交易对最多允许的挂单数量（不包括已关闭的订单） 普通订单与条件订单均计算在内

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "MAX_NUM_ORDERS",  
        "maxNumOrders": 25  
    }  
    

### MAX_NUM_ALGO_ORDERS 最多条件单数[​](/docs/zh-CN/binance-spot-api-docs/filters#max_num_algo_orders-最多条件单数 "MAX_NUM_ALGO_ORDERS 最多条件单数的直接链接")

`MAX_NUM_ALGO_ORDERS`过滤器定义允许账户在交易对上开设的"algo"订单的最大数量。 "Algo"订单是`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`和`TAKE_PROFIT_LIMIT`止盈止损单。

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 5  
    }  
    

### MAX_NUM_ICEBERG_ORDERS 最多冰山单数[​](/docs/zh-CN/binance-spot-api-docs/filters#max_num_iceberg_orders-最多冰山单数 "MAX_NUM_ICEBERG_ORDERS 最多冰山单数的直接链接")

`MAX_NUM_ICEBERG_ORDERS`过滤器定义了允许在交易对上开设账户的`ICEBERG`订单的最大数量。 `ICEBERG`订单是icebergQty大于0的任何订单。

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "MAX_NUM_ICEBERG_ORDERS",  
        "maxNumIcebergOrders": 5  
    }  
    

### MAX_POSITION 过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#max_position-过滤器 "MAX_POSITION 过滤器的直接链接")

这个过滤器定义账户允许的基于`base asset`的最大仓位。一个用户的仓位可以定义为如下资产的总和:

  1. `base asset`的可用余额
  2. `base asset`的锁定余额
  3. 所有处于open的买单的数量总和



如果用户的仓位大于最大的允许仓位，买单会被拒绝。

如果一个订单的数量(`quantity`) 可能导致持有仓位溢出, 会触发过滤器 `MAX_POSITION`.

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "MAX_POSITION",  
        "maxPosition": "10.00000000"  
    }  
    

### TRAILING_DELTA 过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#trailing_delta-过滤器 "TRAILING_DELTA 过滤器的直接链接")

此过滤器定义了参数[`trailingDelta`](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)的最大和最小值.

下追踪止损订单, 需要满足条件:

对于 `STOP_LOSS BUY`, `STOP_LOSS_LIMIT_BUY`, `TAKE_PROFIT SELL` 和 `TAKE_PROFIT_LIMIT SELL` 订单:

  * `trailingDelta` >= `minTrailingAboveDelta`
  * `trailingDelta` <= `maxTrailingAboveDelta`



对于 `STOP_LOSS SELL`, `STOP_LOSS_LIMIT SELL`, `TAKE_PROFIT BUY`, 和 `TAKE_PROFIT_LIMIT BUY` 订单:

  * `trailingDelta` >= `minTrailingBelowDelta`
  * `trailingDelta` <= `maxTrailingBelowDelta`



**/exchangeInfo format:**
    
    
    {  
        "filterType": "TRAILING_DELTA",  
        "minTrailingAboveDelta": 10,  
        "maxTrailingAboveDelta": 2000,  
        "minTrailingBelowDelta": 10,  
        "maxTrailingBelowDelta": 2000  
    }  
    

### MAX_NUM_ORDER_AMENDS 过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#max_num_order_amends-过滤器 "MAX_NUM_ORDER_AMENDS 过滤器的直接链接")

此过滤器定义了指定交易对的订单修改次数上限。

如果单笔订单的修改次数过多，您将会收到 `-2038` 错误代码。

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ORDER_AMENDS",  
        "maxNumOrderAmends": 10  
    }  
    

### MAX_NUM_ORDER_LISTS[​](/docs/zh-CN/binance-spot-api-docs/filters#max_num_order_lists "MAX_NUM_ORDER_LISTS的直接链接")

此过滤器定义了账户在交易对上可持有的最大未平仓订单列表数量。请注意，OTOCO 交易计为一个订单列表。

**/exchangeInfo format:**
    
    
    {  
        "filterType": "MAX_NUM_ORDER_LISTS",  
        "maxNumOrderLists": 20  
    }  
    

## 交易所级别过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#交易所级别过滤器 "交易所级别过滤器的直接链接")

### EXCHANGE_MAX_NUM_ORDERS 最多订单数[​](/docs/zh-CN/binance-spot-api-docs/filters#exchange_max_num_orders-最多订单数 "EXCHANGE_MAX_NUM_ORDERS 最多订单数的直接链接")

`EXCHANGE_MAX_NUM_ORDERS`过滤器定义了允许在交易对上开设账户的最大订单数。 请注意，此过滤器同时计算"algo"订单和常规订单。

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ORDERS",  
        "maxNumOrders": 1000  
    }  
    

### EXCHANGE_MAX_NUM_ALGO_ORDERS 最多条件单数[​](/docs/zh-CN/binance-spot-api-docs/filters#exchange_max_num_algo_orders-最多条件单数 "EXCHANGE_MAX_NUM_ALGO_ORDERS 最多条件单数的直接链接")

`EXCHANGE_MAX_NUM_ALGO_ORDERS` 过滤器定义了允许在交易上开设账户的"algo"订单的最大数量。 "Algo"订单是`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`和`TAKE_PROFIT_LIMIT`订单。

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ALGO_ORDERS",  
        "maxNumAlgoOrders": 200  
    }  
    

### EXCHANGE_MAX_NUM_ICEBERG_ORDERS 冰山订单的最大订单数[​](/docs/zh-CN/binance-spot-api-docs/filters#exchange_max_num_iceberg_orders-冰山订单的最大订单数 "EXCHANGE_MAX_NUM_ICEBERG_ORDERS 冰山订单的最大订单数的直接链接")

此过滤器定义了允许账号持有的最大冰山订单数量.

**/exchangeInfo 响应中的格式:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",  
        "maxNumIcebergOrders": 10000  
    }  
    

### EXCHANGE_MAX_NUM_ORDER_LISTS[​](/docs/zh-CN/binance-spot-api-docs/filters#exchange_max_num_order_lists "EXCHANGE_MAX_NUM_ORDER_LISTS的直接链接")

此过滤器定义了允许账号持有的最大未平仓订单列表数量。请注意，OTOCO 交易计为一个订单列表。

**/exchangeInfo format:**
    
    
    {  
        "filterType": "EXCHANGE_MAX_NUM_ORDER_LISTS",  
        "maxNumOrderLists": 20  
    }  
    

## 资产过滤器[​](/docs/zh-CN/binance-spot-api-docs/filters#资产过滤器 "资产过滤器的直接链接")

### MAX_ASSET[​](/docs/zh-CN/binance-spot-api-docs/filters#max_asset "MAX_ASSET的直接链接")

`MAX_ASSET` 过滤器定义了一个账户在单笔订单中可交易的资产最大数量。

  * 当资产是交易对的基础资产时，该限制适用于订单的数量。
  * 当资产是交易对的报价资产时，该限制适用于订单的名义价值。
  * 例如，针对 USDC 的 MAX_ASSET 过滤器适用于所有以 USDC 作为基础资产或报价资产的交易对，例如： 
    * USDCBNB
    * BNBUSDC



**/myFilters format:**
    
    
    {  
        "filterType": "MAX_ASSET",  
        "asset": "USDC",  
        "limit": "42.00000000"  
    }