---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/open_orders_verbose
api_type: WebSocket
updated_at: 2026-05-27 19:55:50.677388
---

# Open Orders (verbose)

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    open_orders_verbose

This subscription feed publishes information about user open orders. This feed adds extra information about all the post-only orders that failed to cross the book.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `open_orders_verbose `

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

The requested subscription feed `open_orders_verbose `

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "open_orders_verbose",  
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

The total amount of the order that has been filled.

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
    
    
    {  
      "feed": "open_orders_verbose_snapshot",  
      "account": "0f9c23b8-63e2-40e4-9592-6d5aa57c12ba",  
      "orders": [  
        {  
          "instrument": "PI_XBTUSD",  
          "time": 1567428848005,  
          "last_update_time": 1567428848005,  
          "qty": 100.0,  
          "filled": 0.0,  
          "limit_price": 8500.0,  
          "stop_price": 0.0,  
          "type": "limit",  
          "order_id": "566942c8-a3b5-4184-a451-622b09493129",  
          "direction": 0,  
          "reduce_only": false  
        },  
        {  
          "instrument": "PI_XBTUSD",  
          "time": 1567428874347,  
          "last_update_time": 1567428874347,  
          "qty": 1501.0,  
          "filled": 0.0,  
          "limit_price": 7200.0,  
          "stop_price": 0.0,  
          "type": "limit",  
          "order_id": "fcbb1459-6ed2-4b3c-a58c-67c4df7412cf",  
          "direction": 0,  
          "reduce_only": false  
        },  
        {  
          "instrument": "PI_XBTUSD",  
          "time": 1567515137945,  
          "last_update_time": 1567515137945,  
          "qty": 102.0,  
          "filled": 0.0,  
          "limit_price": 8500.0,  
          "stop_price": 0.0,  
          "type": "limit",  
          "order_id": "3deea5c8-0274-4d33-988c-9e5a3895ccf8",  
          "direction": 0,  
          "reduce_only": false  
        }  
      ]  
    }  
    

## Response Delta

  * Response Fields
  * Subscription Delta Data
  * Cancelled subscription

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

The amount of the order that is filled.

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
      "feed": "open_orders_verbose",  
      "order": {  
        "instrument": "PI_XBTUSD",  
        "time": 1567597581495,  
        "last_update_time": 1567597581495,  
        "qty": 102.0,  
        "filled": 0.0,  
        "limit_price": 10601.0,  
        "stop_price": 0.0,  
        "type": "limit",  
        "order_id": "fa9806c9-cba9-4661-9f31-8c5fd045a95d",  
        "direction": 0,  
        "reduce_only": false  
      },  
      "is_cancel": true,  
      "reason": "post_order_failed_because_it_would_be_filled"  
    }  
      
    
    
    
    {  
      "feed": "open_orders_verbose",  
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