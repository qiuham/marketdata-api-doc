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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/quote-request'
updated_at: 2026-11-13
---

# Quote Request

> Authenticated command to open a new RFQ and request a streaming quote.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to request a quote thereby opening a new RFQ. Results of this command will be visible in the Quote stream.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `QuoteRequest`
>
> **data** `array` *required*
>
> Quote request data array.
>
> **properties**
>
> **Symbol** `string` *required*
>
> Symbol of the security to submit an order on.
>
> **Currency** `string` *required*
>
> The currency that the quantity is specified in.
>
> **QuoteReqID** `string` *required*
>
> Unique ID for this request, usually a UUID.
>
> **Side** `string`
>
> Optional side for a one sided request. Possible values: `Buy`, `Sell`. Leave blank for a two way quote.
>
> **OrderQty** `string` *required*
>
> Requested quantity in units of Currency.
>
> **TransactTime** `string`
>
> An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **Timestamp** `string`
>
> Timestamp of the message.
>
> **Parameters** `object`
>
> Optional parameters for the quote request.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 15,
>   "type": "QuoteRequest",
>   "data": [
>     {
>       "QuoteReqID": "8e9540d0-15db-11ec-b5e7-7f4881f01b7d",
>       "OrderQty": "0.75",
>       "Currency": "BTC",
>       "Symbol": "BTC-USD",
>       "TransactTime": "2021-09-15T04:15:27.581000Z",
>       "Parameters": {}
>     }
>   ]
> }
> ```

## Notes

To generate a `QuoteReqID`, we recommend using a UUID4 or another globally unique identifier. `QuoteReqID` must be unique and with length less than or equal to 36 characters.

Quote responses are delivered on the [Quote](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote.md) stream. To accept a quote, see [New Order Single](https://docs.kraken.com/institutional/api-reference/prime-websocket/new-order-single.md) (`OrdType=RFQ`).
