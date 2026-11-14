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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/instrument'
updated_at: 2026-11-13
---

# Instruments

> Subscribe to reference data for all active assets and tradeable pairs

WSS
ws.kraken.com/v2
instrument

The `instrument` channel provides a stream of reference data of all active assets and tradeable pairs.

It provides the symbol identifiers, precisions, trading parameters and rules.

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
> Value: `instrument`
>
> **execution\_venue** `string`
>
> One of: `international`, `bitnomial-exchange`\\
>
> Default: `international`
>
> The execution venue for the instrument channel. If not included, defaults to `international`.
>
> **include\_tokenized\_assets** `boolean`
>
> One of: `false`, `true`\\
>
> Default: `false`
>
> If `true`, include xStocks in the response, otherwise include crypto spot pairs only.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> Request a snapshot after subscribing.
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
> Value: `instrument`
>
> **snapshot** `boolean`
>
> Indicates if a snapshot is requested.
>
> **warnings** `string[]`
>
> An advisory message, highlighting deprecated fields or upcoming changes to the channel.
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

The snapshot and update responses share the same schema.

**channel** `string`

Value: `instrument`

**type** `string`

One of: `snapshot`, `update`

**data** `object`

**properties**

**assets** `object[]`

A list of assets.

**properties**

**borrowable** `boolean`

One of: `true`, `false`

Flag if asset is borrowable.

**collateral\_value** `float`

Valuation as margin collateral (if applicable).

**id** `string`

Asset identifier.

**margin\_rate** `float`

Interest rate to borrow the asset.

**precision** `integer`

Maximum precision for asset ledger, balances.

**precision\_display** `integer`

Recommended display precision.

**multiplier** `float`

Multiplier of the tokenised asset. Fixed conversion rate of the token.

**class** `string`

Asset class (e.g. `currency`).

**status** `string`

One of: `depositonly`, `disabled`, `enabled`, `fundingtemporarilydisabled`, `withdrawalonly`, `workinprogress`

Status of asset.

**pairs** `object[]`

A list of pairs.

**properties**

**base** `string`

Asset identifier of the base currency.

**quote** `string`

Asset identifier of the quote currency.

**cost\_min** `float`

Minimum cost (price \* qty) for new orders.

**cost\_precision** `integer`

Maximum precision used for cost prices.

**has\_index** `boolean`

Whether the pair has an index available for example stop-loss triggers.

**margin\_initial** `float`

Condition: On marginable pairs only

Initial margin requirement (in percent).

**marginable** `boolean`

One of: `true`, `false`

Whether the pair can be traded on margin.

**position\_limit\_long** `integer`

Condition: On marginable pairs only

Limit for long positions.

**position\_limit\_short** `integer`

Condition: On marginable pairs only

Limit for short positions.

**price\_increment** `float`

Minimum price increment for new orders.

**price\_precision** `integer`

Maximum precision used for order prices.

**qty\_increment** `float`

Minimum quantity increment for new orders.

**qty\_min** `float`

Minimum quantity (in base currency) for new orders.

**qty\_precision** `integer`

Maximum precision used for order quantities.

**ws\_display\_price\_precision** `integer`

Recommended display precision for prices in WebSocket feeds.

**status** `string`

One of: `cancel_only`, `delisted`, `limit_only`, `maintenance`, `online`, `post_only`, `reduce_only`, `work_in_progress`

Status of pair.

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**tick\_size** `float` *deprecated*

Deprecated: Use `price_increment`

Minimum price increment for new orders.

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
> Value: `instrument`
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
> Value: `instrument`
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
        "channel": "instrument"
    },
    "req_id": 79
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "req_id": 79,
    "result": {
        "channel": "instrument",
        "snapshot": true,
        "warnings": [
            "tick_size is deprecated, use price_increment"
        ]
    },
    "success": true,
    "time_in": "2023-09-26T16:49:20.962586Z",
    "time_out": "2023-09-26T16:49:20.962630Z"
}
```

```json Snapshot theme={null}
{
    "channel": "instrument",
    "type": "snapshot",
    "data": {
        "assets": [
            {
                "id": "USD",
                "status": "enabled",
                "precision": 4,
                "precision_display": 2,
                "borrowable": true,
                "collateral_value": 1.0,
                "margin_rate": 0.015
            },
            {
                "id": "BTC",
                "status": "enabled",
                "precision": 10,
                "precision_display": 5,
                "borrowable": true,
                "collateral_value": 1.0,
                "margin_rate": 0.01
            },
            {
                "id": "XRP",
                "status": "enabled",
                "precision": 8,
                "precision_display": 5,
                "borrowable": true,
                "collateral_value": 0.0,
                "margin_rate": 0.02
            }
        ],
        "pairs": [
            {
                "symbol": "BTC/USD",
                "base": "BTC",
                "quote": "USD",
                "status": "online",
                "qty_precision": 8,
                "qty_increment": 1e-08,
                "price_precision": 1,
                "cost_precision": 5,
                "marginable": true,
                "has_index": true,
                "cost_min": 0.5,
                "margin_initial": 0.2,
                "position_limit_long": 250,
                "position_limit_short": 200,
                "tick_size": 0.1,
                "price_increment": 0.1,
                "qty_min": 0.0001
            },
            {
                "symbol": "MATIC/GBP",
                "base": "MATIC",
                "quote": "GBP",
                "status": "online",
                "qty_precision": 8,
                "qty_increment": 1e-08,
                "price_precision": 4,
                "cost_precision": 6,
                "marginable": false,
                "has_index": true,
                "cost_min": 0.43,
                "tick_size": 0.0001,
                "price_increment": 0.0001,
                "qty_min": 4.0
            }
        ]
    }
}
```

```json Update theme={null}
{
    "channel": "instrument",
    "type": "update",
    "data": {
       "assets": [
          {
             "id": "BTC",
             "status": "enabled",
             "precision": 10,
             "precision_display": 5,
             "borrowable": true,
             "collateral_value": 1.0,
             "margin_rate": 0.01
          }
       ],
       "pairs": []
    }
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "instrument"
    },
    "req_id": 79
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "req_id": 79,
    "result": {
        "channel": "instrument"
    },
    "success": true,
    "time_in": "2023-09-26T16:49:20.962586Z",
    "time_out": "2023-09-26T16:49:20.962630Z"
}
```
