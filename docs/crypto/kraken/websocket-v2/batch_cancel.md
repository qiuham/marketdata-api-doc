---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/batch_cancel
api_type: WebSocket
updated_at: 2026-05-27 20:11:26.814314
---

# Batch Cancel

**WebSocket Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `batch_cancel` (Authentication Required)
The `batch_cancel` request enables multiple orders to be cancelled in a single request by a range of identifiers (minimum of 2 and maximum 50 in each batch).

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**method** `string` *required*

**Value:** `batch_cancel`

**params** `object`

    ↳ **orders** `array of string` *required*

A list containing either client `order_userref` or Kraken `order_id` identifiers.

        ↳ **cl_ord_id** `array of string`

A list of client `cl_ord_id` identifiers.

            ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "batch_cancel",  
        "params": {  
            "orders": [  
                "1",  
                "2",  
                "ORDERX-IDXXX-XXXXX3"  
            ],  
            "token": "TxxxxxxxxxOxxxxxxxxxxKxxxxxxxExxxxxxxxN"  
        },  
        "req_id": 1234567890  
    }  
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**method** `string`

**Value:** `batch_cancel`

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
        "method": "batch_cancel",  
        "req_id": 1234567890,  
        "result": {  
            "count": 3  
        },  
        "success": true,  
        "time_in": "2022-06-13T08:09:10.123456Z",  
        "time_out": "2022-06-13T08:09:10.7890123"  
    }