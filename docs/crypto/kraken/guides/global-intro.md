---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/global-intro
api_type: Guide
updated_at: 2026-05-27 19:58:01.998670
---

# Kraken APIs

## Introduction

We offer a range of Application Programming Interfaces (APIs) to send order transactions, stream market data, manage accounts, and integrate crypto services into your applications.

### Direct Trading APIs

For direct access to Kraken's spot and futures trading platforms:

  * [**REST API**](/api/docs/guides/spot-rest-intro): REST (REpresentational State Transfer) is one of the most widely used architectures for building web-based applications, use this interface for request-response style messages over HTTP.

  * [**Websocket API**](/api/docs/guides/spot-ws-intro): WebSockets offers 2-way communication over a persisted network connection. This interface is useful for receiving event-driven responses without the need to continuously poll for data.

  * [**FIX API**](/api/docs/guides/fix-intro): FIX (Financial Information eXchange) is used extensively by institutional firms (buy and sell-side) for sending key-value pair trading data over a session based protocol.

### Embed API (B2B / B2B2C)

For businesses looking to integrate crypto services into their own products:

  * [**Embed REST API**](/api/docs/embed-api/list-embed-assets): Enables partners to offer crypto trading, portfolio management, and earn features to their end users. The Embed API is designed for B2B and B2B2C use cases where you want to provide Kraken-powered crypto services under your own brand.

With the Embed API, partners can:

  * Create and manage users on behalf of their customers
  * Execute trades using a quote-based model
  * Access portfolio and earn features
  * Receive real-time updates via webhooks

See the [Embed Authentication Guide](/api/docs/guides/embed-rest-auth) and [Your First Trade](/api/docs/guides/embed-first-trade) to get started.

### Choosing an API

Our APIs offer a versatile ecosystem. Each API has distinct characteristics - clients can choose a single protocol or combination of protocols that best fit their requirements.

Please see the Kraken [support article](https://support.kraken.com/hc/en-us/articles/4404197772052-Which-API-should-I-use-REST-versus-WebSocket) for further information to help choose an API.

### Summary of product versus exchange / API

| **Spot REST**| **Spot Websocket**| **Spot FIX**| **Futures REST**| **Futures Websocket**| **Futures FIX**  
---|---|---|---|---|---|---  
**Market Data**| [Yes](/api/docs/rest-api/get-order-book)| [Yes](/api/docs/websocket-v2/book)| [Yes](/api/docs/fix-api/mdr-fix)| [Yes](/api/docs/futures-api/trading/get-orderbook)| [Yes](/api/docs/futures-api/websocket/book)| [Yes](/api/docs/fix-api/mdr-fix)  
**Order Transactions**| [Yes](/api/docs/rest-api/add-order)| [Yes](/api/docs/websocket-v2/add_order)| [Yes](/api/docs/fix-api/nos-fix)| [Yes](/api/docs/futures-api/trading/send-order)| -| [Yes](/api/docs/fix-api/nos-fix)  
**Account Data**| [Yes](/api/docs/rest-api/get-account-balance)| [Yes](/api/docs/websocket-v2/balances)| -| [Yes](/api/docs/futures-api/trading/get-accounts)| [Yes](/api/docs/futures-api/websocket/balances)| -  
**Funding**| [Yes](/api/docs/rest-api/get-deposit-methods)| -| -| [Yes](/api/docs/futures-api/trading/transfer)| -| -  
**Earn**| [Yes](/api/docs/rest-api/allocate-strategy)| -| -| -| -| -  
**Subaccounts**| [Yes](/api/docs/rest-api/create-subaccount)| -| -| [Yes](/api/docs/futures-api/trading/subaccounts)| -| -  
**Charts**|  -| -| -| [Yes](/api/docs/futures-api/charts/analytics)| -| -  
  
## Futures and Spot Trading

Kraken currently has 2 distinct trading engines, for **spot** and **futures**. There are many similarities in the behaviours between the engines, however the spot and futures engines have important differences in terms of:

  * API protocols and endpoints.
  * Onboarding process and testing.
  * Authentication.
  * Rate limits.
  * Error messages.

## IP Whitelisting

API/programmatic traders can connect directly to Kraken AWS point of presence to improve latency and performance by whitelisting IPs. Detailed instructions on connecting to the UAT environment will be provided by Kraken’s support team.

## Colocation Access

We offer colocation services through our partnership with [Beeks Group](https://kraken.exchange-cloud.beeksgroup.com/), enabling you to host your trading infrastructure in close proximity to Kraken's API endpoints for enhanced performance and reduced latency.

> **Note:** Dedicated URLs are required to access colocation services.

### Endpoint URLs

  * **Spot WebSocket (WS):**
* `colo-london.vip-ws.kraken.com`
* `colo-london.vip-ws-auth.kraken.com`
  * **FIX API:**
* `colo-london.vip-fix.kraken.com`
  * **Futures REST API:**
* `colo-london.vip.futures.kraken.com`
  * **Futures WS API:**
* `wss://colo-london.vip.futures.kraken.com/ws/v1`

## FAQ and Support

Further information can be found on the [API section](https://support.kraken.com/hc/en-us/sections/4402371110548-API) of our support pages.

If you have problems making API requests, please [send us](https://support.kraken.com/hc/en-us/requests/new?ticket_form_id=360000104043) a full 
## Notices

Use of the Kraken APIs is subject to the [Kraken Terms & Conditions](https://www.kraken.com/legal) and [Privacy Notice](https://www.kraken.com/legal/privacy), as well as all other applicable terms and disclosures made available on [www.kraken.com](https://www.kraken.com/).

You must seek our prior permission for certain uses of the Kraken API’s. This includes, but is not limited to, any non-personal commercial use of data from publicly accessible endpoints, such as market data, exchange status, and any other data. You may seek such permission by contacting [marketdata@kraken.com](mailto:marketdata@kraken.com).

  * Introduction
* Direct Trading APIs
* Embed API (B2B / B2B2C)
* Choosing an API
* Summary of product versus exchange / API
  * Futures and Spot Trading
  * IP Whitelisting
  * Colocation Access
* Endpoint URLs
  * FAQ and Support
  * Notices