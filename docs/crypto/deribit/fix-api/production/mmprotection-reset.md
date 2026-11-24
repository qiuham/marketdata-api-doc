---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/mmprotection-reset
api_type: FIX
updated_at: 2026-11-24 18:59:45.355533
---

# MMProtection Reset(MZ) (Production FIX API)

> MMProtectionReset(MZ) clears a triggered market maker protection freeze on the Deribit production FIX API so quoting can resume after an MMP event.

**Important: manual admin action is necessary to activate Market Maker
Protection (MMP) for an account.** This message resets Market Maker Protection
(MMP) after triggering.

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 20114 | `ProtectionRequestID` | String | Yes | Unique identifier assigned by the requestor. Will be returned in responses |
| 15 | `Currency` | String | Yes | First currency of the currency pair to reset MMP for. e.g. `BTC`, `ETH` |
| 5544 | `SecondaryCurrency` | String | No | Secondary currency of the currency pair to reset MMP for. e.g. `USD`, `USDC`, defaults to `USD` if not provided |
| 9019 | `MMPGroup` | String | No | A custom tag of MMP Group |

### Response

The server sends the `MMProtection Result (MR)` message as a response.


## Related topics

- [MMProtection Limits Result (MR) (Production FIX API)](https://docs.deribit.com/fix-api/production/mmprotection-limits-result.md)
- [MMProtection Limits (MM) (Production FIX API)](https://docs.deribit.com/fix-api/production/mmprotection-limits.md)
- [Sequence Reset(4) (Production FIX API)](https://docs.deribit.com/fix-api/production/sequence-reset.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [FIX API Changelog](https://docs.deribit.com/changelogs/fix.md)