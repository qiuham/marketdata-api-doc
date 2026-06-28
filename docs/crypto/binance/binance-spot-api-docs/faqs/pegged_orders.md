---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/faqs/pegged_orders
api_type: REST
updated_at: 2026-06-28 18:49:25.315760
---

# Price Range Execution Rule

**Disclaimer:**

  * The symbols and values used here are fictional and do not imply anything about the actual configuration of the live exchange.



## What are execution rules?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-are-execution-rules "Direct link to What are execution rules?")

Execution rules are trading rules that are enforced at the time of order execution. The only execution rule currently available is the Price Range rule.

## What does the Price Range Execution Rule do?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-does-the-price-range-execution-rule-do "Direct link to What does the Price Range Execution Rule do?")

This rule ensures that trades may only be executed at prices within and equal to a price range around a reference price.

## How can I query the execution price range allowed for a symbol?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#how-can-i-query-the-execution-price-range-allowed-for-a-symbol "Direct link to How can I query the execution price range allowed for a symbol?")

Refer to the following endpoints/methods:

API| Request  
---|---  
REST API| `GET /api/v3/executionRules`  
WebSocket API| `executionRules`  
  
## How can I query the reference price?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#how-can-i-query-the-reference-price "Direct link to How can I query the reference price?")

Refer to the following endpoints/methods:

API| Request  
---|---  
REST API| `GET /api/v3/referencePrice`  
WebSocket API| `referencePrice`  
WebSocket Streams| `<symbol>@referencePrice`  
  
Note that the **reference price is continually changing** , so it is recommended to monitor the reference price via WebSocket Streams.

## How does the Price Range Execution Rule work?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#how-does-the-price-range-execution-rule-work "Direct link to How does the Price Range Execution Rule work?")

As an example, given the hypothetical execution rule for this symbol:
    
    
    {  
      "symbolRules": [  
        {  
          "symbol": "BAZUSD",  
          "rules": [  
            {  
              "ruleType": "PRICE_RANGE",  
              "bidLimitMultUp": "2.0000",  
              "bidLimitMultDown": "0.5000",  
              "askLimitMultUp": "2.0000",  
              "askLimitMultDown": "0.5000"  
            }  
          ]  
        }  
      ]  
    }  
    

If the reference price for the symbol is:
    
    
    {  
      "symbol": "BAZUSD",  
      "referencePrice": "10.00",  
      "timestamp": 1770736694138  
    }  
    

This means that at time `1770736694138`:

  1. an order to `BUY` may not execute at a price more than twice the reference price or less than half the reference price and
  2. an order to `SELL` may not execute at a price more than twice the reference price or less than half the reference price.



## What happens if a symbol has no execution rule of type `PRICE_RANGE` and no reference price?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-happens-if-a-symbol-has-no-execution-rule-of-type-price_range-and-no-reference-price "Direct link to what-happens-if-a-symbol-has-no-execution-rule-of-type-price_range-and-no-reference-price")

The Price Range Execution Rule is not enforced on the symbol.

## What happens if a symbol has no execution rule of type `PRICE_RANGE` but does have a reference price?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-happens-if-a-symbol-has-no-execution-rule-of-type-price_range-but-does-have-a-reference-price "Direct link to what-happens-if-a-symbol-has-no-execution-rule-of-type-price_range-but-does-have-a-reference-price")

The Price Range Execution Rule is not enforced on the symbol.

## What happens if a symbol has an execution rule of type `PRICE_RANGE` but does not have a reference price?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-happens-if-a-symbol-has-an-execution-rule-of-type-price_range-but-does-not-have-a-reference-price "Direct link to what-happens-if-a-symbol-has-an-execution-rule-of-type-price_range-but-does-not-have-a-reference-price")

The Price Range Execution Rule is not enforced on the symbol.

## What happens if a symbol has an execution rule of type `PRICE_RANGE` that does not have all four multipliers?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-happens-if-a-symbol-has-an-execution-rule-of-type-price_range-that-does-not-have-all-four-multipliers "Direct link to what-happens-if-a-symbol-has-an-execution-rule-of-type-price_range-that-does-not-have-all-four-multipliers")

When a multiplier is not set, then Price Range Execution Rule is not enforced on the symbol for that order side and price direction. For example, if `bidMultiplierDown` was not present in the hypothetical execution rule above, then an order to `BUY` could execute at any price at or below twice the reference price.

