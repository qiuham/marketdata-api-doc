---
exchange: deribit
source_url: https://docs.deribit.com/starbase/multicast-channels
api_type: Starbase
updated_at: 2026-11-19 19:05:49.576770
---

# Multicast Channels

> Starbase SBE Market Data Feed multicast channels over UDP. Channel assignments are sharded by product type, with A/B twins for redundancy and low latency.

> [!NOTE]
>
> **Multicast & networking support**: For detailed multicast or networking questions, contact \[[colo-support@coinbase.com](mailto:colo-support@coinbase.com)]\(mailto:[colo-support@coinbase.com](mailto:colo-support@coinbase.com)).

> [!NOTE]
>
> Market data will only be sent by the **active** switch and duplicate data will not be received. The secondary connection will begin to receive market data during a failover scenario.

## Cross-Connects & Non-Colocated Access

Cross-connects are available in LD4. Deribit is running a cable-length equalization process so that latency does not depend on a client's rack placement within the data center. Contact [[colo-support@coinbase.com](mailto:colo-support@coinbase.com)](mailto:colo-support@coinbase.com) to arrange a cross-connect.

Clients who are not colocated or cross-connected can still receive multicast market data over AWS via the [Deribit AWS Multicast Service](https://support.deribit.com/hc/en-us/articles/25944617728285-Deribit-AWS-Multicast-Service-Instruction).

## Feed Characteristics

* Each gateway publishes market data from a **single event-loop thread**, so sequence numbers within a channel are strictly increasing and monotonic.
* Updates are **batched**: a single UDP packet can contain multiple messages (see `messageCount` in the [packet header](https://docs.deribit.com/starbase/binary-api-reference.md#udp-messages)).
* This is a **Level 3 (market-by-order)** feed. Every matching engine event that affects the book is reflected here, including an order that is added and then immediately removed, which still produces both the add (`Buy Put`/`Sell Put`) and the subsequent `Order Delete` message. There is no separate Level 2 (aggregated price-level) feed on Starbase.
* Alongside order book events, the feed publishes derived and reference statistics: index prices via `IndexInfo` (12), price bands and mark prices via `InstrumentInfo` (14), and funding, settlement prices, and open interest via `InstrumentRef` (15). See [Reference Data](https://docs.deribit.com/starbase/reference-data.md#index-prices-and-derived-statistics). Statistics not covered by these messages (for example, 24-hour volume) remain available from the [classic JSON-RPC API](https://docs.deribit.com/articles/json-rpc-overview.md) (for example, [`public/ticker`](https://docs.deribit.com/api-reference/market-data/public-ticker) or [`public/get_book_summary_by_instrument`](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_instrument)).

| Product Type | Feed | Type | IP Address | Port |
| - | - | - | - | - |
| **BTC Perpetuals, Futures and Future Spreads** | A | Snapshot | 224.0.12.192 | 4230 |
| | | Incremental | 224.0.12.193 | 4220 |
| | B | Snapshot | 224.0.12.208 | 4230 |
| | | Incremental | 224.0.12.209 | 4220 |
| | Test | Snapshot | 224.0.12.224 | 4230 |
| | | Incremental | 224.0.12.225 | 4220 |
| **BTC Options and Option Combinations** | A | Snapshot | 224.0.12.194 | 4230 |
| | | Incremental | 224.0.12.195 | 4220 |
| | B | Snapshot | 224.0.12.210 | 4230 |
| | | Incremental | 224.0.12.211 | 4220 |
| | Test | Snapshot | 224.0.12.226 | 4230 |
| | | Incremental | 224.0.12.227 | 4220 |
| **ETH Perpetuals, Futures and Future Spreads** | A | Snapshot | 224.0.12.196 | 4230 |
| | | Incremental | 224.0.12.197 | 4220 |
| | B | Snapshot | 224.0.12.212 | 4230 |
| | | Incremental | 224.0.12.213 | 4220 |
| | Test | Snapshot | 224.0.12.228 | 4230 |
| | | Incremental | 224.0.12.229 | 4220 |
| **ETH Options and Option Combinations** | A | Snapshot | 224.0.12.198 | 4230 |
| | | Incremental | 224.0.12.199 | 4220 |
| | B | Snapshot | 224.0.12.214 | 4230 |
| | | Incremental | 224.0.12.215 | 4220 |
| | Test | Snapshot | 224.0.12.230 | 4230 |
| | | Incremental | 224.0.12.231 | 4220 |
| **Tier 2 Futures, Perpetuals and Future Spreads** | A | Snapshot | 224.0.12.200 | 4230 |
| | | Incremental | 224.0.12.201 | 4220 |
| | B | Snapshot | 224.0.12.216 | 4230 |
| | | Incremental | 224.0.12.217 | 4220 |
| | Test | Snapshot | 224.0.12.232 | 4230 |
| | | Incremental | 224.0.12.233 | 4220 |
| **Tier 2 Options and Option Combinations** | A | Snapshot | 224.0.12.202 | 4230 |
| | | Incremental | 224.0.12.203 | 4220 |
| | B | Snapshot | 224.0.12.218 | 4230 |
| | | Incremental | 224.0.12.219 | 4220 |
| | Test | Snapshot | 224.0.12.234 | 4230 |
| | | Incremental | 224.0.12.235 | 4220 |
| **Tier 3 Futures, Perpetuals and Future Spreads** | A | Snapshot | 224.0.12.204 | 4230 |
| | | Incremental | 224.0.12.205 | 4220 |
| | B | Snapshot | 224.0.12.220 | 4230 |
| | | Incremental | 224.0.12.221 | 4220 |
| | Test | Snapshot | 224.0.12.236 | 4230 |
| | | Incremental | 224.0.12.237 | 4220 |
| **RWA and pre-IPO perpetuals** | A | Snapshot | 224.0.12.206 | 4230 |
| | | Incremental | 224.0.12.207 | 4220 |
| | B | Snapshot | 224.0.12.222 | 4230 |
| | | Incremental | 224.0.12.223 | 4220 |
| | Test | Snapshot | 224.0.12.238 | 4230 |
| | | Incremental | 224.0.12.239 | 4220 |

Retransmit:

Each channel has its own retransmit port. The `Port` column is the UDP unicast port used by colocation and cross-connect clients; the `AWS Port` column is the **TCP** port used by clients connecting over AWS Private Link. See [Retransmit Gateway](https://docs.deribit.com/starbase/retransmit-gateway.md) for the request protocol.

| Product Type | Feed | IP Address | Port | AWS Port (TCP) |
| :- | - | :- | :- | :- |
| **BTC Perpetuals, Futures and Future Spreads** | A | 195.138.37.9 | 4240 | 34240 |
| | B | 195.138.37.10 | 4240 | 24240 |
| | Test | 195.138.37.139 | 4240 | Not yet available |
| **BTC Options and Option Combinations** | A | 195.138.37.9 | 4241 | 34241 |
| | B | 195.138.37.10 | 4241 | 24241 |
| | Test | 195.138.37.139 | 4241 | Not yet available |
| **ETH Perpetuals, Futures and Future Spreads** | A | 195.138.37.9 | 4242 | 34242 |
| | B | 195.138.37.10 | 4242 | 24242 |
| | Test | 195.138.37.139 | 4242 | Not yet available |
| **ETH Options and Option Combinations** | A | 195.138.37.9 | 4243 | 34243 |
| | B | 195.138.37.10 | 4243 | 24243 |
| | Test | 195.138.37.139 | 4243 | Not yet available |
| **Tier 2 Futures, Perpetuals and Future Spreads** | A | 195.138.37.9 | 4244 | 34244 |
| | B | 195.138.37.10 | 4244 | 24244 |
| | Test | 195.138.37.139 | 4244 | Not yet available |
| **Tier 2 Options and Option Combinations** | A | 195.138.37.9 | 4245 | 34245 |
| | B | 195.138.37.10 | 4245 | 24245 |
| | Test | 195.138.37.139 | 4245 | Not yet available |
| **Tier 3 Futures, Perpetuals and Future Spreads** | A | 195.138.37.9 | 4246 | 34246 |
| | B | 195.138.37.10 | 4246 | 24246 |
| | Test | 195.138.37.139 | 4246 | Not yet available |
| **RWA and pre-IPO perpetuals** | A | 195.138.37.9 | 4247 | 34247 |
| | B | 195.138.37.10 | 4247 | 24247 |
| | Test | 195.138.37.139 | 4247 | Not yet available |


## Related topics

- [Multicast Retransmit Gateway](https://docs.deribit.com/starbase/retransmit-gateway.md)
- [Multicast Subscription Guide](https://docs.deribit.com/starbase/multicast-subscription-guide.md)
- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
- [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)