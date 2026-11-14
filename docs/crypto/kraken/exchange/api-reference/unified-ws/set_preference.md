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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/set_preference'
updated_at: 2026-11-13
---

# Set Preference

> Set account preferences through the Unified WebSocket API

UWS
uws.kraken.com/v2/private
set\_preference

Use `set_preference` to change the authenticated account's preferences. Each preference is supplied in its own object within `params`.

Currently, `leverage_mode` is the supported preference and applies to derivatives markets. Send a numeric `max_leverage` to set fixed leverage, or explicitly send `null` to restore cross margin.

The permitted leverage depends on the market's margin schedule and the account's position and available margin. A requested change can be rejected if it exceeds the permitted leverage, leaves insufficient margin, or would cause liquidation.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `set_preference`
>
> **params** `object` *required*
>
> **properties**
>
> **asset\_class** `string` *required*
>
> Value: `derivatives`. Leverage preferences are not available for Spot.
>
> **token** `string` *required*
>
> WebSocket authentication token. See the [Unified WebSocket authentication flow](https://docs.kraken.com/exchange/api-reference/unified-websocket#authentication).
>
> **leverage\_mode** `object` *required*
>
> The leverage preference to set. `symbol` and `max_leverage` must be nested inside this object.
>
> **properties**
>
> **symbol** `string` *required*
>
> Derivatives market identifier, for example `PF_XBTUSD`. The market must be recognised by the exchange.
>
> **max\_leverage** `number | null` *required*
>
> Numeric leverage, for example `5` for 5x, or `null` for cross margin. Send a JSON number, not a quoted string. Omitting this field does not restore cross margin and is rejected. The trading engine validates the permitted range for the market.
>
> **req\_id** `integer`
>
> Optional client request identifier echoed in the response. Must be a non-negative integer less than `18446744073709551616`.

> [tab] Response
>
> **method** `string`
>
> Value: `set_preference`
>
> **result** `object`
>
> Present when `success` is `true`.
>
> **properties**
>
> **leverage\_mode** `object`
>
> **properties**
>
> **symbol** `string`
>
> Canonical market identifier resolved by the exchange.
>
> **max\_leverage** `number | null`
>
> The accepted numeric leverage, or `null` for cross margin.
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

## Examples

```json Fixed leverage request theme={null}
{
    "method": "set_preference",
    "params": {
        "asset_class": "derivatives",
        "token": "YOUR_WEBSOCKET_TOKEN",
        "leverage_mode": {
            "symbol": "PF_XBTUSD",
            "max_leverage": 5
        }
    },
    "req_id": 101
}
```

```json Fixed leverage response theme={null}
{
    "method": "set_preference",
    "result": {
        "leverage_mode": {
            "symbol": "PF_XBTUSD",
            "max_leverage": 5
        }
    },
    "success": true,
    "req_id": 101,
    "time_in": "2026-11-11T09:00:00.000000Z",
    "time_out": "2026-11-11T09:00:00.050000Z"
}
```

```json Cross margin request theme={null}
{
    "method": "set_preference",
    "params": {
        "asset_class": "derivatives",
        "token": "YOUR_WEBSOCKET_TOKEN",
        "leverage_mode": {
            "symbol": "PF_XBTUSD",
            "max_leverage": null
        }
    },
    "req_id": 102
}
```

```json Cross margin response theme={null}
{
    "method": "set_preference",
    "result": {
        "leverage_mode": {
            "symbol": "PF_XBTUSD",
            "max_leverage": null
        }
    },
    "success": true,
    "req_id": 102,
    "time_in": "2026-11-11T09:01:00.000000Z",
    "time_out": "2026-11-11T09:01:00.050000Z"
}
```

```json Rejected change theme={null}
{
    "method": "set_preference",
    "success": false,
    "error": "Insufficient margin for the requested leverage",
    "req_id": 103,
    "time_in": "2026-11-11T09:02:00.000000Z",
    "time_out": "2026-11-11T09:02:00.050000Z"
}
```

## Errors

A rejected change returns `success: false` and an `error` string. Leverage-specific errors include:

* `Leverage exceeds the market's margin schedule`
* `Leverage change would cause liquidation`
* `Insufficient margin for the requested leverage`
* `Leverage is outside the permitted range for this market`
* `Leverage change rejected`

Unknown markets return `Unknown 'params.leverage_mode.symbol'`. Authentication, maintenance, rate limits, or temporary exchange unavailability can also prevent a change.
