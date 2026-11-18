---
exchange: deribit
source_url: https://docs.deribit.com/starbase/gateway-connectivity
api_type: Starbase
updated_at: 2026-11-18 18:59:11.770391
---

# Gateway Connectivity

> Starbase gateway endpoints, host lists, connection credentials, and network requirements for reaching the order entry and market data servers.

## Connectivity

### Test Environment

> [!WARNING]
>
> **The test network does not mirror the production gateway topology.** Test uses a single A/B order-entry pair because the full production hardware footprint is not available in the test environment. Production retains A/B redundancy but is sharded into separate BTC, ETH, Tier 2, Tier 3, and RWA gateway pairs. Build routing from the environment-specific tables below rather than reusing test addresses or connection assumptions in production.

| Gateway | Side | Address | Port | Protocol | AWS Port |
| - | - | - | - | - | - |
| sbe-order | A | 195.138.37.137 | 4210 | TCP | 14210 |
| sbe-order | B | 195.138.37.138 | 4210 | TCP | 24210 |
| fix-drop-copy | A | 195.138.37.139 | 4130 | TCP | 14130 |
| sbe-marketdata-retransmit | A | 195.138.37.139 | 4240 – 4247 | UDP Unicast + UDP Return | Not yet available |
| sbe-marketdata-incremental | A | [See Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) | 4220 | UDP Multicast | Multicast Relay |
| sbe-marketdata-snapshot | A | [See Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) | 4230 | UDP Multicast | Multicast Relay |
| REST | A | 195.138.37.137 | 4410 | HTTP | 14410 |
| REST | B | 195.138.37.138 | 4410 | HTTP | 24410 |

### Production Environment

| Gateway | Side | Address | Port | Protocol | AWS Port |
| - | - | - | - | - | - |
| sbe-order (BTC) | A | 195.138.37.1 | 4210 | TCP | 34210 |
| sbe-order (ETH) | A | 195.138.37.3 | 4211 | TCP | 34211 |
| sbe-order (Tier 2) | A | 195.138.37.5 | 4212 | TCP | 34212 |
| sbe-order (Tier 3) | A | 195.138.37.7 | 4213 | TCP | 34213 |
| sbe-order (RWA) | A | 195.138.37.7 | 4214 | TCP | 34214 |
| sbe-order (BTC) | B | 195.138.37.2 | 4210 | TCP | 44210 |
| sbe-order (ETH) | B | 195.138.37.4 | 4211 | TCP | 44211 |
| sbe-order (Tier 2) | B | 195.138.37.6 | 4212 | TCP | 44212 |
| sbe-order (Tier 3) | B | 195.138.37.8 | 4213 | TCP | 44213 |
| sbe-order (RWA) | B | 195.138.37.8 | 4214 | TCP | 44214 |
| fix-drop-copy | A | 195.138.37.7 | 4130 | TCP | 34130 |
| fix-drop-copy | B | 195.138.37.8 | 4130 | TCP | 44130 |
| sbe-marketdata-retransmit | A | 195.138.37.9 | 4240 – 4247 | UDP Unicast + UDP Return | 34240 – 34247 (TCP) |
| sbe-marketdata-retransmit | B | 195.138.37.10 | 4240 – 4247 | UDP Unicast + UDP Return | 24240 – 24247 (TCP) |
| sbe-marketdata-incremental | A | [See Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) | 4220 | UDP Multicast | Multicast Relay |
| sbe-marketdata-incremental | B | [See Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) | 4220 | UDP Multicast | Multicast Relay |
| sbe-marketdata-snapshot | A | [See Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) | 4230 | UDP Multicast | Multicast Relay |
| sbe-marketdata-snapshot | B | [See Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md) | 4230 | UDP Multicast | Multicast Relay |
| REST | A | 195.138.37.5 | 4410 | HTTP | 34410 |
| REST | B | 195.138.37.6 | 4410 | HTTP | 44410 |

> [!NOTE]
>
> Retransmit uses one port per market data channel. For the mapping of each product type to its retransmit port in both environments, see [Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md).

## Gateway Architecture

Starbase will have multiple gateways available for order entry. Gateways will always be run in pairs, A and B, for resilience. Both gateways run in a **hot-hot** configuration, meaning they are both fully active at all times and neither should be treated as a backup. For optimal latency you should connect to and use both gateways in a pair simultaneously.

