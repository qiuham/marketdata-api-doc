---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/guides/general/errors'
updated_at: 2026-11-13
---

# Error messages

> All error codes returned by the Kraken Spot REST API, organized by category, with causes and handling guidance

Kraken API errors follow a consistent format: a string beginning with a capital-E category prefix, followed by a colon-separated description. Every response includes an `error` array — if non-empty, the request failed.

```json theme={null}
{
  "error": ["EAPI:Invalid key"],
  "result": {}
}
```

## Authentication errors

> [accordion] EAPI:Invalid key
>
> **Cause:** The `API-Key` header is missing, malformed, or refers to a key that has been deleted or revoked.
>
> **Fix:** Verify the key exists in your Kraken account under Settings → API. Regenerate if needed and update your client. Repeatedly sending a key that doesn't exist triggers `EGeneral:Temporary lockout` for every API key used from your IP address.

> [accordion] EAPI:Invalid signature
>
> **Cause:** The `API-Sign` header does not match the expected HMAC-SHA512 signature.
>
> **Common causes:**
>
> * Wrong API secret (base64-decoded correctly?)
> * Nonce or POST body included in the wrong order
> * Extra whitespace or encoding issue in the payload
>
> **Fix:** Review the [authentication guide](https://docs.kraken.com/exchange/guides/rest/authentication.md) and reproduce the signature step-by-step. Use the API test endpoint `/0/private/Balance` with a minimal payload to isolate the issue.

> [accordion] EAPI:Invalid nonce
>
> **Cause:** The nonce submitted is less than or equal to the last accepted nonce for this API key.
>
> **Fix:** Use a monotonically increasing nonce. The most reliable source is the current Unix timestamp in milliseconds. If multiple threads share the same API key, use a counter with a mutex, not the system clock.

> [accordion] EGeneral:Temporary lockout
>
> **Cause:** Too many requests from your IP address used an API key that doesn't exist, for example one that was deleted or has expired. To prevent brute-force attempts, API key requests from that IP address are temporarily blocked. The lockout applies to every API key sent from that IP address, including valid ones.
>
> **Fix:**
>
> 1. Find the client sending the invalid key. Look for `EAPI:Invalid key` responses just before the lockout started, then remove or replace that key.
> 2. Stop retrying requests that fail with `EAPI:Invalid key`. Retrying won't succeed.
> 3. Wait about 20 minutes without sending the invalid key. The lockout then clears by itself. Requests made during the lockout don't extend it, but sending the invalid key again after it clears starts a new one.

> [accordion] EGeneral:Permission denied
>
> **Cause:** The API key exists and authenticated correctly, but does not have the permission required for this endpoint.
>
> **Fix:** Check which permissions the key has under Settings → API. Add the required permission or use a different key that has it.

> [accordion] EAuth:Account temporary disabled
>
> **Cause:** The account has been temporarily suspended, usually due to security concerns or compliance review.
>
> **Fix:** Contact Kraken support.

> [accordion] EAuth:Account unconfirmed
>
> **Cause:** The account email has not been verified.
>
> **Fix:** Complete email verification before making authenticated requests.

> [accordion] EAuth:Rate limit exceeded / EAuth:Too many requests
>
> **Cause:** Too many authentication attempts in a short period.
>
> **Fix:** Back off and retry. Do not hammer the auth endpoints.

## Order errors

> [accordion] EOrder:Insufficient funds
>
> **Cause:** The account does not have enough available balance to place this order (for the quote currency on buys, base currency on sells).
>
> **Fix:** Check your balance via `/0/private/Balance` or `BalanceEx`. Account for any fees that will be deducted.

> [accordion] EOrder:Order minimum not met
>
> **Cause:** The order volume is below the `ordermin` for this pair.
>
> **Fix:** Query `/0/public/AssetPairs` and check the `ordermin` field. Increase the order size.

> [accordion] EOrder:Cost minimum not met
>
> **Cause:** The total cost (price × volume) is below the `costmin` for this pair.
>
> **Fix:** Check `costmin` in `/0/public/AssetPairs`. Increase price or volume so their product exceeds the minimum.

> [accordion] EOrder:Tick size check failed
>
> **Cause:** The price submitted is not a valid multiple of the pair's `tick_size`.
>
> **Fix:** Round your price to the nearest valid tick. `tick_size` is returned by `/0/public/AssetPairs`.

> [accordion] EOrder:Invalid price
>
> **Cause:** The submitted price is zero, negative, or otherwise invalid.
>
> **Fix:** Validate price inputs before sending. Market orders should not include a price parameter.

> [accordion] EOrder:Rate limit exceeded
>
> **Cause:** The account's order rate limit counter has reached its threshold.
>
> **Fix:** See the [rate limits guide](https://docs.kraken.com/exchange/guides/rest/ratelimits.md). Slow down order placement and cancellation. Consider using `amend` instead of cancel + replace.

> [accordion] EOrder:Orders limit exceeded
>
> **Cause:** The account has too many open orders.
>
> **Fix:** Cancel some open orders before placing new ones. See [rate limits](https://docs.kraken.com/exchange/guides/rest/ratelimits.md) for the open order cap by tier.

> [accordion] EOrder:Domain rate limit exceeded
>
> **Cause:** The domain rate limit (master + all sub-accounts) has been reached.
>
> **Fix:** Rate limit is shared across all sub-accounts. Reduce order activity across the whole account group. See [sub-accounts](https://docs.kraken.com/exchange/guides/general/subaccounts.md).

> [accordion] EOrder:Scheduled orders limit exceeded
>
> **Cause:** Too many scheduled (trigger) orders are open simultaneously.
>
> **Fix:** Cancel some scheduled orders before adding more.

> [accordion] EOrder:Positions limit exceeded
>
> **Cause:** The account has reached the maximum number of open margin positions.
>
> **Fix:** Close existing positions before opening new ones.

> [accordion] EOrder:Reduce only — variants
>
> | Error | Cause |
> | :- | :- |
> | `EOrder:Reduce only:Non-PC` | Reduce-only flag submitted on a non-perpetual-contract pair |
> | `EOrder:Reduce only:No position exists` | Reduce-only order submitted but no open position exists for this market |
> | `EOrder:Reduce only:Position is closed` | Order would flip the position — it partially fills and the remainder is canceled |
>
> **Fix:** Only use `reduce_only` when you have an open position in the matching direction.

> [accordion] EOrder:Unknown position
>
> **Cause:** The referenced position ID does not exist or belongs to a different account.
>
> **Fix:** Verify the position ID via `/0/private/OpenPositions`.

## Margin errors

> [accordion] EOrder:Cannot open position / EOrder:Cannot open opposing position
>
> **Cause:** The account tier or account type is not eligible for margin trading.
>
> **Fix:** Upgrade your account tier or complete margin trading verification. Check eligibility in your account settings.

> [accordion] EOrder:Margin allowance exceeded
>
> **Cause:** The order would exceed the account's total margin allowance.
>
> **Fix:** Reduce position size or close existing positions.

> [accordion] EOrder:Margin level too low
>
> **Cause:** The account has insufficient equity or collateral to support this position.
>
> **Fix:** Add funds or reduce open position size to restore margin level.

> [accordion] EOrder:Margin position size exceeded
>
> **Cause:** The order would cause the account to exceed the maximum allowed position size for this pair.
>
> **Fix:** Check the pair's position size limit. Reduce order size.

> [accordion] EOrder:Insufficient margin
>
> **Cause:** Kraken's exchange-side margin pool does not have sufficient funds for this trade. This is a platform-level constraint, not an account issue.
>
> **Fix:** Retry later. If this persists, contact support.

## Service errors

> [accordion] EService:Unavailable
>
> **Cause:** The matching engine or API is offline, typically during a maintenance window.
>
> **Fix:** Check the [system status](https://status.kraken.com) page. Implement backoff and retry logic. Subscribe to the `status` WebSocket channel for advance notice.

> [accordion] EService:Market in cancel\_only mode
>
> **Cause:** The market is in `cancel_only` mode — no new orders can be placed, only cancellations.
>
> **Fix:** Wait for the market to return to normal. Check `SystemStatus` endpoint or the `status` WebSocket channel.

> [accordion] EService:Market in post\_only mode
>
> **Cause:** The market is in `post_only` mode — only maker orders are accepted.
>
> **Fix:** Submit limit orders with `post_only=true`, or wait for normal mode to resume.

> [accordion] EService:Deadline elapsed
>
> **Cause:** The request timed out before the trading engine processed it. Can occur if the `deadline` parameter was set too short, or under high load.
>
> **Fix:** Increase your deadline or remove it. Before retrying, check `OpenOrders` — the order may have been placed despite the timeout.

## General errors

> [accordion] EGeneral:Invalid arguments
>
> **Cause:** The request payload is malformed, missing required parameters, or contains invalid values.
>
> **Fix:** Validate all parameters against the endpoint documentation before sending. Check for incorrect types (string vs number), missing required fields, or unknown parameters.

> [accordion] EGeneral:Invalid arguments:Index unavailable
>
> **Cause:** Index pricing is unavailable for stop or profit orders on this pair.
>
> **Fix:** Use a limit price instead of an index-based trigger for this pair.

> [accordion] EGeneral:Internal error
>
> **Cause:** An unexpected error occurred on Kraken's side. The error may include a numeric code (e.g. `EGeneral:Internal error:5`).
>
> **Fix:** Retry with exponential backoff. If the error persists, contact Kraken support with the full request details and timestamp.

> [accordion] ETrade:Invalid request
>
> **Cause:** The trade request is structurally invalid.
>
> **Fix:** Review the endpoint documentation. Ensure all required fields are present and correctly typed.

> [accordion] EAccount:Invalid permissions
>
> **Cause:** The account does not have the permissions required to perform this action.
>
> **Fix:** Contact Kraken support or check account tier requirements.

## Funding errors

| Error | Cause |
| :- | :- |
| `EFunding:Max fee exceeded` | Withdrawal fee exceeds the `max_fee` set in the `Withdraw` request — increase `max_fee` or remove it |
| `EBM:limit exceeded:CAL` | Exceeded Canadian Acquisition Limits for this cryptocurrency |

## Related guides

> [card] [Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md)
>
> Signature generation, nonce management, and EAPI error fixes

> [card] [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md)
>
> Which permissions to grant to avoid EGeneral:Permission denied

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> How rate limit counters work and how to avoid EOrder:Rate limit exceeded

## Error handling patterns

| Scenario | Recommended approach |
| :- | :- |
| `EAPI:Invalid key` or `EAPI:Invalid signature` | Do not retry — fix the authentication logic first |
| `EAPI:Invalid nonce` | Do not retry the same nonce — generate a fresh one |
| `EService:Unavailable` | Retry with exponential backoff (start at 1s, cap at 60s) |
| `EService:Deadline elapsed` | Check `OpenOrders` before retrying — the order may have placed |
| `EOrder:Rate limit exceeded` | Back off and reduce order frequency; check counter via `TradeBalance` |
| `EGeneral:Internal error` | Retry with backoff; escalate to support if persistent |
| Any `EOrder:Insufficient*` | Check balances before retrying; do not retry immediately |
