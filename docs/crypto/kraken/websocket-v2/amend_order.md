---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/amend_order
api_type: WebSocket
updated_at: 2026-05-27 20:11:05.145084
---

# Amend Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `amend_order` (Authentication Required)
The amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one.

  * The order identifiers assigned by Kraken and/or client will stay the same.
  * Queue priority in the order book will be maintained where possible.
  * If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see [amend transaction guide](/api/docs/guides/spot-amends).

## Request

  * Request Schema
  * Example: Basic
  * Example: Advanced

### MESSAGE BODY

**method** `string` *required*

**Value:** `amend_order`

**params** `object`

    ↳ **order_id** `string` *required*

**Example:** OFGKYQ-FHPCQ-HUQFEK

The Kraken identifier for the order to be amended. Either `order_id` or `cl_ord_id` is required.

    ↳ **cl_ord_id** `string`

**Example:** 6d1b345e-2821-40e2-ad83-4ecb18a06876

The client identifier for the order to be amended. Either `order_id` or `cl_ord_id` is required.

    ↳ **order_qty** `float` *required*

The new order quantity in terms of the base asset.

    ↳ **display_qty** `float` *conditional*

**Condition:** iceberg orders only. 

Defines the new quantity to show in the book while the rest of order quantity remains hidden.   
Minimum value is 1 / 15 of remaining order quantity.

    ↳ **limit_price** `float` *conditional*

**Condition:** For order types that support limit price only. 

The new limit price restriction on the order, used in combination with the `limit_price_type` parameter.

    ↳ **limit_price_type** `string` *conditional*

**Condition:** Currently only available on trailing-stop-limit orders. 

**Possible values:**[`static`, ` pct`, ` quote`] 

The units for `limit_price`:

  * `static`: a static market price for the asset, i.e. limit price at 29000.5 BTC/USD, use price=29000.5 and price_type=static.
  * `pct`: a percentage offset from the reference price, i.e. limit price when market rises by 5%, use price=5 and price_type=pct.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, limit price when market drops by 150 USD, use price=-150 and price_type=quote.

`static` is the default for all order types except for `trailing-stop-limit` which has the default `quote` offset.

    ↳ **post_only** `boolean` *conditional*

**Condition:** Optional parameter for limit price amends. 

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

If `true`, the limit price change will be rejected if the order cannot be posted passively in the book.

    ↳ **trigger_price** `float` *conditional*

**Condition:** For triggered order types only 

The new trigger price to activate the order, used in combination with the `trigger_price_type` parameter.

    ↳ **trigger_price_type** `string` *conditional*

**Condition:** For triggered order types only 

**Possible values:**[`static`, ` pct`, ` quote`] 

**Default value:**`static`

The units for `trigger_price`:

  * `static`: a static market price for the asset, i.e. to trigger at 29000.5 BTC/USD, use price=29000.5 and price_type=static.
  * `pct`: a percentage offset from the reference price, i.e. to trigger when price rises by 5%, use price=5 and price_type=pct.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, to trigger when price drops by 150 USD, use price=-150 and price_type=quote.

    ↳ **deadline** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123Z

Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.

    ↳ **symbol** `string`

**Example:** TSLAx/USD

The `symbol` is required on amends for non-crypto pairs, i.e. provide the pair symbol for xstocks.

    ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

Example: amend the limit price and the quantity on an order using a UUID client order identifier.
    
    
    {  
      "method": "amend_order",  
      "params": {  
          "cl_ord_id": "2c6be801-1f53-4f79-a0bb-4ea1c95dfae9",  
          "limit_price": 490795,  
          "order_qty": 1.2,  
          "token": "PM5Qm0MDrS54l657aQAtb7AhrwN30e2LBg1nUYOd6vU"  
    }  
    

Amends the price on an order using the Kraken order identifier.

  * `post_only` indicates the transaction will be rejected if the new limit price will take liquidity immediately.
  * `deadline` indicates this amend request is latency sensitive, rejected the amend reject if not processed before the time.

    
    
    {  
        "method": "amend_order",  
        "params": {  
            "order_id": "OAIYAU-LGI3M-PFM5VW",  
            "limit_price": 61031.3,  
            "deadline": "2024-07-21T09:53:59.050Z",  
            "post_only": true,  
            "token": "DGB00LiKlPlLI/amQaSKUUr8niqXDb+1zwvtjp34nzk"  
        }  
    }  
    

## Response

  * Response Schema
  * Example

A successful amend request will return the unique Kraken amend identifier.

### MESSAGE BODY

**method** `string`

**Value:** `amend_order`

**result** `object` *conditional*

**Condition:** On successful requests only 

    ↳ **amend_id** `string`

The unique Kraken identifier generated for this amend transaction.

    ↳ **order_id** `string`

The Kraken identifier, if populated in the request.

    ↳ **cl_ord_id** `string`

The client identifier, if populated in the request.

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

Example: response for an order successfully amended with a client order identifier.
    
    
    {  
        "method": "amend_order",  
        "result": {  
            "amend_id": "TTW6PD-RC36L-ZZSWNU",  
            "cl_ord_id": "2c6be801-1f53-4f79-a0bb-4ea1c95dfae9"  
        },  
        "success": true,  
        "time_in": "2024-07-26T13:39:04.922699Z",  
        "time_out": "2024-07-26T13:39:04.924912Z"  
    }