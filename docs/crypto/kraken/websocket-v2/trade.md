---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/trade
api_type: WebSocket
updated_at: 2026-05-27 20:13:06.681244
---

# Trades

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    trade

The `trade` channel generates a trade event when orders are matched in the book.

Multiple trades may be batched in a single message but that does not mean that these trades resulted from a single taker order.

The feed accepts a list symbols for subscription.

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

**Value:** `trade`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

Request a snapshot after subscribing.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `trade`

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
            "channel": "trade",  
            "symbol": [  
                "MATIC/USD"  
            ],  
            "snapshot": true  
        }  
    }  
    
    
    
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
    

## Snapshot and Update Response

The snapshot and update responses share the same schema. An update message is streamed on a trade event.

The snapshot reflects the most recent 50 trades.

  * Response Schema
  * Example: Snapshot
  * Example: Update

### MESSAGE BODY

**channel** `string`

**Value:** `trade`

**type** `string`

**Possible values:**[`snapshot`, ` update`] 

**data** `array [`

A list of trade events.

**[many] trade** object

    ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

    ↳ **side** `string`

The side of the taker order.

    ↳ **qty** `float`

Size of the trade.

    ↳ **price** `float`

Average price of the trade.

    ↳ **ord_type** `string`

**Possible values:**[`limit`, ` market`] 

The order type of the taker order.

    ↳ **trade_id** `integer`

Trade identifier is a sequence number, unique per book. 

    ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The book order update timestamp.

]
    
    
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

**Value:** `trade`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `trade`

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
            "channel": "trade",  
            "symbol": [  
                "MATIC/USD"  
            ],  
            "snapshot": true  
        }  
    }  
    
    
    
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