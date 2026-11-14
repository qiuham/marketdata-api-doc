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
source_url: 'https://docs.kraken.com/exchange/guides/general/api-comparison'
updated_at: 2026-11-13
---

# Choose your protocol

> REST, WebSocket, and FIX — differences, trade-offs, and when to use each

Kraken's Spot and Derivatives markets run on **separate trading engines**, each with its own endpoints and latency characteristics. The right protocol combination depends on which market you trade.

> [tab] Spot
>
> Spot offers three protocols. They share the same rate limit counter — choose based on your latency requirements and feature needs.
>
> | | REST | WebSocket | Unified FIX |
> | :- | :-: | :-: | :-: |
> | Connection model | Request/response | Persistent | Persistent session |
> | Latency profile | Higher, variable | Low | Lowest (colocation) |
> | Market data | ✅ | ✅ | ✅ |
> | Order entry | ✅ | ✅ | ✅ |
> | Account data | ✅ | ✅ | — |
> | L3 order book | ✅ | ✅ (v2 only) | ✅ |
> | Order amend | ✅ | ✅ | ✅ (MsgType=G) |
> | Cancel on disconnect | — | — | ✅ |
> | FIX message replay | — | — | ✅ |
> | Funding / Earn | ✅ | — | — |
> | Subaccount management | ✅ | — | — |
> | FIX broker allocation | — | — | ✅ (Tags 78/79) |
> | Authentication | HMAC-SHA512 | Token (via REST) | Spot FIX API Key |
> | Colocation | — | ✅ | ✅ |
>
> > [accordion] REST
> >
> > Best for: operational tasks that don't require real-time streaming — checking balances, querying order history, managing deposits and withdrawals, Earn, sub-account transfers.
> >
> > Not recommended for: latency-sensitive order entry or real-time market data. Each request incurs a full HTTP round-trip.
> >
> > Base URL: `https://api.kraken.com`
>
> > [accordion] WebSocket (v2 recommended)
> >
> > Best for: most systematic trading use cases. Real-time order updates, market data streaming, L3 book, and order entry in a single persistent connection. The recommended choice for new integrations.
> >
> > Limitations: no Funding or Earn endpoints (use REST for those), no cancel-on-disconnect.
> >
> > Endpoint: `wss://ws.kraken.com/v2`
>
> > [accordion] Unified FIX 4.4
> >
> > Best for: institutional and HFT clients requiring the lowest latency, deterministic message sequencing, cancel-on-disconnect, and session-based message replay. Available for colocated deployments alongside WebSocket.
> >
> > Uses a **Spot FIX API Key** pre-configured with the correct permissions. Covers both Spot and Derivatives in a single session.
> >
> > Limitations: requires NDA and VIP status for production colocation. Cannot cancel orders from a different FIX session. No account data endpoints.

> [tab] Derivatives
>
> Derivatives has its own trading engine with a separate REST API and WebSocket feed. For lowest-latency order management, use the Unified FIX API.
>
> | | REST | WebSocket | Unified FIX |
> | :- | :-: | :-: | :-: |
> | Connection model | Request/response | Persistent (streaming) | Persistent session |
> | Latency profile | Higher, variable | Low | Lowest (colocation) |
> | Market data | ✅ | ✅ | ✅ |
> | Order entry | ✅ | — | ✅ |
> | Account data | ✅ | ✅ | — |
> | L3 order book | — | — | ✅ |
> | Order amend | ✅ | — | ✅ (MsgType=G) |
> | Cancel on disconnect | — | — | ✅ |
> | FIX message replay | — | — | ✅ |
> | Authentication | HMAC-SHA512 | API Key | Spot FIX API Key |
> | Colocation | ✅ | ✅ | ✅ |
>
> > [!NOTE]
> >
> > Derivatives WebSocket is for **streaming market data and account updates only**. Order entry is handled via REST or Unified FIX. Both REST and WebSocket are available for colocated Derivatives deployments.
>
> > [accordion] Derivatives REST
> >
> > Best for: order management, position queries, account data, funding, and any operation requiring a confirmed response. Available in colocation.
> >
> > Base URL: `https://futures.kraken.com/derivatives/api/v3`
>
> > [accordion] Derivatives WebSocket (streaming only)
> >
> > Best for: real-time market data feeds, account balance updates, and position streaming. Not used for order entry — pair with REST or Unified FIX for order management.
> >
> > Endpoint: `wss://futures.kraken.com/ws/v1`
> >
> > Available in colocation alongside REST.
>
> > [accordion] Unified FIX 4.4
> >
> > Best for: lowest-latency order management on Derivatives. Covers both Spot and Derivatives via a single **Spot FIX API Key** — no separate Derivatives FIX credentials required.
> >
> > Provides deterministic message sequencing, cancel-on-disconnect, and session-based message replay. Available in colocation.

