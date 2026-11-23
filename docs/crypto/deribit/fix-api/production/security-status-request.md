---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/security-status-request
api_type: FIX
updated_at: 2026-11-23 19:00:32.204493
---

# Security Status Request(e) (Production FIX API)

> SecurityStatusRequest(e) subscribes to trading status updates for an instrument on the Deribit production FIX API, covering halts, resumes, and settlement.

This message provides for the ability to request the status of a security.

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 324 | `SecurityStatusReqID` | String | Yes | ID of the request |
| 55 | `Symbol` | String | Yes | Instrument symbol. See instrument naming convention for more details |
| 263 | `SubscriptionRequestType` | char | Yes | `0` = `Snapshot`, `1` = `Snapshot + Updates` (`Subscribe`), `2` = `Unsubscribe` (Please note that our system does not send notifications when currencies are **locked**. Users are advised to subscribe to the [platform\_state](https://docs.deribit.com/index.md#platform_state) channel to monitor the state of currencies actively.) |

### Response

The server will respond with a [`Security Status` (`f`)](https://docs.deribit.com/fix-api/production/security-status)
message.


## Related topics

- [Security Status(f) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-status.md)
- [Security List(y) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-list.md)
- [Security Definition(d) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-definition.md)
- [Order Mass Status Request(AF) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-status-request.md)
- [User Request(BE) (Production FIX API)](https://docs.deribit.com/fix-api/production/user-request.md)