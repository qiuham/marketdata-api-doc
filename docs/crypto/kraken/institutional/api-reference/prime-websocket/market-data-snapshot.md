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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/market-data-snapshot'
updated_at: 2026-11-13
---

# Market Data Snapshot

> Public channel for streaming real-time bid/offer levels for a security.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request stream of MarketDataSnapshot messages. To stream security pricing with real-time bid/offer levels.

## Subscribe Request

> [tab] Subscribe Schema
>
> **reqid** `number` *required*
>
> Request ID - will be echoed back in the response structure.
>
> **type** `string` *required*
>
> Request type. Value: `subscribe`
>
> **streams** `array` *required*
>
> Array containing the MarketDataSnapshot stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `MarketDataSnapshot`
>
> **Symbol** `string` *required*
>
> Security to request (e.g. `BTC-USD`).
>
> **Throttle** `string`
>
> Optional throttle duration for updates, defaults to configured MinMarketDataThrottle. Valid time units are "ns", "us", "ms", "s".
>
> **PriceIncrement** `string`
>
> Price increment for levels to enable price bucketing.
>
> **Depth** `number`
>
> Maximum number of bid/offer levels to stream prices for.
>
> **SizeBuckets** `array`
>
> A list of sizes to return price levels for; defaults to configured Security SizeBuckets.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 5,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "MarketDataSnapshot",
>       "Symbol": "BTC-USD"
>     }
>   ]
> }
> ```

## Response

> [tab] Response Schema
>
> **reqid** `number` *required*
>
> A number that relates this response to a request.
>
> **type** `string` *required*
>
> The type of message sent.
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **initial** `boolean`
>
> If this is initial data for a request, the initial flag will be set.
>
> **seqNum** `number` *required*
>
> The sequence number for this response per request.
>
> **action** `string`
>
> "Update" or "Remove" - tells the client if the given entity should be removed or added/updated.
>
> **data** `array` *required*
>
> Array of MarketDataSnapshot data.
>
> **properties**
>
> **Timestamp** `string` *required*
>
> Timestamp of update in ISO-8601 UTC format.
>
> **Symbol** `string` *required*
>
> Security for update.
>
> **Status** `string` *required*
>
> Status of update. Possible values: `Online`, `Offline`
>
> **Bids** `array` *required*
>
> Full list of Bids.
>
> **properties**
>
> **Price** `string` *required*
>
> Limit price of the level.
>
> **Size** `string` *required*
>
> Size on this level.
>
> **Offers** `array` *required*
>
> Full list of Offers.
>
> **properties**
>
> **Price** `string` *required*
>
> Limit price of the level.
>
> **Size** `string` *required*
>
> Size on this level.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 5,
>   "type": "MarketDataSnapshot",
>   "ts": "2026-06-17T11:47:35.341672Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Timestamp": "2026-06-17T11:47:35.340139Z",
>       "Symbol": "BTC-USD",
>       "Status": "Online",
>       "Bids": [
>         {
>           "Price": "64805.0",
>           "Size": "0.50000000"
>         },
>         {
>           "Price": "64805.0",
>           "Size": "2.50000000"
>         }
>       ],
>       "Offers": [
>         {
>           "Price": "64807.9",
>           "Size": "0.50000000"
>         },
>         {
>           "Price": "64807.9",
>           "Size": "2.50000000"
>         }
>       ]
>     }
>   ]
> }
> ```
