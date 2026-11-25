---
exchange: deribit
source_url: https://docs.deribit.com/starbase/amending-order
api_type: Starbase
updated_at: 2026-11-25 19:00:46.335976
---

# Amending an Order

> Amend existing orders using the Starbase Binary API including AmendOrderRequest, AmendOrderResponse, and AmendOrderReject messages.

## Amending an existing order

> [!NOTE]
>
> **Cross-Session Amending**: Orders can be amended from a different SBE session than the one that submitted them. An order submitted on gateway side A can be amended on side B of the same pair.
>
> **Response Routing**: When those sessions differ, `AmendOrderResponse` is delivered to both the session that sent the `AmendOrderRequest` and the session that submitted the order. Fills stay on the submitting session. See [Cross-session acknowledgements](#cross-session-acknowledgements).

### Cross-session acknowledgements

On a hot-hot A/B gateway pair, an amend or cancel can be sent from the side that did not place the order.

**Amend.** When the requesting session and the submitting session differ, [`AmendOrderResponse`](#amendorderresponse-210) is delivered to both. The matching-engine event carries two session stamps: the session that submitted the order, and the session that sent the request. Each gateway forwards the acknowledgement to its own session. Both copies share `clientOrderId`, `orderId`, and `correlationId`. The per-session sequence number differs. Dedupe the copies by `correlationId` and `orderId` across the two sessions.

**Cancel.** The session that sends the cancel receives [`CancelOrderResponse`](https://docs.deribit.com/starbase/cancelling-order#cancelorderresponse-220). When that session is not the one that submitted the order, and the submitting session has negotiated schema version `17` or later, the submitting session receives an unsolicited [`OrdersCanceled` (310)](https://docs.deribit.com/starbase/unsolicited-events#orderscanceled-310). Schema version `17` is additive and backward-compatible: the `OrdersCanceled` layout is unchanged. Sessions negotiated below `17` keep the previous routing, with `CancelOrderResponse` delivered to both sessions. See [Cancelling an Order](https://docs.deribit.com/starbase/cancelling-order.md).

Fills are delivered to the session that submitted the order. A fill carries that submitting session only, so after an amend sent on the other side the fill still arrives on the owning session.

A later amend follows the same split as above. A later cancel from another session again sends `CancelOrderResponse` to the requester and `OrdersCanceled` to the owner. Any fill stays on the owning session.

### Pending amend limit

The number of **unacknowledged amend (replace) requests per order** is capped. An amend counts as pending from the time the exchange receives it until its `AmendOrderResponse` or `AmendOrderReject` is generated:

| Order type | Max pending amends |
| - | - |
| Normal orders | 4 |
| OCO / reduce-only orders | 1 |

Once the cap is reached, any further amend on that order (the 5th for a normal order, the 2nd for an OCO or reduce-only order) is rejected with [`AmendOrderReject`](#amendorderreject-212) reason `19` ([`TOO_MANY_PENDING_REPLACES`](https://docs.deribit.com/starbase/binary-api-reference#rejection-reason-codes)) until one of the pending amends is acknowledged.

This cap applies per order, not per session or connection: it is independent of the [gateway rate limits](https://docs.deribit.com/starbase/api-rate-limits.md) and is not a gateway-side concurrency limit. OCO and per-order reduce-only orders originate on the other Deribit APIs (see [Placing a New Order](https://docs.deribit.com/starbase/placing-new-order.md#neworderrequest-100)); the tighter cap applies to those orders regardless of which API amends them.

### AmendOrderRequest (110)

Request to change the modifiable fields of an existing order.

> [!NOTE]
>
> **Null values**: Some optional fields use `NULL_LONG` / `NULL_QUANTITY` (`0x8000000000000000L`) as a sentinel to indicate "not set". For example, set `displayAmount = NULL_QUANTITY` to keep the order non-iceberg.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | clientOrderId | int64 | 8 | Numeric client order ID |
| 2 | correlationId | int64 | 8 | Client-assigned ID |
| 3 | instrumentId | int64 | 8 | Numeric instrument ID |
| 4 | limitPrice | Price9 | 8 | New price |
| 5 | quantity | Decimal72 | 9 | New quantity |
| 6 | showQty | Decimal72 | 9 | New visible amount for iceberg orders. Setting this field to any value (including equal to `amount`) marks the order as an iceberg order. To submit a non-iceberg order, omit this field or set it to `NULL_QUANTITY`. Iceberg orders are not supported for options and combo instruments. |
| 7 | flags | uint16 | 2 | See the table below. |

The table below outlines the content of field 7 (flags) of `AmendOrderRequest`.

| Bit number (from last to first) | Name | Description |
| - | - | - |
| 1 | postOnly | Enables post-only that amends the order to the best bid/ask if the edit would make it immediately executable. The amended price is then validated against price limits. Mutually exclusive with `postOnlyReject`. |
| 2 | postOnlyReject | Enables post-only that rejects the edit if it would make the order immediately executable. The original order remains in the book unchanged. Mutually exclusive with `postOnly`. |
| 3 | Reserved for future use | |
| 4 | Reserved for future use | |
| 5 | Reserved for future use | |
| 6 | Reserved for future use | |
| 7 | Reserved for future use | |
| 8 | Reserved for future use | |
| 9-16 | Reserved for future use | |

> [!NOTE]
>
> **No reduce-only flag**: reduce-only cannot be set per order in SBE, on amend or on submit. See [Placing a New Order](https://docs.deribit.com/starbase/placing-new-order.md#neworderrequest-100) for the alternatives.

### AmendOrderResponse (210)

Response to confirm an `AmendOrderRequest` was successful, sent from the exchange to the client. When the amend is sent from a different session than the one that submitted the order, this response is delivered on both sessions. See [Cross-session acknowledgements](#cross-session-acknowledgements). Any immediate fills generated by the `AmendOrderRequest` will be included in the `AmendOrderResponse` and will NOT be sent additionally in an `OrderUpdate`.

If the amendment causes the order to aggress and it is speed bumped, the `AmendOrderResponse` is sent immediately with `orderState = 4` (queued). Once the speed bump period expires, an unsolicited `OrderPlaced` message is sent. See [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md) for details.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 6 | instrumentId | int64 | 8 | Numeric instrument ID |
| 7 | limitPrice | Price9 | 8 | Price. Can differ from submitted price when post-only (amend) is enabled |
| 8 | quantity | Decimal72 | 9 | Order quantity accepted by the exchange after the amend |
| 9 | totalFilled | Decimal72 | 9 | Filled quantity |
| 10 | visibleQty | Decimal72 | 9 | Currently visible in market data |
| 11 | receiveTime | int64 | 8 | Nanoseconds since epoch. Time of receipt of order on the gateway. |
| 12 | status | int8 | 1 | `1`=Active `2`=filled `3`=cancelled `4`=queued (speed bumped) |
| 13 | cancelReason | int8 | 1 | See [Cancel Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#cancel-reason-codes) |
| 14 | blockLengthOfFills | uint16 | 2 | 24 (bytes) |
| 15 | numberOfFills | uint16 | 2 | Indicates the length of the following repeating group containing all immediate fills when the order was submitted |
| ->16 | matchId | int64 | 8 | Transaction ID representing match, shared by all fills within match |
| ->17 | fillPrice | Price9 | 8 | Price of fill |
| ->18 | fillQty | Decimal72 | 9 | Quantity of fill |
| 19 | blockLengthOfLegs | uint16 | 2 | 33 (bytes) |
| 20 | numberOfLegs | uint16 | 2 | Indicates the length of the following repeating group containing all combo leg quantities and prices. Non-zero for trades on combo instruments only. |
| ->21 | matchId | int64 | 8 | Transaction ID representing match. |
| ->22 | instrumentId | int64 | 8 | Numeric instrument ID. |
| ->23 | legPrice | Price9 | 8 | Price of this leg in the combo instrument |
| ->24 | legQty | Decimal72 | 9 | Quantity of this leg in the combo instrument |
| ->25 | legSide | int8 | 1 | `1`=BUY `-1`=SELL |

### AmendOrderReject (212)

Reject generated in case an `AmendOrderRequest` is unsuccessful.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 6 | instrumentId | int64 | 8 | Numeric instrument ID |
| 7 | reason | int8 | 1 | Rejection reason code. See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes) for possible values. |
| 8 | details | char | 0-255 | ASCII-encoded string |


## Related topics

- [Order Cancel/Replace Request(G) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-replace.md)
- [Starbase Market Maker Protection (MMP)](https://docs.deribit.com/starbase/mmp.md)
- [Starbase API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md)