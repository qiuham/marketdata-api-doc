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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/order-cancel-replace-request'
updated_at: 2026-11-13
---

# Order Cancel Replace Request

> Authenticated command to modify an open order's price, quantity, or strategy.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to modify an open order. Results of this command will be visible in the Order and ExecutionReport streams.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `OrderCancelReplaceRequest`
>
> **data** `array` *required*
>
> Replace request data array.
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
> **OrderQty** `string` *required*
>
> Order quantity in units of Currency.
>
> **Price** `string`
>
> Order limit price, required for Limit orders.
>
> **TransactTime** `string` *required*
>
> An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **Strategy** `string`
>
> Optional order strategy to use. For algorithmic orders Pegged, TWAP, FullAmount, TimeSliced, and SteadyPace are supported.
>
> **EndTime** `string`
>
> Optional expire time for the order. An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **Parameters** `object`
>
> Optional order strategy parameters.
>
> **Timestamp** `string`
>
> Timestamp of the message.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 14,
>   "type": "OrderCancelReplaceRequest",
>   "data": [
>     {
>       "Price": "44000",
>       "Symbol": "BTC-USD",
>       "OrderID": "16a55364-4248-4575-aa0b-dddd3f694ca3",
>       "ClOrdID": "b5e52570-15da-11ec-b5e7-7f4881f01b7d",
>       "TransactTime": "2021-09-15T04:09:24.039000Z",
>       "OrderQty": "0.5",
>       "Parameters": {
>         "ErrorAction": "Pause"
>       }
>     }
>   ]
> }
> ```
