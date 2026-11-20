---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/user-request
api_type: FIX
updated_at: 2026-11-20 19:00:11.333300
---

# User Request(BE) (Production FIX API)

> UserRequest(BE) requests user status changes such as logging users in or out of the Deribit production FIX API session for account-level control.

This message is used to request a report on a user's status and user account
info.

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 923 | `UserRequestID` | String | Yes | The request ID |
| 924 | `UserRequestType` | int | Yes | Should be equal to `4` (Request individual user status), only `UserRequestType`=`4` supported for now |
| 553 | `Username` | String | Yes | API authenticated 'Client ID', user can request only own info, should be the same as for `LOGON`(`A`) |
| 15 | `Currency` | String | No | Currency of the report. See [`Security List Request`(`x`)](https://docs.deribit.com/fix-api/production/security-list-request). Default is BTC. If `CROSS` is given as currency and user has cross collateral enabled, only the following fields are returned:<ul><li>100001 `DeribitUserEquity`</li><li>100003 `DeribitUserInitialMargin`</li><li>100004 `DeribitUserMaintenanceMargin`</li><li>100013 `DeribitMarginBalance`</li></ul> |

### Response

The server will respond with a `User Response`(`BF`) message.


## Related topics

- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [User Response(BF) (Production FIX API)](https://docs.deribit.com/fix-api/production/user-response.md)
- [Order Cancel Request(F) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-cancel-request.md)
- [Security Status Request(e) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-status-request.md)
- [Security List Request(x) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-list-request.md)