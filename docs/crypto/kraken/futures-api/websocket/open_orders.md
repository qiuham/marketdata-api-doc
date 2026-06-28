---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/open_orders
api_type: WebSocket
updated_at: 2026-05-27 19:55:43.178826
---

# Open Orders

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    open_orders

This subscription feed publishes information about user open orders.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `open_orders`

**api_key** `string` *required*

The user api key

**original_challenge** `string` *required*

The message that is received from a challenge request

**signed_challenge** `string` *required*

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribe",  
      "feed": "open_orders_verbose",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `open_orders`

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "open_orders",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Snapshot

  * Response Fields
  * Subscription Snapshot Data

### MESSAGE BODY

**feed** `string`

The subscribed feed

**account** `string`

The user account

**orders** `list of structures`

The user new order 

**instrument** `string`

The instrument (referred also as symbol or product_id) of the order

**time** `positive integer`

The UTC time in milliseconds.

**last_update_time** `positive integer`

The UTC time in milliseconds that the order was 
**qty** `positive float`

The quantity or the order.

**filled** `positive float`

The total amount of the order that is filled.

**limit_price** `positive float`

The limit price of the order.

**stop_price** `positive float`

The stop price of the order.

**type** `string`

The order type, `limit`, `take_profit`, or `stop`

**order_id** `UUID`

The order id.

**cli_ord_id** `UUID`

The unique client order identifier. This field is returned only if the order has a client order id.

**direction** `integer`

The direction of the order, either 0 for a buy order or 1 for a sell order.

**reduce_only** `boolean`

If true, the order can only reduce open positions, it cannot increase or open new positions.

**triggerSignal** string

Trigger signal selected for take profit or stop loss order. Options are `last`, `mark`, or `spot`. Returned only for take profit or stop loss orders.

**trailing_stop_options** `list of structures`

If this order is a trailing stop, this contains its parameters 

**max_deviation** `double`

The maximum distance the trigger price may be away from the trigger signal.

**unit** `string`

The unit of the deviation, one of:  
`percent`  
`quote_currency`
    
    
    {  
      "feed": "open_orders_snapshot",  
      "account": "e258dba9-4dd4-4da5-bfef-75beb91c098e",  
      "orders": [  
        {  
          "instrument": "PI_XBTUSD",  
          "time": 1612275024153,  
          "last_update_time": 1612275024153,  
          "qty": 1000,  
          "filled": 0,  
          "limit_price": 34900,  
          "stop_price": 13789,  
          "type": "stop",  
          "order_id": "723ba95f-13b7-418b-8fcf-ab7ba6620555",  
          "direction": 1,  
          "reduce_only": false,  
          "triggerSignal": "last"  
        },  
        {  
          "instrument": "PI_XBTUSD",  
          "time": 1612275024153,  
          "last_update_time": 1612275178153,  
          "qty": 12,  
          "filled": 0,  
          "stop_price": 3200.1,  
          "type": "trailing_stop",  
          "order_id": "59302619-41d2-4f0b-941f-7e7914760ad3",  
          "direction": 1,  
          "reduce_only": false,  
          "triggerSignal": "mark",  
          "trailing_stop_options": {  
            "max_deviation": 20.0,  
            "unit": "percent"  
          }  
        },  
        {  
          "instrument": "PI_XBTUSD",  
          "time": 1612275209430,  
          "last_update_time": 1612275209430,  
          "qty": 1000,  
          "filled": 0,  
          "limit_price": 35058,  
          "stop_price": 0,  
          "type": "limit",  
          "order_id": "7a2f793e-26f3-4987-a938-56d296a11560",  
          "direction": 1,  
          "reduce_only": false  
        }  
      ]  
    }  
    

## Response Delta

  * Response Fields
  * Subscription Delta Data
  * Cancelled Subscription

### MESSAGE BODY

**feed** `string`

The subscribed feed

**order** `structure`

The user new order 

**instrument** `string`

The instrument (referred also as symbol or product_id) of the order

**time** `positive integer`

The UTC time in milliseconds.

**last_update_time** `positive integer`

The UTC time in milliseconds that the order was 
**qty** `positive float`

The quantity or the order.

**filled** `positive float`

The total amount of the order that is filled.

**limit_price** `positive float`

The limit price of the order.

**stop_price** `positive float`

The stop price of the order.

**type** `string`

The order type, `limit`, `take_profit`, or `stop`

**order_id** `UUID`

The order id.

**cli_ord_id** `UUID`

The unique client order identifier. This field is returned only if the order has a client order id.

**direction** `integer`

The direction of the order, either 0 for a buy order or 1 for a sell order.

**reduce_only** `boolean`

If true, the order can only reduce open positions, it cannot increase or open new positions.

**triggerSignal** string

Trigger signal selected for take profit or stop loss order. Options are `last`, `mark`, or `spot`. Returned only for take profit or stop loss orders.

**trailing_stop_options** `list of structures`

If this order is a trailing stop, this contains its parameters 

**max_deviation** `double`

The maximum distance the trigger price may be away from the trigger signal.

**unit** `string`

The unit of the deviation, one of:  
`percent`  
`quote_currency`

**is_cancel** `boolean`

If false the open order has been either placed or partially filled and needs to be updated. If true the open order was either fully filled, cancelled or rejected (for post-only). If it was filled or cancelled it must be removed from open orders snapshot.

**reason** `string`

Reason behind the received delta.  
`new_placed_order_by_user`: User placed a new order  
`liquidation`: User position liquidated. The order cancelled  
`stop_order_triggered`: A stop order triggered. The system removed the stop order  
`limit_order_from_stop`: The system created a limit order because an existing stop order triggered  
`partial_fill`: The order filled partially  
`full_fill`: The order filled fully and removed  
`cancelled_by_user`: The order cancelled by the user and removed  
`contract_expired`: The order contract expired. All open orders of that contract removed  
`not_enough_margin`: The order removed due to insufficient margin  
`market_inactive`: The order removed because market became inactive  
`cancelled_by_admin`: The order removed by administrator's action  
`dead_man_switch`: The order removed because dead man's switch was triggered  
`ioc_order_failed_because_it_would_not_be_executed`: The immediate or cancel order was rejected due to insufficient liquidity  
`post_order_failed_because_it_would_filled`: The post only order was rejected as it crosses the spread and would be immediately filled  
`would_execute_self`: The order was rejected as it would execute against another order from the same account  
`would_not_reduce_position`: The order was rejected as it the reduce-only option was selected and it would not reduce the position  
`order_for_edit_not_found`: The order edit was rejected as the order to be edited could not be found
    
    
    {  
      "feed": "open_orders",  
      "order": {  
        "instrument": "PI_XBTUSD",  
        "time": 1567702877410,  
        "last_update_time": 1567702877410,  
        "qty": 304.0,  
        "filled": 0.0,  
        "limit_price": 10640.0,  
        "stop_price": 0.0,  
        "type": "limit",  
        "order_id": "59302619-41d2-4f0b-941f-7e7914760ad3",  
        "direction": 1,  
        "reduce_only": true  
      },  
      "is_cancel": false,  
      "reason": "new_placed_order_by_user"  
    }  
    
    
    
    {  
      "feed": "open_orders",  
      "order_id": "660c6b23-8007-48c1-a7c9-4893f4572e8c",  
      "is_cancel": true,  
      "reason": "cancelled_by_user"  
    }  
      
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

An error message out of:  
`Invalid feed`  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Invalid feed"  
    }