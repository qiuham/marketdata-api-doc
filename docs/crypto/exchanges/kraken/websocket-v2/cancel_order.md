---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/cancel_order
api_type: WebSocket
updated_at: 2026-05-27 20:11:55.155877
---

# Cancel Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `cancel_order` (Authentication Required)
The `cancel_order` request cancels one or more open orders in a single request. The orders to be cancelled can be identified by a range of client or Kraken identifiers. Note, the details of the individual cancelled orders will also be streamed on the `executions` channel.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**method** `string` *required*

**Value:** `cancel_order`

**params** `object`

    ↳ **order_id** `array of string`

A list of Kraken `order_id` identifiers.

        ↳ **cl_ord_id** `array of string`

A list of client `cl_ord_id` identifiers.

            ↳ **order_userref** `array of integer`

A list of client `order_userref` identifiers.

                ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "cancel_order",  
        "params": {  
            "order_id": [  
                "OM5CRX-N2HAL-GFGWE9",  
                "OLUMT4-UTEGU-ZYM7E9"  
            ],  
            "token": "zGXT1dUQQjJjy5VmGXMegdDQngXXehNo5qbMBVolwEQ"  
        },  
        "req_id": 123456789  
    },  
    

## Response

When cancelling multiple orders, there will be a stream of individual order responses.

  * Response Schema
  * Example

### MESSAGE BODY

**method** `string`

**Value:** `cancel_order`

**result** `object` *conditional*

**Condition:** On successful requests only 

    ↳ **order_id** `string`

Kraken identifier of the cancelled order.

    ↳ **cl_ord_id** `string`

Optional client identifier of the cancelled order.

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
      {  
        "method": "cancel_order",  
        "req_id": 123456789,  
        "result": {  
            "order_id": "OLUMT4-UTEGU-ZYM7E9"  
        },  
        "success": true,  
        "time_in": "2023-09-21T14:36:57.428972Z",  
        "time_out": "2023-09-21T14:36:57.437952Z"  
      },  
      {  
        "method": "cancel_order",  
        "req_id": 123456789,  
        "result": {  
            "order_id": "OM5CRX-N2HAL-GFGWE9"  
        },  
        "success": true,  
        "time_in": "2023-09-21T14:36:57.428972Z",  
        "time_out": "2023-09-21T14:36:57.438027Z"  
      }  
    }