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
source_url: 'https://docs.kraken.com/exchange/guides/overview'
updated_at: 2026-11-13
---

# Exchange overview

> Spot and Derivatives trading APIs — REST, WebSocket, and FIX for algorithmic trading, market making, and HFT

Kraken's Exchange APIs give you programmatic access to two separate trading engines — **Spot** and **Derivatives** — each with its own endpoints, rate limits, and authentication flows.

## Markets

| | Spot | Derivatives |
| :- | :- | :- |
| Markets | 700+ crypto pairs | Perpetuals and dated contracts on BTC, ETH, and more |
| Order types | Limit, market, stop, take-profit, trailing stop, IOC, post-only | Limit, market, stop, take-profit, IOC |
| Base URL (REST) | `https://api.kraken.com` | `https://futures.kraken.com` |
| WebSocket | `wss://ws.kraken.com/v2` | `wss://futures.kraken.com/ws/v1` |
| Sandbox | UAT available on request via Account Manager | `https://demo-futures.kraken.com` (self-service) |

## Protocols

All three protocols are available for both Spot and Derivatives, but with different capabilities on each engine.

| Protocol | Best for |
| :- | :- |
| **REST** | Account operations, funding, one-off queries |
| **WebSocket** | Real-time market data, order management, and balance updates |
| **FIX 4.4** | Institutional and HFT — deterministic sequencing, cancel-on-disconnect, colocation |

See [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md) for a full feature matrix, latency comparison, and guidance on which protocol to use.

## Workflows

| Workflow | What you need | Where to start |
| :- | :- | :- |
| **Market data** | Public endpoints — no API key needed | REST `GET /0/public/*` or WebSocket public channels |
| **Algorithmic trading** | Private order endpoints + real-time execution data | REST or WebSocket v2 `executions` channel |
| **Execution algos (TWAP)** | Spot REST Algo Trading endpoints — Kraken executes the strategy for you | [Algo Trading overview](https://docs.kraken.com/exchange/guides/algo-trading/overview.md) |
| **Market making** | Low-latency order entry, live book, cancel-on-disconnect | WebSocket v2 or FIX |
| **Account management** | Balances, ledger, funding | REST private endpoints |
| **HFT** | Deterministic sequencing, colocation, FIX replay | FIX 4.4 or WebSocket (Spot); REST or WebSocket (Derivatives) |
| **Sub-accounts** | Multi-account management | REST `CreateSubaccount`, FIX Tags 78/79 |
| **Earn** | Allocate/deallocate to staking products | REST Earn endpoints |

## Feature matrix

| Feature | Spot REST | Spot WebSocket | Spot FIX | Derivatives REST | Derivatives WebSocket | Derivatives FIX |
| :- | :-: | :-: | :-: | :-: | :-: | :-: |
| Market data | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Order entry | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| Account data | ✅ | ✅ | — | ✅ | ✅ | — |
| Funding | ✅ | — | — | ✅ | — | — |
| Earn | ✅ | — | — | — | — | — |
| Subaccounts | ✅ | — | — | ✅ | — | — |

## Performance and hosting

For latency-sensitive strategies, Kraken offers connectivity options from AWS London (\~2 ms) to direct colocation at Equinix London (\~200 μs). See [Colocation and connectivity](https://docs.kraken.com/exchange/guides/general/colocation.md) for the full breakdown.

## Getting started

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> Detailed comparison of REST, WebSocket, and FIX for each market

> [card] [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md)
>
> Understand which permissions to enable for your use case

> [card] [Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md)
>
> Nonce management and HMAC-SHA512 signature generation

> [card] [Order lifecycle](https://docs.kraken.com/exchange/guides/general/order-lifecycle.md)
>
> How order states and transitions work across all protocols

> [card] [Error reference](https://docs.kraken.com/exchange/guides/general/errors.md)
>
> Common errors and how to fix them

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md)
>
> How rate limits work across REST, WebSocket, and FIX
