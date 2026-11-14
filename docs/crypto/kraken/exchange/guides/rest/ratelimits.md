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
source_url: 'https://docs.kraken.com/exchange/guides/rest/ratelimits'
updated_at: 2026-11-13
---

# Spot REST Rate Limits

> REST API call counter, tier-based limits and decay rates, and matching engine limits that apply across all Spot protocols

## REST Specific Limits

Every REST API user has a "call counter" which starts at `0`. Ledger/trade history calls increase the counter by `2`. All other API calls increase this counter by `1` (except AddOrder, CancelOrder which operate on a different limiter detailed further below).

| Tier | Max API Counter | API Counter Decay |
| - | - | - |
| Starter | 15 | -0.33/sec |
| Intermediate | 20 | -0.5/sec |
| Pro | 20 | -1/sec |

The user's counter is reduced every couple of seconds depending on their verification tier. Each API key's counter is separate, and if the counter exceeds the maximum value, subsequent calls using that API key would be rate limited. If the rate limits are reached, additional calls will be restricted for a few seconds (or possibly longer if calls continue to be made while the rate limits are active).

> [!NOTE]
>
> Master accounts and subaccounts share the same default trading rate limits as determined by the master account's tier.

## Matching engine limits

In addition to the REST-specific limits, the trading engine has its own limits applicable to all protocols. See [Trading engine limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md) and [Derivatives rate limits](https://docs.kraken.com/exchange/guides/futures/ratelimits.md).

## Errors

* "EAPI:Rate limit exceeded" if the REST API counter exceeds the user's maximum.
* "EService: Throttled: \[UNIX timestamp]" if there are too many concurrent requests. Try again after \[timestamp].

Additional information can be found on our [support center](https://support.kraken.com/hc/en-us/articles/206548367-What-are-the-API-rate-limits-).
