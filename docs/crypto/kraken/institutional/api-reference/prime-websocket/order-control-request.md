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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/order-control-request'
updated_at: 2026-11-13
---

# Order Control Request

> Authenticated command to pause or resume an open order.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to Pause or Resume an open order. Results of this command will be visible in the Order and ExecutionReport streams.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `OrderControlRequest`
>
> **data** `array` *required*
>
> Control request data array.
>
> **properties**
>
> **ClOrdID** `string` *required*
>
> Unique Client Order ID for this request, usually a UUID.
>
> **OrigClOrdID** `string`
>
> Client Order ID of the order to submit the control request for, one of OrderID, OrigClOrdID is required.
>
> **OrderID** `string`
>
> Order ID of the order to submit the control request for, one of OrderID, OrigClOrdID is required.
>
> **TransactTime** `string` *required*
>
> An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **Action** `string` *required*
>
> Action to apply on the order. Possible values: `Pause`, `Resume`
>
> **Timestamp** `string`
>
> Timestamp of the message.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 17,
>   "type": "OrderControlRequest",
>   "data": [
>     {
>       "ClOrdID": "9eb07120-15da-11ec-b5e7-7f4881f01b7d",
>       "OrderID": "16a55364-4248-4575-aa0b-dddd3f694ca3",
>       "TransactTime": "2021-09-15T04:10:00.000000Z",
>       "Action": "Pause"
>     }
>   ]
> }
> ```
