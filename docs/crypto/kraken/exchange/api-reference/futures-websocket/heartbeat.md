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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/heartbeat'
updated_at: 2026-11-13
---

# Heartbeat

> Subscribe to heartbeat messages at timed intervals

WSS
futures.kraken.com/ws/v1
heartbeat

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

The `heartbeat` feed publishes a heartbeat message at timed intervals.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `heartbeat`

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "heartbeat"
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `heartbeat`

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "heartbeat"
}
```

***

## Response Snapshot

**feed** `string`

The subscribed feed.

**time** `positive integer`

The UTC time of the server in milliseconds.

```json Example theme={null}
{
  "feed": "heartbeat",
  "time": 1534262350627
}
```

***

## Response Error

**event** `string`

Value: `error`

**message** `string`

One of: `Invalid feed`, `Json Error`

An error message.

```json Example theme={null}
{
  "event": "error",
  "message": "Json Error"
}
```
