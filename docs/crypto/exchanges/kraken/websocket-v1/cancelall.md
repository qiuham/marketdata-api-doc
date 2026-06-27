---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/cancelall
api_type: WebSocket
updated_at: 2026-05-27 20:09:10.300807
---

# Cancel All

**WebSocket Endpoint:** `wss://ws-auth.kraken.com`
    
    cancelAllAuthentication Required

Cancel all open orders. Includes partially-filled orders.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `cancelAll`

**reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**token** `string` *required*

This is a authenticated request, a session token is required.
    
    
    {  
      "event": "cancelAll",  
      "token": "0000000000000000000000000000000000000000"  
    }  
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**event** `string`

**Value:** `cancelAllStatus`

**count** `string`

Number of orders cancelled.

**status** `string`

**Possible values:**[`ok`, `error`] 

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string

Error message for unsuccessful requests.
    
    
    {  
      "count": 2,  
      "event": "cancelAllStatus",  
      "status": "ok"  
    }