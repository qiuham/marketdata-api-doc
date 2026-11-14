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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/mdr'
updated_at: 2026-11-13
---

# Market Data Request

> FIX message to request market data for a specific symbol.

Request market data for a specific symbol. Note that exactly one of either Depth, or SizeBucket must be specified. For example, specifying both Depth and SizeBuckets will result in an error.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `V`
>
> **262 - MDReqID** `string` *required*
>
> Must be unique, or the ID of previous Market Data Request to disable if SubscriptionRequestType(263) = 2 (Disable previous Snapshot + Updates Request).
>
> **263 - SubscriptionRequestType** `integer` *required*
>
> Subscription type for market data.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : Snapshot</li>
>   <li>`1` : Snapshot + Updates (Subscribe)</li>
>   <li>`2` : Unsubscribe</li>
> </ul>
>
> **264 - MarketDepth** `integer`
>
> Depth of market for Book Snapshot / Incremental updates. Exactly one of tag 264 or tag 20020 must be specified.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : Full book depth</li>
>   <li>`1` : Top of book</li>
>   <li>`2 and above` : Book depth (number of levels)</li>
> </ul>
>
> **1070 - MDQuoteType** `integer`
>
> Type of liquidity to be included.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : Indicative</li>
>   <li>`1` : Tradeable (i.e., Firm)</li>
> </ul>
>
> **20020 - NoSizeBucketsSegments** `integer`
>
> A list of sizes to return price levels for. Used to ask for prices of aggregated sizes. Exactly one of tag 264 or tag 20020 must be specified. Only supported with MDUpdateType(265) = 0 (Full refresh).
>
> **20021 - SizeBucket** `float`
>
> Identifies a single size bucket. Required if NoSizeBucketsSegments is used.
>
> **55 - Symbol** `string` *required*
>
> The symbol of the currency pair to subscribe to. For example, BTC-USD.
>
> **trailer** *required*

> [tab] Example
>
> ```text theme={null}
> 8=FIX.4.4|9=186|35=V|34=2|49=CUSTOMER_MD|52=20220930-13:28:06.146|56={{ Customer }}|262=id-220929160342682-26|263=1|264=0|265=0|1070=1|146=1|55=ETH-USD|267=2|269=0|269=1|20020=4|20021=1|20021=2|20021=5|20021=10|10=226|
> ```
