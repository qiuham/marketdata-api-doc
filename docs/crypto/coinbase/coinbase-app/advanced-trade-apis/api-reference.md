---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/api-reference
api_type: Trading
updated_at: 2026-06-28 19:25:26.312142
---

# Coinbase Advanced Trade API

The Advanced Trade API is Coinbase’s programmatic interface for **spot crypto and derivatives** — order entry and management, account and portfolio data, and real-time market data over REST and WebSocket.

## Surfaces

**Spot & US Derivatives** \- Spot crypto and CFTC-regulated US futures.

  * REST at `https://api.coinbase.com/api/v3/brokerage`
  * WebSocket at `wss://advanced-trade-ws.coinbase.com` (public) and `wss://advanced-trade-ws-user.coinbase.com` (private)

**International Derivatives** — migration notice.

  * On September 09, 2026 - Coinbase Advanced is moving international derivatives from INTX onto a Deribit-powered gateway running the next-generation Starbase engine.
  * JSON-RPC 2.0 over HTTP and WebSocket at `https://drb.coinbase.com`.

## Migration from INTX to Deribit-powered gateway

**International derivatives — coming soon.** The Deribit-powered gateway goes live **September 9, 2026**. It’s published ahead of cutover so you can plan your integration now — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

  * New native order types and features — trailing stops, market-limit orders and WebSocket order entry will become available.
  * Deeper liquidity, lower-latency execution and a broader product set (options and dated futures to follow).
  * The gateway speaks **JSON-RPC 2.0** over both HTTP and WebSocket.

## HTTP / WebSockets API

Every JSON-RPC method can be sent over **either HTTP or WebSocket**.Download the [OpenAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-openapi.json).

## WebSockets Streaming API

Streaming channels for live order, position, portfolio, and market-data.Download the [AsyncAPI spec](/api-reference/coinbase-deribit-app-api/adv-starbase-asyncapi.json).