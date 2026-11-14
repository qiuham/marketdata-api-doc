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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/margin'
updated_at: 2026-11-13
---

# Margin

> Subscribe to derivatives wallet margin state

UWS
uws.kraken.com/v2/private
margin

The `margin` channel streams the margin state of your derivatives wallets: the multi-collateral (flex) wallet and each single-collateral wallet.

It carries the margin portion of the Derivatives WebSocket [`balances`](https://docs.kraken.com/exchange/api-reference/futures-websocket/balances) feed — the `flex_futures` and `futures` structures. Use [`balances`](https://docs.kraken.com/exchange/api-reference/unified-ws/balances) for asset quantities and ledger transactions; use this channel for margin requirements, margin equity, and available margin.

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
> Value: `margin`
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
> Value: `subscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `margin`
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

This channel does not accept a `snapshot` parameter. Every message is a full state replacement, and the current state is always delivered on subscribe. Sending `params.snapshot` is rejected with `'params.snapshot' is not valid for the margin channel`.

A connection may hold a single `margin` subscription, bound to the account of the token used to subscribe. A second subscribe attempt on the same connection is rejected with `Already subscribed to margin channel`.

## Messages

Each message carries one complete section of your margin state, identified by `type`: the multi-collateral wallet (`multi_collateral`) or the single-collateral wallets (`single_collateral`). There is no snapshot/update distinction — `data` is always the full current state of that section, never a delta.

Replace any state you hold for a section when a message for it arrives, rather than merging into it. You receive the current state of each applicable section on subscribe, then a fresh message for a section whenever it changes.

> [!NOTE]
>
> All margin figures are sent as JSON numbers. Use a decimal-aware JSON parser if you need to preserve all digits. A figure that is unavailable is omitted from `data` rather than sent as `null`.

### Multi-collateral wallet

**channel** `string`

Value: `margin`

**type** `string`

Value: `multi_collateral`

**data** `object`

Margin state of the multi-collateral (flex) wallet. All values are in USD.

**properties**

**time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`

The time the margin state was computed, with nanosecond precision.

**balance\_value** `float`

The current USD balance of the account.

**portfolio\_value** `float`

The current collateral value with unrealized margin from any open positions.

**collateral\_value** `float`

The current USD balance with haircuts.

**initial\_margin** `float`

The total initial margin for open positions and open orders.

**initial\_margin\_without\_orders** `float`

The total initial margin for open positions.

**maintenance\_margin** `float`

The total maintenance margin for open positions.

**pnl** `float`

The total profit and loss for open positions.

**unrealized\_funding** `float`

The total unrealized funding for open positions.

**total\_unrealized** `float`

The total unrealized funding and pnl.

**total\_unrealized\_as\_margin** `float`

The total unrealized in USD.

**margin\_equity** `float`

The current collateral value and unrealized margin.

**available\_margin** `float`

The margin equity minus initial margin.

**cross** `object`

Condition: if a cross-margin breakdown is available.

The current margin information for cross position(s).

**properties**

**balance\_value** `float`

Total USD balance minus initial margin of isolated positions.

**portfolio\_value** `float`

USD balance plus total unrealized.

**collateral\_value** `float`

USD balance, but with haircuts applied.

**initial\_margin** `float`

Initial margin for all cross positions plus open orders.

**initial\_margin\_without\_orders** `float`

Initial margin for all cross positions.

**maintenance\_margin** `float`

Maintenance margin for all cross positions.

**pnl** `float`

Total profit and loss for all cross positions.

**unrealized\_funding** `float`

Unrealized funding for all cross positions.

**total\_unrealized** `float`

Unrealized funding plus pnl.

**total\_unrealized\_as\_margin** `float`

Total unrealized as USD.

**margin\_equity** `float`

Collateral value plus total unrealized.

**available\_margin** `float`

Margin equity minus initial margin of cross and isolated positions.

**effective\_leverage** `float`

Ratio of position size to margin equity.

**isolated** `object[]`

Per-instrument margin figures for isolated-margin positions. Always present, and may be empty.

**properties**

**tradeable** `string`

Example: `PF_ETHUSD`

The symbol of the isolated position's instrument.

**initial\_margin** `float`

Initial margin for the position plus open orders.

**initial\_margin\_without\_orders** `float`

Initial margin for the position.

**maintenance\_margin** `float`

Maintenance margin for the position.

**pnl** `float`

Total profit and loss for the position.

**unrealized\_funding** `float`

Unrealized funding for the position.

**total\_unrealized** `float`

Unrealized funding plus pnl.

**total\_unrealized\_as\_margin** `float`

Total unrealized as USD.

### Single-collateral wallets

**channel** `string`

Value: `margin`

**type** `string`

Value: `single_collateral`

**data** `object`

**properties**

**time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456789Z`

The time the margin state was computed, with nanosecond precision.

**wallets** `object[]`

The single-collateral wallets, one entry per wallet. Always present, and may be empty.

**properties**

**base\_currency** `string`

Example: `XBT`

The base currency of the wallet's pair.

**quote\_currency** `string`

Example: `USD`

The quote currency of the wallet's pair.

**unit** `string`

Example: `XBT`

The wallet settlement unit. The figures below are denominated in this asset.

**balance** `float`

The current balance in settlement units.

**portfolio\_value** `float`

The current balance with haircuts and any unrealized margin from open positions, in settlement units.

**initial\_margin** `float`

The initial margin for open positions and open orders.

**maintenance\_margin** `float`

The maintenance margin for open positions.

**available** `float`

The current portfolio value minus initial margin.

**unrealized\_funding** `float`

The total unrealized funding for open positions.

**pnl** `float`

The total profit and loss for open positions.

### Margin unavailable

**channel** `string`

Value: `margin`

**error** `string`

One of: `margin_unavailable`

Your margin state cannot be served, and the subscription has been dropped server side. This can arrive after a successful subscribe acknowledgement. Resubscribe to resume the feed.

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
> Value: `margin`
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
> Value: `margin`
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
        "channel": "margin",
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
        "channel": "margin"
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
        "channel": "margin"
    },
    "error": "Already subscribed to margin channel",
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```

```json Multi-collateral theme={null}
{
    "channel": "margin",
    "type": "multi_collateral",
    "data": {
        "time": "2023-10-16T13:18:35.318297123Z",
        "balance_value": 20411.3030,
        "portfolio_value": 20601.9604,
        "collateral_value": 20388.4271,
        "initial_margin": 1042.9500,
        "initial_margin_without_orders": 912.7500,
        "maintenance_margin": 456.3750,
        "pnl": 178.5000,
        "unrealized_funding": 12.1574,
        "total_unrealized": 190.6574,
        "total_unrealized_as_margin": 190.6574,
        "margin_equity": 20579.0845,
        "available_margin": 19536.1345,
        "cross": {
            "balance_value": 20228.3030,
            "portfolio_value": 20412.9604,
            "collateral_value": 20205.4271,
            "initial_margin": 859.9500,
            "initial_margin_without_orders": 729.7500,
            "maintenance_margin": 364.8750,
            "pnl": 172.5000,
            "unrealized_funding": 12.1574,
            "total_unrealized": 184.6574,
            "total_unrealized_as_margin": 184.6574,
            "margin_equity": 20390.0845,
            "available_margin": 19347.1345,
            "effective_leverage": 0.7158
        },
        "isolated": [
            {
                "tradeable": "PF_ETHUSD",
                "initial_margin": 183.0000,
                "initial_margin_without_orders": 183.0000,
                "maintenance_margin": 91.5000,
                "pnl": 6.0000,
                "unrealized_funding": 0.0000,
                "total_unrealized": 6.0000,
                "total_unrealized_as_margin": 6.0000
            }
        ]
    }
}
```

```json No Isolated Positions theme={null}
{
    "channel": "margin",
    "type": "multi_collateral",
    "data": {
        "time": "2023-10-16T13:18:35.318297123Z",
        "balance_value": 20411.3030,
        "portfolio_value": 20601.9604,
        "collateral_value": 20388.4271,
        "initial_margin": 0.0000,
        "initial_margin_without_orders": 0.0000,
        "maintenance_margin": 0.0000,
        "pnl": 0.0000,
        "unrealized_funding": 0.0000,
        "total_unrealized": 0.0000,
        "total_unrealized_as_margin": 0.0000,
        "margin_equity": 20411.3030,
        "available_margin": 20411.3030,
        "isolated": []
    }
}
```

```json Single-collateral theme={null}
{
    "channel": "margin",
    "type": "single_collateral",
    "data": {
        "time": "2023-10-16T13:20:01.442310555Z",
        "wallets": [
            {
                "base_currency": "XBT",
                "quote_currency": "USD",
                "unit": "XBT",
                "balance": 0.1219368845,
                "portfolio_value": 0.1231447102,
                "initial_margin": 0.0048100000,
                "maintenance_margin": 0.0024050000,
                "available": 0.1183347102,
                "unrealized_funding": 0.0000418257,
                "pnl": 0.0011660000
            },
            {
                "base_currency": "ETH",
                "quote_currency": "EUR",
                "unit": "ETH",
                "balance": 1.8714395862,
                "portfolio_value": 1.8714395862,
                "initial_margin": 0.0000000000,
                "maintenance_margin": 0.0000000000,
                "available": 1.8714395862,
                "unrealized_funding": 0.0000000000,
                "pnl": 0.0000000000
            }
        ]
    }
}
```

```json Margin Unavailable theme={null}
{
    "channel": "margin",
    "error": "margin_unavailable"
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "margin",
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
        "channel": "margin"
    },
    "time_in": "2023-10-16T13:30:35.303171Z",
    "time_out": "2023-10-16T13:30:35.318297Z"
}
```
