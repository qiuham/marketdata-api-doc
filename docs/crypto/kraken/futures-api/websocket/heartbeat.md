---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/heartbeat
api_type: WebSocket
updated_at: 2026-05-27 19:55:28.769792
---

# Heartbeat

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    heartbeat

The heartbeat feed publishes a heartbeat message at timed intervals.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `heartbeat`
    
    
    {  
      "event": "subscribe",  
      "feed": "heartbeat"  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `heartbeat`
    
    
    {  
      "event": "subscribed",  
      "feed": "heartbeat"  
    }  
    

## Response Snapshot

  * Response Fields
  * Subscription Data

### MESSAGE BODY

**feed** `string`

The subscribed feeds

**time** `positive integer`

The UTC time of the server in milliseconds
    
    
    {  
      "feed": "heartbeat",  
      "time": 1534262350627  
    }  
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

An error message out of:  
`Invalid feed`  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Json Error"  
    }