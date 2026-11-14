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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/exposure'
updated_at: 2026-11-13
---

# Exposure

> Authenticated channel for streaming real-time credit utilization and exposure limit information.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request for stream of Exposure updates. Provides real-time credit utilization and exposure limit information.

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
> Array containing the Exposure stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Exposure`

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 11,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Exposure"
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
> Array of Exposure data.
>
> **properties**
>
> **ExposureCurrency** `string` *required*
>
> The currency all exposure values are expressed in.
>
> **Exposure** `string` *required*
>
> Current credit utilization expressed in the ExposureCurrency.
>
> **ExposureLimit** `string` *required*
>
> Credit limit expressed in the ExposureCurrency.
>
> **Status** `string` *required*
>
> Status of the exposure information. Possible values: `Online`, `Offline`
>
> **Timestamp** `string` *required*
>
> The last time the credit was updated.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 11,
>   "type": "Exposure",
>   "ts": "2021-09-16T16:17:06.892914Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "ExposureCurrency": "USD",
>       "Exposure": "1000000",
>       "ExposureLimit": "5000000",
>       "Status": "Online",
>       "Timestamp": "2021-09-16T16:17:06.892914Z"
>     }
>   ]
> }
> ```
