---
exchange: deribit
source_url: https://docs.deribit.com/changelogs/starbase
api_type: Changelog
updated_at: 2026-11-26 19:02:01.867595
---

# Starbase API Changelog

> Release notes for the Deribit Starbase binary and REST APIs covering new messages, protocol changes, performance updates, and compatibility notes.

**Starbase Testnet Update 24.11.2026**

> [!NOTE]
>
> Available on testnet from 24 November 2026. The production release date will be announced in this changelog. Production is not affected until then.

## API Changes

### Order Entry

**Multi-part fill messages.** Order entry messages that carry fills are now kept under a maximum message size of 60,000 bytes. When the fills of an aggressing order, amend, mass quote or speed-bump release do not fit in one message, the first message carries the final order or quote state and as many fills as fit. The remaining fills follow immediately in new continuation messages. This works like the existing `isLastMessage` flag on `OrdersCanceled` for mass cancels.

This is a preventative change: no order on production has exceeded the message size limit so far.

* `NewOrderResponse` (200), `AmendOrderResponse` (210) and `OrderPlaced` (312) continue in the new `OrderFillsContinued` (316), matched by `orderId`
* `MassQuoteResponse` (230) and `MassQuoteOrdersPlaced` (314) continue in the new `MassQuoteFillsContinued` (318), matched by `mmpGroupId` (and `correlationId` after a `MassQuoteResponse`)
* `messageFlags.isLastMessage` is set on the last message of the response. A response that fits in one message has it set on that message
* A fill and its legs are always in the same message
* Resting-order fills in `OrderFilled` (300) are unchanged: a large maker fill event is sent as several self-contained `OrderFilled` messages, without a flag

> [!WARNING]
>
> **Move to schema version `24`.** Sessions below version `24` do not receive the continuation messages. If a response overflows, they receive only the first message: its order state (`totalFilled`, `status`) covers every fill, but its fills groups hold only the fills that fit. Trading is not affected otherwise. Deribit recommends that all clients move to version `24` as soon as possible.

### Schema

The order entry SBE schema has been updated to version `24` (`semanticVersion` remains `1.5`). The update is available as the [testnet](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-order-api-testnet.xml) order entry XML. All changes are additive.

* `NewOrderResponse` (200), `AmendOrderResponse` (210), `MassQuoteResponse` (230), `OrderPlaced` (312) and `MassQuoteOrdersPlaced` (314): new `messageFlags` field (`MultiPartEventFlags`, `uint8`, bit 0 `isLastMessage`) at the end of the root block, before the repeating groups
* New message `OrderFillsContinued` (316)
* New message `MassQuoteFillsContinued` (318)

Schema version `23` (the `SPEED_BUMPED` reject reason) is unchanged and is released to production on 26 November 2026.

