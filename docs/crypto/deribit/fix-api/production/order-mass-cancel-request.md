---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/order-mass-cancel-request
api_type: FIX
updated_at: 2026-11-27 19:00:51.970794
---

# Order Mass Cancel Request(q) (Production FIX API)

> OrderMassCancelRequest(q) cancels all open orders matching filters like instrument, side, or underlying in one Deribit production FIX API message.

`Order Mass Cancel Request`(`q`) message will trigger cancellation of a group of
orders.

From Release 1.3.10, it is possible to cancel orders by DeribitLabel, and the
option `10` of the `MassCancelRequestType`(`530`) has been added.

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 11 | `ClOrdID` | String | Yes | Unique ID of `Order Mass Cancel Request`(`q`) as assigned by the client, max 64 grapheme clusters. **This tag operates on grapheme clusters. A grapheme cluster is a user-perceived character, which can be represented by several unicode codepoints. Please refer to [Unicode specification](https://unicode.org/reports/tr29/) for more details about the grapheme clusters** |
| 530 | `MassCancelRequestType` | int | Yes | Specifies the type of cancellation requested. Valid values:<ul><li>`7` = all orders,</li> <li>`5` = orders by security type,</li> <li>`1` = orders by symbol, </li><li>`10` = orders by DeribitLabel</li></ul> |
| 100010 | `DeribitLabel` | String | if `MassCancelRequestType`(`530`)=10 | A custom label for your order, max 64 grapheme clusters. Can be used by [`Order Cancel Request`(`F`)](https://docs.deribit.com/fix-api/production/order-cancel-request) to amend the order later on. Equivalent of REST/WS `cancel_by_label` |
| 167 | `SecurityType` | String | If `MassCancelRequestType`(`530`)=5 | Describes type of security. Possible values: <ul><li>`FUT` for futures,</li><li> `OPT` for options,</li> <li> `FUTCO` for future combo,</li> <li>`OPTCO` for option combo</li></ul>  |
| 55 | `Symbol` | String | If `MassCancelRequestType`(`530`)=1 | The symbols for which to cancel all orders |
| 15 | `Currency` | String | No | To cancel only certain currency if it is applicable. See [`Security List Request`(`x`)](https://docs.deribit.com/fix-api/production/security-list-request) |
| 9031 | `FreezeQuotes` | Boolean | No | Whether or not to reject incoming quotes for 1 second after cancelling |

### Response

After the cancellation, the server responds with
an `Order Mass Cancel Report`(`r`).


## Related topics

- [Order Mass Cancel Report(r) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-cancel-report.md)
- [Order Cancel Request(F) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-request.md)
- [Quote Cancel(Z) (Production FIX API)](https://docs.deribit.com/fix-api/production/quote-cancel.md)
- [Order Cancel/Replace Request(G) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-replace.md)
- [Order Mass Status Request(AF) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-status-request.md)