---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/overview
api_type: Guide
updated_at: 2026-07-20 19:24:38.496805
---

# Welcome to Advanced Trade API

Programmatic trading and order management for spot, US futures, and international derivatives.

The **Coinbase Advanced Trade API** gives you programmatic trading and order management — a [REST API](/coinbase-app/advanced-trade-apis/rest-api) for placing and managing orders, and a [WebSocket protocol](/coinbase-app/advanced-trade-apis/websocket/websocket-overview) for real-time market data and account updates. Official SDKs wrap both. [Advanced Trade](https://www.coinbase.com/advanced-trade) is Coinbase’s trading platform for the more experienced trader — a secure way to buy, sell, and trade digital assets across a wide range of markets.

## Interfaces

Choose the interface that fits your integration. All three share one CDP API key.

## REST API

Place, edit, and cancel orders, and read accounts and market data over HTTP.

## WebSocket

Stream live prices, order book, and order/account updates in real time.

## SDKs

Official and sample SDKs for Python, TypeScript, Go, and Java.

## What you can trade

Market| What it covers  
---|---  
**Spot**|  Buy, sell, and trade digital assets across spot pairs  
**US futures**|  CFTC-regulated futures for eligible US clients  
**International derivatives**|  Perpetuals for eligible non-US clients — options and dated futures to follow  
  
## International derivatives are moving to Deribit

On **September 9, 2026** , Coinbase Advanced moves international derivatives from INTX onto a Deribit-powered gateway running the next-generation **Starbase** matching engine. This is a hard cutover — plan your integration now.

Spot and US futures are unaffected and stay on the [Advanced Trade API](/api-reference/advanced-trade-api/rest-api/introduction). International derivatives move to a new gateway with:

  * **A broader product set** — 125+ perpetual contracts at launch, including equity and commodity perpetuals, with up to 50x leverage. Options and dated futures follow.
  * **New native order types** — trailing stops, market-limit, and iceberg orders, plus WebSocket order entry.
  * **A new protocol** — JSON-RPC 2.0 over HTTP or WebSocket. Keep your existing CDP API key.

## Migration Overview

Timeline, new products, order types, margin models, and the migration plan.

## Technical Guide

Authentication, endpoint and schema mapping, and spec references.

## Advanced Trade API Reference

The JSON-RPC method reference for the new derivatives gateway.

## SDKs

## Python SDK

Official — published on PyPI and actively maintained.

## TypeScript SDK

Sample SDK.

## Go SDK

Sample SDK.

## Java SDK

Sample SDK.

## Next steps

## Create an API key

Create a CDP API key and make your first authenticated call.

## Try the sandbox

Test your integration against the sandbox before going live.

**See also:** [What is Advanced Trade?](https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/what-is-advanced-trade) · [Advanced Developer Program](https://www.coinbase.com/developer-platform/products/advanced-trade-developer-program)