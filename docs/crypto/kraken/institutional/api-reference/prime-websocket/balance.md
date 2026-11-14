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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/balance'
updated_at: 2026-11-13
---

# Balance

> Authenticated channel for streaming real-time account balance updates.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request for stream of Balance updates. Provides real-time account balance information.

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
> Array containing the Balance stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Balance`
>
> **Currencies** `array`
>
> Optional list of currencies to filter these balance updates by, default is all available currencies.
>
> **EquivalentCurrency** `string`
>
> If provided, will provide converted equivalent amounts of each currency in the provided Equivalent Currency.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 11,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Balance",
>       "EquivalentCurrency": "USD"
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
> Array of Balance data.
>
> **properties**
>
> **Currency** `string` *required*
>
> Currency of this balance update.
>
> **Amount** `string` *required*
>
> Current balance amount in the specified currency.
>
> **AvailableAmount** `string` *required*
>
> Amount available for trading right now.
>
> **Equivalent** `object`
>
> If requested equivalent balance amount, will provide a Balance update in the specified equivalent currency.
>
> **properties**
>
> **Currency** `string`
>
> Requested Equivalent Currency.
>
> **Amount** `string`
>
> Amount of this balance in the equivalent currency.
>
> **AvailableAmount** `string`
>
> Equivalent amount of amount available for trading right now.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 11,
>   "type": "Balance",
>   "ts": "2021-09-16T16:17:06.892914Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Currency": "USD",
>       "Amount": "-1928479.77953598",
>       "AvailableAmount": "-1928479.77953598",
>       "Equivalent": {
>         "Currency": "USD",
>         "Amount": "-1928479.78",
>         "AvailableAmount": "-1928479.78"
>       }
>     },
>     {
>       "Currency": "BTC",
>       "Amount": "40.15480673",
>       "AvailableAmount": "40.15480673",
>       "Equivalent": {
>         "Currency": "USD",
>         "Amount": "1930241.56",
>         "AvailableAmount": "1930241.56"
>       }
>     }
>   ]
> }
> ```
