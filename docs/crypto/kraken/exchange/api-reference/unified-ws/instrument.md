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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/instrument'
updated_at: 2026-11-13
---

# Instruments

> Subscribe to reference data for all active assets and tradeable pairs

UWS
uws.kraken.com/v2/public
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
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
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

Example: `0.5`

Minimum price increment for new orders. Order prices must be a multiple of this value.

For `derivatives`, a contract's tick is not always a power of ten, so use this field rather than deriving an increment from `price_precision`. Where the contract publishes an explicit tick size, `price_increment` carries it; otherwise it is `10^-price_precision`.

**price\_precision** `integer`

Maximum precision used for order prices.

**qty\_increment** `float`

Example: `0.0001`

Minimum quantity increment for new orders. Order quantities must be a multiple of this value.

For `derivatives`, this is always `10^-qty_precision`.

**qty\_min** `float`

Example: `0.0001`

Minimum quantity (in base currency) for new orders.

For `derivatives`, this is the contract's minimum order size where one is published, rounded up to the next `qty_increment` so that an order sized at exactly this value is always on the quantity grid. Where no minimum is published, it is one `qty_increment`.

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
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
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
        "channel": "instrument",
        "asset_class": "derivatives"
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
                "margin_rate": 0.03
            },
            {
                "id": "XBT",
                "status": "enabled",
                "precision": 10,
                "precision_display": 5,
                "borrowable": true,
                "collateral_value": 0.99,
                "margin_rate": 0.01
            },
            {
                "id": "ETH",
                "status": "enabled",
                "precision": 10,
                "precision_display": 5,
                "borrowable": true,
                "collateral_value": 0.99,
                "margin_rate": 0.04
            },
            {
                "id": "XRP",
                "status": "enabled",
                "precision": 8,
                "precision_display": 5,
                "borrowable": true,
                "collateral_value": 0.95,
                "margin_rate": 0.04
            }
        ],
        "pairs": [
            {
                "symbol": "PI_XBTUSD",
                "base": "XBT",
                "quote": "USD",
                "status": "online",
                "price_precision": 1,
                "qty_precision": 0,
                "qty_min": 1,
                "qty_increment": 1,
                "price_increment": 0.5
            },
            {
                "symbol": "PF_XBTUSD",
                "base": "XBT",
                "quote": "USD",
                "status": "online",
                "price_precision": 0,
                "qty_precision": 4,
                "qty_min": 0.0001,
                "qty_increment": 0.0001,
                "price_increment": 1
            },
            {
                "symbol": "FF_ETHUSD_260925",
                "base": "ETH",
                "quote": "USD",
                "status": "online",
                "price_precision": 1,
                "qty_precision": 3,
                "qty_min": 0.001,
                "qty_increment": 0.001,
                "price_increment": 0.1
            },
            {
                "symbol": "FI_XRPUSD_260626",
                "base": "XRP",
                "quote": "USD",
                "status": "online",
                "price_precision": 4,
                "qty_precision": 0,
                "qty_min": 1,
                "qty_increment": 1,
                "price_increment": 0.0001
            },
            {
                "symbol": "OF_XBTUSD_260925_106000_C",
                "base": "XBT",
                "quote": "USD",
                "status": "online",
                "price_precision": 0,
                "qty_precision": 1,
                "qty_min": 0.1,
                "qty_increment": 0.1,
                "price_increment": 1
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
             "id": "XBT",
             "status": "enabled",
             "precision": 10,
             "precision_display": 5,
             "borrowable": true,
             "collateral_value": 0.99,
             "margin_rate": 0.01
          }
       ],
       "pairs": [
          {
             "symbol": "PI_XBTUSD",
             "base": "XBT",
             "quote": "USD",
             "status": "online",
             "price_precision": 1,
             "qty_precision": 0,
             "qty_min": 1,
             "qty_increment": 1,
             "price_increment": 0.5
          }
       ]
    }
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "instrument",
        "asset_class": "derivatives"
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
