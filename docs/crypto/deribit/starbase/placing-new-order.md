---
exchange: deribit
source_url: https://docs.deribit.com/starbase/placing-new-order
api_type: Starbase
updated_at: 2026-11-18 18:59:10.374252
---

# Placing a New Order

> Submit new orders via the Starbase Binary API. Covers NewOrderRequest, NewOrderResponse, and NewOrderReject messages, including supported order types and flags.

## Placing a new order

> [!NOTE]
>
> **Fill Limits**: The maximum number of fills on a single order is **2000 fills for single-leg instruments** and **400 fills for combo instruments**.

> [!TIP]
>
> **Lowest-latency order entry**: Set the `MMP` flag (field 10, bit 4) so the order uses the [MMP risk bypass](https://docs.deribit.com/starbase/risk-bypass.md), the lowest-latency method for market access, which skips the pre-trade risk engine. The bypass applies whether the order makes or takes. Most integrating clients should prefer this path for all order entry. The bypass requires the MMP configuration's **Quantity Limit ≤ Max Quote Quantity**.

### NewOrderRequest (100)

Request to place a new order sent by the client. The order will belong to the portfolio with which the connection was authenticated. Will be followed by a `NewOrderResponse` in case the order placement is successful or by a `NewOrderReject` in case the order placement is unsuccessful. Any immediate fills will be added to the `NewOrderResponse` and will NOT be sent in an `OrderFilled`. Any consecutive unsolicited change to the order (including fills) will be sent in an `OrderFilled`.

If the order aggresses and is subject to a speed bump, the `NewOrderResponse` is sent immediately with `orderState = 4` (queued). Once the speed bump period expires and the order is entered into the book, an unsolicited `OrderPlaced` message is sent. See [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md) for details.

> [!NOTE]
>
> **Null values**: Some optional fields use `NULL_LONG` / `NULL_QUANTITY` (`0x8000000000000000L`) as a sentinel to indicate "not set". For example, set `displayAmount = NULL_QUANTITY` to place a non-iceberg order, or `limitPrice = NULL_LONG` for a market order.

> [!NOTE]
>
> **Quantity units**: Encode `quantity` as `Decimal72` in the instrument's `quantityAsset` and validate it against `minOrderQuantity` from the multicast `InstrumentDefinition`. Do not copy a FIX contract count directly into this field, and do not substitute `contract_size` for the Starbase quantity tick. See [Quantity units and contract size](https://docs.deribit.com/starbase/reference-data.md#quantity-units-and-contract-size).

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | clientOrderId | int64 | 8 | Required. Numeric client order ID. Unique per portfolio. |
| 2 | correlationId | int64 | 8 | Required. Client-assigned ID. Scope: per connection. |
| 3 | instrumentId | int64 | 8 | Required. Numeric instrument ID. |
| 4 | limitPrice | Price9 | 8 | Limit price. For market orders set to `0x8000000000000000L` and use `marketLimit` flag. |
| 5 | quantity | Decimal72 | 9 | Required. Quantity. |
| 6 | showQty | Decimal72 | 9 | Visible amount for iceberg orders. Setting this field to any value (including equal to `amount`) marks the order as an iceberg order. To submit a non-iceberg order, omit this field or set it to `NULL_QUANTITY`. Iceberg orders are not supported for options and combo instruments. |
| 7 | selfMatchPreventionId | int64 | 8 | SMP token. This order cannot match with any other orders within the same portfolio with the same token. `0` /null → no SMP enforcement. |
| 8 | side | int8 | 1 | Required. `1`=BUY `-1`=SELL |
| 9 | timeInForce | int8 | 1 | Accepted values only: `-2`=Immediate-or-cancel `-1`=Fill-or-kill `0`=Good-til-cancel `1`=Good-til-day (cancelled at the next 08:00 UTC settlement, not 24 hours after placement). Values greater than `1` are rejected. |
| 10 | flags | uint16 | 2 | See the table below. |
| 11 | smpMode | int8 | 1 | Required. `0`=CancelTaker `1`=CancelMaker **Note**: if the taker order is [speed-bumped](https://docs.deribit.com/starbase/speed-bumps.md), the mode is overridden to `CancelMaker` regardless of this field. |

> [!WARNING]
>
> **Good-til-day is one session only.** The gateway accepts only `-2` (IOC), `-1` (FOK), `0` (GTC), and `1` (GTD). `1` is cancelled at the next 08:00 UTC settlement, the same one-session lifetime as `good_til_day` on the classic APIs. Multi-day GTD (`timeInForce > 1`) is not supported: the field is `int8` on the wire, but any value greater than `1` is rejected with [`NewOrderReject`](#neworderreject-202) reason [`INVALID_FIELD`](https://docs.deribit.com/starbase/binary-api-reference#rejection-reason-codes).

The table below outlines the content of field 10 (flags) of `NewOrderRequest`.

| Bit number (from last to first) | Name | Description |
| - | - | - |
| 0 | cancelOnDisconnect | Order-level cancel-on-disconnect flag. |
| 1 | postOnly | Enables post-only that amends the order price to the best bid/ask if it would be immediately executable. The amended price is then validated against price limits. Mutually exclusive with `postOnlyReject`. |
| 2 | postOnlyReject | Enables post-only that rejects the order if it would be immediately executable. Mutually exclusive with `postOnly`. |
| 3 | marketLimit | Set `limitPrice` based on the top-of-book instead of the price band. |
| 4 | MMP | The order will be subject to the default Market Maker Protection group |
| 5 | resetMmp | Unfreeze orders MMP group |
| 6 | Reserved for future use | |
| 7 | Reserved for future use | |

> [!NOTE]
>
> **No reduce-only flag**: reduce-only cannot be set per order in SBE. It exists only as a portfolio-level restriction applied by Deribit, reported as [`cancelReason = 8`](https://docs.deribit.com/starbase/binary-api-reference#cancel-reason-codes) (`REDUCE_ONLY`) when an order would increase a position. Per-order reduce-only is available on the [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) ([`private/buy`](https://docs.deribit.com/api-reference/trading/private-buy), `reduce_only`) and FIX ([`NewOrderSingle`](https://docs.deribit.com/fix-api/production/new-order-single), `ExecInst = E`) APIs.

### NewOrderResponse (200)

Response to confirm a `NewOrderRequest` was successful, sent from the exchange to the client. Any immediate fills generated by the `NewOrderRequest` will be included in the `NewOrderResponse` and will NOT be sent additionally in an `OrderFilled`.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 6 | instrumentId | int64 | 8 | Numeric instrument ID |
| 7 | limitPrice | Price9 | 8 | Price. Can differ from submitted price when post-only (amend) is enabled |
| 8 | quantity | Decimal72 | 9 | Decimal floating point order quantity accepted by the exchange |
| 10 | totalFilled | Decimal72 | 9 | Immediate fill total |
| 11 | visibleQty | Decimal72 | 9 | For iceberg orders this is the visible amount in the book. For non-icebergs this is the remaining amount (amount - filledAmount). |
| 12 | side | int8 | 1 | `1`=BUY `-1`=SELL |
| 13 | status | int8 | 1 | `1`=Active `2`=filled `3`=cancelled `4`=queued (speed bumped) |
| 14 | cancelReason | int8 | 1 | See [Cancel Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#cancel-reason-codes) |
| 15 | flags | uint16 | 2 | Order flags echoed from the submitted order. Same bits as field 10 of [`NewOrderRequest`](#neworderrequest-100). Added in schema version `19`. |
| 16 | blockLengthOfFills | uint16 | 2 | 25 (bytes). Size in bytes of each fill record in the repeating group. |
| 17 | numberOfFills | uint16 | 2 | Number of fills in the following repeating group. |
| ->18 | matchId | int64 | 8 | Transaction ID representing match. |
| ->19 | fillPrice | Price9 | 8 | Price of fill |
| ->20 | fillQty | Decimal72 | 9 | Quantity of fill |
| 21 | blockLengthOfLegs | uint16 | 2 | 34 (bytes) |
| 22 | numberOfLegs | uint16 | 2 | Indicates the length of the following repeating group containing all combo leg quantities and prices. Non-zero for trades on combo instruments only. |
| ->23 | matchId | int64 | 8 | Transaction ID representing match. |
| ->24 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->25 | legPrice | Price9 | 8 | Price of this leg in the combo instrument |
| ->26 | legQty | Decimal72 | 9 | Quantity of this leg in the combo instrument |
| ->27 | legSide | int8 | 1 | `1`=BUY `-1`=SELL |

> [!NOTE]
>
> `flags` (field 15) was added in schema version `19`. Clients that negotiate a schema version below `19` do not receive this field.

### NewOrderReject (202)

Reject generated in case a `NewOrderRequest` is unsuccessful.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 6 | instrumentId | int64 | 8 | Numeric instrument ID |
| 7 | reason | int8 | 1 | Rejection reason code. See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes) for possible values. Unsupported `timeInForce` (including values greater than `1`) is `INVALID_FIELD`. |
| 8 | details | char | 0-255 | ASCII-encoded string |


## Related topics

- [Amending an Order](https://docs.deribit.com/starbase/amending-order.md)
- [REST Order Gateway Authentication](https://docs.deribit.com/starbase/rest-authentication.md)
- [Starbase Market Maker Protection (MMP)](https://docs.deribit.com/starbase/mmp.md)
- [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md)
- [New Order Single(D) (Production FIX API)](https://docs.deribit.com/fix-api/production/new-order-single.md)