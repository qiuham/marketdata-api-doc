---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/level3
api_type: WebSocket
updated_at: 2026-05-27 20:12:31.135985
---

# Orders (Level 3)

CHANNEL
**Endpoint:** `wss://ws-l3.kraken.com/v2`
    level3Authentication Required

## Summary

The `level3` channel has an additional level of granularity over the `book` channel, it provides visibility of individual orders in the book.

L3 shows orders resting in the visible order book and it will never be crossed (i.e. no overlapping buy and sell orders). This feed excludes:

  * In-flight orders.
  * Unmatched market orders.
  * Untriggered stop-loss and take-profit orders.
  * Hidden quantity of iceberg orders.

For more detail on maintaining the order book and generating a checksum, see [guide](/api/docs/guides/spot-ws-l3-v2).

## Subscription limits

The `level3` channel is authenticated (i.e. it requires an API token to subscribe) and there are restrictions of the number of symbols and the subscription rate.

  * The total number of symbols per websocket connection is `200`. A client can open multiple websockets connections to increase symbol coverage.
  * The subscription rate determined by client tier and order book depth. Standard rate count limit per second is `200` and the pro limit is `500`.
  * The counter increase per book depth subscription is given in the table below.

Order Book Depth| Rate Counter Increase per Symbol  
---|---  
10| 5  
100| 25  
1000| 100  
  
**Example: ** Pro client can subscribe to 100 symbols of 10 depth every second.

## Subscribe Request

Only one subscription to one depth level per symbol is supported, i.e. cannot subscribe to 10 levels and 1000 levels of "BTC/USD".

  * Subscribe Schema
  * Subscribe Ack Schema
  * Example: Subscribe
  * Example: Subscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `level3`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **depth** `integer`

**Possible values:**[`10`, ` 100`, ` 1000`] 

**Default value:**`10`

The number of price levels to be received.

        ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

Request a snapshot after subscribing.

        ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

There is an separate acknowledgement response for each symbol in the subscription list.

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `level3`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

    ↳ **depth** `integer`

**Possible values:**[`10`, ` 100`, ` 1000`] 

The number of price levels to be received.

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
            "channel": "level3",  
            "symbol": [  
                "ALGO/USD",  
                "MATIC/USD"  
            ],  
            "snapshot": true,  
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"  
        }  
    }  
    
    
    
    {  
        "method": "subscribe",  
        "result": {  
            "channel": "level3",  
            "snapshot": true,  
            "symbol": "ALGO/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T18:20:56.506266Z",  
        "time_out": "2023-10-06T18:20:56.521803Z"  
    }  
      
    {  
        "method": "subscribe",  
        "result": {  
            "channel": "level3",  
            "snapshot": true,  
            "symbol": "MATIC/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T18:20:56.506266Z",  
        "time_out": "2023-10-06T18:20:56.521859Z"  
    }  
    

## Snapshot Response

  * Snapshot Response
  * Example: Snapshot

### MESSAGE BODY

**channel** `string`

**Value:** `level3`

**type** `string`

**Value:** `snapshot`

**data** `array [`

**[0] book** object

The book element is always the first and only item in the data payload. 

    ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

    ↳ **bids** `array [`

A list of buy orders posted in the book.

**[many] order** object

        ↳ **order_id** `string`

The Kraken order identifier of the order in the book

        ↳ **limit_price** `float`

Limit price of the order

        ↳ **order_qty** `float`

The remaining order quantity visible in the book

        ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456789Z

The time the order was inserted or amended.

]

        ↳ **asks** `array [`

A list of sell orders posted in the book.

**[many] order** object

            ↳ **order_id** `string`

The Kraken order identifier of the order in the book

            ↳ **limit_price** `float`

Limit price of the order

            ↳ **order_qty** `float`

The remaining order quantity visible in the book

            ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456789Z

The time the order was inserted or amended.

]

            ↳ **checksum** `integer`

CRC32 checksum for the top 10 price levels on both sides.

            ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456789Z

The time this market data message was generated in the matching engine.

]
    
    
    {  
        "channel": "level3",  
        "type": "snapshot",  
        "data": [  
            {  
                "symbol": "MATIC/USD",  
                "checksum": 281817320,  
                "bids": [  
                    {  
                        "order_id": "O6ZQNQ-BXL4E-5WGINO",  
                        "limit_price": 0.5629,  
                        "order_qty": 111.56125344,  
                        "timestamp": "2023-10-06T17:35:00.279389650Z"  
                    },  
                    {  
                        "order_id": "OEP26Y-YAFEF-OFR62B",  
                        "limit_price": 0.5625,  
                        "order_qty": 6390.19338,  
                        "timestamp": "2023-10-06T18:19:55.056070105Z"  
                    },  
                    {  
                        "order_id": "OKNAY7-67JRK-AIZ4JO",  
                        "limit_price": 0.5625,  
                        "order_qty": 14084.5,  
                        "timestamp": "2023-10-06T18:20:55.357467423Z"  
                    }  
                ],  
                "asks": [  
                    {  
                        "order_id": "OLLSXO-HDMT3-BUOKEI",  
                        "limit_price": 0.563,  
                        "order_qty": 4422.9978357,  
                        "timestamp": "2023-10-06T18:18:20.734897896Z"  
                    },  
                    {  
                        "order_id": "O5SR5W-L7OLY-BLDEJV",  
                        "limit_price": 0.563,  
                        "order_qty": 420.0,  
                        "timestamp": "2023-10-06T18:18:20.738706230Z"  
                    },  
                    {  
                        "order_id": "OXV6QS-2GG4Q-F4EECM",  
                        "limit_price": 0.563,  
                        "order_qty": 490.0,  
                        "timestamp": "2023-10-06T18:18:21.064657206Z"  
                    }  
                ]  
            }  
        ]  
    }  
    

