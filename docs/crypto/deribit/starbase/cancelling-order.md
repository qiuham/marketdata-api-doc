---
exchange: deribit
source_url: https://docs.deribit.com/starbase/cancelling-order
api_type: Starbase
updated_at: 2026-11-18 18:59:10.744569
---

# Cancelling an Order

> Cancel a working order with the Starbase Binary API. Covers CancelOrderRequest, CancelOrderResponse, and CancelOrderReject message flow and error codes.

## Cancelling an order

> [!NOTE]
>
> **Cross-Session Cancelling**: Orders can be cancelled from a different SBE session than the one that submitted them. An order submitted on gateway side A can be cancelled on side B of the same pair.
>
> **Response Routing**: The session that sends the cancel receives `CancelOrderResponse`. When that session is not the one that submitted the order, and the submitting session has negotiated schema version `17` or later, the submitting session receives an unsolicited [`OrdersCanceled` (310)](https://docs.deribit.com/starbase/unsolicited-events#orderscanceled-310). The `OrdersCanceled` layout is unchanged (additive, backward-compatible). Sessions negotiated below `17` keep the previous routing: `CancelOrderResponse` is delivered to both sessions. Fills stay on the submitting session. See [Cross-session acknowledgements](https://docs.deribit.com/starbase/amending-order.md#cross-session-acknowledgements).

### CancelOrderRequest (120)

Request to cancel an existing order by its client order ID. This message cannot cancel quotes.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | clientOrderId | int64 | 8 | Numeric client order ID |
| 2 | correlationId | int64 | 8 | Client-assigned ID |
| 3 | instrumentId | int64 | 8 | Instrument identifier |

### CancelOrderByIdRequest (125)

Request to cancel an existing order by its exchange-assigned order ID. Use this when the `clientOrderId` is not known. This message cannot cancel quotes. Responses are the same as for `CancelOrderRequest`: a `CancelOrderResponse` (220) on success or a `CancelOrderReject` (222) on failure.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | orderId | int64 | 8 | Numeric exchange-assigned order ID |
| 2 | correlationId | int64 | 8 | Client-assigned ID |
| 3 | instrumentId | int64 | 8 | Instrument identifier |

### CancelOrderResponse (220)

Response to confirm a `CancelOrderRequest` or `CancelOrderByIdRequest` was successful, sent to the session that sent the cancel. When the cancel is sent from a different session than the one that submitted the order, the submitting session is notified with an unsolicited [`OrdersCanceled` (310)](https://docs.deribit.com/starbase/unsolicited-events#orderscanceled-310) once that session has negotiated schema version `17` or later. See [Cross-session acknowledgements](https://docs.deribit.com/starbase/amending-order.md#cross-session-acknowledgements).

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of exit out of the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 6 | instrumentId | int64 | 8 | Numeric instrument ID |
| 7 | receiveTime | int64 | 8 | Nanoseconds since epoch. Time of receipt of cancellation on the gateway. |
| 8 | quantity | Decimal72 | 9 | Order quantity known to the matching engine. Added in schema version `16`. |
| 9 | totalFilled | Decimal72 | 9 | Cumulative filled quantity. Cancelled/leaves quantity is `quantity - totalFilled`. Added in schema version `16`. |

> [!NOTE]
>
> `quantity` (field 8) and `totalFilled` (field 9) were added in schema version `16`. Clients that negotiate a schema version below `16` do not receive these fields.

### CancelOrderReject (222)

Reject generated in case a `CancelOrderRequest` is unsuccessful.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | clientOrderId | int64 | 8 | Numeric client order ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | orderId | int64 | 8 | Numeric exchange assigned order ID |
| 6 | instrumentId | int64 | 8 | Numeric instrument ID |
| 7 | reason | int8 | 1 | `0`=Error `1`=UnknownOrder `2`=ClientPermissionError `3`=NotAllowedByMarketState `4`=CancelPending `5`=InLiquidation `6`=InvalidInstrument `7`=TimeInForce `8`=SpeedBumpConvertedToIoc |
| 8 | details | char | 0-255 | ASCII-encoded string |


## Related topics

- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md)
- [Amending an Order](https://docs.deribit.com/starbase/amending-order.md)
- [Order Cancel Request(F) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-request.md)
- [Starbase Unsolicited Events](https://docs.deribit.com/starbase/unsolicited-events.md)
- [Rate Limits](https://docs.deribit.com/articles/rate-limits.md)