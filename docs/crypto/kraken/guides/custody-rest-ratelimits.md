---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/custody-rest-ratelimits
api_type: Guide
updated_at: 2026-05-27 19:56:33.925426
---

# Custody Rate Limits

## Specific Limits

Every Custody API user is assigned a "call counter" that begins at 0 and increases by 1 for each call.

The maximum API counter for each user is set at 10. This counter resets after a rolling 10 seconds. Each new request extends the expiration time of the limiter.

When rate limits are reached, additional calls will be restricted for a few seconds, or potentially longer if new calls are initiated while the rate limits remain in effect.

## Errors

  * "EAPI:Rate limit exceeded" indicates that the REST API counter has surpassed the user's maximum limit.
  * "EService: Throttled: [UNIX timestamp]" signifies that there are too many concurrent requests. Please try again after [timestamp].
* Specific Limits
  * Errors