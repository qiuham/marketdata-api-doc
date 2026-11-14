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
source_url: 'https://docs.kraken.com/exchange/guides/fix/introduction'
updated_at: 2026-11-13
---

# FIX Introduction

> Overview of the Kraken FIX 4.4 API — session architecture, supported messages, connectivity, and key design considerations

The Kraken FIX API is a FIX 4.4 implementation for institutional and HFT clients. It provides the lowest-latency order entry path, deterministic message sequencing, cancel-on-disconnect, and session-based message replay. It covers both Spot and Derivatives markets via a single **Spot FIX API Key**.

To get access, contact your Account Manager.

## Session architecture

FIX sessions follow a sticky routing model:

1. **HAProxy** assigns the FIX Gateway instance with the fewest active connections on initial logon (round-robin selection).
2. **Stickiness at SenderCompID level** — once connected, all messages from that session follow the same path: FIX Gateway → OES → Trading Engine.
3. **Ordering guarantee** — NEW and CANCEL messages from the same session arrive at the Trading Engine in order.

> [!NOTE]
>
> Spot and Derivatives have separate trading engines. Each FIX trading session connects to the appropriate engine based on the instrument being traded.

This is distinct from WebSocket, where connections are load-balanced and two sequential messages may follow different paths to the trading engine's inbound queue.

## Supported messages

| Message Type | Tag 35 | Spot | Derivatives |
| :- | :-: | :-: | :-: |
| NewOrderSingle | D | ✅ | ✅ |
| OrderCancelRequest | F | ✅ | ✅ |
| OrderCancelReplaceRequest (Amend) | G | ✅ | Coming soon |
| ExecutionReport | 8 | ✅ | ✅ |
| OrderStatusRequest | H | ✅ | ✅ |
| OrderMassCancelRequest | q | ✅ | ✅ |
| InstrumentListRequest / InstrumentList | — | ✅ | ✅ |
| MarketDataRequest / Snapshot / Incremental | — | ✅ | ✅ |
| TradingSessionStatusRequest / Status | — | ✅ | ✅ |

> [!WARNING]
>
> On FIX, orders can only be cancelled if they were placed on the same FIX session. The exception is `OrderMassCancelRequest` (Tag 35=q), which cancels all orders on the account regardless of origin. WebSocket and REST can cancel orders from any source (FIX, WebSocket, REST, UI). Design your architecture accordingly.

## Order types

All order types are handled at the Trading Engine level:

| Order type | Spot | Derivatives |
| :- | :-: | :-: |
| Market | ✅ | ✅ |
| Limit | ✅ | ✅ |
| Stop-Loss / Stop-Loss-Limit | ✅ | ✅ |
| Take-Profit / Take-Profit-Limit | ✅ | ✅ |
| Trailing-Stop / Trailing-Stop-Limit | ✅ | ✅ |
| Iceberg (DisplayQty, Tag 1138) | ✅ | — |

Synthetic order types (TWAP, etc.) are not yet available via FIX. They will be handled by a new Algo Engine in a future release.

## Cancel on Disconnect (CoD)

Cancel on Disconnect is enabled by default on every FIX trading session. All open orders placed on the session are automatically cancelled on connection loss.

