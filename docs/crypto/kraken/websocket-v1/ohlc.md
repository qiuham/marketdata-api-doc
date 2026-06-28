---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/ohlc
api_type: WebSocket
updated_at: 2026-05-27 20:09:46.112357
---

# Candles (OHLC)

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    ohlc

Open High Low Close (Candle) feed for a currency pair and interval period.

When subscribed for OHLC, a snapshot of the last valid candle (irrespective of the endtime) will be sent, followed by updates to the running candle. For example, if a subscription is made to 1 min candle and there have been no trades for 5 mins, a snapshot of the last 1 min candle from 5 mins ago will be published. The endtime can be used to determine that it is an old candle.

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

**Value:** `ohlc`

        ↳ **interval** `integer`

**Possible values:**[`1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600`] 

**Default value:**`1`

Time interval associated with ohlc subscription in minutes.

        ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "subscribe",  
      "pair": [  
        "XBT/EUR"  
      ],  
      "subscription": {  
        "interval": 5,  
        "name": "ohlc"  
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

**[1] ohlc** array [

The candle detail for a specific interval period. 

**[0] epoc_last** string

Candle last update time, in seconds since epoch

**[1] epoc_end** string

End time of interval, in seconds since epoch

**[2] open** string

Open price of interval

**[3] high** string

High price within interval

**[4] low** string

Low price within interval

**[5] close** string

Close price of interval

**[6] vwap** string

Volume weighted average price within interval

**[7] volume** string

Accumulated volume within interval

**[8] count** string

Number of trades within interval

]

**[2] pair** string

**Example:** "BTC/USD"

The symbol of the currency pair.

**[3] channel_name** string

**Value:** `ohlc-[depth]`

The name of the channel.

]
    
    
    [  
      42,  
      [  
        "1542057314.748456",  
        "1542057360.435743",  
        "3586.70000",  
        "3586.70000",  
        "3586.60000",  
        "3586.60000",  
        "3586.68894",  
        "0.03373000",  
        2  
      ],  
      "ohlc-5",  
      "XBT/USD"  
    ]