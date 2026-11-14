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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/positions'
updated_at: 2026-11-13
---

# Positions

> Subscribe to open derivatives positions for your account

UWS
uws.kraken.com/v2/private
positions

The `positions` channel streams the open positions held on this account, split into `futures` and `options`.

This channel contains account specific data, an authentication token is required in the request.

> [!NOTE]
>
> This channel is currently only available for futures (`derivatives`).

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
> Value: `positions`
>
> **asset\_class** `string` *required*
>
> One of: `derivatives`
>
> The asset class for the request.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> Request a snapshot after subscribing. If `false`, only updates are streamed and no snapshot is sent.
>
> Not valid together with `with_margin`.
>
> **with\_margin** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> Stream the enriched payload with margin and risk figures for each position. See [With margin](#with-margin).
>
> Cannot be combined with `snapshot`.
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
> Value: `positions`
>
> **with\_margin** `boolean`
>
> Condition: present and `true` only when the subscription requested `with_margin: true`.
>
> Echoes that the enriched margin feed is engaged for this subscription.
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

A connection may hold a single `positions` subscription, bound to the account of the token used to subscribe. A second subscribe attempt on the same connection is rejected with `Already subscribed to positions channel`.

## Snapshot / Update

The snapshot provides the full set of open positions on the account. Exactly one snapshot is delivered per subscription, before any update.

Updates are streamed as positions change. Each update carries the positions affected by that event, not the full account state. A position that has been closed is reported on the update path with a `size` of `0`.

**channel** `string`

Value: `positions`

**type** `string`

One of: `snapshot`, `update`

**data** `object`

**properties**

**time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`

The time of the position event, with nanosecond precision.

**futures** `object[]`

A list of open futures positions. Always present, and may be empty.

**properties**

**tradeable** `string`

Example: `PF_XBTUSD`

The symbol of the futures contract.

**size** `float`

The size of the position. On the update path, a value of `0` indicates the position has been closed.

**entry\_price** `float`

The average entry price of the position.

**fill\_time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`\\

Condition: if the fill time is known.

The time of the fill that last changed this position.

**options** `object[]`

A list of open options positions. Always present, and may be empty.

**properties**

**tradeable** `string`

Example: `OP_XBT-20250630-50000-C`

The symbol of the options contract.

**size** `float`

The size of the position. On the update path, a value of `0` indicates the position has been closed.

**entry\_price** `float`

The average entry price of the position.

**fill\_time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`\\

Condition: if the fill time is known.

The time of the fill that last changed this position.

**error** `string`

One of: `snapshot_too_large`\\

Condition: if the snapshot exceeded the maximum message size.

The snapshot could not be delivered. The `futures` and `options` lists are empty and no `time` is sent. Resubscribe to request the snapshot again.

> [!NOTE]
>
> `size` and `entry_price` are sent as JSON numbers. Use a decimal-aware JSON parser if you need to preserve all digits.

## With margin

Subscribing with `with_margin: true` streams an enriched payload sourced from the margin service, adding margin, risk and (for options) greeks figures to each position.

The enriched feed differs from the default feed in three ways:

* No `type` field. Every message is complete per-position state — treat each as a full replace of the account's positions, not a delta.
* No `snapshot` control. Each message already carries full state, so `snapshot` is not accepted alongside `with_margin`.
* Figures are omitted when unavailable. A field whose value is undefined is left out of the row rather than sent as `null`. All numeric figures are sent as JSON numbers.

The `futures` and `options` lists are always present and may be empty, as in the default feed.

**channel** `string`

Value: `positions`

**data** `object`

**properties**

**time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`

The time of the position event, with nanosecond precision.

**futures** `object[]`

A list of open futures positions. Always present, and may be empty.

**properties**

**tradeable** `string`

Example: `PF_XBTUSD`

The symbol of the futures contract.

**size** `float`

The size of the position.

**entry\_price** `float`

The average entry price of the position.

**mark\_price** `float`

The mark price of the position instrument.

**index\_price** `float`

The index price of the position instrument.

**fill\_time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`\\

Condition: if the fill time is known.

The time of the fill that last changed this position.

**pnl** `float`

The profit and loss of the position.

**initial\_margin** `float`

The initial margin for the open position.

**initial\_margin\_with\_orders** `float`

The initial margin for the open position and open orders of the same instrument.

**maintenance\_margin** `float`

The maintenance margin for the open position.

**unrealized\_funding** `float`

Unrealised funding from the funding rate.

**liquidation\_threshold** `float`

Condition: omitted when the account holds any option position.

The mark price of the contract at which the position will be liquidated.

**effective\_leverage** `float`

Condition: omitted when the account holds any option position.

How leveraged the net position is in a given margin account. Formula: Position Value at Market / Portfolio Value.

**return\_on\_equity** `float`

The percentage gain or loss relative to the initial margin used in the position. Formula: PnL/IM.

**max\_fixed\_leverage** `float`

The maximum allowed fixed leverage for the position's instrument.

**pnl\_currency** `string`

The profit currency for the position. Not returned for inverse positions.

**options** `object[]`

A list of open options positions. Always present, and may be empty.

**properties**

**tradeable** `string`

Example: `OP_XBT-20250630-50000-C`

The symbol of the options contract.

**size** `float`

The size of the position.

**entry\_price** `float`

The average entry price of the position.

**mark\_price** `float`

The mark price of the position instrument.

**index\_price** `float`

The index price of the position instrument.

**fill\_time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`\\

Condition: if the fill time is known.

The time of the fill that last changed this position.

**pnl** `float`

The profit and loss of the position.

**iv** `float`

The option's implied volatility.

**delta** `float`

Delta, the option value's sensitivity to change in the underlying price.

**gamma** `float`

Gamma, delta's sensitivity to change in the underlying price.

**vega** `float`

Vega, the option value's sensitivity to change in volatility.

**theta** `float`

Theta, the option value's sensitivity to the passage of time.

**rho** `float`

Rho, the option value's sensitivity to the interest rate.

**error** `string`

One of: `snapshot_too_large`, `margin_unavailable`

A `snapshot_too_large` error is delivered in place of the data when the message exceeded the maximum size; the `futures` and `options` lists are empty and no `time` is sent. A `margin_unavailable` error is delivered if the margin service stops serving this account after the subscription was accepted, and the subscription is closed. Neither error carries a `type` field.

```json Subscribe Request theme={null}
{
    "method": "subscribe",
    "params": {
        "channel": "positions",
        "asset_class": "derivatives",
        "with_margin": true,
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    },
    "req_id": 101
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "success": true,
    "req_id": 101,
    "result": {
        "channel": "positions",
        "with_margin": true
    },
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```

```json Margin Unavailable theme={null}
{
    "method": "subscribe",
    "success": false,
    "req_id": 101,
    "result": {
        "channel": "positions"
    },
    "error": "margin_unavailable",
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```

```json Positions theme={null}
{
    "channel": "positions",
    "data": {
        "time": "2023-10-16T13:18:35.318297123Z",
        "futures": [
            {
                "tradeable": "PF_XBTUSD",
                "size": 0.04,
                "entry_price": 26911.75,
                "mark_price": 29900.81124638736,
                "index_price": 29900.47,
                "fill_time": "2023-10-16T09:12:44.104512000Z",
                "pnl": 119.56244985549435,
                "initial_margin": 21.529400000000003,
                "initial_margin_with_orders": 21.529400000000003,
                "maintenance_margin": 10.764700000000001,
                "unrealized_funding": 0.0004114160669590132,
                "liquidation_threshold": 9572.804662403718,
                "effective_leverage": 0.31865408963748215,
                "return_on_equity": 5.553450159107747,
                "max_fixed_leverage": 50,
                "pnl_currency": "USD"
            }
        ],
        "options": [
            {
                "tradeable": "OP_XBT-20250630-50000-C",
                "size": 5,
                "entry_price": 1250.5,
                "mark_price": 1310.2,
                "index_price": 50120.5,
                "fill_time": "2023-10-16T10:01:02.998001000Z",
                "pnl": 298.5,
                "iv": 0.62,
                "delta": 0.55,
                "gamma": 0.0001,
                "vega": 12.4,
                "theta": -8.1,
                "rho": 9.7
            }
        ]
    }
}
```

```json Snapshot Too Large theme={null}
{
    "channel": "positions",
    "error": "snapshot_too_large",
    "data": {
        "futures": [],
        "options": []
    }
}
```

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
> Value: `positions`
>
> **asset\_class** `string` *required*
>
> One of: `derivatives`
>
> The asset class for the request.
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
> Value: `positions`
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
        "channel": "positions",
        "asset_class": "derivatives",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    },
    "req_id": 101
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "success": true,
    "req_id": 101,
    "result": {
        "channel": "positions"
    },
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```

```json Subscribe Error theme={null}
{
    "method": "subscribe",
    "success": false,
    "req_id": 101,
    "result": {
        "channel": "positions"
    },
    "error": "Already subscribed to positions channel",
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```

```json Snapshot theme={null}
{
    "channel": "positions",
    "type": "snapshot",
    "data": {
        "time": "2023-10-16T13:18:35.318297123Z",
        "futures": [
            {
                "tradeable": "PF_XBTUSD",
                "size": 100,
                "entry_price": 50000,
                "fill_time": "2023-10-16T09:12:44.104512000Z"
            }
        ],
        "options": [
            {
                "tradeable": "OP_XBT-20250630-50000-C",
                "size": 5,
                "entry_price": 1250.5,
                "fill_time": "2023-10-16T10:01:02.998001000Z"
            }
        ]
    }
}
```

```json Empty Snapshot theme={null}
{
    "channel": "positions",
    "type": "snapshot",
    "data": {
        "time": "2023-10-16T13:18:35.318297123Z",
        "futures": [],
        "options": []
    }
}
```

```json Update theme={null}
{
    "channel": "positions",
    "type": "update",
    "data": {
        "time": "2023-10-16T13:20:01.442310555Z",
        "futures": [
            {
                "tradeable": "PF_XBTUSD",
                "size": 150,
                "entry_price": 50166.66,
                "fill_time": "2023-10-16T13:20:01.442100000Z"
            }
        ],
        "options": []
    }
}
```

```json Position Closed theme={null}
{
    "channel": "positions",
    "type": "update",
    "data": {
        "time": "2023-10-16T13:25:47.100200300Z",
        "futures": [
            {
                "tradeable": "PF_XBTUSD",
                "size": 0,
                "entry_price": 50166.66,
                "fill_time": "2023-10-16T13:25:47.100000000Z"
            }
        ],
        "options": []
    }
}
```

```json Snapshot Too Large theme={null}
{
    "channel": "positions",
    "type": "snapshot",
    "error": "snapshot_too_large",
    "data": {
        "futures": [],
        "options": []
    }
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "positions",
        "asset_class": "derivatives",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    },
    "req_id": 102
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "success": true,
    "req_id": 102,
    "result": {
        "channel": "positions"
    },
    "time_in": "2023-10-16T13:30:35.303171Z",
    "time_out": "2023-10-16T13:30:35.318297Z"
}
```
