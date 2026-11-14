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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/amend_order'
updated_at: 2026-11-13
---

# Amend Order

> Amend the parameters of a live order in-place

UWS
uws.kraken.com/v2/private
amend\_order

The amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one. Amend is supported for both spot and futures (derivatives) orders.

* The order identifiers assigned by Kraken and/or client will stay the same.
* Queue priority in the order book will be maintained where possible.
* If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see [amend transaction guide](https://docs.kraken.com/exchange/guides/general/amends.md).

> [tab] Request
>
> **method** `string` *required*
>
> Value: `amend_order`
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
> **order\_id** `string` *required*
>
> Example: `cff769bb-dc52-56e1-98c8-22301dc888ae`
>
> The Kraken identifier for the order to be amended. Either `order_id` or `cl_ord_id` is required.
>
> **cl\_ord\_id** `string`
>
> Example: `6d1b345e-2821-40e2-ad83-4ecb18a06876`
>
> The client identifier for the order to be amended. Either `order_id` or `cl_ord_id` is required.
>
> **order\_qty** `float`
>
> The new order quantity in terms of the base asset.
>
> **display\_qty** `float`
>
> Condition: Not available for derivatives
>
> Defines the new quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of remaining order quantity.
>
> **limit\_price** `float`
>
> Condition: For order types that support limit price only
>
> The new limit price restriction on the order, used in combination with the `limit_price_type` parameter.
>
> **limit\_price\_type** `string`
>
> One of: `static`\\
>
> Condition: Currently only available on trailing-stop-limit orders
>
> The units for `limit_price`. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. limit price at 29000.5 BTC/USD, use price=29000.5 and price\_type=static.
>
> **post\_only** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`\\
>
> Condition: Optional parameter for limit price amends
>
> If `true`, the limit price change will be rejected if the order cannot be posted passively in the book.
>
> **trigger\_price** `float`
>
> Condition: For triggered order types only
>
> The new trigger price to activate the order, used in combination with the `trigger_price_type` parameter.
>
> **trigger\_price\_type** `string`
>
> One of: `static`\\
>
> Default: `static`\\
>
> Condition: For triggered order types only
>
> The units for `trigger_price`. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. to trigger at 29000.5 BTC/USD, use price=29000.5 and price\_type=static.
>
> **deadline** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123Z`
>
> Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
>
> **symbol** `string`
>
> Example: `TSLAx/USD`
>
> The `symbol` is required on amends for non-crypto pairs, i.e. provide the pair symbol for xStocks.
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
> For spot orders, a successful amend request returns the unique Kraken amend identifier. Futures (derivatives) has no amend identifier, so `amend_id` is empty on derivatives amends.
>
> **method** `string`
>
> Value: `amend_order`
>
> **result** `object`
>
> Condition: if `success` is `true`
>
> **properties**
>
> **amend\_id** `string`
>
> Condition: Spot only
>
> The unique Kraken identifier generated for this amend transaction. Futures has no concept of an amend identifier, so this is always empty (`""`) for `derivatives`.
>
> **order\_id** `string`
>
> The Kraken identifier, if populated in the request.
>
> **cl\_ord\_id** `string`
>
> The client identifier, if populated in the request.
>
> **warnings** `array of string`
>
> Non-fatal warnings about the amend, if any.
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

```json Basic theme={null}
{
  "method": "amend_order",
  "params": {
      "asset_class": "derivatives",
      "cl_ord_id": "2c6be801-1f53-4f79-a0bb-4ea1c95dfae9",
      "limit_price": 490795,
      "order_qty": 1.2,
      "token": "PM5Qm0MDrS54l657aQAtb7AhrwN30e2LBg1nUYOd6vU"
  }
}
```

```json Advanced theme={null}
{
    "method": "amend_order",
    "params": {
        "asset_class": "derivatives",
        "order_id": "e66851e7-8721-50ed-bf43-5e6a2ddff423",
        "limit_price": 61031.3,
        "deadline": "2024-07-21T09:53:59.050Z",
        "post_only": true,
        "token": "DGB00LiKlPlLI/amQaSKUUr8niqXDb+1zwvtjp34nzk"
    }
}
```

```json Response theme={null}
{
    "method": "amend_order",
    "result": {
        "amend_id": "",
        "cl_ord_id": "2c6be801-1f53-4f79-a0bb-4ea1c95dfae9"
    },
    "success": true,
    "time_in": "2024-07-26T13:39:04.922699Z",
    "time_out": "2024-07-26T13:39:04.924912Z"
}
```
