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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/batch_cancel'
updated_at: 2026-11-13
---

# Batch Cancel

> Cancel multiple orders in a single request

UWS
uws.kraken.com/v2/private
batch\_cancel

The `batch_cancel` request enables multiple orders to be cancelled in a single request by a range of identifiers (minimum of 2 and maximum 50 in each batch).

> [tab] Request
>
> **method** `string` *required*
>
> Value: `batch_cancel`
>
> **params** `object`
>
> **properties**
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **orders** `string[]`
>
> A list of Kraken `order_id` identifiers. Derivatives order IDs must be UUIDs. `order_userref` is not supported.
>
> **cl\_ord\_id** `string[]`
>
> A list of client `cl_ord_id` identifiers. May be combined with `orders`; supply 2 to 50 identifiers in total.
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
> Value: `batch_cancel`
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
    "method": "batch_cancel",
    "params": {
        "asset_class": "derivatives",
        "orders": [
            "11111111-1111-4111-8111-111111111111",
            "22222222-2222-4222-8222-222222222222",
            "33333333-3333-4333-8333-333333333333"
        ],
        "token": "TxxxxxxxxxOxxxxxxxxxxKxxxxxxxExxxxxxxxN"
    },
    "req_id": 1234567890
}
```

```json Response theme={null}
{
    "method": "batch_cancel",
    "req_id": 1234567890,
    "result": {
        "count": 3
    },
    "success": true,
    "time_in": "2022-06-13T08:09:10.123456Z",
    "time_out": "2022-06-13T08:09:10.7890123Z"
}
```
