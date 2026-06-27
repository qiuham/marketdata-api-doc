---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/amendorder
api_type: WebSocket
updated_at: 2026-05-27 20:08:55.991282
---

# Amend Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com`
    
    amendOrderAuthentication Required

The amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one.

  * The order identifiers assigned by Kraken and/or client will stay the same.
  * Queue priority in the order book will be maintained where possible.
  * If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see [amend transaction guide](/api/docs/guides/spot-amends).

## Request

  * Request Schema
  * Example: Trigger price
  * Example: Volume

### MESSAGE BODY

**event** `string` *required*

**Value:** `amendOrder`

**txid** `string`

**Example:** OFGKYQ-FHPCQ-HUQFEK

The Kraken identifier for the order to be amended. Either `txid` or `cl_ord_id` is required.

**cl_ord_id** `string`

**Example:** 6d1b345e-2821-40e2-ad83-4ecb18a06876

The client identifier for the order to be amended. Either `txid` or `cl_ord_id` is required.

**volume** `string`

The new order quantity in terms of the base asset.

**display_volume** `string` *conditional*

**Condition:** iceberg orders only. 

Defines the new quantity to show in the book while the rest of order quantity remains hidden.   
Minimum value is 1 / 15 of remaining order quantity.

**limit_price** `string` *conditional*

**Condition:** For order types that support limit price only. 

The new limit price restriction on the order.

To specify a relative price, this field can be prefixed by + or - to specify the order price as an offset relative to the market price.

  * `+` prefix: adds the amount to the reference price.
  * `-` prefix: subtracts the amount from the reference price.
  * `%` suffix: signifies the relative amount as a percentage, i.e., for a limit price 2% from last price use `"+2%"`.

**post_only** `boolean` *conditional*

**Condition:** Optional parameter for limit price changes. 

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

Applies to `limit_price` changes in this amend transaction. If `true`, the limit price change will be rejected if the order cannot be posted passively in the book.

**trigger_price** `string` *conditional*

**Condition:** For triggered order types only 

The new trigger price to activate the order.

To specify a relative price, this field can be prefixed by + or - to specify the order price as an offset relative to the market price.

  * `+` prefix: adds the amount to the reference price.
  * `-` prefix: subtracts the amount from the reference price.
  * `%` suffix: signifies the relative amount as a percentage, i.e., for a limit price 2% from last price use `"+2%"`.

**pair** `string`

**Example:** TSLAx/USD

The `symbol` is required on amends for non-crypto pairs, i.e. provide the pair symbol for xstocks.

**deadline** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123Z

Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.

**reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**token** `string` *required*

This is a authenticated request, a session token is required.

Example: amend the trigger price on an stop-loss order using the client order identifier.
    
    
    {  
        "event": "amendOrder",  
        "token": "AxBH/MuD3MyJWjkiViDd1FLPoinFBC8MHQg0/952jKE",  
        "cl_ord_id": "906bcc85-1866-4b4b-9d0d-880bbcbe7447",  
        "trigger_price": "61036.4"  
    }  
    

Example: amend the order quantity using the Kraken order identifier.
    
    
    {  
        "event": "amendOrder",  
        "token": "AxBH/MuD3MyJWjkiViDd1FLPoinFBC8MHQg0/952jKE",  
        "txid": "OB54AL-OBWL7-YOYRZI",  
        "volume": "0.011"  
    }  
      
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**event** `string`

**Value:** `amendOrderStatus`

**amend_id** `string`

The unique Kraken identifier generated for this amend transaction.

**txid** `string`

The Kraken identifier, if populated in the request.

**cl_ord_id** `string`

The client identifier, if populated in the request.

**status** `string`

**Possible values:**[`ok`, `error`] 

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string

Error message for unsuccessful requests.

Example: a successful amend using the client order identifier.
    
    
    {  
        "amend_id": "TGS4UP-DP6E3-YO3KFN",  
        "cl_ord_id": "906bcc85-1866-4b4b-9d0d-880bbcbe7447",  
        "event": "amendOrderStatus",  
        "status": "ok"  
    }