---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/trade
api_type: WebSocket
updated_at: 2026-05-27 20:10:43.678188
---

# Trade

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    trade

Trade feed for a currency pair.

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

**Value:** `trade`

        ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "subscribe",  
      "pair": [  
        "XBT/EUR"  
      ],  
      "subscription": {  
        "name": "trade"  
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

**[1] trades** array [

A list of trades.

**[many] trade** array [

**[0] price** string

Price.

**[1] volume** string

Volume.

**[2] time** string

Time, seconds since epoch.

**[3] side** string

**Possible values:**[`buy`, `sell`] 

Taker side.

**[4] order_type** string

**Possible values:**[`market`, `limit`] 

Taker order type.

**[5] misc** string

Miscellaneous.

]

]

**[2] pair** string

**Example:** "BTC/USD"

The symbol of the currency pair.

**[3] channel_name** string

**Value:** `trade`

The name of the channel.

]
    
    
    [  
      0,  
      [  
        [  
          "5541.20000",  
          "0.15850568",  
          "1534614057.321597",  
          "s",  
          "l",  
          ""  
        ],  
        [  
          "6060.00000",  
          "0.02455000",  
          "1534614057.324998",  
          "b",  
          "l",  
          ""  
        ]  
      ],  
      "trade",  
      "XBT/USD"  
    ]