CoD is configured per session by setting `CancelOrdersOnDisconnect` (Tag 8674) on the Logon message; no onboarding step is required. See the [Logon field reference](https://docs.kraken.com/exchange/api-reference/unified-fix/logon.md) for the accepted values and their behaviour.

For manual intervention, `OrderMassCancelRequest` (Tag 35=q) cancels all orders immediately.

## ClOrdID rules

Each `ClOrdID` (Tag 11) must be **unique within a trading session**. Reuse results in rejection.

Recommended approaches:

* UUIDs
* Incrementing sequence numbers with a session prefix

`ExecID` (Tag 17) is derived from `ClOrdID` at the FIX Gateway level (base32 encoded). If `ClOrdID` is a UUID, only the last 12 hex characters are recoverable from the `ExecID`.

## Self-Trade Prevention (STP)

On **Spot**, STP is configured at the order level via FIX Tag 7928, or at the account level using `SenderSubID` (useful for brokers managing multiple sub-accounts):

| Mode | Tag 7928 | Behaviour |
| :- | :-: | :- |
| Cancel Newest | 1 (default) | Arriving order is cancelled |
| Cancel Oldest | 2 | Resting order is cancelled |
| Cancel Both | 0 | Both orders are cancelled |

On **Derivatives**, STP is managed at the account level via REST API.

## Risk and validation layers

Orders pass through three validation layers before reaching the book:

| Layer | Checks performed |
| :- | :- |
| FIX Gateway | Message format validation, session authentication |
| OES (Order Entry Service) | Account validation, instrument checks, geo-restrictions |
| Trading Engine | Balance checks, self-trade prevention, order limits |

Configurable client-side risk controls (fat-finger limits, max notional per order) are not currently offered. Contact your Account Manager for specific requirements.

## Hours of operation

FIX sessions operate 24/7 with a logical session rollover every day at **22:00 UTC**. The rollover lasts approximately 30 seconds. Both Trading and Market Data sequence numbers reset to `0` after rollover.

## Connectivity

Connections must use **TCP SSL with TLS 1.3**.

### Endpoints

| Environment | Hostname |
| :- | :- |
| Production | `fix.kraken.com` |
| UAT | `fix.uat.kraken.com` |

> [!WARNING]
>
> DNS records carry a 5-minute TTL and must be treated as ephemeral. Always resolve DNS at connection time — do not bind to static IPs.

### FIX port allocation

| Service | Port |
| :- | :- |
| Spot Market Data (L2) | 4000 |
| Spot Trading | 4001 |
| Derivatives Market Data (L2) | 4002 |
| Derivatives Trading | 4003 |
| Derivatives L3 Market Data | 4004 |
| Spot L3 Market Data | 4005 |

WebSocket and REST share TCP 443 (SSL/HTTPS).

### IP whitelisting

Before logging on, your incoming IP addresses must be whitelisted. Kraken will provide your designated CompIDs, hostname, and ports during onboarding.

## Message replay

FIX Gateways support standard sequence number-based replay. If a session reconnects with a lower-than-expected sequence number, the gateway replays `ExecutionReport`s from the requested sequence number, following FIX 4.4 gap-fill and resend request semantics.

Duplicate messages (same sequence number) are handled per FIX protocol standards. If `PossDupFlag` (Tag 43) is set to `Y`, the message is treated as a possible duplicate. Messages with duplicate sequence numbers without the flag may trigger a sequence number resync.

## Rate limits

FIX rate limits are at the **session level** for Derivatives — each FIX session has its own token bucket. For Spot, FIX shares a unified account-level bucket with WebSocket and REST.

When a rate limit is reached, Kraken returns a business-level reject message on FIX. FIX sessions also include an automatic error rate safeguard: if a client generates too many errors per second, the session is automatically disconnected. The threshold can be raised on request through your Account Manager.

See the [rate limits guide](https://docs.kraken.com/exchange/guides/general/ratelimits.md) for full details.

## Related guides

> [card] [FIX authentication](https://docs.kraken.com/exchange/guides/fix/authentication.md)
>
> Logon message, CompID setup, and session establishment

> [card] [Colocation and connectivity](https://docs.kraken.com/exchange/guides/general/colocation.md)
>
> Cross-connect specs, latency tiers, and how to apply for VIP access

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> FIX vs WebSocket vs REST — sequencing, cancel scope, and latency

> [card] [Order lifecycle](https://docs.kraken.com/exchange/guides/general/order-lifecycle.md)
>
> OrdStatus and ExecType values in ExecutionReport (MsgType=8)

> [card] [Order amends](https://docs.kraken.com/exchange/guides/general/amends.md)
>
> Queue priority rules for reduce-only vs price/size amendments

> [card] [Client order IDs](https://docs.kraken.com/exchange/guides/general/clordid.md)
>
> ClOrdID uniqueness, ExecID derivation, and best practices
