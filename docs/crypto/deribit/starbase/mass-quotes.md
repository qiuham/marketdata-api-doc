---
exchange: deribit
source_url: https://docs.deribit.com/starbase/mass-quotes
api_type: Starbase
updated_at: 2026-11-18 05:08:31.999987
---

# Mass Quotes

> Submit many two-sided quotes in one Starbase Binary API message with MassQuoteRequest, MassQuoteResponse, and MassQuoteReject message details.

## Placing multiple quotes

> [!NOTE]
>
> **Mass Quotes Limit**: Mass quotes are limited to 15 double-sided quotes.
>
> **Fill Limits**: The maximum number of fills on a single mass quote is **2000 fills for single-leg instruments** and **400 fills for combo instruments**.

> [!NOTE]
>
> **Duplicate quote handling**: When a client sends the same quote twice (identical price, amount, and instrument), Starbase **preserves** the bid and ask priorities.

> [!TIP]
>
> **Lowest-latency quoting**: Mass quotes are always MMP-enforced and therefore use the [MMP risk bypass](https://docs.deribit.com/starbase/risk-bypass.md), the lowest-latency method for market access, which skips the pre-trade risk engine. For single orders, set the `MMP` flag to get the same treatment. Most integrating clients should prefer this path. The bypass requires the MMP group's **Quantity Limit ≤ Max Quote Quantity**.

> [!WARNING]
>
> **Quote quantity validation is all-or-nothing**: If any quote entry in a `MassQuoteRequest` contains an invalid `buyAmount` or `sellAmount`, the **entire request is rejected** and a `MassQuoteReject` (232) is returned. No quotes in the message are processed. This differs from the [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) mass quote system, where each side is validated independently and one side may succeed while the other fails.

> [!WARNING]
>
> **Member portfolios cannot use the classic mass quotes API**: Once a portfolio is added to a Starbase [Member](https://docs.deribit.com/starbase/account-model.md), classic mass quoting is blocked for that portfolio. [`private/mass_quote`](https://docs.deribit.com/api-reference/trading/private-mass_quote) over [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) (WebSocket) and mass quoting over the FIX API no longer work. Mass quotes for Member portfolios must be submitted through the Starbase Binary API. Regular order entry through the standard APIs is unaffected.

> [!WARNING]
>
> **One mass-quote operating mode per portfolio**: A portfolio cannot use classic JSON-RPC/FIX mass quoting and Starbase mass quoting concurrently. Mass-quote updates replace the resting quote, so accepting both paths at the same time could produce inconsistent quote state. Select either **Classic** or **Starbase** mass-quote mode for the portfolio.

The operating mode can be switched in real time through the API or Account Panel. Before switching, stop quote submission on the current path and reconcile or cancel its resting quotes. Mass-quote enablement remains separate from regular order-entry access.

> [!NOTE]
>
> **Rate limiting and cancels**: Setting a quote's `bidQty` or `askQty` to `0` cancels that side. A `MassQuoteRequest` where **all** quantities are zero is treated as a cancel: it consumes tokens from the mass quote bucket but is never rejected due to rate limits, even when throttled. Any message containing at least one non-zero quantity is subject to normal rate limiting. See [API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md) for details.

### Updating a resting quote

Each side of a quote entry is handled independently. When a side already has a resting order, the result depends on the quantity and price sent for that side:

| Quantity (`bidQty` / `askQty`) | Price (`bidPrice` / `askPrice`) | Result |
| - | - | - |
| `NULL_QUANTITY` | `NULL_LONG` | Side left unchanged: the resting order keeps its price, remaining quantity and fills. |
| `0` | Any | Side cancelled. |
| Quantity | `NULL_LONG` | Side re-quoted at its current price, with the quantity sent as the new resting quantity. |
| `NULL_QUANTITY` | Price | Side re-quoted at the new price, with the last quoted quantity as the new resting quantity. |
| Quantity | Price | Side re-quoted at the new price and quantity. |

Any update other than leaving the side unchanged is a full replenishment of the side: the resulting resting quantity is the quantity sent (or the last quoted quantity if `NULL_QUANTITY`), regardless of fills since the previous quote. For example, quote 100, receive 12 in fills (88 resting), then send `NULL_QUANTITY` with a new price: 100 rests at the new price, so the side can be filled for up to 112 in total across the two quotes. To keep only the remaining size working, send the remaining quantity (88).

### MassQuoteRequest (130)

Place buy and/or sell orders for up to 15 instruments in one message.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | quoteId | int64 | 8 | Numeric client quote ID |
| 2 | correlationId | int64 | 8 | Client-assigned ID |
| 3 | mmpGroupId | int64 | 8 | Identifier of MMP group |
| 4 | selfMatchPreventionId | int64 | 8 | SMPToken. This order cannot match with any other orders within the same portfolio with the same token. Applies to all quotes in the batch. |
| 5 | flags | uint8 | 1 | Message-level flags (`MassQuoteFlags`). Carries `resetMmp` only. See the table below |
| 6 | blockLengthOfQuotes | uint16 | 2 | 44 (bytes) |
| 7 | numberOfQuotes | uint16 | 2 | Number of quotes in repeating group. Maximum is 15. |
| ->8 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->9 | bidPrice | Price9 | 8 | Limit price of buy side. `NULL_LONG` keeps the price of the resting buy order. See [Updating a resting quote](#updating-a-resting-quote) |
| ->10 | askPrice | Price9 | 8 | Limit price of sell side. `NULL_LONG` keeps the price of the resting sell order. See [Updating a resting quote](#updating-a-resting-quote) |
| ->11 | bidQty | Decimal72 | 9 | Buy quantity. 0 to cancel existing buy orders. `NULL_QUANTITY` reuses the last quoted buy quantity. See [Updating a resting quote](#updating-a-resting-quote) |
| ->12 | askQty | Decimal72 | 9 | Sell quantity. 0 to cancel existing sell orders. `NULL_QUANTITY` reuses the last quoted sell quantity. See [Updating a resting quote](#updating-a-resting-quote) |
| ->13 | bidFlags | uint16 | 2 | Per-quote flags (`OrderFlags`) for the buy side. See the table below |
| ->14 | askFlags | uint16 | 2 | Per-quote flags (`OrderFlags`) for the sell side. See the table below |

The table below outlines the content of field 5 (`flags`, type `MassQuoteFlags`) of `MassQuoteRequest`. This message-level field carries `resetMmp` only. All other quote behavior is set per side in `bidFlags`/`askFlags`.

| Bit number (from last to first) | Name | Description |
| :- | :- | :- |
| 0 | resetMmp | `0`=False `1`=True If an MMP freeze is active on the message's `mmpGroupId`, this flag will remove the freeze before processing the rest of the message. Keep in mind there is a mandatory `1` second freeze that cannot be overruled |
| 1 | Reserved for future use | |
| 2 | Reserved for future use | |
| 3 | Reserved for future use | |
| 4 | Reserved for future use | |
| 5 | Reserved for future use | |
| 6 | Reserved for future use | |
| 7 | Reserved for future use | |

The table below outlines the content of fields 13/14 (`bidFlags`/`askFlags`, type `OrderFlags`) of `MassQuoteRequest`. These are the same flags as field 10 of [`NewOrderRequest`](https://docs.deribit.com/starbase/placing-new-order#neworderrequest-100) and are set independently per quote side.

| Bit number (from last to first) | Name | Description |
| - | - | - |
| 0 | cancelOnDisconnect | Tags this quote side for [cancel-on-disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md). Set per side. An untagged side keeps resting when the session drops. |
| 1 | postOnly | Enables post-only that amends the quote price to the best bid/ask if it would be immediately executable. The amended price is then validated against price limits. Mutually exclusive with `postOnlyReject`. |
| 2 | postOnlyReject | Enables post-only that rejects the quote if it would be immediately executable. Mutually exclusive with `postOnly`. |
| 3 | marketLimit | Set `limitPrice` based on the top-of-book instead of the price band. |
| 4 | MMP | The order will be subject to the default Market Maker Protection group |
| 5 | resetMmp | Unfreeze orders MMP group |
| 6 | Reserved for future use | |
| 7 | Reserved for future use | |

> [!NOTE]
>
> **Session-level cancel-on-disconnect**: setting `cancelOnDisconnect` on [`LogonRequest`](https://docs.deribit.com/starbase/session-messages#logonrequest-1) covers every order and quote submitted on that session, including both `NewOrderRequest` and `MassQuoteRequest`, with no need to tag each side individually. The per-side `cancelOnDisconnect` flag remains available. See [Session-level CoD](https://docs.deribit.com/starbase/cancel-on-disconnect.md#session-level-cod).

### MassQuoteResponse (230)

Acknowledges the successful execution of a `MassQuoteRequest`. Quotes do not have a separate fillAmount and amount. A quote's amount will always be what's still available for execution. As such, in a MassQuoteResponse, the amounts of the quotes returned will already incorporate the accompanying fills.

Individual quote sides that aggress may be speed bumped, indicated by `bidStatus = 8` or `askStatus = 8` (Queued). Once the speed bump period expires, an unsolicited `MassQuoteOrdersPlaced` message is sent for the placed sides. See [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md) for details.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | quoteId | int64 | 8 | Numeric client quote ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | mmpGroupId | int64 | 8 | Identifier of MMP group |
| 6 | receiveTime | int64 | 8 | Nanoseconds since epoch. Time of receipt of order on the gateway. |
| 7 | blockLengthOfQuotes | uint16 | 2 | 76 (bytes) |
| 8 | numberOfQuotes | uint16 | 2 | Number of quotes in repeating group. Maximum is 15. |
| ->9 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->10 | bidOrderId | int64 | 8 | Numeric exchange assigned order ID |
| ->11 | askOrderId | int64 | 8 | Numeric exchange assigned order ID |
| ->12 | bidPrice | Price9 | 8 | Limit price of buy side (possibly different from submitted price if postOnly) |
| ->13 | askPrice | Price9 | 8 | Limit price of sell side (possibly different from submitted price if postOnly) |
| ->14 | bidQty | Decimal72 | 9 | Quantity remaining of buy side |
| ->15 | askQty | Decimal72 | 9 | Quantity remaining of sell side |
| ->16 | bidFilledQty | Decimal72 | 9 | Buy quantity filled |
| ->17 | askFilledQty | Decimal72 | 9 | Sell quantity filled |
| ->18 | bidStatus | int8 | 1 | `0`=Inactive `1`=Unmodified `2`=QuantityReduced `3`=Updated `4`=Filled `5`=CanceledByRequest `6`=CanceledByMmp `7`=CanceledBySelfMatch `8`=Queued |
| ->19 | askStatus | int8 | 1 | Refer to bidStatus for possible values |
| ->20 | bidRejectReason | int8 | 1 | Rejection reason code. See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes) for possible values. |
| ->21 | askRejectReason | int8 | 1 | Rejection reason code. See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes) for possible values. |
| 22 | blockLengthOfBidFills | uint16 | 2 | 32 (bytes) |
| 23 | numberOfBidFills | uint16 | 2 | Indicates the length of the following repeating group containing all immediate buy fills when the order was submitted |
| ->24 | matchId | int64 | 8 | Transaction ID representing match |
| ->25 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->26 | fillPrice | Price9 | 8 | Price of fill |
| ->27 | fillQty | Decimal72 | 9 | Quantity of fill |
| 28 | blockLengthOfAskFills | uint16 | 2 | 32 (bytes) |
| 29 | numberOfAskFills | uint16 | 2 | Indicates the length of the following repeating group containing all immediate sell fills when the order was submitted |
| ->30 | matchId | int64 | 8 | Transaction ID representing match |
| ->31 | instrumentId | int64 | 8 | Numeric instrument ID |
| ->32 | fillPrice | Price9 | 8 | Price of fill |
| ->33 | fillQuantity | Decimal72 | 9 | Quantity of fill |
| 34 | blockLengthOfLegs | uint16 | 2 | 33 (bytes) |
| 35 | numberOfLegs | uint16 | 2 | Indicates the length of the following repeating group containing all combo leg quantities and prices. Non-zero for trades on combo instruments only. |
| ->36 | matchId | int64 | 8 | Transaction ID representing match. |
| ->37 | instrumentId | int64 | 8 | Numeric instrument ID. |
| ->38 | legPrice | Price9 | 8 | Price of this leg in the combo instrument |
| ->39 | legQty | Decimal72 | 9 | Quantity of this leg in the combo instrument |
| ->40 | legSide | int8 | 1 | `1`=BUY `-1`=SELL |

### MassQuoteReject (232)

Reject generated in case a `MassQuoteRequest` is unsuccessful.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | transactTime | int64 | 8 | Nanoseconds since epoch. Time of entry into the order book |
| 2 | execId | int64 | 8 | Exchange-assigned event ID |
| 3 | quoteId | int64 | 8 | Numeric client quote ID |
| 4 | correlationId | int64 | 8 | Client-assigned ID |
| 5 | mmpGroupId | int64 | 8 | Identifier of MMP group |
| 6 | reason | int8 | 1 | `0`=SystemError `1`=InvalidMmpGroup `2`=MmpGroupDisabled `3`=MmpGroupFrozen `4`=TooManyQuotes `5`=InvalidInstrument `6`=RateLimit `7`=PortfolioLocked `8`=DuplicateInstrument `9`=MmpMinFreezeTimeNotElapsed |
| 7 | details | char | 0-255 | ASCII-encoded string |


## Related topics

- [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md)
- [Mass Quotes Specifications](https://docs.deribit.com/articles/mass-quotes-specifications.md)
- [private/mass_quote](https://docs.deribit.com/api-reference/trading/private-mass_quote.md)
- [Mass Quote(i) (Production FIX API)](https://docs.deribit.com/fix-api/production/mass-quote.md)
- [Mass Quote Acknowledgement(b) (Production FIX API)](https://docs.deribit.com/fix-api/production/mass-quote-acknowledgement.md)