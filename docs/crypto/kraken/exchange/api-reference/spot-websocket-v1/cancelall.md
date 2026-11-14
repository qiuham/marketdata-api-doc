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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/cancelall'
updated_at: 2026-11-13
---

# Cancel All

> Cancel all open orders including partially-filled orders

WSS
ws-auth.kraken.com
cancelAll

Cancel all open orders. Includes partially-filled orders.

> [tab] Request
>
> **event** `string` *required*
>
> Value: `cancelAll`
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
> Value: `cancelAllStatus`
>
> **count** `string`
>
> Number of orders cancelled.
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
    "event": "cancelAll",
    "token": "0000000000000000000000000000000000000000"
}
```

```json Response theme={null}
{
    "count": 2,
    "event": "cancelAllStatus",
    "status": "ok"
}
```
