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
source_url: 'https://docs.kraken.com/exchange/guides/us-perps/connectivity'
updated_at: 2026-11-13
---

# US Perps connectivity

> How to connect to Kraken US Perps — network connectivity and colocation

US Perps clients connect to Kraken's order entry (FIX), market data (SBE) and drop copy (FIX) sessions. All connections require TLS. Connectivity options range from standard network access to colocation, for clients that need the lowest and most predictable latency.

Before connecting, you'll need credentials and session identifiers (such as your SenderCompID) from Kraken; these are provided during onboarding.

## Guides

Each document opens in a new browser tab.

* [Kraken US Perps — Connectivity Guide (PDF)](https://docs.kraken.com/exchange/api-reference/us-perps/doc-connectivity.pdf)

## Colocation

US Perps is reachable over the same colocation cross-connects that already serve Kraken Spot and Futures. If you already have a cross-connect to Kraken, it will work for US Perps — no new physical connectivity is needed.

If you don't have a cross-connect yet, see [Colocation and connectivity](https://docs.kraken.com/exchange/guides/general/colocation.md) for the options and requirements, and contact your Account Manager to begin onboarding. Network design details are shared under NDA.

## Related

> [card] [API](https://docs.kraken.com/exchange/guides/us-perps/api.md)
>
> Order entry over FIX, market data over SBE, and drop copy over FIX.

> [card] [Overview](https://docs.kraken.com/exchange/guides/us-perps/overview.md)
>
> What US Perps covers.
