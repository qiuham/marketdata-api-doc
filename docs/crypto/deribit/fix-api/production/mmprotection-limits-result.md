---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/mmprotection-limits-result
api_type: FIX
updated_at: 2026-11-25 19:00:46.017817
---

# MMProtection Limits Result (MR) (Production FIX API)

> MMProtectionLimitsResult(MR) is the server response with current MMP settings or a reject on the Deribit production FIX market maker protection endpoint.

**Important: manual admin action is necessary to activate Market Maker
Protection (MMP) for an account.** This message is sent by the server in reply
to [`MMProtection Limits` (`MM`)](https://docs.deribit.com/fix-api/production/mmprotection-limits) or [`MMProtectionReset` (`MZ`)](https://docs.deribit.com/fix-api/production/mmprotection-reset).

### Response

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 20114 | `ProtectionRequestID` | String | Yes | Identifier taken from corresponding [`MM`](https://docs.deribit.com/fix-api/production/mmprotection-limits) or [`MZ`](https://docs.deribit.com/fix-api/production/mmprotection-reset) message |
| 20117 | `ProtectionRequestResult` | Boolean | Yes | `Y` = applied or succeeded, `N` = rejected |
| 58 | `Text` | String | No | Text describes reject reason or equal to `"success"` |


## Related topics

- [MMProtection Limits (MM) (Production FIX API)](https://docs.deribit.com/fix-api/production/mmprotection-limits.md)
- [MMProtection Reset(MZ) (Production FIX API)](https://docs.deribit.com/fix-api/production/mmprotection-reset.md)
- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [FIX API Changelog](https://docs.deribit.com/changelogs/fix.md)
- [Security Status(f) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-status.md)