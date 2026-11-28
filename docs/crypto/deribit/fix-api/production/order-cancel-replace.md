---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/order-cancel-replace
api_type: FIX
updated_at: 2026-11-28 18:58:40.431593
---

# Order Cancel/Replace Request(G) (Production FIX API)

> OrderCancelReplaceRequest(G) modifies the price or quantity of a working order on the Deribit production FIX API without cancelling and resubmitting it.

To change/edit the parameters of an existing order.

From Release 1.3.10, it is possible to amend an order by `ClOrdID` or
`DeribitLabel`, and `OrigClOrdId` is not required anymore, however amending
orders by `OrigClOrdId` is noticeably faster.

#### IMPORTANT:

* to change the order using `ClOrdID` or `DeribitLabel`, this must be the only existing order with such `ClOrdID` or `DeribitLabel`. Multiple orders with the same `ClOrdID` or `DeribitLabel` won't be amended that way.
* when possible it is recommended to use faster `OrigClOrdId`

> [!NOTE]
>
> On spot instruments matched on Coinbase Exchange, `ExecInst`(`18`) accepts only
> `6A` and `DisplayQty`(`1138`) is rejected. See
> [Spot trading venues](https://docs.deribit.com/articles/spot-trading-venues.md).

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 11 | `ClOrdID` | String | Required if `DeribitLabel`, `OrigClOrdId` are absent | Original order identifier assigned by the user, max 64 grapheme clusters. **This tag operates on grapheme clusters. A grapheme cluster is a user-perceived character, which can be represented by several unicode codepoints. Please refer to [Unicode specification](https://unicode.org/reports/tr29/) for more details about the grapheme clusters** |
| 41 | `OrigClOrdId` | String | Required if `DeribitLabel`, `ClOrdID` are absent | Order identifier assigned by Deribit over the user one |
| 100010 | `DeribitLabel` | String | Required if `OrigClOrdId`, `ClOrdID` are absent | A custom label for your order, max 64 grapheme clusters. Can be used by [`Order Cancel Request`(`F`)](https://docs.deribit.com/fix-api/production/order-cancel-request) to amend the order later on |
| 55 | `Symbol` | String | Yes | Instrument symbol, e.g., **BTC-1JAN16** |
| 62 | `ValidUntilTime` | UTCTimestamp | No | Indicates expiration time of indication message, in UTC |
| 15 | `Currency` | String | No | To speed up the search of the order by `DeribitLabel` or `ClOrdID` |
| 54 | `Side` | char | Yes | Should match the original order's side.Valid values: <ul><li>`1` = Buy,</li> <li>`2` = Sell</li></ul> |
| 38 | `OrderQty` | Qty | Yes | Order quantity. Depends on `QtyType`. When `QtyType` is set to `Units`, the `OrderQty` is specified in USD for perpetual and inverse futures, in the underlying base currency coin for linear futures, or in the amount of cryptocurrency contracts for options. The system will automatically convert `Units` to `Contracts` when the order is placed. **Please, note that Quantity is by default defined in Contract units corresponding to the ContractMultiplier in SecurityList** |
| 40 | `OrdType` | char | No | Currently `2` - 'limit' |
| 44 | `Price` | Price | No | Order price (for advanced options orders it could be volatility or USD value if applicable) |
| 18 | `ExecInst` | MultipleCharValue | No | Currently is used to mark POST ONLY orders and REDUCE ONLY orders.POST ONLY valid values:<ul><li>`6` = "Participate don't initiate", </li><li>`A` = "No cross" (only together with 6, "`6A`" -- REJECT POST ONLY when the order is put to the order book unmodified or the request is rejected and order is cancelled),</li></ul> REDUCE ONLY valid values: <ul><li>`E` = "Do not increase - DNI"</li></ul> |
| 854 | `QtyType` | Int | No | Type of quantity. Valid values:<ul><li>`0` = `Units`,</li><li>`1` = `Contracts`</li></ul> Default is `Contracts`. When `QtyType` is `Units`, then for perpetual and inverse futures the `OrderQty` is in USD units, and for linear futures it is the underlying base currency coin, and for options it is the amount of corresponding cryptocurrency (e.g., BTC or ETH). The `Units` will be recalculated into the system's `Contracts` on server automatically when the order is placed. |
| 1138 | `DisplayQty` | Qty | No | The (max) quantity to be displayed in the orderbook. |
| 9008 | `DeribitMMProtection` | Boolean | No | Order Market Maker Protection (MMP) flag, if it is absent then the current MMP flag of the order is not changed. `N` removes the flag if it is set. **Important: manual admin action is necessary to activate Market Maker Protection (MMP) for an account** |

### Response

See `New Order Single`(`D`) response.


## Related topics

- [Order Cancel Reject(9) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-reject.md)
- [Order Cancel Request(F) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-request.md)
- [Order Mass Cancel Request(q) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-cancel-request.md)
- [Order Mass Cancel Report(r) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-cancel-report.md)
- [Quote Cancel(Z) (Production FIX API)](https://docs.deribit.com/fix-api/production/quote-cancel.md)