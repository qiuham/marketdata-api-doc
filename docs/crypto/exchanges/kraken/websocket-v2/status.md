---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/status
api_type: WebSocket
updated_at: 2026-05-27 20:12:52.323414
---

# Status

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    status

The `status` channel provides a mechanism to verify exchange status and successful initial connection.

There is no option to directly request a `status` update, a status will be automatically generated on successful websocket connection and when the trading engine status changes.

## Update Response

  * Update Schema
  * Example

### MESSAGE BODY

**channel** `string`

**Value:** `status`

**type** `string`

**Value:** `update`

**data** `array [`

**[0] status** object

The status element is always the first and only item in the data payload.

    ↳ **system** `string`

**Possible values:**[`online`, ` cancel_only`, ` maintenance`, ` post_only`] 

The status of the trading engine.

  * `online`: Markets are operating normally - all order types may be submitted and order matching can occur.
  * `maintenance`: Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
  * `cancel_only`: Orders can be cancelled but new orders cannot be placed. No order matching will occur.
  * `post_only`: Only limit orders using the `post_only` option can be submitted. Orders can be cancelled. No order matching will occur.

    ↳ **api_version** `string`

**Value:** `v2`

The version of the websockets API.

    ↳ **connection_id** `integer`

A unique connection identifier (for debugging).

    ↳ **version** `string`

The version of the websockets service.

]
    
    
    {  
        "channel": "status",  
        "data": [  
            {  
                "api_version": "v2",  
                "connection_id": 13834774380200032777,  
                "system": "online",  
                "version": "2.0.0"  
            }  
        ],  
        "type": "update"  
    }