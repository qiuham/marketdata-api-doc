---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/cancelallordersafter
api_type: WebSocket
updated_at: 2026-05-27 20:09:17.453790
---

# Cancel on Disconnect

**WebSocket Endpoint:** `wss://ws-auth.kraken.com`
    
    cancelAllOrdersAfterAuthentication Required

`cancelAllOrdersAfter` request provides a "Dead Man's Switch" mechanism to protect the client from network malfunction, extreme latency or unexpected matching engine downtime. The client can send a request with a timeout (in seconds), that will start a countdown timer which will cancel _all_ client orders when the timer expires. The client has to keep sending new requests to push back the trigger time, or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds. This allows the client to keep the orders in place in case of a brief disconnection or transient delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders will be cancelled when the trading engine comes back from downtime - planned or otherwise).

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `cancelAllOrdersAfter`

**timeout** `integer` *required*

Timeout specified in seconds. 0 to disable the timer.

**reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**token** `string` *required*

This is a authenticated request, a session token is required.
    
    
    {  
      "event": "cancelAllOrdersAfter",  
      "reqid": 1608543428050,  
      "timeout": 60,  
      "token": "0000000000000000000000000000000000000000"  
    }  
    

## Response

  * Response Schema
  * Example: Enabled
  * Example: Disabled

### MESSAGE BODY

**event** `string`

**Value:** `cancelAllOrdersAfterStatus`

**currentTime** string

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

Timestamp when the request has been handled (second precision, rounded up).

**triggerTime** string

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

Timestamp at which all open orders will be cancelled, unless the timer is extended or disabled (second precision, rounded up).

**status** `string`

**Possible values:**[`ok`, `error`] 

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string

Error message for unsuccessful requests.
    
    
    {  
      "currentTime": "2020-12-21T09:37:09Z",  
      "event": "cancelAllOrdersAfterStatus",  
      "reqid": 1608543428050,  
      "status": "ok",  
      "triggerTime": "2020-12-21T09:38:09Z"  
    }  
    
    
    
    {  
      "currentTime": "2020-12-21T09:37:09Z",  
      "event": "cancelAllOrdersAfterStatus",  
      "reqid": 1608543428051,  
      "status": "ok",  
      "triggerTime": "0"  
    }