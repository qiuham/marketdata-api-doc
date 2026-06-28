---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/cancel_after
api_type: WebSocket
updated_at: 2026-05-27 20:11:40.896085
---

# Cancel on Disconnect

**WebSocket Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `cancel_all_orders_after` (Authentication Required)
`cancel_all_orders_after` provides a "Dead Man's Switch" mechanism to protect from network malfunction, extreme latency or unexpected matching engine downtime.

  * The client sends request with a timeout (in seconds), that will start a countdown timer in the trading engine which will cancel all client orders when the timer expires.
  * The client must keep sending new requests to reset the trigger time, or deactivate the mechanism by specifying a timeout of 0.
  * If the timer expires, all orders in the account are cancelled and the feature is disabled until the next `cancel_all_orders_after` request.
  * The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds. This allows the client to keep the orders in place in case of a brief disconnection or transient delay, while keeping them safe in case of a network breakdown.

info

It is recommended to disable the timer ahead of scheduled trading engine maintenance (if the timer is enabled, all orders will be cancelled when the trading engine comes back from downtime).

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**method** `string` *required*

**Value:** `cancel_all_orders_after`

**params** `object`

    ↳ **timeout** `integer` *required*

Duration (in seconds) to set/extend the timer, it should be less than `86400` seconds.

    ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "cancel_all_orders_after",  
        "params": {  
            "timeout": 100,  
            "token": "zwpdzWUe18Bn6h4TAMorh26+QbcMeST2B5tamfe+pgQ"  
        },  
        "req_id": 1234567890  
    }  
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**method** `string`

**Value:** `cancel_all_orders_after`

**result** `object` *conditional*

**Condition:** On successful requests only 

**currentTime** string

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The current engine time.

**triggerTime** string

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The time the orders will be expired in the engine.

    ↳ **warnings** `array of strings`

An advisory message, highlighting deprecated fields or upcoming changes to the request.

**error** `string` *conditional*

**Condition:** On unsuccessful requests only 

The error message for a rejected request.

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the request was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the response was sent on the wire, just prior to transmitting data.
    
    
    {  
        "method": "cancel_all_orders_after",  
        "req_id": 1234567890,  
        "result": {  
            "currentTime": "2023-09-21T15:49:29Z",  
            "triggerTime": "2023-09-21T15:51:09Z"  
        },  
        "success": true,  
        "time_in": "2023-09-21T15:49:28.627900Z",  
        "time_out": "2023-09-21T15:49:28.649057Z"  
    }