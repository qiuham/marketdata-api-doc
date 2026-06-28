---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/unsubscribe
api_type: WebSocket
updated_at: 2026-05-27 20:10:50.801514
---

# Unsubscribe

**WebSocket Endpoint:** `wss://ws.kraken.com`
    
    unsubscribe

Unsubscribe, can specify a channelID or multiple currency pairs.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `unsubscribe`

**pair** `array of strings` *conditional*

**Condition:** All channels which support pair subscriptions. 

**Example:**["BTC/USD", "MATIC/GBP"]

Unsubscribe to specific pairs.

    ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.

    ↳ **subscription** `object`

        ↳ **name** `string` *required*

**Possible values:**[`book`, `ohlc`, `openOrders`, `ownTrades`, `spread`, `ticker`, `trade`, `*`] 

The name of the channel to unsubscribe. Wildcard "*" is supported. 

        ↳ **depth** `integer` *conditional*

**Condition:** 'book' channel only. 

Unsubscribe to a specific depth.

        ↳ **interval** `integer` *conditional*

**Condition:** 'ohlc' channel only. 

Unsubscribe to a specific interval.
    
    
    {  
      "event": "unsubscribe",  
      "pair": [  
        "XBT/EUR",  
        "XBT/USD"  
      ],  
      "subscription": {  
        "name": "ticker"  
      }  
    }