## Update Response

  * The updates will be streamed following the initial snapshot, no sequencing is required.
  * The L3 channel is not throttled, updates will be provided in the real-time.
  * If a price level is removed from the subscribed levels (i.e. result of trades/cancels) then all orders in the next available level will generate an add event.

### Maintaining the book

After each update, the book should be truncated to your subscribed depth, there will be no `delete` event for price levels that fall out of scope. In other words, if you are subscribed with `depth` of 10 and an insert into the book results in 11 bids, you must remove the 11th worst bid.

  * Update Schema
  * Example

### MESSAGE BODY

**channel** `string`

**Value:** `level3`

**type** `string`

**Value:** `update`

**data** `array [`

**[0] book** object

The book element is always the first and only item in the data payload. 

    ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

    ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456789Z

The time this market data message was generated in the matching engine.

    ↳ **checksum** `integer`

CRC32 checksum for the top 10 price levels on both sides.

    ↳ **bids** `array [`

A list of order events to the bid side of book.

**[many] order_event** object

        ↳ **event** `string`

**Possible values:**[`add`, ` modify`, ` delete`] 

The type of order event for this update:
  * `add`: A new order added to the book.
  * `modify`: The order quantity has been modified, i.e. a fill.
  * `delete`: The order has been removed from the book, i.e. full fill or cancel.

        ↳ **order_id** `string`

The Kraken order identifier of the order in the book

        ↳ **limit_price** `float`

Limit price of the order

        ↳ **order_qty** `float`

The remaining order quantity visible in the book

        ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456789Z

The time the order was inserted or amended.

]

        ↳ **asks** `array [`

A list of order events to the ask side of book.

**[many] order_event** object

            ↳ **event** `string`

**Possible values:**[`add`, ` modify`, ` delete`] 

The type of order event for this update:
  * `add`: A new order added to the book.
  * `modify`: The order quantity has been modified, i.e. a fill.
  * `delete`: The order has been removed from the book, i.e. full fill or cancel.

            ↳ **order_id** `string`

The Kraken order identifier of the order in the book

            ↳ **limit_price** `float`

Limit price of the order

            ↳ **order_qty** `float`

The remaining order quantity visible in the book

            ↳ **timestamp** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456789Z

The time the order was inserted or amended.

]

]
    
    
    {  
        "channel": "level3",  
        "type": "update",  
        "data": [  
            {  
                "checksum": 2841398499,  
                "symbol": "MATIC/USD",  
                "bids": [],  
                "asks": [  
                    {  
                        "event": "delete",  
                        "order_id": "OOIATY-6EIWY-ACVIUN",  
                        "limit_price": 0.5636,  
                        "order_qty": 302.89736033,  
                        "timestamp": "2023-10-06T18:21:00.097010033Z"  
                    },  
                    {  
                        "event": "add",  
                        "order_id": "O2BN53-5RSB2-V3J57T",  
                        "limit_price": 0.564,  
                        "order_qty": 3500.77668626,  
                        "timestamp": "2023-10-06T18:20:27.383408052Z"  
                    },  
                    {  
                        "event": "add",  
                        "order_id": "OWG5ZU-LHUHH-BICPEX",  
                        "limit_price": 0.564,  
                        "order_qty": 22149.62881248,  
                        "timestamp": "2023-10-06T18:20:50.842854530Z"  
                    },  
                    {  
                        "event": "add",  
                        "order_id": "ONVDB3-2DRUF-Y6MF7D",  
                        "limit_price": 0.564,  
                        "order_qty": 42196.34088652,  
                        "timestamp": "2023-10-06T18:20:58.101850535Z"  
                    }  
                ]  
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

**Value:** `level3`

    ↳ **symbol** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

A list of currency pairs.

        ↳ **depth** `integer`

**Possible values:**[`10`, ` 100`, ` 1000`] 

**Default value:**`10`

The number of price levels to be received.

        ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

There is an separate acknowledgement response for each symbol in the unsubscribe request list.

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `level3`

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The currency pair associated with this subscription.

    ↳ **depth** `integer`

**Possible values:**[`10`, ` 100`, ` 1000`] 

The number of price levels to be unsubscribed.

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
            "channel": "level3",  
            "symbol": [  
                "ALGO/USD",  
                "MATIC/USD"  
            ],  
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"  
        }  
    }  
    
    
    
    {  
        "method": "unsubscribe",  
        "result": {  
            "channel": "level3",  
            "symbol": "ALGO/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T18:20:56.506266Z",  
        "time_out": "2023-10-06T18:20:56.521803Z"  
    }  
      
    {  
        "method": "unsubscribe",  
        "result": {  
            "channel": "level3",  
            "symbol": "MATIC/USD"  
        },  
        "success": true,  
        "time_in": "2023-10-06T18:20:56.506266Z",  
        "time_out": "2023-10-06T18:20:56.521859Z"  
    }