> [tab] Spot + Derivatives
>
> When trading both markets, each has its own trading engine. The Unified FIX API is the only protocol that covers both markets in a single session.
>
> | Protocol | Spot | Derivatives | Colocation |
> | :- | :-: | :-: | :-: |
> | Spot REST | ✅ | — | — |
> | Spot WebSocket | ✅ | — | ✅ |
> | Derivatives REST | — | ✅ | ✅ |
> | Derivatives WebSocket | — | ✅ (streaming) | ✅ |
> | Unified FIX | ✅ | ✅ | ✅ |
>
> **Recommended setup:**
>
> | Need | Protocol |
> | :- | :- |
> | Spot order entry, low latency | WebSocket v2 or Unified FIX |
> | Derivatives order entry | Unified FIX or Derivatives REST |
> | Spot market data | Spot WebSocket v2 |
> | Derivatives market data | Derivatives WebSocket |
> | Balances, history, funding | Spot REST |
> | Lowest latency across both markets | Unified FIX (colocation) |
>
> > [!NOTE]
> >
> > Rate limits are separate: Spot limits are shared across Spot REST, WebSocket, and the Spot leg of FIX. Derivatives limits run independently on a per-session basis for FIX and per-account for REST.

## Rate limits

| Protocol | Rate limit scope |
| :- | :- |
| Spot REST | Account level — shared with Spot WebSocket and FIX |
| Spot WebSocket | Account level — shared with Spot REST and FIX |
| Spot FIX | Account level — shared with Spot REST and WebSocket |
| Derivatives FIX | Session level — each FIX session has its own bucket |
| Derivatives REST | Account level — separate from Derivatives FIX |

> [!WARNING]
>
> If you run parallel order management systems across multiple protocols on Spot, they share a single rate counter. A burst on one will affect capacity on the others.

## Symbol formats

The same instrument has different identifiers across protocols:

| Instrument | REST | WebSocket | FIX (Symbol) |
| :- | :- | :- | :- |
| Bitcoin / USD | `XXBTZUSD` or `XBT/USD` | `BTC/USD` | `XBT/USD` |
| Ethereum / USD | `XETHZUSD` or `ETH/USD` | `ETH/USD` | `ETH/USD` |
| BTC Perpetual (Derivatives) | `PI_XBTUSD` | `PI_XBTUSD` | `PI_XBTUSD` |

> [!TIP]
>
> WebSocket v2 and REST accept the more readable format (e.g. `BTC/USD`). FIX uses the same short format. REST also accepts the legacy Kraken format (e.g. `XXBTZUSD`) for backwards compatibility.

## Cancel scope

| Protocol | Can cancel orders placed via |
| :- | :- |
| REST | Any source (REST, WS, FIX, UI) |
| WebSocket | Any source (REST, WS, FIX, UI) |
| FIX (single order cancel) | **Same FIX session only** |
| FIX (OrderMassCancelRequest) | All orders on the account |

This is a critical architectural consideration. If your FIX session disconnects and reconnects as a new session, you cannot cancel orders from the previous session using FIX `OrderCancelRequest` — you must use `OrderMassCancelRequest` or fall back to REST/WebSocket.

## Sequencing guarantees

**FIX (sticky routing):** Each FIX session is bound to a specific FIX Gateway instance and follows a deterministic path to the trading engine. New orders and cancels from the same session arrive in order at the engine.

**WebSocket (non-sticky):** Connections are load-balanced. Two messages sent on the same connection may follow different paths and arrive out of order at the engine's inbound queue.

**REST:** No ordering guarantees between separate HTTP requests.

For strategies where the sequence of a cancel and a new order matters (e.g. cancel-replace at a specific price), FIX provides the strongest guarantee.

## WebSocket v1 vs v2

| Feature | v1 | v2 |
| :- | :- | :- |
| Message format | Array | Object |
| L3 order-by-order | — | ✅ |
| Book checksum | Updates only | Snapshot + updates |
| Timestamp precision | Epoch sec, μs | ISO 8601, μs |
| Trade ID | — | Sequential int |
| New features | Frozen | Active development |

v1 is maintained for existing integrations. All new integrations should use v2.

## Related guides

> [card] [Quickstart](https://docs.kraken.com/home/guides/quickstart.md)
>
> Set up your first API key and place your first order

> [card] [Order lifecycle](https://docs.kraken.com/exchange/guides/general/order-lifecycle.md)
>
> How order states and transitions work across all protocols

> [card] [Colocation and connectivity](https://docs.kraken.com/exchange/guides/general/colocation.md)
>
> Low-latency connectivity tiers — from cloud to cross-connect

> [card] [WebSocket reconnection](https://docs.kraken.com/exchange/guides/websockets/reconnection.md)
>
> Handle disconnects, re-subscription, and state reconciliation

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> How rate limits work across REST, WebSocket, and FIX

> [card] [Error reference](https://docs.kraken.com/exchange/guides/general/errors.md)
>
> Full list of error codes and how to handle them
