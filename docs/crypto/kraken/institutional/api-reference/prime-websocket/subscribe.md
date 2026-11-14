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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/subscribe'
updated_at: 2026-11-13
---

# Subscribe

> Send a subscription request to begin a stream of data from the Prime WebSocket API.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Send a subscription request to begin a stream of data. An example request that subscribes to data.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID - will be echoed back in the response structure.
>
> **type** `string` *required*
>
> Request type for initializing a subscription. Value: `subscribe`
>
> **tag** `string`
>
> Optional user generated tag to attach to stream data.
>
> **streams** `array` *required*
>
> Streams to subscribe to.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name (e.g., "Security", "MarketDataSnapshot", "ExecutionReport").
>
> **...** `various`
>
> Any required or optional parameters described for the subscription names.
>
> **ts** `string`
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 1,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "MarketDataSnapshot",
>       "Symbol": "BTC-USD"
>     }
>   ],
>   "ts": "2019-02-13T05:17:32.000000Z"
> }
> ```

## Response

> [tab] Response Schema
>
> **reqid** `number` *required*
>
> A number that relates this response to a request.
>
> **seqNum** `number` *required*
>
> The sequence number for this response per request. seqNum begins at 1 on the first message with this reqid and increments by one for each message sent on this reqid.
>
> **type** `string` *required*
>
> The type of message sent. This document describes all valid message types.
>
> **tag** `string`
>
> An optional tag from the stream request.
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **initial** `boolean`
>
> If this is initial data for a request, the initial flag will be set.
>
> **action** `string`
>
> "Update" or "Remove" - tells the client if the given entity should be removed or added/updated.
>
> **total\_count** `number`
>
> The total number of records for this stream.
>
> **data** `array` *required*
>
> Array of response data structured per subscription type.
>
> **next** `string`
>
> If paging, tag for next page of data.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 1,
>   "type": "MarketDataSnapshot",
>   "ts": "2026-06-17T11:27:06.865086Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Timestamp": "2026-06-17T11:27:06.863369Z",
>       "Symbol": "BTC-USD",
>       "Status": "Online",
>       "Bids": [
>         {
>           "Price": "64647.0",
>           "Size": "0.50000000"
>         },
>         {
>           "Price": "64647.0",
>           "Size": "2.50000000"
>         }
>       ],
>       "Offers": [
>         {
>           "Price": "64648.0",
>           "Size": "0.50000000"
>         },
>         {
>           "Price": "64648.0",
>           "Size": "2.50000000"
>         }
>       ]
>     }
>   ]
> }
> ```

## Notes

* `reqid` cannot be equal to 0.
* `seqNum` is for debug purposes only, the client is not required to do any sequencing.
* If a request requires responses with different types, then multiple responses may have the `initial` flag set for different types.
* `action` is either `Update` or `Remove` and tells the client if the given entity should be removed or added/updated. The key for a given entity depends on the message type.
