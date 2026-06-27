---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/cancel_all
api_type: WebSocket
updated_at: 2026-05-27 20:11:48.040718
---

# Cancel All

**WebSocket Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `cancel_all` (Authentication Required)
Cancels all open orders, including untriggered orders and orders resting in the book.

Note, the details of the individual cancelled orders will also be streamed on the `executions` channel.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**method** `string` *required*

**Value:** `cancel_all`

**params** `object`

    ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "cancel_all",  
        "params": {  
            "token": "weeBxllys/7kHy/zHpkATSDIS42BvDgWS2b04ZSZHZ5"  
        },  
        "req_id": 1234567890  
    }  
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**method** `string`

**Value:** `cancel_all`

**result** `object` *conditional*

**Condition:** On successful requests only 

    ↳ **count** `integer`

Number of orders cancelled.

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
        "method": "cancel_all",  
        "req_id": 1234567890,  
        "result": {  
            "count": 1  
        },  
        "success": true,  
        "time_in": "2023-09-26T13:09:48.463201Z",  
        "time_out": "2023-09-26T13:09:48.471419Z"  
    }