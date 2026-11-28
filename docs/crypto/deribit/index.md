---
exchange: deribit
source_url: https://docs.deribit.com/
api_type: Guide
updated_at: 2026-11-28 18:58:37.575822
---

# Welcome to Deribit API

> Deribit is a crypto derivatives exchange offering futures, options, and perpetuals. This documentation is your integration entry point for the API.

> [!NOTE]
>
> Two versions of the API documentation are available. You can switch between them using the version selector button at the top of the page. Changes in the upcoming version will be available in the production version after the next release. For release notes and information about upcoming releases, visit the [Releases section](https://support.deribit.com/hc/en-us/sections/25944734788637-Releases).

## API Interfaces

Deribit provides three different interfaces to access the API:

> [card] [JSON-RPC over WebSocket](https://docs.deribit.com/articles/json-rpc-overview.md#websocket-preferred)
>
> Real-time, bidirectional communication. Recommended for most use cases.

> [card] [JSON-RPC over HTTP](https://docs.deribit.com/articles/json-rpc-overview.md#http-rest)
>
> Simple REST-like interface for HTTP requests.

> [card] [FIX API](https://docs.deribit.com/fix-api/production/overview.md)
>
> Financial Information eXchange protocol for institutional trading.

## Starbase

> [card] [Starbase API](https://docs.deribit.com/starbase/overview.md)
>
> Deribit's high-performance matching engine for institutional traders and market makers, with a Simple Binary Encoding (SBE) order entry API, multicast market data, and FIX Drop Copy.
>
> **Available to selected clients only.** Access requires hosted colocation or a cross-connect in LD4, or AWS PrivateLink. Internet connectivity is not supported.

## Get Started

> [card] [Quickstart Guide](https://docs.deribit.com/articles/deribit-quickstart.md)
>
> Get up and running in minutes with our step-by-step quickstart guide. Make your first API call and start building.

## Core Concepts

> [card] [Authentication](https://docs.deribit.com/articles/creating-api-key.md)
>
> Learn how to create and manage API keys, and authenticate your requests.

> [card] [Rate Limits](https://docs.deribit.com/articles/rate-limits.md)
>
> Understand rate limits, credit system, and how to optimize API usage.

> [card] [Access Scopes](https://docs.deribit.com/articles/access-scope.md)
>
> Learn about API permissions and access scopes for controlling what operations your API keys can perform.

> [card] [Notifications](https://docs.deribit.com/articles/notifications.md)
>
> Subscribe to real-time market data and account updates.

> [card] [Error Codes](https://docs.deribit.com/articles/errors.md)
>
> Reference guide for all API error codes and error handling.

> [card] [API Console](https://test.deribit.com/api_console/)
>
> Interactive API testing tool for exploring and testing API methods.

## Environments

> [!NOTE]
>
> Deribit provides separate test and production environments. All examples in this documentation use the test environment (`test.deribit.com`). Test and production require separate accounts and API keys.

> [card] [Test Environment](https://test.deribit.com/dashboard)
>
> **Purpose:** Development and testing
>
> **HTTP Endpoint:** `https://test.deribit.com/api/v2`
>
> **WebSocket Endpoint:** `wss://test.deribit.com/ws/api/v2`
>
> **Links:**
>
> * [Platform](https://test.deribit.com)
> * [API Console](https://test.deribit.com/api_console/)
> * [API Management](https://test.deribit.com/account/BTC/api)

> [card] [Production Environment](https://www.deribit.com/)
>
> **Purpose:** Live trading
>
> **HTTP Endpoint:** `https://www.deribit.com/api/v2`
>
> **WebSocket Endpoint:** `wss://www.deribit.com/ws/api/v2`
>
> **Links:**
>
> * [Platform](https://www.deribit.com)
> * [API Console](https://www.deribit.com/api_console/)
> * [API Management](https://www.deribit.com/account/BTC/api)

## Need Help?

> [card] [Support Center](https://support.deribit.com)
>
> Browse help articles and documentation.

> [card] [Contact Us](https://insights.deribit.com/contact-us/)
>
> Get technical support, API assistance, or report bugs. Available via Telegram, email, or support portal.


## Related topics

- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [Deribit Block RFQ API Walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough.md)
- [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md)
- [Asymmetric API Keys](https://docs.deribit.com/articles/asymmetric-api-keys.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)