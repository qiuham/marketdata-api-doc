---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/trade-capture-report-request
api_type: FIX
updated_at: 2026-11-26 19:02:03.204836
---

# TradeCaptureReportRequest(AD) (Production FIX API)

> TradeCaptureReportRequest(AD) requests historical or streaming trade capture reports on the Deribit production FIX API, filterable by trade criteria.

Request one or more trade capture reports based upon selection criteria provided
on the trade capture report request.

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 568 | `TradeRequestID` | String | Yes | Identifier for the trade request |
| 569 | `TradeRequestType` | Int | Yes | Describes request type.Valid value:<ul><li>`0` for all trades</li></ul> |
| 55 | `Symbol` | String | Yes | Common, "human understood" representation of the security, e.g., **BTC-28JUL17**, see instrument naming convention for more details |
| 263 | `SubscriptionRequestType` | char | No | Used to subscribe / unsubscribe for trade capture reports. If the field is absent, the value 1 will be the default (subscription). Valid values:<ul><li>1 = Subscribe</li><li> 2 = Unsubscribe</li></ul> (Note: 0 = Snapshot is not implemented for now)  |


## Related topics

- [TradeCaptureReportRequestAck(AQ) (Production FIX API)](https://docs.deribit.com/fix-api/production/trade-capture-report-request-ack.md)
- [TradeCaptureReport(AE) (Production FIX API)](https://docs.deribit.com/fix-api/production/trade-capture-report.md)
- [Starbase FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [FIX API Changelog](https://docs.deribit.com/changelogs/fix.md)