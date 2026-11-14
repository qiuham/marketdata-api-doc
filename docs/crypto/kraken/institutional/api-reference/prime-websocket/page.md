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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/page'
updated_at: 2026-11-13
---

# Continue Paged Stream

> Request the next page of data when a paged stream response includes a next field.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

If you request a stream that is paged, the data on the stream will be delivered with a `next` field populated. When this field is present, request the next set of data with the structure below. The response continues as with the original stream.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> The request ID to continue the page. Must match the original request ID from the [Subscribe](https://docs.kraken.com/institutional/api-reference/prime-websocket/subscribe.md) request.
>
> **type** `string` *required*
>
> Request type for continuing the paged stream. Value: `page`
>
> **streams** `array` *required*
>
> Streams to continue paging.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name to continue the page.
>
> **after** `string` *required*
>
> Delivered `next` value from the paged stream payload.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 3,
>   "type": "page",
>   "streams": [
>     {
>       "name": "Trade",
>       "after": "aGVsbG8="
>     }
>   ]
> }
> ```

## Response

The response structure remains the same as the original subscription, with additional data continuing from where the previous page ended.

> [tab] Response Schema
>
> Same structure as the original subscription response, with continuing data and potentially another `next` field if more pages are available.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 3,
>   "type": "Trade",
>   "data": [],
>   "page": true
> }
> ```
