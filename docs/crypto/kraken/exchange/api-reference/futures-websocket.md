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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket'
updated_at: 2026-11-13
---

# Derivatives WebSocket

> Real-time market data and account streaming for the Kraken Derivatives WebSocket API

> [!WARNING]
>
> **Derivatives WebSocket is being deprecated.** For new integrations, use the
> [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket), which streams
> Spot and Derivatives over a single connection. Existing integrations continue
> to work until **1 March 2027**, when the Derivatives WebSocket will no
> longer be available. Migrate to the Unified WebSocket before then.
>
> To use private channels or trade on the Unified WebSocket, you need a
> Kraken API key, not a Derivatives API key. Use it to get a token from
> [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token). See
> [Unified WebSocket authentication](https://docs.kraken.com/exchange/api-reference/unified-websocket#authentication).

Real-time market data and streaming account updates for Kraken's
Derivatives market.

> [!NOTE]
>
> Derivatives WebSocket is **streaming-only**. Order entry on Derivatives
> is handled via the [Derivatives REST
> API](https://docs.kraken.com/exchange/guides/futures/rest.md) or the
> [Unified FIX API](https://docs.kraken.com/exchange/api-reference/unified-fix.md). For end-to-end
> guidance, see the
> [Derivatives Introduction](https://docs.kraken.com/exchange/guides/futures/introduction.md).

## Endpoint

```text theme={null}
wss://futures.kraken.com/ws/v1
```

A colocated endpoint is available alongside the Derivatives REST and
Unified FIX surfaces. Connection details are provided during
onboarding.

## Authentication

Private feeds use a signed-challenge model:

1. Connect to the WebSocket endpoint.
2. Request a challenge using your `api_key`.
3. Sign the challenge with your `api_secret` (SHA-256 → HMAC-SHA-512 →
   Base64).
4. Include both `original_challenge` and `signed_challenge` in every
   `subscribe`/`unsubscribe` for private feeds.

The signing flow is documented in full in the [Derivatives WebSocket
guide](https://docs.kraken.com/exchange/guides/futures/websockets.md#sign-challenge).

## Quick start

> [card] [book (L2)](https://docs.kraken.com/exchange/api-reference/futures-websocket/book.md)
>
> Order book snapshots and incremental updates.

> [card] [ticker](https://docs.kraken.com/exchange/api-reference/futures-websocket/ticker.md)
>
> Best-bid / best-offer with funding and mark.

> [card] [open\_orders](https://docs.kraken.com/exchange/api-reference/futures-websocket/open_orders.md)
>
> Private open-order snapshot and updates.

> [card] [fills](https://docs.kraken.com/exchange/api-reference/futures-websocket/fills.md)
>
> Per-fill execution stream.

The complete public catalog (`book`, `ticker`, `ticker_lite`, `trade`,
`heartbeat`) and private catalog (`open_orders`,
`open_orders_verbose`, `open_position`, `balances`, `fills`,
`account_log`, `notifications`, `challenge`) is available in the
**Derivatives WebSocket** dropdown in the left navigation.

## Connection management

Send a ping at least every 60 seconds to keep the connection open. On
reconnect, re-issue subscribe requests for each feed; most feeds send a
fresh snapshot followed by incremental updates.

## Related

> [card] [Derivatives WebSocket guide](https://docs.kraken.com/exchange/guides/futures/websockets.md)
>
> Authentication flow, subscribe/unsubscribe semantics.

> [card] [Derivatives Introduction](https://docs.kraken.com/exchange/guides/futures/introduction.md)
>
> Endpoints, protocols, and surface overview.

> [card] [Derivatives REST](https://docs.kraken.com/exchange/guides/futures/rest.md)
>
> Order entry and account-data endpoints.

> [card] [Unified FIX](https://docs.kraken.com/exchange/api-reference/unified-fix.md)
>
> Lowest-latency order entry across Spot + Derivatives.

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> REST vs WebSocket vs FIX — sequencing and cancel scope.
