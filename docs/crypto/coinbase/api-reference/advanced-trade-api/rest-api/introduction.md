---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/introduction
api_type: REST
updated_at: 2026-08-29 18:52:42.750187
---

# Coinbase Advanced Trade API

The Advanced Trade API is Coinbase’s programmatic interface for **spot crypto and derivatives** — order entry and management, account and portfolio data, and real-time market data over REST and WebSocket.

## Spot & US Derivatives

Spot crypto and CFTC-regulated US futures.

  * Market, limit, stop-limit, bracket and attached take-profit/stop-loss orders.
  * Accounts, portfolios and converts on the same REST host as the order path.
  * The API is **REST** for request-response and **WebSocket** for market data and user streams.

## REST

Order entry and management, accounts, portfolios, and market data over REST.Download the [OpenAPI spec](/api-reference/advanced-trade-api/rest-api/advanced-trade-spec.yaml).

## WebSocket Streams

Real-time market data and user order, position, and futures balance streams.Download the [AsyncAPI spec](/api-reference/advanced-trade-api/advanced-trade-asyncapi.json).

## Global Derivatives

**Coming soon.** The Deribit-powered gateway goes live **September 9, 2026**. It is published ahead of cutover so you can plan your integration now — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

On **September 9, 2026** , Advanced Trade is moving Global Derivatives from INTX onto a Deribit-powered gateway running on the Starbase platform.

  * New native order types and features — trailing stops, market-limit orders and WebSocket order entry.
  * Deeper liquidity, lower-latency execution and a broader product set (options and dated futures to follow).
  * The gateway is **JSON-RPC 2.0** over both HTTP and WebSocket.

## REST

JSON-RPC request-response over HTTP. Snapshots such as `public/get_index_price`.Download the [OpenAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-openapi.json).

## WebSocket

Public market data on the public WebSocket. Order and user channels on the private WebSocket.Download the [AsyncAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-asyncapi.json).

## URLs

REST uses one URL for public and private methods.

Venue| REST (public and private)  
---|---  
Spot and US Derivatives| `https://api.coinbase.com/api/v3/brokerage`  
Global Derivatives| `https://drb.coinbase.com/api/v2`  
  
WebSocket uses a public host and a private host.

Venue| WebSocket public| WebSocket private  
---|---|---  
Spot and US Derivatives| `wss://advanced-trade-ws.coinbase.com`| `wss://advanced-trade-ws-user.coinbase.com`  
Global Derivatives| `wss://streams.drb.coinbase.com/ws/api/v2`| `wss://drb.coinbase.com/ws/api/v2`  
  
On Global Derivatives, HTTP methods also run on the private WebSocket. The public WebSocket is subscription-only.