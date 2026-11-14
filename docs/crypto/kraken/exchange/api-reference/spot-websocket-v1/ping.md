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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/ping'
updated_at: 2026-11-13
---

# Ping

> Client ping to determine whether the connection is alive

WSS
ws.kraken.com
ping

Client can ping server to determine whether the connection is alive. This is an application level ping as opposed to default ping in the WebSocket standard which is server initiated.

> [tab] Request
>
> **event** `string` *required*
>
> Value: `ping`
>
> **reqid** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **event** `string`
>
> Value: `pong`
>
> **reqid** `integer`
>
> Client originated identifier for the request that initiated this response.

```json Request theme={null}
{
  "event": "ping",
  "reqid": 42
}
```

```json Response theme={null}
{
  "event": "pong",
  "reqid": 42
}
```
