---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/overview
api_type: Guide
updated_at: 2026-08-29 18:52:49.653095
---

# Welcome to Advanced Trade API

Programmatic trading and order management for spot, US futures, and Global Derivatives.

The **Coinbase Advanced Trade API** gives you programmatic trading and order management — a [REST API](/coinbase-app/advanced-trade-apis/rest-api) for placing and managing orders, and a [WebSocket protocol](/coinbase-app/advanced-trade-apis/websocket/websocket-overview) for real-time market data and account updates. Official SDKs wrap both. [Advanced Trade](https://www.coinbase.com/advanced-trade) is Coinbase’s trading platform for the more experienced trader — a secure way to buy, sell, and trade digital assets across a wide range of markets.

## Interfaces

Choose the interface that fits your integration. All three share one CDP API key.

## REST API

Place, edit, and cancel orders, and read accounts and market data over HTTP.

## WebSocket

Stream live prices, order book, and order/account updates in real time.

## SDKs

Official and sample SDKs for Python, TypeScript, Go, and Java.

## What you can tradeAdvanced Trade APIs

# Welcome to Advanced Trade API

Programmatic trading and order management for spot, US futures, and Global Derivatives.

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
**Global Derivatives**|  Perpetuals for eligible non-US clients — options and dated futures to follow  
  
## International derivatives are moving to Deribit

On **September 9, 2026** , Advanced Trade moves international derivatives from INTX onto a Deribit-powered gateway running on the **Starbase** platform. This is a hard cutover — plan your integration now.

Spot and US futures are unaffected and stay on the [Advanced Trade API](/api-reference/advanced-trade-api/rest-api/introduction). International derivatives move to a new gateway with:

  * **A broader product set** — 125+ perpetual contracts at launch, including equity and commodity perpetuals, with up to 50x leverage. Options and dated futures follow.
  * **New native order types** — trailing stops, market-limit, and iceberg orders, plus WebSocket order entry.
  * **A new protocol** — JSON-RPC 2.0 over HTTP or WebSocket. Keep your existing CDP API key.

## Migration Overview

Timeline, new products, order types, margin models, and the migration plan.

## Technical Guide

Authentication, endpoint and schema mapping, and spec references.

## Advanced Trade API Reference

Hosts and specs for spot, US derivatives, and Global Derivatives.

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

Guides

# Listen for Order Updates with the WebSocket SDK

This quickstart explains how to set up and subscribe to WebSocket channels with the **Advanced API Python WebSocket Client**. This WebSocket Client is a Python package that makes it easy to interact with the [WebSocket API](/coinbase-app/advanced-trade-apis/websocket/websocket-overview).

## Introduction

Consider going through the [REST SDK quickstart](/coinbase-app/advanced-trade-apis/guides/sdk-rest-api) first as it is referenced in this tutorial.

See the SDK [README](https://github.com/coinbase/coinbase-advanced-py/blob/master/README.md) for detailed instructions, plus the full suite of SDK functions.

## Prerequisites

### Creating API Keys

To you use the SDK, you must first create your own [API key](/coinbase-app/authentication-authorization/api-key-authentication) on the Coinbase Developer Platform (CDP).

### Installing the SDK

To install the Coinbase Advanced API Python SDK, run the following command in a terminal:
    
    
    pip3 install coinbase-advanced-py
    Market| What it covers  
    **Spot**|  Buy, sell, and trade digital assets across spot pairs  
    **US futures**|  CFTC-regulated futures for eligible US clients  
    **Global Derivatives**|  Perpetuals for eligible non-US clients — options and dated futures to follow  
      
    
    
    
    ## 
    
    
    
    International derivatives are moving to Deribit
    
    
    
    
    On **September 9, 2026** , Advanced Trade moves international derivatives from INTX onto a Deribit-powered gateway running on the **Starbase** platform. This is a hard cutover — plan your integration now.
    
    
    Spot and US futures are unaffected and stay on the [Advanced Trade API](/api-reference/advanced-trade-api/rest-api/introduction). International derivatives move to a new gateway with:
    
    
    
    
        * **A broader product set** — 125+ perpetual contracts at launch, including equity and commodity perpetuals, with up to 50x leverage. Options and dated futures follow.
    
    
        * **New native order types** — trailing stops, market-limit, and iceberg orders, plus WebSocket order entry.
    
    
        * **A new protocol** — JSON-RPC 2.0 over HTTP or WebSocket. Keep your existing CDP API key.
    
    
    
    
    
    ## Migration Overview
    
    Timeline, new products, order types, margin models, and the migration plan.
    
    ## Technical Guide
    
    Authentication, endpoint and schema mapping, and spec references.
    
    ## Advanced Trade API Reference
    
    Hosts and specs for spot, US derivatives, and Global Derivatives.
    
    
    
    
    ## 
    
    
    
    SDKs
    
    
    
    
    ## Python SDK
    
    Official — published on PyPI and actively maintained.
    
    ## TypeScript SDK
    
    Sample SDK.
    
    ## Go SDK
    
    Sample SDK.
    
    ## Java SDK
    
    Sample SDK.
    
    
    
    
    ## 
    
    
    
    Next steps
    
    
    
    
    ## Create an API key
    
    Create a CDP API key and make your first authenticated call.
    
    ## Try the sandbox
    
    Test your integration against the sandbox before going live.
    
    
    **See also:** [What is Advanced Trade?](https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/what-is-advanced-trade) · [Advanced Developer Program](https://www.coinbase.com/developer-platform/products/advanced-trade-developer-program)