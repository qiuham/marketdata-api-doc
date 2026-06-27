---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/ticker
api_type: WebSocket
updated_at: 2026-05-27 20:10:36.431372
---

# Ticker (Level 1)

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    ticker

Ticker information on currency pair.

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

**Value:** `ticker`

        ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "subscribe",  
      "pair": [  
        "XBT/EUR"  
      ],  
      "subscription": {  
        "name": "ticker"  
      }  
    }  
    

## Subscription Snapshot and Update Response

  * Response Schema
  * Example

### MESSAGE BODY

****array [

**[0] channel_id** integer deprecated

**Deprecated Usage:** Use 'channel_name' and 'pair'.

Channel identifier.

**[1] ticker** object

**a** `array [`

Best Ask 

**[0] price** string

Best ask price.

**[1] whole_lot_volume** integer

Whole lot volume.

**[2] decimal** string

Lot volume

]

    ↳ **b** `array [`

Best Bid 

**[0] price** string

Best bid price.

**[1] whole_lot_volume** integer

Whole lot volume.

**[2] decimal** string

Lot volume

]

        ↳ **c** `array [`

Close 

**[0] price** string

Price.

**[1] lot_volume** string

Lot volume

]

            ↳ **v** `array [`

Volume 

**[0] today** string

Value today.

**[1] last_24h** string

Value over last 24 hours

]

                ↳ **p** `array [`

Volume Weighted Average Price 

**[0] today** string

Value today.

**[1] last_24h** string

Value over last 24 hours

]

                    ↳ **t** `array [`

Number of trades 

**[0] today** integer

Value today.

**[1] last_24h** integer

Value over last 24 hours

]

                        ↳ **l** `array [`

Low price 

**[0] today** string

Value today.

**[1] last_24h** string

Value over last 24 hours

]

                            ↳ **h** `array [`

High price 

**[0] today** string

Value today.

**[1] last_24h** string

Value over last 24 hours

]

                                ↳ **o** `array [`

Open Price 

**[0] today** string

Value today.

**[1] last_24h** string

Value over last 24 hours

]

**[2] pair** string

**Example:** "BTC/USD"

The symbol of the currency pair.

**[3] channel_name** string

**Value:** `ticker`

The name of the channel.

]
    
    
    [  
      0,  
      {  
        "a": [  
          "5525.40000",  
          1,  
          "1.000"  
        ],  
        "b": [  
          "5525.10000",  
          1,  
          "1.000"  
        ],  
        "c": [  
          "5525.10000",  
          "0.00398963"  
        ],  
        "h": [  
          "5783.00000",  
          "5783.00000"  
        ],  
        "l": [  
          "5505.00000",  
          "5505.00000"  
        ],  
        "o": [  
          "5760.70000",  
          "5763.40000"  
        ],  
        "p": [  
          "5631.44067",  
          "5653.78939"  
        ],  
        "t": [  
          11493,  
          16267  
        ],  
        "v": [  
          "2634.11501494",  
          "3591.17907851"  
        ]  
      },  
      "ticker",  
      "XBT/USD"  
    ]