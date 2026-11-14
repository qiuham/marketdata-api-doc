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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/ohlc'
updated_at: 2026-11-13
---

# Candles (OHLC)

> Subscribe to Open, High, Low and Close (OHLC) candle data for specific interval periods

UWS
uws.kraken.com/v2/public
ohlc

The `ohlc` channel streams the Open, High, Low and Close (OHLC) data for the specific interval period.

The feed accepts a list of symbols for subscription and the updates are generated on trade events.

## Subscribe

There is an acknowledgement response for each symbol in the subscription list.

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
> Value: `ohlc`
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **interval** `integer`
>
> One of: `1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600`
>
> The interval timeframe in minutes.
>
> **tick\_type** `string`
>
> One of: `trade`, `mark`, `spot`\\
>
> Default: `trade`
>
> The candle type - specifically for Futures.
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
> Value: `ohlc`
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
> **interval** `integer`
>
> The requested OHLC interval in minutes.
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

Value: `ohlc`

**type** `string`

One of: `snapshot`, `update`

**data** `object[]`

A list of candle events.

**properties**

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**open** `float`

The opening trade price within the interval.

**high** `float`

The highest trade price within the interval.

**low** `float`

The lowest trade price within the interval.

**close** `float`

The last trade price within the interval.

**vwap** `float`

Volume weighted average trade price within the interval.

**trades** `integer`

Number of trades within the interval.

**volume** `float`

Total traded volume (in base currency terms) within the interval.

**interval\_begin** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

The timestamp of start of the interval.

**interval** `integer`

The timeframe from the interval in minutes.

**timestamp** `string` *deprecated*

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`\\

Deprecated: Use `interval_begin`

The timestamp of start of the interval.

## Unsubscribe

There is an acknowledgement response for each symbol in the unsubscribe list.

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
> Value: `ohlc`
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **interval** `integer`
>
> One of: `1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600`
>
> The interval timeframe in minutes.
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
> Value: `ohlc`
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
        "channel": "ohlc",
        "asset_class": "derivatives",
        "tick_type": "mark",
        "symbol": [
            "ALGO/USD",
            "MATIC/USD"
        ],
        "interval": 5
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "ohlc",
        "interval": 5,
        "snapshot": true,
        "symbol": "ALGO/USD",
        "warnings": [
            "timestamp is deprecated, use interval_begin"
        ]
    },
    "success": true,
    "time_in": "2023-10-04T16:26:01.802708Z",
    "time_out": "2023-10-04T16:26:01.802791Z"
}

{
    "method": "subscribe",
    "result": {
        "channel": "ohlc",
        "interval": 5,
        "snapshot": true,
        "symbol": "MATIC/USD",
        "warnings": [
            "timestamp is deprecated, use interval_begin"
        ]
    },
    "success": true,
    "time_in": "2023-10-04T16:26:01.802708Z",
    "time_out": "2023-10-04T16:26:01.802791Z"
}
```

```json Snapshot theme={null}
{
    "channel": "ohlc",
    "type": "snapshot",
    "timestamp": "2023-10-04T16:26:01.806315597Z",
    "data": [
        {
            "symbol": "ALGO/USD",
            "open": 0.09875,
            "high": 0.09875,
            "low": 0.09875,
            "close": 0.09875,
            "trades": 1,
            "volume": 201.86015,
            "vwap": 0.09875,
            "interval_begin": "2023-10-04T15:25:00.000000000Z",
            "interval": 5,
            "timestamp": "2023-10-04T15:30:00.000000Z"
        },
        {
            "symbol": "ALGO/USD",
            "open": 0.09875,
            "high": 0.0988,
            "low": 0.09875,
            "close": 0.09875,
            "trades": 13,
            "volume": 16255.46368,
            "vwap": 0.09879,
            "interval_begin": "2023-10-04T15:30:00.000000000Z",
            "interval": 5,
            "timestamp": "2023-10-04T15:35:00.000000Z"
        }
    ]
}
```

```json Update theme={null}
{
    "channel": "ohlc",
    "type": "update",
    "timestamp": "2023-10-04T16:26:30.524394914Z",
    "data": [
        {
            "symbol": "MATIC/USD",
            "open": 0.5624,
            "high": 0.5628,
            "low": 0.5622,
            "close": 0.5627,
            "trades": 12,
            "volume": 30927.68066226,
            "vwap": 0.5626,
            "interval_begin": "2023-10-04T16:25:00.000000000Z",
            "interval": 5,
            "timestamp": "2023-10-04T16:30:00.000000Z"
        }
    ]
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "ohlc",
        "asset_class": "derivatives",
        "symbol": [
            "ALGO/USD",
            "MATIC/USD"
        ],
        "interval": 5
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "ohlc",
        "interval": 5,
        "symbol": "ALGO/USD"
    },
    "success": true,
    "time_in": "2023-10-04T16:26:01.802708Z",
    "time_out": "2023-10-04T16:26:01.802791Z"
}

{
    "method": "unsubscribe",
    "result": {
        "channel": "ohlc",
        "interval": 5,
        "symbol": "MATIC/USD"
    },
    "success": true,
    "time_in": "2023-10-04T16:26:01.802708Z",
    "time_out": "2023-10-04T16:26:01.802791Z"
}
```
