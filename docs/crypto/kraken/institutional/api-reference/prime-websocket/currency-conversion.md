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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/currency-conversion'
updated_at: 2026-11-13
---

# Currency Conversion

> Public channel for streaming real-time currency conversion rates.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request for stream of currency conversion rates.

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
> Array containing the Currency Conversion stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `CurrencyConversion`
>
> **EquivalentCurrency** `string` *required*
>
> Quote currency to base the conversion rates on.
>
> **Currencies** `array`
>
> List of currencies and securities to generate conversion rates for; defaults to all available currencies.
>
> **Throttle** `string`
>
> Optional throttle interval for conversion rate updates. Minimal/default value: 10s.
>
> **Tolerance** `string`
>
> Optional param to indicate what conversion rate percent change should trigger sending out an update. Minimal/default value: 0.0001 which means 1 bps.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 4,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "CurrencyConversion",
>       "EquivalentCurrency": "USD",
>       "Currencies": ["BTC", "ETH", "BCH-USD"],
>       "Throttle": "15s",
>       "Tolerance": "0.0002"
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
> Array of CurrencyConversion data.
>
> **properties**
>
> **Timestamp** `string` *required*
>
> Timestamp of message publication.
>
> **EquivalentCurrency** `string` *required*
>
> Currency symbol for equivalent currency.
>
> **Currency** `string` *required*
>
> Currency symbol for base currency on conversion.
>
> **Rate** `string` *required*
>
> Currency conversion rate.
>
> **Status** `string` *required*
>
> Status of the conversion rate.
>
> **ConversionPath** `string` *required*
>
> Path used for the conversion.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 4,
>   "type": "CurrencyConversion",
>   "ts": "2021-09-14T22:16:18.604996Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Timestamp": "2021-09-14T22:16:18.604674Z",
>       "EquivalentCurrency": "USD",
>       "Currency": "ETH",
>       "Rate": "3368.16",
>       "Status": "Online",
>       "ConversionPath": "(ETH-USD)"
>     },
>     {
>       "Timestamp": "2021-09-14T22:16:18.604674Z",
>       "EquivalentCurrency": "USD",
>       "Currency": "BTC",
>       "Rate": "46841.35",
>       "Status": "Online",
>       "ConversionPath": "(BTC-USD)"
>     }
>   ]
> }
> ```