See [Multi-part fill messages](https://docs.deribit.com/starbase/upcoming/binary-api-reference.md#multi-part-fill-messages), [OrderFillsContinued (316)](https://docs.deribit.com/starbase/upcoming/unsolicited-events.md#orderfillscontinued-316) and [MassQuoteFillsContinued (318)](https://docs.deribit.com/starbase/upcoming/unsolicited-events.md#massquotefillscontinued-318).

**Starbase Update 26.11.2026**

> [!NOTE]
>
> Available on testnet from 20 November 2026. Production release is planned for 26 November 2026.

## API Changes

### Order Entry

> [!WARNING]
>
> **Breaking change: speed-bumped orders and quotes can no longer be amended.** Clients that amend or re-quote orders while they are queued in the speed bump must update their handling.

**Amends of speed-bumped orders are rejected.** An `AmendOrderRequest` for an order that is queued in the [speed bump](https://docs.deribit.com/starbase/upcoming/speed-bumps.md) (`orderState = 4`) is rejected with the new reason `SPEED_BUMPED` (`34`). This applies to any change of price, quantity or both, including a quantity reduction and a re-price to a passive price. The order is not changed: it keeps its place in the speed bump queue and its release time, and enters the book unchanged when the speed bump elapses.

* An amend sent while the order is still awaiting its pre-trade risk check is also rejected if the order is speed-bumped by the time the amend is processed
* Cancelling a speed-bumped order is unchanged: the order is converted to IOC and can still trade at release
* Once the speed bump has elapsed, the order can be amended as before

Previously, an amend of a speed-bumped order was applied: an aggressing amend restarted the speed bump and a passive amend added the order to the book immediately.

### Mass Quotes

Each quote side is handled separately. Changes to a side that is not speed-bumped are processed as before.

* **Changing a speed-bumped side.** If a `MassQuoteRequest` changes the price or quantity of a speed-bumped quote side, including a quantity reduction at the same price, that side is reported with `bidStatus` / `askStatus` = `UNMODIFIED` and `bidRejectReason` / `askRejectReason` = `SPEED_BUMPED` (`34`). The queued quote is left unchanged. Previously, the queued quote was replaced
* **Re-sending a speed-bumped side unchanged** returns `UNMODIFIED` with no reject reason (unchanged)
* **Quantity `0` on a speed-bumped side** converts it to IOC, like a cancel (unchanged)
* **Crossed or invalid mass quote.** If the request fails validation (bid at or above ask, or an invalid quantity) while one side is speed-bumped, the speed-bumped side is converted to IOC and reported with status `SPEED_BUMPED` (`8`) and no reject reason. It can still trade at its existing price when the speed bump elapses. The other side is rejected and its resting quote cancelled, as before. Previously, the speed-bumped side was removed
* **New side at or through a speed-bumped side.** If one side is speed-bumped (for example an ask at `100`) and the request moves the other side to or through its price (for example a bid at `101` and an ask at `102`), the speed-bumped side is reported `UNMODIFIED` with reject reason `SPEED_BUMPED` and stays at its old price. The other side is processed normally and can rest at or through that price. On release, the speed-bumped side matches like a new order, and self-match prevention cancels it if it would trade against your own quote

### Market Maker Protection

When a mass quote trips MMP, speed-bumped quote sides in that same request are converted to IOC and reported with status `SPEED_BUMPED` (`8`). They can still trade when the speed bump elapses. This covers sides that were already speed-bumped and sides newly speed-bumped earlier in the same request. Previously, these sides were removed. Speed-bumped quotes that are not in the triggering request are converted to IOC, as before. See [MMP and speed bumps](https://docs.deribit.com/starbase/upcoming/speed-bumps.md#mmp-and-speed-bumps).

### Schema

The order entry SBE schema has been updated to version `23` (`semanticVersion` remains `1.5`). The update is available as the [testnet](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-order-api-testnet.xml) order entry XML.

* `OrderRejectReason`: new reason code `SPEED_BUMPED` (`34`), used in `AmendOrderReject` and in `bidRejectReason` / `askRejectReason` of `MassQuoteResponse`
* `MassQuoteResponse` (230): new combination of `bidStatus` / `askStatus` = `UNMODIFIED` with reject reason `SPEED_BUMPED` for a rejected change to a speed-bumped side

The reject is sent regardless of the session's schema version. A decoder generated from schema version `22` or earlier does not know value `34` and decodes it as an unknown value (`SBE_UNKNOWN` in generated Java codecs). Update your codecs to version `23` to identify the reason.

### JSON-RPC API

The same rule applies to orders and quotes submitted through the JSON-RPC API: [private/edit](https://docs.deribit.com/api-reference/trading/private-edit.md) and [private/edit\_by\_label](https://docs.deribit.com/api-reference/trading/private-edit_by_label.md) on a speed-bumped order are rejected, and in [private/mass\_quote](https://docs.deribit.com/api-reference/trading/private-mass_quote.md) a change to a speed-bumped quote is not applied. See the [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md).

See [Amending speed-bumped orders and quotes](https://docs.deribit.com/starbase/upcoming/speed-bumps.md#amending-speed-bumped-orders-and-quotes), [Amending an Order](https://docs.deribit.com/starbase/upcoming/amending-order.md), [Mass Quotes](https://docs.deribit.com/starbase/upcoming/mass-quotes.md) and [Rejection Reason Codes](https://docs.deribit.com/starbase/upcoming/binary-api-reference.md#rejection-reason-codes).

**Starbase Update 18.11.2026**

## API Changes

### Market Data

**`sortOrderId` assigned when an order rests.** The `sortOrderId` on `Buy Put` (20) and `Sell Put` (21) is now assigned when the order goes on the book, after any applicable pre-trade risk check or speed bump, instead of when the matching engine accepts it. This applies to all resting orders. A newly resting order always joins the back of its price level, so the order of `Buy Put`/`Sell Put` messages at a price level, `sortOrderId` order and fill order now agree.

Previously, an order waiting on its pre-trade risk check could rest after a later order that skipped the check (for example an MMP order), yet take a place ahead of it in the queue.

* `sortOrderId` values are still strictly increasing, but no longer consecutive. Consecutive resting orders typically differ by `2` (e.g. `101`, `103`). Do not use `sortOrderId` gaps to detect missed messages; use the packet `sequenceNum`
* An order's `sortOrderId` never changes once it appears in market data
* `transactTime` in the message header of a `Buy Put` or `Sell Put` is the time the order went on the book. It is not an indicator of queue priority

Always sort each price level by `sortOrderId`, not by message sequence or `transactTime`. The market data SBE schema is unchanged.

See [Queue priority](https://docs.deribit.com/starbase/order-book-maintenance.md#queue-priority) and [Best Practices Summary](https://docs.deribit.com/starbase/connectivity-best-practices.md#best-practices-summary).

**Starbase Update 12.11.2026**

## API Changes

### Order Entry

**Reject reason for open order size limits.** A new order or a replace that would breach a Portfolio Margin open order size limit is now rejected with `ORDER_SIZE_LIMIT_EXCEEDED` (`28`) instead of `POSITION_LIMIT_EXCEEDED` (`27`). These limits cap the total size of resting orders, not position size. This applies to:

* `pm_max_future_open_order_size`: maximum total size of future open orders per side
* `pm_max_option_open_contracts`: maximum total size of option open contracts per side

Position size limits (such as `sm_max_future_position_size`) still reject with `POSITION_LIMIT_EXCEEDED`. Open order count limits are unchanged. The SBE order entry schema is unchanged: both reason codes already exist. Clients that handle `POSITION_LIMIT_EXCEEDED` for these limits should also handle `ORDER_SIZE_LIMIT_EXCEEDED`.

See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes) and [Position Limits](https://docs.deribit.com/starbase/portfolio-management.md#position-limits).

**Starbase Update 10.11.2026**

> [!NOTE]
>
> This release was postponed from 5 November 2026 to 10 November 2026.

## API Changes

### Self-Match Prevention

**SMP across Members.** Deribit can now extend [Self-Match Prevention](https://docs.deribit.com/starbase/smp.md) across all Members of the same main account. Until now, SMP never triggered between orders from different Members. The setting is enabled by Deribit on request and applies to the main account and all of its subaccounts. It is mainly relevant to accounts with several Members, such as brokers with multi-Member access.

When the setting is enabled:

* If self-match prevention is enabled on the account, the SBE gateway sets the SMP token of every order and mass quote to the main portfolio ID, ignoring `selfMatchPreventionId` in the request. Orders submitted via the WebSocket API, FIX API or UI carry the same token. Orders from any Member under the main account do not match each other
* If self-matching is allowed on the account, SMP stays opt-in: orders with the same non-null SMP token do not match each other across all Members of the main account

The SBE order entry schema is unchanged. Classic JSON-RPC [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) and [`private/get_account_summaries`](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries) return a new `self_trading_extended_across_members` field when `extended` is `true`.

**SMP token for orders from other systems.** With self-match prevention extended to subaccounts, orders submitted via the WebSocket API, FIX API or UI now carry the Member ID as their SMP token instead of the main portfolio ID. The SBE gateway already uses the Member ID for that setting, so these orders and SBE orders from the same Member no longer match each other.

See [SMP across Members](https://docs.deribit.com/starbase/smp.md#smp-across-members) and [Orders from different systems](https://docs.deribit.com/starbase/smp.md#orders-from-different-systems).

### Market Data

**Delayed Deribit Block RFQ trade publication.** The market data SBE schema has been updated to version `2` (`semanticVersion` remains `1.0`). The change is additive and backwards compatible. The new fields are at the end of the message, with no repeating groups. The updated schema is available as the [production](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml) and [testnet](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api-testnet.xml) market data XMLs.

* `BlockTrade` (33): new `padding2` (`int16`) and `executionTimestamp` (`TimestampNanos`, optional) fields at the end of the message. The message body grows from 78 to 88 bytes, and `messageLength` in the message header from `96` to `104`. Clients that use `messageLength` to step to the next message need no change
* `TradeFlags`: new `wasDelayed` choice (bit 3). Set on `BlockTrade` messages for qualifying Block RFQ trades published after a delay. On those prints `executionTimestamp` is the execution time and `transactTime` in the message header is the publication time. On all other Block Trades and Block RFQ trades `wasDelayed` is `0` and `executionTimestamp` is null
* The message header `version` field is `2` on all market data messages

Delayed Block RFQ trades are not published on the incremental channel at execution. The eligibility rules and delay are the same as for the JSON-RPC API; see the [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md).

**Decoding new fields.** Decode market data with the published SBE schema and use `messageLength` in the message header to find the next message. Do not hard-code message sizes. Fields added at the end of a message keep every existing field at its offset, so a decoder built from an older schema reads the known fields and skips the extra bytes.

See [Block Trade](https://docs.deribit.com/starbase/trades.md#block-trade-33) and [Delayed Block RFQ trades](https://docs.deribit.com/starbase/trades.md#delayed-block-rfq-trades).

**Starbase Update 29.10.2026**

## API Changes

### Order Entry

**Staggered weekly sequence reset.** The A and B gateways of each SBE order-entry pair no longer reset at the same moment. A-side gateways (production BTC, ETH, Tier 2, Tier 3 and RWA; testnet BTC and RWA) now run the weekly Saturday sequence reset at approximately **11:55 US Central**. B-side gateways keep **12:00 US Central**. A client connected to both A and B no longer loses every connection at once. The disconnect reason (`SEQUENCE_RESET`) and the reconnect procedure (`resetSeqNum=1`) are unchanged. FIX Drop Copy is unaffected.

See [Weekly sequence reset](https://docs.deribit.com/starbase/session-messages.md#weekly-sequence-reset).

**Opt-in liquidation notifications.** The order entry SBE schema has been updated to version `22` (`semanticVersion` remains `1.5`), on both production and testnet. The change is additive. Sessions that do not opt in see no change.

* `LogonRequest` (1): new optional `liquidationNotifications` field (`Bool`). When set to `1`, the session receives unsolicited liquidation notifications for the logged-on portfolio. A logon that sets it with a `schemaVersion` below `22` is rejected
* `OrderFilled` (300): new `isLiquidation` choice (bit 3) on `FillFlags`. Opted-in sessions receive an unsolicited `OrderFilled` with this flag set for fills of exchange-initiated liquidation orders on their portfolio
* `PositionMoved` (330): new unsolicited message for LSP and ADL position moves, sent to opted-in sessions of both the liquidated portfolio (`role=TAKER`) and the receiving portfolio (`role=MAKER`), with `reason` `LSP` or `ADL`

See [Liquidation notifications](https://docs.deribit.com/starbase/unsolicited-events.md#liquidation-notifications), [PositionMoved](https://docs.deribit.com/starbase/unsolicited-events.md#positionmoved-330) and [LogonRequest](https://docs.deribit.com/starbase/session-messages.md#logonrequest-1).

**Starbase Update 13.10.2026**

## API Changes

### Order Entry

The order entry SBE schema has been updated to version `19` (`semanticVersion` remains `1.5`), on both production and testnet. Both changes are additive.

Schema version `18`:

* `OrderRejectReason`: new reason code `CANCEL_ONLY` (`31`). While global algo cancel-only mode is active, new algo parent submissions are rejected with this reason. Only cancel-only orders can be submitted.

Schema version `19`:

* `NewOrderResponse` (200): new `flags` field (`OrderFlags`, `uint16`) echoing the order flags from the submitted order. Present only when the session has negotiated schema version `19` or later. Sessions negotiated below `19` do not receive this field.

See [NewOrderResponse](https://docs.deribit.com/starbase/placing-new-order.md#neworderresponse-200) and [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes).

**Starbase Update 24.09.2026**

## API Changes

### REST gateway

`GET /api/v2/private/get_starbase_risk_limits` returns the effective per-underlying position limits for the authenticated portfolio. An optional `currency` query parameter selects one underlying. The call is read-only.

Each field is the portfolio override when that field is set, otherwise the currency-pair default. Unset fields are omitted. `-1` means explicitly unlimited. The endpoint is capped at 1 request per minute per portfolio per REST gateway.

`GET /api/v2/private/get_open_orders` is capped at 10 requests per minute per portfolio on each REST gateway. The A and B gateways enforce this cap independently. See [REST Gateway Limits](https://docs.deribit.com/starbase/api-rate-limits.md#rest-gateway-limits).

See [Get Starbase Risk Limits](https://docs.deribit.com/api-reference/portfolio-management/get-starbase-risk-limits.md) and [Portfolio Management](https://docs.deribit.com/starbase/portfolio-management.md#position-limits).

**Starbase Update 22.09.2026**

## API Changes

### Order Entry

The order entry SBE schema has been updated to version `17` (`semanticVersion` remains `1.5`), on both production and testnet. The change is additive and backward-compatible: no message layouts changed, so codecs generated from schema version `16` still decode the feed.

* When another session cancels an order, the session that submitted the order receives an unsolicited [`OrdersCanceled` (310)](https://docs.deribit.com/starbase/unsolicited-events#orderscanceled-310). The session that sent the cancel still receives [`CancelOrderResponse` (220)](https://docs.deribit.com/starbase/cancelling-order#cancelorderresponse-220). The submitting session receives this `OrdersCanceled` when it has negotiated schema version `17` or later. Sessions negotiated below `17` keep the previous routing: `CancelOrderResponse` is delivered to both sessions.

See [Cancelling an Order](https://docs.deribit.com/starbase/cancelling-order.md).

### REST gateway

`GET /api/v2/public/get_instruments` accepts three additional optional filters. Supplied filters are combined:

* `instrument_id`: the numeric instrument id
* `product_group`: Starbase product group (`BTC`, `ETH`, `TIER_2`, `TIER_3`), case-insensitive
* `state`: instrument lifecycle state (`open`, `inactive`, `settlement`, `delivered`, `locked`, `halted`), case-insensitive. These match SBE `InstrumentStatus`

`GET /api/v2/private/get_open_orders` now includes `instrument_id` and `product_group` on each order.

See [List Instruments](https://docs.deribit.com/api-reference/market-data/list-instruments.md) and [Get Open Orders](https://docs.deribit.com/api-reference/trading/get-open-orders.md).

### Market Data

Delivered instruments can be removed from the market-data snapshot cache. `EVICT_DELIVERED_INSTRUMENTS_FROM_MD_SNAPSHOT` ships **off**. This deploy does not change snapshot contents. Eviction runs only after that flag is turned on, and only when `EMIT_MD_INSTRUMENT_STATUS_ONLY` and `EMIT_INDEX_DEFINITION` are also on.

While eviction is active, an instrument that reaches status `DELIVERED` (`3`) is dropped from the snapshot cache and omitted from later snapshot cycles. Joined clients still see the transition on the incremental feed as [`InstrumentStatusUpdate` (16)](https://docs.deribit.com/starbase/reference-data#instrumentstatusupdate-16). The market-data schema `version` / `semanticVersion` remains `1` / `1.0`.

See [Snapshot messages](https://docs.deribit.com/starbase/order-book-maintenance.md#snapshot-messages).

**Starbase Update 16.09.2026**

## API Changes

### Order Entry

A dedicated SBE order-entry gateway pair is now available for RWA instruments. It shares the Tier 3 hosts and uses port `4214`:

| Gateway | Side | Address | Port | Protocol | AWS Port |
| - | - | - | - | - | - |
| sbe-order (RWA) | A | 195.138.37.7 | 4214 | TCP | 34214 |
| sbe-order (RWA) | B | 195.138.37.8 | 4214 | TCP | 44214 |

See [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md).

### FIX Drop Copy

FIX Drop Copy no longer sends cancel reports (`150=4`) for:

* `MassQuoteCancelRequest`
* `MassCancelRequest`
* Cancel on Disconnect (COD)

Single-order cancels via `CancelOrderRequest` still produce a Canceled (`150=4`) Execution Report. For mass cancels and COD, cancelled orders are reported on the originating SBE session as [`OrdersCanceled` (310)](https://docs.deribit.com/starbase/unsolicited-events#orderscanceled-310).

See [ExecutionReport 150=0/4/5](https://docs.deribit.com/starbase/fix-drop-copy-api.md#order-execution-reports).

**Starbase Update 10.09.2026**

## API Changes

### Order Entry

The order entry SBE schema has been updated to version `16` (`semanticVersion` remains `1.5`), on both production and testnet:

* `CancelOrderResponse` (220): new `quantity` and `totalFilled` fields (`Decimal72`). `quantity` is the order quantity known to the matching engine; `totalFilled` is the cumulative filled quantity. Clients derive cancelled/leaves quantity as `quantity - totalFilled`. Present only when the session has negotiated schema version `16` or later.

See [Cancelling an Order](https://docs.deribit.com/starbase/cancelling-order.md#cancelorderresponse-220).

### FIX Drop Copy

The Drop Copy application schema is now version `2`:

* The [FIX Specification XML](https://docs.deribit.com/specifications/FIX50.xml) root carries `custApplVerId='2'`
* New `OrdRejReason` (103) value: `70` (`MMP_MIN_FREEZE_TIME_NOT_ELAPSED`)

Orders, amends, and mass quotes submitted during the mandatory 1-second MMP freeze (including those that set the `resetMmp` flag) are rejected with this reason. This matches the SBE `OrderRejectReason` `30` / `MassQuoteRejectReason` `9` added on 25.08.2026.

See [FIX Version](https://docs.deribit.com/starbase/fix-drop-copy-api.md#fix-version) and [Market Maker Protection](https://docs.deribit.com/starbase/mmp.md#resetting-mmp).

**Starbase Update 25.08.2026**

## API Changes

### Order Entry

The order entry SBE schema has been updated to version `15` (`semanticVersion` remains `1.5`), on both production and testnet:

* `OrderRejectReason`: new reason code `MMP_MIN_FREEZE_TIME_NOT_ELAPSED` (30): the MMP minimum freeze duration has not yet elapsed
* `MassQuoteRejectReason`: new reason code `MMP_MIN_FREEZE_TIME_NOT_ELAPSED` (9): the MMP minimum freeze duration has not yet elapsed

Orders, amends, and mass quotes submitted during the mandatory 1-second MMP freeze (including those that set the `resetMmp` flag) are rejected with this reason.

See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes) and [MassQuoteReject](https://docs.deribit.com/starbase/mass-quotes.md#massquotereject-232).

**Starbase Update 24.08.2026**

## API Changes

### FIX Drop Copy

The Drop Copy application schema is now versioned. The current version is `1`:

* The [FIX Specification XML](https://docs.deribit.com/specifications/FIX50.xml) root carries `custApplVerId='1'`
* The gateway echoes the same value on the **server** Logon as `DefaultCstmApplVerID` (Tag `1408`). There is no version negotiation. The client does not send this tag, and the session remains fully backwards compatible. A higher value than you last integrated against means new fields may have been added; download the latest spec

See [FIX Version](https://docs.deribit.com/starbase/fix-drop-copy-api.md#fix-version) for full details.

### REST gateway

`GET /api/v2/private/get_open_orders` now returns order flags:

* `post_only`: post-only (price is amended to the best bid/ask if the order would take). Corresponds to SBE `postOnly`
* `reject_post_only`: post-only reject (the order is rejected if it would take). Corresponds to SBE `postOnlyReject`. Mutually exclusive with `post_only`
* `reduce_only`: reduce-only. Per-order reduce-only originates from [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) or FIX; it cannot be set per order in SBE

See [Get Open Orders](https://docs.deribit.com/api-reference/trading/get-open-orders.md).

**Starbase Release 11.08.2026**

## API Changes

The following changes go live with the direct access (SBE order entry) gateway go-live on **Tuesday, 11th of August**.

### FIX Drop Copy

Per-portfolio scoping of a Drop Copy session:

* New optional `PortfolioScopeOnly` field (Tag `25002`) on the logon message: `Y` scopes the session to the single portfolio (subaccount) the logon credentials belong to. The gateway filters out events for the Member's other subaccounts server-side, including the open order snapshot on connect. `N` or omitted keeps the default full per-Member feed. Every Execution Report and Trade Capture Report identifies its portfolio in Tag 1 `Account` (the `portfolioId`)

See [Scoping a Session to One Portfolio](https://docs.deribit.com/starbase/fix-drop-copy-api.md#scoping-a-session-to-one-portfolio-25002) for full details.

### Market Data

TCP retransmit for clients connecting over AWS Private Link:

* The market data retransmit service is available over **TCP** on the AWS ports listed in [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md): `34240–34247` (A-side) and `24240–24247` (B-side). Direct cross-connect and colocation clients continue to use the UDP unicast protocol described on the [Retransmit Gateway](https://docs.deribit.com/starbase/retransmit-gateway.md) page. On the test environment, retransmit over AWS is not yet available

### Session Messages

The order entry SBE schema has been updated to version `14` (`semanticVersion` remains `1.5`), on both production and testnet:

* `Reject` (30): new reason code `GATEWAY_NOT_ACTIVE` (6): the target gateway is not active

See [Reject](https://docs.deribit.com/starbase/session-messages.md#reject-30) for the full list of reject reason codes.

The updated [order entry SDK](https://docs.deribit.com/starbase/binary-api-reference.md#downloads) `14.0`, built from schema version `14`, has been uploaded and is available for download.

Session-wide cancel-on-disconnect, announced with schema version `13` (`semanticVersion` `1.5`) on 07.08.2026, is live with the gateway go-live:

* `LogonRequest` (1): the optional `cancelOnDisconnect` field opts the entire session into CoD: the gateway applies cancel-on-disconnect to every `NewOrderRequest` and mass-quote leg submitted on the session, so resting liquidity is pulled if the client disconnects. The session value is a floor, not an override. An individual order cannot opt out once the session has opted in

See [Session-level CoD](https://docs.deribit.com/starbase/cancel-on-disconnect.md#session-level-cod) for full details on cancel-on-disconnect handling.

**Announcement 09.08.2026**

## Announcement

### Client Checklist for the August 11th Go-Live

Ahead of the direct access (SBE order entry) gateway go-live on **Tuesday, 11th of August** (immediately after the scheduled maintenance at 9:00 AM UTC), we have published a [production readiness checklist](https://docs.deribit.com/starbase/production-readiness-checklist.md) for clients already onboarded to Starbase.

The checklist covers Member setup, API key scopes for SBE order entry, the MMP risk bypass for the lowest-latency order path, the latest SBE XML versions, and logon and heartbeat testing on the production gateways. Please work through it before Tuesday and reach out to your technical account manager with any questions.

**Starbase Release 07.08.2026: v1.5**

## API Changes

The order entry SBE schema has been updated to version `13` (`semanticVersion` `1.5`).

### Session Messages

Session-wide cancel-on-disconnect opt-in at logon:

* `LogonRequest` (1): new optional `cancelOnDisconnect` field: when set, the gateway applies cancel-on-disconnect to every `NewOrderRequest` and mass-quote leg submitted on the session, so resting liquidity is pulled if the client disconnects. The session value is a floor, not an override. An individual order cannot opt out once the session has opted in. If absent, each order and quote leg carries its own per-message `cancelOnDisconnect` flag

See [Session-level CoD](https://docs.deribit.com/starbase/cancel-on-disconnect.md#session-level-cod) for full details on cancel-on-disconnect handling.

**Starbase Bugfix 07.08.2026**

## Bugfix

### Market Data

The market data SBE XML has been corrected. Index prices, mark prices, price bands, funding, and open interest are published on the multicast feeds:

* `IndexInfo` (12): index price per currency pair (`indexId` = `currencyPairId`), shared across the pair's instruments; sent on index price change and at the start of every snapshot cycle (one per known index price on the channel, batched into as few packets as fit)
* `InstrumentInfo` (14): `minSellPrice`, `maxBuyPrice`, and `markPrice` per instrument
* `InstrumentRef` (15): funding, settlement/delivery prices, and open interest per instrument (all optional)

The schema `version`/`semanticVersion` remains `1`/`1.0`.

**Action required:** re-download the SBE XMLs ([order entry](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-order-api.xml), [market data](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml)) and regenerate your SBE codecs (or update to the latest SDK).

See [Reference Data](https://docs.deribit.com/starbase/reference-data.md#index-prices-and-derived-statistics) for full message details.

**Starbase Release 04.08.2026: v1.4**

## API Changes

The order entry SBE schema has been updated to version `12` (`semanticVersion` `1.4`).

### Session Messages

Explicit schema version negotiation at logon:

* `LogonRequest` (1): new optional `schemaVersion` field: the SBE schema (protocol) version the client wants to use. It acts as a gate, determining whether new messages and new versions of existing messages are sent to the client. A value outside the gateway's accepted range is rejected at logon
* `LogonResponse` (2): new `schemaVersion` field echoing the schema version accepted by the gateway

See [Session Messages](https://docs.deribit.com/starbase/session-messages.md#logonrequest-1) for full message details.

**Announcement 30.07.2026**

## Announcement

### Revised Go-Live Schedule

During testing over the last few days, we discovered several gaps in Starbase's pre-trade risk module. A go-live with these gaps, however small, would create unacceptable platform risk. The gaps do not affect the current Production environment because all orders still pass through existing risk modules. When the [direct access gateways](https://docs.deribit.com/starbase/gateway-connectivity.md) are enabled, these risk modules would be bypassed. We are confident we can close these gaps, but it involves a few code changes and a scheduled maintenance. This scheduled maintenance will be on **August 11th at 9AM UTC**, instead of the previously announced August 4th. We will enable the direct access gateways immediately after the scheduled maintenance.

We had planned to enable [speed bumps](https://docs.deribit.com/starbase/speed-bumps.md) on production on Thursday, July 30th. We have also decided to push this back from July 30th to **August 4th**. Enabling the speed bump ahead of the direct access gateway go-live allows us time to monitor, and a week is adequate. Another postponement also allows time to adjust to the recent API changes announced on Sunday.

To summarize:

* **Speed bump enablement** is moved from Thursday, 30th of July between 9 and 11 AM UTC to **Tuesday, 4th of August between 9 and 11 AM UTC**
* **Direct access gateway go-live** is moved from Tuesday, 4th of August 9AM UTC to **Tuesday, 11th of August 9AM UTC**

We sincerely apologize for the additional delay. We feel this is the prudent decision to guarantee stability and market quality throughout this transition. Please reach out to your technical account manager with any questions.

**Announcement 28.07.2026**

## Announcement

### Speed Bump API Change

Due to a large amount of client feedback, we are changing the appearance of the [speed bump](https://docs.deribit.com/starbase/speed-bumps.md) in Deribit's WebSocket and non-Starbase FIX APIs. Currently, the response generated by a speed-bumped order or quote indicates that the order or quote has been speed bumped. For example, the WebSocket API will return a response with `order_state: speed_bumped`. After this change is made, the response generated by a speed-bumped order or quote will be exactly the same as for an order not subject to a speed bump, simply 10 milliseconds slower (the speed bump duration).

This change ensures that any existing client integration remains fully backwards-compatible when the speed bump is enabled. We realize that some clients would prefer an early acknowledgment. However, for most latency-sensitive clients, 10 milliseconds is below their average exchange-side roundtrip latency. Additionally, when a client switches to Starbase's order entry gateway on August 4th, this design decision will no longer affect them. We apologize for any inconvenience experienced in the interim.

To allow us to complete this change, we will enable the speed bump not on Tuesday, 28th of July, as previously communicated, but on **Thursday, 30th of July**. We will enable the speed bump separately per settlement currency:

* **30th of July, 9AM UTC:** All USDC-settled instruments
* **30th of July, 10AM UTC:** All ETH-settled instruments
* **30th of July, 11AM UTC:** All BTC-settled instruments

For any questions on the implications of the above change, please contact your technical account manager.

### Rolling Deployment of FIX Drop Copy and Multicast

Starbase has the ability to conduct rolling deployments: deploying each of a set of redundant components one-by-one so clients can fail over to one of the other components without disruption of their activities. Today, Tuesday, 28th of July, we will deploy all A-side components of the production Starbase Multicast feeds, Starbase FIX Drop Copy and Starbase order entry gateways. On Wednesday, we will deploy all B-side components of the same APIs. Please ensure that your integrations can fail over from the A-side to the B-side, if you are already relying on these production APIs. Please reach out to your technical account manager if you require a more specific timeslot.

### Go-Live of the Order Entry Gateway

The go-live of the order entry gateway is still scheduled for **August 4th**. There will be a scheduled maintenance at 9AM UTC, followed by a longer cancel-only period, during which the order entry gateways will be fully available. Mass quoting via the WebSocket or FIX APIs is not possible on subaccounts enabled for Starbase access by being included in a Member. To ensure falling back in case of issues is easy, we've documented the following endpoints. Please note that these are also available in the Starbase tab of your UI.

* [private/set\_member](https://docs.deribit.com/api-reference/account-management/private-set_member.md)
* [private/delete\_member](https://docs.deribit.com/api-reference/account-management/private-delete_member.md)
* [private/get\_members](https://docs.deribit.com/api-reference/account-management/private-get_members.md)

After the speed bump is enabled on Thursday, another circular will be sent, including the final details and reminders for the August 4th go-live.

**Starbase Release 21.07.2026: v1.3**

## API Changes

The order entry SBE schema has been updated to version `11` (`semanticVersion` `1.3`).

Updated SBE XMLs ([order entry](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-order-api.xml), [market data](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml)) and [Starbase SDK](https://docs.deribit.com/starbase/binary-api-reference.md#downloads) `0.5.1` reflecting these changes have been uploaded and are available for download.

### Order Entry

New messages for querying MMP freeze status:

* `GetMassQuoteMmpStatusRequest` (155): request the MMP status for a given `mmpGroupId`
* `GetOrdersMmpStatusRequest` (156): request the MMP status for a given underlying index (`currencyPairId`)
* `GetMassQuoteMmpStatusResponse` (280): returns `mmpGroupId` and `frozenUntilTime` (optional, present only while frozen)
* `GetMassQuoteMmpStatusReject` (281): rejects the request with a `reason`
* `GetOrdersMmpStatusResponse` (282): returns the underlying index and `frozenUntilTime` (optional, present only while frozen)
* `GetOrdersMmpStatusReject` (283): rejects the request with a `reason`

See [Querying MMP Status](https://docs.deribit.com/starbase/mmp.md#binary-api) for full message details.

New `MmpStatusRejectReason` enum, used by the reject messages above:

* `SYSTEM_ERROR` (0)
* `INVALID_MMP_GROUP` (1)

New `OrderFlags` value (`NewOrderRequest`):

* `resetMmp`: reset MMP for the order's `mmpGroupId` before processing it

### Session Messages

New `RejectReason` value, used by the `Reject` (30) message:

* `MESSAGE_DISABLED` (5): the message being submitted has been administratively disabled

The `Reject` (30) message and its `RejectReason` enum are now documented on the [Session Messages](https://docs.deribit.com/starbase/session-messages.md#reject-30) page.

## Announcement

The IP and port layout of the SBE Order Entry Gateway was changed from:

| Gateway | Side | Address | Port | Protocol | AWS Port |
| - | - | - | - | - | - |
| sbe-order | A | 195.138.37.1 195.138.37.1 195.138.37.3 195.138.37.3 | 4210 4211 4212 4213 | TCP | 34210 34211 34212 34213 |
| sbe-order | B | 195.138.37.2 195.138.37.2 195.138.37.4 195.138.37.4 | 4210 4211 4212 4213 | TCP | 44210 44211 44212 44213 |

to:

| Gateway | Side | Address | Port | Protocol | AWS Port |
| - | - | - | - | - | - |
| sbe-order (BTC) | A | 195.138.37.1 | 4210 | TCP | 34210 |
| sbe-order (ETH) | A | 195.138.37.3 | 4211 | TCP | 34211 |
| sbe-order (Tier 2) | A | 195.138.37.5 | 4212 | TCP | 34212 |
| sbe-order (Tier 3) | A | 195.138.37.7 | 4213 | TCP | 34213 |
| sbe-order (BTC) | B | 195.138.37.2 | 4210 | TCP | 44210 |
| sbe-order (ETH) | B | 195.138.37.4 | 4211 | TCP | 44211 |
| sbe-order (Tier 2) | B | 195.138.37.6 | 4212 | TCP | 44212 |
| sbe-order (Tier 3) | B | 195.138.37.8 | 4213 | TCP | 44213 |

See the [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md) page for full, up-to-date connection details.

**Starbase Release 15.07.2026: v1.2**

## API Changes

The order entry SBE schema has been updated to version `9` (`semanticVersion` `1.2`).

### Order Entry

New `OrderFlags` value (`NewOrderRequest`):

* `cancelOnDisconnect`: new order-level flag for cancel-on-disconnect handling

New `CancelReason` value:

* `QTY_TICK_SIZE_RESCALE` (17): instrument `qtyTickSize` changed and the order's quantity is not exactly representable under the new tick

New `OrderRejectReason` value:

* `MEMBER_SPEED_BUMP_LIMIT_EXCEEDED` (29): member has too many live speed-bumped orders

New `CancelOrderRejectReason` values:

* `TIME_IN_FORCE` (7): cancel rejected based on the order's time in force
* `SPEED_BUMP_CONVERTED_TO_IOC` (8): cancel rejected because the speed-bumped order was already converted to IOC

`OrderPlaced` (312) updated:

* New `correlationId` field: echoes the `correlationId` from the originating `NewOrderRequest`, aligning `OrderPlaced` with other order-entry response messages

### FIX Drop Copy

New `ExecutionReport` fields:

* `TransferReason`
* `MmpGroupId` (tag `8001`)

New `OrdRejReason` (103) value:

* `69`: `MEMBER_SPEED_BUMP_LIMIT_EXCEEDED`

New `ExecType` (150) value:

* `I`: `ORDER_STATUS`

**Announcement 03.07.2026**

## Announcement

We're writing to inform you of a **delay** to the Starbase production go-live. The two key dates are changing, resulting in a total delay **of 2 weeks**.

* Market data, FIX Drop Copy and gateway connectivity: now 21st of July, previously 13th of July
* Speed bump activation: now 28th of July, previously 13th of July
* SBE order entry gateway access: now 4th of August, previously 20th of July

We have recently experienced postponements in production deployments, which in turn delayed the rollout of key features. To ensure stability throughout the entire migration, we are adjusting the schedule.

Certain production order books are already matching on Starbase. The more order books we have on Starbase and the longer they match, the more certain we are of performance and resilience. We migrated some order books later than we would have liked and feel additional time is prudent.

Three key features will appear on Starbase's test environment in the coming week or so. To give you and us ample time to test these, two extra weeks are necessary.

* Speed bumps. We aim to activate speed bumps on the test environment early next week.
* Cancel-on-disconnect. Cancel-on-disconnect (CoD) is not yet available on the test environment. We will ensure this is available one week before the 4th of August.
* L2 market data. As some of you have noticed, orders or quotes submitted directly on Starbase are not yet reflected in the Deribit UI or legacy L2 market data feeds. We aim to integrate this on the test environment next week.

Deribit is undergoing many changes this year. We want to assure you that many of the other key initiatives are NOT affected by this delay, including:

* The merger with Coinbase International, now scheduled for the 9th of September. This was communicated to Coinbase International clients earlier this week. If you are unaware, please reach out to your point of contact.
* We plan to list all of Coinbase International's perpetuals on Deribit between the 10th of August and 9th of September.
* Our BTC and ETH options will switch from cash-settled to futures-settled as of August 1st.
* New fees, quoting programs and the launch of the Liquidity Support Program are still slated for August 1st.

We apologize for the delay and hope the additional two weeks allow you to better support Starbase at launch. Please reach out to your point of contact with any questions or concerns.

**Starbase Release 26.06.2026: v1.1**

## API Changes

The order entry SBE schema has been updated to version `4`.

### Order Entry

New message:

* `CancelOrderByIdRequest` (125): cancel an order by its exchange-assigned `orderId` instead of `clientOrderId`

New `CancelOrderRejectReason` values:

* `IN_LIQUIDATION` (5): cancel rejected because the portfolio is in liquidation
* `INVALID_INSTRUMENT` (6): cancel rejected because the instrument is not valid

New `MassQuoteRejectReason` value:

* `DUPLICATE_INSTRUMENT` (8): the same instrument appears in more than one entry of a single mass quote

**Announcement 18.06.2026**

## Announcement

We are one month away from the go-live of Starbase. Below is a confirmation of key timelines along with important details on speed bumps, rate limits, spot and circuit redundancy.

### Confirmation of Timelines

* **July 13th:** Member and API key creation will be available in the UI, along with four SBE Order Entry endpoints for connectivity testing: Logon, Logout, Heartbeat, and Test. Access to market data and FIX drop copy will also be enabled on this date. Multicast market data feeds will begin propagating to client servers within LD4, AWS eu-west-2 and AWS ap-northeast-1 for all derivatives. This phased rollout ensures a smooth transition before order entry go-live.
* **July 20th (Go-Live):** Clients will receive full access to the SBE Order Entry gateway for all derivatives.

### Speed Bumps

We have experienced delays in the rollout of [speed bumps](https://docs.deribit.com/starbase/speed-bumps.md) to the test environment due to some downstream processes not handling the new order state well. The speed bump as described in our documentation will go live on Starbase's test environment at least two weeks ahead of the production go-live.

Speed bumps will apply to every instrument except the top 5 crypto perpetuals by volume: BTC, ETH, SOL, XRP and HYPE. This also means BTC and ETH inverse perpetuals are exempt from speed bumps. The following instruments will all be speed bumped:

* All crypto and RWA perpetuals, except BTC, ETH, SOL, XRP and HYPE
* All options, both inverse and linear
* All dated futures, both inverse and linear
* All multi-leg instruments including one of the above as a leg (future spreads, option combinations)

To align with market standards, each order or quote in the speed bump is guaranteed to be firm. Cancelling an order or quote in the speed bump will convert its TIF into IOC. CoD or triggers will also convert speed-bumped orders and quotes into IOCs. An order or quote subject to [self-match prevention](https://docs.deribit.com/starbase/smp.md) that leaves the speed bump will have the `CANCEL_MAKER` behavior, even if `CANCEL_TAKER` is configured.

### Rate Limits

The Starbase rate limit framework has been finalised. See the [rate limits article](https://docs.deribit.com/starbase/api-rate-limits.md) for a full explanation of the mechanics. Two important points:

* Members receiving this announcement will likely receive a **Member Override**. Do not assume the default values in the article apply to you; treat them as illustrative examples. Please reach out to your account manager to confirm your production rate limits as of July 20th.
* Rate limits are applied **per member, per gateway**. As each instrument is available through two gateways, not utilising both means not utilising your full rate limit allocation.

### Spot

Deribit's spot order books will not be available on Starbase. Shortly after go-live, spot orders will be routed to Coinbase Exchange, located in the US. Until that migration, spot order books will remain available only via the current WebSocket and FIX APIs. A small subset of order books not available on Coinbase (such as BUIDL, USYC and USDE) will remain on Deribit's legacy matching engine indefinitely.

### Redundant Cross-Connect

We strongly recommend maintaining a primary and a secondary circuit. During switch maintenance or cable-length validations, we assume clients have redundant connectivity in place so that trading can continue uninterrupted.

Starbase is only available via hosted co-location, cross-connect or AWS PrivateLink. Downtime on a single circuit may require you to fall back to the WebSocket API. Please reach out to \[[colo-support@coinbase.com](mailto:colo-support@coinbase.com)]\(mailto:[colo-support@coinbase.com](mailto:colo-support@coinbase.com)) or your technical account manager with any questions.

**Starbase Release 06.05.2026: v1.0**

## Starbase Release

### Key Dates & Access

* **July 13th:** Member and API key creation will become available in the UI, along with four SBE Order Entry endpoints for connectivity testing: Logon, Logout, Heartbeat, and Test. Access to market data and FIX drop copy will also be granted on this date. Multicast market data feeds will begin propagating to client servers within LD4, AWS eu-west-2 and AWS ap-northeast-1 for all derivatives.
* **July 20th (Go-Live):** Clients will receive full access to the SBE Order Entry gateway for all derivatives.

### Equalization

Due to hardware shortages and delivery delays, equalization of all connections for trading on Starbase is expected before the end of August. The maximum possible latency difference between the fastest and slowest member is \<5 microseconds, depending on the length of the cross connects. Equalization will involve migrating existing cross connects; no new cross connects are necessary. Because Deribit's hosted co-location uses very short cables to the edge switch, hosted co-location is expected to be a few microseconds faster than cross connects during July and some parts of August.

### Stability

Starbase's test environment has performed stably for two consecutive weeks and is well positioned to support technical integration.

### Introduction of ETH to Starbase's test environment

Inverse and linear ETH products have been migrated from the legacy matching engine to Starbase on test.deribit.com. The following products are now matching on Starbase in the test environment:

* Linear ETH options, futures and the perpetual (options and futures with a 10ms speed bump)
* Inverse ETH options, futures and the perpetual (options and futures with a 10ms speed bump)
* AVAX options, futures and perpetual (all with a 10ms speed bump)
* PAXG perpetual

All BTC products remain on the legacy matching engine.

### REST gateway

A REST API with utility endpoints is now [available](https://docs.deribit.com/starbase/rest-authentication.md). Notable endpoints include:

* **Platform-wide mass cancellation:** allows cancellation of all open orders across the platform.
* **Subaccount lock:** enables you to completely lock Starbase APIs from accessing a specific subaccount. This endpoint also cancels all open orders and will be made available over the internet.

### Environment resets

In the coming weeks, engineers may trigger resets of Starbase's test environment. These resets will cause only brief downtime and will not reset any credentials or configurations. However, they will disconnect open connections and wipe all open orders and related histories. Please reach out to your account manager to be notified in advance of any resets.

### Documentation updates

Now that Starbase has stabilized, the SDK and PCAPs will be versioned with the `version` and `semanticVersion` from the XML messageSchema. The latest `version` and `semanticVersion` will appear on the specification pages.

## API Changes

### Market Data

`Instrument` message has been renamed to `InstrumentDefinition` and redesigned:

* New fields added: `indexId`, `underlying`, `quantityAsset`, `priceAsset`, `minOrderQuantity`
* Removed fields: `symbol`, `baseCurrency`, `quoteCurrency`, `baseIncrement`, `creationTime`, `logicalExpiry`
* Large tick size information is now represented as a repeating `largeTickSizes` group instead of flat fields
* A new repeating `legs` group has been added to support combo instruments

New `IndexDefinition` message added, providing `indexId` and `name` for each index.

Message ID changes:

* `TradingStatusUpdate` has been removed and replaced by `InstrumentStatusUpdate`
* `InstrumentInfo` and `InstrumentRef` have been renumbered

`sortOrderId` field added to `Buy Put` and `Sell Put` messages.

`TradeSummary` message redesigned:

* `impliedVolatility` field removed
* `tradeCount` field added: indicates the number of `Trade` messages following the summary
* `takerFlags` field renumbered

### Order Entry

New `CancelReason` values:

* `PORTFOLIO_LOCKED`: order cancelled because the portfolio is locked
* `POST_ONLY`: post-only order would have crossed

New `OrderRejectReason` values:

* `PORTFOLIO_LOCKED`: order rejected because the portfolio is locked
* `POSITION_LIMIT_EXCEEDED`: future or options position size limit exceeded
* `ORDER_SIZE_LIMIT_EXCEEDED`: open order aggregate size limit exceeded

New `MassQuoteRejectReason` value:

* `PORTFOLIO_LOCKED`: mass quote rejected because the portfolio is locked

**Announcement 17.04.2026**

## Announcement

Thank you to everyone who has already started trading on the Starbase test environment. Members have logged on and sent, amended, and cancelled orders, including mass quotes.

### Documentation and downloads

Refreshed XMLs, PCAPs and SDKs can be found on the [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md) page. Updated documentation is available across the [Starbase](https://docs.deribit.com/starbase/overview.md) section.

### Multicast

Nothing will change for the current production multicast feeds. They will continue as-is under all circumstances. To receive the new Starbase multicast feeds:

1. **Deribit-hosted colo servers:** No changes needed. Send an IGMP join for the multicast feeds you want to consume.
2. **Cross-connected clients:** PIM configuration with an RP is required. For configuration details, contact \[[colo-support@coinbase.com](mailto:colo-support@coinbase.com)]\(mailto:[colo-support@coinbase.com](mailto:colo-support@coinbase.com)).
3. **Third-party clients (Beeks, UltraFX, LiquidityConnect, AWS):** Setup is in progress. You will be notified when connectivity is verified and ready.

Since only AVAX/USDC and PAXG/USDC instruments have been migrated, not every multicast channel has market data flowing yet. To test connectivity, use channel `224.0.12.234`, which includes all AVAX options. All channels are listed on the [Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) page. A [table mapping underlyings to tiers](https://docs.deribit.com/starbase/underlying-tiers.md) is also available.

For any questions or concerns, contact \[[colo-support@coinbase.com](mailto:colo-support@coinbase.com)]\(mailto:[colo-support@coinbase.com](mailto:colo-support@coinbase.com)).

**Announcement 08.04.2026**

## Announcement

Starbase is now live on test.deribit.com. Starbase is Deribit's new matching engine, which unlocks throughput of more than 100k orders per second with submillisecond latencies, and will be the home of all of Coinbase's international derivatives. To learn more, see the [Starbase overview](https://docs.deribit.com/starbase/overview.md).

### Instruments on Starbase (test.deribit.com)

The following instruments are currently handled by Starbase:

* PAXG\_USDC-PERPETUAL
* AVAX\_USDC-PERPETUAL
* All AVAX\_USDC dated futures
* All AVAX\_USDC options

All other instruments operate on the legacy matching engine. Starbase is under active development, so improvements will be added to the test.deribit.com deployment often and without notice.

### Connecting

1. Contact your Deribit account manager via Telegram or Slack with your test.deribit.com main account user ID. They will enable direct access for all underlying subaccounts.
2. [Create and assign a Member](https://docs.deribit.com/starbase/creating-member.md) on the main account before generating any key.
3. [Create a Starbase API key](https://docs.deribit.com/starbase/creating-api-key.md).
4. Use the connectivity details below for order entry and market data.

No changes are required for existing cross-connects or other direct connections. Full connectivity details are available on the [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md) page.

### SDK and specifications

The latest [SDK](https://docs.deribit.com/starbase/binary-api-reference.md#downloads) is available for download. XML schemas for the SBE APIs are included with the SDK release.

Starbase remains on track to go live on Deribit's production environment for all derivatives in the first half of July.

**Announcement 11.03.2026**

## Announcement

Starbase will replace some order books on test.deribit.com on **April 8th**. On that date:

* Members can create API keys to authenticate against Starbase using the existing API key creation UI on test.deribit.com.
* Members will receive an email with the IPs of the gateways and the usable ports.
* Market data will be published on the [multicast channels](https://docs.deribit.com/starbase/multicast-channels.md).
* That same email will include a list of instruments whose order books have been migrated to Starbase.
* XML specs for the SBE APIs will be made available.

[FIX Drop Copy specifications](https://docs.deribit.com/starbase/fix-drop-copy-api.md) are now available. A Python SDK (.whl) is also available to kickstart integration of the Starbase order entry and market data APIs.

**Announcement 01.02.2026**

## Announcement

A change in company strategy has led to changes in technology and timelines, driven by the decision to align with other Coinbase exchanges.

### What won't change

All existing APIs will continue to work throughout the ME replacement. The physical location and network connectivity won't change, and the tradeable contracts will stay the same. Unless you care about performance, you won't notice a thing.

### Timelines

* **Early April:** A test environment will be made available.
* **Early June:** We will start rolling out direct access.
* **August:** Every order book will have moved over and every direct access API will be available.

### Starbase specifications

The new matching engine, Starbase, comes with a low-latency order entry API and multicast market data feed. The specifications are available [here](https://docs.deribit.com/starbase/overview.md). Other key information:

* [Market model](https://docs.deribit.com/starbase/market-model.md)
* [Account model](https://docs.deribit.com/starbase/account-model.md)
* [Market Maker Protection](https://docs.deribit.com/starbase/mmp.md)
* [Self-Match Prevention](https://docs.deribit.com/starbase/smp.md)
* [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md)
* [Gateway connectivity model and limits](https://docs.deribit.com/starbase/gateway-connectivity.md)

This is made available early to allow for feedback and to help with planning your integration.

### Coming soon

* FIX Drop Copy specifications will be made available next month
* A REST API with utility endpoints will be made available next month
* XML specs of the SBE and FIX APIs will be available before the test environment is live
* PCAPs of all APIs will be available before the test environment is live
* Code examples will be available before the test environment is live

Minor updates to the APIs can be expected as designs are adapted based on member feedback.


## Related topics

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Starbase API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md)
- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md)
- [FIX API Changelog](https://docs.deribit.com/changelogs/fix.md)
- [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md)