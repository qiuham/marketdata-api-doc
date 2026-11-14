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
source_url: 'https://docs.kraken.com/exchange/guides/affiliate/ratelimits'
updated_at: 2026-11-13
---

# Affiliate Rate Limits

> API key request counter and polling cadence for the Affiliate REST API

## API key request counter

Each authenticated Affiliate REST request adds `1` to its Kraken API key request
counter. Each API key has a separate counter. These limits apply to the
Affiliate REST endpoints:

| Account tier | Maximum counter | Counter decay |
| :- | -: | :- |
| Starter | 30 | 2 every 3 seconds |
| Intermediate | 50 | 2 every second |
| Pro | 60 | 16 every second |

Requests that exceed the maximum are rejected until the counter decays. Back
off before retrying a rate-limited request.

## Polling

A trade day's figures can change when activity is reported later. Use `revision`
(day request, first page) to see whether **your** figures changed, then re-check
the trailing 35 days.

Hourly or daily polling is enough for trading figures. Sub-minute polling will
not see new trading figures.
Walk pages with `cursor` rather than retrying the same request.

`revision` tracks trading data only. New enrollments and changes to data-sharing
settings do not advance it. Poll the full roster with `all_users=true` to discover
quiet signups and opt-outs, even when `revision` has not changed.

The roster reflects enrollment and data-sharing settings available when your
request is processed.
