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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/currency'
updated_at: 2026-11-13
---

# Currency

> Public channel for streaming available currencies used within trading.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request for stream of available currencies used within trading. On initial request, a snapshot of all available currencies is provided. All subsequent messages are deltas to the currency snapshot.

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
> Array containing the Currency stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Currency`
>
> **Symbols** `array`
>
> Optional list of currency symbols to filter the subscription on.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 3,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Currency"
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
> Array of Currency data.
>
> **properties**
>
> **Timestamp** `number` *required*
>
> Timestamp of message publication as nanoseconds since the Unix epoch.
>
> **UpdateAction** `string` *required*
>
> "Update" or "Remove" where the latter indicates the Currency is no longer available. Possible values: `Update`, `Remove`
>
> **CurrencyID** `number` *required*
>
> System ID for Currency - for information only.
>
> **Symbol** `string` *required*
>
> Symbol for currency.
>
> **MinIncrement** `string` *required*
>
> Minimum increment for Currency.
>
> **DefaultIncrement** `string` *required*
>
> Default increment used in all Market Data and Orders.
>
> **Description** `string` *required*
>
> Description of Currency.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 3,
>   "type": "Currency",
>   "ts": "2021-09-14T22:11:47.512168Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Timestamp": 1676936489075207000,
>       "UpdateAction": "Update",
>       "CurrencyID": 2,
>       "Symbol": "USD",
>       "MinIncrement": "0.01",
>       "DefaultIncrement": "0.01",
>       "Description": "U.S. Dollar"
>     },
>     {
>       "Timestamp": 1676936515053193000,
>       "UpdateAction": "Update",
>       "CurrencyID": 17,
>       "Symbol": "ETH",
>       "MinIncrement": "0.00000001",
>       "DefaultIncrement": "0.0001",
>       "Description": "Ethereum"
>     }
>   ]
> }
> ```
