---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/cancelorder
api_type: WebSocket
updated_at: 2026-05-27 20:09:24.390062
---

# Cancel Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com`
    
    cancelOrderAuthentication Required

The `cancelOrder` request cancels one or more open orders in a single request. The orders to be cancelled can be identified by a range of client or Kraken identifiers.

  * For every cancelled order, a `cancelOrderStatus` message is sent.
  * For example, if a cancelOrder request is sent for cancelling three orders [A, B, C], then if two update messages for 'cancelOrderStatus' are received along with an error such as 'EOrder: Unknown order', then it would imply that the third order is not cancelled. The error message could be different based on the condition which was not met by the 'cancelOrder' request.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `cancelOrder`

**txid** `array of string` *required*

A list containing either client `order_userref` or Kraken `order_id` identifiers.

    ↳ **cl_ord_id** `array of string`

A list of client `cl_ord_id` identifiers.

        ↳ **reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

        ↳ **token** `string` *required*

This is a authenticated request, a session token is required.
    
    
    {  
      "event": "cancelOrder",  
      "token": "0000000000000000000000000000000000000000",  
      "txid": [  
        "OGTT3Y-C6I3P-XRI6HX",  
        "OGTT3Y-C6I3P-X2I6HX"  
      ]  
    }  
    

## Response

  * Response Schema
  * Example
  * Example

### MESSAGE BODY

**event** `string`

**Value:** `cancelAllStatus`

**status** `string`

**Possible values:**[`ok`, `error`] 

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string

Error message for unsuccessful requests.
    
    
    {  
      "event": "cancelOrderStatus",  
      "status": "ok"  
    }  
    
    
    
    {  
      "errorMessage": "EOrder:Unknown order",  
      "event": "cancelOrderStatus",  
      "status": "error"  
    }