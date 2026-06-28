---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/spread
api_type: WebSocket
updated_at: 2026-05-27 20:10:14.893675
---

# Spreads

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    spread

Spread feed for a currency pair.

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

**Value:** `spread`

        ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "subscribe",  
      "pair": [  
        "XBT/EUR"  
      ],  
      "subscription": {  
        "name": "spread"  
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

**[1] spread** array [

**[0] bid** string

Bid price

**[1] ask** string

Ask price

**[2] timestamp** string

Time, seconds since epoch

**[3] bid_volume** string

Bid Volume

**[4] ask_volume** string

Ask Volume

]

**[2] pair** string

**Example:** "BTC/USD"

The symbol of the currency pair.

**[3] channel_name** string

**Value:** `spread`

The name of the channel.

]
    
    
    [  
      0,  
      [  
        "5698.40000",  
        "5700.00000",  
        "1542057299.545897",  
        "1.01234567",  
        "0.98765432"  
      ],  
      "spread",  
      "XBT/USD"  
    ]