---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/editorder
api_type: WebSocket
updated_at: 2026-05-27 20:09:31.648173
---

# Edit Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com`
    
    editOrderAuthentication Required

Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be created with the adjusted parameters a new `txid` will be returned in the response.

note

The new [amendOrder](/api/docs/websocket-v1/amendorder) endpoint resolves the caveats listed below and has additional performance gains.

There are a number of caveats for `editOrder`:

  * triggered stop loss or profit take profit orders are not supported.
  * orders with conditional close terms attached are not supported.
  * orders where the executed volume is greater than the newly supplied volume will be rejected.
  * `cl_ord_id` is not supported.
  * existing executions will are associated with the original order and not copied to the amended order.
  * queue position will not be maintained.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `editOrder`

**orderid** `string`

Original Order ID or userref.

**pair** `string` *required*

Currency pair.

**price** `string`

Dependent on order type - order price.

**price2** string

Dependent on order type - order secondary price.

**volume** `string` *required*

Order volume in base currency.

**oflags** `string`

Comma delimited list of order flags. post = post only order (available when ordertype = limit).

**newuserref** `string`

User reference ID for new order (should be an integer in quotes).

**validate** `boolean`

Validate inputs only; do not submit order.

**reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**token** `string` *required*

This is a authenticated request, a session token is required.
    
    
    {  
      "event": "editOrder",  
      "newuserref": "666",  
      "oflags": "",  
      "orderid": "O26VH7-COEPR-YFYXLK",  
      "pair": "XBT/USD",  
      "price": "9000",  
      "reqid": 3,  
      "token": "0000000000000000000000000000000000000000"  
    }  
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**event** `string`

**Value:** `editOrderStatus`

**txid** `string`

A new Kraken order identifier for the amended order.

**originaltxid** `string`

The Kraken order identifier for the original order.

**descr** `string`

A descriptive summary for the amended order.

**status** `string`

**Possible values:**[`ok`, `error`] 

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string

Error message for unsuccessful requests.
    
    
    {  
      "descr": "order edited price = 9000.00000000",  
      "event": "editOrderStatus",  
      "originaltxid": "O65KZW-J4AW3-VFS74A",  
      "reqid": 3,  
      "status": "ok",  
      "txid": "OTI672-HJFAO-XOIPPK"  
    }