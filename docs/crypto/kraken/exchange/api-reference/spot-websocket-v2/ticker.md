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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/ticker'
updated_at: 2026-11-13
---

# Ticker

> Subscribe to level 1 market data (top of book and recent trades)

WSS
ws.kraken.com/v2
ticker

The `ticker` channel streams level 1 market data, i.e. top of the book (best bid/offer) and recent trade data.

The feed accepts a list of symbols for subscription and the updates are generated on trade events.

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
> Value: `ticker`
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **event\_trigger** `string`
>
> One of: `bbo`, `trades`\\
>
> Default: `trades`
>
> The book event that causes a new ticker update to be published on the channel.
>
> * `bbo`: on a change in the best-bid-offer price levels.
> * `trades`: on every trade.
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
> Value: `ticker`
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The currency pair associated with this subscription.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`
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

**channel** `string`

Value: `ticker`

**type** `string`

One of: `snapshot`, `update`

**data** `object[]`

**properties**

**ask** `float`

Best ask price.

**ask\_qty** `float`

Best ask quantity.

**bid** `float`

Best bid price.

**bid\_qty** `float`

Best bid quantity.

**change** `float`

24-hour price change (in quote currency).

**change\_pct** `float`

24-hour price change (in percentage points).

**high** `float`

24-hour highest trade price.

**last** `float`

Last traded price (only guaranteed if traded within the past 24 hours).

**low** `float`

24-hour lowest trade price.

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

The ticker data timestamp.

**volume** `float`

24-hour traded volume (in base currency terms).

**vwap** `float`

24-hour volume weighted average price.

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
> Value: `ticker`
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **event\_trigger** `string`
>
> One of: `bbo`, `trades`\\
>
> Default: `trades`
>
> The book event that causes a new ticker update to be published on the channel.
>
> * `bbo`: on a change in the best-bid-offer price levels.
> * `trades`: on every trade.
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
> Value: `ticker`
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The currency pair associated with this subscription.
>
> **event\_trigger** `string`
>
> One of: `bbo`, `trades`\\
>
> Default: `trades`
>
> The book event that causes a new ticker update to be published on the channel.
>
> * `bbo`: on a change in the best-bid-offer price levels.
> * `trades`: on every trade.
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
        "channel": "ticker",
        "symbol": [
            "ALGO/USD"
        ]
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "ticker",
        "snapshot": true,
        "symbol": "ALGO/USD"
    },
    "success": true,
    "time_in": "2023-09-25T09:04:31.742599Z",
    "time_out": "2023-09-25T09:04:31.742648Z"
}
```

```json Snapshot theme={null}
{
    "channel": "ticker",
    "type": "snapshot",
    "data": [
        {
            "symbol": "ALGO/USD",
            "bid": 0.10025,
            "bid_qty": 740.0,
            "ask": 0.10036,
            "ask_qty": 1361.44813783,
            "last": 0.10035,
            "volume": 997038.98383185,
            "vwap": 0.10148,
            "low": 0.09979,
            "high": 0.10285,
            "change": -0.00017,
            "change_pct": -0.17,
            "timestamp": "2023-09-25T09:04:31.742648Z"
        }
    ]
}
```

```json Update theme={null}
{
    "channel": "ticker",
    "type": "update",
    "data": [
        {
            "symbol": "ALGO/USD",
            "bid": 0.10025,
            "bid_qty": 740.0,
            "ask": 0.10035,
            "ask_qty": 740.0,
            "last": 0.10035,
            "volume": 997038.98383185,
            "vwap": 0.10148,
            "low": 0.09979,
            "high": 0.10285,
            "change": -0.00017,
            "change_pct": -0.17,
            "timestamp": "2023-09-25T09:04:31.742648Z"
        }
    ]
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "ticker",
        "symbol": [
            "ALGO/USD"
        ]
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "ticker",
        "event_trigger": "trades",
        "symbol": "ALGO/USD"
    },
    "success": true,
    "time_in": "2023-09-25T09:04:31.742599Z",
    "time_out": "2023-09-25T09:04:31.742648Z"
}
```
