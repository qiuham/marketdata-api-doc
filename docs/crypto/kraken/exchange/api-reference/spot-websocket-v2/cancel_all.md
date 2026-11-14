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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/cancel_all'
updated_at: 2026-11-13
---

# Cancel All

> Cancel all open orders

WSS
ws-auth.kraken.com/v2
cancel\_all

Cancels all open orders, including untriggered orders and orders resting in the book.

Note, the details of the individual cancelled orders will also be streamed on the `executions` channel.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `cancel_all`
>
> **params** `object`
>
> **properties**
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string`
>
> Value: `cancel_all`
>
> **result** `object`
>
> Condition: if `success` is `true`
>
> **properties**
>
> **count** `integer`
>
> Number of orders cancelled.
>
> **warnings** `array of string`
>
> Non-fatal warnings, if any.
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
    "method": "cancel_all",
    "params": {
        "token": "weeBxllys/7kHy/zHpkATSDIS42BvDgWS2b04ZSZHZ5"
    },
    "req_id": 1234567890
}
```

```json Response theme={null}
{
    "method": "cancel_all",
    "req_id": 1234567890,
    "result": {
        "count": 1
    },
    "success": true,
    "time_in": "2023-09-26T13:09:48.463201Z",
    "time_out": "2023-09-26T13:09:48.471419Z"
}
```
