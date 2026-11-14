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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/cancel_after'
updated_at: 2026-11-13
---

# Cancel on Disconnect

> Dead Man's Switch mechanism to cancel all orders after a timeout

WSS
ws-auth.kraken.com/v2
cancel\_all\_orders\_after

`cancel_all_orders_after` provides a "Dead Man's Switch" mechanism to protect from network malfunction, extreme latency or unexpected matching engine downtime.

* The client sends request with a timeout (in seconds), that will start a countdown timer in the trading engine which will cancel all client orders when the timer expires.
* The client must keep sending new requests to reset the trigger time, or deactivate the mechanism by specifying a timeout of 0.
* If the timer expires, all orders in the account are cancelled and the feature is disabled until the next `cancel_all_orders_after` request.
* The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds. This allows the client to keep the orders in place in case of a brief disconnection or transient delay, while keeping them safe in case of a network breakdown.

> [!NOTE]
>
> It is recommended to disable the timer ahead of scheduled trading engine maintenance (if the timer is enabled, all orders will be cancelled when the trading engine comes back from downtime).

> [tab] Request
>
> **method** `string` *required*
>
> Value: `cancel_all_orders_after`
>
> **params** `object`
>
> **properties**
>
> **timeout** `integer` *required*
>
> Duration (in seconds) to set/extend the timer, it should be less than `86400` seconds.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string`
>
> Value: `cancel_all_orders_after`
>
> **result** `object`
>
> Condition: if `success` is `true`
>
> **properties**
>
> **currentTime** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123456Z`
>
> The current engine time.
>
> **triggerTime** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123456Z`
>
> The time the orders will be expired in the engine.
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **time\_in** `string`
>
> The timestamp when the request was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the response was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`

```json Request theme={null}
{
    "method": "cancel_all_orders_after",
    "params": {
        "timeout": 100,
        "token": "zwpdzWUe18Bn6h4TAMorh26+QbcMeST2B5tamfe+pgQ"
    },
    "req_id": 1234567890
}
```

```json Response theme={null}
{
    "method": "cancel_all_orders_after",
    "req_id": 1234567890,
    "result": {
        "currentTime": "2023-09-21T15:49:29Z",
        "triggerTime": "2023-09-21T15:51:09Z"
    },
    "success": true,
    "time_in": "2023-09-21T15:49:28.627900Z",
    "time_out": "2023-09-21T15:49:28.649057Z"
}
```
