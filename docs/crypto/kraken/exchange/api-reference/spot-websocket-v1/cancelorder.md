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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/cancelorder'
updated_at: 2026-11-13
---

# Cancel Order

> Cancel one or more open orders

WSS
ws-auth.kraken.com
cancelOrder

The `cancelOrder` request cancels one or more open orders in a single request. The orders to be cancelled can be identified by a range of client or Kraken identifiers.

> [tab] Request
>
> **event** `string` *required*
>
> Value: `cancelOrder`
>
> **txid** `array of string` *required*
>
> A list containing either client `order_userref` or Kraken `order_id` identifiers.
>
> **cl\_ord\_id** `array of string`
>
> A list of client `cl_ord_id` identifiers.
>
> **reqid** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **token** `string` *required*
>
> Session token from the [GetWebSocketsToken](https://docs.kraken.com/api-reference/trading/get-websockets-token.md) REST endpoint.

> [tab] Response
>
> **event** `string`
>
> Value: `cancelOrderStatus`
>
> **status** `string`
>
> One of: `ok`, `error`
>
> **reqid** `integer`
>
> Client originated identifier for the request that initiated this response.
>
> **errorMessage** `string`
>
> Error message for unsuccessful requests.

```json Request theme={null}
{
    "event": "cancelOrder",
    "token": "0000000000000000000000000000000000000000",
    "txid": [
        "OGTT3Y-C6I3P-XRI6HX",
        "OGTT3Y-C6I3P-X2I6HX"
    ]
}
```

```json Response theme={null}
{
    "event": "cancelOrderStatus",
    "status": "ok"
}
```

```json Error theme={null}
{
    "errorMessage": "EOrder:Unknown order",
    "event": "cancelOrderStatus",
    "status": "error"
}
```
