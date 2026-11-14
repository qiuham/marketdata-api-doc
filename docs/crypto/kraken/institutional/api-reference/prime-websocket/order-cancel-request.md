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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/order-cancel-request'
updated_at: 2026-11-13
---

# Order Cancel Request

> Authenticated command to cancel an open order.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to cancel an open order. Results of this command will be visible in the Order and ExecutionReport streams.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `OrderCancelRequest`
>
> **data** `array` *required*
>
> Cancel request data array.
>
> **properties**
>
> **Symbol** `string` *required*
>
> Symbol of the security to submit an order on.
>
> **ClOrdID** `string` *required*
>
> Unique Client Order ID for this request, usually a UUID.
>
> **OrigClOrdID** `string`
>
> Client Order ID of the order to cancel, one of OrderID, OrigClOrdID is required.
>
> **OrderID** `string`
>
> Order ID of the order to cancel, one of OrderID, OrigClOrdID is required.
>
> **TransactTime** `string` *required*
>
> An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **Timestamp** `string`
>
> Timestamp of the message.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 13,
>   "type": "OrderCancelRequest",
>   "data": [
>     {
>       "Symbol": "BTC-USD",
>       "ClOrdID": "c0be17e0-15da-11ec-b5e7-7f4881f01b7d",
>       "OrderID": "16a55364-4248-4575-aa0b-dddd3f694ca3",
>       "TransactTime": "2021-09-15T04:09:42.238000Z"
>     }
>   ]
> }
> ```
