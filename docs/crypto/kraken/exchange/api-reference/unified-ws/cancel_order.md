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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/cancel_order'
updated_at: 2026-11-13
---

# Cancel Order

> Cancel one or more open orders via WebSocket

UWS
uws.kraken.com/v2/private
cancel\_order

The `cancel_order` request cancels one or more open orders in a single request. The orders to be cancelled can be identified by a range of client or Kraken identifiers. Note, the details of the individual cancelled orders will also be streamed on the `executions` channel.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `cancel_order`
>
> **params** `object` *required*
>
> **properties**
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **order\_id** `array of string`
>
> A list of Kraken `order_id` identifiers. Derivatives order IDs must be UUIDs. Cannot be combined with `cl_ord_id` or `order_userref` in the same request.
>
> **cl\_ord\_id** `array of string`
>
> A list of client `cl_ord_id` identifiers. Cannot be combined with `order_id` or `order_userref` in the same request.
>
> **order\_userref** `array of integer`
>
> Condition: Not available for derivatives (use `cl_ord_id` instead)
>
> A list of client `order_userref` identifiers. Cannot be combined with `order_id` or `cl_ord_id` in the same request.
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
> When cancelling multiple orders, there will be a stream of individual order responses.
>
> **method** `string`
>
> Value: `cancel_order`
>
> **result** `object`
>
> **properties**
>
> **order\_id** `string`
>
> Kraken identifier of the cancelled order.
>
> **cl\_ord\_id** `string`
>
> Optional client identifier of the cancelled order.
>
> **warnings** `array of string`
>
> Non-fatal warnings about the cancellation, if any.
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
    "method": "cancel_order",
    "params": {
        "asset_class": "derivatives",
        "order_id": [
            "eed6e140-fbb2-5c60-8041-ef395844b692",
            "549d5d1f-5702-5589-bf57-0ad3ed3a0842"
        ],
        "token": "zGXT1dUQQjJjy5VmGXMegdDQngXXehNo5qbMBVolwEQ"
    },
    "req_id": 123456789
}
```

```json Response theme={null}
{
    "method": "cancel_order",
    "req_id": 123456789,
    "result": {
        "order_id": "549d5d1f-5702-5589-bf57-0ad3ed3a0842"
    },
    "success": true,
    "time_in": "2023-09-21T14:36:57.428972Z",
    "time_out": "2023-09-21T14:36:57.437952Z"
}
```