## What happens if the symbol's reference price is `null`?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-happens-if-the-symbols-reference-price-is-null "Direct link to what-happens-if-the-symbols-reference-price-is-null")

The Price Range Execution Rule is not enforced on the symbol.

## When are the execution price limits for an order set?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#when-are-the-execution-price-limits-for-an-order-set "Direct link to When are the execution price limits for an order set?")

When an order enters its taker phase, the reference price is recalculated to set the execution price limits for the order's entire taker phase. Note that a single taker order may match with many maker orders during its taker phase.

## What happens if an order attempts to execute at a price outside of the allowed price range?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#what-happens-if-an-order-attempts-to-execute-at-a-price-outside-of-the-allowed-price-range "Direct link to What happens if an order attempts to execute at a price outside of the allowed price range?")

If a taker order attempts to execute at a price outside of the allowed price range, it will be expired (i.e. status: `EXPIRED`) with the expiry reason `EXECUTION_RULE_PRICE_RANGE_EXCEEDED`.

Service| Reference  
---|---  
Non-FIX APIs| `expiryReason`  
FIX APIs| `ExpiryReason <25056>`  
User Data Stream| `"eR"`  
  
## How is the reference price calculated?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#how-is-the-reference-price-calculated "Direct link to How is the reference price calculated?")

If the reference price is being calculated by the Matching Engine, then a query for the reference price calculation returns `"calculationType": "ARITHMETIC_MEAN"`.

If the reference price is being calculated outside the matching engine, then a query for the reference price calculation returns `"calculationType": "EXTERNAL"`. See below for more details.

## How does the Matching Engine calculate the reference price?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#how-does-the-matching-engine-calculate-the-reference-price "Direct link to How does the Matching Engine calculate the reference price?")

The matching engine calculates the reference price as a simple moving average of trade prices over a time window. The calculation is configured with a bucket width in milliseconds (`bucketWidthMs`) and the number of buckets (`bucketCount`). The bucket width multiplied by the number of buckets defines the size of the time window.

When a trade occurs, the matching engine captures the trade price and adds it to the current bucket. Each bucket has

  * an open time, which is aligned to engine time modulo the bucket width
  * a trade count, which is a fixed-point integer with four decimal places of precision
  * a sum of all the trade prices represented in that bucket, which is a fixed-point integer with an extra four decimal places of precision over the quote asset precision.



The matching engine calculates the average of a particular bucket by dividing the sum by the trade count. The first trade for a given open time creates a bucket and the matching engine gradually accumulates buckets as trades happen. The matching engine drops a bucket when its close time is outside the time window. This means that:

  * The oldest bucket at any given time likely has an open time outside of the time window and a close time inside of the time window.
  * The maximum number of buckets tracked by the engine is actually 1 more than the configured `bucketCount`.



The remainder of this explanation refers to the oldest time in the time window as the "cutoff time".

