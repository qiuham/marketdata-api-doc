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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/challenge'
updated_at: 2026-11-13
---

# Challenge

> Request a challenge for user authentication handshake

WSS
futures.kraken.com/ws/v1
challenge

> [!WARNING]
>
> **Derivatives WebSocket is being deprecated.** For new integrations, use the
> [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket), which streams
> Spot and Derivatives over a single connection. Existing integrations continue
> to work until **1 March 2027**, when the Derivatives WebSocket will no
> longer be available. Migrate to the Unified WebSocket before then.
>
> To use private channels or trade on the Unified WebSocket, you need a
> Kraken API key, not a Derivatives API key. Use it to get a token from
> [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token). See
> [Unified WebSocket authentication](https://docs.kraken.com/exchange/api-reference/unified-websocket#authentication).

This request returns a challenge to be used in handshake for user authentication.

***

## Request

**event** `string` *required*

The request event type.

**api\_key** `string` *required*

The user API key.

```json Example theme={null}
{
  "event": "challenge",
  "api_key": "CMl2SeSn09Tz+2tWuzPfdaJdsahq6qv5UaexXuQ3SnahDQU/gO3aT+"
}
```

***

## Response Success

**event** `string`

Value: `challenge`

**message** `string`

The message that user will have to sign for authentication reasons.

```json Example theme={null}
{
  "event": "challenge",
  "message": "226aee50-88fc-4618-a42a-34f7709570b2"
}
```

***

## Response Error

**event** `string`

Value: `error`

**message** `string`

An error message. Value: `Json Error`

```json Example theme={null}
{
  "event": "error",
  "message": "Json Error"
}
```