**Rate limits on A and B are independent.** For example, a rate limit of 100 requests/s means you can send 100 requests/s on Gateway A *and* 100 requests/s on Gateway B, for an effective combined rate of 200 requests/s per pair.

Each pair of gateways will provide access to a set of order books, to allow for horizontal scaling. The available set of order books per gateway might change depending on the distribution of throughput per order book. Order books belonging to the same underlying asset will always appear on the same gateway to ensure the atomicity of MMP and implied matching. See below for an example order book layout of the gateways.

| Gateway | Order Books |
| - | - |
| Gateway 1 A | All BTC\_USD and BTC\_USDC derivatives |
| Gateway 1 B | All BTC\_USD and BTC\_USDC derivatives |
| Gateway 2 A | All ETH\_USD and ETH\_USDC derivatives |
| Gateway 2 B | All ETH\_USD and ETH\_USDC derivatives |
| Gateway 3 A | All [Tier 2](https://docs.deribit.com/starbase/underlying-tiers.md#tier-2) derivatives |
| Gateway 3 B | All [Tier 2](https://docs.deribit.com/starbase/underlying-tiers.md#tier-2) derivatives |
| Gateway 4 A | All [Tier 3](https://docs.deribit.com/starbase/underlying-tiers.md#tier-3) derivatives |
| Gateway 4 B | All [Tier 3](https://docs.deribit.com/starbase/underlying-tiers.md#tier-3) derivatives |
| Gateway 5 A | All RWA and pre-IPO derivatives |
| Gateway 5 B | All RWA and pre-IPO derivatives |

## API Keys

Starbase uses its own API keys, separate from standard Deribit API keys and created in the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel. A standard Deribit API key cannot authenticate to a Starbase gateway. Create and assign a [Member](https://docs.deribit.com/starbase/creating-member.md) first, then follow [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md) for key scopes and the rest of the setup flow.

Each API key can establish exactly one connection to each gateway. For example, if there are 5 gateway pairs, one API key can be used to establish 10 connections. This ensures a clear audit trail for messages to help both Deribit and the client to debug and eliminates the need for gateways to communicate with each other.

Trying to establish a second connection with the same key to the same gateway will result in a disconnection of the first connection.

### Connecting to multiple gateways

**Connection Rules**:

* Clients can have only **one connection per gateway instance per API key**
* Clients can use the **same API key on every gateway**

This means you can connect to different gateway instances using the same API credentials, but you cannot maintain multiple simultaneous connections to the same gateway instance with the same credentials.

**Event Scoping**: An SBE connection receives events about orders sent by the API key on that gateway:

* Orders submitted on Gateway A with API Key X generate events on the Gateway A connection using API Key X
* Orders submitted on Gateway B with API Key X generate events on the Gateway B connection using API Key X
* When an amend for that order is sent from the other gateway, `AmendOrderResponse` is delivered on both connections. The two copies share `clientOrderId`, `orderId`, and `correlationId`. A cancel sent from the other gateway delivers `CancelOrderResponse` on the cancelling connection and an unsolicited `OrdersCanceled` on the submitting connection (schema version `17` or later). Fills stay on the gateway that submitted the order. See [Cross-session acknowledgements](https://docs.deribit.com/starbase/amending-order.md#cross-session-acknowledgements)
* Orders submitted with API Key A do not generate events on connections established with API Key B
* Exception: sessions that opt in to [liquidation notifications](https://docs.deribit.com/starbase/unsolicited-events.md#liquidation-notifications) (schema version `22`) receive liquidation fills and LSP/ADL position moves for their portfolio, whichever session or key the activity relates to

This is done to ensure many API Keys can be given out to a single Portfolio without Portfolio-level bottlenecks becoming an issue.

For a consolidated view of all activity on a single Portfolio, the [FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md) is available. Standard Deribit WebSocket APIs (e.g. `private/get_user_trades_by_instrument`) work for trades placed through Starbase, but `private/get_open_orders*` and private order subscriptions do not return open Starbase orders. Use the Starbase REST order snapshot, FIX Drop Copy, or an SBE session to see open order state.


## Related topics

- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)
- [REST Order Gateway Authentication](https://docs.deribit.com/starbase/rest-authentication.md)
- [Multicast Retransmit Gateway](https://docs.deribit.com/starbase/retransmit-gateway.md)
- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md)