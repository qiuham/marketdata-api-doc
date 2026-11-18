---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/trade-capture-report-request-ack
api_type: FIX
updated_at: 2026-11-18 18:59:09.987619
---

# TradeCaptureReportRequestAck(AQ) (Production FIX API)

> TradeCaptureReportRequestAck(AQ) acknowledges a TradeCaptureReportRequest on the Deribit production FIX API and indicates whether reports will follow.

The Trade Capture Request Ack message is used to:

* Provide an acknowledgement to a Trade Capture Report Request `AD` in the case
  where the Trade Capture Report Request `AD` is used to specify a subscription.
* The Trade Capture Request was invalid for some business reason, such as the
  request is not authorized, invalid or unknown instrument, party, trading
  session, etc.

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 568 | `TradeRequestID` | String | Yes | Identifier for the trade request |
| 569 | `TradeRequestType` | Int | Yes | Describes request type.Valid value:<ul><li>`0` for all trades</li></ul> |
| 571 | `TradeRequestResult` | Int | Yes | Result of Trade Request.Valid values:<ul><li>`0` - Successful</li><li>`2` - Invalid type of trade requested</li></ul> |
| 750 | `TradeRequestStatus` | Int | Yes | Status of Trade Request.Valid values:<ul><li>`0` - Accepted</li><li>`2` - Rejected</li></ul> |
| 55 | `Symbol` | String | Yes | Common, "human understood" representation of the security, e.g., **BTC-28JUL17**, see instrument naming convention for more details |


## Related topics

- [Starbase FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md)
- [TradeCaptureReportRequest(AD) (Production FIX API)](https://docs.deribit.com/fix-api/production/trade-capture-report-request.md)
- [TradeCaptureReport(AE) (Production FIX API)](https://docs.deribit.com/fix-api/production/trade-capture-report.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [FIX API Changelog](https://docs.deribit.com/changelogs/fix.md)