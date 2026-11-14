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
source_url: 'https://docs.kraken.com/exchange/guides/affiliate/introduction'
updated_at: 2026-11-13
---

# Affiliate Introduction

> Overview of the Affiliate REST API — referred-user activity, CPA progress, and payouts for approved partners

The Affiliate API is for approved affiliates. It does not accept trades or
offer a WebSocket or FIX feed; all requests use REST on
`https://api.kraken.com`.

The API uses the account that owns your key to determine which referrals you can see.

> [card] [Affiliate REST OpenAPI](https://docs.kraken.com/openapi/affiliate-rest.yaml)
>
> Download the Affiliate REST OpenAPI spec (YAML)

## What you can do

| Workflow | Endpoint |
| - | - |
| Full referral roster, including quiet users | `GET /affiliate/v1/daily-activity?activity_date=&all_users=true` |
| Activity for one UTC trade day | `GET /affiliate/v1/daily-activity?activity_date=` |
| Activity for up to ten known participants over a date range | `GET /affiliate/v1/daily-activity?iiban=&start_date=&end_date=` |
| CPA qualification progress for one referred trader | `GET /affiliate/v1/cpa-progress?iiban=` |
| Affiliate payout history, including sub-affiliate commissions, retainers, and remediations | `GET /affiliate/v1/payout-history` |

Each daily activity item is one referred user, split by plan and then by product
(volume, fees, commission). In full-roster and person-history requests, opted-out
users remain visible as existence stubs with a stable
reference, enrollment time, and referral code, but no account identifier or
individual trading data.
Users sharing activity also include their full Kraken account identifier in `iiban`.
Schemas are in [Get Daily Activity](https://docs.kraken.com/api-reference/affiliate/get-daily-activity.md),
[Get CPA Progress](https://docs.kraken.com/api-reference/affiliate/get-cpa-progress.md), and
[Get Payout History](https://docs.kraken.com/api-reference/affiliate/get-payout-history.md).

A referred user who shares activity does not need to trade to appear in the results. On their
enrollment day, they have an entry with `enrolled_at` and empty `products`,
confirming that they are enrolled. Empty `products` may be omitted. Use `all_users=true` to include quiet users
on later requested days while they remain enrolled.

See the [request and response examples](https://docs.kraken.com/exchange/guides/affiliate/rest.md#full-referral-roster)
for trading users, users who have not traded, and users who opted out.

## Prerequisites

* An approved affiliate account with your own active affiliate plan
* An API key with **Query affiliate participants** enabled
* Your API secret for request signing

> [!NOTE]
>
> Sub-affiliates can use these endpoints with their own API key and active affiliate
> plan. Without an active affiliate plan, the API returns `403`.

## API key permission

When creating or editing your API key, select the **Query affiliate participants**
checkbox and save the key. This is the permission required for the Affiliate API.
See [API key setup](https://docs.kraken.com/exchange/guides/rest/api-keys.md) for the general setup steps.

## Conventions

* **UTC calendar days** (`YYYY-MM-DD`) for daily activity. Today or one of the previous 89 UTC days.
* **Daily activity reporting currency** is `USD` today — not the payout asset.
  CPA rewards and payout rows identify their asset in `reward_asset` or `asset`.
* **Authentication** is the same HMAC-SHA512 key as other private Exchange REST
  calls. The signed path includes the query string.

## Getting started

> [card] [REST](https://docs.kraken.com/exchange/guides/affiliate/rest.md)
>
> Signing, activity, CPA progress, payouts, and pagination

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/affiliate/ratelimits.md)
>
> Call counter, polling cadence, and throttle errors

> [card] [Get Daily Activity](https://docs.kraken.com/api-reference/affiliate/get-daily-activity.md)
>
> Request and response schemas

> [card] [Get CPA Progress](https://docs.kraken.com/api-reference/affiliate/get-cpa-progress.md)
>
> Qualification status, requirements, and exact progress

> [card] [Get Payout History](https://docs.kraken.com/api-reference/affiliate/get-payout-history.md)
>
> Payout rows and whole-history totals
