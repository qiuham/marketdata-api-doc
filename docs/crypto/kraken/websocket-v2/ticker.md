---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/ticker
api_type: WebSocket
updated_at: 2026-05-27 20:12:59.524154
---

# Ticker (Level 1)

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    ticker

The `ticker` channel streams level 1 market data, i.e. top of the book (best bid/offer) and recent trade data.

The feed accepts a list symbols for subscription and the updates are generated on trade events.

## Subscribe Request

  * Subscribe Schema
  * Subscribe Ack Schema
  * Example: Subscribe
  * Example: Subscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `ticker`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **event_trigger** `string`

**Possible values:**[`bbo`, ` trades`] 

**Default value:**`trades`

The book event that causes a new ticker update to be published on the channel.

  * `bbo`: on a change in the best-bid-offer price levels.
  * `trades`: on every trade.

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

**Value:** `ticker`

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
            "channel": "ticker",  
            "symbol": [  
                "ALGO/USD"  
            ]  
        }  
    }  
    
    
    
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
    

## Snapshot / Update Response

The snapshot and update responses share the same schema. An update message is streamed on a trade event.

  * Snapshot / Update Schema
  * Example: Snapshot
  * Example: Update

### MESSAGE BODY

**channel** `string`

**Value:** `ticker`

**type** `string`

**Possible values:**[`snapshot`, ` update`] 

**data** `array [`

**[0] ticker** object

The ticker element is always the first and only item in the data payload. 

    ↳ **ask** `float`

Best ask price.

    ↳ **ask_qty** `float`

Best ask quantity.

    ↳ **bid** `float`

Best bid price.

    ↳ **bid_qty** `float`

Best bid quantity.

    ↳ **change** `float`

24-hour price change (in quote currency).

    ↳ **change_pct** `float`

24-hour price change (in percentage points).

    ↳ **high** `float`

24-hour highest trade price.

    ↳ **last** `float`

Last traded price (only guaranteed if traded within the past 24 hours).

    ↳ **low** `float`

24-hour lowest trade price.

    ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

    ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The ticker data timestamp.

    ↳ **volume** `float`

24-hour traded volume (in base currency terms).

    ↳ **vwap** `float`

24-hour volume weighted average price.

]
    
    
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
    

## Unsubscribe Request

  * Unsubscribe Schema
  * Unsubscribe Ack Schema
  * Example: Unsubscribe
  * Example: Unsubscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `ticker`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **event_trigger** `string`

**Possible values:**[`bbo`, ` trades`] 

**Default value:**`trades`

The book event that causes a new ticker update to be published on the channel.

  * `bbo`: on a change in the best-bid-offer price levels.
  * `trades`: on every trade.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `ticker`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

    ↳ **event_trigger** `string`

**Possible values:**[`bbo`, ` trades`] 

**Default value:**`trades`

The book event that causes a new ticker update to be published on the channel.

  * `bbo`: on a change in the best-bid-offer price levels.
  * `trades`: on every trade.

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
            "channel": "ticker",  
            "symbol": [  
                "ALGO/USD"  
            ]  
        }  
    }  
    
    
    
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