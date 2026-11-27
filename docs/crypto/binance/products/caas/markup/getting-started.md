---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/markup/getting-started
api_type: Guide
updated_at: 2026-11-27 18:41:16.673029
---

# Getting Started

Complete [CAAS Getting Started](/products/caas/getting-started) first — Markup is enabled on top of
an existing CAAS integration and uses the same master account.

## Endpoints, signing and rate limits

The Markup endpoints are `/sapi/v1/vip/caas/commission/*` on **https://api.binance.com**, so they
follow the main-API rules in [API basics](/products/caas/basics/1.base-urls) — base endpoints,
request signing, error payloads, and the `/sapi/*` rate limits.

Two points specific to Markup:

- Every Markup endpoint is security type **`TRADE`**, so all of them are `SIGNED` and require a
  valid API key plus `signature` and `timestamp`. There are no public Markup endpoints.
- The API key must belong to your **master account**, not to a sub-account.

Because these are `/sapi/*` endpoints, each carries its own independent rate limit rather than
sharing a pool, and exceeding it returns `429` — the `418` IP-ban escalation does not apply. See
[`/api/*` and `/sapi/*` differ](/products/caas/basics/4.rate-limits#api-and-sapi-differ--check-which-family-you-are-calling).

---

# Getting Started

Complete [CAAS Getting Started](/products/caas/getting-started) first — Markup is enabled on top of
an existing CAAS integration and uses the same master account.

## Endpoints, signing and rate limits

The Markup endpoints are `/sapi/v1/vip/caas/commission/*` on **https://api.binance.com**, so they
follow the main-API rules in [API basics](/products/caas/basics/1.base-urls) — base endpoints,
request signing, error payloads, and the `/sapi/*` rate limits.

Two points specific to Markup:

- Every Markup endpoint is security type **`TRADE`**, so all of them are `SIGNED` and require a
  valid API key plus `signature` and `timestamp`. There are no public Markup endpoints.
- The API key must belong to your **master account**, not to a sub-account.

Because these are `/sapi/*` endpoints, each carries its own independent rate limit rather than
sharing a pool, and exceeding it returns `429` — the `418` IP-ban escalation does not apply. See
[`/api/*` and `/sapi/*` differ](/products/caas/basics/4.rate-limits#api-and-sapi-differ--check-which-family-you-are-calling).