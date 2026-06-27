---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/fills
api_type: WebSocket
updated_at: 2026-05-27 19:55:21.596945
---

# Fills

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    fills

This subscription feed publishes fills information.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `fills`

**product_ids** `list`

Optionally, the `product_ids` field can be used to subscribe only to specific product. 

**api_key** `string` *required*

The user api key

**original_challenge** `string` *required*

The message that is received from a challenge request

**signed_challenge** `string` *required*

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribe",  
      "feed": "fills",  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge":"RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `fills`

**product_ids** `list`

List of product identifiers to subscribe for. Other products are ignored. 

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "fills",  
      "product_ids": ["FI_XBTUSD_200925"],  
      "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",  
      "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",  
      "signed_challenge":"RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="  
    }  
    

## Response Snapshot & Delta

  * Response Fields
  * Subscription Snapshot Data

### MESSAGE BODY

**feed** `string`

The subscribed feed

**account** `string`

The user account.

**fills** `list of structures`

A list containing fill elements of the user account. 

**instrument** `string`

The fill instrument (referred also as symbol or product_id).

**time** `positive integer`

The server UTC date and time in milliseconds.

**price** `positive float`

The price at which the order was filled.

**seq** `positive integer`

The subscription message sequence number.

**buy** `boolean`

A flag that shows if filled order was a buy.

**qty** `positive float`

The quantity that was filled.

**remaining_order_qty** `positive float`

he remaining unfilled quantity in the order.

**order_id** `UUID`

The order id that was filled.

**cli_ord_id** `UUID`

The unique client order identifier. This field is returned only if the order has a client order id.

**fill_id** `UUID`

The fill id.

**fill_type** `string`

The classification of the fill:  
`maker` if the user has a limit order that gets filled,  
`taker` if the user makes an execution that crosses the spread,  
`liquidation` if an execution is the result of a liquidation,  
`assignee` if an execution is a result of a counterparty receiving an Assignment in PAS,  
`assignor` if an execution is a result of the user assigning their position due to a failed liquidation,  
`unwindBankrupt` any portion of a liquidated position cannot be filled or assigned, the remaining contracts are unwound.  
`unwindCounterparty` any portion of your counterparty's position is liquidated and cannot be filled or assigned the remaining contracts are unwound. More information on our Equity Protection Process.  
`takerAfterEdit` if the user edits the order and it is instantly executed.

**fee_paid** `positive float`

Fee paid on fill.

**fee_currency** `string`

Currency in which the fee was charged. See "Currencies" on Ticker Symbols.

**taker_order_type** `string`

The order type of the taker execution:  
`lmt` limit order,  
`ioc` immediate-or-cancel order,  
`post` post-only order,  
`liquidation` order resulting from a liquidation,  
`assignment` order resulting from an assignment,  
`stp` stop order,  
`unwind` order resulting from an unwind process,  
`market` market order,  
`block` block trade order,  
`coveredLiquidation` covered liquidation order,  
`hedgeImmediateOrCancel` hedge IOC order,  
`hedgeAssignment` hedge assignment order,  
`fillOrKill` fill-or-kill order.

**order_type** `string`

The order type associated with the fill:  
`lmt` limit order,  
`ioc` immediate-or-cancel order,  
`post` post-only order,  
`liquidation` order resulting from a liquidation,  
`assignment` order resulting from an assignment,  
`stp` stop order,  
`unwind` order resulting from an unwind process,  
`market` market order,  
`block` block trade order,  
`coveredLiquidation` covered liquidation order,  
`hedgeImmediateOrCancel` hedge IOC order,  
`hedgeAssignment` hedge assignment order,  
`fillOrKill` fill-or-kill order.
    
    
    {  
      "feed": "fills_snapshot",  
      "account": "DemoUser",  
      "fills": [  
        {  
          "instrument": "FI_XBTUSD_200925",  
          "time": 1600256910739,  
          "price": 10937.5,  
          "seq": 36,  
          "buy": true,  
          "qty": 5000.0,  
          "remaining_order_qty":0.0,  
          "order_id": "9e30258b-5a98-4002-968a-5b0e149bcfbf",  
          "fill_id": "cad76f07-814e-4dc6-8478-7867407b6bff",  
          "fill_type": "maker",  
          "fee_paid": -0.00009142857,  
          "fee_currency": "BTC",  
          "taker_order_type": "ioc",  
          "order_type": "limit"  
        },  
        {  
          "instrument": "PI_ETHUSD",  
          "time": 1600256945531,  
          "price": 364.65,  
          "seq": 39,  
          "buy": true,  
          "qty": 5000.0,  
          "remaining_order_qty":0.0,  
          "order_id": "7e60b6e8-e4c2-4ce8-bbd0-ef81e18b65bb",  
          "fill_id": "b1aa44b2-4f2a-4031-999c-ae1175c91580",  
          "fill_type": "taker",  
          "fee_paid": 0.00685588921,  
          "fee_currency": "ETH",  
          "taker_order_type": "market",  
          "order_type": "limit"  
        }  
      ]  
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