---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/perps/overview'
updated_at: 2026-11-13
---

# Overview

> Explore the APIs available for building with Polymarket Perps.

## APIs

The Perps API is available over HTTP and WebSocket, with public market data and
authenticated trading and account operations on both.

> [card] HTTP API
>
> `https://api.perpetuals.polymarket.com`
>
> Make request-response calls for market data, trading, and account
> management.

> [card] WebSocket API
>
> `wss://ws.perpetuals.polymarket.com/v1/ws`
>
> Stream public and private updates, or send trading actions over a persistent
> connection.

## Before You Integrate

> [card] [Authentication](https://docs.polymarket.com/perps/authenticated-sessions.md)
>
> Set up credentials for private HTTP and WebSocket access.

> [card] [Rate Limits](https://docs.polymarket.com/api-reference/perps/rate-limits.md)
>
> Review request, trading action, and WebSocket limits.

> [card] [Geographic Restrictions](https://docs.polymarket.com/api-reference/perps/geographic-restrictions.md)
>
> Check where Perps order placement is available.

## Correlate Requests with Exchange Logs

Every HTTP response the exchange produces — including errors and overload
responses — carries an `x-pmp-pod` header identifying the gateway pod that
produced it. WebSocket handshake responses carry the same header, on both the
successful `101` upgrade and handshake rejections. Record it with your request
logs so your traffic can be matched against exchange logs when you work with
support.

The value is the gateway pod name, or a hexadecimal process instance ID when
the pod name is unavailable. It is correlation metadata only: pods are not
addressable, and a cached response keeps the identity of the pod that
originally produced it. Responses to malformed HTTP carry no header. Browsers
can read the header through CORS, but browser WebSocket APIs do not expose
handshake headers — authenticated WebSocket sessions instead receive the pod
identity in the successful auth acknowledgement, described in
[Authenticated Sessions](https://docs.polymarket.com/perps/authenticated-sessions.md). Treat the header and
the field as optional: responses from older pods omit them during a rolling
deploy.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
