---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/subscriptionstatus
api_type: WebSocket
updated_at: 2026-05-27 20:10:22.052015
---

# Subscription Status

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    subscriptionStatus

Subscription status response to subscribe, unsubscribe or exchange initiated unsubscribe.

## Payload

  * Response Schema
  * Example: Ticker
  * Example: OHLC
  * Example: ownTrades
  * Example: book

### MESSAGE BODY

**event** `string`

**Value:** `subscriptionStatus`

**channelName** string required

**Possible values:**[`book`, `ohlc`, `openOrders`, `ownTrades`, `spread`, `ticker`, `trade`, `*`] 

The name of the channel.

**pair** `string`

**Example:** "BTC/USD"

The currency pair associated with this subscription.

**status** `string`

**Possible values:**[`subscribed`, `unsubscribed`, `ok`, `error`] 

**subscription** `object`

    ↳ **depth** `integer` *conditional*

**Condition:** 'book' channel only. 

The book depth.

    ↳ **interval** `integer` *conditional*

**Condition:** 'ohlc' channel only. 

The ohlc interval.

    ↳ **maxratecount** `integer`

The rate counter.

    ↳ **name** `string` *required*

**Possible values:**[`book`, `ohlc`, `openOrders`, `ownTrades`, `spread`, `ticker`, `trade`, `*`] 

The name of the channel.

    ↳ **token** `string` *conditional*

**Condition:** Authenticated requests only. 

The authentication token associated with the request.

    ↳ **reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string conditional

**Condition:** Unsuccessful requests only. 

Error message for unsuccessful requests.

**channelID** integer

Channel ID on successful subscription, applicable to public messages only - deprecated, use channelName and pair.
    
    
    {  
      "channelID": 10001,  
      "channelName": "ticker",  
      "event": "subscriptionStatus",  
      "pair": "XBT/EUR",  
      "status": "subscribed",  
      "subscription": {  
        "name": "ticker"  
      }  
    }  
    
    
    
    {  
      "channelID": 10001,  
      "channelName": "ohlc-5",  
      "event": "subscriptionStatus",  
      "pair": "XBT/EUR",  
      "reqid": 42,  
      "status": "unsubscribed",  
      "subscription": {  
        "interval": 5,  
        "name": "ohlc"  
      }  
    }  
    
    
    
    {  
      "channelName": "ownTrades",  
      "event": "subscriptionStatus",  
      "status": "subscribed",  
      "subscription": {  
        "name": "ownTrades"  
      }  
    }  
    
    
    
    {  
      "errorMessage": "Subscription depth not supported",  
      "event": "subscriptionStatus",  
      "pair": "XBT/USD",  
      "status": "error",  
      "subscription": {  
        "depth": 42,  
        "name": "book"  
      }  
    }