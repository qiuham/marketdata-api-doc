---
exchange: deribit
source_url: https://docs.deribit.com/changelogs/fix
api_type: Changelog
updated_at: 2026-11-16 20:31:59.197598
---

# FIX API Changelog

> Release notes for the Deribit FIX API covering new tags, message changes, session behavior updates, and backward-compatibility announcements.

**Release 10.11.2026**

> [!NOTE]
>
> This release was postponed from 5 November 2026 to 10 November 2026.

Qualifying Deribit Block RFQ trades with delayed publication are omitted from FIX market data until they are published. The delay and the size thresholds are the same as for the public JSON-RPC trade feeds. See the [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md).

`OpenInterest` (`746`) on `Market Data Snapshot/Full Refresh` (`W`) and `Market Data Incremental Refresh` (`X`) is the open interest as of 8 hours ago, for all futures and options. This applies to all open interest, regardless of how the trades were executed (on-screen, Block Trade or Block RFQ), not only to Block RFQ trades with delayed publication. Real-time open interest is no longer available.

`TradeVolume24h` (`100087`) on those messages follows the combined 24-hour volume: real-time volume over the last 24 hours plus delayed Block RFQ volume from the 24-hour window that ends 8 hours ago. FIX does not return the `volume_realtime` / `volume_delayed` breakdown.

**Release 13.10.2026**

The named MMP group limit of 16 now applies per currency pair. Each pair, for example `btc_usd` and `btc_usdc`, has its own budget of 16 named groups.

The FIX rejection text names the currency pair that hit the limit.

**Release 18.08.2026**

For spot instruments routed to Coinbase Exchange (CBE), several order-entry fields are restricted:

* `OrdType` (`40`): only `1` = Market, `2` = Limit and `4` = Stop Limit are accepted.
* `TimeInForce` (`59`): `0` = Good Til Day is rejected for all spot.
* `ExecInst` (`18`): only `6A` (post-only with reject) is accepted. A bare `6` is rejected with `post_only_not_allowed`, and `E` (reduce only) with `reduce_only_not_allowed`.
* `DisplayQty` (`1138`): rejected with `iceberg_not_allowed`.
* `DeribitConditionTriggerMethod`: required on routed stop-limits and must be `2` = trade.
* `MDEntryType` (`269`): `2` = Trade is rejected in market data requests; `0` = Bid and `1` = Offer in the same request are still served.

**Release 30.06.2026**

`Security List` (`y`): `UnderlyingSecurityType` (`310`) is now included in the response for all instruments. Possible values: `CRYPTO`, `COMMODITY`, `EQUITY`.

**Release 17.02.2026**

`Execution Reports` (`8`): added nonmandatory tag `CashOrderQty` (`152`) to differentiate value based orders from quantity based orders. For value based orders (BTC & ETH inverse futures and perpetuals where the order size is specified as a USD amount), both `OrderQty` (`38`) and `CashOrderQty` (`152`) are present and equal. For quantity based orders, `CashOrderQty` is absent.

**Release 07.10.2025**

Removed deprecated RFQ messages as previously announced.

* Removed Quote Request (R)
* Removed Quote Request Reject (AG)
* Removed Quote Status Report (AI)
* Removed RFQ Request (AH)

**Release 10.06.2025**

* `MaxShow` (`210`) is replaced with `DisplayQty` (`1138`). The iceberg orders cannot be fully invisible anymore. Setting `DisplayQty` (`1138`) = 0 is interpreted as no hidden volume, i.e. the full order quantity is displayed to the market. Omitting the field gives the same result.
* `Execution Reports` (`8`): added nonmandatory tag `RefreshQty` (`1088`).

**Release 06.03.2025**

Support for non-printable ASCII characters (such as control characters ranging from 0x00 to 0x1F) in string values has been removed to ensure compliance with the WS/REST API. Attempting to use non-printable ASCII characters will now result in a decoding error.

**Release 04.02.2025**

