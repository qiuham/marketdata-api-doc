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
source_url: 'https://docs.kraken.com/exchange/guides/futures/websockets'
updated_at: 2026-11-13
---

# Derivatives WebSocket

> Authentication, subscriptions, and real-time feeds for the Kraken Derivatives WebSocket API

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

## Deprecation and Unified WebSocket

The Derivatives WebSocket (`wss://futures.kraken.com/ws/v1`) is being
deprecated. Existing integrations
continue to work until **1 March 2027**, when the Derivatives
WebSocket will no longer be available. Migrate to the Unified WebSocket
before then.

If you are starting a new integration, use the
[Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket). It
covers Spot and Derivatives over a single connection. You choose the
market by setting `asset_class` to `derivatives` on each subscription
or order message.

| | Derivatives WebSocket | Unified WebSocket |
| :- | :- | :- |
| Markets | Derivatives only | Spot and Derivatives |
| Endpoint | `wss://futures.kraken.com/ws/v1` | `wss://uws.kraken.com/v2/public`, `wss://uws.kraken.com/v2/private` |
| Order entry | Not supported (streaming only) | `add_order`, `amend_order`, `cancel_order`, `cancel_all`, `cancel_after` |
| Authentication | Signed challenge per private subscription | WebSocket token from [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token) |
| Message format | v1 (`event` / `feed`) | v2 (`method` / `channel`) |

### Connect to the Unified WebSocket

Public channels, such as `ticker` and `book`, need no authentication.
Connect to `wss://uws.kraken.com/v2/public` and subscribe.

Private channels and trading use a WebSocket token instead of the
signed challenge:

1. Create a Kraken API key at
   [Settings → API](https://www.kraken.com/u/security/api), with the
   **Access WebSocket API** permission and the permissions your
   integration needs. Derivatives API keys do not work with the Unified
   WebSocket. See [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md).
2. Call the Spot REST endpoint
   [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token)
   with that key. Tokens are short-lived, so get a fresh one for each
   connection.
3. Connect to `wss://uws.kraken.com/v2/private` and send the token in
   `params.token` on each private subscription and trading request.

See [WebSocket authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md)
for code examples of the token request.

Example of subscribing to a Derivatives ticker on the Unified WebSocket:

```json theme={null}
{
  "method": "subscribe",
  "params": {
    "channel": "ticker",
    "asset_class": "derivatives",
    "symbol": ["PF_XBTUSD"]
  }
}
```

The rest of this page describes the Derivatives WebSocket.

## Endpoint

```text theme={null}
wss://futures.kraken.com/ws/v1
```

## Keeping the connection alive

Send a ping request at least every 60 seconds to keep the connection open. See the [sample implementation](https://github.com/CryptoFacilities/WebSocket-v1-Python/blob/master/cfWebSocketApiV1.py#L138) for reference.

## Snapshots and updates

Most feeds send a snapshot of the current state first, followed by real-time incremental updates.

## Authentication

Private feeds require a signed challenge. The process:

1. Connect to the WebSocket endpoint.
2. Send a request to obtain a challenge (using your `api_key`).
3. Sign the challenge with your `api_secret` (see [Sign challenge](#sign-challenge) below).
4. Include both `original_challenge` and `signed_challenge` in every subscribe/unsubscribe message for private feeds.

## Sign challenge

### Signing steps

Given a `challenge` string:

1. Hash the challenge with [SHA-256](https://en.wikipedia.org/wiki/SHA-2)
2. [Base64-decode](https://en.wikipedia.org/wiki/Base64) your `api_secret`
3. Hash the result of step 1 with the result of step 2 using [HMAC-SHA-512](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
4. [Base64-encode](https://en.wikipedia.org/wiki/Base64) the result of step 3

The result of step 4 is the `signed_challenge`.

### Example

| Field | Value |
| :- | :- |
| `challenge` | `c100b894-1729-464d-ace1-52dbce11db42` |
| `api_secret` | `7zxMEF5p/Z8l2p2U7Ghv6x14Af+Fx+92tPgUdVQ748FOIrEoT9bgT+bTRfXc5pz8na+hL/QdrCVG7bh9KpT0eMTm` |
| `signed_challenge` | `4JEpF3ix66GA2B+ooK128Ift4XQVtc137N9yeg4Kqsn9PI0Kpzbysl9M1IeCEdjg0zl00wkVqcsnG4bmnlMb3A==` |

The challenge is a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) string.

## Subscribe request

```json theme={null}
{
  "event": "subscribe",
  "feed": "ticker",
  "product_ids": [
    "PI_XBTUSD",
    "FI_ETHUSD_210625"
  ]
}
```

For private feeds, include the challenge fields:

```json theme={null}
{
  "event": "subscribe",
  "feed": "open_orders",
  "api_key": "<your_api_key>",
  "original_challenge": "<challenge>",
  "signed_challenge": "<signed_challenge>"
}
```
