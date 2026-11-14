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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket'
updated_at: 2026-11-13
---

# Spot WebSocket

> Reference for the Spot WebSocket API — v2 (recommended) and v1 (maintained)

Real-time market data and streaming order entry over a persistent
connection. **v2 is recommended for all new integrations**; v1 is
maintained for existing clients.

For connection details, version differences, ping/pong, and rate-limit
behaviour, see the [Spot WebSocket
overview](https://docs.kraken.com/exchange/guides/websockets/introduction.md).

## Endpoints

| Environment | Public | Private (auth) |
| :- | :- | :- |
| v2 — Primary | `wss://ws.kraken.com/v2` | `wss://ws-auth.kraken.com/v2` |
| v2 — Beta | `wss://beta-ws.kraken.com/v2` | `wss://beta-ws-auth.kraken.com/v2` |
| v1 — Primary | `wss://ws.kraken.com` | `wss://ws-auth.kraken.com` |
| v1 — Beta | `wss://beta-ws.kraken.com` | `wss://beta-ws-auth.kraken.com` |

Beta endpoints share the production trading engine but receive new
features ahead of primary — used for client validation when announced.

## Authentication

Private channels require a **WebSocket token**, retrieved via the Spot
REST endpoint
[`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token).
Tokens are short-lived; obtain a fresh token on each connection.

See [WebSocket
authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for the
full flow.

## v2 vs v1

| Feature | v1 | v2 |
| :- | :- | :- |
| Message format | Array | Normalised JSON object |
| Symbol format | `XBT/USD` | `BTC/USD` |
| Timestamp | Epoch sec, μs | RFC 3339 (`2026-04-28T...`) |
| L3 order-by-order book | — | ✅ |
| Book checksum | Updates only | Snapshot + updates |
| Trade ID | — | Sequential int |
| New features | Frozen | Active |

## Quick start

> [card] [book (L2)](https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/book.md)
>
> Order book snapshots + incremental updates with CRC32 checksums.

> [card] [executions](https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/executions.md)
>
> Private order acks, fills, and amends — the canonical order-state stream.

> [card] [add\_order](https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/add_order.md)
>
> Place an order over the open WebSocket connection.

> [card] [cancel\_after](https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/cancel_after.md)
>
> Dead-man's switch — cancel all orders if the client stops checking in.

The complete v2 catalog (book, level3, ticker, trade, ohlc, instrument,
executions, balances, add\_order, amend\_order, cancel\_order, batch\_add,
batch\_cancel, cancel\_all, cancel\_after, ping, heartbeat, status) and
the v1 catalog (book, ticker, trade, spread, ohlc, ownTrades,
openOrders, addOrder, cancelOrder, cancelAll, systemStatus, heartbeat,
ping) are available under the **Spot WebSocket v2** and **Spot
WebSocket v1** dropdowns in the left navigation.

## Connection management

Send a `ping` at least every 60 seconds. On reconnect, resubscribe to
each channel and reconcile state — the
[reconnection guide](https://docs.kraken.com/exchange/guides/websockets/reconnection.md) walks
through resubscription, sequence handling, and book recovery.

## Related

> [card] [WebSocket overview](https://docs.kraken.com/exchange/guides/websockets/introduction.md)
>
> Connection details, v1 vs v2, beta endpoints.

> [card] [WebSocket authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md)
>
> Token retrieval and signed challenge flow.

> [card] [Book checksum (v2)](https://docs.kraken.com/exchange/guides/websockets/book-checksum-v2.md)
>
> Validate book consistency after every update.

> [card] [L3 checksum (v2)](https://docs.kraken.com/exchange/guides/websockets/l3-checksum-v2.md)
>
> L3 order-by-order checksum logic.

> [card] [Reconnection](https://docs.kraken.com/exchange/guides/websockets/reconnection.md)
>
> Disconnect handling and resubscribe.

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> WebSocket vs FIX vs REST trade-offs.
