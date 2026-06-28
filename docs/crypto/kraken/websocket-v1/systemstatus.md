---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/systemstatus
api_type: WebSocket
updated_at: 2026-05-27 20:10:29.167580
---

# System Status

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    systemStatus

Status sent on connection or system status changes.

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**event** `string`

**Value:** `systemStatus`

**status** `string`

**Possible values:**[`online`, ` cancel_only`, ` maintenance`, ` post_only`] 

The status of the trading engine.

  * `online`: Markets are operating normally - all order types may be submitted and order matching can occur.
  * `maintenance`: Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
  * `cancel_only`: Orders can be cancelled but new orders cannot be placed. No order matching will occur.
  * `post_only`: Only limit orders using the `post_only` option can be submitted. Orders can be cancelled. No order matching will occur.

**version** `string`

The version of the websockets service.

**connectionID** integer

A unique connection identifier (for debugging).
    
    
    {  
      "connectionID": 8628615390848610000,  
      "event": "systemStatus",  
      "status": "online",  
      "version": "1.9.1"  
    }