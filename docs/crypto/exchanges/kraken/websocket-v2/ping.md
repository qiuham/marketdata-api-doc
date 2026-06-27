---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/ping
api_type: WebSocket
updated_at: 2026-05-27 20:12:45.193982
---

# Ping

**WebSocket Endpoint:** `wss://ws.kraken.com/v2`
    
    ping

Clients can ping the server to verify connection is alive and the server will respond with a `pong`.

This is an application level ping, distinct from the protocol-level ping in the WebSockets standard.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**method** `string` *required*

**Value:** `ping`

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "ping",  
        "req_id": 101  
    }  
    

## Response

  * Response Schema
  * Response Schema

### MESSAGE BODY

**method** `string`

**Value:** `pong`

**result** `object` *conditional*

**Condition:** On successful requests only 

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
        "method": "pong",  
        "req_id": 101,  
        "time_in": "2023-09-24T14:10:23.799685Z",  
        "time_out": "2023-09-24T14:10:23.799703Z"  
    }