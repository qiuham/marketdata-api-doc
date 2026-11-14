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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/ping'
updated_at: 2026-11-13
---

# Ping

> Verify the WebSocket connection is alive with a ping/pong request

UWS
uws.kraken.com/v2/public
ping

Clients can ping the server to verify connection is alive and the server will respond with a `pong`.

This is an application level ping, distinct from the protocol-level ping in the WebSockets standard.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `ping`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string`
>
> Value: `pong`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **time\_in** `string`
>
> The timestamp when the request was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the response was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`

```json Request theme={null}
{
    "method": "ping",
    "req_id": 101
}
```

```json Response theme={null}
{
    "method": "pong",
    "req_id": 101,
    "time_in": "2023-09-24T14:10:23.799685Z",
    "time_out": "2023-09-24T14:10:23.799703Z"
}
```
