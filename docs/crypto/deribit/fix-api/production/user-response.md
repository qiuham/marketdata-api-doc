---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/user-response
api_type: FIX
updated_at: 2026-11-22 18:59:24.111934
---

# User Response(BF) (Production FIX API)

> UserResponse(BF) is the server response to a UserRequest on the Deribit production FIX API, reporting the current user status after processing.

This message is used to respond to a [`USER REQUEST`(`BE`)](https://docs.deribit.com/fix-api/production/user-request)
message, it reports the status of the user and user's account info.

### Response

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 923 | `UserRequestID` | String | Yes | The request ID |
| 553 | `Username` | String | Yes | User's API 'Client ID' |
| 926 | `UserStatus` | int | No | `1` = logged in, current implementation accepts USER REQUEST-s only from logged in users |
| 15 | `Currency` | String | No | Currency of the report. See [`Security List Request`(`x`)](https://docs.deribit.com/fix-api/production/security-list-request). Default is BTC. If `CROSS` is given as currency and user has cross collateral enabled, only the following fields are returned:<ul><li>100001 `DeribitUserEquity`</li><li>100003 `DeribitUserInitialMargin`</li><li>100004 `DeribitUserMaintenanceMargin`</li><li>100013 `DeribitMarginBalance`</li></ul> |
| 100001 | `DeribitUserEquity` | float | No | Equity of the user |
| 100002 | `DeribitUserBalance` | float | No | Balance of the user |
| 100003 | `DeribitUserInitialMargin` | float | No | Initial margin of the user |
| 100004 | `DeribitUserMaintenanceMargin` | float | No | Maintenance margin of the user |
| 100005 | `DeribitUnrealizedPl` | float | No | Unrealized P/L of the user |
| 100006 | `DeribitRealizedPl` | float | No | Realized P/L of the user |
| 100011 | `DeribitTotalPl` | float | No | Total P/L of the user |
| 100013 | `DeribitMarginBalance` | float | No | Margin Balance |


## Related topics

- [User Request(BE) (Production FIX API)](https://docs.deribit.com/fix-api/production/user-request.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [Order Cancel Reject(9) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-reject.md)
- [Logon(A) (Production FIX API)](https://docs.deribit.com/fix-api/production/logon.md)
- [Heartbeat(0) (Production FIX API)](https://docs.deribit.com/fix-api/production/heartbeat.md)