---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/changelog'
updated_at: 2026-11-13
---

# Release notes

> A history of changes to Kraken's Exchange APIs

## 2026

### 12 November 2026 — Unified WS for Futures - Derivatives WS v1

* **DEPRECATED** the [Derivatives WebSocket](https://docs.kraken.com/exchange/api-reference/futures-websocket.md) (`wss://futures.kraken.com/ws/v1`). Existing integrations continue to work until 1 March 2027, when the Derivatives WebSocket will no longer be available
* New integrations should use the [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket), which streams Spot and Derivatives over a single connection. Set `asset_class` to `derivatives` on each subscription or order message to select Derivatives markets. Docs available here [https://docs.kraken.com/exchange/api-reference/unified-ws/ticker](https://docs.kraken.com/exchange/api-reference/unified-ws/ticker.md).
* The Unified WebSocket also supports order entry (`add_order`, `amend_order`, `cancel_order`, `cancel_all`, `cancel_after`) and authenticates with a token from [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token), requested with a Kraken API key rather than a Derivatives API key
* See the [Derivatives WebSocket guide](https://docs.kraken.com/exchange/guides/futures/websockets.md#deprecation-and-unified-websocket) for a comparison and a subscribe example
* To make the move easier, Kraken's [SDKs](https://github.com/krakenfx/kraken-api-sdk) now support Futures on the Unified WebSocket. The [Rust SDK](https://docs.kraken.com/home/sdks/rust.md) covers Derivatives market data, private streams (executions, positions, margin and balances) and order entry, and handles authentication, token refresh, reconnects and order-book checksums for you ([https://docs.kraken.com/home/sdks/index](https://docs.kraken.com/home/sdks/index.md))

### 12 November 2026 — Derivatives

* From 12 November 2026, `POST /transfer` can move funds between any Futures wallet and your Kraken Spot wallet. Pass `spot` as `fromAccount` or `toAccount`. The transfer settles before the response is sent, so there is nothing to poll
* A transfer to or from Spot requires an API key with the withdrawal permission, costs 100 rate-limit units (10 for transfers between Futures wallets) and is only available to accounts linked to a Kraken account. It can fail with `insufficientFunds`, `invalidAmount`, `invalidUnit`, `invalidCurrency` or `transferFailed`
* A transfer between Futures wallets now returns the specific reason it was refused (`invalidAmount`, `invalidCurrency`, `cashAccountTypeNotFound`, `cashAccountTypeAccessForbidden`, `accountNotFound`, `cancelOnly` or `transferFailed`) instead of always `insufficientFunds`
* Added `GET /transfer/assets`, which lists the assets your account can transfer, the minimum and maximum amount for a transfer to or from Spot (`minSpotTransferAmount`, `maxSpotTransferAmount`) and whether MTF accounts can move the asset to Spot (`allowMtfSpotTransfers`). It costs 2 rate-limit units. See [Rate limits](https://docs.kraken.com/exchange/guides/futures/ratelimits.md)
* **DEPRECATED** `POST /withdrawal`. Use `POST /transfer` with `toAccount=spot` instead. Once withdrawals settle as immediate balance transfers, `uid` in the response is the nil UUID `00000000-0000-0000-0000-000000000000`
* **DEPRECATED** `GET /transfers`. It only lists transfers made through the legacy cross-exchange transfer system. Transfers made with `POST /transfer` appear in the account log
* `POST /withdrawal` and `GET /transfers` will be removed on 30 November 2026. Move your integrations to `POST /transfer` before then
* A request refused by the [Maker Protection](https://docs.kraken.com/exchange/guides/futures/maker-protection.md#how-many-orders-you-can-have-held-at-once) concurrent-hold cap (500 requests held at once) now returns its own error: `makerProtectionOrderLimitExceeded` (REST v3), `MAKER_PROTECTION_ORDER_LIMIT_EXCEEDED` (REST v4, market data / SBE) and `EGeneral:Other:MAKER_PROTECTION_ORDER_LIMIT_EXCEEDED` (FIX). It was previously reported as `tooManyOrders` / `TOO_MANY_ORDERS` / `ORDER_LIMIT_EXCEEDED`, which now mean only that you have hit your open-order limit
* `POST /cancelallorders` now returns a `CANCEL` event in `orderEvents` for each trigger order it cancels (`type`, `uid`, `orderTrigger`). `status` stays `noOrdersToCancel` when only trigger orders were cancelled, so read `orderEvents` rather than `status` to see whether anything was cancelled

### 27 October 2026 — Spot REST v1

* Added **Algo Trading** endpoints for TWAP (time-weighted average price) strategies: [`AddStrategy`](https://docs.kraken.com/api-reference/algo-trading/add-strategy), [`CancelStrategy`](https://docs.kraken.com/api-reference/algo-trading/cancel-strategy), [`GetOpenStrategies`](https://docs.kraken.com/api-reference/algo-trading/get-open-strategies), [`QueryStrategies`](https://docs.kraken.com/api-reference/algo-trading/query-strategies) and [`GetClosedStrategies`](https://docs.kraken.com/api-reference/algo-trading/get-closed-strategies)
* A TWAP executes a total `volume` evenly between `starttm` and `expiretm` (minimum horizon 60 seconds) as `market` or `limit` child orders. Child orders are immediate-or-cancel limit orders that do not rest on the book. Completed child orders appear in `ClosedOrders` and trade history, and the strategy endpoints report overall progress
* Strategies are identified by a server-assigned `strategy_id` (prefix `AS`) and move through `pending` → `open` → `closed` / `expired` / `cancelled`
* `GetClosedStrategies` uses cursor-based pagination (`limit`, `cursor`, `next_cursor`). `ofs` and `count` are not supported

### 23 October 2026 — Affiliate REST

* Expanded `GET /affiliate/v1/payout-history` to include sub-affiliate commissions, approved retainers, and approved remediation payouts

### 22 October 2026 — Derivatives

* Announced [Maker Protection](https://docs.kraken.com/exchange/guides/futures/maker-protection.md) Phase 3: 51 further markets added on 29 October 2026 at 08:00 UTC. See the guide for the full list, and read `makerProtectionMillis` on `/instruments` for the live set
* From 29 October 2026 at 08:00 UTC, Maker Protection holds only placements and edits that would take liquidity from the book as they arrive. A limit order or edit that would rest is processed at once, without the delay. See the [Maker Protection guide](https://docs.kraken.com/exchange/guides/futures/maker-protection.md)
* A size reduction in a crossing edit is applied at once; only the reprice waits out the window
* A second edit of an order whose edit is still held is refused with the new error `editAlreadyHeld` (REST v4 `EDIT_ALREADY_HELD`). An edit of an order whose placement is still held is rejected with `orderForEditNotFound`
* In batch orders, each instruction that would take liquidity is held on its own and every other instruction is processed on arrival, wherever it sits in the batch. The window no longer starts at the first liquidity-taking instruction
* Leverage and margin-mode changes are no longer refused while you have orders held. They are checked against your held orders as well as your resting orders and positions
* A cancel of a held order, including your own cancel-all and dead man's switch, is now answered when the hold releases rather than at once. The order is matched as submitted, then the cancel takes whatever would have rested: `cancelled` if anything was left, `notFound` if the order filled whole or could not rest. A held order is no longer converted to immediate-or-cancel. A second cancel of a held order is refused at once with `notFound`. See [Cancelling a held order](https://docs.kraken.com/exchange/guides/futures/maker-protection.md#cancelling-a-held-order)
* A held FOK now cancels your own resting order in its way, as every other released taker does. FOK fillability is measured only against makers it could actually trade, so a FOK that only your own liquidity could complete is refused on arrival. The same applies to an unheld FOK when your self-trade strategy is `CANCEL_MAKER`: it is refused for insufficient liquidity rather than part-filled. See [Self-trade prevention](https://docs.kraken.com/exchange/guides/futures/maker-protection.md#self-trade-prevention)

### 19 October 2026 — Derivatives

* Raised the [Maker Protection](https://docs.kraken.com/exchange/guides/futures/maker-protection.md#how-many-orders-you-can-have-held-at-once) concurrent-hold cap from 250 to 500 requests held at once per member. Requests past the cap are still refused with `tooManyOrders` / `TOO_MANY_ORDERS` / `ORDER_LIMIT_EXCEEDED`

### 6 October 2026 — Spot REST v1

* Added cursor-based pagination (`with_cursor`, `cursor`) to `Ledgers`, with a `cursor.next` response field. `count` is `null` on cursor pages
* The deprecated `ofs` parameter on `Ledgers` is superseded by `with_cursor` and `cursor` and must be absent or `0` when `with_cursor` is `true`

### 1 October 2026 — Derivatives

* Announced [Maker Protection](https://docs.kraken.com/exchange/guides/futures/maker-protection.md) Phase 2: 61 further markets added on 8 October 2026. See the guide for the full list, and read `makerProtectionMillis` on `/instruments` for the live set

### 5 October 2026 — Affiliate REST

* Added `GET /affiliate/v1/cpa-progress` to show each CPA bounty, its status, requirements, exact measurable values, and completion percentage for one referred trader
* Added `GET /affiliate/v1/payout-history` for paginated RevShare, Prop, CPA, and Futures Accelerator payout rows with whole-history totals
* Both endpoints use the existing **Query affiliate participants** API key permission and signed Affiliate REST authentication
* See the [Affiliate guide](https://docs.kraken.com/exchange/guides/affiliate/introduction.md), [Get CPA Progress](https://docs.kraken.com/api-reference/affiliate/get-cpa-progress.md), and [Get Payout History](https://docs.kraken.com/api-reference/affiliate/get-payout-history.md)

### 30 September 2026 — Spot REST v1

* Added `account_id` query parameter to `BalanceEx`, `CreditLines`, `TradeBalance`, `OpenOrders`, `ClosedOrders`, `QueryOrders`, `OrderAmends`, `TradesHistory`, `QueryTrades`, `OpenPositions` and `QueryLedgers` to select a specific wallet account
* Added cursor-based pagination (`with_cursor`, `cursor`) to `TradesHistory`, `ClosedOrders` and `OpenOrders`, with a `cursor.next` response field. `OpenOrders` also accepts `limit`
* **DEPRECATED** the `ofs` parameter on `TradesHistory`, `ClosedOrders` and `Ledgers`
* **DEPRECATED** the `aclass` parameter on `Ledgers`. Use the `{ asset, aclass }` list form of `asset` instead
* **DEPRECATED** the `trades` parameter on `QueryLedgers`
* Added `cl_ord_id` filter to `QueryOrders`, `consolidate_taker` to `OpenOrders` and `ledgers` to `QueryTrades`
* Added `displayvol`, `displayvolremain`, `ext_ord_id`, `link_id` and `reduce_only` to order info in `OpenOrders`, `ClosedOrders` and `QueryOrders`
* Added `ext_exec_id` to trade info in `TradesHistory` and `QueryTrades`
* Added `amount_token` to `QueryLedgers` entries for tokenized assets
* Added `rollover_fees` and `reserve_fees` (the credit line's rollover and reserve rates, in percent per rollover period) to `CreditLines` asset details. The credit limit field is `credit` (previously documented as `credit_limit`), and `available_credit` is not returned
* Documented the consolidated (`consolidation=market`) response of `OpenPositions`

### 17 September 2026 — Affiliate REST

* Added `GET /affiliate/v1/daily-activity` for approved affiliates. The path is on `https://api.kraken.com` (no `/0` prefix) and requires permission to query referrals
* Two request variants: one UTC trade day (`activity_date`), or up to ten known participants over a date range (`iiban`, `start_date`, `end_date`). Dates must be today or one of the previous 89 UTC days
* The response is the object itself (no `{ "error", "result" }` envelope). Day-wide `totals` include activity from people who have not opted out; activity from people who opted out may be returned separately under `opted_out`
* See the [Affiliate guide](https://docs.kraken.com/exchange/guides/affiliate/introduction.md) and [Get Daily Activity](https://docs.kraken.com/api-reference/affiliate/get-daily-activity.md)

### 8 September 2026 — Spot REST v1

* **DEPRECATED** the `fees` and `fees_maker` fields on the `AssetPairs` response. Both now always return an empty array (`[]`) for every pair
* The fields are not removed. They remain present in the response and keep their array type for backwards compatibility, but no longer carry any fee data
* Fee rates and fee schedules should be retrieved from the `GetTradeVolume` endpoint. Set `fee_schedule` to `true` to receive the full per-pair fee schedule in the `schedules` field

### 8 September 2026 — Derivatives

* Announced [Maker Protection](https://docs.kraken.com/exchange/guides/futures/maker-protection.md), live on selected markets from 24 September 2026. Order actions that could take liquidity — any order not marked post-only — are held for a short, fixed window before reaching the matching engine. Post-only placements and all cancellations are never held
* Added `makerProtectionMillis` to the `Instrument` and `InstrumentAuthenticated` responses on `/instruments` and `/trading/instruments`, giving the configured window in milliseconds for each market. Omitted when the market has no Maker Protection configured
* Cancelling inside the window removes a held order's right to rest, not its obligation to trade. The order is released as immediate-or-cancel at its original expiry and reports `iocWouldNotExecute` (`IOC_WOULD_ENTER_BOOK` on market data) if it cannot trade; the cancel itself is acknowledged as `cancelled`
* Cancelling while an amend is held is acknowledged without cancelling the target order. At release the amendment reprices that same order and gives up its right to rest, keeping its order ID, client order ID and order group
* `cancelallorders` leaves the targets of claimed amends resting, so a sweep can deliberately spare an order. `cancelallordersafter` and admin cancel-alls purge held orders outright
* An order released from a hold cancels a resting order of your own that it would match, overriding the account's self-trade strategy, and reports `CANCELLED_BY_SELF_TRADE` on the cancelled maker. FOK orders and RFQ are unaffected
* An edit the engine refuses by cancelling the order is reported as a reject on the FIX trading channel. On the v4 API, a converted amend that part-fills and is then refused reports `REJECTED_AFTER_EXECUTION`
* Available for testing in the client UAT environment from 27 August 2026

### 1 September 2026

Scheduled maintenance and unplanned incident advisories are now surfaced across all Spot API protocols, so clients can wind down activity ahead of a maintenance window and understand why the engine is in a restricted state.

* Announced upcoming maintenance status visibility
* Advisories are additive on every protocol. Clients that do not read the new fields are unaffected, and the existing system status value continues to be driven by the trading engine — an advisory explains why a state is happening or coming, it does not dictate engine state
* Scheduled advisories carry a `phase` derived from the time remaining: `announced`, `reminder_24h`, `approaching_30m`, `imminent_5m`, `final_warning_30s`
* Emergency advisories relay the status page incident state 1:1: `investigating`, `identified`, `monitoring`. They are cleared at `resolved` and carry no order guidance — derive it from `incident_status`, `next_steps` and the system status value
* Affected surfaces are named with the tokens `spot_ws`, `spot_rest`, `spot_fix`, `spot_trading`, `futures_ws`, `futures_rest`, `futures_fix`, `futures_trading` and `all`

**WS v2**

* Added `upcoming_maintenance` object to the `status` channel `data[]`. Present when a trading-relevant scheduled event is within 72 hours, `null` otherwise, and cleared once the window starts. Carries `event_id`, `expected_start_utc`, `expected_end_utc`, `time_to_start_s`, `phase`, `affected_services`, `order_submission`, `recommended_action` and `cancel_before_utc`
* Added `emergency` object to the same `status` channel messages. Present while a status page incident is unresolved. Carries `event_id`, `incident_status`, `impact`, `affected_services`, `started_at_utc`, `next_steps` and `source_url`
* `next_steps` entries carry `applies_to`, `type` (one of `expected_restart`, `expected_cancel_only`, `expected_post_only`, `expected_online`) and `expected_at_utc`, ordered by `expected_at_utc` ascending. The array is empty when no forecast has been published
* `time_to_start_s` is refreshed on a 10-second push cadence during the approach phases
* Existing `system` field is unchanged

**WS v1**

* Added `upcoming_maintenance` and `emergency` objects to the `systemStatus` message, matching the WS v2 `status` channel field for field
* Existing `status` field is unchanged

**REST v1**

* Added `upcoming_maintenance` and `emergency` arrays to the `SystemStatus` response. `upcoming_maintenance` carries scheduled events within the next 72 hours, ordered by `expected_start_utc` ascending; `emergency` carries unresolved incidents. Both are empty or absent when no advisory is active, and the existing `status` and `timestamp` fields are unchanged
* Each `upcoming_maintenance` entry carries `event_id`, `title`, `expected_start_utc`, `expected_end_utc`, `time_to_start_s`, `phase`, `affected_services`, `order_submission`, `recommended_action`, `cancel_before_utc` and `source_url`
* Each `emergency` entry carries `event_id`, `title`, `incident_status`, `impact`, `affected_services`, `started_at_utc`, `next_steps` and `source_url`
* Added `MaintenanceSchedule` endpoint, returning `events` — all scheduled maintenance in the next 7 days, ordered by `expected_start_utc` ascending. Emergency incidents are not scheduled and do not appear here
* `cancel_before_utc` is `expected_start_utc` minus 5 minutes while an event is scheduled, and absent otherwise
* `time_to_start_s` is evaluated when the response is served. Responses are cacheable, so derive live countdowns from `expected_start_utc` rather than re-reading the field

**FIX v1**

* Added Tag `5200` (`KrakenIncludeAdvisories`) to `TradingSessionStatusRequest` (`35=g`) to opt in to advisories. Defaults to `N`; unsubscribe with `SubscriptionRequestType (263)` = `2`. Advisories are never auto-emitted on Logon
* Added News (`35=B`) advisory messages, sent once per active advisory on subscription and again on every subsequent phase transition. Documented under API Reference → Unified FIX → News
* News reuses the native FIX 4.4 fields `OrigTime (42)`, `Urgency (61)` — `0` for maintenance, `1` for emergency — `Headline (148)`, `URLLink (149)`, `ValidUntilTime (62)`, and the standard `NoLinesOfText` group form (`33=1` with `58`)
* Added the FIX 5.0 News fields `NewsID (1472)`, `NewsCategory (1473)` — always `3` (Technical News) — `NewsRefID (1476)` and `NewsRefType (1477)`. Phase transitions emit a fresh `NewsID` with `NewsRefID` pointing at the previous message and `NewsRefType` = `0` (Replacement), letting clients correlate updates for a single event
* Added Kraken Tags `5203` (`KrakenEventPhase`), `5204` (`KrakenAffectedServices`), `5205` (`KrakenExpectedStartUTC`), `5206` (`KrakenExpectedEndUTC`), `5207` (`KrakenCancelBeforeUTC`), `5208` (`KrakenRecommendedAction`), `5209` (`KrakenOrderSubmission`), `5210` (`KrakenTimeToStartSec`), `5211` (`KrakenNextStepType`), `5212` (`KrakenNextStepAtUTC`) and `5213` (`KrakenNextStepAppliesTo`)
* Broadcast is scoped per gateway: Spot gateways emit News when `5204` includes `spot_fix`. Cross-product events are broadcast on both Spot and Derivatives gateways with the same `NewsID`, so clients connected to both should deduplicate on `NewsID`. Tag `5204` always carries the full list
* `5210` (`KrakenTimeToStartSec`) is computed once per transition rather than pushed on a timer — derive a live countdown from `5205`
* `URLLink (149)` is currently populated on emergency advisories only; scheduled maintenance advisories will carry it in a follow-up release

### 20 August 2026 — Derivatives REST v1

* Announced upcoming off-book risk preferences, available from 27 August 2026, 07:00 UTC
* Added `/rfq-assignment/max-leverage` endpoints (`GET`, `PUT`, `DELETE`) to read, set and clear an account-level maximum leverage cap applied to off-book fills — liquidation assignments and RFQ offer fills. Book (maker/taker) orders are unaffected; master accounts only
* Added `minimumProfitabilityPerAssignmentLongBps` and `minimumProfitabilityPerAssignmentShortBps` parameters to `/assignmentprogram/add` and to the assignment participant response, setting the minimum profitability per assignment in integer basis points. Participants with a lower minimum receive assignments first

### 19 August 2026 — Spot REST v1

* Added `ListWalletAccounts` endpoint to list wallet accounts associated with the authenticated user
* Added `account_id` query parameter to `Balance` and `Ledgers` to select a specific wallet account

### 14 July 2026 — Spot REST v1

* Added `pair` request parameter to `TradesHistory` to filter results to a single trading pair
* Added `aclass` request parameter to `TradesHistory` to set the asset class of the `pair` filter (defaults to `forex`)
* Added `limit` request parameter to `TradesHistory` to set the number of trades returned per page (`1`–`100`, defaults to `50`)

### 3 July 2026 — Spot FIX v1

* Added Tag `5052` (`MDPricePrecision`) to the Instrument List (`35=y`) response. Specifies the price decimal precision used on market data feeds, which may be greater than `PricePrecision (2349)` for rebased xStocks pairs

### 22 June 2026 — Derivatives REST v1

* **DEPRECATED** the Futures `Fee Schedules` endpoints and related fields (`feeScheduleUid`, `FeeSchedule`, `FeeScheduleVolumes`, `FeeTier`). Fee calculation for Futures trades has been migrated to a centralised Kraken fee service — use the Spot `GetTradeVolume` endpoint to determine the fee rate applied to your trades

### 16 June 2026 — Spot REST v1

* `TradeVolume` `pair` parameter now also accepts a list of `{ asset, aclass }` objects, enabling fee queries for non-forex classes (such as `derivatives` and `equity_pair`)
* Added `fee_schedule` request parameter to `TradeVolume` to return the full per-pair fee schedule in the new `schedules` response field

### 18 May 2026 — Derivatives REST v1

* Added `unknown` value to multiple enums (order `direction`, `orderType`, `triggerSignal`, `triggerSide`, trailing-stop / max-deviation `unit`, and `HistoricalPositionUpdateElement` fields `positionChange`, `tradeType`, `updateReason`) as a fallback when the source value cannot be decoded

### 12 May 2026 — Spot REST v1

* Added `FOK` (fill-or-kill) value to `timeinforce` parameter on `AddOrder` and `AddOrderBatch` endpoints

### 7 May 2026 — Spot REST v1

* Added `broker` request body parameter to `AddOrder` and `AddOrderBatch` for qualified partners in Kraken's API Partner Program

### 30 April 2026 — Spot REST v1

* Added `execution_venue` query parameter to `AssetPairs` endpoint (filter by `international` or `bitnomial_exchange`)

### 28 April 2026 — Spot WS v2

* Added `execution_venue` subscription parameter to the `instrument` channel (one of `international`, `bitnomial-exchange`; defaults to `international`)

### 27 April 2026 — Spot REST v1

* Added `execution_venue` field to `AssetPairs` response (one of `international`, `bitnomial_exchange`)

### 11 March 2026 — Spot REST v1

* Added `GetApiKeyInfo` endpoint to retrieve API key configuration and usage

***

## 2025

### 15 December 2025 — Spot REST v1

* Added `Level3` endpoint for individual order-level (L3) order book data
* Added `GroupedBook` endpoint for aggregated order book data over configurable tick size

### 15 December 2025 — General Docs

* Migrated blog content to guides section
* Refreshed navigation menus for improved discoverability

### 2 December 2025 — Spot WS v2

* L3 WebSocket endpoint URL changed from `wss://ws-auth.kraken.com/v2` to `wss://ws-l3.kraken.com/v2`

### 13 November 2025 — Spot ALL

* Deprecated `.F` asset values returned by `Balance` and `BalanceEx` endpoints

### 18 September 2025 — Spot ALL

* Deprecated `no_mpp` parameter on `AddOrder`, `EditOrder`, and `AddOrderBatch`

### 5 September 2025 — Spot REST v1

* Added `asset_class` filter parameter to `Ticker` endpoint

### 15 August 2025 — Spot REST v1

* Added `asset_class` parameter to market data and trading endpoints for xStocks

### 15 August 2025 — Spot WS v2

* Added `rebased` parameter to `executions` and `balances` requests to specify xStocks mode

### 15 August 2025 — Spot WS v1

* Added `rebased` parameter to `openOrders` and `ownTrades` requests to specify xStocks mode

### 15 August 2025 — Spot FIX v1

* Added Tag `5051` to Logon requests to specify xStocks mode
* Added `TS` SecurityType to `InstrumentListRequest`

### 4 August 2025 — Derivatives REST v1

* Announced upcoming authentication breaking change effective October 1st, 2025

### 28 July 2025 — Spot REST v1

* Added documentation for `CreditLines` endpoint

### 24 June 2025 — Spot REST v1

* Fixed error message formatting on Account Data endpoints

### 29 May 2025 — Spot FIX v1

* Added Tag 78 and 79 for Subaccount Management for Broker accounts

### 28 May 2025 — Spot REST v1

* Moved OTC endpoints to Institutional menu section

### 28 May 2025 — Spot WS v2

* Added `user` field to `executions` and `balances` channels to help identify the account

### 8 May 2025 — Spot WS v1 (v1.9.6)

* Added `stp_type` to `addOrder` providing self trade prevention options

### 8 May 2025 — Spot WS v2 (v2.0.10)

* Added `timestamp` field to `level3` channel to help clients track market data sequence

### 8 March 2025 — Derivatives FIX v1

* FIX now supports futures trading

***

## 2024

### 28 September 2024 — Spot FIX v1

* Added Tag `5050` `LiquidityInd` in `ExecutionReport`

### 27 September 2024 — Spot REST v1

* Added `AmendOrder` endpoint to modify order parameters
* Added `OrderAmends` endpoint to retrieve an audit trail of amend transactions
* Added `amended` flag to `OpenOrders` and `ClosedOrders` endpoints to identify amended orders

### 27 September 2024 — Spot WS v1 (v1.9.5)

* Added `amendOrder` endpoint to modify order parameters
* Added `amended` flag to `openOrders` channel to identify amended orders

### 27 September 2024 — Spot WS v2 (v2.0.9)

* Added `amend_order` endpoint to modify order parameters
* Added `amended` exec\_type to `executions` channel to identify amended orders

### 27 September 2024 — Spot FIX v1

* Added order cancel-replace request message `MsgType=G` to modify order parameters

### 5 September 2024 — Spot REST v1

* Added `cl_ord_id` parameter to query endpoints: `ClosedOrders`, `OpenOrders`

### 22 August 2024 — Spot WS v2 (v2.0.8)

* Added `liquidated` flag to `executions` channel to show when an order has been liquidated
* Added subscription rate limits to the `level3` market data feed

### 1 August 2024 — Spot WS v2 (v2.0.7)

* `snap_trades` parameter now defaults to `false`
* Added `ext_ord_id` field to `openOrders` and `executions`
* Added `ext_exec_id` field to `ownTrades` and `executions`
* Added `margin_borrow` flag to `ownTrades` and `executions`

### 27 June 2024 — Spot WS v2 (v2.0.6)

* Deprecated `snapshot` and `snapshot_trades` in `executions` channel

### 24 June 2024 — Spot REST v1

* Added `cl_ord_id` parameter to order endpoints: `AddOrder`, `CancelOrder`

### 30 May 2024 — Spot WS v2 (v2.0.5)

* Modified `balances` channel to always include wallet breakdown and cumulative balance
* Added `asset_class` to `balances` channel for future expansion

### 23 May 2024 — Spot FIX v1.8

* Changed `ClOrdId` (Tag 11) and `OrigClOrdId` format and validation

### 21 May 2024 — Spot REST v1

* Added `country_code` parameter to `AssetPairs`

### 16 May 2024 — Spot WS v2 (v2.0.4)

* Added `cl_ord_id` and `sender_sub_id` client order identifiers
* Clarified that GTD expire time is one month

### 16 May 2024 — Spot WS v1 (v1.9.3)

* Added `cl_ord_id` and `sender_sub_id` client order identifiers
* Added `margin` indicator for leveraged orders

### 14 May 2024 — Spot REST v1

* Added `cl_ord_id` and `sender_sub_id` identifiers to order queries
* Added `margin` indicator to leveraged orders

### 18 April 2024 — Spot FIX v1.7

* Added `iceberg` and `trailing-stop` order types to FIX

### 1 March 2024 — Spot REST v1

* Removed `Staking` section, deprecated and no longer supported

### 1 March 2024 — Spot WS v2 (v2.0.3)

* Added `event_trigger` parameter to the `ticker` channel

### 15 February 2024 — Spot WS v2 (v2.0.2)

* Added `cash_order_qty` to the `executions` channel

### 1 February 2024 — Spot REST v1

* Added `maker` and `ledgers` fields to `TradesHistory` and `QueryTrades`

### 10 January 2024 — Spot WS v1 (v1.9.2)

* Narrowed range of valid offsets (from current time) for the `deadline` parameter

### 1 January 2024 — Spot REST v1

* Removed support for POST requests to all public endpoints
* Added migration notes to `Balance` and `Ledger` endpoints

***

## 2023

### 14 December 2023 — Spot WS v2 (v2.0.1)

* Added `trailing-stop` and `trailing-stop-limit` order types
* Added trigger protection during connectivity issues with index providers

### 14 December 2023 — Spot REST v1

* Added `trailing-stop` and `trailing-stop-limit` order types

### 7 December 2023 — Spot WS v2 (v2.0.0)

* WebSocket v2 taken out of beta
* Added `status` and `restated` values to `exec_type`
* Added support for native amends in `level3` channel
* Enabled `level3` channel in all environments
* Added support for new ledger types in `balances` channel
* Enabled `balances` channel in all environments
* Deprecated `cancel_reason` in `executions` channel — use `reason` instead

### 1 November 2023 — Spot REST v1

* Added `WithdrawMethods` and `WithdrawAddresses` endpoints
* Added `start`, `end`, `cursor`, and `limit` parameters to `WithdrawStatus`

### 30 October 2023 — Spot FIX v1.0.0

* Added Tag `5041` `ChecksumOrderBook` parameter

### 1 October 2023 — Spot REST v1

* Added `max_fee` parameter to `Withdraw` and minimum field in response

### 1 September 2023 — Spot REST v1

* Added `start`, `end`, `cursor`, and `limit` parameters to `DepositStatus`

### 1 August 2023 — Spot REST v1

* Added earn / balance service documentation

### 14 July 2023 — Spot WS v2 (beta)

* Added support for `iceberg` order type

### 1 July 2023 — Spot REST v1

* Added private `BalanceEx` documentation

### 1 June 2023 — Spot FIX v1.0.0

* First version of FIX API in production beta

### 1 June 2023 — Spot REST v1

* Added `amount` parameter to `DepositAddresses`
* Added `count` parameter to `Trades`

### 1 May 2023 — Spot REST v1

* Added `address` parameter to `Withdraw`
* Added `since` parameter to `Spread`

### 3 April 2023 — Spot WS v2 (beta)

* `OHLC` channel: added `interval` field to request parameters

### 22 March 2023 — Spot WS v2 (beta)

* Edit Order request: added `limit_price` field, deprecated `price` field
* `executions` channel: added `margin` field to order details
* `instrument` channel: added additional support for `price_precision`

### 15 March 2023 — Spot WS v2 (beta)

* `executions` channel: added `last_qty` and `last_price` fields to trade events
* OHLC channel: added `interval` and `interval_begin` fields
* Corrected default `time_in_force` settings

### 2 March 2023 — Spot WS v1 (v1.9.1)

* Added `contingent` field on private open order feed
* Enabled fast reconnect on WebSockets following trading engine maintenance

### 1 March 2023 — Spot REST v1

* Added `originators` parameter to `DepositStatus`

### 1 February 2023 — Spot REST v1

* Added long and short position limits to `AssetPairs`
* Specified minimum and maximum number of txids and userrefs
* Specified maximum number of responses for `DepositStatus` and `WithdrawStatus`
* Added note to use `%2b` instead of `+` for URL encoding

### 1 January 2023 — Spot REST v1

* Removed requirement for `asset` in `DepositStatus` and `WithdrawStatus`
* Documented `reduce_only` parameter
* Added `consolidate_taker` to `TradesHistory`, `ClosedOrders`, and `QueryOrders`
* Added Subaccounts section
* Added `trade_id` to private `TradesHistory`

***

## 2022

### 1 December 2022 — Spot REST v1

* Fixed pair parameter restriction on `TradeVolume`
* `EditOrder` now allowed on margin orders

### 28 November 2022 — Spot WS v2 (beta)

* Corrected several details in the `executions` channel

### 22 November 2022 — Spot WS v2 (beta)

* Removed internal version from the About section
* Multiple formatting and data corrections

### 1 November 2022 — Spot REST v1

* Added `tick_size` and `status` parameters to `AssetPairs`
* Added `status` and `collateral_value` to `Assets`
* Added `trade_id` to public `Trades`

### 1 October 2022 — Spot REST v1

* Documented `uv` (unexecuted value) field in `TradeBalance`
* Added `costmin` trading parameter to `AssetPairs`
* Ticker wildcard support — `pair` no longer required

### 1 September 2022 — Spot REST v1

* `AddOrder`, `EditOrder`, and `AddOrderBatch` now support iceberg orders

### 1 July 2022 — Spot REST v1

* Added support for restricting API keys to specified IP address(es)

### 1 June 2022 — Spot REST v1

* Added custom self trade prevention options

### 1 May 2022 — Spot REST v1

* New `AddOrderBatch` endpoint to send multiple new orders
* New `CancelOrderBatch` endpoint to cancel multiple open orders

### 22 March 2022 — Spot WS v1 (v1.9.0)

* Added support for `editOrder`

### 1 March 2022 — Spot REST v1

* New `EditOrder` endpoint to edit volume and price on open orders

***

## 2021

### 1 December 2021 — Spot REST v1

* Added `trigger` optional parameter to `AddOrder`

### 31 March 2021 — Spot WS v1 (v1.8.3)

* Added `deadline` support to `addOrder`

### 25 February 2021 — Spot WS v1 (v1.8.0)

* Added `timeinforce` and Immediate-or-Cancel (IOC) support

### 4 February 2021 — Spot WS v1 (v1.7.1)

* Changed close code to 1008 (Policy Violation) from 1013
* Added policy rule for maximum rate of subscriptions
* Added new generic error type with optional internal error codes
* Improved public market data snapshot performance

### 30 January 2021 — Spot WS v1 (v1.7.0)

* Added `userref` field to `openOrders` and `ownTrades` update messages

### 13 January 2021 — Spot WS v1 (v1.6.1)

* Added Dead Man's Switch (`cancelAllOrdersAfter`) REST endpoint
* Fixed intermittent public data WebSocket feed latency

***

## 2020

### 21 December 2020 — Spot WS v1 (v1.6.0)

* Introduced `post_only` trading mode for maintenance procedure

### 5 December 2020 — Spot WS v1 (v1.5.0)

* Added optional `ratecounter` argument for `openOrders` subscription
* Added `maxratecount` and current `ratecount` reporting
* Added `cancel_only` trading mode
* Relaxed slow-consumer constraint on WebSocket connections
* Maintained private WebSocket connections during maintenance
* Improved public market data snapshot/stream synchronisation

### 18 November 2020 — Spot WS v1 (v1.4.1)

* Added `cancelAll` REST endpoint

### 2 November 2020 — Spot WS v1 (v1.4.0)

* Added `cancelAll` trading request functionality
* Performance upgrade to `cancelOrder` request handling
* Improved messages and close codes when closing WebSocket connections
* Fixed incorrect error for `addOrder` with invalid pair

### 27 October 2020 — Spot WS v1 (v1.3.0)

* Added sequence numbers on private feeds (`openOrders`, `ownTrades`)

### 12 October 2020 — Spot WS v1 (v1.2.1)

* Eliminated trading rate limit penalty for filled orders
* Performance improvement for REST real-time and historical market data
* Rejected `market` conditional close orders
* Fixed intermittent bug affecting Ticker REST endpoint

### 31 August 2020 — Spot WS v1 (v1.2.0)

* Added `cancel_reason` to `openOrders` stream
* Added optional `snapshot` parameter for `ownTrades` feed

### 22 June 2020 — Spot WS v1 (v1.1.0)

* Added order book `checksum`

### 18 February 2020 — Spot WS v1 (v1.0.7)

* Added `addOrder` and `cancelOrder` endpoints

***

## 2019

### 1 October 2019 — Spot WS v1 (v1.0.6)

* Introduced `openOrders` and `ownTrades` channels

### 4 February 2019 — Spot WS v1 (v1.0.5)

* Fixed publishing of deleted price levels

### 23 January 2019 — Spot WS v1 (v1.0.4)

* Added `connectionID` field to `systemStatus` message

### 18 January 2019 — Spot WS v1 (v1.0.3)

* Added open prices on `ohlc` including 24-hour values
* Increased timestamp precision to microseconds
* Updated sandbox URL

***

## 2018

### 24 December 2018 — Spot WS v1 (v1.0.2)

* Changed timestamp field to string type

### 7 December 2018 — Spot WS v1 (v1.0.1)

* Released WebSocket public market data sandbox v0.0.4
* Changed timestamp precision to milliseconds

### 28 November 2018 — Spot WS v1 (v1.0.0)

* Released WebSocket public market data sandbox v0.0.3