* `Order Cancel/Replace Request` (`G`): removed support of undocumented tag `MaxShow` (`210`) in compliance with the WS/REST API.
* `Order Mass Status Request` (`AF`): added the `History` (`10`) value of the `MassStatusReqType` (`585`) tag for retrieving history of orders that have been partially or fully filled; added optional tags `OrderHistoryIncludeUnfilled` (`9037`), `OrderHistoryOffset` (`9039`) and `TotNumReports` (`911`).

**Release 03.09.2024**

`New Order Single` (`D`) and `Order Cancel/Replace Request` (`G`) once again support `QtyType=Units`, allowing the `OrderQty` to be sent in units (amount) instead of contracts.

**Release 08.08.2024**

`Order Mass Cancel Request` (`q`): added `FreezeQuotes` (`9031`) tag.

**Release 03.07.2024**

* `Mass Quote Acknowledgement` (`b`): added more values of `QuoteEntryStatus` (`1167`): `18 = Canceled by MM`, `19 = Replaced`, `20 = Filled`, `21 = Open`, `22 = Closed`, `23 = Triggered`, `24 = Untriggered`, `25 = Unknown`.
* `MMProtection Limits` (`MM`): added `ProtectionVegaLimit` (`20118`).

**Release 04.06.2024**

* `New Order Single` (`D`): added nonmandatory tag `ValidUntilTime` (`62`).
* `Order Cancel/Replace Request` (`G`): added nonmandatory tag `ValidUntilTime` (`62`).
* `Mass Quote` (`i`): added nonmandatory tag `ValidUntilTime` (`62`).
* `Execution Reports` (`8`): added nonmandatory tags `IsLiquidation` (`9034`), `IsRebalance` (`9035`) and `IsRiskReducing` (`9036`).
* `SecurityListRequest` (`x`): added `Currency`, `SecurityType` and `SecondaryCurrency`.

**Release 09.03.2024**

* `SecurityStatusRequest` (`e`): added subscription.
* `SecurityStatus` (`f`): added `Text` field.
* Changed scope for `MMProtection Limits` (`MM`) from `account` to `trade`.

**Release 13.02.2024**

* Added `Mass Quote` (`i`).
* Added `Mass Quote Acknowledgement` (`b`).
* `Execution Reports` (`8`): added nonmandatory tags `MMPGroup` (`9019`), `QuoteSetID` (`302`), `QuoteID` (`117`) and `QuoteEntryID` (`299`) related to Mass Quoting.
* Added `Quote Cancel` (`Z`).
* `Mass Cancel Report` (`r`): added one more type for `MassCancelRequestType`; added an optional field `QuoteCancelType` for mass cancel reports generated by `Quote Cancel` (`Z`); `ClOrdID` is no longer a required tag.
* `MMProtection Reset` (`MZ`) and `MMProtection Limits` (`MM`): added optional `MMPGroup`.

**Release 12.12.2023**

Fixed an issue where `Reject` (`3`) was incorrectly returned instead of `OrderCancelReject` (`9`), with the specified `ClOrdID`, `DeribitLabel`, or `OrigClOrdId`, in response to an `Order Cancel Request` (`F`).

**Release 02.11.2023**

`User Request` (`BE`): added `CROSS` as currency.

**Release 27.09.2023**

`DeribitLiquidation` is hidden from the public for the first hour after the trade (to prevent abuse).

**Release 06.07.2023**

Changed `MMProtectionLimits` and `MMProtectionReset` to work with a currency pair instead of a single currency.

**Release 13.06.2023**

* Added fields `NoTickRules` (`1205`), `StartTickPriceRange` (`1206`) and `TickIncrement` (`1208`) to the instrument for tick size steps.
* Added option `DisplayIncrementSteps` (`9018`) to `Logon` and `Security List Request` (`x`) so the client can enable receiving the above-mentioned new fields in the instrument.

**Release 09.06.2023**

