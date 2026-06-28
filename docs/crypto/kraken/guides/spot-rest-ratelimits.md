---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-rest-ratelimits
api_type: Guide
updated_at: 2026-05-27 19:59:13.561298
---

# Spot REST Rate Limits

## REST Specific Limits

Every REST API user has a "call counter" which starts at `0`. Ledger/trade history calls increase the counter by `4`. All other API calls increase this counter by `1` (except AddOrder, CancelOrder which operate on a different limiter detailed further below).

Tier| Max API Counter| API Counter Decay  
---|---|---  
Intermediate| 20| -0.5/sec  
Pro| 20| -1/sec  
  
The user's counter is reduced every couple of seconds depending on their verification tier. Each API key's counter is separate, and if the counter exceeds the maximum value, subsequent calls using that API key would be rate limited. If the rate limits are reached, additional calls will be restricted for a few seconds (or possibly longer if calls continue to be made while the rate limits are active).

note

Master accounts and subaccounts will share the same default trading rate limits as determined by the master account's tier.

## Matching Engine Limits

In extension to the REST specific limits, the trading engine has additional limits applicable to all user flow. See [Trading Engine Rate Limits](/api/docs/guides/spot-ratelimits)

## Errors

  * "EAPI:Rate limit exceeded" if the REST API counter exceeds the user's maximum.
  * "EService: Throttled: [UNIX timestamp]" if there are too many concurrent requests. Try again after [timestamp].

Additional information can be found on our [support center](https://support.kraken.com/hc/en-us/articles/206548367-What-are-the-API-rate-limits-).

  * REST Specific Limits
  * Matching Engine Limits
  * Errors