When the oldest bucket straddles the cutoff time, its contents are _prorated_ :

  * The fraction of the bucket outside the moving window is: (cutoff time - the bucket's open time) divided by the bucket width. Call this the "expired fraction."
  * The bucket's trade count is reduced by the expired fraction.
  * The bucket's sum is reduced by the expired fraction.
  * The open time is set to the cutoff time.



The reference price is the total of the sum in each bucket divided by the total of the trade count in each bucket. Division is truncating integer division.

## How are reference prices calculated outside the matching engine?[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#how-are-reference-prices-calculated-outside-the-matching-engine "Direct link to How are reference prices calculated outside the matching engine?")

If the reference price is being calculated outside the matching engine, then a query for the reference price calculation returns `"externalCalculationId":` followed by an integer number. Each of these numbers indicates a different calculation method.

## External Reference Price Calculation Method 0[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#external-reference-price-calculation-method-0 "Direct link to External Reference Price Calculation Method 0")

The reference price was set manually by a human operator. This calculation method will only be used in situations when algorithmic calculation of the reference price has been deemed unsuitable.

## External Reference Price Calculation Method 1[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#external-reference-price-calculation-method-1 "Direct link to External Reference Price Calculation Method 1")

The reference price is calculated as the average of the trading price from 4 external data providers.

## External Reference Price Calculation Method 2[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#external-reference-price-calculation-method-2 "Direct link to External Reference Price Calculation Method 2")

The reference price is the index price of the corresponding USDⓈ-M Binance Futures.

## External Reference Price Calculation Method 3[​](/docs/binance-spot-api-docs/faqs/price_range_execution_rules#external-reference-price-calculation-method-3 "Direct link to External Reference Price Calculation Method 3")

The reference price is calculated as the 5 minute SMA of the Binance Spot mid-spread price.

---

# 价格区间执行规则

**免责声明：**

  * 此处使用的交易对和数值均为虚构，不代表实际交易所的配置。



## 什么是执行规则？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#什么是执行规则 "什么是执行规则？的直接链接")

执行规则是在订单执行时强制执行的交易规则。目前唯一可用的执行规则是价格区间规则。

## 价格区间执行规则的作用是什么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#价格区间执行规则的作用是什么 "价格区间执行规则的作用是什么？的直接链接")

该规则确保交易只能在参考价格附近的价格区间内（包括区间边界）执行。

## 如何查询某个交易对允许的执行价格区间？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如何查询某个交易对允许的执行价格区间 "如何查询某个交易对允许的执行价格区间？的直接链接")

请参考以下接口/方法：

API| 请求  
---|---  
REST API| `GET /api/v3/executionRules`  
WebSocket API| `executionRules`  
  
## 如何查询参考价格？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如何查询参考价格 "如何查询参考价格？的直接链接")

请参考以下接口/方法：

API| 请求  
---|---  
REST API| `GET /api/v3/referencePrice`  
WebSocket API| `referencePrice`  
WebSocket 数据流| `<symbol>@referencePrice`  
  
请注意，**参考价格是持续变化的** ，建议通过 WebSocket 数据流实时监控参考价格。 

## 价格区间执行规则如何工作？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#价格区间执行规则如何工作 "价格区间执行规则如何工作？的直接链接")

举例说明，假设该交易对的执行规则如下：
    
    
    {  
      "symbolRules": [  
        {  
          "symbol": "BAZUSD",  
          "rules": [  
            {  
              "ruleType": "PRICE_RANGE",  
              "bidLimitMultUp": "2.0000",  
              "bidLimitMultDown": "0.5000",  
              "askLimitMultUp": "2.0000",  
              "askLimitMultDown": "0.5000"  
            }  
          ]  
        }  
      ]  
    }  
    

如果该交易对的参考价格为：
    
    
    {  
      "symbol": "BAZUSD",  
      "referencePrice": "10.00",  
      "timestamp": 1770736694138  
    }  
    

这意味着在时间点 `1770736694138`：

  1. 买入订单的执行价格不得高于参考价格的两倍，也不得低于参考价格的一半。
  2. 卖出订单的执行价格不得高于参考价格的两倍，也不得低于参考价格的一半。



## 如果某个交易对没有类型为 `PRICE_RANGE` 的执行规则，也没有参考价格，会发生什么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如果某个交易对没有类型为-price_range-的执行规则也没有参考价格会发生什么 "如果某个交易对没有类型为-price_range-的执行规则也没有参考价格会发生什么的直接链接")

该交易对不会强制执行价格区间执行规则。

## 如果某个交易对没有类型为 `PRICE_RANGE` 的执行规则，但有参考价格，会发生什么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如果某个交易对没有类型为-price_range-的执行规则但有参考价格会发生什么 "如果某个交易对没有类型为-price_range-的执行规则但有参考价格会发生什么的直接链接")

该交易对不会强制执行价格区间执行规则。

## 如果某个交易对有类型为 `PRICE_RANGE` 的执行规则，但没有参考价格，会发生什么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如果某个交易对有类型为-price_range-的执行规则但没有参考价格会发生什么 "如果某个交易对有类型为-price_range-的执行规则但没有参考价格会发生什么的直接链接")

该交易对不会强制执行价格区间执行规则。

## 如果某个交易对有类型为 `PRICE_RANGE` 的执行规则，但没有全部四个乘数，会发生什么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如果某个交易对有类型为-price_range-的执行规则但没有全部四个乘数会发生什么 "如果某个交易对有类型为-price_range-的执行规则但没有全部四个乘数会发生什么的直接链接")

当某个乘数未设置时，该交易对在对应的订单方向和价格方向上不会强制执行价格区间执行规则。 例如，如果执行规则中没有 `bidMultiplierDown`，那么一笔 `BUY` 订单可以在低于或等于参考价格两倍的任意价格成交。

## 如果该交易对的参考价格为 `null`，会发生什么？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如果该交易对的参考价格为-null会发生什么 "如果该交易对的参考价格为-null会发生什么的直接链接")

该交易对不会强制执行价格区间执行规则。

## 订单的执行价格限制何时设定？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#订单的执行价格限制何时设定 "订单的执行价格限制何时设定？的直接链接")

当订单进入吃单阶段时，会重新计算参考价格，以设定该订单整个吃单阶段的执行价格限制。请注意，单个吃单订单在其吃单阶段可能会与多个挂单订单匹配。

## 如果订单尝试以超出允许价格区间的价格执行，会发生什么[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#如果订单尝试以超出允许价格区间的价格执行会发生什么 "如果订单尝试以超出允许价格区间的价格执行，会发生什么的直接链接")

如果吃单尝试以超出允许价格区间的价格执行，该订单将会过期（状态为 `EXPIRED`），过期原因是 `EXECUTION_RULE_PRICE_RANGE_EXCEEDED`。

服务| 参考字段  
---|---  
非FIX接口| `expiryReason`  
FIX接口| `ExpiryReason <25056>`  
用户数据流| `"eR"`  
  
## 参考价格是如何计算的？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#参考价格是如何计算的 "参考价格是如何计算的？的直接链接")

如果参考价格由撮合引擎计算，则查询参考价格计算方式时返回 `"calculationType": "ARITHMETIC_MEAN"`。

如果参考价格由撮合引擎外部计算，则查询参考价格计算方式时返回 `"calculationType": "EXTERNAL"`。详情见下文。

## 撮合引擎如何计算参考价格？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#撮合引擎如何计算参考价格 "撮合引擎如何计算参考价格？的直接链接")

撮合引擎将参考价格计算为一段时间窗口内交易价格的简单移动平均。计算配置包括毫秒级的桶宽（`bucketWidthMs`）和桶数量（`bucketCount`）。桶宽乘以桶数量定义了时间窗口大小。

当发生交易时，撮合引擎会记录该交易价格并将其添加到当前的时间桶中。每个时间桶包含：

  * 开始时间（open time），该时间是引擎时间与桶宽度取模
  * 交易数量（trade count），以固定小数点表示，精确到小数点后四位
  * 该时间桶内所有交易价格的总和，以固定小数点表示，精度比报价资产的精度多四位小数



撮合引擎通过将总和除以交易数量计算该桶的平均价格。某个开始时间的第一个交易创建该桶，随着交易发生，撮合引擎逐渐累积桶。当桶的结束时间超出时间窗口时，该桶会被丢弃。这意味着：

  * 当前时间点最旧的桶的开始时间可能在时间窗口之外，但结束时间在时间窗口内。
  * 引擎维护的最大桶数实际上比配置的 `bucketCount` 多1。



以下说明中，将时间窗口的最旧时间称为“截止时间”。

当最旧的桶跨越截止时间时，其内容会被按比例调整：

  * 桶外过期部分的比例为：（截止时间 - 桶的开始时间）除以桶宽，称为“过期比例”。
  * 桶的交易数量按过期比例减少。
  * 桶的总和按过期比例减少。
  * 桶的开始时间设置为截止时间。



参考价格为所有桶的总和除以所有桶的交易数量，除法为截断式整数除法。

## 外部计算参考价格的方式？[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#外部计算参考价格的方式 "外部计算参考价格的方式？的直接链接")

如果参考价格由撮合引擎外部计算，则查询参考价格计算方式时返回 `"externalCalculationId":` 后跟一个整数。每个数字代表不同的计算方法。

## 外部参考价格计算方法 0[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#外部参考价格计算方法-0 "外部参考价格计算方法 0的直接链接")

参考价格由人工手动设置。该计算方法仅在不适合使用算法计算参考价格的情况下使用。

## 外部参考价格计算方法 1[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#外部参考价格计算方法-1 "外部参考价格计算方法 1的直接链接")

参考价格为 4 个外部数据提供方的交易价格的平均值。

## 外部参考价格计算方法 2[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#外部参考价格计算方法-2 "外部参考价格计算方法 2的直接链接")

参考价格为对应的 USDⓈ-M 币安合约的指数价格。

## 外部参考价格计算方法 3[​](/docs/zh-CN/binance-spot-api-docs/faqs/price_range_execution_rules#外部参考价格计算方法-3 "外部参考价格计算方法 3的直接链接")

参考价格为币安现货买卖中间价的 5 分钟简单移动平均值（SMA）。