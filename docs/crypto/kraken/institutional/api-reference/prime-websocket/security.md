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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/security'
updated_at: 2026-11-13
---

# Security

> Public channel for streaming the list of available securities and real-time updates to their properties.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request for stream of available securities for trading. On initial request, a snapshot of all available securities is provided. All subsequent messages are deltas to the securities snapshot.

Kraken maintains a security master which contains up-to-date information about the securities supported over API that are available to trade.

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
> Array containing the Security stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Security`
>
> **Symbols** `array`
>
> Optional list of symbols to filter the subscription on.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 2,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Security"
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
> Array of Security data.
>
> **properties**
>
> **Timestamp** `string` *required*
>
> Timestamp of message publication in ISO-8601 UTC format.
>
> **UpdateAction** `string` *required*
>
> "Update" or "Remove" where the latter indicates the Security is no longer available.
>
> **SecurityID** `number` *required*
>
> System ID for Security - for information only.
>
> **Symbol** `string` *required*
>
> Symbol for security.
>
> **MinPriceIncrement** `string` *required*
>
> Minimum Price Increment for Security.
>
> **MinSizeIncrement** `string` *required*
>
> Minimum Size Increment for Security. This increment is used to validate orders and RFQS expressed in base currency of the security.
>
> **MinAmtIncrement** `string`
>
> Minimum Amount Increment for Security. This increment is used to validate orders and RFQS expressed in quote currency of the security.
>
> **MinimumSize** `string` *required*
>
> Minimum Size for an Order on this Security.
>
> **MaximumSize** `string`
>
> Maximum Size for an Order on this Security.
>
> **QuoteCurrency** `string` *required*
>
> Currency in which the Security is quoted.
>
> **BaseCurrency** `string` *required*
>
> Base currency for the Security.
>
> **EndTime** `string`
>
> Date this security was Disabled.
>
> **DefaultPriceIncrement** `string` *required*
>
> Default price increment used in all Market Data and Orders.
>
> **DefaultSizeIncrement** `string` *required*
>
> Default size increment used in all Market Data and Orders.
>
> **PriceDisplaySpec** `string` *required*
>
> String specification describing the price display.
>
> **SizeDisplaySpec** `string` *required*
>
> String specification describing the size display.
>
> **NormalSize** `string`
>
> Normal size of Security.
>
> **ProductType** `string`
>
> Product type of Security.
>
> **PositionCurrency** `string` *required*
>
> Currency in which any position on this Security is tracked.
>
> **SettlementCurrency** `string`
>
> Currency in which any settlement on this Security is negotiated.
>
> **NotionalMultiplier** `string`
>
> Notional Multiplier of Security.
>
> **Expiration** `string`
>
> Expiration of Security.
>
> **SizeBuckets** `array` *required*
>
> Default array of Size Buckets for Market Data Snapshot Streams.
>
> **DisplaySymbol** `string` *required*
>
> Display symbol for Security.
>
> **Description** `string` *required*
>
> Description of Security.
>
> **Rank** `number`
>
> Security rank.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 2,
>   "type": "Security",
>   "ts": "2021-09-14T22:11:47.512168Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Timestamp": "2021-09-14T22:11:47.512168Z",
>       "UpdateAction": "Update",
>       "SecurityID": 2,
>       "Symbol": "ETH-USD",
>       "MinPriceIncrement": "0.01",
>       "MinSizeIncrement": "0.00000001",
>       "MinAmtIncrement": "0.01",
>       "MinimumSize": "0.00000001",
>       "MaximumSize": "10000000",
>       "QuoteCurrency": "USD",
>       "BaseCurrency": "ETH",
>       "DefaultPriceIncrement": "0.01",
>       "DefaultSizeIncrement": "0.0001",
>       "PriceDisplaySpec": "M.m",
>       "SizeDisplaySpec": "M.m",
>       "NormalSize": "2",
>       "ProductType": "Spot",
>       "PositionCurrency": "ETH",
>       "SettlementCurrency": "USD",
>       "NotionalMultiplier": "1",
>       "SizeBuckets": [
>         {
>           "Size": "0"
>         }
>       ],
>       "DisplaySymbol": "ETH-USD",
>       "Description": "Ethereum/U.S. Dollar",
>       "Rank": 2
>     }
>   ]
> }
> ```
