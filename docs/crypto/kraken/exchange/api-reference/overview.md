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
source_url: 'https://docs.kraken.com/exchange/api-reference/overview'
updated_at: 2026-11-13
---

# Exchange API reference

> Choose a protocol — REST, WebSocket, or FIX — for Spot, Derivatives, or Affiliate

Kraken's Exchange APIs span two trading engines (Spot and Derivatives) and three protocols (REST, WebSocket, FIX), plus a separate Affiliate REST surface for approved partners. Pick the surface that matches your workflow.

> [!NOTE]
>
> New here? Start with [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md) for a side-by-side feature and latency comparison.

## Spot

Order management, account data, market data, funding, and Earn on Kraken's Spot trading engine.

> [card] [Spot REST](https://docs.kraken.com/api-reference/market-data/get-server-time.md)
>
> Account, trading, algo trading, funding, and Earn. Public and private endpoints over HTTPS.

> [card] [Spot WebSocket](https://docs.kraken.com/exchange/api-reference/spot-websocket.md)
>
> Real-time market data and order entry. v2 recommended; v1 maintained.

> [card] [Spot FIX](https://docs.kraken.com/exchange/api-reference/unified-fix.md)
>
> Lowest-latency order entry via Unified FIX 4.4.

## Derivatives

Perpetuals and dated contracts on BTC, ETH, and more.

> [card] [Derivatives REST](https://docs.kraken.com/api-reference/market-data/get-tickers.md)
>
> Order entry, account, positions, fills, and historical data.

> [card] [Derivatives WebSocket](https://docs.kraken.com/exchange/api-reference/futures-websocket.md)
>
> Streaming-only market data and account updates.

> [card] [Derivatives FIX](https://docs.kraken.com/exchange/api-reference/unified-fix.md)
>
> Order entry via Unified FIX 4.4 — same session as Spot FIX.

## Affiliate

Referred-user activity for approved affiliates. Use the same host and HMAC-SHA512 API keys as Exchange REST.

> [card] [Introduction](https://docs.kraken.com/exchange/guides/affiliate/introduction.md)
>
> Who it is for, prerequisites, and conventions.

> [card] [REST](https://docs.kraken.com/exchange/guides/affiliate/rest.md)
>
> Signing, day vs history, product keys, pagination.

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/affiliate/ratelimits.md)
>
> Call counter and polling cadence.

## Not sure where to start?

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> Side-by-side feature, latency, and sequencing comparison.

> [card] [Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md)
>
> HMAC-SHA512 signing for REST and WebSocket private endpoints.

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> Limits across REST, WebSocket, and FIX.

> [card] [Errors](https://docs.kraken.com/exchange/guides/general/errors.md)
>
> Common errors and how to resolve them.
