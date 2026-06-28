---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/book
api_type: WebSocket
updated_at: 2026-05-27 20:11:33.771272
---

# Book (Level 2)

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    book

The `book` channel streams level 2 (L2) order book. It describes the individual price levels in the book with aggregated order quantities at each level.

Subscriptions to this channel can be made for multiple symbols at once by specifying a list of pairs in the `symbol`.

For more detail on maintaining the order book and generating a checksum, see [guide](/api/docs/guides/spot-ws-book-v2).

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

**Value:** `book`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **depth** `integer`

**Possible values:**[`10`, ` 25`, ` 100`, ` 500`, ` 1000`] 

**Default value:**`10`

The number of price levels to be received.

        ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

Request a snapshot after subscribing.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

There is an separate acknowledgement response for each symbol in the subscription list.

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `book`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

    ↳ **depth** `integer`

**Possible values:**[`10`, ` 25`, ` 100`, ` 500`, ` 1000`] 

Specifies the number of price levels (in each side of the book) to be received.

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
            "channel": "book",  
            "symbol": [  
                "ALGO/USD",  
                "MATIC/USD"  
            ]  
        }  
    }  
    
    
    
    {  
        "method": "subscribe",  
        "result": {  
            "channel": "book",  
            "depth": 10,  
            "snapshot": true,  
            "symbol": "ALGO/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T17:35:55.219022Z",  
        "time_out": "2023-10-06T17:35:55.219067Z"  
    }  
      
    {  
        "method": "subscribe",  
        "result": {  
            "channel": "book",  
            "depth": 10,  
            "snapshot": true,  
            "symbol": "MATIC/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T17:35:55.219022Z",  
        "time_out": "2023-10-06T17:35:55.219067Z"  
    }  
    

## Snapshot Response

  * Snapshot Schema
  * Example

The returned snapshot data contains the specified number of bids and asks for the symbol including a CRC32 checksum of the top 10 bids and asks.

### MESSAGE BODY

**channel** `string`

**Value:** `book`

**type** `string`

**Value:** `snapshot`

**data** `array [`

**[0] book** object

The book element is always the first and only item in the data payload.

    ↳ **asks** `array [`

**[many] level** object

        ↳ **price** `float`

The ask price.

        ↳ **qty** `float`

The ask quantity.

]

        ↳ **bids** `array [`

**[many] level** object

            ↳ **price** `float`

The bid price.

            ↳ **qty** `float`

The bid quantity.

]

            ↳ **checksum** `integer`

CRC32 checksum for the top 10 bids and asks.

            ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

            ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp of the order book snapshot.

]
    
    
    {  
        "channel": "book",  
        "type": "snapshot",  
        "data": [  
            {  
                "symbol": "MATIC/USD",  
                "bids": [  
                    {  
                        "price": 0.5666,  
                        "qty": 4831.75496356  
                    },  
                    {  
                        "price": 0.5665,  
                        "qty": 6658.22734739  
                    },  
                    {  
                        "price": 0.5664,  
                        "qty": 18724.91513344  
                    },  
                    {  
                        "price": 0.5663,  
                        "qty": 11563.92544914  
                    },  
                    {  
                        "price": 0.5662,  
                        "qty": 14006.65365711  
                    },  
                    {  
                        "price": 0.5661,  
                        "qty": 17454.85679807  
                    },  
                    {  
                        "price": 0.566,  
                        "qty": 18097.1547  
                    },  
                    {  
                        "price": 0.5659,  
                        "qty": 33644.89175666  
                    },  
                    {  
                        "price": 0.5658,  
                        "qty": 148.3464  
                    },  
                    {  
                        "price": 0.5657,  
                        "qty": 606.70854372  
                    }  
                ],  
                "asks": [  
                    {  
                        "price": 0.5668,  
                        "qty": 4410.79769741  
                    },  
                    {  
                        "price": 0.5669,  
                        "qty": 4655.40412487  
                    },  
                    {  
                        "price": 0.567,  
                        "qty": 49844.89424998  
                    },  
                    {  
                        "price": 0.5671,  
                        "qty": 24306.41678  
                    },  
                    {  
                        "price": 0.5672,  
                        "qty": 29783.25223475  
                    },  
                    {  
                        "price": 0.5673,  
                        "qty": 57234.71239278  
                    },  
                    {  
                        "price": 0.5674,  
                        "qty": 45065.04744  
                    },  
                    {  
                        "price": 0.5675,  
                        "qty": 5912.76380354  
                    },  
                    {  
                        "price": 0.5676,  
                        "qty": 42514.92434778  
                    },  
                    {  
                        "price": 0.5677,  
                        "qty": 36304.0847022  
                    }  
                ],  
                "checksum": 2439117997,  
                "timestamp": "2023-10-06T17:35:55.440295Z"  
            }  
        ]  
    }  
    

## Update Response

The data contains the updates of the bids and asks for the relevant symbol including a CRC32 checksum of the top 10 bids and asks.

Note, it is possible to have multiple updates to the same price level in a single update message. Updates should always be processed in sequence.

  * Update Schema
  * Example

### MESSAGE BODY

**channel** `string`

**Value:** `book`

**type** `string`

**Value:** `update`

**data** `array [`

**[0] book** object

The book element is always the first and only item in the data payload.

    ↳ **asks** `array [`

**[many] level** object

        ↳ **price** `float`

The ask price.

        ↳ **qty** `float`

The ask quantity.

]

        ↳ **bids** `array [`

**[many] level** object

            ↳ **price** `float`

The bid price.

            ↳ **qty** `float`

The bid quantity.

]

            ↳ **checksum** `integer`

CRC32 checksum for the top 10 bids and asks.

            ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

            ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The book order update timestamp.

]
    
    
    {  
        "channel": "book",  
        "type": "update",  
        "data": [  
            {  
                "symbol": "MATIC/USD",  
                "bids": [  
                    {  
                        "price": 0.5657,  
                        "qty": 1098.3947558  
                    }  
                ],  
                "asks": [],  
                "checksum": 2114181697,  
                "timestamp": "2023-10-06T17:35:55.440295Z"  
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

**Value:** `book`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **depth** `integer`

**Possible values:**[`10`, ` 25`, ` 100`, ` 500`, ` 1000`] 

The number of price levels to be unsubscribed.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

There is an separate acknowledgement response for each symbol in the unsubscription list.

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `book`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

    ↳ **depth** `integer`

**Possible values:**[`10`, ` 25`, ` 100`, ` 500`, ` 1000`] 

Specifies the number of price levels (in each side of the book) to be unsubscribed.

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
            "channel": "book",  
            "symbol": [  
                "ALGO/USD",  
                "MATIC/USD"  
            ]  
        }  
    }  
    
    
    
    {  
        "method": "unsubscribe",  
        "result": {  
            "channel": "book",  
            "depth": 10,  
            "snapshot": true,  
            "symbol": "ALGO/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T17:35:55.219022Z",  
        "time_out": "2023-10-06T17:35:55.219067Z"  
    }  
      
    {  
        "method": "unsubscribe",  
        "result": {  
            "channel": "book",  
            "depth": 10,  
            "snapshot": true,  
            "symbol": "MATIC/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T17:35:55.219022Z",  
        "time_out": "2023-10-06T17:35:55.219067Z"  
    }