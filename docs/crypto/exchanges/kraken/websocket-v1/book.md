---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/book
api_type: WebSocket
updated_at: 2026-05-27 20:09:03.163892
---

# Book (Level 2)

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    book

Order book levels. On subscription, a snapshot will be published at the specified depth, following the snapshot, level updates will be published

## Subscription Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `subscribe`

**pair** `array of strings` *required*

**Example:**["BTC/USD", "MATIC/GBP"]

The currency pairs for this request.

    ↳ **subscription** `object`

        ↳ **name** `string` *required*

**Value:** `book`

        ↳ **depth** `integer`

**Possible values:**[`10`, ` 25`, ` 100`, ` 500`, ` 1000`] 

**Default value:**`10`

Specifies the number of price levels (in each side of the book) to be received.

        ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "subscribe",  
      "pair": [  
        "XBT/USD",  
        "XBT/EUR"  
      ],  
      "subscription": {  
        "name": "book"  
      }  
    }  
    

## Subscription Snapshot and Update Response

Note, there is no checksum on the snapshot.

  * Response Schema
  * Example

### MESSAGE BODY

****array [

**[0] channel_id** integer deprecated

**Deprecated Usage:** Use 'channel_name' and 'pair'.

Channel identifier.

**[1] book** object

**as** `array [`

Ask price levels, ascending from best ask.

**[many] level** array [

**[0] price** string

The price of this level.

**[1] volume** string

Price level volume, for updates volume = 0 for level removal/deletion

**[2] timestamp** string

**Format:** Epoch Seconds

**Example:** 1534614248.456738

Timestamp when the level 
]

]

    ↳ **bs** `array [`

Bid price levels, ascending from best bid.

**[many] level** array [

**[0] price** string

Price level

**[1] volume** string

Price level volume, for updates volume = 0 for level removal/deletion

**[2] timestamp** string

**Format:** Epoch Seconds

**Example:** 1534614248.456738

Timestamp when the level 
]

]

**[2] pair** string

**Example:** "BTC/USD"

The symbol of the currency pair.

**[3] channel_name** string

**Value:** `book-[depth]`

The name of the channel.

]
    
    
    [  
      0,  
      {  
        "as": [  
          [  
            "5541.30000",  
            "2.50700000",  
            "1534614248.123678"  
          ],  
          [  
            "5541.80000",  
            "0.33000000",  
            "1534614098.345543"  
          ],  
          [  
            "5542.70000",  
            "0.64700000",  
            "1534614244.654432"  
          ]  
        ],  
        "bs": [  
          [  
            "5541.20000",  
            "1.52900000",  
            "1534614248.765567"  
          ],  
          [  
            "5539.90000",  
            "0.30000000",  
            "1534614241.769870"  
          ],  
          [  
            "5539.50000",  
            "5.00000000",  
            "1534613831.243486"  
          ]  
        ]  
      },  
      "book-100",  
      "XBT/USD"  
    ]  
    

## Update Response

  * Response Schema
  * Example: Asks
  * Example: Bids
  * Example: Bids and asks
  * Example: Republish

### MESSAGE BODY

****array [

**[0] channel_id** integer deprecated

**Deprecated Usage:** Use 'channel_name' and 'pair'.

Channel identifier.

**[1] book** object

**a** `array [`

Ask price levels.

**[many] level** array [

**[0] price** string

The price for this level.

**[1] volume** string

The cumulative volume at this price level. If volume is 0, remove level from book.

**[2] timestamp** string

**Format:** Epoch Seconds

**Example:** 1534614248.456738

Timestamp when the level was 
**[3] update_type** string conditional

**Condition:** Republish only. 

**Value:** `r`

]

    ↳ **c** `string` *conditional*

**Condition:** Only present on last update. 

**Example:** "4088505763"

Book checksum as a quoted unsigned 32-bit integer.

]

    ↳ **b** `array [`

Bid price levels.

**[many] level** array [

**[0] price** string

The price for this level.

**[1] volume** string

The cumulative volume at this price level. If volume is 0, remove level from book.

**[2] timestamp** string

**Format:** Epoch Seconds

**Example:** 1534614248.456738

Timestamp when the level was 
**[3] update_type** string conditional

**Condition:** Republish only. 

**Value:** `r`

]

        ↳ **c** `string` *conditional*

**Condition:** Only present on last update. 

**Example:** "4088505763"

Book checksum as a quoted unsigned 32-bit integer.

]

**[2] pair** string

**Example:** "BTC/USD"

The symbol of the currency pair.

**[3] channel_name** string

**Value:** `book-[depth]`

The name of the channel.

]
    
    
    [  
      1234,  
      {  
        "a": [  
          [  
            "5541.30000",  
            "2.50700000",  
            "1534614248.456738"  
          ],  
          [  
            "5542.50000",  
            "0.40100000",  
            "1534614248.456738"  
          ]  
        ],  
        "c": "974942666"  
      },  
      "book-10",  
      "XBT/USD"  
    ]  
    
    
    
    [  
      1234,  
      {  
        "b": [  
          [  
            "5541.30000",  
            "0.00000000",  
            "1534614335.345903"  
          ]  
        ],  
        "c": "974942666"  
      },  
      "book-10",  
      "XBT/USD"  
    ]  
    
    
    
    [  
      1234,  
      {  
        "a": [  
          [  
            "5541.30000",  
            "2.50700000",  
            "1534614248.456738"  
          ],  
          [  
            "5542.50000",  
            "0.40100000",  
            "1534614248.456738"  
          ]  
        ]  
      },  
      {  
        "b": [  
          [  
            "5541.30000",  
            "0.00000000",  
            "1534614335.345903"  
          ]  
        ],  
        "c": "974942666"  
      },  
      "book-10",  
      "XBT/USD"  
    ]  
    
    
    
    [  
      1234,  
      {  
        "a": [  
          [  
            "5541.30000",  
            "2.50700000",  
            "1534614248.456738",  
            "r"  
          ],  
          [  
            "5542.50000",  
            "0.40100000",  
            "1534614248.456738",  
            "r"  
          ]  
        ],  
        "c": "974942666"  
      },  
      "book-25",  
      "XBT/USD"  
    ]