---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/test-request
api_type: FIX
updated_at: 2026-11-19 19:05:44.709614
---

# Test Request(1) (Production FIX API)

> TestRequest(1) solicits a Heartbeat response from the counterparty to verify the Deribit production FIX session is responsive during idle connection periods.

The `Test Request`(`1`) message forces a heartbeat from the opposing
application. The opposing application responds with a
[`Heartbeat`(`0`)](https://docs.deribit.com/fix-api/production/heartbeat) containing the `TestReqID`(`112`).

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 112 | `TestReqId` | String | Yes | Mirrors the original request ID |


## Related topics

- [Heartbeat(0) (Production FIX API)](https://docs.deribit.com/fix-api/production/heartbeat.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [Request For Positions(AN) (Production FIX API)](https://docs.deribit.com/fix-api/production/request-for-positions.md)
- [User Request(BE) (Production FIX API)](https://docs.deribit.com/fix-api/production/user-request.md)
- [Resend Request(2) (Production FIX API)](https://docs.deribit.com/fix-api/production/resend-request.md)