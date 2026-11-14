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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/preferences'
updated_at: 2026-11-13
---

# Preferences

> Read account preferences, including whether the user may trade futures

UWS
uws.kraken.com/v2/private
preferences

The `preferences` channel streams the user's account preferences, including the account's futures (perpetuals) trading permission. Use it to decide whether to present futures functionality.

This channel contains account specific data, an authentication token is required in the request.

On subscribe, `preferences` sends a snapshot. It then sends an update whenever a value changes.

If preferences are not available yet, the subscribe fails with the error `Preferences are not available yet, try again later`. Retry the subscribe after a short delay.

To set a derivatives market's leverage preference, use
[`set_preference`](https://docs.kraken.com/exchange/api-reference/unified-ws/set_preference).

## Subscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `preferences`
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
> **method** `string` *required*
>
> Value: `subscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `preferences`
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot / Update

The snapshot provides the user's current preferences. An update carries the new value after a change.

**channel** `string`

Value: `preferences`

**type** `string`

One of: `snapshot`, `update`

**data** `object`

**properties**

**futures\_trading** `string`

One of: `enabled`, `reduce_only`, `disabled`

The futures (perpetuals) trading permission on the user's account. The value is derived from the account's verification (KYC) attributes, in this order:

* `enabled`: the account has a futures trading permission.
* `reduce_only`: the account has no futures trading permission, but has a reduce-only futures permission. Only orders that reduce or close existing futures positions are allowed.
* `disabled`: the account has neither permission, or has no attributes on record. Hide futures functionality and do not attempt futures orders.

## Unsubscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `preferences`
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
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `preferences`
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

```json Subscribe Request theme={null}
{
    "method": "subscribe",
    "params": {
        "channel": "preferences",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "preferences"
    },
    "success": true,
    "time_in": "2023-10-16T13:29:13.111530Z",
    "time_out": "2023-10-16T13:29:13.111775Z"
}
```

```json Snapshot theme={null}
{
    "channel": "preferences",
    "type": "snapshot",
    "data": {
        "futures_trading": "enabled"
    }
}
```

```json Update theme={null}
{
    "channel": "preferences",
    "type": "update",
    "data": {
        "futures_trading": "reduce_only"
    }
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "preferences",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "preferences"
    },
    "success": true,
    "time_in": "2023-10-16T13:29:13.111530Z",
    "time_out": "2023-10-16T13:29:13.111775Z"
}
```
