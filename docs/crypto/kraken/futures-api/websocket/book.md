---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/book
api_type: WebSocket
updated_at: 2026-07-21 19:24:40.610395
---

# Exchange overview

Kraken’s Exchange APIs give you programmatic access to two separate trading engines — **Spot** and **Derivatives** — each with its own endpoints, rate limits, and authentication flows.

## 

Markets

| Spot| Derivatives  
---|---|---  
Markets| 700+ crypto pairs| Perpetuals and dated contracts on BTC, ETH, and more  
Order types| Limit, market, stop, take-profit, trailing stop, IOC, post-only| Limit, market, stop, take-profit, IOC  
Base URL (REST)| `https://api.kraken.com`| `https://futures.kraken.com`  
WebSocket| `wss://ws.kraken.com/v2`| `wss://futures.kraken.com/ws/v1`  
Sandbox| UAT available on request via Account Manager| `https://demo-futures.kraken.com` (self-service)  
  
## 

Protocols

All three protocols are available for both Spot and Derivatives, but with different capabilities on each engine.

Protocol| Best for  
---|---  
**REST**|  Account operations, funding, one-off queries  
**WebSocket**|  Real-time market data, order management, and balance updates  
**FIX 4.4**|  Institutional and HFT — deterministic sequencing, cancel-on-disconnect, colocation  
  
See [Choose your protocol](/exchange/guides/general/api-comparison) for a full feature matrix, latency comparison, and guidance on which protocol to use.

## 

Workflows

Workflow| What you need| Where to start  
---|---|---  
**Market data**|  Public endpoints — no API key needed| REST `GET /0/public/*` or WebSocket public channels  
**Algorithmic trading**|  Private order endpoints + real-time execution data| REST or WebSocket v2 `executions` channel  
**Market making**|  Low-latency order entry, live book, cancel-on-disconnect| WebSocket v2 or FIX  
**Account management**|  Balances, ledger, funding| REST private endpoints  
**HFT**|  Deterministic sequencing, colocation, FIX replay| FIX 4.4 or WebSocket (Spot); REST or WebSocket (Derivatives)  
**Sub-accounts**|  Multi-account management| REST `CreateSubaccount`, FIX Tags 78/79  
**Earn**|  Allocate/deallocate to staking products| REST Earn endpoints  
  
## 

Feature matrix

Feature| Spot REST| Spot WebSocket| Spot FIX| Derivatives REST| Derivatives WebSocket| Derivatives FIX  
---|---|---|---|---|---|---  
Market data| ✅| ✅| ✅| ✅| ✅| ✅  
Order entry| ✅| ✅| ✅| ✅| —| ✅  
Account data| ✅| ✅| —| ✅| ✅| —  
Funding| ✅| —| —| ✅| —| —  
Earn| ✅| —| —| —| —| —  
Subaccounts| ✅| —| —| ✅| —| —  
  
## 

Performance and hosting

For latency-sensitive strategies, Kraken offers connectivity options from AWS London (~2 ms) to direct colocation at Equinix London (~200 μs). See [Colocation and connectivity](/exchange/guides/general/colocation) for the full breakdown.

## 

Getting started

## [Choose your protocolDetailed comparison of REST, WebSocket, and FIX for each market](/exchange/guides/general/api-comparison)

## [API key permissionsUnderstand which permissions to enable for your use case](/exchange/guides/rest/api-keys)

## [AuthenticationNonce management and HMAC-SHA512 signature generation](/exchange/guides/rest/authentication)

## [Order lifecycleHow order states and transitions work across all protocols](/exchange/guides/general/order-lifecycle)

## [Error referenceCommon errors and how to fix them](/exchange/guides/general/errors)

## [Rate limitsHow rate limits work across REST, WebSocket, and FIX](/exchange/guides/general/ratelimits)

Was this page helpful?

[Choose your protocol](/exchange/guides/general/api-comparison)

Ctrl+I