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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/trade'
updated_at: 2026-11-13
---

# Trades

> Subscribe to real-time trade events when orders are matched in the book

WSS
ws.kraken.com/v2
trade

The `trade` channel generates a trade event when orders are matched in the book.

Multiple trades may be batched in a single message but that does not mean that these trades resulted from a single taker order.

The feed accepts a list of symbols for subscription.

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
> Value: `trade`
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
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
> Value: `trade`
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The currency pair associated with this subscription.
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

The snapshot and update responses share the same schema. An update message is streamed on a trade event.

The snapshot reflects the most recent 50 trades.

**channel** `string`

Value: `trade`

**type** `string`

One of: `snapshot`, `update`

**data** `object[]`

A list of trade events.

**properties**

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**side** `string`

The side of the taker order.

**qty** `float`

Size of the trade.

**price** `float`

Average price of the trade.

**ord\_type** `string`

One of: `limit`, `market`

The order type of the taker order.

**trade\_id** `integer`

Trade identifier is a sequence number, unique per book.

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

The book order update timestamp.

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
> Value: `trade`
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
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
> Value: `trade`
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The currency pair associated with this subscription.
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
        "channel": "trade",
        "symbol": [
            "MATIC/USD"
        ],
        "snapshot": true
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "trade",
        "snapshot": true,
        "symbol": "MATIC/USD"
    },
    "success": true,
    "time_in": "2023-09-25T09:21:10.428340Z",
    "time_out": "2023-09-25T09:21:10.428375Z"
}
```

```json Snapshot theme={null}
{
    "channel": "trade",
    "type": "snapshot",
    "data": [
        {
            "symbol": "MATIC/USD",
            "side": "buy",
            "price": 0.5147,
            "qty": 6423.46326,
            "ord_type": "limit",
            "trade_id": 4665846,
            "timestamp": "2023-09-25T07:48:36.925533Z"
        },
        {
            "symbol": "MATIC/USD",
            "side": "buy",
            "price": 0.5147,
            "qty": 1136.19677815,
            "ord_type": "limit",
            "trade_id": 4665847,
            "timestamp": "2023-09-25T07:49:36.925603Z"
        }
    ]
}
```

```json Update theme={null}
{
    "channel": "trade",
    "type": "update",
    "data": [
        {
            "symbol": "MATIC/USD",
            "side": "sell",
            "price": 0.5117,
            "qty": 40.0,
            "ord_type": "market",
            "trade_id": 4665906,
            "timestamp": "2023-09-25T07:49:37.708706Z"
        }
    ]
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "trade",
        "symbol": [
            "MATIC/USD"
        ],
        "snapshot": true
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "trade",
        "symbol": "MATIC/USD"
    },
    "success": true,
    "time_in": "2023-09-25T09:21:10.428340Z",
    "time_out": "2023-09-25T09:21:10.428375Z"
}
```
