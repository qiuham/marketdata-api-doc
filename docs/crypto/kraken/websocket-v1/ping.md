---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/ping
api_type: WebSocket
updated_at: 2026-05-27 20:10:07.759935
---

# Ping

**WebSocket Endpoint:** `wss://ws.kraken.com`
    
    ping

Client can ping server to determine whether connection is alive, server responds with pong. This is an application level ping as opposed to default ping in websockets standard which is server initiated

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `ping`

**reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "ping",  
      "reqid": 42  
    }  
    

## Pong Response

  * Response Schema
  * Example

### MESSAGE BODY

**event** `string`

**Value:** `pong`

**reqid** `integer`

Client originated identifier for the request that initiated this response.
    
    
    {  
      "event": "pong",  
      "reqid": 42  
    }