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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/quote-cancel-request'
updated_at: 2026-11-13
---

# Quote Cancel Request

> Authenticated command to cancel an open RFQ.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to cancel an open RFQ. Results of this command will be visible in the Quote stream.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `QuoteCancelRequest`
>
> **data** `array` *required*
>
> Quote cancel request data array.
>
> **properties**
>
> **QuoteReqID** `string` *required*
>
> QuoteReqID from the request to cancel.
>
> **RFQID** `string` *required*
>
> RFQID to cancel, required and must align with QuoteReqID.
>
> **TransactTime** `string` *required*
>
> An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 16,
>   "type": "QuoteCancelRequest",
>   "data": [
>     {
>       "QuoteReqID": "8e9540d0-15db-11ec-b5e7-7f4881f01b7d",
>       "RFQID": "f47bfb99-4d1e-4179-b62c-a96e83cc93ba",
>       "TransactTime": "2021-09-15T04:15:24.581000Z"
>     }
>   ]
> }
> ```