Added the following messages: `TradeCaptureReportRequest` (`AD`), `TradeCaptureReportRequestAck` (`AQ`) and `TradeCaptureReport` (`AE`). Clients can now utilize these to subscribe for receiving reports on their own trades.

**Release 21.03.2023**

* Added the possibility to search closed orders by `ClOrdID` or `DeribitLabel` via `OrderMassStatusRequest`.
* Incremental refresh for indices now has 1 entry instead of 2.
* BTC-DVOL and ETH-DVOL are renamed in compliance with other indices: `BTCDVOL_USDC-DERIBIT-INDEX`, `ETHDVOL_USDC-DERIBIT-INDEX`.

**Release 16.02.2023**

* `SecurityList` (`y`): added new value `FXSPOT` of `SecurityType` for the currency exchange spot market.
* `SecurityList` (`y`): added `PriceQuoteCurrency` (`1524`).

**Release 13.10.2022**

Documentation alignment.

**Release 30.03.2022**

* Added `Security Definition Request` (`c`).
* Added `Security Definition` (`d`).
* Added `Quote Request` (`R`).
* Added `Quote Request Reject` (`AG`).
* Added `Quote Status Report` (`AI`).
* Added `RFQ Request` (`AH`).

**Release 21.12.2021**

* `MarketData Request` (`V`): added `DeribitShowBlockTradeId` (`9012`).
* `MarketData` (`W`) and (`X`): added `TrdMatchID` (`880`) as block trade ID.

**Release 13.10.2021**

`MarketData Request` (`V`): added `DeribitSkipBlockTrades` (`9011`).

**Release 10.08.2021**

Added the possibility to use the client's `ClOrdID` and `DeribitLabel` in `Order Cancel Request` (`F`), `Order Mass Cancel Request` (`q`) and `Order Cancel/Replace Request` (`G`) without an exchange-generated `OrigClOrdID` (equivalent of REST/WS `cancel_by_label` etc.).

**Release 14.07.2021**

* Added `Sequence Reset` (`4`).
* `Security List Request` (`x`): added `SubscriptionRequestType` (`263`) so clients can get notifications about new or terminated instruments.
* `SecurityList` (`y`): added `SecurityStatus` (`965`) in the notifications.

**Release 18.03.2021**

`Logon` (`A`): added custom tag `ConnectionOnlyExecutionReports` (`9010`).

**Release 01.03.2021**

`Order Cancel/Replace Request` (`G`): adjusted behavior for MMP orders when the `DeribitMMProtection` (`9008`) flag is not specified.

**Release 11.12.2020**

* `SecurityList` (`y`): added Deribit Volatility Index instruments: BTC-VIX, ETH-VIX.
* `MarketData Request` (`V`): added requests for the Deribit Volatility Index.

**Release 22.06.2020**

* Added `MMProtection Limits` (`MM`).
* Added `MMProtection Limits Result/Reject` (`MR`).
* Added `MMProtection Reset` (`MZ`).
* `New Order Single` (`D`): added nonmandatory `DeribitMMProtection` (`9008`).
* `Order Cancel/Replace Request` (`G`): added nonmandatory `DeribitMMProtection` (`9008`).
* `Execution Reports` (`8`): added nonmandatory `DeribitMMProtection` (`9008`).

**Release 21.05.2020**

* `Logon` (`A`): added custom tag `DeribitSequential` (`9007`).
* `Execution Reports` (`8`): added `SecondaryExecID`, which is the ID of the last change of the order.

**Release 26.03.2020**

* FIX parameter `9003` `DontCancelOnDisconnect` has been added to disable 'Cancel On Disconnect' actions.
* A `Security Status Request` has been added, with a response message of `Security Status`.

**Release 17.01.2020**

Added `SecurityStatusRequest` (`e`) request and `SecurityStatus` (`f`) response.


## Related topics

- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Logon(A) (Production FIX API)](https://docs.deribit.com/fix-api/production/logon.md)
- [Logout(5) (Production FIX API)](https://docs.deribit.com/fix-api/production/logout.md)