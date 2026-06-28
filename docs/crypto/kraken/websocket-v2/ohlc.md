---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/ohlc
api_type: WebSocket
updated_at: 2026-05-27 20:12:38.061852
---

# Candles (OHLC)

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    ohlc

The `ohlc` channel streams the Open, High, Low and Close (OHLC) data for the specific interval period.

The feed accepts a list symbols for subscription and the updates are generated on trade events.

## Subscribe Request

There is an acknowledgement response for each symbol in the subscription list.

  * Subscribe Schema
  * Subscribe Ack Schema
  * Example: Subscribe
  * Example: Subscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `ohlc`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **interval** `integer`

**Possible values:**[`1`, ` 5`, ` 15`, ` 30`, ` 60`, ` 240`, ` 1440`, ` 10080`, ` 21600`] 

The interval timeframe in minutes.

        ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

Request a snapshot after subscribing.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `ohlc`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

    ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if a snapshot is requested.

    ↳ **warnings** `array of strings`

An advisory message, highlighting deprecated fields or upcoming changes to the channel.

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**error** `string` *conditional*

**Condition:** If success is false. 

Error message.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the subscription was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "subscribe",  
        "params": {  
            "channel": "ohlc",  
            "symbol": [  
                "ALGO/USD",  
                "MATIC/USD"  
            ],  
            "interval": 5  
        }  
    }  
    
    
    
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
    

## Snapshot and Update Response

The snapshot and update responses share the same schema. An update message is streamed on a trade event.

  * Response Schema
  * Example: Snapshot
  * Example: Update

### MESSAGE BODY

**channel** `string`

**Value:** `ohlc`

**type** `string`

**Possible values:**[`snapshot`, ` update`] 

**data** `array [`

A list of candle events.

**[many] candle** object

    ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

    ↳ **open** `float`

The opening trade price within the interval.

    ↳ **high** `float`

The highest trade price within the interval.

    ↳ **low** `float`

The lowest trade price within the interval.

    ↳ **close** `float`

The last trade price within the interval.

    ↳ **vwap** `float`

Volume weighted average trade price within the interval.

    ↳ **trades** `float`

Number of trades within the interval.

    ↳ **volume** `float`

Total traded volume (in base currency terms) within the interval.

    ↳ **interval_begin** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp of start of the interval.

    ↳ **interval** `integer`

The timeframe from the interval in minutes.

    ↳ **timestamp** `string deprecated`

**Deprecated Usage:** Use 'interval_begin'.

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp of start of the interval.

]
    
    
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
    

## Unsubscribe Request

There is an acknowledgement response for each symbol in the unsubscribe list.

  * Unsubscribe Schema
  * Unsubscribe Ack Schema
  * Example: Unsubscribe
  * Example: Unsubscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `ohlc`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **interval** `integer`

**Possible values:**[`1`, ` 5`, ` 15`, ` 30`, ` 60`, ` 240`, ` 1440`, ` 10080`, ` 21600`] 

The interval timeframe in minutes.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `ohlc`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**error** `string` *conditional*

**Condition:** If success is false. 

Error message.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the subscription was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "unsubscribe",  
        "params": {  
            "channel": "ohlc",  
            "symbol": [  
                "ALGO/USD",  
                "MATIC/USD"  
            ],  
            "interval": 5  
        }  
    }  
    
    
    
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