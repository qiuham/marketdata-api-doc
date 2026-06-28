---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/addorder
api_type: WebSocket
updated_at: 2026-05-27 20:08:48.990284
---

# Add Order

**WebSocket Endpoint:** `wss://ws-auth.kraken.com`
    
    addOrderAuthentication Required

Sends a single, new order into the exchange. A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below.

## Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `addOrder`

**ordertype** `string` *required*

**Possible values:**[`limit`, `market`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`, `settle-position`] 

The execution model for the order.

**type** `string` *required*

**Possible values:**[`buy`, `sell`] 

Side of the order.

**pair** `string` *required*

**Example:** 'BTC/USD'

Currency pair.

**price** `string`

This parameter represents the limit price or trigger price depending on the order type:

  * **limit** price for `limit` orders.
  * **trigger** price for `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop` and `trailing-stop-limit` orders

To specify a relative price, this field can be prefixed by +, -, or # to specify the order price as an offset relative to the last traded price.

  * `+` adds the amount to the last traded price.
  * `-` subtracts the amount from the last traded price.
  * `#` will either add or subtract the amount to the last traded price, depending on the direction.

Prices can also be suffixed with a `%` to signify the relative amount as a percentage, rather than an absolute price difference in the quote currency. Example, to specify a price as 2% from last price use `"+2%"`.

Note, trailing stop order types must use a relative price for this field, i.e. `+` to represent the reversion from the peak / trough price.

**price2** string

This parameter represents the **limit** price for `stop-loss-limit`, `take-profit-limit` and `trailing-stop-limit` orders.

To specify a relative price, this field can be prefixed by + or - to specify the order price as an offset relative to the market price.

  * `+` adds the amount to the reference price.
  * `-` subtracts the amount from the reference price.

Prices can also be suffixed with a `%` to signify the relative amount as a percentage, rather than an absolute price difference in the quote currency. Example, to specify a price as 2% from last price use `"+2%"`.

Note, trailing stop order types must use a relative price for this field, i.e. `+` or `-` to represent the offset from the triggered price.

**volume** `string` *required*

Order volume in base currency.

**leverage** `string`

**Possible values:**[`2`, `3`, `4`, `5`] 

Funds the order on margin using the amount of leverage specified. The maximum leverage available differs across pairs.

**margin** `boolean`

**Possible values:**[`false`, `true`] 

**Default value:**`false`

Funds the order on margin using the maximum leverage for the pair. Note, absolute max leverage is 5.

**reduce_only** `boolean` *conditional*

**Condition:** Margin orders only. 

**Possible values:**[`false`, `true`] 

**Default value:**`false`

If true, order will only reduce a currently open position, not increase it or open a new position.

**oflags** `string`

**Possible values:**[`fciq`, `fcib`, `nompp`, `post`, `viqc`] 

Comma delimited list of order flags.

  * `fcib`: prefer fee in base currency (default if selling)
  * `fciq`: prefer fee in quote currency (default if buying, mutually exclusive with fcib)
  * `nompp`: no market price protection. DEPRECATED. If supplied, the flag is accepted but ignored
  * `post`: post only order (only on limit orders).
  * `viqc`: volume in quote currency (only available on buy market orders without margin funding).

**starttm** `string`

Scheduled start time. 0 = now (default) `+n` = schedule start time `n` seconds from now `n` = unix timestamp of start time.

**expiretm** `string`

Expiration time. 0 = no expiration (default) `+n` = expire`n` seconds from now `n` = unix timestamp of expiration time. GTD orders can have an expiry time up to one month in future.

**deadline** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123Z

Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.

**cl_ord_id** `string`

Adds a alphanumeric client order identifier which uniquely identifies an open order for each client. This field is mutually exclusive with `userref` parameter.

The `cl_ord_id` parameter can be one of the following formats:

  * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
  * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
  * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.

**userref** `string`

**Example:** "123456789"

This is an optional non-unique, numeric identifier which can associated with a number of orders by the client. This field is mutually exclusive with `cl_ord_id` parameter.

Many clients choose a unique integer value generated by their systems (i.e. a timestamp). However, because we don't enforce uniqueness on our side, it can also be used to easily tag a group of orders for querying or cancelling.

**sender_sub_id** `string` *conditional*

**Condition:** For institutional accounts with enhanced Self Trade Prevention (STP) 

Adds a alphanumeric sub-account/trader identifier which enables STP to be performed at a more granular level.

The `sender_sub_id` parameter can be one of the following formats:

  * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
  * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
  * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.

**stp_type** `string`

**Possible values:**[`cancel_newest`, ` cancel_oldest`, ` cancel_both`] 

**Default value:**`cancel_newest`

Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves. To prevent a self-match, one of the following STP modes can be used to define which order(s) will be expired:

  * `cancel_newest`: arriving order will be canceled.
  * `cancel_oldest`: resting order will be canceled.
  * `cancel_both`: both arriving and resting orders will be canceled.

**validate** `string`

Validate inputs only; do not submit order.

**timeinforce** `string`

**Possible values:**[`GTC`, ` GTD`, ` IOC`] 

**Default value:**`GTC`

Time-in-force specifies how long an order remains in effect before expiry.

  * `GTC`: Good Till Canceled - until user has cancelled.
  * `GTD`: Good Till Date - until `expiretm` parameter.
  * `IOC`: Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.

**close[ordertype]** string

Order type of the secondary OTO order.

**close[price]** string

`price` of OTO secondary order - see `price` parameter.

**close[price2]** string

`price2` of OTO secondary order - see `price2` parameter.

**reqid** `integer`

Optional client originated request identifier sent as acknowledgment in the response.

**token** `string` *required*

This is a authenticated request, a session token is required.
    
    
    {  
      "event": "addOrder",  
      "ordertype": "limit",  
      "pair": "XBT/USD",  
      "price": "9000",  
      "token": "0000000000000000000000000000000000000000",  
      "type": "buy",  
      "volume": "10.123"  
    }  
    

## Response

  * Response Schema
  * Example
  * Example Error

### MESSAGE BODY

**event** `string`

**Value:** `addOrderStatus`

**txid** `string`

A Kraken order identifier for the new order.

**cl_ord_id** `string`

An optional, alphanumeric identifier specified by the client in the `add_order` parameters.

**descr** `string`

A descriptive summary for the new order.

**status** `string`

**Possible values:**[`ok`, `error`] 

**reqid** `integer`

Client originated identifier for the request that initiated this response.

**errorMessage** string

Error message for unsuccessful requests.
    
    
    {  
      "descr": "buy 0.01770000 XBTUSD @ limit 4000",  
      "event": "addOrderStatus",  
      "status": "ok",  
      "txid": "ONPNXH-KMKMU-F4MR5V"  
    }  
    
    
    
    {  
      "errorMessage": "EOrder:Order minimum not met",  
      "event": "addOrderStatus",  
      "status": "error"  
    }