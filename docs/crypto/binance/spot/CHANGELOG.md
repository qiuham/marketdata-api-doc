---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/CHANGELOG
api_type: REST
updated_at: 2026-11-13 20:24:28.887696
---

# CHANGELOG for Binance's API

**Last Updated: 2026-11-11**

### 2026-11-11

  * Error code documentation corrections:
    * `PARAM_OVERFLOW` is [`-1018`](/en/docs/products/spot/errors#-1018-param_overflow). It was previously documented as `-1108`.
    * [`-1108 BAD_ASSET`](/en/docs/products/spot/errors#-1108-bad_asset) "Invalid asset." is now documented. It was previously documented in the testnet [changelog](/en/docs/products/spot/testnet/CHANGELOG#2026-10-28).



**Notice: The changes in this section are being rolled out gradually, and will take approximately two weeks to complete.**

#### New Features

  * `userDataStream.subscribe` and `userDataStream.subscribe.signature` now accept an optional `filter` parameter controlling which events are delivered. Supports filtering by event type (`e`), symbol (`s`), asset (`a`), and execution type (`x`).
    * WebSocket API: See [User Data Stream Subscription Filters](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters).
    * Unknown symbols and assets in `filter` are rejected with [`-1121`](/en/docs/products/spot/errors#-1121-bad_symbol) and [`-1108`](/en/docs/products/spot/errors#-1108-bad_asset) respectively.



#### General Changes

  * The `serverShutdown` event payload now includes a `T` field indicating when the WebSocket session will be shut down.
    * [WebSocket API](/en/docs/products/spot/web-socket-api#server-shutdown)
    * [WebSocket Streams](/en/docs/products/spot/web-socket-streams#server-shutdown)
    * [SBE Market Data Streams](/en/docs/products/spot/sbe-market-data-streams#server-shutdown)
    * In SBE sessions, the `T` field is only present in SBE schema 3:6 and later.
  * The error message from `-1015 TOO_MANY_ORDERS` has been changed to "Too many orders placed without trading; current limit is X non-trading orders per Y. Unable to place new orders until trades occur or window resets." See [`-1015`](/en/docs/products/spot/errors#-1015-too_many_orders) and the [Spot Unfilled Order Count Rules FAQ](/en/docs/products/spot/faqs/order_count_decrement#spot-unfilled-order-count-rules).



#### SBE

  * REST and WebSocket API SBE schema [spot_3_6.xml](/en/docs/products/spot/sbe/schemas/spot_3_6.xml)
    * The current schema 3:5 [spot_3_5.xml](/en/docs/products/spot/sbe/schemas/spot_3_5.xml) is deprecated and will be retired in 6 months per our [schema deprecation policy](/en/docs/products/spot/faqs/sbe_faq#regarding-legacy-support).
    * Changes in schema 3:6:
      * Existing `expiryReason` enum: new variants `Exhausted` (9) and `InsufficientQuoteNotionalLimit` (10)
      * `ServerShutdownEvent`: new field `shutdownTime`
      * `ExchangeInfoResponse` (symbols group): new fields `marketQuoteNotionalLimitAllowed`, `limitQuoteNotionalLimitAllowed`, `opoAllowed`
      * `NewOrderResultResponse`, `NewOrderFullResponse`, `OrderResponse`, `CancelOrderResponse`, `OrdersResponse`, `NewOrderListResultResponse`, `NewOrderListFullResponse`, `CancelOrderListResponse`, `OrderAmendKeepPriorityResponse`, `ExecutionReportEvent`: new field `quoteNotionalLimit`
        * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.
      * `ExecutionReportEvent`: new field `effectiveSelfTradePreventionMode`
        * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.
      * `NewOrderFullResponse` and `NewOrderListFullResponse.orderReports` `preventedMatches` group: new field `effectiveSelfTradePreventionMode`
        * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.
    * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.
  * FIX SBE schema [spot-fixsbe-1_2.xml](/en/docs/products/spot/sbe/schemas/spot-fixsbe-1_2.xml)
    * The current schema 1:1 [spot-fixsbe-1_1.xml](/en/docs/products/spot/sbe/schemas/spot-fixsbe-1_1.xml) is deprecated and will be retired in 6 months per our [schema deprecation policy](/en/docs/products/spot/faqs/sbe_faq#regarding-legacy-support).
    * Changes in schema 1:2:
      * Existing `expiryReason` enum: new variants `Exhausted` (9) and `InsufficientQuoteNotionalLimit` (10)
      * `ExecutionReport`, `OrderCancelRequestAndNewOrderSingle`, `NewOrderSingle`, `NewOrderList` (`Orders` group): new field `QuoteNotionalLimit` (custom tag 25057)
        * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.
      * `ExecutionReport`: new field `EffectiveSelfTradePreventionMode` (custom tag 25058)
        * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.
    * The [FIX SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_fix_schema_lifecycle_prod.json) has been updated to reflect this change.



#### FIX API

  * The [QuickFix schema for FIX OE](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml) has been updated:
    * `ExpiryReason` (custom tag 25056): new values `EXHAUSTED` (9) and `INSUFFICIENT_QUOTE_NOTIONAL_LIMIT` (10)
    * `ExecutionReport`, `OrderCancelRequestAndNewOrderSingle`, `NewOrderSingle`, `NewOrderList` (`Orders` group): new field `QuoteNotionalLimit` (custom tag 25057)
      * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.
    * `ExecutionReport`: new field `EffectiveSelfTradePreventionMode` (custom tag 25058)
      * For more details on this field, see [New Features](/en/docs/products/spot/CHANGELOG#2026-11-20-new-features) below.



**Notice: The following changes will be available after 2026-11-20 07:00 UTC.**

#### New Features

  * Orders on the `BUY` side accept a new optional parameter `quoteNotionalLimit`, which limits the amount of the quote asset the order can spend. **The time this feature will be enabled has not been decided.**
    * Order lists accept `aboveQuoteNotionalLimit` / `belowQuoteNotionalLimit` (OCO) and `workingQuoteNotionalLimit` / `pendingQuoteNotionalLimit` / `pendingAboveQuoteNotionalLimit` / `pendingBelowQuoteNotionalLimit` (OTO, OTOCO, OPO, OPOCO). See [Quote Notional Limit FAQ](/en/docs/products/spot/faqs/quoteNotionalLimit).
    * [REST API](/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info) and [WebSocket API](/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info) `exchangeInfo` responses show whether a symbol supports the parameter in the new fields `marketQuoteNotionalLimitAllowed` and `limitQuoteNotionalLimitAllowed`.
    * The new `expiryReason` value [`INSUFFICIENT_QUOTE_NOTIONAL_LIMIT`](/en/docs/products/spot/enums#expiry-reasons) is emitted when the order's `quoteNotionalLimit` prevents the remaining quantity from executing or resting.
    * SOR endpoints parse the parameter but reject it with [`-1106`](/en/docs/products/spot/errors#-1106-param_not_required).
    * The legacy OCO endpoints (REST API `POST /api/v3/order/oco`, WebSocket API `orderList.place`) do not accept the new parameters.
  * User Data Stream [`executionReport`](/en/docs/products/spot/user-data-stream#order-update) events, FIX API [`ExecutionReport<8>`](/en/docs/products/spot/fix-api#executionreport-8) messages, and FULL order response `preventedMatches[]` entries now carry an optional `effectiveSelfTradePreventionMode` (`eV` on JSON streams, FIX tag `25058`) distinguishing the STP mode the engine applied from the one the order was placed with. The field is only emitted on prevented-match reports and only when the applied mode differs from the order's own `selfTradePreventionMode`. Values: `EXPIRE_MAKER`, `EXPIRE_BOTH`, `DECREMENT` (never `NONE`, `EXPIRE_TAKER` or `TRANSFER`).



#### General Changes

  * Orders amended down to their filled quantity or less now carry `expiryReason` = [`EXHAUSTED`](/en/docs/products/spot/enums#expiry-reasons). Previously, these orders expired without an `expiryReason`.
  * `BUY` limit orders that trade on entry and then rest now release any order lock above what the remaining quantity needs to rest (remaining quantity × limit price). The surplus, usually the price improvement from the trade, is returned to `free` in the same balance update that the order rests in. Previously, the surplus stayed locked until the order ended.
    * Applies to `LIMIT` `GTC` orders, triggered `STOP_LOSS_LIMIT` and `TAKE_PROFIT_LIMIT` orders, limit orders in order lists, and SOR orders. Iceberg orders keep the lock for their whole remaining quantity, including the hidden part.



#### Bug Fixes

  * SBE responses for canceling an order list now encode `listClientOrderId` as the `listClientOrderId` of the original order list, matching the JSON response. Previously, SBE responses encoded the `listClientOrderId` sent in the cancel request.
    * REST API: `DELETE /api/v3/orderList`, `DELETE /api/v3/openOrders`
    * WebSocket API: `orderList.cancel`, `openOrders.cancelAll`



* * *

### 2026-10-30

REST and WebSocket API:

  * Reminder that SBE 3:3 schema will be retired on 2026-11-09, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2026-10-27

  * Added ExpiryReason(25056) in the [FIX API documentation](/en/docs/products/spot/fix-api#executionreport-8) which was previously undocumented but was announced in an [earlier update](/en/docs/products/spot/CHANGELOG#2026-03-09).



* * *

### 2026-09-18

REST and WebSocket API:

  * Reminder that SBE 3:2 schema will be retired on 2026-09-25, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



FIX API:

  * Reminder that FIX SBE 1:0 schema will be retired on 2026-09-25, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [FIX SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_fix_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2026-09-02

#### FIX API

  * Removed the top-level `Symbol (55)` field from `ListStatus <N>` in the [QuickFIX Order Entry schema](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml) and API documentation since, as [previously announced](/en/docs/products/spot/CHANGELOG#2025-12-02) the API no longer emits this field.



* * *

### 2026-07-27

  * Updated [Price Range Execution Rule](/en/docs/products/spot/faqs/price_range_execution_rules#external-reference-price-calculation-method-4) with additional External Reference Price Calculation Methods.



* * *

### 2026-07-17

The following will occur on **2026-08-04 at approximately 07:00 UTC**.

  * The update speed of the below SBE Market Data Streams will be changed **from 25ms to 20ms** :
    * SBE Market Data Streams: [Diff Depth Streams](/en/docs/products/spot/sbe-market-data-streams#diff-depth-streams)
    * FIX SBE: [MarketDataIncrementalDepth](/en/docs/products/spot/fix-api#marketdataincrementaldepth)



* * *

### 2026-07-01

**Notice: The following changes will occur on 2026-07-07 and will take a few days to complete.**

#### New Features

  * The new `symbolStatus` value `CANCEL_ONLY` can appear in Exchange Information responses.
    * REST API: `GET /api/v3/exchangeInfo`
    * WebSocket API: `exchangeInfo`
  * REST and WebSocket API SBE schema [spot_3_5.xml](/en/docs/products/spot/sbe/schemas/spot_3_5.xml)
    * The current schema 3:4 [spot_3_4.xml](/en/docs/products/spot/sbe/schemas/spot_3_4.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
    * Changes in schema 3:5:
      * Updated `symbolStatus` enum: new variant `CANCEL_ONLY`



* * *

### 2026-06-24

  * Beginning at **2026-07-09 07:00 UTC** , [WebSocket Streams](/en/docs/products/spot/web-socket-streams) will undergo an infrastructure upgrade and will approximately take up to an hour.
  * During the upgrade, your WebSocket connection may be disconnected; please reconnect to restore your connection.



* * *

### 2026-06-22

REST and WebSocket API:

  * Reminder that SBE 3:1 schema will be retired on 2026-06-29, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2026-06-10

#### FIX API

  * Documentation update: removed `LastFragment (893)` from [FIX API](/en/docs/products/spot/fix-api#marketdataincrementalrefresh).
    * As [previously announced](/en/docs/products/spot/CHANGELOG#2025-12-02), `MarketDataIncrementalRefresh <X>` messages stopped being fragmented on 2025-12-18, and the server no longer sends `LastFragment (893)`.
    * The field has been removed from the [FIX API](/en/docs/products/spot/fix-api) field list and from the corresponding [QuickFIX MD schema](/en/docs/products/spot/fix/schemas/spot-fix-md.xml).
  * Documentation update: updated the [News `<B>`](/en/docs/products/spot/fix-api#news-b) message description to be consistent with the announcement from [2026-06-09](/en/docs/products/spot/CHANGELOG#2026-06-09).



* * *

### 2026-06-09

**Update:**

  * Updated the [Price Range Execution Rule FAQ](/en/docs/products/spot/faqs/price_range_execution_rules#external-reference-price-calculation-method-1) with new External Reference Price Calculation Methods.



The `serverShutdown` event will be sent when the **server is about to be shut down** ; when you receive this event, please disconnect and open a new connection.

All mention of a fixed time before the server shuts down has been removed from the documentation.

  * Documented the `serverShutdown` event in [SBE Market Data Streams](/en/docs/products/spot/sbe-market-data-streams#server-shutdown).
    * ~~`serverShutdown` event will be sent 10 minutes before disconnection.~~
    * Please establish a new connection as soon as possible to prevent connection interruption.
    * Note that you will receive `serverShutdown` events in JSON in WebSocket text frames.



* * *

### 2026-05-11

The following rollout will occur at **approximately 07:00 UTC on 2026-05-12**.

  * Added WebSocket Stream support for [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425).
    * New stream:
      * `<symbol>@blockTrade`



* * *

### 2026-05-06

**Notice: The following changes will be deployed on 2026-05-08, starting at 06:00 UTC and may take several hours to complete.**

  * Added `serverShutdown` event to [WebSocket API](/en/docs/products/spot/web-socket-api#server-shutdown) and [WebSocket Streams](/en/docs/products/spot/web-socket-streams#server-shutdown).

    * `serverShutdown` event will be sent 10 minutes before disconnection.
  * [`PERCENT_PRICE`](/en/docs/products/spot/filters#percent_price), [`PERCENT_PRICE_BY_SIDE`](/en/docs/products/spot/filters#percent_price_by_side), [`MIN_NOTIONAL`](/en/docs/products/spot/filters#min_notional), and [`NOTIONAL`](/en/docs/products/spot/filters#notional) filters now use [reference price](/en/docs/products/spot/faqs/price_range_execution_rules) when it exists and is non-null. The filters fall back to their previous behavior when the reference price does not exist or is null.

  * Market data for [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425).

    * New Endpoints/Methods
      * REST API:
        * `GET /api/v3/historicalBlockTrades`
      * WebSocket API:
        * `blockTrades.historical`
  * Order query responses may include an [`expiryReason`](/en/docs/products/spot/enums#expiry-reasons) field.

    * This field is returned **only for expired orders** and helps users understand why an order expired, including cases where the order is expired due to the **execution price range rule**.
    * This field is included in both JSON and SBE 3:4 responses.
    * This applies to the following endpoint/method:
      * REST API:
        * `GET /api/v3/order`
        * `GET /api/v3/allOrders`
        * `GET /api/v3/orderList`
        * `GET /api/v3/allOrderList`
      * WebSocket API:
        * `order.status`
        * `allOrders`
        * `orderList.status`
        * `allOrderLists`
  * REST and WebSocket API SBE schema 3:4

    * The current schema 3:3 [spot_3_3.xml](/en/docs/products/spot/sbe/schemas/spot_3_3.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
    * Changes in schema 3:4:
      * New message `BlockTradesResponse`
      * New type `blockTradeId`
      * New field `expiryReason` in `OrderResponse` and `OrdersResponse`



* * *

### 2026-04-28

  * Corrected the JSON in the `Price Range Execution Rule FAQ` for the question [`How does the Price Range Execution Rule work?`](/en/docs/products/spot/faqs/price_range_execution_rules#how-does-the-price-range-execution-rule-work).



* * *

### 2026-04-17

The following will occur on **2026-05-05 at approximately 10:00 UTC**.

  * The update speed of the below SBE Market Data Streams will be changed **from 50ms to 25ms** :
    * SBE Market Data Streams: [Diff Depth Streams](/en/docs/products/spot/sbe-market-data-streams#diff-depth-streams)
    * FIX SBE: [MarketDataIncrementalDepth](/en/docs/products/spot/fix-api#marketdataincrementaldepth)



* * *

### 2026-04-16

  * Updated the documentation to clarify that if a symbol has never had a reference price set, an error code [`-2043`](/en/docs/products/spot/errors#-2043-no_reference_price) is returned when querying the reference price. This applies to the following endpoint/method:
    * REST API: `GET /api/v3/referencePrice`
    * WebSocket API: `referencePrice`



* * *

### 2026-04-06

  * Updated [Price Range Execution Rule](/en/docs/products/spot/faqs/price_range_execution_rules#what-happens-if-a-symbol-has-no-execution-rule-of-type-price_range-and-no-reference-price) with additional information on rule enforcement.



* * *

### 2026-04-02

Clarifcation on the announcement from [2026-03-27](/en/docs/products/spot/CHANGELOG#2026-03-27) regarding new behavior for request weight charged on selected endpoints:

For orders that are amended, the request weight only becomes 0 when the order expires because of the amendment. Successful requests that do not cause the order to expire are still charged the documented weight. Failed requests are still charged the documented weight.

This applies to the following endpoint and method:

  * REST API: `PUT /api/v3/order/amend/keepPriority`
  * WebSocket API: `order.amend.keepPriority`



* * *

### 2026-03-30

  * Updated [Price Range Execution Rule](/en/docs/products/spot/faqs/price_range_execution_rules#when-are-the-execution-price-limits-for-an-order-set) to explain execution price limits for an order.



* * *

### 2026-03-27

The following will occur on **2026-04-02 at approximately 07:00 UTC**.

  * `RAW_REQUESTS` rate limit increases to 300,000 per 5 minutes.

  * Request weights for the following endpoints and methods become 0 when the request is successful. Failed requests are still charged the documented weight. IPs that only call these endpoints and methods successfully will never hit the `REQUEST_WEIGHT` rate limit.

    * REST API
      * `POST /api/v3/order`
      * `POST /api/v3/sor/order`
      * `DELETE /api/v3/order`
      * `DELETE /api/v3/openOrders`
      * `POST /api/v3/order/cancelReplace`
      * `POST /api/v3/order/oco`
      * `POST /api/v3/orderList/oco`
      * `POST /api/v3/orderList/oto`
      * `POST /api/v3/orderList/otoco`
      * `POST /api/v3/orderList/opo`
      * `POST /api/v3/orderList/opoco`
      * `DELETE /api/v3/orderList`
      * `PUT /api/v3/order/amend/keepPriority` (see [2026-04-02](/en/docs/products/spot/CHANGELOG#2026-04-02) for an update)
    * WebSocket API
      * `order.place`
      * `sor.order.place`
      * `order.cancel`
      * `openOrders.cancelAll`
      * `order.cancelReplace`
      * `orderList.place`
      * `orderList.place.oco`
      * `orderList.place.oto`
      * `orderList.place.otoco`
      * `orderList.place.opo`
      * `orderList.place.opoco`
      * `orderList.cancel`
      * `order.amend.keepPriority` (see [2026-04-02](/en/docs/products/spot/CHANGELOG#2026-04-02) for an update)
  * [STP Transfer](/en/docs/products/spot/faqs/stp_faq) will be allowed on all symbols on **2026-04-02 at approximately 07:00 UTC**.




* * *

### 2026-03-13

  * Updated [Price Range Execution Rule](/en/docs/products/spot/faqs/price_range_execution_rules#external-reference-price-calculation-method-0) with a new External Reference Price Calculation Method.



* * *

### 2026-03-11

**Notice:** FIX TLS Connectivity Update on **2026-06-08** , starting from **03:00 UTC** and will take about 1 hour to complete.

**Action Required:**

During the update window, existing FIX connections may drop intermittently. To ensure successful reconnections and new connections afterward, please verify before our update that your client sends SNI (Server Name Indication) during the TLS handshake and validates the certificate against the requested hostname.  Clients without SNI may receive an error message during handshake related to incorrect certificate during or after the update window, leading to TLS handshake or hostname verification failures. This can occur with some Node.js clients if SNI is not explicitly configured. Please consult the [FIX API documentation](/en/docs/products/spot/fix-api#general-api-information) for full context.

* * *

### 2026-03-10

  * Clarified about the reference price calculation for [Price Range Execution Rule](/en/docs/products/spot/faqs/price_range_execution_rules#how-does-the-matching-engine-calculate-the-reference-price)



* * *

### 2026-03-09

**Notice:** The changes in this section will be gradually rolled out and will take approximately three weeks to complete.

#### New Features

  * [Price Range Execution Rule](/en/docs/products/spot/faqs/price_range_execution_rules)
    * New Endpoints/Methods
      * REST API:
        * `GET /api/v3/executionRules`
        * `GET /api/v3/referencePrice`
        * `GET /api/v3/referencePrice/calculation`
      * WebSocket API:
        * `executionRules`
        * `referencePrice`
        * `referencePrice.calculation`
    * New JSON Stream: `<symbol>@referencePrice`
  * REST and WebSocket API SBE schema 3:3
    * The current schema 3:2 [spot_3_2.xml](/en/docs/products/spot/sbe/schemas/spot_3_2.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
    * Changes in schema 3:3:
      * New message `ExecutionRulesResponse`
      * New message `PriceRangeExecutionRule` (to be embedded in `ExecutionRulesResponse`)
      * New message `ReferencePriceResponse`
      * New message `ReferencePriceCalculationResponse`
      * New enum `executionRuleType`
      * New enum `expiryReason`
      * New enum `calculationType`
      * New field `expiryReason` in `NewOrderResultResponse`, `NewOrderFullResponse`, `NewOrderListResultResponse` and `NewOrderListFullResponse`
      * New field `expiryReason` in `ExecutionReportEvent`
      * New message `ServerShutdownEvent` for WebSocket API only
  * FIX SBE schema 1:1
    * This will be used for FIX Order Entry, FIX Drop Copy, and FIX Market Data.
    * The current FIX schema 1:0 [spot-fixsbe-1_0.xml](/en/docs/products/spot/sbe/schemas/spot-fixsbe-1_0.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
    * Changes in schema 1:1:
      * New enum `expiryReason`
      * New field `ExpiryReason` in `ExecutionReport`



#### FIX API

  * ExpiryReason `<25056>` is optionally added to the ExecutionReport `<T>` message.
    * Updated QuickFIX Schema for FIX Market Data and FIX Order Entry.



#### WebSocket API

  * `serverShutdown` event added.



#### Future Changes

  * These endpoints have been [deprecated](/en/docs/products/spot/CHANGELOG#2019-11-13) for a long time and will be retired on **2026-03-25** :
    * `GET /api/v1/ping`
    * `GET /api/v1/time`
    * `POST /api/v1/userDataStream`
    * `PUT /api/v1/userDataStream`
    * `GET /api/v1/ticker/bookTicker`
    * `GET /api/v1/ticker/price`
    * `GET /api/v1/klines`
    * `GET /api/v1/historicalTrades`
    * `GET /api/v1/depth`
    * `GET /api/v1/aggTrades`
    * `GET /api/v1/ticker/24hr`
  * The following endpoints will be retired **2026-03-25** :
    * `GET /api/v1/userDataStream`
    * `DELETE /api/v1/userDataStream`
    * `GET /api/v1/trades`
  * **The following changes will occur at 2026-03-26 at approximately 07:00 UTC**
    * The responses to order placement and order list placement endpoints display the expiry reason depending on the value of `newOrderRespAck`:
      * If `newOrderRespType=ACK`, the expiry reason is not displayed.
      * If `newOrderRespType=RESULT` or `newOrderRespType=FULL` mode, the expiry reason, if any, is displayed in field `expiryReason`.
        * This affects the following endpoints/methods:
          * REST API
            * `POST /api/v3/order`
            * `POST /api/v3/sor/order`
            * `POST /api/v3/order/cancelReplace`
            * `POST /api/v3/order/oco`
            * `POST /api/v3/orderList/oco`
            * `POST /api/v3/orderList/oto`
            * `POST /api/v3/orderList/otoco`
            * `POST /api/v3/orderList/opo`
            * `POST /api/v3/orderList/opoco`
          * WebSocket API
            * `order.place`
            * `sor.order.place`
            * `order.cancelReplace`
            * `orderList.place`
            * `orderList.place.oco`
            * `orderList.place.oto`
            * `orderList.place.otoco`
            * `orderList.place.opo`
            * `orderList.place.opoco`
    * In User Data Streams, `executionReport` events have a new optional field, `eR`, which shows the expiry reason, if any.



* * *

### 2026-02-24

  * [ICEBERG_PARTS](/en/docs/products/spot/filters#iceberg_parts) will be increased to 100 for all symbols at **2026-03-12 07:00 UTC**.
  * Following the announcement on [2025-12-02](/en/docs/products/spot/CHANGELOG#2025-12-02), `!ticker@arr` will be retired on **2026-03-26**.



* * *

### 2026-02-12

REST and WebSocket API:

  * Reminder that SBE 3:0 schema will be retired on 2026-02-19, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2026-02-09

  * Clarified exponent field requirements in [FIX SBE documentation](/en/docs/products/spot/fix-api#fix-sbe)



* * *

### 2026-02-02

  * Documented that [FIX Drop Copy session](/en/docs/products/spot/fix-api#fix-api-drop-copy-sessions) data is delayed by 1 second. This has been the delay since the inception of the FIX API.



* * *

### 2026-01-29

  * [Demo Mode](/en/docs/products/spot/demo-mode/general-info) is now available.
  * For information on when the Spot Demo Mode environment will be unavailable due to maintenance, please refer to the [Demo Mode Changelog](/en/docs/products/spot/demo-mode/CHANGELOG)



* * *

### 2026-01-27

**Notice: The following changes will occur at 2026-02-11 7:00 UTC** :

  * [ICEBERG_PARTS](/en/docs/products/spot/filters#iceberg_parts) will be increased to 50 for all symbols.



* * *

### 2026-01-26

  * Added undocumented `recvWindow` to `userDataStream.subscribe.signature`.



* * *

### 2026-01-21

Following the announcement from [2025-10-24](/en/docs/products/spot/CHANGELOG#2025-10-24), the following endpoints/methods will no longer be available starting from **2026-02-20,07:00 UTC**

REST API

  * `POST /api/v3/userDataStream`
  * `PUT /api/v3/userDataStream`
  * `DELETE /api/v3/userDataStream`



WebSocket API

  * `userDataStream.start`
  * `userDataStream.ping`
  * `userDataStream.stop`



* * *

### 2025-12-18

  * Updated [FIX SBE documentation](/en/docs/products/spot/fix-api#fix-sbe)
  * Clarified User Data Stream documentation regarding [`eventStreamTerminated`](/en/docs/products/spot/user-data-stream#event-stream-terminated).
  * Assets `这是测试币` and `456` and symbol `这是测试币456` have been added to [SPOT Testnet](http://testnet.binance.vision) for testing endpoints/methods with a Unicode symbol. See the [Testnet CHANGELOG](/en/docs/products/spot/testnet/CHANGELOG) for more information.



* * *

### 2025-12-17

#### Time-sensitive Notice

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/en/docs/products/spot/errors#-1022-invalid_signature). Please review and update your signing logic accordingly. This has now been enabled on [SPOT Testnet](http://testnet.binance.vision)



#### REST API

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/en/docs/products/spot/rest-api#signed-endpoint-examples-for-post-apiv3order).



#### WebSocket API

  * Updated documentation for WebSocket API regarding [SIGNED request security](/en/docs/products/spot/web-socket-api#request-security).



* * *

### 2025-12-15

**Clarification Regarding UTF-8 Encoding:**

  * In [FIX](/en/docs/products/spot/fix-api), [REST](/en/docs/products/spot/rest-api#general-information-on-endpoints), and [WebSocket APIs](/en/docs/products/spot/web-socket-api#general-websocket-api-information), if your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * In REST and WebSocket APIs, some endpoints/methods may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
  * In [WebSocket Streams](/en/docs/products/spot/web-socket-streams), if your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.
  * In WebSocket Streams, [All Market Mini Tickers Stream](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker) and [All Market Rolling Window Statistics Streams](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-market-rolling-window-ticker) events may contain non-ASCII characters encoded in UTF-8.
  * In [SBE Market Data Streams](/en/docs/products/spot/sbe-market-data-streams), if your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.
  * [UserDataStream events](/en/docs/products/spot/user-data-stream) may contain non-ASCII characters encoded in UTF-8 if you own or trade any assets or symbols whose names contain non-ASCII characters.
  * For full compatibility with Binance APIs, please ensure your code is designed to handle UTF-8-encoded strings.



* * *

### 2025-12-09

  * [Schema for FIX SBE](/en/docs/products/spot/sbe/schemas/spot-fixsbe-1_0.xml) has been updated to use `smallGroupSize16Encoding` in `MarketDataSnapshot` and use `presence="optional"` for incremental book ticker/depth `MDEntrySize` fields.
  * Updated documentation re: [FIX vs FIX SBE](/en/docs/products/spot/fix-api#fix-vs-fix-sbe)
  * Added documentation in REST, and WebSocket APIs stating: **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule.  See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.



* * *

### 2025-12-02

**Notice:** The changes in this section will be gradually rolled out, and will take approximately up to two weeks to complete.

#### General Changes

  * Parameter `symbol` and `symbols` can now support Unicode values encoded in UTF-8.
  * Following the announcement from [2025-11-14](/en/docs/products/spot/CHANGELOG#2025-11-14), all documentation related to `!ticker@arr` has been removed.
    * The feature will remain available until a future retirement announcement is made.
    * Please use `<symbol>@ticker` or `!miniTicker@arr` instead.



#### FIX API

  * Unicode values encoded in UTF-8 can now be accepted in FIX messages. This is allowed for the following tags only:
    * `Currency (15)`
    * `MiscFeeCurr (138)`
    * `Symbol (55)`
    * `SecondarySymbol (25019)`
    * `CounterSymbol (25028)`
    * `SecurityDesc (107)`
  * When Unicode is put in a tag value that is not one of the tags above, FIX API will now send back a `RefTagID (371)` tag in the Reject `<3>`, pointing to exactly which tag is not allowed to contain Unicode.
  * NewOrderList `<E>` accepts `TriggerPriceDirection (1109)` without `TriggerPrice (1102)`.



#### WebSocket Streams

  * WebSocket Market Streams supports URL-encoded urls. 



**Notice: The following changes will occur at approximately 2025-12-18 7:00 UTC** :

  * [ICEBERG_PARTS](/en/docs/products/spot/filters#iceberg_parts) will be increased to 25 for all symbols.
  * [FIX SBE support](/en/docs/products/spot/fix-api) becomes available.
  * [One Pays the Other (OPO)](/en/docs/products/spot/faqs/opo) becomes available on all symbols.
    * `opoAllowed` begins to appear in Exchange Information requests, indicating if One-Pays-the-Other (OPO) orders are supported on each symbol.
      * REST API: `GET /api/v3/exchangeInfo`
      * WebSocket API: `exchangeInfo`
    * New requests for OPO:
      * REST API:
        * `POST /api/v3/orderList/opo`
        * `POST /api/v3/orderList/opoco`
      * WebSocket API
        * `orderList.place.opo`
        * `orderList.place.opoco`
      * FIX API
        * NewOrderList `<E>` has field `OPO (25046)`. Please update to the latest QuickFIX Schema for OPO support.
  * STP mode [`TRANSFER`](/en/docs/products/spot/faqs/stp_faq) has been added. The exact date that STP `TRANSFER` will be enabled has not yet been determined.
  * **SBE: A new schema 3:2 ([spot_3_2.xml](/en/docs/products/spot/sbe/schemas/spot_3_2.xml)) is available.**
    * The current schema 3:1 ([spot_3_1.xml](/en/docs/products/spot/sbe/schemas/spot_3_1.xml)) is deprecated and will be retired in 6 months as per our schema deprecation policy.
    * Changes in 3:2:
      * New enum variant `TRANSFER` for `selfTradePreventionMode` and `allowedSelfTradePreventionModes`.
      * All schemas below 3:1 are unable to represent any response that could contain the STP mode `TRANSFER` (e.g. Exchange Information, order placement, order cancellation, or querying the status of an order).  When a response cannot be represented in the requested schema, an error is returned.
  * FIX API changes:
    * `LastFragment (893)` becomes deprecated.
      * This means that the MarketIncrementalRefresh `<X>` messages will no longer be fragmented and may contain more than 10,000 entries.
      * The documentation has been updated to reflect this change.
    * ListStatus `<N>` will no longer emit the optional `symbol` field.
      * This applies to FIX Order Entry and FIX Drop Copy.
      * The documentation has been updated to reflect this change.



* * *

### 2025-11-14

  * All Market Tickers Stream (`!ticker@arr`) has been deprecated; This means this will be removed both from the documentation and from our systems at a later date. More details to follow.
  * Please use [`<symbol>@ticker`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#ticker) or [`!miniTicker@arr`](/en/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker) instead.



* * *

### 2025-11-12

  * The steps on [how to manage a local order book correctly](/en/docs/products/spot/web-socket-streams#how-to-manage-a-local-order-book-correctly) has been corrected.



* * *

### 2025-11-11

#### SBE Market Data

  * **At 2025-11-26 07:00 UTC, the update speed of`<symbol>@depth` and `<symbol>@depth20` streams will be changed to 50ms**.
    * This change will apply automatically to all users of SBE Market Data and doesn't require any action.
    * The total amount of data received per second will be increased (up to 2x).
    * [SPOT Testnet](https://testnet.binance.vision/) will have these changes at **2025-11-11 07:00 UTC**.
    * [SBE Market Data](/en/docs/products/spot/sbe-market-data-streams) has been updated to reflect these changes.



* * *

### 2025-11-10

  * "Last Updated" dates will be removed from all documents except for CHANGELOG.
  * Moving forward, CHANGELOG will be the source of reference for when changes were made to any document.



* * *

### 2025-10-28

**Notice: The following changes will be deployed on 2025-10-28, starting at 04:00 UTC and may take several hours to complete:**

  * An optional parameter, `symbolStatus`, has been added to the following endpoints:
    * **REST API**
      * `GET /api/v3/depth`
      * `GET /api/v3/ticker/price`
      * `GET /api/v3/ticker/bookTicker`
      * `GET /api/v3/ticker/24hr`
      * `GET /api/v3/ticker/tradingDay`
      * `GET /api/v3/ticker`
    * **WebSocket API**
      * `depth`
      * `ticker.price`
      * `ticker.book`
      * `ticker.24hr`
      * `ticker.tradingDay`
      * `ticker`
  * When the parameter `symbolStatus=<STATUS>` is provided, only symbols whose trading status matches the specified `STATUS` will be included in the response:_
    * If a single symbol is specified using the `symbol=<SYMBOL>` parameter and its trading status does not match the given `STATUS`, the endpoint will return error code [`-1220 SYMBOL_DOES_NOT_MATCH_STATUS`](/en/docs/products/spot/errors#-1220-symbol_does_not_match_status).
    * If multiple symbols are specified using the `symbols=[...]` parameter, the response will be an array that excludes any symbols whose trading status does not match `STATUS`. If no symbols from the symbols parameter have a trading status that matches `STATUS`, the response is an empty array.
    * For endpoints where the `symbol` and `symbols` parameters are optional, omitting these parameters is treated as if all symbols had been specified in the `symbols=[...]` parameter. See the previous line for the behavior of `symbolStatus=<STATUS>`.



* * *

### 2025-10-24

#### SBE

  * SBE: schema 3:1 ([spot_3_1.xml](/en/docs/products/spot/sbe/schemas/spot_3_1.xml)) has been updated to support [listenToken Subscription Methods](/en/docs/products/margin-trading/listen-token-data-stream) for Margin Trading.



#### REST and WebSocket API

Following the announcement from [2025-04-07](/en/docs/products/spot/CHANGELOG#2025-04-07), all documentation related with `listenKey` for use on `wss://stream.binance.com` has been removed.

**We remind you that you should instead get user data updates by subscribing to the[User Data Stream on the WebSocket API](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream). This will offer better performance (lower latency).**

Please refer to the list of requests and methods below for more information.

The features will remain available until a future retirement announcement is made.

  * REST API

    * `POST /api/v3/userDataStream`
    * `PUT /api/v3/userDataStream`
    * `DELETE /api/v3/userDataStream`
  * WebSocket API

    * `userDataStream.start`
    * `userDataStream.ping`
    * `userDataStream.stop`



* * *

### 2025-10-21

REST and WebSocket API:

  * Reminder that SBE 2:1 schema will be retired on 2025-10-24, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2025-10-08

#### FIX API

  * Updated [QuickFIX Schema](/en/docs/products/spot/fix/schemas/spot-fix-md.xml) for FIX Market Data:
    * Updated `RecvWindow(25000)` to reflect microsecond support announced on [2025-08-12](/en/docs/products/spot/CHANGELOG#2025-08-12).
    * Updated [InstrumentList `<y>`](/en/docs/products/spot/fix-api#instrumentlist-y) message:
      * Added fields: `StartPriceRange`, `EndPriceRange`.
      * Made the following fields optional: `MinTradeVol(562)`, `MaxTradeVol(1140)`, `MinQtyIncrement(25039)`, `MarketMinTradeVol(25040)`, `MarketMaxTradeVol(25041)`, `MarketMinQtyIncrement(25042)`, `MinPriceIncrement(969)`.
    * **The changes to InstrumentList are breaking changes, and will roll out at around 2025-10-23 07:00 UTC. Please update to the new schema before then.**
    * [SPOT Testnet](https://testnet.binance.vision/) has the breaking changes already enabled.



* * *

### 2025-09-29

**Notice: The following changes will be deployed on 2025-09-29, starting at 10:00 UTC and may take several hours to complete.**

  * Added an endpoint to retrieve the list of filters relevant to an account on a given symbol. This is the only endpoint that shows if an account has `MAX_ASSET` filters applied to it.
    * REST API: [`GET /api/v3/myFilters`](/en/docs/catalog/core-trading-spot-trading/api/rest-api/account#my-filters)
    * WebSocket API: [`myFilters`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/account#my-filters)
  * Comments in **SBE: schema 3:1 ([spot_3_1.xml](/en/docs/products/spot/sbe/schemas/spot_3_1.xml))** have been added, modified, and removed. Although there is no need for users of `3:1` to update to this version of the file, we advise updating to maintain consistency.
  * Added documentation for filter [`MAX_ASSET`](/en/docs/products/spot/filters#max_asset).



* * *

### 2025-09-18

  * Updated documentation for `recvWindow` to reflect microsecond support announced on [2025-08-12](/en/docs/products/spot/CHANGELOG#2025-08-12).
    * REST API: [Timing Security](/en/docs/products/spot/rest-api#timing-security)
    * WebSocket API: [Timing Security](/en/docs/products/spot/web-socket-api#timing-security)



* * *

### 2025-09-12

  * The [QuickFix schema for FIX Order Entry](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml) has been updated to support Pegged Orders.
  * Updated FIX API Documentation for `RecvWindow` in
    * [Message Components](/en/docs/products/spot/fix-api#header)
    * [Timing Security](/en/docs/products/spot/fix-api#timing-security)



* * *

### 2025-08-28

  * Updated SBE FAQ section [regarding legacy support](/en/docs/products/spot/faqs/sbe_faq#regarding-legacy-support) to include more details on schema compatibility and explain `NonRepresentable` and `NonRepresentableMessage`.



* * *

### 2025-08-26

  * Updated "Request Security" documentation for [REST API](/en/docs/products/spot/rest-api#request-security) and [WebSocket API](/en/docs/products/spot/web-socket-api#request-security) with no functional changes.



* * *

### 2025-08-25

  * **SBE: schema 3:1 ([spot_3_1.xml](/en/docs/products/spot/sbe/schemas/spot_3_1.xml))** will be updated on **2025-08-25 at 05:00 UTC**
    * The following fields have been renamed because the [SbeTool](/en/docs/products/spot/faqs/sbe_faq#generate-sbe-decoders) code generator has been found to generate Java code that does not compile.
      * Although only users impacted by this issue need to update the schema, we advise all users to upgrade to the latest version to maintain consistency.
      * Message `MaxAssetFilter`
        * field `limitExponent` renamed to `qtyExponent`
        * field `limit` renamed to `maxQty`



* * *

### 2025-08-19

  * `userDataStream.subscribe` returns `subscriptionId` in the responses.  This was missed in the [previous](/en/docs/products/spot/CHANGELOG#2025-08-12) changelog entry.



* * *

### 2025-08-12

**Notice:** The changes in this section will be gradually rolled out, and will take approximately up to two weeks to complete.

#### General Changes

  * New error codes `-1120` and `1211`. See [Errors](/en/docs/products/spot/errors) for more information.
  * The following requests have a new structure called `specialCommission`. See [Commission Rates](/en/docs/products/spot/faqs/commission_faq).
    * REST API
      * `GET /api/v3/account/commission`
      * `POST /api/v3/order/test` with `computeCommissionRates=true`
      * `POST /api/v3/sor/order/test` with `computeCommissionRates=true`
    * WebSocket API
      * `account.commission`
      * `order.test` with `computeCommissionRates=true`
      * `sor.order.test` with `computeCommissionRates=true`
  * **SBE: A new schema 3:1 ([spot_3_1.xml](/en/docs/products/spot/sbe/schemas/spot_3_1.xml)) is available.**
    * The current schema 3:0 ([spot_3_0.xml](/en/docs/products/spot/sbe/schemas/spot_3_0.xml)) is deprecated and will retire in 6 months as per our schema deprecation policy.
    * Changes in schema 3:1:
      * `ExchangeInfoResponse`: new field `pegInstructionsAllowed`
      * `ExecutionReportEvent`: new fields `pricePeg`, `pricePegOffsetLevel`, `peggedPrice`
      * `UserDataStreamSubscribeResponse`: new field `subscriptionId`
      * New field `subscriptionId` for all user data stream events.
      * Field `apiKey` renamed to `loggedOnApiKey` for `WebSocketSessionLogonResponse`, `WebSocketSessionStatusResponse` and `WebSocketSessionLogoutResponse`
      * `OrderTestWithCommissionsResponse`: 2 new fields `specialCommissionForOrderMaker` and `specialCommissionForOrderTaker`
      * `AccountCommissionResponse`: 4 new fields `specialCommissionMaker`, `specialCommissionTaker`, `specialCommissionBuyer` and `specialCommissionSeller`
      * Support for `EXCHANGE_MAX_NUM_ORDER_LISTS`, `MAX_NUM_ORDER_LISTS`, and `MAX_NUM_ORDER_AMENDS` filters.
      * `ExecutionReportEvent`: fields `rejectReason` and `origClientOrderId` now show their default values in SBE format to match the JSON format.
      * `NonRepresentableMessage`: New message added to represent a message that cannot be represented in this schema ID and version. Receipt of this message indicates that something should be available, but it is not representable using the SBE schema currently in use.
  * Orders with cumulative quantity of 0 in the final state `EXPIRED_IN_MATCH` (i.e., the order expired due to STP) will be archived after 90 days.
  * Query order lists requests will first query the data in the cache, and if it cannot be found, will query the database.
    * REST API: `GET /api/v3/openOrderLists`
    * WebSocket API: `openOrderLists.status`



#### WebSocket API

  * A single WebSocket connection can subscribe to multiple User Data Streams at once.
    * Only one subscription per account is allowed on a single connection.
  * Method `userDataStream.subscribe.signature` has been added that allows you to subscribe to the User Data Stream without needing to login first.
    * This also doesn’t require an Ed25519 API Key, and can work with any [API Key type](/en/docs/products/spot/faqs/api_key_types).
    * For [SBE support](/en/docs/products/spot/faqs/sbe_faq), you need to use at least schema 3:1.
  * Method `session.subscriptions` has been added to list all active subscriptions for the current session.
  * The meaning of the field `userDataStream` in the session requests has changed slightly.
    * Previously, this returned `true` if you were subscribed to the user data stream of your logged-on account.
    * Now returns `true` if you have at least one active user data stream subscription, otherwise `false`.
  * `userDataStream.unsubscribe` supports closing multiple subscriptions.
    * When called with no parameter, this will close all subscriptions.
    * When called with `subscriptionId`, this will attempt to close the subscription matching that Id, if it exists.
    * The authorization for this request has been changed to `NONE`.
  * Field `subscriptionId` has been added to the User Data Stream events payload when listening through the [WebSocket API](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe). This will identify which subscription the event is coming from.



#### FIX API

  * When a client sends a reject message, the FIX API will no longer send the client back a Reject `<3>` message.
  * Error messages are now clearer when a tag is invalid, missing a value, or when the field value is empty or malformed.
    * Code
          
          { "code": -1169, "msg": "Invalid tag number." }

    * Code
          
          { "code": -1177, "msg": "Tag specified without a value." }

    * Code
          
          { "code": -1102, "msg": "Field value was empty or malformed." }




#### Future Changes

The following changes will be available on **2025-08-27 starting at 07:00 UTC** :

  * Exchange Information requests will emit a new field, `pegInstructionsAllowed`.
  * Bug fix: The Matching Engine will no longer accept order lists that exceed the order count filter limits. Affected filters:
    * `MAX_NUM_ORDERS`
    * `MAX_ALGO_ORDERS`
    * `MAX_ICEBERG_ORDERS`
    * `EXCHANGE_MAX_NUM_ORDERS`
    * `EXCHANGE_MAX_ALGO_ORDERS`
    * `EXCHANGE_MAX_ICEBERG_ORDERS`



The following changes will be available on **2025-08-28 starting at 07:00 UTC** :

  * The [pegged orders](/en/docs/products/spot/faqs/pegged_orders) functionality will be available.
    * `pegInstructionsAllowed` will be set to `true` for all symbols, enabling the use of pegged orders for all APIs.
    * The following conditional fields `pegPriceType`, `pegOffSetType`, `pegOffsetValues`, and `peggedPrice` will appear in responses of the following requests if the order is a pegged order:
      * REST API
        * `GET /api/v3/order`
        * `GET /api/v3/orderList`
        * `GET /api/v3/openOrderList`
        * `GET /api/v3/allOrders`
        * `DELETE /api/v3/order`
        * `DELETE /api/v3/orderList`
        * `DELETE /api/v3/openOrders`
        * `PUT /api/v3/order/amend/keepPriority`
      * WebSocket API
        * `order.status`
        * `orderList.status`
        * `allOrders`
        * `order.cancel`
        * `orderList.cancel`
        * `openOrders.cancelAll`
        * `order.amend.keepPriority`
    * FIX API
      * `OrdType(40)` supports new value `P(PEGGED)`
      * Tags `PegOffsetValue(211)`, `PegPriceType(1094)`, `PegMoveType(835)`, and `PegOffsetType(836)` have been added to the following messages:
        * NewOrderSingle `<D>`
        * NewOrderList `<E>`
        * OrderCancelRequestAndNewOrderSingle `<XCN>`
      * When placing an order, the `ExecutionReport` `<8>` message will echo back `PegInstructions`, with an extra optional field `PeggedPrice (839)`.
    * New error messages for pegged orders are added. Please see the [Errors](/en/docs/products/spot/errors) document for more information.
  * Changes with `recvWindow` will be enabled.
    * A third check is performed after your message leaves our message broker, just before it is sent to the Matching Engine.
      * This does not cover potential delays inside the Matching Engine itself.
    * `recvWindow` supports microseconds.
      * The value is still specified in milliseconds, but it can now include a decimal component for higher precision.
      * This means the parameter can now support up to **three decimal places** (e.g., 6000.346).
      * APIs affected:
        * FIX API
        * REST API
        * WebSocket API
  * New [`MAX_NUM_ORDER_LISTS`](/en/docs/products/spot/filters#max_num_order_lists) filter will be enabled, limiting the number of order lists to 20 per symbol.
  * New [`MAX_NUM_ORDER_AMENDS`](/en/docs/products/spot/filters#max_num_order_amends) filter will be enabled, limiting each order to a maximum of 10 amendments.



* * *

### 2025-08-07

  * Updated FIX API documentation
    * [FIX Market Data limits](/en/docs/products/spot/fix-api#connection-limits): The subscription limit has always been present but was undocumented.
    * [On message processing order](/en/docs/products/spot/fix-api#on-message-processing-order): Reworded and reformatted.



* * *

### 2025-07-03

  * Beginning at **2025-07-08 07:00 UTC** , [WebSocket Streams](/en/docs/products/spot/web-socket-streams) will be upgraded.
  * During the upgrade, **existing and new connections may be disconnected in less than 24 hours**.
  * The upgrade may take up to 2 hours; We apologize for the inconvenience.



* * *

### 2025-06-04

REST and WebSocket API:

  * Reminder that SBE 2:0 schema will be retired on 2025-06-12, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq#sbe-schema).
  * The [SBE lifecycle for Production](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2025-05-28

  * Documented API timeout value and error under General API Information for each API:
    * [FIX](/en/docs/products/spot/fix-api#general-api-information)
    * [REST](/en/docs/products/spot/rest-api#general-rest-api-information)
    * [WebSocket](/en/docs/products/spot/web-socket-api#general-api-information)



* * *

### 2025-05-22

**Notice: The following changes will happen at 2025-06-06 7:00 UTC.**

  * The previous behavior of `recvWindow` on FIX, REST, and WebSocket APIs will be augmented by an additional check.
    * To review, the existing behavior is:
      * If `timestamp` is greater than `serverTime` \+ 1 second at receipt of the request, the request is rejected. Rejection by this check increments message limits (FIX API) and IP limits (REST and WebSocket APIs), but not Unfilled Order Count (order placement endpoints of all APIs).
      * If the difference between `timestamp` and `serverTime` at receipt of the request is greater than `recvWindow`, the request is rejected. Rejection by this check increments message limits (FIX API) and IP limits (REST and WebSocket APIs) but not Unfilled Order Count (order placement endpoints of all APIs).
    * The additional check is:
      * Just before a request is forwarded to the Matching Engine, if the difference between `timestamp` and the current `serverTime` is greater than `recvWindow`, the request is rejected. Rejection by this check increments message limits (FIX API), IP limits (REST and WebSocket APIs), and Unfilled Order Count (order placement endpoints of all APIs).
    * The documentation for Timing security has been updated to reflect the additional check.
      * [REST API](/en/docs/products/spot/rest-api#timing-security)
      * [WebSocket API](/en/docs/products/spot/web-socket-api#timing-security)
      * [FIX API](/en/docs/products/spot/fix-api#timing-security)
  * Fixed a bug in FIX Market Data message InstrumentList `<y>`. Previously, the value of `NoRelatedSym(146)` could have been incorrect.



* * *

### 2025-04-29

  * Features that currently require an Ed25519 API key will soon be opened up to HMAC and RSA keys.
    * For example, subscribing to User Data Stream in WebSocket API will be possible with any API key type before listenKeys are removed.
    * Users are still encouraged to migrate to Ed25519 API keys as they are more secure and performant on Binance Spot Trading.
    * More details to come.



* * *

### 2025-04-25

  * The following request weights have been increased from 1 to 4:
    * REST API: `PUT /api/v3/order/amend/keepPriority`
    * WebSocket API: `order.amend.keepPriority`
    * The documentation for both REST and WebSocket API has been updated to reflect these changes.
  * Clarified that `SEQNUM` in the FIX-API is a 32-bit unsigned integer that rolls over. This has been the `SEQNUM` data type since the inception of the FIX-API.



* * *

### 2025-04-21

**Clarification on the release of[Order Amend Keep Priority](/en/docs/products/spot/faqs/order_amend_keep_priority) and [STP Decrement](/en/docs/products/spot/faqs/stp_faq):**

  * At **2025-05-07 07:00 UTC**
    * Order Amend Keep Priority will be enabled on all symbols.
    * STP Decrement will be allowed on all symbols.
  * At **2025-04-24, 07:00 UTC** , the field `amendAllowed` will become visible on Exchange Information requests, but the feature will not be enabled yet.
  * [SPOT Testnet](https://testnet.binance.vision/) has both features enabled/allowed on all symbols.



* * *

### 2025-04-08

**Notice:** The changes in this section will be gradually rolled out, and will take a week to complete.

  * New Error code `-2039` where if querying an order with both `orderId` and `origClientOrderId` and no order is found with this combination.
    * Affected requests:
      * REST API: `GET /api/v3/order`
      * WebSocket API: `order.status`
  * The [Errors Documentation](/en/docs/products/spot/errors) has also been updated with the new error messages for code `-1034` when the FIX connection rate limits have exceeded. (More details can be found in yesterday's [update](/en/docs/products/spot/CHANGELOG#2025-04-07))



* * *

### 2025-04-07

#### General Changes

**Notice:** The changes in this section will be gradually rolled out, and will take a week to complete.

  * FIX Market Data connection limits were increased from 5 to 100 on January 16, 2025. This was not previously highlighted in changelog.
  * New Error code `-2038` for order amend keep priority requests that fail.
  * New messages for error code `-1034`.
  * If the unfilled order count for `intervalNum:DAY` is exceeded, the unfilled order count for `intervalNum:SECOND` is no longer incremented.
  * Previously, the request weight for myTrades was 20 regardless of the parameters provided. Now, if you provide `orderId`, the request weight is 5.
    * REST API: `GET /api/v3/myTrades`
    * WebSocket API: `myTrades`
  * Change when querying and deleting orders:
    * When neither `orderId` nor `origClientOrderId` are present, the request is now rejected with `-1102` instead of `-1128`.
    * Affected requests:
      * REST API:
        * `GET /api/v3/order`
        * `DELETE /api/v3/order`
      * WebSocket API
        * `order.status`
        * `order.cancel`
      * FIX API
        * OrderCancelRequest `<F>`



#### FIX API

**Notice:** The following changes will occur during April 21, 2025.

  * FIX API verifies that `EncryptMethod(98)` is 0 at Logon `<A>`.
  * FIX Order Entry connection limits will be a maximum of 10 concurrent connections per account.
  * The connection rate limits are now enforced. Note that these limits are checked independently for both the account and the IP address.
    * FIX Order Entry: 15 connection attempts within 30 seconds
    * FIX Drop Copy: 15 connection attempts within 30 seconds
    * FIX Market Data: 300 connection attempts within 300 seconds
  * News `<B>` contains a countdown until disconnection in the Headline field.
    * Following the completion of this update, when the server enters maintenance, a `News` message will be sent to clients **every 10 seconds for 10 minutes**. After this period, clients will be logged out and their sessions will be closed.
  * OrderCancelRequest `<F>` and OrderCancelRequestAndNewOrderSingle `<XCN>` now allow both `orderId` and `clientOrderId`.
  * The [QuickFix schema for FIX OE](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml) is updated to support the Order Amend Keep Priority feature and new STP mode, `DECREMENT`.



#### User Data Streams

  * **Receiving user data streams on wss://stream.binance.com:9443 using a`listenKey` is now deprecated.**
    * This feature will be removed from our systems at a later date.
  * **Instead, you should get user data updates by subscribing to the[User Data Stream on the WebSocket API](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream)**.
    * This should offer slightly better performance **(lower latency)**.
    * This requires the use of an Ed25519 API Key.
  * In a future update, information about the base WebSocket endpoint for the User Data Streams will be removed.
  * In a future update, the following requests will be removed from the documentation:
    * `POST /api/v3/userDataStream`
    * `PUT /api/v3/userDataStream`
    * `DELETE /api/v3/userDataStream`
    * `userDataStream.start`
    * `userDataStream.ping`
    * `userDataStream.stop`
  * The [User Data Stream documentation](/en/docs/products/spot/user-data-stream) will remain as reference for the payloads you can receive.



#### Future Changes

The following changes will occur at **April 24, 2025, 07:00 UTC** :

  * ~~[Order Amend Keep Priority](/en/docs/products/spot/faqs/order_amend_keep_priority) becomes available. (Note that the symbol has to have the feature enabled to be used.)~~
    * **UPDATE 2025-04-21: The exact date "Order Amend Keep Priority" will be enabled has not yet been determined.**
    * New field `amendAllowed` becomes visible in Exchange Information responses.
      * REST API: `GET /api/v3/exchangeInfo`
      * WebSocket API: `exchangeInfo`
    * FIX API: New Order Entry Messages **OrderAmendKeepPriorityRequest** and **OrderAmendReject**
    * REST API: `PUT /api/v3/order/amend/keepPriority`
    * WebSocket API: `order.amend.keepPriority`
  * ~~STP mode`DECREMENT` becomes visible in Exchange Information if the symbol has it configured.~~
    * **UPDATE 2025-04-21: The exact date`DECREMENT` STP will be enabled has not yet been determined.**
    * Instead of expiring only the maker, only the taker, or unconditionally both orders, STP decrement decreases the available quantity of **both** orders and increases the `prevented quantity` of **both** orders by the amount of the prevented match.
    * This expires the order with less available quantity as (`filled quantity` \+ `prevented quantity`) equals `order quantity`. Both orders expire if their available quantities are equal. It is called a "decrement" because it reduces available quantity.
  * Behavior when querying and/or canceling with `orderId` and `origClientOrderId/cancelOrigClientOrderId`:
    * The behavior when both parameters were provided was not consistent across all endpoints.
    * Moving forward, when both parameters are provided, the order is first searched for using its `orderId`, and if found, `origClientOrderId`/`cancelOrigClientOrderId` is checked against that order. If both conditions pass, the request succeeds. If both conditions are not met the request is rejected.
    * Affected requests:
      * REST API:
        * `GET /api/v3/order`
        * `DELETE /api/v3/order`
        * `POST /api/v3/order/cancelReplace`
      * WebSocket API:
        * `order.status`
        * `order.cancel`
        * `order.cancelReplace`
      * FIX API
        * OrderCancelRequest `<F>`
        * OrderCancelRequestAndNewOrderSingle `<XCN>`
  * Behavior when canceling with `listOrderId` and `listClientOrderId`:
    * The behavior when both parameters were provided was not consistent across all endpoints.
    * Moving forward, when both parameters are passed, the order list is first searched for using its `listOrderId`, and if found, `listClientOrderId` is checked against that order list. If both conditions are not met the request is rejected.
    * Affected requests:
      * REST API
        * `DELETE /api/v3/orderList`
      * WebSocket API
        * `orderList.cancel`
  * **SBE: A new schema 3:0 ([spot_3_0.xml](/en/docs/products/spot/sbe/schemas/spot_3_0.xml)) is now available.**
    * The current schema 2:1 ([spot_2_1.xml](/en/docs/products/spot/sbe/schemas/spot_2_1.xml)) is now deprecated and will be retired in 6 months as per our schema deprecation policy.
    * Note that trying to use schema 3:0 before it is released will result in an error.
    * Changes in schema 3:0:
      * Support for Order Amend Keep Priority:
        * Added field `amendAllowed` to ExchangeInfoResponse.
        * New Messages `OrderAmendmentsResponse` and `OrderAmendKeepPriorityResponse`
      * All enums now have a `NON_REPRESENTABLE` variant. This will be used to encode new enum values in the future, which would be incompatible with 3:0.
      * New enum variant `DECREMENT` for `selfTradePreventionMode` and `allowedSelfTradePreventionModes`
      * `symbolStatus` enum values `AUCTION_MATCH`, `PRE_TRADING` and `POST_TRADING` have been removed.
      * Fields `usedSor`, `orderCapacity`, `workingFloor`, `preventedQuantity`, and `matchType` are no longer optional.
      * Field `orderCreationTime` in `ExecutionReportEvent` is now optional.
    * When using deprecated schema 2:1 on the WebSocket API to listen to the User Data Stream:
      * `ListStatusEvent` field `listStatusType` will be rendered as `ExecStarted` when it should have been `Updated`. Upgrade to schema 3:0 to get the correct value.
      * `ExecutionReportEvent` field `selfTradePreventionMode` will be rendered as `None` when it should have been `Decrement`. This only happens when `executionType` is `TradePrevention`.
      * `ExecutionReportEvent` field `orderCreationTime` will be rendered as -1 when it has no value.
    * All schemas below 3:0 are unable to represent responses for Order Amend Keep Priority requests and any response that could contain the STP mode `DECREMENT` (e.g. Exchange Information, order placement, order cancelation, or querying the status of your order). When a response cannot be represented in the requested schema, an error is returned.



* * *

### 2025-04-03

  * Following SPOT Testnet's latest announcement, updating the URL in the WebSocket API to the latest URL for [SPOT Testnet](https://testnet.binance.vision/).



* * *

### 2025-03-31

  * Added a clarification on the performance of canceling an order.



* * *

### 2025-03-10

  * **Notice: The following changes will happen on 2025-03-13 09:00 UTC**
    * FIX Drop Copy sessions will have a limit of **60 messages per minute**.
    * FIX Market Data sessions will have a limit of **2000 messages per minute**.
    * The FIX API documentation has been updated to reflect the upcoming changes.
  * **SBE Market Data Streams will be available on March 18 2025, 07:00 UTC.** These streams offer a smaller payload and should offer better latency than the equivalent JSON streams for a subset of latency-sensitive market data streams.
    * Streams available in SBE format:
      * Real-time: trade stream
      * Real-time: best bid/ask
      * Every 100 ms: diff. depth
      * Every 100 ms: partial book depth
    * For more information please refer to the [SBE Market Data Streams](/en/docs/products/spot/sbe-market-data-streams).



* * *

### 2025-03-05

  * **Notice: The following changes will happen on March 10, 2025 12:00 UTC.** The following request weights will be increased from 2 to 4:
    * REST API: `GET /api/v3/aggTrade`
    * WebSocket API: `trades.aggregate`
  * The documentation for both REST and WebSocket API has been updated to reflect the upcoming changes.



* * *

### 2025-02-12

  * **Notice: These changes will take effect on February 26, 2025 05:00 UTC.** Please ensure you have downloaded the latest schema before then.
  * `AggressorSide (2446)` will be rendered in the [FIX Market Data Trade Stream](/en/docs/products/spot/fix-api#marketdatarequest-v). The QuickFix schema [file](/en/docs/products/spot/fix/schemas/spot-fix-md.xml) has also been updated.



* * *

### 2025-01-28

  * **Notice: These changes will be gradually rolled out between February 3, 2025 and February 14, 2025.** **The following changes will apply to WebSocket Market Data Streams, User Data Streams, and the WebSocket API:**
    * Our WebSocket services will send a ping frame **every 20 seconds** instead of 3 minutes.
    * The allowed pong delay will be **every 1 minute** instead of 10 minutes.
    * The documentation for these services have been updated to reflect the change.



* * *

### 2025-01-09

  * FIX Market Data will be available at **January 16, 05:00 UTC**. The FIX API documentation has been updated regarding this feature.
  * Please refer to this [link](/en/docs/products/spot/fix/schemas/spot-fix-md.xml) for the QuickFIX Schema for FIX Market Data.



* * *

### 2024-12-17

General Changes:

The system now supports microseconds in all related time and/or timestamp fields. Microsecond support is **opt-in** , by default the requests and responses still use milliseconds. Examples in documentation are also using milliseconds for the foreseeable future.

WebSocket Streams

  * A new optional parameter `timeUnit` can be used in the connection URL to select the time unit.
    * For example: `/stream?streams=btcusdt@trade&timeUnit=millisecond`
    * Supported values are:
      * `MILLISECOND`
      * `millisecond`
      * `MICROSECOND`
      * `microsecond`
    * If the time unit is not selected, milliseconds will be used by default.



REST API

  * A new optional header `X-MBX-TIME-UNIT` can be sent in the request to select the time unit.
    * Supported values:
      * `MILLISECOND`
      * `millisecond`
      * `MICROSECOND`
      * `microsecond`
    * The time unit affects timestamp fields in JSON responses (e.g., `time`, `transactTime`).
      * SBE responses continue to be in microseconds regardless of time unit.
    * If the time unit is not selected, milliseconds will be used by default.
  * Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp)` can now be passed in milliseconds or microseconds.



WebSocket API

  * A new optional parameter `timeUnit` can be used in the connection URL to select the time unit.
    * Supported values:
      * `MILLISECOND`
      * `millisecond`
      * `MICROSECOND`
      * `microsecond`
    * The time unit affects timestamp fields in JSON responses (e.g., `time`, `transactTime`).
      * SBE responses continue to be in microseconds regardless of time unit.
    * If the time unit is not selected, milliseconds will be used by default.
  * Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp)` can now be passed in milliseconds or microseconds.



User Data Streams

  * A new optional parameter `timeUnit` can be used in the connection URL to select the time unit.
    * Supported values
      * `MILLISECOND`
      * `MICROSECOND`.
      * `microsecond`
      * `millisecond`



* * *

### 2024-12-09

**Notice:** The changes below will be rolled out starting at **2024-12-12** and may take approximately a week to complete.

General Changes

  * Timestamp parameters now reject values too far into the past or the future. To be specific, the parameter will be rejected if:
    * `timestamp` before 2017-01-01 (less than 1483228800000)
    * `timestamp` is more than 10 seconds after the current time (e.g., if current time is 1729745280000 then it is an error to use 1729745291000 or greater)
  * If `startTime` and/or `endTime` values are outside of range, the values will be adjusted to fit the correct range.
  * The field for quote order quantity (`origQuoteOrderQty`) has been added to responses that previously did not have it. Note that for order placement endpoints the field will only appear for requests with `newOrderRespType` set to `RESULT` or `FULL`.
    * Please refer to the table below for affected requests with: `origQuoteOrderQty`:

Service| Request  
---|---  
REST| `POST /api/v3/order`  
| `POST /api/v3/sor/order`  
| `POST /api/v3/order/oco`  
| `POST /api/v3/orderList/oco`  
| `POST /api/v3/orderList/oto`  
| `POST /api/v3/orderList/otoco`  
| `DELETE /api/v3/order`  
| `DELETE /api/v3/orderList`  
| `POST /api/v3/order/cancelReplace`  
WebSocket API| `order.place`  
| `sor.order.place`  
| `orderList.place`  
| `orderList.place.oco`  
| `orderList.place.oto`  
| `orderList.place.otoco`  
| `order.cancel`  
| `orderList.cancel`  
| `order.cancelReplace`  
  
SBE

  * A new schema 2:1 [spot_2_1.xml](/en/docs/products/spot/sbe/schemas/spot_2_1.xml) has been released. The current schema 2:0 [spot_2_0.xml](/en/docs/products/spot/sbe/schemas/spot_2_0.xml) will thus be deprecated, and retired from the API in 6 months as per our schema deprecation policy.
  * Schema 2:1 is a backward compatible update of schema 2:0. You will always receive payloads in 2:1 format when you request either schema 2:0 or 2:1.
  * Changes in SBE schema 2:1:
    * New field `origQuoteOrderQty` in order placement/cancellation responses (Note: Decoders generated using the 2:0 schema will skip this field.):
      * `NewOrderResultResponse`
      * `NewOrderFullResponse`
      * `CancelOrderResponse`
      * `NewOrderListResultResponse`
      * `NewOrderListFullResponse`
      * `CancelOrderListResponse`
    * WebSocket API only: New field `userDataStream` in session status responses:
      * `WebSocketSessionLogonResponse`
      * `WebSocketSessionStatusResponse`
      * `WebSocketSessionLogoutResponse`
    * WebSocket API only: New messages for User Data Stream support:
      * `UserDataStreamSubscribeResponse`
      * `UserDataStreamUnsubscribeResponse`
      * `BalanceUpdateEvent`
      * `EventStreamTerminatedEvent`
      * `ExecutionReportEvent`
      * `ExternalLockUpdateEvent`
      * `ListStatusEvent`
      * `OutboundAccountPositionEvent`



WebSocket API

  * You can now subscribe to User Data Stream events through your WebSocket API connection.
    * Note: This feature is only available for users of the Ed25519 API keys.
    * Note: New SBE schema 2:1 is required for User Data Stream subscriptions in SBE format.
  * New requests:
    * `userDataStream.subscribe`
    * `userDataStream.unsubscribe`
  * Changes to `session.logon`, `session.status`, and `session.logout`
    * Added a new field `userDataStream` indicating if the user data stream subscription is active.
  * Fixed a bug where you wouldn't receive a new listenKey using `userDataStream.start` after `session.logon`



User Data Stream

  * WebSocket API only: New event `eventStreamTerminated` is emitted when you either logout from your WebSocket session or you have unsubscribed from the user data stream.
  * New event `externalLockUpdate` is sent when your spot wallet balance is locked/unlocked by an external system.



FIX API

  * The [schema](/en/docs/products/spot/fix/schemas/spot-fix-oe.xml) has been updated with a new Administrative message News <B>, which can be used for all FIX services. Receiving this message indicates that your connection is about to be closed.



The following changes will occur **between 2024-12-16 to 2024-12-20** :

  * Fixed a bug that prevented orders from being placed when submitting OCOs on the `BUY` side without providing a `stopPrice`.
  * `TAKE_PROFIT` and `TAKE_PROFIT_LIMIT` support has been added for OCOs.
    * Previously OCOs could only be composed by the following order types:
      * `LIMIT_MAKER` \+ `STOP_LOSS`
      * `LIMIT_MAKER` \+ `STOP_LOSS_LIMIT`
    * Now OCOs can be composed of the following order types:
      * `LIMIT_MAKER` \+ `STOP_LOSS`
      * `LIMIT_MAKER` \+ `STOP_LOSS_LIMIT`
      * `TAKE_PROFIT` \+ `STOP_LOSS`
      * `TAKE_PROFIT` \+ `STOP_LOSS_LIMIT`
      * `TAKE_PROFIT_LIMIT` \+ `STOP_LOSS`
      * `TAKE_PROFIT_LIMIT` \+ `STOP_LOSS_LIMIT`
    * This is supported by the following requests:
      * `POST /api/v3/orderList/oco`
      * `POST /api/v3/orderList/otoco`
      * `orderList.place.oco`
      * `orderList.place.otoco`
      * `NewOrderList<E>`
    * Error code -1167 will be obsolete after this update and will be removed from the documentation in a later update.



* * *

### 2024-10-18

REST and WebSocket API:

  * Reminder that SBE 1:0 schema will be disabled on 2024-10-25, [6 months after being deprecated](/en/docs/products/spot/faqs/sbe_faq), as per our SBE policy.
  * The [SBE lifecycle for Prod](/en/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.



* * *

### 2024-10-17

Changes to Exchange Information (i.e. [`GET /api/v3/exchangeInfo`](/en/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info) from REST and [`exchangeInfo`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info) for WebSocket API).

  * A new optional parameter `showPermissionSets` can be used to hide the permissions from `permissionsSets`; This can be used for a reduced payload size.
  * A new optional parameter `symbolStatus` can now be used to only show symbols with the specified status. (e.g. `TRADING`, `HALT`, `BREAK`)



* * *

### 2024-08-26

  * [Spot Unfilled Order Count Rules](/en/docs/products/spot/faqs/order_count_decrement) have been updated to explain how to decrease your unfilled order count when placing orders.



* * *

### 2024-08-16

**Notice:** The changes below are being rolled out gradually, and may take approximately a week to complete.

General Changes:

  * New error messages have been added when quote quantity market orders (aka reverse market orders) are rejected in low-liquidity situations.



* * *

### 2024-08-01

  * [FIX API and Drop Copy Sessions](/en/docs/products/spot/fix-api) will be available on **August 8, 05:00 UTC**.



* * *

### 2024-07-26

  * [FIX API and Drop Copy Sessions](/en/docs/products/spot/fix-api) has been added to the documentation.
  * The release date to the live exchange has not been determined.



* * *

### 2024-07-22

General changes:

  * Fixed a bug where klines had incorrect timestamps.
    * REST API: `GET /api/v3/klines` and `GET /api/v3/uiKlines` with `timeZone` parameter
    * WebSocket API: `klines` and `uiKlines` with `timeZone` parameter
    * WebSocket Streams: `<symbol>@kline_<interval>@+08:00` streams



* * *

### 2024-06-11

  * On **June 11, 05:00 UTC** , One-Triggers-the-Other (OTO) orders and One-Triggers-a-One-Cancels-The-Other (OTOCO) orders will be enabled. (Note this may take a few hours to be rolled out to all servers.)
    * New requests have been added:
      * REST API:
        * `POST /api/v3/orderList/oto`
        * `POST /api/v3/orderList/otoco`
      * WebSocket API:
        * `orderList.place.oto`
        * `orderList.place.otoco`
  * On **June 18, 05:00 UTC** , Buyer order ID `b` and Seller order ID `a` will be removed from the Trade Streams (i.e. `<symbol>@trade`). (Note that this may take a few hours to be rolled out to all servers.)
    * [WebSocket Streams](/en/docs/products/spot/web-socket-streams) has been updated regarding this change.
    * To monitor if your order was part of a trade, please listen to the [User Data Streams](/en/docs/products/spot/user-data-stream)



* * *

### 2024-06-06

This will be available by **June 6, 11:59 UTC**.

REST API

  * `orderRateLimitExceededMode` has been added to `POST /api/v3/order/cancelReplace`.



WebSocket API

  * `orderRateLimitExceededMode` has been added to `order.cancelReplace`.



* * *

### 2024-05-30

WebSocket Streams:

  * Kline/Candlestick streams can now support a UTC+8 timezone offset. (e.g. `btcusdt@kline_1d@+08:00`)



* * *

### 2024-04-10

The following changes have been postponed to take effect on **April 25, 05:00 UTC**

General changes:

  * Symbol permission information in Exchange Information responses has moved from field `permissions` to field `permissionSets`.
  * Field `permissions` will be empty and will be removed in a future release.
  * Previously, `"permissions":["SPOT","MARGIN"]` meant that you could place an order on the symbol if your account had `SPOT` or `MARGIN` permissions. The equivalent is `"permissionSets":[["SPOT","MARGIN"]]`. (Note the extra set of square brackets.) Each array of permissions inside the `permissionSets` array is called a "permission set".
  * Symbol permissions can now be more complex. `"permissionSets":[["SPOT","MARGIN"],["TRD_GRP_004","TRD_GRP_005"]]` means that you may place an order on the symbol if your account has SPOT or MARGIN permissions **and** `TRD_GRP_004` or `TRD_GRP_005` permissions. There may be an arbitrary number of permission sets in a symbol's `permissionSets`.



REST API

  * `otoAllowed` will now appear on `GET /api/v3/exchangeInfo`, that indicates if One-Triggers-the-Other (OTO) orders are supported on that symbol.



WebSocket API

  * `otoAllowed` will now appear on `exchangeInfo`, that indicates if One-Triggers-the-Other (OTO) orders are supported on that symbol.



SBE

  * A new schema 2:0 [spot_2_0.xml](/en/docs/products/spot/sbe/schemas/spot_2_0.xml) has been released. The current schema 1:0 [spot_1_0.xml](/en/docs/products/spot/sbe/schemas/spot_1_0.xml) will thus be deprecated, and retired from the API in 6 months as per our schema deprecation policy.
  * When using schema 1:0 on REST API or WebSocket API, group "permissions" in message "ExchangeInfoResponse" will always be empty. Upgrade to schema 2:0 to find permission information in group "permissionSets". See General changes above for more details.
  * Deprecated OCO requests will still be supported by the latest schema.
  * Note that trying to use schema 2:0 before it is actually released will result in an error.



* * *

### 2024-04-02

**Notice:** The changes below are being rolled out gradually, and will take approximately a week to complete.

General changes:

  * `GET /api/v3/account` has a new optional parameter `omitZeroBalances`, which if enabled hides all zero balances.
  * `account.status` has a new optional parameter `omitZeroBalances` which if enabled hides all zero balances.
  * **The weight of the following requests has been increased from 10 to 25 (This will take effect on April 4, 2024)** :
    * `GET /api/v3/trades`
    * `GET /api/v3/historicalTrades`
    * `trades.recent`
    * `trades.historical`



User Data Stream:

  * New event `listenKeyExpired` that will be emitted in the streams if the `listenKey` expired.



REST API

  * The `POST /api/v3/order/oco` endpoint is now deprecated on the REST API. You should use the new `POST /api/v3/orderList/oco` endpoint instead. Note that this new endpoint uses different parameters.



WebSocket API

  * The `orderList.place` request is now deprecated on the WebSocket API. You should now use the new `orderList.place.oco` request instead. Note that this new request uses different parameters.



**The following will take effect _approximately_ a week after the release date:**

General changes:

  * Symbol permission information in Exchange Information responses has moved from field `permissions` to field `permissionSets`.
  * Field `permissions` will be empty and will be removed in a future release.
  * Previously, `"permissions":["SPOT","MARGIN"]` meant that you could place an order on the symbol if your account had `SPOT` or `MARGIN` permissions. The equivalent is `"permissionSets":[["SPOT","MARGIN"]]`. (Note the extra set of square brackets.) Each array of permissions inside the `permissionSets` array is called a "permission set".
  * Symbol permissions can now be more complex. `"permissionSets":[["SPOT","MARGIN"],["TRD_GRP_004","TRD_GRP_005"]]` means that you may place an order on the symbol if your account has SPOT or MARGIN permissions **and** `TRD_GRP_004` or `TRD_GRP_005` permissions. There may be an arbitrary number of permission sets in a symbol's `permissionSets`.



REST API

  * `otoAllowed` will now appear on `GET /api/v3/exchangeInfo`, that indicates if One-Triggers-the-Other (OTO) orders are supported on that symbol.



WebSocket API

  * `otoAllowed` will now appear on `exchangeInfo`, that indicates if One-Triggers-the-Other (OTO) orders are supported on that symbol.



SBE

  * A new schema 2:0 [spot_2_0.xml](/en/docs/products/spot/sbe/schemas/spot_2_0.xml) has been released. The current schema 1:0 [spot_1_0.xml](/en/docs/products/spot/sbe/schemas/spot_1_0.xml) will thus be deprecated, and retired from the API in 6 months as per our schema deprecation policy.
  * When using schema 1:0 on REST API or WebSocket API, group "permissions" in message "ExchangeInfoResponse" will always be empty. Upgrade to schema 2:0 to find permission information in group "permissionSets". See General changes above for more details.
  * Deprecated OCO requests will still be supported by the latest schema.
  * Note that trying to use schema 2:0 before it is actually released will result in an error.



* * *

### 2024-02-28

**This will take effect on March 5, 2024.**

Simple Binary Encoding (SBE) will be added to the live exchange, both for the Rest API and WebSocket API.

For more information on SBE, please refer to the [FAQ](/en/docs/products/spot/faqs/sbe_faq)

* * *

### 2024-02-08

The SPOT WebSocket API can now support SBE on [SPOT Testnet](https://testnet.binance.vision).

The SBE schema has been updated with WebSocket API metadata without incrementing either `schemaId` or `version`.

Users using SBE only on the REST API may continue to use the SBE schema with git commit hash [`128b94b2591944a536ae427626b795000100cf1d`](/en/docs/products/spot/sbe/schemas/spot_1_0.xml) or update to the newly-published SBE schema.

Users who want to use SBE on the WebSocket API must use the [newly-published SBE schema](/en/docs/products/spot/sbe/schemas/spot_1_0.xml).

The [FAQ](/en/docs/products/spot/faqs/sbe_faq) for SBE has been updated.

* * *

### 2023-12-08

Simple Binary Encoding (SBE) has been added to [SPOT Testnet](https://testnet.binance.vision).

This will be added to the live exchange at a later date.

For more information on what SBE is, please refer to the [FAQ](/en/docs/products/spot/faqs/sbe_faq)

* * *

### 2023-12-04

**Notice:** The changes below are being rolled out gradually, and will take approximately a week to complete.

General Changes:

  * Error message `Precision is over the maximum defined for this asset.` has been changed to `Parameter '%s' has too much precision.`
    * This error message is returned when a parameter has more precision than allowed: e.g. if `base asset` precision is 6 and `quantity=0.1234567` then this error message will appear.
    * This affects all requests with the following parameters:
      * `quantity`
      * `quoteOrderQty`
      * `icebergQty`
      * `limitIcebergQty`
      * `stopIcebergQty`
      * `price`
      * `stopPrice`
      * `stopLimitPrice`
  * Requests for open OCO now correctly return results in **ascending order**. This affects the following requests:
    * REST API: `GET /api/v3/openOrderList`
    * WebSocket API: `openOrderList.status`
  * Requests for all OCO now correctly return results in **ascending order** when `startTime` or `fromId` are specified. This affects the following requests:
    * REST API: `GET /api/v3/allOrderList`
    * WebSocket API: `allOrderLists`
  * Fixed a bug where order query requests would incorrectly return [`-2026 ORDER_ARCHIVED`](/en/docs/products/spot/errors#-2026-order_archived) error for newly placed orders.
    * REST API: `GET /api/v3/order`
    * WebSocket API: `order.status`



REST API

  * New endpoint `GET /api/v3/account/commission`
  * New endpoint `GET /api/v3/ticker/tradingDay`
  * `GET /api/v3/avgPrice` response has a new field `closeTime`, indicating the last trade time.
  * `GET /api/v3/klines` and `/api/v3/uiKlines` have a new optional parameter `timeZone`.
  * `POST /api/v3/order/test` and `POST /api/v3/sor/order/test` have a new optional parameter `computeCommissionRates`.
  * Changes regarding invalid endpoints being sent:
    * Previously, if you query an non-existing endpoint (e.g. `curl -X GET "https://api.binance.com/api/v3/exchangie`) you would get a HTTP 404 code with the response `<html><body><h2>404 Not found</h2></body></html>`
    * From now on the HTML response will only appear if the Accept request header has `text/html` for this situation. The HTTP code will remain the same.



WebSocket API

  * New request `account.commission`
  * New requests to allow session authentication: **(Note that these requests can only be used with Ed25519 keys.)**
    * `session.logon`
    * `session.logout`
    * `session.status`
  * New request `ticker.tradingDay`
  * `avgPrice` response has a new field `closeTime`, indicating the last trade time.
  * `klines` and `uiKlines` have a new optional parameter `timeZone`.
  * `order.test` and `sor.order.test` have a new optional parameter `computeCommissionRates`.
  * Fixed a bug where unsolicited pongs sent before the ping would cause disconnection.



WebSocket Streams

  * New stream `<symbol>@avgPrice`
  * `id` now supports the same values as used for `id` in the WebSocket API:
    * 64-bit signed integers (previously this was unsigned)
    * Alphanumeric strings, max of 36 in length
    * `null`
  * Fixed a bug where unsolicited pongs sent before the ping would cause disconnection.



User Data Streams

  * When an event of type `executionReport` has an execution type (`x`) of `TRADE_PREVENTION`, fields `l`, `L` and `Y` will now always be 0. New fields `pl`, `pL` and `pY` will describe the prevented execution quantity, prevented execution price, and prevented execution notional instead. These new fields show the values of what would `l`, `L` and `Y` have been if the taker order didn't have self-trade prevention enabled.



**The following will take effect _approximately_ a week after the release date:**

  * Symbol Permissions will only affect order placement, not cancellation.
    * `permissions` still apply to Cancel-Replace orders (i.e. The cancellation won't be allowed if your account does have the permission to place an order using this request.)



* * *

### 2023-10-19

**Effective on 2023-10-19 00:00 UTC**

  * The request weights of the following requests have been increased:

REST API| WebSocket API| Condition| Previous Request Weight| New Request Weight  
---|---|---|---|---  
`GET /api/v3/trades`| `trades.recent`| N/A| 2| 10  
`GET /api/v3/depth`| `depth`| **Limit 1-100**|  2| 5  
`GET /api/v3/depth`| `depth`| **Limit 101-500**|  10| 25  
`GET /api/v3/depth`| `depth`| **Limit 501-1000**|  20| 50  
`GET /api/v3/depth`| `depth`| **Limit 1001-5000**|  100| 250  
  
* * *

### 2023-10-03

  * **Order decrement feature went live at 06:15 UTC**.
  * For more information on this feature, please refer to our [FAQ](/en/docs/products/spot/faqs/order_count_decrement)



* * *

### 2023-08-25

  * For WebSocket API, removed `RAW REQUESTS` rate limit in `exchangeInfo`, replaced it with `CONNECTIONS` rate limit, which is the limit for new Websocket connections.



**The following changes will be effective from 2023-08-25 at UTC 00:00.**

  * The `CONNECTIONS` rate limit for WebSocket API has been adjusted to 300 every 5 minutes.
  * The `REQUEST_WEIGHT` rate limit for both REST and WebSocket API has been adjusted to 6,000 every minute.
  * The `RAW_REQUESTS` rate limit for REST API has been adjusted to 61,000 every 5 minutes.
  * Previously, connecting to WebSocket API used to cost 1 weight. **The cost is now 2**.
  * The weights to the following requests for both REST API and WebSocket API have been adjusted.



Please refer to the table for more details:

Request| Previous Request Weight| New Request Weight  
---|---|---  
`GET /api/v3/order` `order.status`| 2| 4  
`GET /api/v3/orderList` orderList.status| 2| 4  
`GET /api/v3/openOrders` `openOrders.status` \- **With`symbol`**| 3| 6  
`GET /api/v3/openOrders` `openOrders.status` \- **Without`symbol`**| 40| 80  
`GET /api/v3/openOrderList` `openOrderLists.status`| 3| 6  
`GET /api/v3/allOrders` `allOrders`| 10| 20  
`GET /api/v3/allOrderList` `allOrderLists`| 10| 20  
`GET /api/v3/myTrades` `myTrades`| 10| 20  
`GET /api/v3/myAllocations` `myAllocations`| 10| 20  
`GET /api/v3/myPreventedMatches` `myPreventedMatches` \- **Using`preventedMatchId`**| 1| 2  
`GET /api/v3/myPreventedMatches` `myPreventedMatches` \- **Using`orderId`**| 10| 20  
`GET /api/v3/account` `account.status`| 10| 20  
`GET /api/v3/rateLimit/order` `account.rateLimits.orders`| 20| 40  
`GET /api/v3/exchangeInfo` `exchangeInfo`| 10| 20  
`GET /api/v3/depth` `depth` \- **Limit 1-100**|  1| 2  
`GET /api/v3/depth` `depth` \- **Limit 101-500**|  5| 10  
`GET /api/v3/depth` `depth` \- **Limit 501-1000**|  10| 20  
`GET /api/v3/depth` `depth` \- **Limit 1001-5000**|  50| 100  
`GET /api/v3/aggTrades` `trades.aggregate`| 1| 2  
`GET /api/v3/trades` `trades.recent`| 1| 2  
`GET /api/v3/historicalTrades` `trades.historical`| 5| 10  
`GET /api/v3/klines` `klines`| 1| 2  
`GET /api/v3/uiKlines` `uiKlines`| 1| 2  
`GET /api/v3/ticker/bookTicker` `ticker.book` \- **With`symbol`**| 1| 2  
`GET /api/v3/ticker/bookTicker` `ticker.book` \- **Without`symbol`** or **With`symbols`**| 2| 4  
`GET /api/v3/ticker/price` `ticker.price` \- **With`symbol`**| 1| 2  
`GET /api/v3/ticker/price` `ticker.price` \- **Without`symbol`** or **With`symbols`**| 2| 4  
`GET /api/v3/ticker/24hr` `ticker.24hr` \- **With`symbol`** or **With`symbols` using 1-20 symbols**| 1| 2  
`GET /api/v3/ticker/24hr` `ticker.24hr` \- **With`symbols using 21-100 symbols`**| 20| 40  
`GET /api/v3/ticker/24hr` `ticker.24hr` \- **Without`symbol` or `symbols using 101 or more symbols`**| 40| 80  
`GET /api/v3/avgPrice` `avgPrice`| 1| 2  
`GET /api/v3/ticker` `ticker`| 2| 4  
`GET /api/v3/ticker` `ticker` \- Maximum weight for this request| 100| 200  
`POST /api/v3/userDataStream` `userDataStream.start`| 1| 2  
`PUT /api/v3/userDataStream` `userDataStream.ping`| 1| 2  
`DELETE /api/v3/userDataStream` `userDataStream.stop`| 1| 2  
  
* * *

### 2023-08-08

Smart Order Routing (SOR) has been added to the APIs. For more information please refer to our [FAQ](/en/docs/products/spot/faqs/sor_faq). Please wait for future announcements on when the feature will be enabled.

REST API

  * Changes to `GET /api/v3/exchangeInfo`:
    * New field in response: `sors`, describing SORs enabled on the exchange.
  * Changes to `GET /api/v3/myPreventedMatches`
    * New field `makerSymbol` will appear in the response for all prevented matches.
  * New endpoints for order placement using SOR:
    * `POST /api/v3/sor/order`
    * `POST /api/v3/sor/order/test`
  * New endpoint `GET /api/v3/myAllocations`



WEBSOCKET API

  * Changes to `exchangeInfo`:
    * New field in response: `sors`, describing SORs enabled on the exchange.
  * Changes to `myPreventedMatches`:
    * New field `makerSymbol` will appear in the response for all prevented matches.
  * New requests for order placement using SOR:
    * `sor.order.place`
    * `sor.order.test`
  * New request `myAllocations`



USER DATA STREAM

  * Changes to `executionReport`:
    * These fields are only relevant for orders placed using SOR:
      * New field `b` for `matchType`
      * New field `a` for `allocId`
      * New field `k` for `workingFloor`
    * This field is only relevant for orders expiring due to STP:
      * New field `Cs` for `counterSymbol`



* * *

### 2023-07-18

  * New API key type – Ed25519 – is now supported. (UI support will be released this week.)
    * Ed25519 API keys are an alternative to RSA API keys, using asymmetric cryptography to authenticate your requests on the API.
    * **We recommend switching to Ed25519** for improved performance and security.  For more information, please refer to the [API Key Types](/en/docs/products/spot/faqs/api_key_types).
  * Documentation has been updated with how to sign a payload with Ed25519 keys.



* * *

### 2023-07-11

**Notice:** The change below are being rolled out, and will take approximately a week to complete.

General Changes:

  * Changes to error messages:
    * Previously, when duplicate symbols were passed to requests that do not allow it, the error would be "Mandatory parameter symbols was not sent, was empty/null, or malformed."
    * Now, the error message is "Symbol is present multiple times in the list", with a new error code `-1151`
    * This affects the following requests:
      * `GET /api/v3/exchangeInfo`
      * `GET /api/v3/ticker/24hr`
      * `GET /api/v3/ticker/price`
      * `GET/api/v3/ticker/bookTicker`
      * `exchangeInfo`
      * `ticker.24hr`
      * `ticker.price`
      * `ticker.book`
  * Fixed a bug where some non-archived orders being queried would receive the error code that their order was archived.



Rest API

  * Changes to `GET /api/v3/account`:
    * New field `preventSor` will appear in the response.
    * New field `uid` that shows the User Id/Account will appear in the response.
  * Changes to `GET /api/v3/historicalTrades`:
    * Changed security type from `MARKET_DATA` to `NONE`.
    * This means that the `X-MBX-APIKEY` header is no longer necessary and is now ignored.



Websocket API

  * Changes to `account.status`:
    * New field `preventSor` will appear in the response.
    * New field `uid` that shows the User Id/Account will appear in the response.
  * Changes to `trades.historical`:
    * Changed security type from `MARKET_DATA` to `NONE`.
    * This means that the `apiKey` parameter is no longer necessary and is now ignored.



**The following changes will take effect _approximately a week from the release date_ :**:

  * Fixed multiple bugs with orders that use `type=MARKET` and `quoteOrderQty`, also known as “reverse market orders”:
    * Reverse market orders are no longer partially filled, or filled for zero or negative quantity under extreme market conditions.
    * `MARKET_LOT_SIZE` filter now correctly rejects reverse market orders that go over the symbol's `maxQty`.
  * Fixed a bug where OCO orders using `trailingDelta` could have an incorrect `trailingTime` value after either leg of the OCO is touched.
  * New field `transactTime` will appear in order cancellation responses. This affects the following requests:
    * `DELETE /api/v3/order`
    * `POST /api/v3/order/cancelReplace`
    * `DELETE /api/v3/openOrders`
    * `DELETE /api/v3/orderList`
    * `order.cancel`
    * `order.cancelReplace`
    * `openOrders.cancelAll`
    * `orderList.cancel`



* * *

### 2023-06-06

  * A new endpoint is now available for redundancy: **<https://api-gcp.binance.com/>**
    * This is using the GCP (Google Cloud Platform) CDN and may have slower performance compared to `api1`-`api4` endpoints.



* * *

### 2023-05-26

**Notice:** The change below are being rolled out, and will take approximately a week to complete.

  * The following base endpoints may give better performance but have less stability than **<https://api.binance.com>** :
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**



* * *

### 2023-05-24

  * **The previous market data URLs have been deprecated. Please update your code immediately to prevent interruption of our services.**
    * API Market data from `data.binance.com` can now be accessed from `data-api.binance.vision`.
    * Websocket Market Data from `data-stream.binance.com` can now be accessed from `data-stream.binance.vision`.



* * *

### 2023-03-13

**Notice:** All changes are being rolled out gradually to all our servers, and may take a week to complete.

GENERAL CHANGES

  * The error messages for certain issues have been improved for easier troubleshooting.

Situation| Old Error Message| New Error Message  
---|---|---  
An account cannot place or cancel an order, due to trading ability disabled.| This action is disabled on this account.| This account may not place or cancel orders.  
When the permissions configured on the symbol do not match the permissions on the account.| This action is disabled on this account.| This symbol is not permitted for this account.  
When the account tries to place an order on a symbol it has no permissions for.| This action is disabled on this account.| This symbol is restricted for this account.  
Placing an order when `symbol` is not `TRADING`.| Unsupported order combination.| This order type is not possible in this trading phase.  
Placing an order with `timeinForce`=`IOC` or `FOK` on a trading phase that does not support it.| Unsupported order combination.| Limit orders require GTC for this phase.  
  
  * Fixed error message for querying archived orders:

    * Previously, if an archived order (i.e. order with status `CANCELED` or `EXPIRED` where `executedQty` == 0 that occurred more than 90 days in the past.) is queried, the error message would be:
    
    Code
    
    {
      "code": -2013,
      "msg": "Order does not exist."
    }

    * Now, the error message is:
    
    Code
    
    {
      "code": -2026,
      "msg": "Order was canceled or expired with no executed qty over 90 days ago and has been archived."
    }

  * Behavior for API requests with `startTime` and `endTime`:

    * Previously some requests failed if the `startTime` == `endTime`.
    * Now, all API requests that accept `startTime` and `endTime` allow the parameters to be equal. This applies to the following requests:
      * Rest API
        * `GET /api/v3/aggTrades`
        * `GET /api/v3/klines`
        * `GET /api/v3/allOrderList`
        * `GET /api/v3/allOrders`
        * `GET /api/v3/myTrades`
      * Websocket API
        * `trades.aggregate`
        * `klines`
        * `allOrderList`
        * `allOrders`
        * `myTrades`
  * Users connected to the websocket API will now be disconnected if their IP is banned due to violation of the IP rate limits (status `418`).




The following changes will take effect **approximately a week from the release date** , but the rest of the documentation has been updated to reflect the future changes:

  * Changes to Filter Evaluation:
    * Previous behavior: `LOT_SIZE` and `MARKET_LOT_SIZE` required that (`quantity` \- `minQty`) % `stepSize` == 0.
    * New behavior: This has now been changed to (`quantity` % `stepSize`) == 0.
  * Bug fix with reverse `MARKET` orders (i.e., `MARKET` using `quoteOrderQty`):
    * Previous behavior: Reverse market orders would always have the status `FILLED` even if the order did not fully fill due to low liquidity.
    * New behavior: If the reverse market order did not fully fill due to low liquidity the order status will be `EXPIRED`, and `FILLED` only if the order was completely filled.



REST API

  * Changes to `DELETE /api/v3/order` and `POST /api/v3/order/cancelReplace`:
    * A new optional parameter `cancelRestrictions` that determines whether the cancel will succeed if the order status is `NEW` or `PARTIALLY_FILLED`.
    * If the order cancellation fails due to `cancelRestrictions`, the error will be:
    
    Code
    
    {
      "code": -2011,
      "msg": "Order was not canceled due to cancel restrictions."
    }




WEBSOCKET API

  * Changes to `order.cancel` and `order.cancelReplace`:
    * A new optional parameter `cancelRestrictions` that determines whether the cancel will succeed if the order status is `NEW` or `PARTIALLY_FILLED`.
    * If the order cancellation fails due to `cancelRestrictions`, the error will be:
    
    Code
    
    {
      "code": -2011,
      "msg": "Order was not canceled due to cancel restrictions."
    }




* * *

### 2023-02-17

**Changes to Websocket Limits**

The WS-API and Websocket Stream now only allows 300 connections requests every 5 minutes.

This limit is **per IP address**.

Please be careful when trying to open multiple connections or reconnecting to the Websocket API.

* * *

### 2023-01-26

As per the [announcement](https://www.binance.com/en/support/announcement/binance-spot-launches-self-trade-prevention-stp-function-on-api-312fd0112fb44635b397c116e56d8f84), Self Trade Prevention will be enabled at **2023-01-26 08:00 UTC**.

Please refer to `GET /api/v3/exchangeInfo` from the Rest API or `exchangeInfo` from the Websocket API on the default and allowed modes.

* * *

### 2023-01-23

New API cluster has been added. Note that all endpoints are functionally equal, but may vary in performance.

  * <https://api4.binance.com>



* * *

### 2023-01-19

**ACTUAL RELEASE DATE TBD**

**New Feature** : Self-Trade Prevention (aka STP) will be added to the system at a later date. This will prevent orders from matching with orders from the same account, or accounts under the same `tradeGroupId`.

Please refer to `GET /api/v3/exchangeInfo` from the Rest API or `exchangeInfo` from the Websocket API on the status.
    
    
    Code
    
    {
        "defaultSelfTradePreventionMode": "NONE",     // If selfTradePreventionMode not provided, this will be the value passed to the engine
        "allowedSelfTradePreventionModes": [          // What the allowed modes of selfTradePrevention are
            "NONE",
            "EXPIRE_TAKER",
            "EXPIRE_BOTH",
            "EXPIRE_MAKER"
        ]
    }

Additional details on the functionality of STP is explained in the [STP FAQ](/en/docs/products/spot/faqs/stp_faq) document.

REST API

  * New order status: `EXPIRED_IN_MATCH` \- This means that the order expired due to STP being triggered.
  * New endpoint:
    * `GET /api/v3/myPreventedMatches` \- This queries the orders that expired due to STP being triggered.
  * New optional parameter `selfTradePreventionMode` has been added to the following endpoints:
    * `POST /api/v3/order`
    * `POST /api/v3/order/oco`
    * `POST /api/v3/cancelReplace`
  * New responses that will appear for all order placement endpoints if there was a prevented match (i.e. if an order could have matched with an order of the same account, or the accounts are in the same `tradeGroupId`):
    * `tradeGroupId` \- This will only appear if account is configured to a `tradeGroupId` and if there was a prevented match.
    * `preventedQuantity` \- Only appears if there was a prevented match.
    * An array `preventedMatches` with the following fields:
      * `preventedMatchId`
      * `makerOrderId`
      * `price`
      * `takerPreventedQuantity` \- This will only appear if `selfTradePreventionMode` set is `EXPIRE_TAKER` or `EXPIRE_BOTH`.
      * `makerPreventedQuantity` \- This will only appear if `selfTradePreventionMode` set is `EXPIRE_MAKER` or `EXPIRE_BOTH`.
  * New fields `preventedMatchId` and `preventedQuantity` that can appear in the order query endpoints if the order had expired due to an STP trigger:
    * `GET /api/v3/order`
    * `GET /api/v3/openOrders`
    * `GET /api/v3/allOrders`



WEBSOCKET API

  * New order status: `EXPIRED_IN_MATCH` \- This means that the order expired due to STP being triggered.
  * New optional parameter `selfTradePreventionMode` has been added to the following requests:
    * `order.place`
    * `orderList.place`
    * `order.cancelReplace`
  * New request: `myPreventedMatches` \- This queries the orders that expired due to STP being triggered.
  * New responses that will appear for all order placement endpoints if there was a prevented match (i.e. if an order could have matched with an order of the same account, or the accounts are in the same `tradeGroupId`):
    * `tradeGroupId` \- This will only appear if account is configured to a `tradeGroupId` and if there was a prevented match.
    * `preventedQuantity` \- Only appears if there was a prevented match.
    * An array `preventedMatches` with the following fields:
      * `preventedMatchId`
      * `makerOrderId`
      * `price`
      * `takerPreventedQuantity` \- This will only appear if `selfTradePreventionMode` set is `EXPIRE_TAKER` or `EXPIRE_BOTH`.
      * `makerPreventedQuantity` \- This will only appear if `selfTradePreventionMode` set is `EXPIRE_MAKER` or `EXPIRE_BOTH`.
  * New fields `preventedMatchId` and `preventedQuantity` that can appear in the order query requests if the order had expired due to STP trigger:
    * `order.status`
    * `openOrders.status`
    * `allOrders`



USER DATA STREAM

  * New execution Type: `TRADE_PREVENTION`
  * New fields for `executionReport` (These fields will only appear if the order has expired due to STP trigger)
    * `u` \- `tradeGroupId`
    * `v` \- `preventedMatchId`
    * `U` \- `counterOrderId`
    * `A` \- `preventedQuantity`
    * `B` \- `lastPreventedQuantity`



* * *

### 2022-12-28

  * SPOT WebSocket API documentation has been updated to show how to sign a request using an RSA key.



* * *

### 2022-12-26

  * Spot WebSocket API is now available on the live exchange.
  * Spot Websocket API can be accessed through this URL: `wss://ws-api.binance.com/ws-api/v3`



* * *

### 2022-12-15

  * New RSA signature
    * Documentation has been updated to show how to create RSA keys.
    * For security reasons, we recommend to use RSA keys instead of HMAC keys when generating an API key.
    * We accept `PKCS#8` (BEGIN PUBLIC KEY).
    * More details on how to upload your RSA public key will be added at a later date.
  * SPOT WebSocket API is now available on **SPOT Testnet**.
    * WebSocket API allows placing orders, canceling orders, etc. through a WebSocket connection.
    * WebSocket API is a **separate** service from WebSocket Market Data streams. I.e., placing orders and listening to market data requires two separate WebSocket connections.
    * WebSocket API is subject to the same Filter and Rate Limit rules as REST API.
    * WebSocket API and REST API are functionally equivalent: they provide the same features, accept the same parameters, return the same status and error codes.



**WEBSOCKET API WILL BE AVAILABLE ON THE LIVE EXCHANGE AT A LATER DATE.**

* * *

### 2022-12-13

REST API

Some error messages on error code `-1003` have changed.

  * Previous error message: `Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.` has been updated to:


    
    
    Code
    
    Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.

  * Previous error message `Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.` has been updated to:


    
    
    Code
    
    Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.

* * *

### 2022-12-05

**Notice:** These changes are being rolled out gradually to all our servers, and will take approximately a week to complete.

WEBSOCKET

  * `!bookTicker` will be removed by **December 7, 2022**. Please use the Individual Book Ticker Streams instead (`<symbol>@bookTicker`).
    * Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection. (E.g. `wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker`)



REST API

  * New error code `-1135`
    * This error code will occur if a parameter requiring a JSON object is invalid.
  * New error code `-1108`
    * This error will occur if a value to a parameter being sent was too large, potentially causing overflow.
    * This error code can occur in the following endpoints:
      * `POST /api/v3/order`
      * `POST /api/v3/order/cancelReplace`
      * `POST /api/v3/order/oco`
  * Changes to `GET /api/v3/aggTrades`
    * Previous behavior: `startTime` and `endTime` had to be used in combination and could only be an hour apart.
    * New behavior: `startTime` and `endTime` can be used individually and the 1 hour limit has been removed.
      * When using `startTime` only, this will return trades from that time, up to the `limit` provided.
      * When using `endTime` only, this will return trades before that time, up to the `limit` provided.
      * If `limit` not provided, regardless of used in combination or sent individually, the endpoint will use the default limit.
  * Changes to `GET /api/v3/myTrades`
    * Fixed a bug where `symbol` \+ `orderId` combination would return all trades even if the number of trades went beyond the `500` default limit.

    * Previous behavior: The API would send specific error messages depending on the combination of parameters sent. E.g:
          
          Code
          
          {
            "code": -1106,
            "msg": "Parameter X was sent when not required."
          }

    * New behavior: If the combinations of optional parameters to the endpoint were not supported, then the endpoint will respond with the generic error:
          
          Code
          
          {
            "code": -1128,
            "msg": "Combination of optional parameters invalid."
          }

    * Added a new combination of supported parameters: `symbol` \+ `orderId` \+ `fromId`.

    * The following combinations of parameters were previously supported but no longer accepted, as these combinations were only taking `fromId` into consideration, ignoring `startTime` and `endTime`:

      * `symbol` \+ `fromId` \+ `startTime`
      * `symbol` \+ `fromId` \+ `endTime`
      * `symbol` \+ `fromId` \+ `startTime` \+ `endTime`
    * Thus, these are the supported combinations of parameters:

      * `symbol`
      * `symbol` \+ `orderId`
      * `symbol` \+ `startTime`
      * `symbol` \+ `endTime`
      * `symbol` \+ `fromId`
      * `symbol` \+ `startTime` \+ `endTime`
      * `symbol`\+ `orderId` \+ `fromId`



**Note:** These new fields will appear approximately a week from the release date.

  * Changes to `GET /api/v3/exchangeInfo`
    * New fields `defaultSelfTradePreventionMode` and `allowedSelfTradePreventionModes`
  * Changes to the Order Placement Endpoints/Order Query/Order Cancellation Endpoints:
    * New field `selfTradePreventionMode` will appear in the response.
    * Affects the following endpoints:
      * `POST /api/v3/order`
      * `POST /api/v3/order/oco`
      * `POST /api/v3/order/cancelReplace`
      * `GET /api/v3/order`
      * `DELETE /api/v3/order`
      * `DELETE /api/v3/orderList`
  * Changes to `GET /api/v3/account`
    * New field `requireSelfTradePrevention` will appear in the response.
  * New field `workingTime`, indicating when the order started working on the order book, will appear in the following endpoints:
    * `POST /api/v3/order`
    * `GET /api/v3/order`
    * `POST /api/v3/order/cancelReplace`
    * `POST /api/v3/order/oco`
    * `GET /api/v3/order`
    * `GET /api/v3/openOrders`
    * `GET /api/v3/allOrders`
  * Field `trailingTime`, indicating the time when the trailing order is active and tracking price changes, will appear for the following order types (`TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `STOP_LOSS`, `STOP_LOSS_LIMIT` if `trailingDelta` parameter was provided) for the following endpoints:
    * `POST /api/v3/order`
    * `GET /api/v3/order`
    * `GET /api/v3/openOrders`
    * `GET /api/v3/allOrders`
    * `POST /api/v3/order/cancelReplace`
    * `DELETE /api/v3/order`
  * Field `commissionRates` will appear in the `GET /api/v3/acccount` response



USER DATA STREAM

  * eventType `executionReport` has new fields
    * `V` \- `selfTradePreventionMode`
    * `D` \- `trailing_time` (Appears if the trailing stop order is active)
    * `W` \- `workingTime` (Appears if `isWorking`=`true`)



* * *

### 2022-12-02

  * Added a new market data base URL `https://data.binance.com`.
  * Added a new WebSocket URL `wss://data-stream.binance.com`.



* * *

### 2022-09-30

Scheduled changes to the removal of `!bookTicker` around November 2022.

  * The All Book Tickers stream (`!bookTicker`) is set to be removed in **November 2022**.
  * More details of the actual removal date will be announced at a later time.
  * Please use the Individual Book Ticker Streams instead. (`<symbol>@bookTicker`).
  * Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection.
    * Example: wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker



* * *

### 2022-09-15

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

  * Changes to `GET /api/v3/exchangeInfo`
    * New optional parameter `permissions` added to display all symbols with the permissions matching the parameter provided. (eg.`SPOT`,`MARGIN`)
    * If not provided, the default value will be `["SPOT","MARGIN","LEVERAGED"]`.
      * This means the request `GET /api/v3/exchangeInfo` without any parameters will show all symbols that can be used for `SPOT`, `MARGIN`, and/or `LEVERAGED` trading.
      * To search for symbols that can be traded on other permissions (e.g. `TRD_GRP_004`, etc), then this needs to be searched for explicitly. (e.g.`permissions`=`TRD_GRP_004`)
    * Cannot be combined with `symbol` or `symbols`



* * *

### 2022-08-23

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

  * Changes to `GET /api/v3/ticker` and `GET /api/v3/ticker/24hr`
    * New optional parameter `type` added
    * Supported values for parameter `type` are `FULL` and `MINI`
      * `FULL` is the default value and the response that is currently being returned from the endpoint
      * `MINI` omits the following fields from the response: `priceChangePercent`, `weightedAvgPrice`, `bidPrice`, `bidQty`, `askPrice`, `askQty`, and `lastQty`
  * New error code `-1008`
    * This is sent whenever the servers are overloaded with requests.
  * New field `brokered` has been added to `GET /api/v3/account`
  * New kline interval: `1s`
  * New endpoint added: `GET /api/v3/uiKlines`



* * *

### 2022-08-08

REST API

  * Changes to `POST /api/v3/order` and `POST /api/v3/order/cancelReplace`
    * New optional fields `strategyId` and `strategyType`
      * `strategyId` is a parameter used to identify an order as part of a strategy.
      * `strategyType` is a parameter used to identify what strategy was running. (E.g. If all the orders are part of spot grid strategy, it can be set to `strategyType=1000000`)
        * Note that the minimum value allowed for `strategyType` is `1000000`.
  * Changes to `POST /api/v3/order/oco`
    * New optional fields `limitStrategyId`, `limitStrategyType`, `stopStrategyId`, `stopStrategyType`
    * These are the strategy metadata parameters for both legs of the OCO orders.
    * `limitStrategyType` and `stopStrategyType` both cannot be less than `1000000`.
  * Changes to `GET /api/v3/order`, `GET /api/v3/openOrders`, and `GET /api/v3/allOrders`
    * New fields `strategyId` and `strategyType` will appear in the response JSON for orders that had these fields populated upon order placement.
  * Changes to `DELETE /api/v3/order` and `DELETE /api/v3/openOrders`
    * New fields `strategyId` and `strategyType` will appear in the response JSON for cancelled orders that had these fields populated upon order placement.



USER DATA STREAM

  * New fields to eventType `executionReport`
    * `j` for `strategyId`
    * `J` for `strategyType`
    * Note that these fields only appear if these were populated upon order placement.



* * *

### 2022-06-20

Changes to `GET /api/v3/ticker`

  * Weight has been reduced from 5 to 2 per symbol, regardless of `windowSize`.
  * The max number of symbols that can be processed in a request is 100.
    * If the number of `symbols` sent is more than 100, the error will be as follows:
    
    Code
    
    {
      "code": -1101,
      "msg": "Too many values sent for parameter 'symbols', maximum allowed up to 100."
    }

  * The max Weight for this endpoint will cap at 100.
    * I.e. If the request has more than 50 symbols, the Weight will still be 100, regardless of `windowSize`.



* * *

### 2022-06-15

**Note:** The update is being rolled out over the next few days, so these changes may not be visible right away.

SPOT API

  * `GET /api/v3/ticker` added
    * Rolling window price change statistics based on `windowSize` provided.
    * Contrary to `GET /api/v3/ticker/24hr` the list of symbols cannot be omitted.
    * If `windowSize` not specified, the value will default to `1d`.
    * Response is similar to `GET /api/v3/ticker/24hr`, minus the following fields: `prevClosePrice`, `lastQty`, `bidPrice`, `bidQty`, `askPrice`, `askQty`
  * `GET /api/v3/exchangeInfo` returns new field `cancelReplaceAllowed` in `symbols` list.
  * `POST /api/v3/order/cancelReplace` added
    * Cancels an existing order and places a new order on the same symbol.
    * The filters are evaluated **before** the cancel order is placed.
      * e.g. If the `MAX_NUM_ORDERS` filter is 10, and the total number of open orders on the account is also 10, when using `POST /api/v3/order/cancelReplace` both the cancel order placement and new order will fail because of the filter.
    * The change is being rolled out in the next few days, thus this feature will be enabled once the upgrade is completed.
  * New filter `NOTIONAL` has been added.
    * Defines the allowed notional value (`price * quantity`) based on a configured `minNotional` and `maxNotional`
  * New exchange filter `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` has been added.
    * Defines the limit of open iceberg orders on an account



* * *

### 2022-05-23

  * Changes to Order Book Depth Levels

    * Quantities in the Depth levels were returning negative values in situations where they were exceeding the max value, resulting in an overflow.
    * Going forward depth levels will not overflow, but will be capped at the max value based on the precision of the base asset. This means that the depth level is at max value _or more_.
      * E.g. If the precision is 8, then the max value for quantity will be at 92,233,720,368.54775807.
    * When the fix has been applied, a change in the order book at the affected price level is required for the changes to be visible.
  * What does this affect?

    * SPOT API
      * `GET /api/v3/depth`
    * Websocket Streams
      * `<symbol>@depth`
      * `<symbol>@depth@100ms`
      * `<symbol>@depth<levels>`
      * `<symbol>@depth<levels>@100ms`
  * Updates to `MAX_POSITION`

    * If an order's `quantity` can cause the position to overflow, this will now fail the `MAX_POSITION` filter.



* * *

### 2022-05-17

  * Changes to GET `api/v3/aggTrades`
    * When providing `startTime` and `endTime`, the oldest items are returned.
  * Changed error messaging on `GET /api/v3/myTrades` where parameter `symbol` is not provided:


    
    
    Code
    
    {
      "code": -1102,
      "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
    }

  * The following endpoints now support multi-symbol querying using the parameter `symbols`.
    * `GET /api/v3/ticker/24hr`
    * `GET /api/v3/ticker/price`
    * `GET /api/v3/ticker/bookTicker`
  * In the above, the request weight will depend on the number of symbols provided in `symbols`.  Please refer to the table below:

Endpoint| Number of Symbols| Weight  
---|---|---  
`GET /api/v3/ticker/price`| Any| 2  
`GET /api/v3/ticker/bookTicker`| Any| 2  
`GET /api/v3/ticker/24hr`| 1-20| 1  
`GET /api/v3/ticker/24hr`| 21-100| 20  
`GET /api/v3/ticker/24hr`| 101 or more| 40  
  
* * *

### 2022-04-13

REST API

  * Trailing Stops have been enabled.
    * This is a type of algo order where the activation is based on a percentage of a price change in the market using the new parameter `trailingDelta`.
    * This can only used with any of the following order types: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.
    * The `trailingDelta` parameter will be done in Basis Points or BIPS.
      * For example: a STOP_LOSS SELL order with a `trailingDelta` of 100 will trigger after a price decrease of 1% from the highest price after the order is placed. (100 / 10,000 => 0.01 => 1%)
    * When used in combination with OCO Orders, the `trailingDelta` will determine when the contingent leg of the OCO will trigger.
    * When `trailingDelta` is used in combination with `stopPrice`, once the `stopPrice` condition is met, the trailing stop starts tracking the price change from the `stopPrice` based on the `trailingDelta` provided.
    * When no `stopPrice` is sent, the trailing stop starts tracking the price changes from the last price based on the `trailingDelta` provided.
  * Changes to POST `/api/v3/order`
    * New optional field `trailingDelta`
  * Changes to POST `/api/v3/order/test`
    * New optional field `trailingDelta`
  * Changes to POST `/api/v3/order/oco`
    * New optional field `trailingDelta`
  * A new filter `TRAILING_DELTA` has been added.
    * This filter is defined by the minimum and maximum values for the `trailingDelta` value.



USER DATA STREAM

  * New field in `executionReport`
    * "d" for `trailingDelta`



* * *

### 2022-04-12

**Note:** The changes are being rolled out during the next few days, so these will not appear right away.

  * Error message changed on `GET api/v3/allOrders` where `symbol` is not provided:
        
        Code
        
        {
          "code": -1102,
          "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
        }

  * Fixed a typo with an error message when an account has disabled permissions (e.g. to withdraw, to trade, etc)
        
        Code
        
        "This action is disabled on this account."

  * During a market data audit, we detected some issues with the Spot aggregate trade data.
    * Missing aggregate trades were recovered.
    * Duplicated records were marked invalid with the following values:
      * p = '0' // price
      * q = '0' // qty
      * f = -1 // ﬁrst_trade_id
      * l = -1 // last_trade_id



* * *

### 2022-02-28

  * New field `allowTrailingStop` has been added to `GET /api/v3/exchangeInfo`



* * *

### 2022-02-24

  * `(price-minPrice) % tickSize == 0` rule in `PRICE_FILTER` has been changed to `price % tickSize == 0`.
  * A new filter `PERCENT_PRICE_BY_SIDE` has been added.
  * Changes to GET `api/v3/depth`
    * The `limit` value can be outside of the previous values (i.e. 5, 10, 20, 50, 100, 500, 1000,5000) and will return the correct limit. (i.e. if limit=3 then the response will be the top 3 bids and asks)
    * The limit still cannot exceed 5000. If the limit provided is greater than 5000, then the response will be truncated to 5000.
    * Due to the changes, these are the updated request weights based on the limit value provided:

Limit| Request Weight  
---|---  
1-100| 1  
101-500| 5  
501-1000| 10  
1001-5000| 50  
  
  * Changes to GET `api/v3/aggTrades`
    * When providing `startTime` and `endTime`, the oldest items are returned.



* * *

### 2021-12-29

  * Removed out dated "Symbol Type" enum; added "Permissions" enum.



### 2021-11-01

  * `GET /api/v3/rateLimit/order` added
    * The endpoint will display the user's current order count usage for all intervals.
    * This endpoint will have a request weight of 20.



### 2021-09-14

  * Add a [YAML file](https://github.com/binance/binance-api-swagger) with OpenApi specification on the RESTful API.



### 2021-08-12

  * GET `api/v3/myTrades` has a new optional field `orderId`



* * *

### 2021-05-12

  * Added `Data Source` in the documentation to explain where each endpoint is retrieving its data.
  * Added field `Data Source` to each API endpoint in the documentation
  * GET `api/v3/exchangeInfo` now supports single or multi-symbol query



* * *

### 2021-04-26

On **April 28, 2021 00:00 UTC** the weights to the following endpoints will be adjusted:

  * `GET /api/v3/order` weight increased to 2
  * `GET /api/v3/openOrders` weight increased to 3
  * `GET /api/v3/allOrders` weight increased to 10
  * `GET /api/v3/orderList` weight increased to 2
  * `GET /api/v3/openOrderList` weight increased to 3
  * `GET /api/v3/account` weight increased to 10
  * `GET /api/v3/myTrades` weight increased to 10
  * `GET /api/v3/exchangeInfo` weight increased to 10



* * *

### 2021-01-01

**USER DATA STREAM**

  * `outboundAccountInfo` has been removed.



* * *

### 2020-11-27

New API clusters have been added in order to improve performance.

Users can access any of the following API clusters, in addition to `api.binance.com`

If there are any performance issues with accessing `api.binance.com` please try any of the following instead:

  * <https://api1.binance.com/api/v3/>*
  * <https://api2.binance.com/api/v3/>*
  * <https://api3.binance.com/api/v3/>*



### 2020-09-09

USER DATA STREAM

  * `outboundAccountInfo` has been deprecated.
  * `outboundAccountInfo` will be removed in the future. (Exact date unknown) **Please use`outboundAccountPosition` instead.**
  * `outboundAccountInfo` will now only show the balance of non-zero assets and assets that have been reduced to 0.



* * *

### 2020-05-01

  * From 2020-05-01 UTC 00:00, all symbols will have a limit of 200 open orders using the [MAX_NUM_ORDERS](/en/docs/products/spot/filters#max_num_orders) filter.
    * No existing orders will be removed or canceled.
    * Accounts that have 200 or more open orders on a symbol will not be able to place new orders on that symbol until the open order count is below 200.
    * OCO orders count as 2 open orders before the `LIMIT` order is touched or the `STOP_LOSS` (or `STOP_LOSS_LIMIT`) order is triggered; once this happens the other order is canceled and will no longer count as an open order.



* * *

### 2020-04-25

REST API

  * New field `permissions`
    * Defines the trading permissions that are allowed on accounts and symbols.
    * `permissions` is an enum array; values:
      * `SPOT`
      * `MARGIN`
    * `permissions` will replace `isSpotTradingAllowed` and `isMarginTradingAllowed` on `GET api/v3/exchangeInfo` in future API versions (v4+).
    * For an account to trade on a symbol, the account and symbol must share at least 1 permission in common.
  * Updates to `GET api/v3/exchangeInfo`
    * New field `permissions` added.
    * New field `quoteAssetPrecision` added; a duplicate of the `quotePrecision` field. `quotePrecision` will be removed in future API versions (v4+).
  * Updates to `GET api/v3/account`
    * New field `permissions` added.
  * New endpoint `DELETE api/v3/openOrders`
    * This will allow a user to cancel all open orders on a single symbol.
    * This endpoint will cancel all open orders including OCO orders.
  * Orders can be canceled via the API on symbols in the `BREAK` or `HALT` status.



USER DATA STREAM

  * `OutboundAccountInfo` has new field `P` which shows the trading permissions of the account.



* * *

### 2020-04-23

WEB SOCKET STREAM

  * WebSocket connections have a limit of 5 incoming messages per second. A message is considered:
    * A PING frame
    * A PONG frame
    * A JSON control message (e.g. subscribe, unsubscribe)
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of 1024 streams.



* * *

### 2020-03-24

  * `MAX_POSITION` filter added.
    * This filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

      * free balance of the base asset
      * locked balance of the base asset
      * sum of the qty of all open BUY orders
    * `BUY` orders will be rejected if the account's position is greater than the maximum position allowed.




* * *

### 2019-11-22

  * Quote Order Qty Market orders have been enabled on all symbols.
    * Quote Order Qty `MARKET` orders allow a user to specify the total `quoteOrderQty` spent or received in the `MARKET` order.
    * Quote Order Qty `MARKET` orders will not break `LOT_SIZE` filter rules; the order will execute a quantity that will have the notional value as close as possible to `quoteOrderQty`.
    * Using `BNBBTC` as an example:
      * On the `BUY` side, the order will buy as many BNB as `quoteOrderQty` BTC can.
      * On the `SELL` side, the order will sell as much BNB as needed to receive `quoteOrderQty` BTC.



* * *

### 2019-11-13

REST API

  * api/v3/exchangeInfo has new fields:
    * `quoteOrderQtyMarketAllowed`
    * `baseCommissionDecimalPlaces`
    * `quoteCommissionDecimalPlaces`
  * `MARKET` orders have a new optional field: `quoteOrderQty` used to specify the quote quantity to BUY or SELL. This cannot be used in combination with `quantity`.
    * The exact timing that `quoteOrderQty` MARKET orders will be enabled is TBD. There will be a separate announcement and further details at that time.
  * All order query endpoints will return a new field `origQuoteOrderQty` in the JSON payload. (e.g. GET api/v3/allOrders)
  * Updated error messages for -1128
    * Sending an `OCO` with a `stopLimitPrice` but without a `stopLimitTimeInForce` will return the error:
    
    Code
    
    {
      "code": -1128,
      "msg": "Combination of optional parameters invalid. Recommendation: 'stopLimitTimeInForce' should also be sent."
    }

  * Updated error messages for -1003 to specify the limit is referring to the request weight, not to the number of requests.



**Deprecation of v1 endpoints** :

By end of Q1 2020, the following endpoints will be removed from the API. The documentation has been updated to use the v3 versions of these endpoints.

  * GET api/v1/depth
  * GET api/v1/historicalTrades
  * GET api/v1/aggTrades
  * GET api/v1/klines
  * GET api/v1/ticker/24hr
  * GET api/v1/ticker/price
  * GET api/v1/exchangeInfo
  * POST api/v1/userDataStream
  * PUT api/v1/userDataStream
  * GET api/v1/ping
  * GET api/v1/time
  * GET api/v1/ticker/bookTicker



**These endpoints however, will NOT be migrated to v3. Please use the following endpoints instead moving forward.**

Old V1 Endpoints| New V3 Endpoints  
---|---  
GET api/v1/ticker/allPrices| GET api/v3/ticker/price  
GET api/v1/ticker/allBookTickers| GET api/v3/ticker/bookTicker  
  
USER DATA STREAM

  * Changes to`executionReport` event

    * If the C field is empty, it will now properly return `null`, instead of `"null"`.
    * New field Q which represents the `quoteOrderQty`.
  * `balanceUpdate` event type added

    * This event occurs when funds are deposited or withdrawn from your account.



WEB SOCKET STREAMS

  * WSS now supports live subscribing/unsubscribing to streams.



* * *

### 2019-09-09

  * New WebSocket streams for bookTickers added: `<symbol>@bookTicker` and `!bookTicker`. See `web-socket-streams.md` for details.



* * *

### 2019-09-03

  * Faster order book data with 100ms updates: `<symbol>@depth@100ms` and `<symbol>@depth#@100ms`
  * Added "Update Speed:" to `web-socket-streams.md`
  * Removed deprecated v1 endpoints as per previous announcement:
    * GET api/v1/order
    * GET api/v1/openOrders
    * POST api/v1/order
    * DELETE api/v1/order
    * GET api/v1/allOrders
    * GET api/v1/account
    * GET api/v1/myTrades



* * *

### 2019-08-16 (Update 2)

  * GET api/v1/depth `limit` of 10000 has been temporarily removed



* * *

### 2019-08-16

  * In Q4 2017, the following endpoints were deprecated and removed from the API documentation. They have been permanently removed from the API as of this version. We apologize for the omission from the original changelog:

    * GET api/v1/order
    * GET api/v1/openOrders
    * POST api/v1/order
    * DELETE api/v1/order
    * GET api/v1/allOrders
    * GET api/v1/account
    * GET api/v1/myTrades
  * Streams, endpoints, parameters, payloads, etc. described in the documents in this repository are **considered official** and **supported**. The use of any other streams, endpoints, parameters, or payloads, etc. is **not supported; use them at your own risk and with no guarantees.**




* * *

### 2019-08-15

REST API

  * New order type: OCO ("One Cancels the Other")

    * An OCO has 2 orders: (also known as legs in financial terms)

      * `STOP_LOSS` or `STOP_LOSS_LIMIT` leg
      * `LIMIT_MAKER` leg
    * Price Restrictions:

      * `SELL Orders` : Limit Price > Last Price > Stop Price
      * `BUY Orders` : Limit Price < Last Price < Stop Price
      * As stated, the prices must "straddle" the last traded price on the symbol. EX: If the last price is 10:
        * A SELL OCO must have the limit price greater than 10, and the stop price less than 10.
        * A BUY OCO must have a limit price less than 10, and the stop price greater than 10.
    * Quantity Restrictions:

      * Both legs must have the **same quantity**.
      * `ICEBERG` quantities however, do not have to be the same.
    * Execution Order:

      * If the `LIMIT_MAKER` is touched, the limit maker leg will be executed first BEFORE canceling the Stop Loss Leg.
      * if the Market Price moves such that the `STOP_LOSS` or `STOP_LOSS_LIMIT` will trigger, the Limit Maker leg will be canceled BEFORE executing the `STOP_LOSS` Leg.
    * Canceling an OCO

      * Canceling either order leg will cancel the entire OCO.
      * The entire OCO can be canceled via the `orderListId` or the `listClientOrderId`.
    * New Enums for OCO:

      1. `ListStatusType`
         * `RESPONSE` \- used when ListStatus is responding to a failed action. (either order list placement or cancellation)
         * `EXEC_STARTED` \- used when an order list has been placed or there is an update to a list's status.
         * `ALL_DONE` \- used when an order list has finished executing and is no longer active.
      2. `ListOrderStatus`
         * `EXECUTING` \- used when an order list has been placed or there is an update to a list's status.
         * `ALL_DONE` \- used when an order list has finished executing and is no longer active.
         * `REJECT` \- used when ListStatus is responding to a failed action. (either order list placement or cancellation)
      3. `ContingencyType`
         * `OCO` \- specifies the type of order list.
    * New Endpoints:

      * POST api/v3/order/oco
      * DELETE api/v3/orderList
      * GET api/v3/orderList
  * `recvWindow` cannot exceed 60000.

  * New `intervalLetter` values for headers:

    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
  * New Headers `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` will give your current used request weight for the (intervalNum)(intervalLetter) rate limiter. For example, if there is a one minute request rate weight limiter set, you will get a `X-MBX-USED-WEIGHT-1M` header in the response. The legacy header `X-MBX-USED-WEIGHT` will still be returned and will represent the current used weight for the one minute request rate weight limit.

  * New Header `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`that is updated on any valid order placement and tracks your current order count for the interval; rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.

    * Eg. `X-MBX-ORDER-COUNT-1S` for "orders per 1 second" and `X-MBX-ORDER-COUNT-1D` for orders per "one day"
  * GET api/v1/depth now supports `limit` 5000 and 10000; weights are 50 and 100 respectively.

  * GET api/v1/exchangeInfo has a new parameter `ocoAllowed`.




USER DATA STREAM

  * `executionReport` event now contains "g" which has the `orderListId`; it will be set to -1 for non-OCO orders.
  * New Event Type `listStatus`; `listStatus` is sent on an update to any OCO order.
  * New Event Type `outboundAccountPosition`; `outboundAccountPosition` is sent any time an account's balance changes and contains the assets that could have changed by the event that generated the balance change (a deposit, withdrawal, trade, order placement, or cancellation).



NEW ERRORS

  * **-1131 BAD_RECV_WINDOW**
    * `recvWindow` must be less than 60000
  * **-1099 Not found, authenticated, or authorized**
    * This replaces error code -1999



NEW -2011 ERRORS

  * **OCO_BAD_ORDER_PARAMS**
    * A parameter for one of the orders is incorrect.
  * **OCO_BAD_PRICES**
    * The relationship of the prices for the orders is not correct.
  * **UNSUPPORTED_ORD_OCO**
    * OCO orders are not supported for this symbol.



* * *

### 2019-03-12

REST API

  * X-MBX-USED-WEIGHT header added to Rest API responses.
  * Retry-After header added to Rest API 418 and 429 responses.
  * When canceling the Rest API can now return `errorCode` -1013 OR -2011 if the symbol's `status` isn't `TRADING`.
  * `api/v1/depth` no longer has the ignored and empty `[]`.
  * `api/v3/myTrades` now returns `quoteQty`; the price * qty of for the trade.



WEBSOCKET STREAMS

  * `<symbol>@depth` and `<symbol>@depthX` streams no longer have the ignored and empty `[]`.



SYSTEM IMPROVEMENTS

  * Matching Engine stability/reliability improvements.
  * Rest API performance improvements.



* * *

### 2018-11-13

REST API

  * Can now cancel orders through the Rest API during a trading ban.
  * New filters: `PERCENT_PRICE`, `MARKET_LOT_SIZE`, `MAX_NUM_ICEBERG_ORDERS`.
  * Added `RAW_REQUESTS` rate limit. Limits based on the number of requests over X minutes regardless of weight.
  * /api/v3/ticker/price increased to weight of 2 for a no symbol query.
  * /api/v3/ticker/bookTicker increased weight of 2 for a no symbol query.
  * DELETE /api/v3/order will now return an execution report of the final state of the order.
  * `MIN_NOTIONAL` filter has two new parameters: `applyToMarket` (whether or not the filter is applied to MARKET orders) and `avgPriceMins` (the number of minutes over which the price averaged for the notional estimation).
  * `intervalNum` added to /api/v1/exchangeInfo limits. `intervalNum` describes the amount of the interval. For example: `intervalNum` 5, with `interval` minute, means "every 5 minutes".



#### Explanation for the average price calculation:

  1. (qty * price) of all trades / sum of qty of all trades over previous 5 minutes.

  2. If there is no trade in the last 5 minutes, it takes the first trade that happened outside of the 5min window. For example if the last trade was 20 minutes ago, that trade's price is the 5 min average.

  3. If there is no trade on the symbol, there is no average price and market orders cannot be placed. On a new symbol with `applyToMarket` enabled on the `MIN_NOTIONAL` filter, market orders cannot be placed until there is at least 1 trade.

  4. The current average price can be checked here: `https://api.binance.com/api/v3/avgPrice?symbol=<symbol>` For example: <https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT>




USER DATA STREAM

  * `Last quote asset transacted quantity` (as variable `Y`) added to execution reports. Represents the `lastPrice` * `lastQty` (`L` * `l`).



* * *

### 2018-07-18

REST API

  * New filter: `ICEBERG_PARTS`
  * `POST api/v3/order` new defaults for `newOrderRespType`. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.
  * POST api/v3/order `RESULT` and `FULL` responses now have `cummulativeQuoteQty`
  * GET api/v3/openOrders with no symbol weight reduced to 40.
  * GET api/v3/ticker/24hr with no symbol weight reduced to 40.
  * Max amount of trades from GET /api/v1/trades increased to 1000.
  * Max amount of trades from GET /api/v1/historicalTrades increased to 1000.
  * Max amount of aggregate trades from GET /api/v1/aggTrades increased to 1000.
  * Max amount of aggregate trades from GET /api/v1/klines increased to 1000.
  * Rest API Order lookups now return `updateTime` which represents the last time the order was updated; `time` is the order creation time.
  * Order lookup endpoints will now return `cummulativeQuoteQty`. If `cummulativeQuoteQty` is < 0, it means the data isn't available for this order at this time.
  * `REQUESTS` rate limit type changed to `REQUEST_WEIGHT`. This limit was always logically request weight and the previous name for it caused confusion.



USER DATA STREAM

  * `cummulativeQuoteQty` field added to order responses and execution reports (as variable `Z`). Represents the cummulative amount of the `quote` that has been spent (with a `BUY` order) or received (with a `SELL` order). Historical orders will have a value < 0 in this field indicating the data is not available at this time. `cummulativeQuoteQty` divided by `cummulativeQty` will give the average price for an order.
  * `O` (order creation time) added to execution reports



* * *

### 2018-01-23

  * GET /api/v1/historicalTrades weight decreased to 5
  * GET /api/v1/aggTrades weight decreased to 1
  * GET /api/v1/klines weight decreased to 1
  * GET /api/v1/ticker/24hr all symbols weight decreased to number of trading symbols / 2
  * GET /api/v3/allOrders weight decreased to 5
  * GET /api/v3/myTrades weight decreased to 5
  * GET /api/v3/account weight decreased to 5
  * GET /api/v1/depth limit=500 weight decreased to 5
  * GET /api/v1/depth limit=1000 weight decreased to 10
  * -1003 error message updated to direct users to websockets



* * *

### 2018-01-20

  * GET /api/v1/ticker/24hr single symbol weight decreased to 1
  * GET /api/v3/openOrders all symbols weight decreased to number of trading symbols / 2
  * GET /api/v3/allOrders weight decreased to 15
  * GET /api/v3/myTrades weight decreased to 15
  * GET /api/v3/order weight decreased to 1
  * myTrades will now return both sides of a self-trade/wash-trade



* * *

### 2018-01-14

  * GET /api/v1/aggTrades weight changed to 2
  * GET /api/v1/klines weight changed to 2
  * GET /api/v3/order weight changed to 2
  * GET /api/v3/allOrders weight changed to 20
  * GET /api/v3/account weight changed to 20
  * GET /api/v3/myTrades weight changed to 20
  * GET /api/v3/historicalTrades weight changed to 20



Was this page helpful?

Last modified on November 12, 2026

[Introduction](/en/docs/introduction)[Filters](/en/docs/products/spot/filters)

---

# 更新日志

**最近更新：2026-11-11**

### 2026-11-11

  * 错误代码文档更正：
    * `PARAM_OVERFLOW` 的错误代码为 [`-1018`](/zh-CN/docs/products/spot/errors#-1018-%E5%8F%82%E6%95%B0%E6%BA%A2%E5%87%BA)，此前文档误写为 `-1108`。
    * 新增 [`-1108 BAD_ASSET`](/zh-CN/docs/products/spot/errors#-1108-%E6%97%A0%E6%95%88%E7%9A%84%E8%B5%84%E4%BA%A7) "Invalid asset." 的文档说明。此前已在测试网[更新日志](/zh-CN/docs/products/spot/testnet/CHANGELOG#2026-10-28)中说明。



**注意：本节中的变更正在逐步推出，预计大约需要两周时间完成。**

#### 新功能

  * `userDataStream.subscribe` 和 `userDataStream.subscribe.signature` 现在支持可选参数 `filter`，用于控制推送哪些事件。支持按事件类型（`e`）、交易对（`s`）、资产（`a`）和执行类型（`x`）进行过滤。
    * WebSocket API：参见 [用户数据流订阅过滤器](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscription-filters)。
    * `filter` 中的未知交易对和未知资产将分别被拒绝并返回 [`-1121`](/zh-CN/docs/products/spot/errors#-1121-%E6%97%A0%E6%95%88%E7%9A%84%E4%BA%A4%E6%98%93%E5%AF%B9) 和 [`-1108`](/zh-CN/docs/products/spot/errors#-1108-%E6%97%A0%E6%95%88%E7%9A%84%E8%B5%84%E4%BA%A7)。



#### 常规更改

  * `serverShutdown` 事件现在包含 `T` 字段，表示 WebSocket 会话将被关闭的时间。
    * [WebSocket API](/zh-CN/docs/products/spot/web-socket-api#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD)
    * [WebSocket 行情接口](/zh-CN/docs/products/spot/web-socket-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD)
    * [SBE 市场数据流](/zh-CN/docs/products/spot/sbe-market-data-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD)
    * 在 SBE 会话中，`T` 字段仅在 SBE schema 3:6 及更高版本中出现。
  * `-1015 TOO_MANY_ORDERS` 的错误消息已更改为：“Too many orders placed without trading; current limit is X non-trading orders per Y. Unable to place new orders until trades occur or window resets.”参见 [`-1015`](/zh-CN/docs/products/spot/errors#-1015-%E8%AE%A2%E5%8D%95%E5%A4%AA%E5%A4%9A) 和 [现货未成交订单计数规则常见问题](/zh-CN/docs/products/spot/faqs/order_count_decrement#%E7%8E%B0%E8%B4%A7%E6%9C%AA%E6%88%90%E4%BA%A4%E8%AE%A2%E5%8D%95%E8%AE%A1%E6%95%B0%E8%A7%84%E5%88%99)。



#### SBE

  * REST 和 WebSocket API SBE schema [spot_3_6.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_6.xml)
    * 当前的 schema 3:5 [spot_3_5.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_5.xml) 已被弃用，将根据我们的 [schema 弃用政策](/zh-CN/docs/products/spot/faqs/sbe_faq#%E5%85%B3%E4%BA%8E%E5%AF%B9%E6%97%A7%E7%89%88%E6%9C%AC%E7%9A%84%E6%94%AF%E6%8C%81)在 6 个月后停用。
    * schema 3:6 中的变更：
      * 现有枚举 `expiryReason`：新增枚举值 `Exhausted` (9) 和 `InsufficientQuoteNotionalLimit` (10)
      * `ServerShutdownEvent`：新增字段 `shutdownTime`
      * `ExchangeInfoResponse`（symbols 组）：新增字段 `marketQuoteNotionalLimitAllowed`、 `limitQuoteNotionalLimitAllowed`、`opoAllowed`
      * `NewOrderResultResponse`、`NewOrderFullResponse`、`OrderResponse`、`CancelOrderResponse`、 `OrdersResponse`、`NewOrderListResultResponse`、`NewOrderListFullResponse`、 `CancelOrderListResponse`、`OrderAmendKeepPriorityResponse`、`ExecutionReportEvent`：新增字段 `quoteNotionalLimit`
        * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。
      * `ExecutionReportEvent`：新增字段 `effectiveSelfTradePreventionMode`
        * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。
      * `NewOrderFullResponse` 和 `NewOrderListFullResponse.orderReports` 的 `preventedMatches` 组：新增字段 `effectiveSelfTradePreventionMode`
        * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。
    * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。
  * FIX SBE schema [spot-fixsbe-1_2.xml](/zh-CN/docs/products/spot/sbe/schemas/spot-fixsbe-1_2.xml)
    * 当前的 schema 1:1 [spot-fixsbe-1_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot-fixsbe-1_1.xml) 已被弃用，将根据我们的 [schema 弃用政策](/zh-CN/docs/products/spot/faqs/sbe_faq#%E5%85%B3%E4%BA%8E%E5%AF%B9%E6%97%A7%E7%89%88%E6%9C%AC%E7%9A%84%E6%94%AF%E6%8C%81)在 6 个月后停用。
    * schema 1:2 中的变更：
      * 现有枚举 `expiryReason`：新增枚举值 `Exhausted` (9) 和 `InsufficientQuoteNotionalLimit` (10)
      * `ExecutionReport`、`OrderCancelRequestAndNewOrderSingle`、`NewOrderSingle`、`NewOrderList` （`Orders` 组）：新增字段 `QuoteNotionalLimit`（自定义标签 25057）
        * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。
      * `ExecutionReport`：新增字段 `EffectiveSelfTradePreventionMode`（自定义标签 25058）
        * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。
  * SBE 生命周期文件已更新以反映这些变更：
    * [生产环境 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json)
    * [生产环境 FIX SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_fix_schema_lifecycle_prod.json)



#### FIX API

  * [FIX OE 的 QuickFIX schema](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml) 已更新：
    * `ExpiryReason`（自定义标签 25056）：新增值 `EXHAUSTED` (9) 和 `INSUFFICIENT_QUOTE_NOTIONAL_LIMIT` (10)
    * `ExecutionReport`、`OrderCancelRequestAndNewOrderSingle`、`NewOrderSingle`、`NewOrderList` （`Orders` 组）：新增字段 `QuoteNotionalLimit`（自定义标签 25057）
      * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。
    * `ExecutionReport`：新增字段 `EffectiveSelfTradePreventionMode`（自定义标签 25058）
      * 有关该字段的更多详情，请参见下方的 [新功能](/zh-CN/docs/products/spot/CHANGELOG#2026-11-20-new-features)。



**注意：以下变更将于 2026-11-20 07:00 UTC 之后生效。**

#### 新功能

  * `BUY` 方向的订单支持新的可选参数 `quoteNotionalLimit`，用于限制订单可消耗的报价资产名义价值。 **该功能将于晚些时候启用。**
    * 订单列表接受 `aboveQuoteNotionalLimit` / `belowQuoteNotionalLimit`（OCO）以及 `workingQuoteNotionalLimit` / `pendingQuoteNotionalLimit` / `pendingAboveQuoteNotionalLimit` / `pendingBelowQuoteNotionalLimit`（OTO、OTOCO、OPO、OPOCO）。参见 [报价资产名义价值上限 FAQ](/zh-CN/docs/products/spot/faqs/quoteNotionalLimit)。
    * `exchangeInfo` 响应（[REST API](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info)、 [WebSocket API](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info)）通过新字段 `marketQuoteNotionalLimitAllowed` 和 `limitQuoteNotionalLimitAllowed` 显示某个交易对是否支持该参数。
    * 当订单的 `quoteNotionalLimit` 导致剩余数量无法成交或挂单时，将返回新的 `expiryReason` 值 [`INSUFFICIENT_QUOTE_NOTIONAL_LIMIT`](/zh-CN/docs/products/spot/enums#%E8%BF%87%E6%9C%9F%E5%8E%9F%E5%9B%A0)。
    * SOR 端点会解析该参数，但会拒绝并返回 [`-1106`](/zh-CN/docs/products/spot/errors#-1106-%E9%9D%9E%E5%BF%85%E9%9C%80%E5%8F%82%E6%95%B0)。
    * 旧版 OCO 端点（REST API `POST /api/v3/order/oco`、WebSocket API `orderList.place`）不接受这些新参数。
  * 用户数据流 [`executionReport`](/zh-CN/docs/products/spot/user-data-stream#%E8%AE%A2%E5%8D%95%E6%9B%B4%E6%96%B0) 事件、FIX API [`ExecutionReport<8>`](/zh-CN/docs/products/spot/fix-api#executionreport-8) 消息以及 FULL 订单响应的 `preventedMatches[]` 条目现在会包含可选字段 `effectiveSelfTradePreventionMode`（JSON 数据流中为 `eV`，FIX 标签为 `25058`），用于区分撮合引擎实际生效的 STP 模式与下单时指定的 STP 模式。该字段仅出现在 `prevented-match` 报告中，且仅当实际生效的模式与订单自身的 `selfTradePreventionMode` 不同时出现。可能的值：`EXPIRE_MAKER`、`EXPIRE_BOTH`、`DECREMENT`（不会出现 `NONE`、`EXPIRE_TAKER` 或 `TRANSFER`）。



#### 常规更改

  * 修改后数量等于或低于已成交数量的订单，现在会带有 `expiryReason` = [`EXHAUSTED`](/zh-CN/docs/products/spot/enums#%E8%BF%87%E6%9C%9F%E5%8E%9F%E5%9B%A0)。此前，这些订单过期时不带 `expiryReason`。
  * 下单时即成交、随后挂单的 `BUY` 限价单，现在会释放超出剩余数量挂单所需（remaining quantity × limit price）的订单锁定资金。多出的部分（通常是成交带来的价格改善）会在订单挂单的同一次余额更新中退回到 `free`。此前，多出的部分会一直锁定，直到订单结束。
    * 适用于 `LIMIT` `GTC` 订单、已触发的 `STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单、订单列表中的限价单以及 SOR 订单。冰山订单会为其全部剩余数量（包括隐藏部分）保留锁定。



#### 问题修复

  * 撤销订单列表的 SBE 响应现在会将 `listClientOrderId` 编码为原订单列表的 `listClientOrderId`，与 JSON 响应一致。此前，SBE 响应编码的是撤单请求中发送的 `listClientOrderId`。
    * REST API：`DELETE /api/v3/orderList`、`DELETE /api/v3/openOrders`
    * WebSocket API：`orderList.cancel`、`openOrders.cancelAll`



* * *

### 2026-10-30

REST 和 WebSocket API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)，SBE 3：3 模式将于 2026 年 11 月 09 日被停用。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

**最近更新：2026-10-27**

### 2026-10-27

  * 在 [FIX API 文档](/zh-CN/docs/products/spot/fix-api#executionreport-8) 中添加了字段 ExpiryReason(25056) 的说明。该字段已在[此前公告](/zh-CN/docs/products/spot/CHANGELOG#2026-03-09)中公布，但之前未有文档说明。



* * *

### 2026-09-18

REST 和 WebSocket API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)，SBE 3：2 模式将于 2026 年 09 月 25 日被停用。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



FIX API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)，FIX SBE 1：0 模式将于 2026 年 09 月 25 日被停用。
  * [面向生产的 FIX SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_fix_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

### 2026-09-02

#### FIX API

  * 从 [QuickFIX 订单接入 schema](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml) 和 API 文档中的 `ListStatus <N>` 移除了顶层字段 `Symbol (55)`。正如[此前公告](/zh-CN/docs/products/spot/CHANGELOG#2025-12-02)中所述，API 已不再发送该字段。



* * *

### 2026-07-27

  * 更新了 [价格区间执行规则 FAQ](/zh-CN/docs/products/spot/faqs/price_range_execution_rules)，新增了外部参考价格计算方法。



* * *

### 2026-07-17

以下事项将于 **2026年8月4日 大约07:00 UTC** 发生。

  * 以下SBE 市场数据流中的更新速度将从 **25毫秒调整为20毫秒** 。
    * SBE 市场数据流: [增量深度信息](/zh-CN/docs/products/spot/sbe-market-data-streams#diff-depth-streams)
    * FIX SBE: [市场数据增量深度](/zh-CN/docs/products/spot/fix-api#marketdataincrementaldepth)



* * *

### 2026-07-01

**注意：以下变更将于 2026 年 07 月 07 日推出，需要几天才能完成部署。**

#### 新功能

  * Exchange Information 响应中可能出现新的 `symbolStatus` 取值 `CANCEL_ONLY`。
    * REST API: `GET /api/v3/exchangeInfo`
    * WebSocket API: `exchangeInfo`
  * REST 和 WebSocket API SBE schema [spot_3_5.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_5.xml)
    * 当前的 schema 3:4 [spot_3_4.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_4.xml) 已被弃用，将根据我们的 schema 弃用政策在 6 个月后停用。
    * schema 3:5 中的变更：
      * 更新 `symbolStatus` 枚举：新增取值 `CANCEL_ONLY`



* * *

### 2026-06-24

  * 自 **2026-07-09 07:00 UTC** 起，[WebSocket 行情接口](/zh-CN/docs/products/spot/web-socket-streams) 将进行基础设施升级，整个升级过程最长耗时 1 小时。
  * 升级期间，您的 WebSocket 连接可能会断开；如发生此情况，请重新连接。



* * *

### 2026-06-22

REST 和 WebSocket API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)，SBE 3：1 模式将于 2026 年 06 月 29 日被停用。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

### 2026-06-10

#### FIX API

  * 文档更新：从 [FIX API](/zh-CN/docs/products/spot/fix-api#marketdataincrementalrefresh) 中移除了 `LastFragment (893)`。
    * 正如[此前公告](/zh-CN/docs/products/spot/CHANGELOG#2025-12-02)中所述，`MarketDataIncrementalRefresh <X>` 消息已于 2025-12-18 起不再分片，服务器也不再发送 `LastFragment (893)`。
    * 该字段已从 [FIX API](/zh-CN/docs/products/spot/fix-api) 字段列表和对应的 [QuickFIX MD schema](/zh-CN/docs/products/spot/fix/schemas/spot-fix-md.xml) 中移除。
  * 文档更新：更新了 [News `<B>`](/zh-CN/docs/products/spot/fix-api#news-b) 消息的说明，以与 [2026-06-09](/zh-CN/docs/products/spot/CHANGELOG#2026-06-09) 的公告保持一致。



* * *

### 2026-06-09

**更新：**

  * 更新了 [价格区间执行规则 FAQ](/zh-CN/docs/products/spot/faqs/price_range_execution_rules)，新增了外部参考价格计算方法。



当**服务器即将关闭** 时，系统将发送 `serverShutdown` 事件；当您收到此事件时，请断开连接并建立新连接。

文档中所有关于服务器关闭前固定时间的描述均已移除。

  * 在 [SBE 行情接口](/zh-CN/docs/products/spot/sbe-market-data-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 中补充了 `serverShutdown` 事件的说明。
    * ~~系统会在断开连接前 10 分钟发送`serverShutdown` 事件。~~
    * 请尽快建立新连接，以防中断。
    * 请注意，`serverShutdown` 事件将以 JSON 格式通过 WebSocket text 帧发送。



* * *

### 2026-06-03

  * 中文文档术语统一与文字校对：
    * 统一中文术语：`手续费`/`交易费` → `佣金`，`智能指令路由` → `智能订单路由`，`WebSocket 账户信息推送` → `用户数据流`，`订单薄` → `订单簿` 等。
    * 修正了部分文档中的措辞与排版问题。



* * *

### 2026-05-11

**注意：以下变更将于 2026 年 05 月 12 日 07:00 (UTC) 左右发生。**

  * 新增对 [大宗交易](https://www.binance.info/zh-CN/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425) 的 WebSocket 行情接口支持。
    * 新 Stream:
      * `<symbol>@blockTrade`



* * *

### 2026-05-06

**注意：以下变更将于 2026 年 05 月 08 日 06:00 (UTC) 推出，可能需要几个小时才能完成部署。**

  * 在 [WebSocket API](/zh-CN/docs/products/spot/web-socket-api#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 和 [WebSocket 行情接口](/zh-CN/docs/products/spot/web-socket-streams#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%85%B3%E9%97%AD) 中新增了 `serverShutdown` 事件。

    * 系统会在断开连接前 10 分钟发送 `serverShutdown` 事件。
  * 当 [`参考价格`](/zh-CN/docs/products/spot/faqs/price_range_execution_rules) 存在且不为空时， [`PERCENT_PRICE`](/zh-CN/docs/products/spot/filters#percent_price)、[`PERCENT_PRICE_BY_SIDE`](/zh-CN/docs/products/spot/filters#percent_price_by_side)、[`MIN_NOTIONAL`](/zh-CN/docs/products/spot/filters#min_notional-%E6%9C%80%E5%B0%8F%E9%87%91%E9%A2%9D) 和 [`NOTIONAL`](/zh-CN/docs/products/spot/filters#notional-%E5%90%8D%E4%B9%89%E4%BB%B7%E5%80%BC) 过滤器现在将使用`参考价格`。当参考价格不存在或为空时，这些过滤器将改为使用原有行为。

  * [大宗交易](https://www.binance.info/zh-CN/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425) 的市场数据。

    * 新增端点/方法
      * REST API:
        * `GET /api/v3/historicalBlockTrades`
      * WebSocket API:
        * `blockTrades.historical`
  * 订单查询响应中可能会包含 [`expiryReason`](/zh-CN/docs/products/spot/enums#%E8%BF%87%E6%9C%9F%E5%8E%9F%E5%9B%A0) 字段。

    * 该字段仅针对**已过期订单** 返回，用于帮助用户了解订单过期的原因，包括因**价格区间执行规则** 而导致订单过期的情况。
    * 该字段会包含在 JSON 和 SBE 3:4 响应中。
    * 适用于以下端点/方法：
      * REST API:
        * `GET /api/v3/order`
        * `GET /api/v3/allOrders`
        * `GET /api/v3/orderList`
        * `GET /api/v3/allOrderList`
      * WebSocket API:
        * `order.status`
        * `allOrders`
        * `orderList.status`
        * `allOrderLists`
  * REST 和 WebSocket API SBE schema 3:4

    * 当前的 schema 3:3 [spot_3_3.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_3.xml) 已被弃用，将根据我们的 schema 弃用政策在 6 个月后停用。
    * schema 3:4 中的变更：
      * 新增消息 `BlockTradesResponse`
      * 新增类型 `blockTradeId`
      * 在 `OrderResponse` 和 `OrdersResponse` 中新增字段 `expiryReason`



* * *

### 2026-04-28

  * 更正了 `价格区间执行规则 FAQ` 内 [`价格区间执行规则如何工作？`](/zh-CN/docs/products/spot/faqs/price_range_execution_rules)问题中所对应的 JSON 内容。



* * *

### 2026-04-17

以下事项将于 **2026年5月5日 大约10:00 UTC** 发生。

  * 以下SBE 市场数据流中的更新速度将从 **50毫秒调整为25毫秒** 。
    * SBE 市场数据流: [增量深度信息](/zh-CN/docs/products/spot/sbe-market-data-streams#diff-depth-streams)
    * FIX SBE: [市场数据增量深度](/zh-CN/docs/products/spot/fix-api#marketdataincrementaldepth)



* * *

### 2026-04-16

  * 更新了文档，明确说明了如果某个交易对从未设置过参考价格，那么查询参考价格时就会返回错误代码 [`-2043`](/zh-CN/docs/products/spot/errors#-2043-%E6%97%A0%E5%8F%82%E8%80%83%E4%BB%B7%E6%A0%BC)。此规则适用于以下接口/方法：
    * REST API：`GET /api/v3/referencePrice`
    * WebSocket API：`referencePrice`



* * *

### 2026-04-15

  * “WebSocket 账户接口”文档已更名为“用户数据流”，详见：[用户数据流](/zh-CN/docs/products/spot/user-data-stream)。相关词条的引用部分也已同步更新。
  * 对中文版与英文版因翻译或排版导致的部分差异进行了修正。



* * *

### 2026-04-06

  * 补充了有关 [价格区间执行规则](/zh-CN/docs/products/spot/faqs/price_range_execution_rules) 中规则执行的更多信息。



* * *

### 2026-04-02

关于 [2026-03-27](/zh-CN/docs/products/spot/CHANGELOG#2026-03-27) 公告中针对部分端点请求权重计算的说明：

对于被修改的订单，只有当订单因该次修改过期时，请求权重才会变为 0。未导致订单过期的成功请求，仍会按文档中说明的方法消耗权重值。失败的请求，同样会按文档中说明的计算方法消耗权重值。

此规则适用于以下端点和方法：

  * REST API: `PUT /api/v3/order/amend/keepPriority`
  * WebSocket API: `order.amend.keepPriority`



* * *

### 2026-03-30

  * 更新了[价格区间执行规则](/zh-CN/docs/products/spot/faqs/price_range_execution_rules)，以说明订单的执行价格限制。



* * *

### 2026-03-27

以下内容将于**2026年4月2日大约07:00 UTC** 生效。

  * `RAW_REQUESTS` 速率限制提升至每5分钟300,000次。

  * 以下端点和方法的请求权重在请求成功时变为0。请求失败仍会按照文档中规定的方法计算权重。 仅有成功调用这些端点的IP将永远不会受到 `REQUEST_WEIGHT` 速率限制。

    * REST API
      * `POST /api/v3/order`
      * `POST /api/v3/sor/order`
      * `DELETE /api/v3/order`
      * `DELETE /api/v3/openOrders`
      * `POST /api/v3/order/cancelReplace`
      * `POST /api/v3/order/oco`
      * `POST /api/v3/orderList/oco`
      * `POST /api/v3/orderList/oto`
      * `POST /api/v3/orderList/otoco`
      * `POST /api/v3/orderList/opo`
      * `POST /api/v3/orderList/opoco`
      * `DELETE /api/v3/orderList`
      * `PUT /api/v3/order/amend/keepPriority` （请参见 [2026-04-02](/zh-CN/docs/products/spot/CHANGELOG#2026-04-02) 的更新）
    * WebSocket API
      * `order.place`
      * `sor.order.place`
      * `order.cancel`
      * `openOrders.cancelAll`
      * `order.cancelReplace`
      * `orderList.place`
      * `orderList.place.oco`
      * `orderList.place.oto`
      * `orderList.place.otoco`
      * `orderList.place.opo`
      * `orderList.place.opoco`
      * `orderList.cancel`
      * `order.amend.keepPriority` （请参见 [2026-04-02](/zh-CN/docs/products/spot/CHANGELOG#2026-04-02) 的更新）
  * [STP TRANSFER 模式](/zh-CN/docs/products/spot/faqs/stp_faq) 将在 **2026-04-02 07:00 UTC** 生效




* * *

### 2026-03-13

  * 在[价格区间执行规则](/zh-CN/docs/products/spot/faqs/price_range_execution_rules) 中新增了外部参考价格计算方法。



* * *

### 2026-03-11

**通知：** FIX TLS 连接更新将于 **2026-06-08** ，从 **03:00 UTC** 开始，预计耗时约 1 小时完成。

**请注意及时处理：**

  * 在更新期间，现有的 FIX 连接可能会间歇性断开。为确保更新后能够成功重新连接和建立新连接，请在我们更新之前确认您的客户端在 TLS 握手过程中发送了 SNI（服务器名称指示）并且对目标主机名进行了证书验证。
  * 未发送 SNI 的客户端可能会在更新期间或之后收到证书错误的消息，导致 TLS 握手或主机名验证失败。这种情况可能发生在某些未配置 SNI 的 Node.js 客户端上。
  * 请查阅 [FIX API 文档](/zh-CN/docs/products/spot/fix-api#%E4%B8%80%E8%88%AC-api-%E4%BF%A1%E6%81%AF) 以获取完整信息。



* * *

### 2026-03-10

说明了关于[价格区间执行规则](/zh-CN/docs/products/spot/faqs/price_range_execution_rules) 中参考价格的计算方法。

* * *

### 2026-03-09

**注意：** 本部分的变更将逐步推出，预计大约需要三周时间完成。

#### 新功能

  * [价格区间执行规则](/zh-CN/docs/products/spot/faqs/price_range_execution_rules))
    * 新增接口/方法
      * REST API:
        * `GET /api/v3/executionRules`
        * `GET /api/v3/referencePrice`
        * `GET /api/v3/referencePrice/calculation`
      * WebSocket API:
        * `executionRules`
        * `referencePrice`
        * `referencePrice.calculation`
    * 新增 JSON 数据流：`<symbol>@referencePrice`
  * REST 和 WebSocket API SBE schema 3:3
    * 当前的 schema 3:2 [spot_3_2.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_2.xml) 已被废止，将根据我们的 schema 废止政策在6个月内停止使用。
    * schema 3:3 的变更内容：
      * 新消息 `ExecutionRulesResponse`
      * 新消息 `PriceRangeExecutionRule`（嵌入于 `ExecutionRulesResponse` 中）
      * 新消息 `ReferencePriceResponse`
      * 新消息 `ReferencePriceCalculationResponse`
      * 新枚举 `executionRuleType`
      * 新枚举 `expiryReason`
      * 新枚举 `calculationType`
      * 在 `NewOrderResultResponse`、`NewOrderFullResponse`、`NewOrderListResultResponse` 和 `NewOrderListFullResponse` 中新增字段 `expiryReason`
      * 在 `ExecutionReportEvent` 中新增字段 `expiryReason`
      * 新消息 `ServerShutdownEvent`（仅限 WebSocket API）
  * FIX SBE schema 1:1
    * 该 schema 将用于 FIX 订单接入、FIX Drop Copy 和 FIX 市场数据流。
    * 当前的 FIX schema 1:0 [spot-fixsbe-1_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot-fixsbe-1_0.xml) 已被废止，将根据我们的 schema 废止政策在6个月内停用。
    * schema 1:1 的变更内容：
      * 新枚举 `expiryReason`
      * 在 `ExecutionReport` 中新增字段 `ExpiryReason`



#### FIX API

  * 在 ExecutionReport `<T>` 消息中可选新增字段 ExpiryReason `<25056>`。
    * 更新了用于 FIX 市场数据流和 FIX 订单接入的 QuickFIX Schema。



#### WebSocket API

  * 新增 `serverShutdown` 事件。



#### 未来的更新

  * 以下接口已在 **2019-11-13** 废止，将于 **2026-03-25** 停用：
    * `GET /api/v1/ping`
    * `GET /api/v1/time`
    * `POST /api/v1/userDataStream`
    * `PUT /api/v1/userDataStream`
    * `GET /api/v1/ticker/bookTicker`
    * `GET /api/v1/ticker/price`
    * `GET /api/v1/klines`
    * `GET /api/v1/historicalTrades`
    * `GET /api/v1/depth`
    * `GET /api/v1/aggTrades`
    * `GET /api/v1/ticker/24hr`
  * 以下接口将于 **2026-03-25** 停用：
    * `GET /api/v1/userDataStream`
    * `DELETE /api/v1/userDataStream`
    * `GET /api/v1/trades`
  * **以下变更将于 2026-03-26 约 07:00 UTC 生效**
    * 下单及订单列表下单接口的响应将根据 `newOrderRespAck` 的值显示订单过期原因：
      * 如果 `newOrderRespType=ACK`，则不显示过期原因。
      * 如果 `newOrderRespType=RESULT` 或 `newOrderRespType=FULL` 模式，如果出现订单过期，则在字段 `expiryReason` 中显示过期原因。
        * 影响的接口/方法包括：
          * REST API
            * `POST /api/v3/order`
            * `POST /api/v3/sor/order`
            * `POST /api/v3/order/cancelReplace`
            * `POST /api/v3/order/oco`
            * `POST /api/v3/orderList/oco`
            * `POST /api/v3/orderList/oto`
            * `POST /api/v3/orderList/otoco`
            * `POST /api/v3/orderList/opo`
            * `POST /api/v3/orderList/opoco`
          * WebSocket API
            * `order.place`
            * `sor.order.place`
            * `order.cancelReplace`
            * `orderList.place`
            * `orderList.place.oco`
            * `orderList.place.oto`
            * `orderList.place.otoco`
            * `orderList.place.opo`
            * `orderList.place.opoco`
    * 在用户数据流中，`executionReport` 事件新增可选字段 `eR`，如果出现订单过期，则用于显示订单过期原因。



* * *

### 2026-02-24

  * 所有交易对的 [ICEBERG_PARTS](/zh-CN/docs/products/spot/filters#iceberg_parts-%E5%86%B0%E5%B1%B1%E8%AE%A2%E5%8D%95%E6%8B%86%E5%88%86%E6%95%B0) 将于 **2026-03-12 07:00 UTC** 提升至 100。
  * 根据[2025-12-02](/zh-CN/docs/products/spot/CHANGELOG#2025-12-02)的公告，`!ticker@arr` 将于 **2026-03-24 07:00 UTC** 停用。



* * *

### 2026-02-12

REST 和 WebSocket API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)， SBE 3：0 模式将于 2026 年 02 月 19 日被停用。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

### 2026-02-09

  * 在 [FIX SBE 文档](/zh-CN/docs/products/spot/fix-api#fix-sbe) 中阐明了有关指数字段的要求



* * *

### 2026-02-02

  * 记录了 [FIX Drop Copy 会话](/zh-CN/docs/products/spot/fix-api#fix-api-drop-copy-%E4%BC%9A%E8%AF%9D) 数据存在 1 秒的延迟。自 FIX API 推出以来，该延迟一直存在。



* * *

### 2026-01-29

  * [模拟交易](/zh-CN/docs/products/spot/demo-mode/general-info) 现已开放。
  * 有关现货模拟交易环境因维护而不可用的时间信息，请参阅 [模拟交易更新日志](/zh-CN/docs/products/spot/demo-mode/CHANGELOG)。



* * *

### 2026-01-27

**通知：以下变更将于 2026-02-11 07:00 UTC 生效** ：

  * 所有交易对的 [ICEBERG_PARTS](/zh-CN/docs/products/spot/filters#iceberg_parts-%E5%86%B0%E5%B1%B1%E8%AE%A2%E5%8D%95%E6%8B%86%E5%88%86%E6%95%B0) 将增加到 50。



* * *

### 2026-01-26

  * 在 `userDataStream.subscribe.signature` 中添加了字段 `recvWindow`的说明。



* * *

### 2026-01-21

根据 **2025-10-24** 的公告，以下端点和方法将从 **2026-02-20 07:00 UTC** 起不再可用。

## REST API

  * `POST /api/v3/userDataStream`
  * `PUT /api/v3/userDataStream`
  * `DELETE /api/v3/userDataStream`



## WebSocket API

  * `userDataStream.start`
  * `userDataStream.ping`
  * `userDataStream.stop`



* * *

### 2025-12-18

  * [FIX SBE 文档](/zh-CN/docs/products/spot/fix-api#fix-sbe) 已更新。
  * 澄清了用户数据流文档中关于 [`eventStreamTerminated`](/zh-CN/docs/products/spot/user-data-stream#%E4%BA%8B%E4%BB%B6%E6%B5%81%E5%B7%B2%E7%BB%88%E6%AD%A2) 的说明
  * 资产 `这是测试币` 和 `456` 以及交易对 `这是测试币456` 已被添加到 [现货测试网](http://testnet.binance.vision) 以供用户测试含有 Unicode 交易对的端点/方法。 预知详情，请参考 [现货测试网的相关更新日志](/zh-CN/docs/products/spot/testnet/general-info)。



* * *

### 2025-12-17

#### 时效性通知

  * **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** 调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/zh-CN/docs/products/spot/errors#-1022-%E7%AD%BE%E5%90%8D%E4%B8%8D%E6%AD%A3%E7%A1%AE)。请检查并相应地更新您代码中的签名逻辑部分。这项功能现已在 [SPOT Testnet](http://testnet.binance.vision) 上启用。



#### REST API

  * 更新了 REST API 文档中有关于 [签名请求示例](/zh-CN/docs/products/spot/rest-api#hmac-keys) 的部分。



#### WebSocket API

  * 更新了 WebSocket API 文档中有关于 [签名请求示例](/zh-CN/docs/products/spot/web-socket-api#signed-%E8%AF%B7%E6%B1%82%E7%A4%BA%E4%BE%8B-hmac) 的部分。



* * *

### 2025-12-15

**关于 UTF-8 编码的说明：**

  * 在 [FIX API](/zh-CN/docs/products/spot/fix-api)、[REST API](/zh-CN/docs/products/spot/rest-api) 和 [WebSocket API](/zh-CN/docs/products/spot/web-socket-api) 中，如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 在 REST 和 WebSocket API 中，即使请求本身不包含非 ASCII 字符，某些端点/方法也可能返回包含以 UTF-8 编码的非 ASCII 字符的资产和/或交易对名称。
  * 在 [WebSocket 行情接口](/zh-CN/docs/products/spot/web-socket-streams) 中，如果您的请求包含非 ASCII 字符的交易对名称，那么数据流事件中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 在 WebSocket 行情接口中，[全市场所有 Symbol 的精简 Ticker](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker) 和 [全市场滚动窗口统计](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-market-rolling-window-ticker) 事件可能包含以 UTF-8 编码的非 ASCII 字符。
  * 在 [SBE 市场数据流](/zh-CN/docs/products/spot/sbe-market-data-streams) 中，如果您的请求包含包含非 ASCII 字符的交易对名称，那么数据流事件中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 如果您持有或交易任何名称包含非 ASCII 字符的资产或交易对，那么 [用户数据流](/zh-CN/docs/products/spot/user-data-stream) 中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 为了与币安 API 完全兼容，请务必确保您的代码能够处理 UTF-8 编码的字符串。



* * *

### 2025-12-09

  * [FIX SBE Schema](/zh-CN/docs/products/spot/sbe/schemas/spot-fixsbe-1_0.xml) 已更新，会在 `MarketDataSnapshot` 中使用 `smallGroupSize16Encoding`。并在增量单个交易对订单簿数据流/深度数据流的 `MDEntrySize` 的字段中使用 `presence="optional"`。
  * 更新了关于 [FIX 与 FIX SBE](/zh-CN/docs/products/spot/fix-api#fix-%E4%B8%8E-fix-sbe-%E6%A8%A1%E5%BC%8F%E5%AF%B9%E6%AF%94) 的文档说明
  * 在 REST 和 WebSocket API 文档中新增说明：**请避免在请求中使用 SQL 关键字** ，因为这可能会触发 Web 应用防火墙（WAF）规则导致安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232> 。



* * *

### 2025-12-02

**注意： 本节中的变更将逐步推出，预计大约需要两周时间完成。**

#### 常规更改

  * 参数 `symbol` 和 `symbols` 现在支持以 UTF-8 编码的 Unicode 值。
  * 根据 [2025-11-14](/zh-CN/docs/products/spot/CHANGELOG#2025-11-14) 的公告，所有与 `!ticker@arr` 相关的内容已经在文档被移除。
    * 该功能将在未来弃用公告发布前继续可用。
    * 请改用 `<symbol>@ticker` 或 `!miniTicker@arr`。



#### FIX API

  * 现在 FIX 消息中可以接受以 UTF-8 编码的 Unicode 值。仅允许以下标签使用：
    * `Currency (15)`
    * `MiscFeeCurr (138)`
    * `Symbol (55)`
    * `SecondarySymbol (25019)`
    * `CounterSymbol (25028)`
    * `SecurityDesc (107)`
  * 当 Unicode 出现在非上述标签的值中时，FIX API 会在拒绝消息 `<3>` 中返回 `RefTagID (371)` 标签，指明具体哪个标签不允许包含 Unicode。
  * NewOrderList `<E>` 可以接受没有 `TriggerPrice (1102)` 的 `TriggerPriceDirection (1109)`。



#### WebSocket 数据流

  * WebSocket 市场数据流支持 URL 编码的 URL。 



**注意：以下变更预计于 2025-12-18 07:00 UTC 左右生效** ：

  * [ICEBERG_PARTS](/zh-CN/docs/products/spot/filters#iceberg_parts-%E5%86%B0%E5%B1%B1%E8%AE%A2%E5%8D%95%E6%8B%86%E5%88%86%E6%95%B0) 将对所有交易对提升至 25。
  * [FIX SBE 支持](/zh-CN/docs/products/spot/fix-api) 将上线。
  * [一个订单支付另一个订单（OPO）](/zh-CN/docs/products/spot/faqs/opo) 将在所有交易对上线。
    * `opoAllowed` 将开始出现在 `Exchange Information` 请求中，指示每个交易对是否支持一个订单支付另一个订单（OPO）。
      * REST API: `GET /api/v3/exchangeInfo`
      * WebSocket API: `exchangeInfo`
    * OPO 新请求：
      * REST API：
        * `POST /api/v3/orderList/opo`
        * `POST /api/v3/orderList/opoco`
      * WebSocket API：
        * `orderList.place.opo`
        * `orderList.place.opoco`
      * FIX API：
        * NewOrderList `<E>` 新增字段 `OPO (25046)`。请更新至最新 QuickFIX 模式以支持 OPO。
  * 新增 STP 模式 [`TRANSFER`](/zh-CN/docs/products/spot/faqs/stp_faq)。STP `TRANSFER` 启用的具体日期尚未确定。
  * **SBE：新增 schema 3:2 版本 ([spot_3_2.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_2.xml))。**
    * 当前 schema 3:1 ([spot_3_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_1.xml)) 已被弃用，将根据我们的 schema 弃用政策在 6 个月后停用。
    * 3:2 版本变更：
      * 为 `selfTradePreventionMode` 和 `allowedSelfTradePreventionModes` 新增枚举值 `TRANSFER`。
      * 所有低于 3:1 的 schema 无法返回包含 STP 模式 `TRANSFER` 的响应（例如 Exchange Information、下单、撤单或订单状态查询）。当响应无法用请求的 schema 表示时，将返回错误。
  * FIX API 变更：
    * `LastFragment (893)` 被弃用。
      * 这意味着 MarketIncrementalRefresh `<X>` 消息将不再分片，可能包含超过 10,000 条目。
      * 文档已更新以反映此变更。
    * ListStatus `<N>` 将不再发送可选的 `symbol` 字段。
      * 适用于 FIX 订单接入和 FIX Drop Copy。
      * 文档已更新以反映此变更。



* * *

### 2025-11-14

  * 全市场所有交易对的完整Ticker（`!ticker@arr`）已被弃用；这意味着该接口将在后续从文档和系统中移除，具体时间另行通知。
  * 请改用 [`<symbol>@ticker`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~#ticker) 或 [`!miniTicker@arr`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-streams/~#all-mini-ticker)。



* * *

### 2025-11-12

  * 关于[如何正确管理本地订单簿](/zh-CN/docs/products/spot/web-socket-streams#%E5%A6%82%E4%BD%95%E6%AD%A3%E7%A1%AE%E5%9C%A8%E6%9C%AC%E5%9C%B0%E7%BB%B4%E6%8A%A4%E4%B8%80%E4%B8%AAorder-book%E5%89%AF%E6%9C%AC)的步骤已被修正。



* * *

### 2025-11-11

#### SBE 市场数据流

  * **从 2025 年 11 月 26 日 07:00 UTC 起，`<symbol>@depth` 和 `<symbol>@depth20` 数据流的更新速度将变为 50 毫秒**。
    * 此变更将自动部署到 SBE 市场数据的所有用户端，因此客户无需进行任何操作。
    * 每秒可接收的总数据量将增加（最高可达 2 倍速）。
    * [SPOT 测试网](https://testnet.binance.vision/) 将会从 **2025 年 11 月 11 日 07:00 UTC** 起应用这些变更。
    * [SBE 市场数据流](/zh-CN/docs/products/spot/sbe-market-data-streams) 已更新以反映这些变更。



* * *

### 2025-11-10

  * 除了更新日志之外，所有文档中的“最近更新”日期将被移除。
  * 今后，更新日志将作为所有文档变更时间的唯一参考来源。



* * *

### 2025-10-28

**注意：以下变更将于 2025 年 10 月 28 日 04:00 (UTC) 推出，可能需要几个小时才能完成部署。**

  * 可选参数 `symbolStatus` 已添加到以下端点：
    * **REST API**
      * `GET /api/v3/depth`
      * `GET /api/v3/ticker/price`
      * `GET /api/v3/ticker/bookTicker`
      * `GET /api/v3/ticker/24hr`
      * `GET /api/v3/ticker/tradingDay`
      * `GET /api/v3/ticker`
    * **WebSocket API**
      * `depth`
      * `ticker.price`
      * `ticker.book`
      * `ticker.24hr`
      * `ticker.tradingDay`
      * `ticker`
  * 当提供参数 `symbolStatus=<STATUS>` 时，只有交易状态与指定的 `STATUS` 相匹配的交易对才会包含在响应中：
    * 如果使用 `symbol=<SYMBOL>` 参数指定单个交易对，但是这个交易对的状态与指定的 `STATUS` 不匹配时，端点将返回错误代码 [`-1220 SYMBOL_DOES_NOT_MATCH_STATUS`](/zh-CN/docs/products/spot/errors#-1020-%E4%B8%8D%E6%94%AF%E6%8C%81%E7%9A%84%E6%93%8D%E4%BD%9C)。
    * 如果使用 `symbols=[...]` 参数指定了多个交易对，那么响应将是一个数组。该数组中将不会包括交易状态与 `STATUS` 不匹配的交易对。当 symbols 参数中所指定的交易对中没有任何一个交易对的状态与 `STATUS` 相匹配时，响应将为一个空数组。
    * 对于 `symbol` 和 `symbols` 参数为可选参数的端点，省略这些参数将被视为在 `symbols=[...]` 参数中指定了所有交易对。有关 `symbolStatus=<STATUS>` 的行为，请参阅上一行。



* * *

### 2025-10-24

#### SBE

  * SBE：schema 3:1（[spot_3_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_1.xml)）已更新，支持保证金交易的[listenToken 订阅方法](/zh-CN/docs/products/margin-trading/listen-token-data-stream)。



#### REST 和 WebSocket API

根据 [2025-04-07](/zh-CN/docs/products/spot/CHANGELOG#2025-04-07) 的公告，所有关于在 `wss://stream.binance.com` 上使用 `listenKey` 的文档已被移除。请参阅以下请求和方法列表以获取详细信息。该功能将在未来发布停用公告之前继续可用。

**特此提醒您： 您应该通过订阅[在 WebSocket API 内的用户数据流](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream) 来获得用户账户更新。这样可以提供更好的性能（更低的延迟）。**

请参阅下方请求和方法列表来了解更多详情。

这些功能将持续可用，直至另行发布停用公告。

  * REST API

    * `POST /api/v3/userDataStream`
    * `PUT /api/v3/userDataStream`
    * `DELETE /api/v3/userDataStream`
  * WebSocket API

    * `userDataStream.start`
    * `userDataStream.ping`
    * `userDataStream.stop`



* * *

### 2025-10-21

REST 和 WebSocket API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)， SBE 2:1 模式将于 2025 年 10 月 24 日被禁用。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

### 2025-10-08

  * 更新了用于 FIX 市场数据的 [QuickFIX Schema](/zh-CN/docs/products/spot/fix/schemas/spot-fix-md.xml)：
    * 更新了 `RecvWindow(25000)`，以便对在 [2025-08-12](/zh-CN/docs/products/spot/CHANGELOG#2025-08-12) 公布的微秒级进行支持。
    * 更新了 [`InstrumentList`](/zh-CN/docs/products/spot/fix-api#instrumentlist-y) 消息：
      * 新增字段：`StartPriceRange`、`EndPriceRange`。
      * 以下字段改为可选：`MinTradeVol`、`MaxTradeVol`、`MinQtyIncrement`、`MarketMinTradeVol`、`MarketMaxTradeVol`、`MarketMinQtyIncrement`、`MinPriceIncrement`。
    * **InstrumentList`<y>` 的变更属于破坏性变更，预计将于 2025-10-23 07:00 UTC 左右发布。请在此之前更新到新的模式。**
    * 在[SPOT 测试网](https://testnet.binance.vision/) 上已经启用了这个重大更改。



* * *

### 2025-09-29

**注意：以下变更将于 2025 年 9 月 29 日 10:00 (UTC) 推出，可能需要几个小时才能完成部署。**

  * 新增一个端点，用于检索与指定交易品种的账户相关的过滤器列表。这是唯一一个目前会显示账户是否应用了 `MAX_ASSET` 过滤器的端点。
    * REST API： [`GET /api/v3/myFilters`](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/account#my-filters)
    * WebSocket API： [`myFilters`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/account#my-filters)
  * 对 **SBE: schema 3:1 ([spot_3_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_1.xml))** 中的部分注释进行了添加、修改和删除。虽然 `3:1` 用户无需更新到此版本的模式，但我们建议您进行更新以保持一致性。
  * 新增了有关过滤器 [`MAX_ASSET`](/zh-CN/docs/products/spot/filters#max_asset) 的文档。



* * *

### 2025-09-18

  * 更新了文档中有关 `recvWindow` 的部分， 用以体现在 [2025-08-12](/zh-CN/docs/products/spot/CHANGELOG#2025-08-12) 发表的微秒级支持。
    * REST API: [时间同步安全](/zh-CN/docs/products/spot/rest-api#%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5%E5%AE%89%E5%85%A8)
    * WebSocket API: [时间同步安全](/zh-CN/docs/products/spot/web-socket-api#%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5%E5%AE%89%E5%85%A8)



* * *

### 2025-09-12

  * 更新了 FIX 订单接入 API 的 [QuickFix 模式](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml)，用以支持挂钩订单。
  * 在 FIX API 文档中， 对以下部分的 `RecvWindow` 进行了更新：
    * [消息组件](/zh-CN/docs/products/spot/fix-api#header)
    * [时间同步安全](/zh-CN/docs/products/spot/fix-api#%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5%E5%AE%89%E5%85%A8)



* * *

### 2025-08-28

  * 更新了 “简单二进制编码（SBE）常见问题” 文档中 [关于对旧版本的支持](/zh-CN/docs/products/spot/faqs/sbe_faq#%E5%85%B3%E4%BA%8E%E5%AF%B9%E6%97%A7%E7%89%88%E6%9C%AC%E7%9A%84%E6%94%AF%E6%8C%81) 部分，增加了关于模式兼容性的更多细节，并解释了 `NonRepresentable` 和 `NonRepresentableMessage` 的用法。



* * *

### 2025-08-26

  * 更新了 [REST API](/zh-CN/docs/products/spot/rest-api#%E8%AF%B7%E6%B1%82%E9%89%B4%E6%9D%83%E7%B1%BB%E5%9E%8B) 和 [WebSocket API](/zh-CN/docs/products/spot/web-socket-api#%E8%AF%B7%E6%B1%82%E9%89%B4%E6%9D%83%E7%B1%BB%E5%9E%8B) 文档的 “请求鉴权类型” 部分，不过相关的功能没有改动。



* * *

### 2025-08-25

  * **SBE: 模式 3:1 ([spot_3_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_1.xml))**将于** 2025-08-25 05:00 UTC** 进行更新。
    * 以下字段已被重命名，用于解决通过 [SbeTool](/zh-CN/docs/products/spot/faqs/sbe_faq#%E7%94%9F%E6%88%90%E8%A7%A3%E7%A0%81%E5%99%A8) 代码生成器所生成的 Java 代码被发现无法进行编译的问题。
      * 虽然只有受此问题影响的用户才需要更新模式文档，但我们建议所有用户都升级到最新版本以保持一致性。
      * 消息 `MaxAssetFilter`
        * 字段 `limitExponent` 重命名为 `qtyExponent`
        * 字段 `limit` 重命名为 `maxQty`



* * *

### 2025-08-19

  * `userDataStream.subscribe` 在响应中返回 `subscriptionId`。 这在 [previous](/zh-CN/docs/products/spot/CHANGELOG#2025-08-12) 变更日志条目中被遗漏了



* * *

### 2025-08-12

**通知:** 本节中的更改将逐步推出,需要大约两周时间才能完成部署。

#### 常规更改

  * 新的错误代码 `-1120` 和 `1211`。有关详情，请参阅 [错误代码汇总](/zh-CN/docs/products/spot/errors)。
  * 以下请求包含一个名为 `specialCommission` 的新结构。请参阅 [佣金率](/zh-CN/docs/products/spot/faqs/commission_faq)。
    * REST API
      * `GET /api/v3/account/commission`
      * `POST /api/v3/order/test` 并设置 `computeCommissionRates=true`
      * `POST /api/v3/sor/order/test` 并设置 `computeCommissionRates=true`
    * WebSocket API
      * `account.commission`
      * `order.test` 并设置 `computeCommissionRates=true`
      * `sor.order.test` 并设置 `computeCommissionRates=true`
  * **SBE: 新模式 3:1 ([spot_3_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_1.xml)) 将可以使用。**
    * 现行模式 3:0 ([spot_3_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_0.xml)) 将会被废止并根据我们的废止政策，在6个月内停止使用。
    * 模式 3:1 中的更改：
      * `ExchangeInfoResponse`：增加新字段 `pegInstructionsAllowed`
      * `ExecutionReportEvent`：增加新字段 `pricePeg`，`pricePegOffsetLevel` 和 `peggedPrice`
      * `UserDataStreamSubscribeResponse`：新字段 `subscriptionId`
      * 所有的用户数据流事件都增加了新字段 `subscriptionId`。
      * 对于 `WebSocketSessionLogonResponse`，`WebSocketSessionStatusResponse` 和 `WebSocketSessionLogoutResponse`，字段 `apiKey` 被改名为 `loggedOnApiKey`
      * `OrderTestWithCommissionsResponse`：增加2个新字段 `specialCommissionForOrderMaker` 和 `specialCommissionForOrderTaker`
      * `AccountCommissionResponse`：增加4个新字段 `specialCommissionMaker`，`specialCommissionTaker`，`specialCommissionBuyer` 和 `specialCommissionSeller`
      * 支持 `EXCHANGE_MAX_NUM_ORDER_LISTS`，`MAX_NUM_ORDER_LISTS` 和 `MAX_NUM_ORDER_AMENDS` 过滤器。
      * `ExecutionReportEvent`：字段 `rejectReason` 和 `origClientOrderId` 在 SBE 格式也会显示它们的默认值，以和 JSON 格式保持一致，
      * `NonRepresentableMessage`：添加了一条新消息，用于表示无法使用现有 `schema ID` 和 `version` 来显示的信息。收到此消息则表示应该有可用内容，但不适用于当前使用的 SBE 模式。
  * 最终状态为 `EXPIRED_IN_MATCH`（即因 STP 而过期的订单）且累计数量为 0 的订单将在 90 天后做归档处理。
  * 查询订单列表请求将首先查询缓存中的数据，如果找不到，再去查询数据库。
    * REST API：`GET /api/v3/openOrderLists`
    * WebSocket API：`openOrderLists.status`



#### WebSocket API

  * 单个 WebSocket 连接可以同时订阅多个用户数据流。
    * 单个连接上，每个帐户只能有一个订阅。
  * 新增了 `userDataStream.subscribe.signature` 方法，允许您无需事先登录即可订阅用户数据流。
    * 此方法也不需要 Ed25519 API 密钥，并且可以与任何 [API Key 类型](/zh-CN/docs/products/spot/faqs/api_key_types) 配合使用。
    * 为了获得 [SBE 支持](/zh-CN/docs/products/spot/faqs/sbe_faq)，您至少需要使用架构 3:1。
  * 新增了 `session.subscriptions` 方法，用于列出当前会话中所有有效的订阅。
  * 会话请求中字段 `userDataStream` 的含义略有变化。
    * 之前，如果您订阅了已登录帐户的用户数据流，则此方法返回 `true`。
    * 现在，如果您至少有一个有效的用户数据流订阅，它将返回 `true`，否则为 `false`。
  * `userDataStream.unsubscribe` 支持关闭多个订阅。
    * 调用时不带参数，将关闭所有订阅。
    * 调用时传入 `subscriptionId`，如果该 ID 存在的话，将尝试关闭与该 ID 匹配的订阅。
    * 此请求的授权已更改为 `NONE`。
  * 通过 [WebSocket API](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) 进行监听时，用户数据流事件负载中新增了字段 `subscriptionId`。这个字段会标识事件来自哪个订阅。



#### FIX API

  * 当客户端发送拒绝消息时，FIX API 将不再向客户端返回 `<3>` 拒绝消息。
  * 现在，当标签无效、缺少值、字段值为空或格式错误时，错误消息将更加清晰明了。
    * Code
          
          { "code": -1169, "msg": "Invalid tag number." }

    * Code
          
          { "code": -1177, "msg": "Tag specified without a value." }

    * Code
          
          { "code": -1102, "msg": "Field value was empty or malformed." }




#### 将会发生的更改

以下变更将于**2025-08-27 07:00 UTC 开始发生** ：

  * 交易所信息请求将发送字段 `pegInstructionsAllowed`。
  * 已修复的问题：撮合引擎不会再接受数量超出订单数量过滤器上限的订单列表。受到影响的过滤器包括：
    * `MAX_NUM_ORDERS`
    * `MAX_ALGO_ORDERS`
    * `MAX_ICEBERG_ORDERS`
    * `EXCHANGE_MAX_NUM_ORDERS`
    * `EXCHANGE_MAX_ALGO_ORDERS`
    * `EXCHANGE_MAX_ICEBERG_ORDERS`



以下变更将于**2025-08-28 07:00 UTC 开始发生** ：

  * [挂钩订单](/zh-CN/docs/products/spot/faqs/pegged_orders) 功能将可以使用。
    * `pegInstructionsAllowed` 将在所有的交易对上被设为 `true`, 在所有的 API 上正式启用挂钩订单相关功能。
    * 如果订单是挂钩订单，那么以下条件字段 `pegPriceType`， `pegOffSetType`， `pegOffsetValues` 和 `peggedPrice` 将出现在以下请求的响应中：
      * REST API
        * `GET /api/v3/order`
        * `GET /api/v3/orderList`
        * `GET /api/v3/openOrderList`
        * `GET /api/v3/allOrders`
        * `DELETE /api/v3/order`
        * `DELETE /api/v3/orderList`
        * `DELETE /api/v3/openOrders`
        * `PUT /api/v3/order/amend/keepPriority`
      * WebSocket API
        * `order.status`
        * `orderList.status`
        * `allOrders`
        * `order.cancel`
        * `orderList.cancel`
        * `openOrders.cancelAll`
        * `order.amend.keepPriority`
    * FIX API
      * `OrdType(40)` 支持新的数值 `P(PEGGED)`
      * 字段 `PegOffsetValue(211)`，`PegPriceType(1094)`，`PegMoveType(835)` 和 `PegOffsetType(836)` 被添加到以下消息中：
        * NewOrderSingle `<D>`
        * NewOrderList `<E>`
        * OrderCancelRequestAndNewOrderSingle `<XCN>`
      * 下单时，`ExecutionReport` `<8>` 消息将回显 PegInstructions，并带有一个额外的可选字段 `PeggedPrice (839)`
    * 添加了新的挂钩订单错误消息。欲知详情，请参阅 [错误代码汇总](/zh-CN/docs/products/spot/errors) 文档。
  * `recvWindow` 上的变更将被启用。
    * 当您的消息离开我方的消息代理后，在即将发送到撮合引擎之前，将进行第三次检查。
      * 这不包括撮合引擎本身内部的潜在延迟。
    * `recvWindow` 支持微秒级。
      * 该值仍然以毫秒为单位指定，但现在可以采用小数部分来指定更高的精度。
      * 这意味着该参数现在支持**最大精度为 3 位小数** 。（例如， 6000.346）
      * 受影响的 API：
        * FIX API
        * REST API
        * WebSocket API
  * 新的 [`MAX_NUM_ORDER_LISTS`](/zh-CN/docs/products/spot/filters#max_num_order_lists) 过滤器将被启用：会允许每个交易对上最多有 20 个订单列表挂单。
  * 新的 [`MAX_NUM_ORDER_AMENDS`](/zh-CN/docs/products/spot/filters#max_num_order_amends-%E8%BF%87%E6%BB%A4%E5%99%A8) 过滤器将被启用：会以 10 次为上限来限制订单修改次数。



* * *

### 2025-08-07

  * 更新了 FIX API 文档
    * [FIX 市场数据限制](/zh-CN/docs/products/spot/fix-api#%E6%9C%AA%E6%88%90%E4%BA%A4%E8%AE%A2%E5%8D%95%E8%AE%A1%E6%95%B0)：订阅限制一直存在，但之前未有文档说明。
    * [消息处理顺序](/zh-CN/docs/products/spot/fix-api#%E5%85%B3%E4%BA%8E%E6%B6%88%E6%81%AF%E5%A4%84%E7%90%86%E9%A1%BA%E5%BA%8F)：重新措辞并调整了格式。



* * *

### 2025-07-03

  * 自 **2025-07-08 07:00 UTC** 起，[WebSocket 行情接口](/zh-CN/docs/products/spot/web-socket-streams) 将会进行升级。
  * 升级期间，**现有连接和新连接可能会在 24 小时内断开** 。
  * 升级过程最多可能需要 2 小时。若有不便之处，敬请谅解。



* * *

### 2025-06-04

REST 和 WebSocket API：

  * 注意：根据我们的 SBE 政策，[在被废止 6 个月后](/zh-CN/docs/products/spot/faqs/sbe_faq#sbe-schema)， SBE 2：0 模式将于 2025 年 06 月 12 日被禁用。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

### 2025-05-28

  * 在 “API 基本信息” 下，记录每个 API 的超时值和错误：
    * [FIX](/zh-CN/docs/products/spot/fix-api#%E4%B8%80%E8%88%AC-api-%E4%BF%A1%E6%81%AF)
    * [REST](/zh-CN/docs/products/spot/rest-api#%E6%8E%A5%E5%8F%A3%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)
    * [WebSocket](/zh-CN/docs/products/spot/web-socket-api#websocket-api-%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF)



* * *

### 2025-05-22

**注意：以下变更将于 2025 年 6 月 6 日 7:00 (UTC) 生效。**

  * 将通过一项额外的检查，对 FIX、REST 和 WebSocket API 上先前关于`recvWindow` 的行为进行强化。
    * 让我们回顾一下现有行为：
      * 如果在接收请求时， `timestamp` 大于 `serverTime` \+ 1 秒，则请求会被拒绝。此检查被拒绝的话，将会增加消息限制（FIX API）和 IP 限制（REST 和 WebSocket API），但不会增加未成交订单计数（所有 API 的下单端点）。
      * 如果在接收请求时， `timestamp` 和 `serverTime` 之间的差值大于 `recvWindow`，则请求被拒绝。此检查被拒绝的话，将会增加消息限制（FIX API）和 IP 限制（REST 和 WebSocket API），但不会增加未成交订单计数（所有 API 的下单端点）。
    * 附加检查：
      * 在请求转发到撮合引擎之前，如果 `timestamp` 与当前 `serverTime` 之间的差值大于 `recvWindow`，则拒绝该请求。此检查被拒绝的话，将会增加消息限制（FIX API）、IP 限制（REST 和 WebSocket API）以及未成交订单计数（所有 API 的下单端点）。
    * 已更新 Timing 安全性文档，以反映新增的附加检查。
      * [REST API](/zh-CN/docs/products/spot/rest-api#%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5%E5%AE%89%E5%85%A8)
      * [WebSocket API](/zh-CN/docs/products/spot/web-socket-api#%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5%E5%AE%89%E5%85%A8)
      * [FIX API](/zh-CN/docs/products/spot/fix-api#%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5%E5%AE%89%E5%85%A8)
  * 修复了 FIX Market Data 消息 InstrumentList `<y>` 中的一个错误。之前，`NoRelatedSym(146)` 的值可能会不正确。



* * *

### 2025-04-29

  * 目前需要 Ed25519 API 密钥才能使用的功能将很快会对 HMAC 和 RSA 密钥开放。
    * 例如，在 listenKeys 被移除前，您可以使用任何 API 密钥类型在 WebSocket API 中订阅账户数据流。
    * 我们仍然鼓励用户迁移到 Ed25519 API 密钥，因为它们在币安现货交易中更安全、性能更佳。
    * 更多详情即将公布，敬请关注，不要错过。



* * *

### 2025-04-25

  * 以下请求权重将从 1 增加到 4：
    * REST API: `PUT /api/v3/order/amend/keepPriority`
    * WebSocket API: `order.amend.keepPriority`
    * REST 和 WebSocket API 的文档均已更新，以反映即将发生的更改。
  * 澄清了 FIX-API 中的 `SEQNUM` 是一个累计到最大值后将会归 0，然后重新开始计数的 32 位无符号整数。自 FIX-API 诞生以来，它一直是 `SEQNUM` 数据类型。



* * *

### 2025-04-21

**关于[保留优先级的修改订单请求 (Order Amend Keep Priority)](/zh-CN/docs/products/spot/faqs/order_amend_keep_priority) 和 [STP 方式 `DECREMENT`（递减）](/zh-CN/docs/products/spot/faqs/stp_faq) 发布的说明：**

  * 于 **2025-05-07 07:00 UTC**
    * 所有交易对将启用 ”保留优先级的修改订单请求“ 功能。
    * 所有交易对将允许 “STP 递减”。
  * 自**2025年4月24日 07:00 UTC** 起，`amendAllowed` 字段将在交易所信息请求中可见，但该功能尚未启用。
  * [SPOT 测试网](https://testnet.binance.vision/) 在所有交易对上都启用了这两项功能。



* * *

### 2025-04-08

**通知:** 本节中的更改将逐步推出,需要一周时间才能完成.

  * 新的错误代码 `-2039`，如果查询同时具有 `orderId` 和 `origClientOrderId` 的订单，并且未找到具有此组合的订单.
    * 受影响的请求:
      * REST API:`GET /api/v3/order`
      * WebSocket API:`order.status`
  * [错误代码文档](/zh-CN/docs/products/spot/errors) 在错误代码 `-1034` 中更新了新的错误消息, 当超过 FIX 连接速率限制时会出现。(更多细节参看昨天的 [更新](/zh-CN/docs/products/spot/CHANGELOG#2025-04-07))



* * *

### 2025-04-07

#### 常规更改

**通知:** 本节中的更改将逐步推出,需要一周时间才能完成.

  * 在2025 年 1 月 16 日，FIX Market Data 会话的连接限制从 5 个增加到了 100 个。这个改变没有在之前的更改日志中被明示。
  * 新的错误代码 `-2038`，将在保留优先权的修改订单请求失败时出现。
  * 错误代码 `-1034` 有了新消息。
  * 如果未成交订单计数超过了在 `intervalNum:DAY` 里定义的限制, 那么 `intervalNum:SECOND` 下的未成交订单计数将不再递增。
  * 以前，无论提供的参数如何，myTrades 请求的权重都是 20。现在，如果您提供 `orderId` ，请求的权重将为 5。
    * REST API：`GET /api/v3/myTrades`
    * WebSocket API：`myTrades`
  * 查询和删除订单的变化：
    * 现在，当 `orderId` 和 `origClientOrderId` 都不存在时，请求将被拒绝，并显示 `-1102` 而不是 `-1128`。
    * 受影响的请求：
      * REST API：
        * `GET /api/v3/order`
        * `DELETE /api/v3/order`
      * WebSocket API：
        * `order.status`
        * `order.cancel`
      * FIX API：
        * OrderCancelRequest `<F>`



#### FIX API

**通知:** 以下变更将于 2025 年 4 月 21 日期间发生。

  * FIX API 会验证 `EncryptMethod(98)` 在登录 Logon `<A>` 时是否为 0。
  * FIX 订单接入会话的每个账户有 10 个并发 TCP 连接的限制。
  * 现在强制实施连接速率限制.请注意，这些限制是针对账户和 IP 地址独立检查的。
    * FIX 订单接入会话：在 30 秒内 15 次连接尝试的限制
    * FIX Drop Copy 会话：在 30 秒内 15 次连接尝试的限制。
    * FIX Market Data 会话：在 300 秒内 300 次连接尝试的限制。
  * News `<B>` 在 Headline 字段中包括了一个倒计时消息。
    * 在本次更新完成后： 当服务器进入维护状态时，将向客户端**每隔 10 秒发送一条** `News` 消息，并**持续 10 分钟** 。在10分钟过后，客户端将被注销，其会话将被关闭。
  * OrderCancelRequest `<F>` 和 OrderCancelRequestAndNewOrderSingle `<XCN>` 现在允许使用 `orderId` 和 `clientOrderId`。
  * [FIX 订单接入会话的 QuickFix 模式](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml) 已被更新，将支持保留优先级的修改订单请求（Order Amend Keep Priority）和新的 STP 方式 `DECREMENT`。



#### User Data Streams

  * **我们将弃用此功能： 通过使用`listenKey` 来访问 wss://stream.binance.com:9443 以监听账户信息的。**
    * 以后但不是当前，此功将被能从我们的系统中删除。
  * **您应该通过订阅[在 WebSocket API 内的用户数据流](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream) 来获得用户账户更新。**
    * 这个方式会提供稍好的性能 **（较低的延迟）** 。
    * 必须使用 Ed25519 API 密钥
  * 在未来的更新中，将删除有关账户数据流的 WebSocket 基本访问地址的信息。
  * 在未来的更新中，以下请求将被从文档中删除：
    * `POST /api/v3/userDataStream`
    * `PUT /api/v3/userDataStream`
    * `DELETE /api/v3/userDataStream`
    * `userDataStream.start`
    * `userDataStream.ping`
    * `userDataStream.stop`
  * [用户数据流](/zh-CN/docs/products/spot/user-data-stream) 将保留可以接收的有效负载，以供您参考。



#### 将会发生的更改

以下变更将于**2025 年 4 月 24 日 07:00 UTC** 发生：

  * ~~[保留优先级的修改订单请求（Order Amend Keep Priority）](/zh-CN/docs/products/spot/faqs/order_amend_keep_priority) 将可以使用。 (请注意，必须在相应交易对上启用该功能后才能使用。)~~
    * 新字段 `amendAllowed` 会出现在 Exchange Information 响应中。
      * **2025-04-21 更新 ："保留优先级的修改订单请求" 的具体启用日期尚未确定**
      * REST API： `GET /api/v3/exchangeInfo`
      * WebSocket API： `exchangeInfo`
    * FIX API：新的 Order Entry 消息 **OrderAmendKeepPriorityRequest** 和 **OrderAmendReject**
    * REST API：`PUT /api/v3/order/amend/keepPriority`
    * WebSocket API： `order.amend.keepPriority`
  * ~~如果已在交易对上作了相应配置，那么 STP 方式`DECREMENT` （递减） 将在 Exchange Information 中可见。~~
    * **2025-04-21 更新 ："STP 方式 DECREMENT" 的具体启用日期尚未确定。**
    * 通过不仅仅使挂单或吃单过期,或无条件地让两种订单都过期，STP 递减会减少**两种** 订单的可用数量，并将通过阻止匹配的数量来增加**两种** 订单的 `prevented quantity` 值。
    * 这将使可用数量较少的订单过期，因为(`filled quantity` \+ `prevented quantity`)等于 `order quantity`。如果两个订单的可用数量相等，那么两个订单都将过期。这种情况被称为“递减”，因为可用数量减少了。
  * 使用 `orderId` 和 `origClientOrderId/cancelOrigClientOrderId` 来查询和/或取消订单：
    * 以前，当两个参数都提供时，在各个端点的上行为并不一致。
    * 以后，当同时提供两个参数时，系统首先将会使用订单的 `orderId` 来搜索订单。如果订单被找到， `origClientOrderId`/`cancelOrigClientOrderId` 的值将会被用来验证被找到的订单。如果两个检测条件都通过，那么请求成功。如果两个条件都不满足，则请求将被拒绝。
    * 受影响的请求：
      * REST API：
        * `GET /api/v3/order`
        * `DELETE /api/v3/order`
        * `POST /api/v3/order/cancelReplace`
      * WebSocket API：
        * `order.status`
        * `order.cancel`
        * `order.cancelReplace`
      * FIX API：
        * OrderCancelRequest `<F>`
        * OrderCancelRequestAndNewOrderSingle `<XCN>`
  * 使用 `listOrderId` 和 `listClientOrderId` 来取消订单:
    * 以前，当两个参数都提供时，在各个端点的上行为并不一致。
    * 以后，当同时提供两个参数时，系统首先将会使用 `listOrderId` 来搜索订单列表。如果找到相应的订单列表，`listClientOrderId` 将会被用来验证被找到的订单列表。如果两个条件都不满足，请求将被拒绝。
    * 受影响的请求
      * REST API
        * `DELETE /api/v3/orderList`
      * WebSocket API
        * `orderList.cancel`
  * **SBE： 新模式 3:0 ([spot_3_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_3_0.xml)) 将可以使用。**
    * 现行模式 2:1 ([spot_2_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_2_1.xml)) 将会被废止并根据我们的废止政策，在6个月内停止使用。
    * 请注意：在新模式被发布前，尝试使用模式 3:0 将导致错误。
    * 3:0 中的更改：
      * 将会支持保留优先级的修改订单（Order Amend Keep Priority）请求:
        * 在 ExchangeInfoResponse 中添加了 `amendAllowed` 字段。
        * 新消息 `OrderAmendmentsResponse` 和 `OrderAmendKeepPriorityResponse`。
      * 所有的枚举类型都有了新变量：`NON_REPRESENTABLE`。这将用于将来，对新的枚举值进行编码。新模式的枚举类型可能会与 3:0 不兼容。
      * 新增针对 `selfTradePreventionMode` 和 `allowedSelfTradePreventionModes` 的新枚举变量 `DECREMENT`。
      * `symbolStatus` 枚举下的值 `AUCTION_MATCH`， `PRE_TRADING` 以及 `POST_TRADING` 已被删除。
      * 字段 `usedSor`, `orderCapacity`， `workingFloor`，`preventedQuantity` 以及 `matchType` 将不再是可选的参数。
      * 更改了 `ExecutionReportEvent`：现在，字段 `orderCreationTime` 是可选的。
    * 通过 WebSocket API 来使用被废止的 2:1 版本的模式来侦听账户数据流：
      * `ListStatusEvent` 的字段 `listStatusType` 在 `Updated` 时，会呈现为 `ExecStarted`。升级到模式 3:0 来获取正确的值。
      * `ExecutionReportEvent` 的字段 `selfTradePreventionMode` 在 `Decrement` 时，会呈现为 `None`。 这将只在 `executionType` 为 `TradePrevention` 时发生。
      * `ExecutionReportEvent` 的字段 `orderCreationTime` 在没有值时将呈现为 -1。
    * 所有低于 3:0 版本的模式不会支持对保留优先级修改订单请求（Order Amend Keep Priority）的响应，以及任何可能包含 STP 方式 `DECREMENT` 的响应（比如，Exchange Information，下单，取消订单或查询您的订单状态）。当响应无法用被指定的模式来表达时，系统将返回错误。



* * *

### 2025-04-03

关注 SPOT 测试网的最新更新,将 WebSocket API 中的 URL 更新为 [SPOT Testnet] 的最新 URL(<https://testnet.binance.vision/>).

* * *

### 2025-03-31

  * 添加了对取消订单性能的说明.



* * *

### 2025-03-10

  * **注意：以下变更将于 2025 年 3 月 13 日 09:00 UTC 发生。**
    * FIX Drop Copy 会话的限制将会为**每分钟 60 条消息** 。
    * FIX Market Data 会话的限制将会为**每分钟 2000 条消息** 。
    * FIX API 文档已更新，以反映即将发生的更改。
  * **SBE 市场数据流将于 2025 年 3 月 18 日 07:00 UTC 上线。** 这些流会提供较小的有效负载，将为部分对延迟比较敏感的市场数据连接提供更快的响应时间。
    * 以 SBE 格式提供的数据流：
    * 实时：逐笔交易
    * 实时：最优挂单信息
      * 每 100 毫秒：增量深度信息
    * 每 100 毫秒：有限档深度信息
    * 有关更多信息，请参阅 [SBE 市场数据连流](/zh-CN/docs/products/spot/sbe-market-data-streams)。



* * *

### 2025-03-05

  * **注意：以下变更将于 2025 年 3 月 10 日 12:00 UTC 发生。** 以下请求权重将从 2 增加到 4：
    * REST API： `GET /api/v3/aggTrade`
    * WebSocket API： `trades.aggregate`
  * REST 和 WebSocket API 的文档均已更新，以反映即将发生的更改。



* * *

### 2025-02-12

  * **注意：这些更改将于 2025 年 2 月 26 日 05：00 UTC 生效。请确保在此之前您已下载最新的模式。
  * `AggressorSide （2446)` 将在 FIX 市场数据流中提供。QuickFIX 模式 [file](/zh-CN/docs/products/spot/fix/schemas/spot-fix-md.xml) 也已更新。



* * *

### 2024-01-28

**注意: 该变更会在2025年2月3日到2025年2月14日之间逐步推出。**

  * **以下变更将会同时应用于用户数据流，WebSocket 行情接口 和 WebSocket API:**
    * WebSocket 服务将会**每20秒** 发送发送 PING 消息而不是每3分钟。
    * PONG 消息的延迟将会是每1分钟而不是每10分钟。
    * 相关服务的更改所对应的文档都已经更新。



* * *

### 2025-01-09

  * FIX 市场数据将在 **January 16, 05:00 UTC** 提供。FIX API 文档已更新有关此功能。
  * 请参阅此 [链接](/zh-CN/docs/products/spot/fix/schemas/spot-fix-md.xml) 以获取 FIX市场数据的 QuickFIX 模式。



* * *

### 2024-12-17

常规更改：

系统现在在所有相关时间和/或时间戳的字段中支持微秒。微秒支持是 **opt-in** ，默认情况下，请求和响应仍然使用毫秒。文档中的示例也在可预见的将来使用毫秒。

WebSocket Streams

  * 可以在连接 URL 中使用新的可选参数 `timeUnit` 来选择时间单位。
    * 例如：`/stream？streams=btcusdt@trade&timeUnit=millisecond`
    * 支持的值为：
      * `MILLISECOND`
      * `millisecond`
      * `MICROSECOND`
      * `microsecond`
    * 如果未选择时间单位，则默认使用毫秒。



REST API

  * 可以在请求中发送新的可选报文头 `X-MBX-TIME-UNIT` 来选择时间单位。
    * 支持的值：
      * `MILLISECOND`
      * `millisecond`
      * `MICROSECOND`
      * `microsecond`
    * 时间单位会影响 JSON 响应中的时间戳字段（例如，`time`、`transactTime`）。
      * 无论时间单位如何，SBE 响应都将继续以微秒为单位。
    * 如果未选择时间单位，则默认使用毫秒。
  * 时间戳参数（例如 'startTime'、'endTime'、'timestamp）' 现在可以以毫秒或微秒为单位传递。



WebSocket API

  * 可以在连接 URL 中使用新的可选参数 `timeUnit` 来选择时间单位。
    * 支持的值：
      * `MILLISECOND`
      * `millisecond`
      * `MICROSECOND`
      * `microsecond`
    * 时间单位会影响 JSON 响应中的时间戳字段（例如，`time`、`transactTime`）。
      * 无论时间单位如何，SBE 响应都将继续以微秒为单位。
    * 如果未选择时间单位，则默认使用毫秒。
  * 时间戳参数（例如 `startTime`、`endTime`、`timestamp`） 现在可以以毫秒或微秒为单位传递。



User Data Streams

  * 可以在连接 URL 中使用新的可选参数 `timeUnit` 来选择时间单位。
    * 支持的值
      * `MILLISECOND`
      * `MICROSECOND`
      * `microsecond`
      * `millisecond`



* * *

### 2024-12-09

**注意：** 以下的变更会从**2024 年 12 月 12日** 开始推出，可能需要大约一周的时间才能完成。

常规更改：

  * 现在会拒绝距离过去或未来太远的时间戳参数值。
  * 时间戳数值在 2017 年 1 月 1 日之前（小于 1483228800000）
  * 时间戳数值超过当前时间 10 秒以后（例如，如果当前时间为 1729745280000, 那么使用 1729745290000 或更大是错误的）
  * 如果 `startTime` 和/或 `endTime` 的值超出范围，数值会被调整至正确的范围。
  * 已将 `quote order quantity` （`origQuoteOrderQty`） 字段添加到原先没有该字段的响应中。请注意，对于下单相关的接口，该字段将仅针对 `newOrderRespType` 设置为 `RESULT` 或 `FULL` 的请求显示。



请参阅以下列表，以便了解因带有： `origQuoteOrderQty` 而受影响的请求：

服务| 请求  
---|---  
REST| `POST /api/v3/order`  
| `POST /api/v3/sor/order`  
| `POST /api/v3/order/oco`  
| `POST /api/v3/orderList/oco`  
| `POST /api/v3/orderList/oto`  
| `POST /api/v3/orderList/otoco`  
| `DELETE /api/v3/order`  
| `DELETE /api/v3/orderList`  
| `POST /api/v3/order/cancelReplace`  
WebSocket API| `order.place`  
| `sor.order.place`  
| `orderList.place`  
| `orderList.place.oco`  
| `orderList.place.oto`  
| `orderList.place.otoco`  
| `order.cancel`  
| `orderList.cancel`  
| `order.cancelReplace`  
  
SBE

  * 已发布新模式 2:1 [spot_2_1.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_2_1.xml)。 当前模式 2:0 [spot_2_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_2_0.xml) 将被弃用。根据我们的模式弃用政策，当前模式 2:0 会将在 6个月内从 API 中停用。
  * 模式 2：1 是 模式 2：0 的向后兼容更新版本。当您请求模式 2：0 或 2：1 时，您将始终收到 2：1 格式的有效载荷。
  * SBE 模式 2：1 中的更改：
    * 下单/取消订单响应中的新字段 `origQuoteOrderQty` （注意：使用 2：0 模式生成的解码器将忽略此字段）：
      * `NewOrderResultResponse`
      * `NewOrderFullResponse`
      * `CancelOrderResponse`
      * `NewOrderListResultResponse`
      * `NewOrderListFullResponse`
      * `CancelOrderListResponse`
    * 仅限 WebSocket API：会话状态响应中的新字段 `userDataStream`：
      * `WebSocketSessionLogonResponse`
      * `WebSocketSessionStatusResponse`
      * `WebSocketSessionLogoutResponse`
    * 仅限 WebSocket API：在 User Data Stream 中会支持的新消息：
      * `UserDataStreamSubscribeResponse`
      * `UserDataStreamUnsubscribeResponse`
      * `BalanceUpdateEvent`
      * `EventStreamTerminatedEvent`
      * `ExecutionReportEvent`
      * `ExternalLockUpdateEvent`
      * `ListStatusEvent`
      * `OutboundAccountPositionEvent`



WebSocket API

  * 您现在可以通过 WebSocket API 连接订阅账户数据流事件。
    * 请注意：此功能仅适用于使用 Ed25519 API 密钥的用户。
    * 请注意：如果您要订阅使用 SBE 格式的账户数据流，则需使用新的 SBE 模式 2:1。
  * 新请求：
    * `userDataStream.subscribe`
    * `userDataStream.unsubscribe`
  * 对于 `session.logon`、 `session.status` 和 `session.logout` 的更改。
    * 添加了一个新字段 `userDataStream`，用于显示账户数据流订阅是否处于活跃状态。
  * 修复了在 `session.logon` 之后使用 `userDataStream.start` 不会收到新 listenKey 的错误。



User Data Stream

  * 仅限于 WebSocket API：当您从 websocket 会话注销或取消订阅账户数据流时，新事件 `eventStreamTerminated` 将会被发出。
  * 当您的现货钱包余额被外部系统锁定/解锁时，新事件 `externalLockUpdate` 将会被发送。



FIX API

  * [模式](/zh-CN/docs/products/spot/fix/schemas/spot-fix-oe.xml) 中已添加了新的管理消息 News <B>，该消息可用于所有 FIX 服务。收到此消息意味着您的连接即将关闭。



以下更改将在**2024 年 12 月 16 日到 2024 年 12 月 20日之间** 发生：

  * 修复一个错误： `BUY` 方 OCO 单如果不提供 `stopPrice` 就会被阻止下单。
  * 在 OCO 中添加了对 `TAKE_PROFIT` 和 `TAKE_PROFIT_LIMIT` 的支持。
    * 以前，OCO 只能由以下订单类型组成：
      * `LIMIT_MAKER` \+ '`STOP_LOSS`
      * `LIMIT_MAKER` \+ `STOP_LOSS_LIMIT`
    * 现在，OCO 可以由以下订单类型组成：
      * `LIMIT_MAKER` \+ `STOP_LOSS`
      * `LIMIT_MAKER` \+ `STOP_LOSS_LIMIT`
      * `TAKE_PROFIT` \+ `STOP_LOSS`
      * `TAKE_PROFIT` \+ `STOP_LOSS_LIMIT`
      * `TAKE_PROFIT_LIMIT` \+ `STOP_LOSS`
      * `TAKE_PROFIT_LIMIT` \+ `STOP_LOSS_LIMIT`
    * 以下请求支持此功能：
      * `POST /api/v3/orderList/oco`
      * `POST /api/v3/orderList/otoco`
      * `orderList.place.oco`
      * `orderList.place.otoco`
      * `NewOrderList<E>`
    * 错误代码 -1167 将在此次更新后过时，并将在以后的更新中从文档中删除。



* * *

### 2024-10-18

Rest 和 WebSocket API:

  * 注意：根据我们的 SBE 政策，SBE 1：0 模式将于 2024 年 10 月 25 日被禁用 [废止后 6 个月](/zh-CN/docs/products/spot/faqs/sbe_faq)。
  * [面向生产的 SBE 生命周期](/zh-CN/docs/products/spot/sbe/schemas/sbe_schema_lifecycle_prod.json) 已基于本次更改进行了更新。



* * *

### 2024-10-17

Exchange Information 的更改 （即 REST API 的 [`GET /api/v3/exchangeInfo`](/zh-CN/docs/catalog/core-trading-spot-trading/api/rest-api/general#exchange-info) 和 WebSocket API 的 [`exchangeInfo`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/general#exchange-info)）。

  * 新的可选参数 `showPermissionSets` 可用于隐藏 `permissionsSets` 的权限信息;这可用于减小消息大小。
  * 新的可选参数 `symbolStatus` 用于仅显示具有指定状态的交易对。（例如：`TRADING`， `HALT`， `BREAK`）



* * *

### 2024-08-26

  * [现货未成交订单计数规则](/zh-CN/docs/products/spot/faqs/order_count_decrement) 已更新，解释了如何在下订单时减少未成交的订单数量。



* * *

### 2024-08-16

**注意：** 以下的变更正在逐步推出，可能需要大约一周的时间才能完成。

常规更改：

  * 在市场流动性低的情况下，当提交包含 `quoteOrderQty` 的市价单（又名反向市价单）被拒绝时，添加了新的错误消息。



* * *

### 2024-08-01

  * [FIX API 和 Drop Copy 会话](/zh-CN/docs/products/spot/fix-api) 将于 **8 月 8 日 05:00 UTC** 上线。



* * *

### 2024-07-26

  * [FIX API 和 Drop Copy 会话](/zh-CN/docs/products/spot/fix-api) 已添加到文档中。
  * 实时交换的发布日期尚未确定。



* * *

### 2024-07-22

常规更改：

  * 修复了 klines 的时间戳不正确的 bug。
    * REST API： 带有 `timeZone` 参数的 `GET /api/v3/klines` 和 `GET /api/v3/uiKlines`
    * WebSocket API： 带有 `timeZone` 参数的 `klines` 和 `uiKlines`
    * WebSocket Streams: `<symbol>@kline_<interval>@+08：00`



* * *

### 2024-06-11

  * 在 **6月11日 UTC 时间 05:00** ，我们将开始推出新功能 `One-Triggers-the-Other` (OTO) 订单和 `One-Triggers-a-One-Cancels-The-Other` (OTOCO) 订单。（请注意，我们可能需要花几个小时来部署到所有服务器。）
    * 有关详细信息，请参阅以下页面：
      * REST API：
        * `POST /api/v3/orderList/oto`
        * `POST /api/v3/orderList/otoco`
      * WebSocket API：
        * `orderList.place.oto`
        * `orderList.place.otoco`
  * 在 **6月18日 UTC 时间 05:00** ，我们将会把买方的订单 ID（`b`） 和卖方的订单 ID（`a`） 从交易流中删除（i.e. `<symbol>@trade`）。 （请注意，我们可能需要花几个小时来部署到所有服务器。）
    * [WebSocket 行情接口](/zh-CN/docs/products/spot/web-socket-streams) 与其相关的文档已经被更改了。
    * 要监控您的订单是否是交易的一部分，请订阅 [用户数据流](/zh-CN/docs/products/spot/user-data-stream)。



* * *

### 2024-06-06

此功能将在**6月6日 UTC时间11:59** 前上线。

REST API

  * `POST /api/v3/order/cancelReplace` 新加可选参数 `orderRateLimitExceededMode`。



WebSocket API

  * `order.cancelReplace` 新加可选参数 `orderRateLimitExceededMode`。



* * *

### 2024-05-30

WebSocket Streams

  * Kline 新增加了对 UTC+8 时区的支持。（例如，`btcusdt@kline_1d@+08:00`）



* * *

### 2024-04-10

以下更新的生效时间已被推迟到 **4月25日 05：00 UTC**

  * "交易规范信息"响应中的交易对权限信息已从字段 `permissions` 移至字段 `permissionSets`。
  * 字段 `permissions` 将为空，并将在未来版本中删除。
  * 以前，`"permissions":["SPOT","MARGIN"]` 代表如果您的账户具有 `SPOT` 或 `MARGIN` 权限，您就可以在该交易对上下订单。现在，等效项是 `"permissionSets":[["SPOT","MARGIN"]]`（请注意额外的方括号）。`permissionSets`数组中的每个权限数组称为 "permission set"。
  * 交易对的权限现在可以有更多权限类型。例如，`"permissionSets":[["SPOT","MARGIN"],["TRD_GRP_004","TRD_GRP_005"]]` 指示除了支持以上提过的权限集，也接受 `TRD_GRP_004` 或 `TRD_GRP_005`。交易对的 `permissionSets` 中可以有任意排列组合的权限集。



REST API

  * `otoAllowed` 现在将出现在 `GET /api/v3/exchangeInfo` 上，指示该交易品种是否支持 One-Triggers-the-Other (OTO) 订单。



WebSocket API

  * `otoAllowed` 现在将出现在 `exchangeInfo` 上，指示该交易品种是否支持 One-Triggers-the-Other (OTO) 订单。



SBE

  * 已发布新模式 2:0 [Spot_2_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_2_0.xml)。 当前模式 1:0 [spot_1_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_1_0.xml) 将被弃用，并从根据我们模式弃用政策，会将在 6 个月内下线。
  * 在 REST API 或 WebSocket API 上使用模式 1:0 时，消息 `ExchangeInfoResponse` 中的组"权限"将始终为空。在升级到模式 2:0后， 您才可以在 `permissionSets` 组中查找权限信息。
  * 最新模式仍将支持已弃用的 OCO 请求。
  * 请注意，在模式 2:0 实际发布之前尝试使用它会导致错误。



* * *

### 2024-04-02

**注意：** 以下的变更将逐步推出，并预计需要大约一周的时间完成。

  * `GET /api/v3/account` 新加可选参数 `omitZeroBalances`，如果启用，则会隐藏所有零余额。
  * `account.status` 新加可选参数 `omitZeroBalances`，如果启用，则会隐藏所有零余额。
  * **以下请求的权重已从 10 增加到 25 （该规定将于2024年4月4日生效）** ：
    * `GET /api/v3/trades`
    * `GET /api/v3/historicalTrades`
    * `trades.recent`
    * `trades.historical`



User Data Stream

  * 如果 `listenKey` 过期，将在流中发出新事件 `listenKeyExpired`。



REST API

  * REST API 上现已弃用 `POST /api/v3/order/oco` 接口。从今开始，请使用新的 `POST /api/v3/orderList/oco` 接口（请注意，新接口使用不同的参数）。



WebSocket API

  * WebSocket API 上现已弃用 `orderList.place` 请求。从今开始，请使用新的 `orderList.place.oco` 请求（请注意，新接口使用不同的参数）。



**以下内容将于发布日期 _大约_ 一周后生效：**

  * "交易规范信息"响应中的交易对权限信息已从字段 `permissions` 移至字段 `permissionSets`。
  * 字段 `permissions` 将为空，并将在未来版本中删除。
  * 以前，`"permissions":["SPOT","MARGIN"]` 代表如果您的账户具有 `SPOT` 或 `MARGIN` 权限，您就可以在该交易对上下订单。现在，等效项是 `"permissionSets":[["SPOT","MARGIN"]]`（请注意额外的方括号）。`permissionSets`数组中的每个权限数组称为 "permission set"。
  * 交易对的权限现在可以有更多权限类型。例如，`"permissionSets":[["SPOT","MARGIN"],["TRD_GRP_004","TRD_GRP_005"]]` 指示除了支持以上提过的权限集，也接受 `TRD_GRP_004` 或 `TRD_GRP_005`。交易对的 `permissionSets` 中可以有任意排列组合的权限集。



REST API

  * `otoAllowed` 现在将出现在 `GET /api/v3/exchangeInfo` 上，指示该交易品种是否支持 One-Triggers-the-Other (OTO) 订单。



WebSocket API

  * `otoAllowed` 现在将出现在 `exchangeInfo` 上，指示该交易品种是否支持 One-Triggers-the-Other (OTO) 订单。



SBE

  * 已发布新模式 2:0 [Spot_2_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_2_0.xml)。 当前模式 1:0 [spot_1_0.xml](/zh-CN/docs/products/spot/sbe/schemas/spot_1_0.xml) 将被弃用，并从根据我们模式弃用政策，会将在 6 个月内下线。
  * 在 REST API 或 WebSocket API 上使用模式 1:0 时，消息 `ExchangeInfoResponse` 中的组"权限"将始终为空。在升级到模式 2:0后， 您才可以在 `permissionSets` 组中查找权限信息。
  * 最新模式仍将支持已弃用的 OCO 请求。
  * 请注意，在模式 2:0 实际发布之前尝试使用它会导致错误。



### 2024-02-28

**将于 2024 年 3 月 5 日生效。**

简单二进制编码 (SBE) 将部署到现货的 Rest API 和 WebSocket API 生产系统上。

更多关于SBE的信息, 请参考[常见问题解答 (FAQ)](/zh-CN/docs/products/spot/faqs/sbe_faq)

* * *

### 2024-02-08

现货的 WebSocket API 现在在[测试网](https://testnet.binance.vision)上支持简单二进制编码(SBE)。

SBE 模式已经更新了 WebSocket API 元数据，但并没有增加 `schemaId` 或者 `version`。

  * 仅在 REST API 上使用 SBE 的用户可以继续使用 SBE 模式 [`128b94b2591944a536ae427626b795000100cf1d`](/zh-CN/docs/products/spot/sbe/schemas/spot_1_0.xml)，或者更新到新提交的 SBE 模式。

  * 希望在 WebSocket API 上使用 SBE 的用户，需要更新到[最新的 SBE 模式](/zh-CN/docs/products/spot/sbe/schemas/spot_1_0.xml)。




SBE 的 [FAQ](/zh-CN/docs/products/spot/faqs/sbe_faq) 已经更新。

* * *

### 2023-12-08

简单二进制编码 (SBE) 已经在[现货测试网](https://testnet.binance.vision)上线。生产系统会在随后支持。更多关于SBE的信息, 请参考[常见问题解答 (FAQ)](/zh-CN/docs/products/spot/faqs/sbe_faq)

* * *

### 2023-12-04

**注意** ： 以下的变更将逐步推出，并预计需要大约一周的时间完成。

  * 错误消息 `Precision is over the maximum defined for this asset.` 被改为 `Parameter '%s' has too much precision.`
    * 当参数的精度超出允许范围时，将返回此错误消息。例如，如果基础资产（`base asset`）精度为6，但是设置`quantity=0.1234567`，则会出现此错误消息。
    * 这会影响所有具有以下参数的请求:
      * `quantity`
      * `quoteOrderQty`
      * `icebergQty`
      * `limitIcebergQty`
      * `stopIcebergQty`
      * `price`
      * `stopPrice`
      * `stopLimitPrice`
  * 现在，请求查询OCO开单时会正确返回**升序** 的结果。这会影响以下请求：
    * REST API: `GET /api/v3/openOrderList`
    * WebSocket API: `openOrderList.status`
  * 现在，当指定`startTime`或`fromId`时，请求查询所有 OCO 订单会正确返回**升序** 的结果。这会影响以下请求：
    * REST API: `GET /api/v3/allOrderList`
    * WebSocket API: `allOrderLists`
  * 修复了一个错误。订单查询请求不再会对新下的订单错误返回[`-2026 ORDER_ARCHIVED`](/zh-CN/docs/products/spot/errors#-2026-%E4%BA%A4%E6%98%93%E8%A2%AB%E5%BD%92%E6%A1%A3)错误。
    * REST API: `GET /api/v3/order`
    * WebSocket API: `order.status`



REST API

  * 新接口 `GET /api/v3/account/commission`
  * 新接口 `GET /api/v3/ticker/tradingDay`
  * `GET /api/v3/avgPrice` 新加字段 `closeTime`, 用于显示最后交易时间。
  * `GET /api/v3/klines` 和 `/api/v3/uiKlines` 新加可选参数 `timeZone`。
  * `POST /api/v3/order/test` 和 `POST /api/v3/sor/order/test` 新加可选参数 `computeCommissionRates`。
  * 关于发送无效接口的变动：
    * 以前，如果查询一个不存在的端点（例如 `curl -X GET "https://api.binance.com/api/v3/exchangie"`），你会收到 HTTP 404 状态码，以及响应 "`<html><body><h2>404 Not found</h2></body></html>`"。
    * 从现在开始，只有当接受请求头中包含`text/html`时，HTML响应才会出现在这种情况下。HTTP状态码将保持不变。



WebSocket API

  * 新请求 `account.commission`
  * 新增请求以允许会话身份验证: **(请注意，这些请求只能使用Ed25519密钥。)**
    * `session.logon`
    * `session.logout`
    * `session.status`
  * 新请求 `ticker.tradingDay`
  * 方法 `avgPrice` 新加字段 `closeTime`, 用于显示最后交易时间。
  * 方法 `klines` 和 `uiKlines` 新加可选参数 `timeZone`。
  * 方法 `order.test` 和 `sor.order.test` 新加可选参数 `computeCommissionRates`.
  * 修复了一个错误。之前在发送 ping 之前未经请求发送的 pongs 会导致断开连接。



WebSocket Streams

  * 新数据流 `<symbol>@avgPrice`
  * 请求中的`id`现在支持和 WebSocket API 里`id`一样的值:
    * 64位有符号整数 (之前是无符号整数)
    * 字母数字字符串；最大长度36
    * `null`
  * 修复了一个错误，之前在发送 ping 之前未经请求发送的 pongs 会导致断开连接。



User Data Streams

  * 当事件类型为 `executionReport`，而执行类型（x）为`TRADE_PREVENTION`时，字段`l`、`L`和`Y`现在将始终为0。新增字段`pl`、`pL`和`pY`将描述被阻止执行的数量、被阻止执行的价格和被阻止执行的名义金额。这些新字段显示了如果接收方订单没有启用自成交防止功能时，`l`、`L`和`Y`会是什么值。



**以下将在发布日期后 _大约_ 一周后生效:**

  * 交易对权限将仅影响下单，而不影响取消订单。
    * `permissions`仍然适用于撤消挂单再下单（Cancel-Replace orders）（比如，如果您的账户有使用此请求下单的权限，则将不允许取消操作）。



* * *

### 2023-10-19

**从 2023-10-19 00:00 UTC 开始生效**

  * 调高如下接口的请求权重:

REST API| WebSocket API| 条件| 之前的权重| 调整后权重  
---|---|---|---|---  
`GET /api/v3/trades`| `trades.recent`| N/A| 2| 10  
`GET /api/v3/depth`| `depth`| **Limit 1-100**|  2| 5  
`GET /api/v3/depth`| `depth`| **Limit 101-500**|  10| 25  
`GET /api/v3/depth`| `depth`| **Limit 501-1000**|  20| 50  
`GET /api/v3/depth`| `depth`| **Limit 1001-5000**|  100| 250  
  
* * *

### 2023-10-03

  * **下单量的退回(`Order decrement`)功能在 06:15 UTC上线.**
  * 此功能的更详细信息, 请参考 [FAQ](/zh-CN/docs/products/spot/faqs/order_count_decrement)



* * *

### 2023-08-25

  * Websocket API 的 `exchangeInfo` 中的 `RAW REQUESTS` 被移除，新增了用于表示WebSocket连接数限制的 `CONNECTIONS`。



**下面的变更会在UTC时间 2023-08-25 00:00 上线**

  * WebSocket API 的 `CONNECTIONS` 被调整为每5分钟300。
  * REST API 和 WebSocket API 的 `REQUEST_WEIGHT` 调整为每分钟6,000。
  * REST API 中的 `RAW_REQUESTS` 调整为每5分钟61,000。
  * 之前连接到 WebSocket API 的权重为1。**现权重调整到 2** 。
  * 下表的 REST API 和 WebSocket API 请求的权重被调整:

请求接口| 之前请求权重| 新请求权重  
---|---|---  
`GET /api/v3/order` `order.status`| 2| 4  
`GET /api/v3/orderList` orderList.status| 2| 4  
`GET /api/v3/openOrders` `openOrders.status` \- **带`symbol`**| 3| 6  
`GET /api/v3/openOrders` `openOrders.status` \- **不带`symbol`**| 40| 80  
`GET /api/v3/openOrderList` `openOrderLists.status`| 3| 6  
`GET /api/v3/allOrders` `allOrders`| 10| 20  
`GET /api/v3/allOrderList` `allOrderLists`| 10| 20  
`GET /api/v3/myTrades` `myTrades`| 10| 20  
`GET /api/v3/myAllocations` `myAllocations`| 10| 20  
`GET /api/v3/myPreventedMatches` `myPreventedMatches` \- **使用`preventedMatchId`**| 1| 2  
`GET /api/v3/myPreventedMatches` `myPreventedMatches` \- **使用`orderId`**| 10| 20  
`GET /api/v3/account` `account.status`| 10| 20  
`GET /api/v3/rateLimit/order` `account.rateLimits.orders`| 20| 40  
`GET /api/v3/exchangeInfo` `exchangeInfo`| 10| 20  
`GET /api/v3/depth` `depth` \- **Limit 1-100**|  1| 2  
`GET /api/v3/depth` `depth` \- **Limit 101-500**|  5| 10  
`GET /api/v3/depth` `depth` \- **Limit 501-1000**|  10| 20  
`GET /api/v3/depth` `depth` \- **Limit 1001-5000**|  50| 100  
`GET /api/v3/aggTrades` `trades.aggregate`| 1| 2  
`GET /api/v3/trades` `trades.recent`| 1| 2  
`GET /api/v3/historicalTrades` `trades.historical`| 5| 10  
`GET /api/v3/klines` `klines`| 1| 2  
`GET /api/v3/uiKlines` `uiKlines`| 1| 2  
`GET /api/v3/ticker/bookTicker` `ticker.book` \- **带`symbol`**| 1| 2  
`GET /api/v3/ticker/bookTicker` `ticker.book` \- **不带`symbol`** 或者 **带`symbols`**| 2| 4  
`GET /api/v3/ticker/price` `ticker.price` \- **带`symbol`**| 1| 2  
`GET /api/v3/ticker/price` `ticker.price` \- **不带`symbol`** 或者 **带`symbols`**| 2| 4  
`GET /api/v3/ticker/24hr` `ticker.24hr` \- **带`symbol`** 或者 ** `symbols` 带 1-20 交易对**| 1| 2  
`GET /api/v3/ticker/24hr` `ticker.24hr` \- **带`symbols` 21-100 交易对**| 20| 40  
`GET /api/v3/ticker/24hr` `ticker.24hr` \- **不带`symbol` 或者 `symbols` 带 101 个或者更多交易对**| 40| 80  
`GET /api/v3/avgPrice` `avgPrice`| 1| 2  
`GET /api/v3/ticker` `ticker`| 2| 4  
`GET /api/v3/ticker` `ticker` \- 请求的最大权重| 100| 200  
`POST /api/v3/userDataStream` `userDataStream.start`| 1| 2  
`PUT /api/v3/userDataStream` `userDataStream.ping`| 1| 2  
`DELETE /api/v3/userDataStream` `userDataStream.stop`| 1| 2  
  
* * *

### 2023-08-08

智能订单路由(Smart Order Routing：SOR）添加到 API 中。您可以在[SOR 常见问题](/zh-CN/docs/products/spot/faqs/sor_faq) 文档中找到更多详细信息。具体上线时间请关注相关公告。

REST API

  * `GET /api/v3/exchangeInfo` 变动：
    * 返回数据中添加新字段: `sors`, 用于描述交易中是否使用了 SOR。
  * `GET /api/v3/myPreventedMatches` 变动：
    * 对于所有的 Prevented Matches， 返回数据中添加新字段 `makerSymbol` 。
  * 为了在下单时使用 SOR 而添加的新接口：
    * `POST /api/v3/sor/order`
    * `POST /api/v3/sor/order/test`
  * 添加新接口: `GET /api/v3/myAllocations`



WEBSOCKET API

  * `exchangeInfo` 变动：
    * 返回数据中添加新字段: `sors` , 用于描述交易中是否使用了 SOR。
  * `myPreventedMatches` 变动：
    * 对于所有的 Prevented Matches， 返回数据中添加新字段 `makerSymbol`。
  * 为了在下单时使用 SOR 而添加的新请求：
    * `sor.order.place`
    * `sor.order.test`
  * 添加新请求 `myAllocations`



USER DATA STREAM

  * `executionReport` 变动：
    * 以下这些字段只适用于下单时使用 SOR 的情况：
      * 新字段 `b` 代表 `matchType`
      * 新字段 `a` 代表 `allocId`
      * 新字段 `k` 代表 `workingFloor`
    * 这个字段只适用于订单因为触发 STP 而将过期的情况：
      * 新字段 `Cs` 代表 `counterSymbol`



* * *

### 2023-07-18

  * 现在支持使用 Ed25519 类型的 API key。(UI 会在本周发布更新支持)
    * Ed25519 API keys 是 RSA API keys 的替代品，使用非对称加密技术来验证您的 API 请求。
    * **我们建议切换到 Ed25519** 以提高性能和安全性。  详情请参考[API Key 类型](/zh-CN/docs/products/spot/faqs/api_key_types)。
  * 文档已更新，包括了有关如何使用 Ed25519 key 对有效载荷进行签名的说明。



* * *

### 2023-07-11

**注意:** 所有更改都将逐步推出，可能需要一周时间才能完成。

  * 错误消息的变动:
    * 之前当发送重复交易对时，会返回错误信息: "Mandatory parameter symbols was not sent, was empty/null, or malformed."
    * 现在则返回消息: "Symbol is present multiple times in the list", with a new error code `-1151`
    * 受影响的接口:
      * `GET /api/v3/exchangeInfo`
      * `GET /api/v3/ticker/24hr`
      * `GET /api/v3/ticker/price`
      * `GET/api/v3/ticker/bookTicker`
      * `exchangeInfo`
      * `ticker.24hr`
      * `ticker.price`
      * `ticker.book`
  * 修复一个bug，当查询没有被存档的订单时候，可能返回错误消息称已经被存档。



Rest API

  * `GET /api/v3/account` 变动：
    * 返回数据中添加新字段 `preventSor`。
    * 返回数据中添加用户ID的新字段 `uid`。
  * `GET /api/v3/historicalTrades` 变动：
    * 鉴权类型从 `MARKET_DATA` 变更为 `NONE`。
    * 不需要设置 `X-MBX-APIKEY` 到请求的header中。



Websocket API

  * `account.status` 变动：

    * 返回数据中添加新字段 `preventSor`。
    * 返回数据中添加用户ID的新字段 `uid`。
  * `trades.historical` 变动：

    * 鉴权类型从 `MARKET_DATA` 变更为 `NONE`。
    * 请求中不需要设置 `apiKey`。
  * 修改了几个bugs: 当下单时设置 `type=MARKET` 和 `quoteOrderQty`, 也被称为"反向市价单":

    * 当处于极端市场情况下, 订单不会返回部分成交，或者成交的数量为0甚至是负数。
    * 当这种反向市价单的成交数量超过交易对的 `maxQty`, 订单会因为违反`MARKET_LOT_SIZE` 过滤器而被拒绝。
  * 修复一个OCO订单的bug: 当使用 `trailingDelta` 时候, 当任何leg被触发时, `trailingTime` 值可能不正确。

  * 这些接口的返回数据中添加新字段 `transactTime` :

    * `DELETE /api/v3/order`
    * `POST /api/v3/order/cancelReplace`
    * `DELETE /api/v3/openOrders`
    * `DELETE /api/v3/orderList`
    * `order.cancel`
    * `order.cancelReplace`
    * `openOrders.cancelAll`
    * `orderList.cancel`



* * *

### 2023-06-06

  * 为了提供系统的冗余能力，新加一个API接入网址: **<https://api-gcp.binance.com/>**
    * 此网址利用了 GCP (Google Cloud Platform) 的CDN，可能在性能上比`api1`-`api4`要慢。



* * *

### 2023-05-26

**注意:** 所有更改都将逐步推出到我们的所有服务器，并可能需要一周时间才能完成。

  * 以下基本接口可能会提供比 **<https://api.binance.com>** 更好的性能但其稳定性略为逊色:
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**



* * *

### 2023-05-24

  * **以前的市场数据 URL 已不建议使用。请立即更新您的代码，以防止来自我们的服务被中断**
    * 来自 `data.binance.com` 的 API 市场数据现在可以从 `data-api.binance.vision` 访问。
    * 来自 `data-stream.binance.com` 的 Websocket 市场数据现在可以从 `data-stream.binance.vision` 访问。



* * *

### 2023-03-13

**注意:** 所有更改都将逐步推出到我们的所有服务器，并可能需要一周时间才能完成。

  * 某些问题的错误消息已经改进，以便更轻松地进行解决。

情况| 之前的错误消息| 新错误消息  
---|---|---  
由于交易权限被禁用，账户无法下订单或取消订单。| This action is disabled on this account.| This account may not place or cancel orders.  
当配置在交易对上的权限与账户上的权限不匹配时。| This action is disabled on this account.| This symbol is not permitted for this account.  
当账户在其没有权限的交易对上下订单时。| This action is disabled on this account.| This symbol is restricted for this account.  
当 `symbol` 不在 `TRADING` 时下订单。| Unsupported order combination.| This order type is not possible in this trading phase.  
在不支持 `IOC` 或 `FOK` 的交易阶段上使用 `timeinForce` = `IOC` 或 `FOK` 下订单时。| Unsupported order combination.| Limit orders require GTC for this phase.  
  
  * 更正了查询归档订单的错误消息：

    * 之前，如果查询了一个归档订单（即状态为 `CANCELED` 或 `EXPIRED`，`executedQty` == 0 而且最后的更新在 90 天以前），错误消息将是：
    
    Code
    
    {
      "code": -2013,
      "msg": "Order does not exist."
    }

    * 现在，错误消息为：
    
    Code
    
    {
      "code": -2026,
      "msg": "Order was canceled or expired with no executed qty over 90 days ago and has been archived."
    }

  * API 请求使用 `startTime` 和 `endTime` 的行为：

    * 之前，如果 `startTime` == `endTime`，一些请求会失败。
    * 现在，所有接受 `startTime` 和 `endTime` 的 API 请求会允许这些参数相等。这适用于以下接口：
      * Rest API
        * `GET /api/v3/aggTrades`
        * `GET /api/v3/klines`
        * `GET /api/v3/allOrderList`
        * `GET /api/v3/allOrders`
        * `GET /api/v3/myTrades`
      * Websocket API
        * `trades.aggregate`
        * `klines`
        * `allOrderList`
        * `allOrders`
        * `myTrades`
  * 如果用户的IP地址因违反 IP 速率限制（状态码为 `418`）而被禁止，那么连接到 WebSocket API 的用户将被断开连接。




虽然以下更改将在发布日期后 **大约一周内生效** ，但是与其相关的文档已经被更改了：

  * 过滤器评估的更改：
    * 之前的行为: `LOT_SIZE` 和 `MARKET_LOT_SIZE` 要求 (`quantity` \- `minQty`) % `stepSize` == 0。
    * 新行为: 现在已更改为 (`quantity` % `stepSize`) == 0。
  * 使用 `quoteOrderQty` 的 `MARKET`订单的错误修复：
    * 之前的行为: 订单的状态将始终为 `FILLED`，即使订单没有完全成交。
    * 新行为: 如果订单由于流动性不足而没有完全成交，则订单状态将为 `EXPIRED`，仅当订单完全成交时状态为 `FILLED`。



REST API

  * `DELETE /api/v3/order` 和 `POST /api/v3/order/cancelReplace` 的更改:
    * 新的可选参数 `cancelRestrictions`，该参数用于决定是否能成功取消状态为 `NEW` 或 `PARTIALLY_FILLED` 的订单。
    * 如果由于 `cancelRestrictions` 而取消订单失败，错误将是：
    
    Code
    
    {
      "code": -2011,
      "msg": "Order was not canceled due to cancel restrictions."
    }




WEBSOCKET API

  * `order.cancel` 和 `order.cancelReplace` 的更改:
    * 新的可选参数 `cancelRestrictions`，该参数用于决定是否能成功取消状态为 `NEW` 或 `PARTIALLY_FILLED` 的订单。
    * 如果由于 `cancelRestrictions` 而取消订单失败，错误将是：
    
    Code
    
    {
      "code": -2011,
      "msg": "Order was not canceled due to cancel restrictions."
    }




* * *

### 2023-02-17

**WebSocket频率限制变动**

`WS-API` 和 `Websocket Stream` 现在限制每个IP地址、每5分钟可以发送连接请求的上限是300次。

* * *

### 2023-01-26

根据此[公告](https://www.binance.com/zh-CN/support/announcement/%E5%B9%A3%E5%AE%89%E7%8F%BE%E8%B2%A8%E6%8E%A8%E5%87%BAapi%E8%87%AA%E6%88%90%E4%BA%A4%E9%A0%90%E9%98%B2-stp-%E5%8A%9F%E8%83%BD-312fd0112fb44635b397c116e56d8f84)，Self-Trade Prevention 将在 **2023-01-26 08:00 UTC** 发布。

* * *

### 2023-01-23

  * 添加了新的 API 集群 <https://api4.binance.com>



* * *

### 2023-01-19

实际发布日期待定

**新功能** ：Self-Trade Prevention（STP）会添加到系统中。此功能将阻止订单与来自同一账户或者同一 `tradeGroupId` 账户的订单交易。

请使用现货 REST API 的 `GET /api/v3/exchangeInfo` 或 Websocket API 的 `exchangeInfo` 看 STP 的状态。
    
    
    Code
    
    {
        "defaultSelfTradePreventionMode": "NONE",     // selfTradePreventionMode 的默认值
        "allowedSelfTradePreventionModes": [          // selfTradePrevention 的可用模式
            "NONE",
            "EXPIRE_TAKER",
            "EXPIRE_BOTH",
            "EXPIRE_MAKER"
        ]
    }

在[STP 常见问题](/zh-CN/docs/products/spot/faqs/stp_faq) 文档中可以找到更多其它关于 STP 功能的详细信息。

REST API

  * 新的订单状态：`EXPIRED_IN_MATCH` \- 订单由于 STP 触发而过期。
  * 新的接口：
    * `GET /api/v3/myPreventedMatches` \- 获取由于 STP 触发而过期的订单。
  * 新的可选参数 `selfTradePreventionMode` 已添加到以下的接口：
    * `POST /api/v3/order`
    * `POST /api/v3/order/oco`
    * `POST /api/v3/cancelReplace`
  * 如果有预防自我交易(Prevented Match)，所有下单相关的接口会出现新字段：
    * `tradeGroupId` \- 仅当账户配置为 `tradeGroupId` 时才会出现。
    * `preventedQuantity` \- 被防止交易的订单数量。
    * `preventedMatches` 数组会有以下的字段：
      * `preventedMatchId`
      * `makerOrderId`
      * `price`
      * `takerPreventedQuantity` \- 仅当 `selfTradePreventionMode` 设置为 `EXPIRE_TAKER` 或 `EXPIRE_BOTH` 时才会出现。
      * `makerPreventedQuantity` \- 仅当 `selfTradePreventionMode` 设置为 `EXPIRE_MAKER` 或 `EXPIRE_BOTH` 时才会出现。
  * 如果订单因 STP 触发而过期，以下查询订单接口的响应中可以出现新的字段 `preventedMatchId` 和 `preventedQuantity`：
    * `GET /api/v3/order`
    * `GET /api/v3/openOrders`
    * `GET /api/v3/allOrders`



WEBSOCKET API

  * 新的订单状态：`EXPIRED_IN_MATCH` \- 订单由于 STP 触发而过期。
  * 新的请求：`myPreventedMatches` \- 获取由于 STP 触发而过期的订单。
  * 新的可选参数 `selfTradePreventionMode` 已添加到以下的请求：
    * `order.place`
    * `orderList.place`
    * `order.cancelReplace`
  * 如果有防止自我交易，将为所有下订单的请求会出现的新响应：
    * `tradeGroupId` \- 仅当账户配置为 `tradeGroupId` 时才会出现。
    * `preventedQuantity` \- 被防止交易的订单数量。
    * `preventedMatches` 数组会有以下的字段：
      * `preventedMatchId`
      * `makerOrderId`
      * `price`
      * `takerPreventedQuantity` \- 仅当 `selfTradePreventionMode` 设置为 `EXPIRE_TAKER` 或 `EXPIRE_BOTH` 时才会出现。
      * `makerPreventedQuantity` \- 仅当 `selfTradePreventionMode` 设置为 `EXPIRE_MAKER` 或 `EXPIRE_BOTH` 时才会出现。
  * 如果订单因 STP 触发而过期，以下查询订单接口的响应中可以出现新的字段 `preventedMatchId` 和 `preventedQuantity`：
    * `order.status`
    * `openOrders.status`
    * `allOrders`



USER DATA STREAM

  * 新的执行类型：`TRADE_PREVENTION`。
  * `executionReport` 的新字段（这些字段只会在订单因 STP 触发而过期时出现）：
    * `u` \- `tradeGroupId`
    * `v` \- `preventedMatchId`
    * `U` \- `counterOrderId`
    * `A` \- `preventedQuantity`
    * `B` \- `lastPreventedQuantity`



* * *

### 2022-12-28

  * 现货 WebSocket API 文档已更新，添加了如何使用 RSA key 签署请求。



* * *

### 2022-12-26

  * 现货的 Websocket API 发布到生产系统中。
  * 现货的 Websocket API 可以通过URL: `wss://ws-api.binance.com/ws-api/v3` 来访问。



* * *

### 2022-12-15

  * 添加新的RSA签名验证方式
    * 文档已更新以显示如何创建 RSA keys。
    * 建议在生成 API key 时使用 RSA keys。
    * 我们接受`PKCS#8`（BEGIN PUBLIC KEY）。
    * 稍后将添加有关如何上传 RSA public key 的更多详细信息。
  * 现货 WebSocket API 现在可以在 SPOT 测试网上使用。
    * WebSocket API 允许通过 WebSocket 连接下订单、取消订单等。
    * WebSocket API 是一个 **独立** 于 WebSocket 市场数据流的服务。 即，下订单和收听市场数据需要两个独立的 WebSocket 连接。
    * WebSocket API 与 REST API 相同过滤器和速率限制规则。
    * WebSocket API 与 REST API 提供相同的功能，接受相同的参数，返回相同的状态和错误代码。



**WEBSOCKET API 会晚些时候在生产系统中可用。**

* * *

### 2022-12-13

REST API

错误代码 `-1003` 的一些错误消息已更改

  * 之前的错误消息: `Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.` 改成了：


    
    
    Code
    
    Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.

  * 之前的错误消息: `Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.` 改成了：


    
    
    Code
    
    Way too much request weight used; IP banned until %s Please use WebSocket Streams for live updates to avoid bans.

* * *

### 2022-12-05

**备注：** 这些更新正在逐步部署到我们所有的服务器，大约需要一周时间才能完成。

WEBSOCKET

  * `!bookTicker` 在 **2022-12-07** 下线。 请改用按 symbol 的最优挂单信息的数据流（`<symbol>@bookTicker`）。
    * 可以通过一个连接订阅多个 `<symbol>@bookTicker` 数据流。 （例如`wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker`）



REST API

  * 新的错误代码 `-1135`
    * 如果参数是无效的 JSON 格式，则会出现此错误代码。
  * 新的错误代码 `-1108`
    * 如果发送的参数的值太长，可能会导致溢出，则会发生此错误。
    * 此错误代码可能出现在以下接口：
      * `POST /api/v3/order`
      * `POST /api/v3/order/cancelReplace`
      * `POST /api/v3/order/oco`
  * `GET /api/v3/aggTrades` 更新
    * 之前的规则: `startTime` 和 `endTime` 必须结合使用，并且只能相隔一个小时。
    * 新的规则: `startTime` 和 `endTime` 可以单独使用，一个小时的限制已被取消。
      * 仅使用 startTime 时，如果limit的值为N, 将返回从此时间开始的N条交易。
      * 仅使用 endTime 时，如果limit的值为N, 将返回到此时间的N条交易.
      * 如果不提供 `limit`，无论是组合使用还是单独发送，服务器端都将使用默认的 `limit`。
  * `GET /api/v3/myTrades` 更新
    * 修复了 `symbol` \+ `orderId` 组合会返回所有交易，可能会超过`LIMIT`的默认值`500`。

    * 之前的行为： API 将根据发送的参数组合发送特定的错误消息。 例如：
          
          Code
          
          {
            "code": -1106,
            "msg": "Parameter X was sent when not required."
          }

    * 新的行为: 如果接口不支持可选参数组合，那么服务器会返回一般性的错误:
          
          Code
          
          {
            "code": -1128,
            "msg": "Combination of optional parameters invalid."
          }

    * 添加一个新的参数组合: `symbol` \+ `orderId` \+ `fromId`.

    * 下面的参数组合不再支持:

      * `symbol` \+ `fromId` \+ `startTime`
      * `symbol` \+ `fromId` \+ `endTime`
      * `symbol` \+ `fromId` \+ `startTime` \+ `endTime`
    * 当前支持的所有参数组合：

      * `symbol`
      * `symbol` \+ `orderId`
      * `symbol` \+ `startTime`
      * `symbol` \+ `endTime`
      * `symbol` \+ `fromId`
      * `symbol` \+ `startTime` \+ `endTime`
      * `symbol`\+ `orderId` \+ `fromId`



**备注：** 这些新字段将在发布日期后大约一周出现。

  * `GET /api/v3/exchangeInfo` 更新
    * 新字段 `defaultSelfTradePreventionMode` 和 `allowedSelfTradePreventionModes`
  * 下单，查询订单和撤销订单接口的更新:
    * 响应中会出现新的字段 `selfTradePreventionMode`。
    * 以下接口会受到影响:
      * `POST /api/v3/order`
      * `POST /api/v3/order/oco`
      * `POST /api/v3/order/cancelReplace`
      * `GET /api/v3/order`
      * `DELETE /api/v3/order`
      * `DELETE /api/v3/orderList`
  * `GET /api/v3/account` 更新
    * 响应中会出现新的字段 `requireSelfTradePrevention`.
  * 以下接口的响应中会出现新字段 `workingTime`（指示订单何时添加到了订单簿）：
    * `POST /api/v3/order`
    * `GET /api/v3/order`
    * `POST /api/v3/order/cancelReplace`
    * `POST /api/v3/order/oco`
    * `GET /api/v3/order`
    * `GET /api/v3/openOrders`
    * `GET /api/v3/allOrders`
  * 如果`trailingDelta`作为参数提供给了`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`，`STOP_LOSS`或 `STOP_LOSS_LIMIT`的订单，那么下面接口中会出现`trailingTime`, 用来表示追踪单被激活和跟踪价格变化的时间:
    * `POST /api/v3/order`
    * `GET /api/v3/order`
    * `GET /api/v3/openOrders`
    * `GET /api/v3/allOrders`
    * `POST /api/v3/order/cancelReplace`
    * `DELETE /api/v3/order`
  * 字段 `commissionRates` 会在 `GET /api/v3/acccount` 的响应中出现。



USER DATA STREAM

  * eventType `executionReport` 有新的字段
    * `V` \- `selfTradePreventionMode`
    * `D` \- `trailing_time` (追踪单被激活时会出现)
    * `W` \- `workingTime` (如果 `isWorking`=`true` 会出现)



* * *

### 2022-12-02

  * 新增一个用于访问市场信息的RESTful API URL: `https://data.binance.com`.
  * 新增一个用于访问市场信息的WebSocket URL: `wss://data-stream.binance.com`.



* * *

### 2022-09-30

`!bookTicker`的WebSocket推送的变更.

  * 全市场最优挂单信息推送(`!bookTicker`)计划在**2022年11月** 下线, 具体下线的时间会在后面通告.
  * 请使用按Symbol的最优挂单信息推送(`<symbol>@bookTicker`).
  * 多个 `<symbol>@bookTicker` 可以订阅在一个WebSocket连接上.
    * 比如 `wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker`



* * *

### 2022-09-15

这些变动会是滚动发布，可能需要几天才会部署到所有服务器.

  * 接口 `GET /api/v3/exchangeInfo` 的变动
    * 添加一个新的参数 `permissions` , 用于查询适用于相应权限的所有交易对.
    * 如果查询时不提供此参数, 则默认值是 `["SPOT","MARGIN","LEVERAGED"]`.
      * 这表示如果请求 `GET /api/v3/exchangeInfo` 时候没有任何参数, 则会返回拥有权限是 `SPOT`, `MARGIN` , `LEVERAGED` 的交易对.
      * 如果要查询其他交易权限, 比如`TRD_GRP_004`等, 需要在查询参数里设置(比如`permissions`=`TRD_GRP_004`).
    * 此参数不可以同时和 `symbol` 或者 `symbols` 使用.



* * *

### 2022-08-23

此变动会滚动发布, 可能需要一段时间更新到所有服务器上。

  * 接口 `GET /api/v3/ticker` 与 `GET /api/v3/ticker/24hr` 变动
    * 添加新可选参数 `type`
    * `type` 可接受的参数值有 `FULL` 与 `MINI`
      * `FULL` 是默认值， 也是原来接口所返回的响应
      * `MINI` 省略了以下字段: `priceChangePercent`, `weightedAvgPrice`, `bidPrice`, `bidQty`, `askPrice`, `askQty` 与 `lastQty`
  * 添加新错误代码 `-1008`
    * 每当服务器的请求超载时都会发送此消息
    * 此错误代码只会在 SPOT API 里出现
  * 接口 `GET /api/v3/account` 添加新参数 `brokered`
  * 添加新接口: `GET /api/v3/uiKlines`
  * 添加新k线间隔: `1s`



* * *

### 2022-08-08

REST API

  * 接口 `POST /api/v3/order` 与 `POST /api/v3/order/cancelReplace` 变动
    * 添加新可选参数 `strategyId` 与 `strategyType`
      * `strategyId` 是用于将订单标识为某策略的参数。
      * `strategyType` 是用于标识在执行的策略。(例如：如果所有订单属于现货网格策略，订单可设置为`strategyType=1000000`)
  * 接口 `POST /api/v3/order/oco` 变动
    * 添加新可选参数 `limitStrategyId`, `limitStrategyType`, `stopStrategyId`, `stopStrategyType`
    * 这些是OCO订单里两个leg的策略元数据
    * `limitStrategyType` 和 `stopStrategyType` 都不能低于 `1000000`
  * 接口 `GET /api/v3/order`, `GET /api/v3/openOrders` 与 `GET /api/v3/allOrders` 变动
    * 新增参数 `strategyId` 与 `strategyType` 必须在下单时填上字段才会在回应JSON里返回
  * 接口 `DELETE /api/v3/order` 与 `DELETE /api/v3/openOrders` 变动
    * 新增参数 `strategyId` 与 `strategyType` 必须在下单时填上字段才会在回应JSON里返回



USER DATA STREAM

  * eventType `executionReport` 新增参数
    * `j` 代表 `strategyId`
    * `J` 代表 `strategyType`
    * 必须在下单时填上字段才会在回应里返回



* * *

### 2022-06-20

接口 `GET /api/v3/ticker` 变动

  * 权重从每`symbol` 5 降低到 2.
  * 每次请求最多可以有100个交易对.
    * 如果`symbols`请求超过100个交易对, 会收到如下错误信息:
    
    Code
    
    {
      "code": -1101,
      "msg": "Too many values sent for parameter 'symbols', maximum allowed up to 100."
    }

  * 单请求的权重上限为100.
    * 比如，如果请求的交易对超过50个，请求的权重是100.



* * *

### 2022-06-15

**注意:** 此变动不会立刻可用, 会在后面几天上线。

SPOT API

  * 添加新接口 `GET /api/v3/ticker`
    * 基于 `windowSize` 返回最近的价格变动。
    * 无需像 `GET /api/v3/ticker/24hr` 提供symbols参数。
    * 如果不提供 `windowSize` 参数，默认值是`1d`。
    * 响应和 `GET /api/v3/ticker/24hr` 相似，但不包括以下数据：`prevClosePrice`, `lastQty`, `bidPrice`, `bidQty`, `askPrice`, `askQty`
  * 添加新接口 `POST /api/v3/order/cancelReplace`
    * 撤消当前的挂单并在同样的交易对上下新订单。
    * 过滤器会在**撤单前** 做判断。
      * 例如，`MAX_NUM_ORDERS` 是 10，如果目前挂单也是10，调用 `POST /api/v3/order/cancelReplace`会失败。撤单与下单的操作都不会被执行。
    * 更新将在几天后上线，升级完毕后才会开启此功能。
  * `GET /api/v3/exchangeInfo` 在`symbols`列表里返回新数据`cancelReplaceAllowed`。
  * 添加新的过滤器 `NOTIONAL`
    * 基于`minNotional` 与 `maxNotional` 值来限制名义价值 (`price * quantity`)
  * 添加新的过滤器 `EXCHANGE_MAX_NUM_ICEBERG_ORDERS`
    * 账号最大冰山挂单数



WEBSOCKETS

  * 新的symbol ticker流, 可以选择 `1h` 或者 `4h`时间窗口：
    * 单个交易对: `<symbol>@ticker_<window-size>`
    * 市场所有交易对: `!ticker_<window-size>@arr`



* * *

### 2022-05-23

  * Order Book 深度的变动

    * 之前深度的数量在一些极端情况下会出现负数.
    * 之后深度数量不会溢出, 而是限制在64位的最大值, 这表示深度的数量达到，或者超过了最大值. 最大值和交易对的`base asset`的精度有关. 比如如果精度是8位小数，最大值则为92,233,720,368.54775807.
    * 原有的深度价位, 在修复上线后, 需要价位上有变动, 才能体现新的修复.
  * 哪里有影响?

    * 现货深度接口
      * `GET /api/v3/depth`
    * Websocket Streams
      * `<symbol>@depth`
      * `<symbol>@depth@100ms`
      * `<symbol>@depth<levels>`
      * `<symbol>@depth<levels>@100ms`
  * `MAX_POSITION` 的更新

    * 如果一个订单的数量(`quantity`) 可能导致持有仓位溢出, 会触发过滤器 `MAX_POSITION`.
  * `GET api/v3/aggTrades` 更新

    * 如果同时提供 `startTime` 和 `endTime`, 旧的记录会返回.
  * 如果接口 `GET /api/v3/myTrades` 中没有提供参数 `symbol`, 错误消息变为:



    
    
    Code
    
    {
      "code": -1102,
      "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
    }

  * 下面的接口提供参数 `symbols` 用于查询多个symbol.

    * `GET /api/v3/ticker/24hr`
    * `GET /api/v3/ticker/price`
    * `GET /api/v3/ticker/bookTicker`
  * 上面接口的权重取决于请求 `symbols` 的数量, 具体请看下面的列表:


接口| Symbols的数量| 权重  
---|---|---  
`GET /api/v3/ticker/price`| Any| 2  
`GET /api/v3/ticker/bookTicker`| Any| 2  
`GET /api/v3/ticker/24hr`| 1-20| 1  
`GET /api/v3/ticker/24hr`| 21-100| 20  
`GET /api/v3/ticker/24hr`| >= 101| 40  
  
* * *

### 2022-04-13

REST API

  * 现货交易支持追踪止损(Trailing Stop)订单.
    * 追踪止损通过一个新的参数`trailingDelta`来设置基于市场价的一个自动触发价格.
    * 只适用于订单类型: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.
    * 参数`trailingDelta`的单位为基点(BIPS).
      * 比如一个`STOP_LOSS`卖单设置`trailingDelta`为100, 那么订单会在当前市场价格从下单后的最高点下降1%的时候被触发。(100 / 10,000 => 0.01 => 1%)
    * 用于OCO订单的时候, 如果市场变动触发了`STOP_LOSS`订单, 那么此止损订单变成追踪止损订单.
    * 当参数`trailingDelta`和`stopPrice`一起使用时, 一旦`stopPrice`条件被触发，系统会开始追踪当前的价格变动. 从`stopPrice`价格开始，到基于`trailingDelta`值之间变动.
    * 如果没有提供`stopPrice`, 系统开始追踪价格从最新价到基于`trailingDelta`值之间变动.
  * `POST /api/v3/order` 变动
    * 添加新可选参数 `trailingDelta`
  * `POST /api/v3/order/test` 变动
    * 添加新可选参数 `trailingDelta`
  * `POST /api/v3/order/oco` 变动
    * 添加新可选参数 `trailingDelta`
  * 添加新的过滤器 `TRAILING_DELTA`
    * 用于限定 `trailingDelta` 的最大和最小值.



USER DATA STREAM

  * User Data Stream 的`executionReport`添加新参数
    * "d" 代表`trailingDelta`



* * *

### 2022-04-12

**Note:** 下面的变更会在后面几天上线.

  * `GET api/v3/allOrders` 如果没有提供 `symbol`, 则返回错误信息:
        
        Code
        
        {
          "code": -1102,
          "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
        }

  * 修复一个错误信息中的拼写错误。 如果账号被禁用了相应的权限(比如提款，交易等), 则服务器返回错误:
        
        Code
        
        "This action is disabled on this account."

  * 在市场数据(market data)审计中，发现了一些现货的聚合交易数据(aggTrades)中的问题.
    * 丢失的记录已经被补回.
    * 重复的记录被标记成无效，具体的值设置成如下:
      * p = '0' // price
      * q = '0' // qty
      * f = -1 // ﬁrst_trade_id
      * l = -1 // last_trade_id



* * *

### 2022-02-28

  * 在接口`GET /api/v3/exchangeInfo`中添加新字段`allowTrailingStop`.



* * *

### 2022-02-24

  * 现货规则`PRICE_FILTER`里面的 `(price-minPrice) % tickSize == 0` 改成 `price % tickSize == 0`
  * 新添加了一个规则 `PERCENT_PRICE_BY_SIDE`.
  * 接口 `GET api/v3/depth` 的变动:
    * `limit` 原先必须是固定值(比如 5, 10, 20, 50, 100, 500, 1000, 5000), 现在可以是在1-5000之间的任意的正整数, 服务器会返回指定的limit数量。(比如如果设置limit=3, 会返回前3个最好的卖价和买价)
    * 如果`limit`超过5000, 服务器也最多返回5000条记录.
    * 相应的, 此接口的权重变成:

Limit| Request Weight  
---|---  
1-100| 1  
101-500| 5  
501-1000| 10  
1001-5000| 50  
  
  * GET `api/v3/aggTrades` 接口的变动:
    * 当同时提供参数 `startTime` 和 `endTime`, 最旧的订单会优先返回.



* * *

### 2021-12-29

  * 移除交易对类型枚举
  * 新增权限枚举



* * *

### 2021-11-01

  * 新增接口 `GET /api/v3/rateLimit/order`
    * 回传用户在当前时间区间内的下单总数
    * 此接口的权重为20



* * *

### 2021-09-14

  * 添加一个基于OpenAPI规范的RESTful API接口定义的[YAML文件](https://github.com/binance/binance-api-swagger)



* * *

### 2021-08-12

  * GET `api/v3/myTrades` 添加新的参数 `orderId`



* * *

### 2021-05-12

  * 在文档中添加接口的数据来源说明
  * 在每个接口中添加相应的数据源
  * GET `api/v3/exchangeInfo` 现在支持单个或者多个交易对查询



* * *

### 2021-04-26

从 **April 28, 2021 00:00 UTC** 开始,下面接口的权重有如下变动:

  * `GET /api/v3/order` 权重改为 2
  * `GET /api/v3/openOrders` 权重改为 3
  * `GET /api/v3/allOrders` 权重改为 10
  * `GET /api/v3/orderList` 权重改为 2
  * `GET /api/v3/openOrderList` 权重改为 3
  * `GET /api/v3/account` 权重改为 10
  * `GET /api/v3/myTrades` 权重改为 10
  * `GET /api/v3/exchangeInfo` 权重改为 10



* * *

### 2021-01-01

**USER DATA STREAM**

  * 移除`outboundAccountInfo`事件.



* * *

### 2020-11-27

为了优化性能，除了当前的`api.binance.com`，新加了一些API的集群。如果访问`api.binance.com`有性能问题，也可以尝试访问:

  * <https://api1.binance.com/api/v3/>*
  * <https://api2.binance.com/api/v3/>*
  * <https://api3.binance.com/api/v3/>*



### 2020-09-09

用户数据 STREAM

  * `outboundAccountInfo`事件不再推荐使用。
  * `outboundAccountInfo`事件以后会被删除(具体时间未定) **请使用`outboundAccountPosition` 事件.**
  * `outboundAccountInfo`只推送余额不为0，以及余额刚变成0的资产。



* * *

### 2020-05-01

  * 从2020-05-01 UTC 00:00开始, 所有交易对都会有最多200个挂单的限制, 体现在过滤器[MAX_NUM_ORDERS](/zh-CN/docs/products/spot/filters#max_num_orders-%E6%9C%80%E5%A4%9A%E8%AE%A2%E5%8D%95%E6%95%B0)上.
    * 已经存在的挂单不会被移除或者撤销。
    * 单交易对(`symbol`)的挂单数量达到或超过200的账号, 无法在此交易对上下新的订单, 除非挂单数量低于200。
    * OCO订单在被触发成`LIMIT`订单, 或者被触发成`STOP_LOSS`(或者`STOP_LOSS_LIMIT`)前, 被认为是2个挂单量. 一旦OCO订单被触发, 就只被算作一个挂单。



* * *

### 2020-04-23

WEB SOCKET 连接限制

  * Websocket服务器每秒最多接受5个消息。消息包括:
    * PING帧
    * PONG帧
    * JSON格式的消息, 比如订阅, 断开订阅.
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅 **1024** 个Streams。



* * *

### 2020-03-24

  * 添加过滤器 `MAX_POSITION`.
    * 这个过滤器定义账户允许的基于`base asset`的最大仓位。一个用户的仓位可以定义为如下资产的总和:

      * `base asset`的可用余额
      * `base asset`的锁定余额
      * 所有处于open的买单的数量总和
    * 如果用户的仓位大于最大的允许仓位，买单会被拒绝。




* * *

### 2018-11-13

REST API

  * 账户交易权限被禁时允许进行撤单操作。
  * 增加了新的过滤器: `PERCENT_PRICE`, `MARKET_LOT_SIZE`, `MAX_NUM_ICEBERG_ORDERS`。
  * 增加了 `RAW_REQUESTS` 频率限制. 该限制仅统计请求次数，不统计请求权重。
  * /api/v3/ticker/price 无symbol参数时，权重增加到2。
  * /api/v3/ticker/bookTicker 无symbol参数时，权重增加到2。
  * DELETE /api/v3/order 现在会返回订单撤销前所处的末次状态。
  * `MIN_NOTIONAL` 新增两个参数: `applyToMarket` (是否对市价单生效) and `avgPriceMins` (对市价单生效时，估算金额时使用过去几分钟的平均价格?).
  * /api/v1/exchangeInfo 中的限制增加了`intervalNum`. `intervalNum`表示该限制针对多少时间间隔进行统计. 例如: `intervalNum`= 5, `interval` = minute, 表示该限制对每5分钟内的行为进行统计。



#### 如何计算过去n分钟平均价格:

  1. [对过去n分钟所有订单的数量*价格求和] / 过去n分钟所有订单的数量
  2. 如果过去n分钟没有交易发生，则继续向前追溯，直到找到第一个交易，以此价格作为过去n分钟平均价格。
  3. 如果该交易对之前从未发生过交易，则无平均价格，亦即无法在该交易对下市价单，必须至少有一个（双方均未限价单）的交易成交后才可以下市价单。
  4. 当前系统使用的平均价格可以通过接口 `https://api.binance.com/api/v3/avgPrice?symbol=<symbol>`查询例如 <https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT>



USER DATA STREAM

  * 成交报告中增加了 `末次成交金额` (`Y`)，等于 `末次成交量` * `末次成交价格` (`L` * `l`).



* * *

### 2018-07-18

REST API

  * 新过滤器: `ICEBERG_PARTS`
  * `POST api/v3/order` 中 `newOrderRespType` 参数的缺省值更改; `MARKET` `LIMIT` 默认为 `FULL`, 其他默认为 `ACK`.
  * POST api/v3/order `RESULT` 与 `FULL` 响应中增加 `cummulativeQuoteQty`
  * GET api/v3/openOrders 无symbol调用权重下降为 40.
  * GET api/v3/ticker/24hr 无symbol调用权重下降为 40.
  * GET /api/v1/trades amount最大可取到1000.
  * GET /api/v1/historicalTrades amount最大可取到1000.
  * GET /api/v1/aggTrades amount最大可取到1000.
  * GET /api/v1/klines amount最大可取到1000.
  * 订单查询结果返回中增加 `updateTime` 字段，代表该订单末次更新(创建、成交、过期、取消、拒绝等等)时间; `time` 仅表示创建时间.
  * 订单查询结果中增加 `cummulativeQuoteQty`字段. 负值表示尚无任何成交，该字段不可用.
  * `REQUESTS` 限制更名为 `REQUEST_WEIGHT`. 避免名字造成的误解。



USER DATA STREAM

  * 订单报告与成交报告中增加`cummulativeQuoteQty` 字段 (`Z`). 表示已经成交的金额， 即已经花费的金额(买入订单)或已经收到的金额(卖出订单)，均未计算手续费. 此功能增加之前成交的订单在历史订单接口中查询到的该字段可能小于零.
  * `cummulativeQuoteQty`/`cummulativeQty` 可以用来计算该订单已经成交部分的平均价格。
  * 成交报告中增加了 `O`字段 (订单创建时间)



* * *

### 2018-01-23

  * GET /api/v1/historicalTrades权重降为 5
  * GET /api/v1/aggTrades 权重降为 1
  * GET /api/v1/klines 权重降为 1
  * GET /api/v1/ticker/24hr 不带symbol参数的权重降为 symbols总数 / 2
  * GET /api/v3/allOrders 权重降为 5
  * GET /api/v3/myTrades 权重降为 5
  * GET /api/v3/account 权重降为 5
  * GET /api/v1/depth limit=500 权重降为 5
  * GET /api/v1/depth limit=1000 权重降为 10
  * websocket 用户增加 -1003 error code



* * *

### 2018-01-20

  * GET /api/v1/ticker/24hr 单symbol参数调用权重降为 1
  * GET /api/v3/openOrders 不带symbol参数的权重降为 symbols总数 / 2
  * GET /api/v3/allOrders 权重降为 15
  * GET /api/v3/myTrades 权重降为 15
  * GET /api/v3/order 权重降为 1
  * 自成交现在会在myTrades结果中有两条记录。



* * *

### 2018-01-14

  * GET /api/v1/aggTrades 权重改为 2
  * GET /api/v1/klines 权重改为 2
  * GET /api/v3/order 权重改为 2
  * GET /api/v3/allOrders 权重改为 20
  * GET /api/v3/account 权重改为 20
  * GET /api/v3/myTrades 权重改为 20
  * GET /api/v3/historicalTrades 权重改为 20



此页面是否有帮助？

Last modified on November 12, 2026

[介绍](/zh-CN/docs/introduction)[过滤器](/zh-CN/docs/products/spot/filters)