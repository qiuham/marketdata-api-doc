---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/edit_order
api_type: WebSocket
updated_at: 2026-05-27 20:12:02.295409
---

# Edit Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com/v2`
**Method:** `edit_order` (Authentication Required)
Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be created with the adjusted parameters a new `order_id` will be returned in the response.

note

The new [amend_order](/api/docs/websocket-v2/amend_order) endpoint resolves the caveats listed below and has additional performance gains.

There are a number of caveats for `edit_order`:

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

**method** `string` *required*

**Value:** `edit_order`

**params** `object`

    ↳ **deadline** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123Z

Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.

    ↳ **display_qty** `float` *conditional*

**Condition:** Iceberg orders only. 

Defines the quantity to show in the book while the rest of order quantity remains hidden.   
Minimum value is 1 / 15 of `order_qty`.

    ↳ **fee_preference** `string`

**Possible values:**[`base`, ` quote`] 

Fee preference base or quote currency. `quote` is the default for buy orders, `base` is the default for sell orders.

    ↳ **limit_price** `float`

Limit price for order types that support limit price restriction.

    ↳ **no_mpp** `boolean deprecated`

**Deprecated Usage:** If supplied, the flag is accepted but ignored.

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

Disables Market Price Protection (MPP) if set to `true`. MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market. See [MPP support article](https://support.kraken.com/hc/en-us/articles/201648183-Market-Price-Protection).

    ↳ **order_id** `string` *required*

**Example:** OFGKYQ-FHPCQ-HUQFEK

The Kraken identifier for the order to be amended.

    ↳ **order_qty** `float`

Order quantity in terms of the base asset.

    ↳ **order_userref** `integer`

User defined reference to be placed on the amended order. It does not identifier the order to be amended, use `order_id`.

    ↳ **post_only** `boolean` *conditional*

**Condition:** Orders with limit price only. 

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.

    ↳ **reduce_only** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.

    ↳ **symbol** `string` *required*

**Example:** "BTC/USD"

The original symbol identifier for the pair. Note, the `symbol` cannot be amended. 

    ↳ **triggers** `object` *conditional*

**Condition:** Required for triggered order types only. 

The parameters for setting the trigger price conditions.

        ↳ **reference** `string`

**Possible values:**[`index`, ` last`] 

**Default value:**`last`

The reference price to track for triggering orders.

  * `index`: the index price in the broader market (for this pair). Note, to keep triggers serviceable during connectivity issues with external index feeds, the last price will be used as the reference price.
  * `last`: the last traded price in the Kraken order book (for this pair).

        ↳ **price** `float`

Specifies the amount for the trigger price - it supports both static market prices and relative prices. This field is used in combination with the `price_type` field below to determine the effective trigger price.   
**Examples:**

  * To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
  * To trigger when price rises by 5%, use price=5, price_type=pct.
  * To trigger when price drops by 150 USD, use price=-150, price_type=quote.

Note, for `trailing-stop` and `trailing-stop-limit` order types, the price represents the reversion from the peak. It is always a positive offset value.

        ↳ **price_type** `string`

**Possible values:**[`static`, ` pct`, ` quote`] 

**Default value:**`static`

The units for the trigger price.

  * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
  * `pct`: a percentage offset from the reference price, i.e. -10% from index price.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price

        ↳ **validate** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`false`

If set to `true` the order will be validated only, it will not trade in the matching engine.

        ↳ **price** `float deprecated`

**Deprecated Usage:** Use 'limit_price' parameter.

        ↳ **trigger** `string deprecated`

**Deprecated Usage:** Use 'triggers.reference' parameter.

        ↳ **stop_price** `float deprecated`

**Deprecated Usage:** Use 'triggers.price' parameter.

        ↳ **token** `string` *required*

This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "method": "edit_order",  
      "params": {  
        "order_id": "ORDERX-IDXXX-XXXXX1",  
        "order_qty": 0.2123456789,  
        "symbol": "BTC/USD",  
        "token": "TxxxxxxxxxOxxxxxxxxxxKxxxxxxxExxxxxxxxN"  
      },  
      "req_id": 1234567890  
    }  
    

## Response

  * Response Schema
  * Example

### MESSAGE BODY

**method** `string`

**Value:** `edit_order`

**result** `object` *conditional*

**Condition:** On successful requests only 

    ↳ **order_id** `string`

Unique ID of the order

    ↳ **original_order_id** `string`

ID of the order that have been edited

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
      "method": "edit_order",  
      "req_id": 1234567890,  
      "result": {  
        "order_id": "ORDERX-IDXXX-XXXXX2",  
        "original_order_id": "ORDERX-IDXXX-XXXXX1"  
      },  
      "success": true,  
      "time_in": "2022-07-15T12:56:09.876488Z",  
      "time_out": "2022-07-15T12:56:09.923422Z"  
    }