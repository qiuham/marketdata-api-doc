---
exchange: deribit
source_url: https://docs.deribit.com/starbase/unsolicited-events
api_type: Starbase
updated_at: 2026-11-18 18:59:10.751476
---

# Starbase Unsolicited Events

> Server-initiated Starbase Binary API events: maker OrderFilled fills, OrdersCanceled, MMP trigger and unfreeze events, and opt-in liquidation notifications.

## Unsolicited events

Unsolicited events are sent by the exchange when activity occurs on your resting orders or quotes without you directly requesting it. Examples include fills as a maker, system cancellations, or MMP triggers.

> [!NOTE]
>
> **Maker vs. taker fills**: `OrderFilled` unsolicited events are only sent to the **maker**. If your order or quote was the aggressor (taker), all fill information is returned directly on the acknowledgement message (`NewOrderResponse`, `AmendOrderResponse`, or `MassQuoteResponse`). You will not receive a separate `OrderFilled` event for taker fills. The exception is [liquidation notifications](#liquidation-notifications): a session that opts in receives fills of exchange-initiated liquidation orders on its portfolio as unsolicited `OrderFilled`, whether the liquidation order was maker or taker.

### OrderFilled (300)

Event generated when one or more resting orders are filled by a taker order. This may include orders from different instruments if the taker order was for a combo instrument and matched an implied order.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | blockLengthOfFills | uint16 | 2 | 60 (bytes) |
| 4 | numberOfFills | uint16 | 2 | Indicates the length of the following repeating group containing all immediate fills when the order was submitted |
| ->5 | clientOrderId | int64 | 8 | Numeric client order ID. Set to the `quoteId` if the order was submitted as part of a `MassQuote` |
| ->6 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| ->7 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->8 | matchId | int64 | 8 | Transaction ID representing match, shared by all fills within match |
| ->9 | fillPrice | Price9 | 8 | Price of fill |
| ->10 | fillQty | Decimal72 | 9 | Quantity of fill |
| ->11 | totalFilled | Decimal72 | 9 | Cumulative amount filled |
| ->12 | side | int8 | 1 | `1`=BUY `-1`=SELL |
| ->13 | flags | uint8 | 1 | Defined in following table |
| 14 | blockLengthOfLegs | uint16 | 2 | 34 (bytes) |
| 15 | numberOfLegs | uint16 | 2 | Indicates the length of the following repeating group containing all combo leg quantities and prices. Non-zero for trades on combo instruments only. |
| ->16 | matchId | int64 | 8 | Transaction ID representing match. |
| ->17 | instrumentId | int64 | 8 | Numeric instrument ID. |
| ->18 | legPrice | Price9 | 8 | Price of this leg in the combo instrument |
| ->19 | legQuantity | Decimal72 | 9 | Quantity of this leg in the combo instrument |
| ->20 | legSide | int8 | 1 | `1`=BUY `-1`=SELL |

The table below outlines the content of field 13 (flags).

| Bit number (from last to first) | Name | Description |
| - | - | - |
| 1 | isQuote | `0`=False (order) `1`=True (quote) |
| 2 | isFullyFilled | `0`=PartiallyFilled `1`=FullyFilled |
| 3 | isLiquidation | `0`=False `1`=True (fill of an exchange-initiated liquidation order on this portfolio). Added in schema version `22`. Set only on sessions that opted in to [liquidation notifications](#liquidation-notifications) |
| 4 | Reserved for future use | |
| 5 | Reserved for future use | |
| 6 | Reserved for future use | |
| 7 | Reserved for future use | |
| 8 | Reserved for future use | |

### OrdersCanceled (310)

Event generated when one or more orders and/or quotes submitted via this binary API session are canceled for some reason other than in direct response to a request on this same session (`NewOrderRequest`, `AmendOrderRequest`, `CancelOrderRequest`, `MassQuoteRequest`). For example, end-of-day expiries, liquidation, admin action, a mass cancel, an MMP trigger, or a cancel sent from a different session.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | flags | uint8 | 1 | `0`=isLastMessage |
| 4 | blockLengthOfOrders | uint16 | 2 | 35 (bytes) |
| 5 | numberOfOrders | uint16 | 2 | Length of the following repeating group of canceled orders |
| ->6 | clientOrderId | int64 | 8 | Numeric client order ID |
| ->7 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| ->8 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->9 | totalFilled | Decimal72 | 9 | Filled quantity of canceled order |
| ->10 | cancelReason | int8 | 1 | See [Cancel Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#cancel-reason-codes) |
| ->11 | flags | uint8 | 1 | `1`=isQuote |

> [!NOTE]
>
> **Cross-session cancels** (schema version `17`): When another session cancels an order this session submitted, this session receives `OrdersCanceled` if it negotiated schema version `17` or later. The cancelling session receives [`CancelOrderResponse` (220)](https://docs.deribit.com/starbase/cancelling-order#cancelorderresponse-220). The message layout is unchanged from schema version `16` (additive, backward-compatible). Sessions negotiated below `17` still receive `CancelOrderResponse` on the submitting session. See [Cancelling an Order](https://docs.deribit.com/starbase/cancelling-order.md).

> [!NOTE]
>
> **Liquidation cancels**: Orders cancelled by liquidation arrive on the gateway where the order was originally placed. Consistent with [event scoping](https://docs.deribit.com/starbase/gateway-connectivity.md#connecting-to-multiple-gateways), they are not broadcast to your other sessions. Monitor `OrdersCanceled` with `cancelReason = 5` (`LIQUIDATION`) on every order-entry session to detect them. To also receive the resulting liquidation fills and LSP/ADL position moves, opt in to [liquidation notifications](#liquidation-notifications).

### OrderPlaced (312)

Unsolicited event sent when a speed-bumped order completes the speed bump period and is entered into the book. Sent to the session that originally submitted the order. When the order matches immediately upon book entry, `numberOfFills` is greater than 0 and the fills repeating group is populated.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 5 | instrumentId | int64 | 8 | Numeric instrument ID |
| 6 | limitPrice | Price9 | 8 | Price at which the order was placed in the book |
| 7 | quantity | Decimal72 | 9 | Quantity |
| 8 | totalFilled | Decimal72 | 9 | Total quantity filled upon book entry. `0` if no immediate fills |
| 9 | visibleQty | Decimal72 | 9 | Amount currently visible in market data |
| 10 | status | int8 | 1 | `1`=Active `2`=Filled `3`=Cancelled (if cancelled during the speed bump period) |
| 11 | cancelReason | int8 | 1 | See [Cancel Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#cancel-reason-codes) |
| 12 | correlationId | int64 | 8 | `correlationId` from the originating `NewOrderRequest` |
| 13 | blockLengthOfFills | uint16 | 2 | 25 (bytes) |
| 14 | numberOfFills | uint16 | 2 | Number of fills. `0` if the order entered the book without immediately matching |
| ->15 | matchId | int64 | 8 | Transaction ID representing match |
| ->16 | fillPrice | Price9 | 8 | Price of fill |
| ->17 | fillQty | Decimal72 | 9 | Quantity of fill |
| 18 | blockLengthOfLegs | uint16 | 2 | 34 (bytes) |
| 19 | numberOfLegs | uint16 | 2 | Indicates the length of the following repeating group containing all combo leg quantities and prices. Non-zero for trades on combo instruments only. |
| ->20 | matchId | int64 | 8 | Transaction ID representing match. |
| ->21 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->22 | legPrice | Price9 | 8 | Price of this leg in the combo instrument |
| ->23 | legQty | Decimal72 | 9 | Quantity of this leg in the combo instrument |
| ->24 | legSide | int8 | 1 | `1`=BUY `-1`=SELL |

> [!NOTE]
>
> `correlationId` (field 12) and the 3-byte alignment padding preceding it were added in schema version `8`; earlier versions of this message did not carry a `correlationId`.

### MassQuoteOrdersPlaced (314)

Unsolicited event sent when one or more speed-bumped quote sides complete the speed bump period and are entered into the book. Sent to the session that originally submitted the `MassQuoteRequest`. Each placed side is reported as an entry in the `orders` repeating group (with `status` and `cancelReason`). When a side was converted to IOC during the bump, infer that from `status` / `cancelReason`. There is no separate `timeInForce` field. See [Mass quote message flow](https://docs.deribit.com/starbase/speed-bumps.md#mass-quote-message-flow).

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | mmpGroupId | int64 | 8 | Identifier of MMP group |
| 4 | blockLengthOfOrders | uint16 | 2 | Bytes per entry in the orders repeating group |
| 5 | numberOfOrders | uint16 | 2 | Number of placed quote-side orders in this message |
| ->6 | clientOrderId | int64 | 8 | Numeric client order ID |
| ->7 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| ->8 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->9 | price | Price9 | 8 | Limit price |
| ->10 | quantity | Decimal72 | 9 | Quantity |
| ->11 | totalFilled | Decimal72 | 9 | Total quantity filled upon book entry. `0` if no immediate fills |
| ->12 | visibleQty | Decimal72 | 9 | Amount currently visible in market data |
| ->13 | side | int8 | 1 | `1`=BUY `-1`=SELL |
| ->14 | status | int8 | 1 | `1`=Active `2`=Filled `3`=Cancelled `4`=Queued |
| ->15 | cancelReason | int8 | 1 | See [Cancel Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#cancel-reason-codes) |
| 16 | blockLengthOfFills | uint16 | 2 | Bytes per entry in the fills repeating group |
| 17 | numberOfFills | uint16 | 2 | Number of fills. `0` if no immediate fills |
| ->18 | matchId | int64 | 8 | Transaction ID representing match |
| ->19 | orderId | int64 | 8 | Order ID that received the fill |
| ->20 | fillPrice | Price9 | 8 | Price of fill |
| ->21 | fillQty | Decimal72 | 9 | Quantity of fill |
| 22 | blockLengthOfLegs | uint16 | 2 | Bytes per entry in the legs repeating group |
| 23 | numberOfLegs | uint16 | 2 | Non-zero for trades on combo instruments only |
| ->24 | matchId | int64 | 8 | Transaction ID representing match |
| ->25 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->26 | legPrice | Price9 | 8 | Price of this leg in the combo instrument |
| ->27 | legQty | Decimal72 | 9 | Quantity of this leg in the combo instrument |
| ->28 | legSide | int8 | 1 | `1`=BUY `-1`=SELL |

### MassQuoteMmpTriggered (320)

Event generated when a mass quote Market Maker Protection limit is triggered. Followed by one or more OrdersCanceled messages.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of trigger in the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | mmpGroupId | int64 | 8 | Identifier of MMP group |
| 4 | frozenUntil | int64 | 8 | Nanoseconds since epoch |
| 5 | quantityLevel | double | 8 | The total traded quantity, within a given interval, at the time of the trigger |
| 6 | vegaLevel | double | 8 | The change in vega exposure within a given interval, at the time of the trigger |
| 7 | deltaLevel | double | 8 | The change in delta within a given interval, at the time of the trigger |
| 8 | trigger | int8 | 1 | 0=quantity 1=delta 2=vega |

### OrdersMmpTriggered (322)

Event generated when an orders Market Maker Protection limit is triggered. Followed by one or more OrdersCanceled messages.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of trigger in the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | indexId | int64 | 8 | Underlying [index](https://docs.deribit.com/starbase/market-model.md#index) ID, same as `index_id` on [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) and `currencyPairId` in the SBE schema |
| 4 | frozenUntil | int64 | 8 | Nanoseconds since epoch |
| 5 | quantityLevel | double | 8 | The total traded quantity, within a given interval, at the time of the trigger |
| 6 | vegaLevel | double | 8 | The change in vega exposure within a given interval, at the time of the trigger |
| 7 | deltaLevel | double | 8 | The change in delta within a given interval |
| 8 | trigger | int8 | 1 | 0=quantity 1=delta 2=vega |

### MassQuoteMmpUnfrozen (324)

Event generated when a mass quote Market Maker Protection group is unfrozen, either in response to a reset request or because the `frozenUntil` timer elapsed.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of trigger in the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | mmpGroupId | int64 | 8 | Identifier of MMP group |
| 4 | correlationId | int64 | 8 | Client-assigned ID, or `0x8000000000000000` if unsolicited (timer elapsed) |

### OrdersMmpUnfrozen (326)

Event generated when an orders Market Maker Protection group is unfrozen, either in response to a reset request or because the `frozenUntil` timer elapsed.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of trigger in the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | indexId | int64 | 8 | Underlying [index](https://docs.deribit.com/starbase/market-model.md#index) ID, same as `index_id` on [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments) and `currencyPairId` in the SBE schema |
| 4 | correlationId | int64 | 8 | Client-assigned ID, or `0x8000000000000000` if unsolicited (timer elapsed) |

### Liquidation notifications

Sessions can opt in to unsolicited notifications about liquidations on their portfolio by setting `liquidationNotifications=1` on [`LogonRequest`](https://docs.deribit.com/starbase/session-messages#logonrequest-1) with `schemaVersion` `22` or later. A logon that sets the flag with a lower `schemaVersion` is rejected. Sessions that do not opt in see no change.

An opted-in session receives:

* **Liquidation fills**: an unsolicited [`OrderFilled` (300)](#orderfilled-300) for each fill of an exchange-initiated liquidation order on the portfolio, with `flags.isLiquidation` (bit 3) set. This covers resting, aggressive, speed-bumped, and replaced liquidation orders. If the same session also submitted an order filled in the same event, it receives a single `OrderFilled` that carries both its own fills and the liquidation fills.
* **Position moves**: a [`PositionMoved` (330)](#positionmoved-330) message when a Liquidity Support Provider (LSP) or Auto-Deleveraging (ADL) assignment moves a position into or out of the portfolio. Admin position moves are not reported.

Notifications go to every connected session of the portfolio that opted in, on any API key. These notifications are an exception to the usual [event scoping](https://docs.deribit.com/starbase/gateway-connectivity.md#connecting-to-multiple-gateways). A client that opts in on both the A and B gateway receives a copy on each session and should deduplicate by `matchId`.

### PositionMoved (330)

Unsolicited event sent to opted-in sessions when an LSP or ADL assignment moves a position into or out of this portfolio. Added in schema version `22`. Each portfolio involved in a move is notified on its opted-in sessions: the liquidated portfolio with `role=TAKER`, and the receiving portfolio with `role=MAKER`. The two notifications share the same `matchId`.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of the move in the matching engine |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | instrumentId | int64 | 8 | Numeric instrument ID |
| 4 | matchId | int64 | 8 | Transaction ID of the move, shared by the `TAKER` and `MAKER` notifications of the same move |
| 5 | price | Price9 | 8 | Price at which the position was moved |
| 6 | quantity | Decimal72 | 9 | Quantity moved |
| 7 | side | int8 | 1 | Side of this portfolio's position change: `1`=BUY `-1`=SELL |
| 8 | role | int8 | 1 | `1`=TAKER (this portfolio is the source of the move, the liquidated portfolio) `2`=MAKER (this portfolio received the moved position) |
| 9 | reason | int8 | 1 | `1`=LSP (position absorbed by a Liquidity Support Provider) `2`=ADL (position assigned by Auto-Deleveraging) |


## Related topics

- [Starbase Market Maker Protection (MMP)](https://docs.deribit.com/starbase/mmp.md)
- [Starbase FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md)
- [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md)
- [Starbase Mass Cancel Messages](https://docs.deribit.com/starbase/mass-cancel.md)
- [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md)