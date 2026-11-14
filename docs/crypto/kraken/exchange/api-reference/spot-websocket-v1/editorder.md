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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/editorder'
updated_at: 2026-11-13
---

# Edit Order

> Edit the parameters of a live order by cancelling and recreating it

WSS
ws-auth.kraken.com
editOrder

Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be created with the adjusted parameters and a new `txid` will be returned in the response.

> [!WARNING]
>
> The newer [amendOrder](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/amendorder.md) endpoint resolves the caveats listed below and has additional performance gains.
>
> There are a number of caveats for `editOrder`:
>
> * `editOrder` cannot be used on partially filled orders.
> * `editOrder` is a cancel and replace, so queue priority is not maintained.
> * `editOrder` generates a new `txid` for the order.

> [tab] Request
>
> **event** `string` *required*
>
> Value: `editOrder`
>
> **orderid** `string`
>
> Original Order ID or userref.
>
> **pair** `string` *required*
>
> Currency pair.
>
> **price** `string`
>
> Dependent on order type - order price.
>
> **price2** `string`
>
> Dependent on order type - order secondary price.
>
> **volume** `string` *required*
>
> Order volume in base currency.
>
> **oflags** `string`
>
> Comma delimited list of order flags. `post` = post only order (available when ordertype = limit).
>
> **newuserref** `string`
>
> User reference ID for new order (should be an integer in quotes).
>
> **validate** `boolean`
>
> Validate inputs only; do not submit order.
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
> Value: `editOrderStatus`
>
> **txid** `string`
>
> A new Kraken order identifier for the amended order.
>
> **originaltxid** `string`
>
> The Kraken order identifier for the original order.
>
> **descr** `string`
>
> A descriptive summary for the amended order.
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
    "event": "editOrder",
    "newuserref": "666",
    "oflags": "",
    "orderid": "O26VH7-COEPR-YFYXLK",
    "pair": "XBT/USD",
    "price": "9000",
    "reqid": 3,
    "token": "0000000000000000000000000000000000000000"
}
```

```json Response theme={null}
{
    "descr": "order edited price = 9000.00000000",
    "event": "editOrderStatus",
    "originaltxid": "O65KZW-J4AW3-VFS74A",
    "reqid": 3,
    "status": "ok",
    "txid": "OTI672-HJFAO-XOIPPK"
}
```
