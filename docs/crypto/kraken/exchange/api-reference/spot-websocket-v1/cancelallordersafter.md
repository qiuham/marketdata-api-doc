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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/cancelallordersafter'
updated_at: 2026-11-13
---

# Cancel on Disconnect

> Dead Man's Switch mechanism to cancel all orders after a timeout

WSS
ws-auth.kraken.com
cancelAllOrdersAfter

`cancelAllOrdersAfter` provides a "Dead Man's Switch" mechanism to protect the client from network malfunction, extreme latency or unexpected matching engine downtime. The client can send a request with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders when the timer expires.

The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.

> [tab] Request
>
> **event** `string` *required*
>
> Value: `cancelAllOrdersAfter`
>
> **timeout** `integer` *required*
>
> Timeout specified in seconds. 0 to disable the timer.
>
> **reqid** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **token** `string` *required*
>
> Session token from the [GetWebSocketsToken](https://docs.kraken.com/api-reference/trading/get-websockets-token.md) REST endpoint.

> [tab] Response
>
> **event** `string`
>
> Value: `cancelAllOrdersAfterStatus`
>
> **currentTime** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123456Z`
>
> Timestamp when the request has been handled (second precision, rounded up).
>
> **triggerTime** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123456Z`
>
> Timestamp at which all open orders will be cancelled, unless the timer is extended or disabled (second precision, rounded up).
>
> **status** `string`
>
> One of: `ok`, `error`
>
> **reqid** `integer`
>
> Client originated identifier for the request that initiated this response.
>
> **errorMessage** `string`
>
> Error message for unsuccessful requests.

```json Request theme={null}
{
    "event": "cancelAllOrdersAfter",
    "reqid": 1608543428050,
    "timeout": 60,
    "token": "0000000000000000000000000000000000000000"
}
```

```json Response: Enabled theme={null}
{
    "currentTime": "2020-12-21T09:37:09Z",
    "event": "cancelAllOrdersAfterStatus",
    "reqid": 1608543428050,
    "status": "ok",
    "triggerTime": "2020-12-21T09:38:09Z"
}
```

```json Response: Disabled theme={null}
{
    "currentTime": "2020-12-21T09:37:09Z",
    "event": "cancelAllOrdersAfterStatus",
    "reqid": 1608543428051,
    "status": "ok",
    "triggerTime": "0"
}
```
