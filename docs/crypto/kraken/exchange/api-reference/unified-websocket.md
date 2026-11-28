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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-websocket'
updated_at: 2026-11-28
---

# Unified WebSocket

> One WebSocket for market data, account updates and order entry across Spot and Derivatives, with lower latency, one API key and official SDKs

> [!WARNING]
>
> **Availability**
>
> * **Spot is a work in progress, planned for Q1 2027.** Until then, the Unified
>   WebSocket supports Derivatives only (`asset_class: derivatives`).

> [!NOTE]
>
> **Using the Derivatives WebSocket today?** It will be decommissioned on
> **1 March 2027**. The Unified WebSocket replaces it and adds order entry. See
> [Migrate from the Derivatives WebSocket](#migrate-from-the-derivatives-websocket).

The Kraken Unified WebSocket API provides real-time market data, account
updates and streaming order entry for both **Spot and Derivatives** markets
through a single WebSocket connection. Supported channels accept `asset_class`
to select Spot or Derivatives instruments. Channel availability depends on the
asset class.

The Unified WebSocket uses the same v2 message format as the Spot
WebSocket v2, with normalised JSON objects, RFC 3339 timestamps, and
sequential trade IDs.

For connection details, ping/pong, and rate-limit behaviour, see the
[WebSocket overview](https://docs.kraken.com/exchange/guides/websockets/introduction.md).

## Why use the Unified WebSocket

> [card] [Trade on the same socket](#trade-on-the-same-socket)
>
> Order entry, market data and account updates share one connection. Add, amend, cancel, batch orders, cancel-all and a dead man's switch.

> [card] [Faster data](#faster-data)
>
> Median publish latency of 9.9µs, 15× faster than the Derivatives WebSocket it replaces.

> [card] [SDKs to speed up onboarding](#sdks-to-speed-up-onboarding)
>
> The Kraken API SDK handles authentication, token refresh, reconnects and order book checksums.

> [card] [One key, one format](#one-key-one-message-format)
>
> Use your Kraken API key and the same v2 message format as the Spot WebSocket v2.

### Trade on the same socket

The Unified WebSocket adds order entry to the same socket as market data and
account updates. You no longer need a separate REST or FIX connection to place
and manage Derivatives orders.

| Operation | Channel |
| :- | :- |
| Place an order | [`add_order`](https://docs.kraken.com/exchange/api-reference/unified-ws/add_order) |
| Amend an order | [`amend_order`](https://docs.kraken.com/exchange/api-reference/unified-ws/amend_order) |
| Cancel an order | [`cancel_order`](https://docs.kraken.com/exchange/api-reference/unified-ws/cancel_order) |
| Place orders in a batch | [`batch_add`](https://docs.kraken.com/exchange/api-reference/unified-ws/batch_add) |
| Cancel orders in a batch | [`batch_cancel`](https://docs.kraken.com/exchange/api-reference/unified-ws/batch_cancel) |
| Cancel all orders | [`cancel_all`](https://docs.kraken.com/exchange/api-reference/unified-ws/cancel_all) |
| Dead man's switch | [`cancel_all_orders_after`](https://docs.kraken.com/exchange/api-reference/unified-ws/cancel_after) |

Options market makers also get the read-only
[`rfqs`](https://docs.kraken.com/exchange/api-reference/unified-ws/rfqs) and
[`quotes`](https://docs.kraken.com/exchange/api-reference/unified-ws/quotes) channels.

### Faster data

Publish latency is the time from the gateway receiving an event to the update
being written to your stream. Compared with the Derivatives WebSocket it
replaces:

| Percentile | Derivatives WebSocket | Unified WebSocket | Improvement |
| :- | -: | -: | :- |
| Median (P50) | 150µs | **9.9µs** | 15× faster |
| P95 | 500µs | **361µs** | 1.4× faster |
| P99 | 2ms | **715µs** | about 3× faster |

> [!NOTE]
>
> These figures are measured at the gateway, so they exclude network transit to
> you. They apply to Futures only.

### SDKs to speed up onboarding

The [Kraken API SDK](https://docs.kraken.com/home/sdks/rust.md) for Rust (v0.2.0) supports Futures on the
Unified WebSocket. It covers market data, private account streams and order
entry. It handles authentication, token refresh, reconnects and order book
checksums, and it rejects orders the venue would refuse before sending them.
A Python SDK is in review.

### One key, one message format

* **One API key.** Private channels and trading use a Kraken API key and a
  WebSocket token from [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token).
  You do not need a Derivatives API key or the signed-challenge flow.
* **One message format.** Requests and responses follow the same v2 format as
  the Spot WebSocket v2, so code you write for one market carries over to the other.
* **Checked books.** [`book`](https://docs.kraken.com/exchange/api-reference/unified-ws/book) updates carry
  CRC32 checksums, so you can detect and recover from a gap.

## Endpoints

| Environment | Public | Private (auth) |
| :- | :- | :- |
| Primary | `wss://uws.kraken.com/v2/public` | `wss://uws.kraken.com/v2/private` |

## Authentication

Public channels need no authentication. Private channels and trading
require a **WebSocket token**, retrieved via the Spot REST endpoint
[`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token)
and sent in `params.token` on each private request. Request the token
with a Kraken API key that has the **Access WebSocket API** permission
(see [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md)). This
applies to Derivatives too: Derivatives API keys and the Derivatives
WebSocket signed challenge are not used. Tokens are short-lived; obtain
a fresh token on each connection.

See [WebSocket
authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for the
full flow.

## Asset class selection

Subscription and order messages that apply to a market include an
`asset_class` field set to either `spot` or `derivatives`. This
determines which market the request applies to, allowing both markets
to be streamed and traded on the same connection.

> [!NOTE]
>
> `asset_class: spot` is planned for Q1 2027. Until then, use `derivatives`.

```json theme={null}
{
  "method": "subscribe",
  "params": {
    "channel": "book",
    "asset_class": "spot",
    "symbol": ["BTC/USD"]
  }
}
```

`book`, `trade`, and `executions` accept `spot` or `derivatives`. Other
market-specific channels currently accept only `derivatives`.

The account-wide
[`balances`](https://docs.kraken.com/exchange/api-reference/unified-ws/balances) and
[`ledgers`](https://docs.kraken.com/exchange/api-reference/unified-ws/ledgers) channels cover
every asset class at once, so they reject `asset_class` rather than
accepting it. The account-wide
[`preferences`](https://docs.kraken.com/exchange/api-reference/unified-ws/preferences) channel does not
require `asset_class`.

## Migrate from the Derivatives WebSocket

The [Derivatives WebSocket](https://docs.kraken.com/exchange/api-reference/futures-websocket.md) is
deprecated. Existing integrations keep working until **1 March 2027**, when it
will no longer be available.

To migrate:

1. **Get a Kraken API key** with the **Access WebSocket API** permission, and
   request a token with [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token).
   The Derivatives signed challenge is not used.
2. **Connect to the Unified WebSocket** at `wss://uws.kraken.com/v2/public` or
   `wss://uws.kraken.com/v2/private`.
3. **Rewrite your messages** to the v2 format. Requests use `method`, `params`
   and `req_id` instead of `event` and `feed`, and market channels take
   `asset_class: derivatives`. Look up valid symbols with the
   [`instrument`](https://docs.kraken.com/exchange/api-reference/unified-ws/instrument) channel.
4. **Move your channels** using the table below.
5. **Move order entry onto the socket** if you place orders over Derivatives
   REST or FIX today.

| Derivatives WebSocket | Unified WebSocket |
| :- | :- |
| `book` | [`book`](https://docs.kraken.com/exchange/api-reference/unified-ws/book) |
| `ticker` | [`ticker`](https://docs.kraken.com/exchange/api-reference/unified-ws/ticker) |
| `trade` | [`trade`](https://docs.kraken.com/exchange/api-reference/unified-ws/trade) |
| `heartbeat` | [`heartbeat`](https://docs.kraken.com/exchange/api-reference/unified-ws/heartbeat) |
| `open_orders`, `fills` | [`executions`](https://docs.kraken.com/exchange/api-reference/unified-ws/executions) |
| `open_position` | [`positions`](https://docs.kraken.com/exchange/api-reference/unified-ws/positions) |
| `balances` | [`balances`](https://docs.kraken.com/exchange/api-reference/unified-ws/balances) |

## Quick start

> [card] [book (L2)](https://docs.kraken.com/exchange/api-reference/unified-ws/book.md)
>
> Order book snapshots + incremental updates with CRC32 checksums.

> [card] [executions](https://docs.kraken.com/exchange/api-reference/unified-ws/executions.md)
>
> Private order acks, fills, and amends — the canonical order-state stream.

> [card] [add\_order](https://docs.kraken.com/exchange/api-reference/unified-ws/add_order.md)
>
> Place a Spot or Derivatives order over the open connection.

> [card] [ticker](https://docs.kraken.com/exchange/api-reference/unified-ws/ticker.md)
>
> Level 1 market data — top of book and recent trade summary.

The complete channel catalog (book, level3, ticker, trade, ohlc,
instrument, rfqs, status, heartbeat, executions, balances, ledgers,
margin, positions, preferences, quotes, add\_order, amend\_order, cancel\_order,
cancel\_all, cancel\_all\_orders\_after, batch\_add, batch\_cancel, set\_preference, ping) is available under the
**Unified WebSocket** dropdown in the left navigation.

## Connection management

Send a `ping` at least every 60 seconds. On reconnect, resubscribe to
each channel and reconcile state — the
[reconnection guide](https://docs.kraken.com/exchange/guides/websockets/reconnection.md) walks
through resubscription, sequence handling, and book recovery.

## Related

> [card] [Kraken API SDK (Rust)](https://docs.kraken.com/home/sdks/rust.md)
>
> Official SDK with Futures support on the Unified WebSocket.

> [card] [WebSocket overview](https://docs.kraken.com/exchange/guides/websockets/introduction.md)
>
> Connection details, ping/pong, beta endpoints.

> [card] [WebSocket authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md)
>
> How to request a WebSocket token with your API key.

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
