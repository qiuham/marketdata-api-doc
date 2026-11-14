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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/hello'
updated_at: 2026-11-13
---

# Hello

> Server-sent hello message on a successful WebSocket connection.

> [!NOTE]
>
> Connect to: `wss://wss.prime.kraken.com/ws/v1`

The server sends a `hello` message on a successful connection. After a client connects, the server will send an unsolicited `hello` message.

## Response

> [tab] Response Schema
>
> **type** `string` *required*
>
> Message type. Value: `hello`
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **session\_id** `string` *required*
>
> A session ID that uniquely identifies this websocket session.

> [tab] Example
>
> ```json theme={null}
> {
>   "type": "hello",
>   "ts": "2019-02-13T05:17:32.000000Z",
>   "session_id": "1SJGEGSYMZ800"
> }
> ```
