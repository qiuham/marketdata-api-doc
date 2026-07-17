---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/introduction
api_type: REST
updated_at: 2026-07-17 19:04:50.564813
---

# Coinbase Advanced Trade API

The Advanced Trade API is Coinbase’s programmatic interface for **spot crypto and derivatives** — order entry and management, account and portfolio data, and real-time market data over REST and WebSocket.

## Spot & US Derivatives

Spot crypto and CFTC-regulated US futures.

  * **REST** at `https://api.coinbase.com/api/v3/brokerage`
  * **WebSocket** at `wss://advanced-trade-ws.coinbase.com` (public) and `wss://advanced-trade-ws-user.coinbase.com` (private)

## REST

Order entry and management, accounts, portfolios, and market data over REST.Download the [OpenAPI spec](/api-reference/advanced-trade-api/rest-api/advanced-trade-spec.yaml).

## WebSocket Streams

Real-time market data and user order, position, and futures balance streams.Download the [AsyncAPI spec](/api-reference/advanced-trade-api/advanced-trade-asyncapi.json).

## International Derivatives

**Coming soon.** The Deribit-powered gateway goes live **September 9, 2026**. It’s published ahead of cutover so you can plan your integration now — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

On **September 9, 2026** , Coinbase Advanced is moving international derivatives from INTX onto a Deribit-powered gateway running the next-generation Starbase engine.

  * New native order types and features — trailing stops, market-limit orders and WebSocket order entry.
  * Deeper liquidity, lower-latency execution and a broader product set (options and dated futures to follow).
  * The gateway is **JSON-RPC 2.0** over both HTTP and WebSocket.

## HTTP / WebSocket

Every JSON-RPC method can be sent over **either HTTP or WebSocket**.Download the [OpenAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-openapi.json).

## Websocket Streams

Streaming channels for live order, position, portfolio, and market data.Download the [AsyncAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-asyncapi.json).