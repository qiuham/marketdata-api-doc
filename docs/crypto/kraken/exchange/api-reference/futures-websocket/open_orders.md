---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/open_orders'
updated_at: 2026-11-13
---

# Open Orders

> Subscribe to open orders information for your account

WSS
futures.kraken.com/ws/v1
open\_orders

> [!WARNING]
>
> **Derivatives WebSocket is being deprecated.** For new integrations, use the
> [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket), which streams
> Spot and Derivatives over a single connection. Existing integrations continue
> to work until **1 March 2027**, when the Derivatives WebSocket will no
> longer be available. Migrate to the Unified WebSocket before then.
>
> To use private channels or trade on the Unified WebSocket, you need a
> Kraken API key, not a Derivatives API key. Use it to get a token from
> [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token). See
> [Unified WebSocket authentication](https://docs.kraken.com/exchange/api-reference/unified-websocket#authentication).

This subscription feed publishes information about user open orders.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `open_orders`

**api\_key** `string` *required*

The user API key.

**original\_challenge** `string` *required*

The message that is received from a challenge request.

**signed\_challenge** `string` *required*

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "open_orders",
  "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",
  "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",
  "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `open_orders`

**api\_key** `string`

The user API key.

**original\_challenge** `string`

The message that is received from a challenge request.

**signed\_challenge** `string`

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "open_orders",
  "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",
  "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",
  "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="
}
```

***

## Response Snapshot

**feed** `string`

The subscribed feed.

**account** `string`

The user account.

**orders** `list of structures`

The user open orders.

**properties**

**instrument** `string`

The instrument (referred also as symbol or product\_id) of the order.

**time** `positive integer`

The UTC time in milliseconds.

**last\_update\_time** `positive integer`

The UTC time in milliseconds that the order was last updated.

**qty** `positive float`

The quantity of the order.

**filled** `positive float`

The total amount of the order that is filled.

**limit\_price** `positive float`

The limit price of the order.

**stop\_price** `positive float`

The stop price of the order.

**type** `string`

The order type: `limit`, `take_profit`, or `stop`.

**order\_id** `UUID`

The order id.

**cli\_ord\_id** `UUID`

The unique client order identifier. This field is returned only if the order has a client order id.

**direction** `integer`

The direction of the order, either 0 for a buy order or 1 for a sell order.

**reduce\_only** `boolean`

If true, the order can only reduce open positions, it cannot increase or open new positions.

**triggerSignal** `string`

Trigger signal selected for take profit or stop loss order. Options are `last`, `mark`, or `spot`. Returned only for take profit or stop loss orders.

**trailing\_stop\_options** `list of structures`

If this order is a trailing stop, this contains its parameters.

**properties**

**max\_deviation** `double`

The maximum distance the trigger price may be away from the trigger signal.

**unit** `string`

One of: `percent`, `quote_currency`

The unit of the deviation.

```json Example theme={null}
{
  "feed": "open_orders_snapshot",
  "account": "e258dba9-4dd4-4da5-bfef-75beb91c098e",
  "orders": [
    {
      "instrument": "PF_XBTUSD",
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
      "instrument": "PF_XBTUSD",
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
      "instrument": "PF_XBTUSD",
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
```

***

## Response Delta

**feed** `string`

The subscribed feed.

**order** `structure`

The user order.

**properties**

**instrument** `string`

The instrument (referred also as symbol or product\_id) of the order.

**time** `positive integer`

The UTC time in milliseconds.

**last\_update\_time** `positive integer`

The UTC time in milliseconds that the order was last updated.

**qty** `positive float`

The quantity of the order.

**filled** `positive float`

The total amount of the order that is filled.

**limit\_price** `positive float`

The limit price of the order.

**stop\_price** `positive float`

The stop price of the order.

**type** `string`

The order type: `limit`, `take_profit`, or `stop`.

**order\_id** `UUID`

The order id.

**cli\_ord\_id** `UUID`

The unique client order identifier. This field is returned only if the order has a client order id.

**direction** `integer`

The direction of the order, either 0 for a buy order or 1 for a sell order.

**reduce\_only** `boolean`

If true, the order can only reduce open positions, it cannot increase or open new positions.

**triggerSignal** `string`

Trigger signal selected for take profit or stop loss order. Options are `last`, `mark`, or `spot`. Returned only for take profit or stop loss orders.

**trailing\_stop\_options** `list of structures`

If this order is a trailing stop, this contains its parameters.

**properties**

**max\_deviation** `double`

The maximum distance the trigger price may be away from the trigger signal.

**unit** `string`

One of: `percent`, `quote_currency`

The unit of the deviation.

**is\_cancel** `boolean`

If false the open order has been either placed or partially filled and needs to be updated. If true the open order was either fully filled, cancelled or rejected (for post-only). If it was filled or cancelled it must be removed from open orders snapshot.

**reason** `string`

Reason behind the received delta:

* `new_placed_order_by_user`: User placed a new order
* `liquidation`: User position liquidated. The order cancelled
* `stop_order_triggered`: A stop order triggered. The system removed the stop order
* `limit_order_from_stop`: The system created a limit order because an existing stop order triggered
* `partial_fill`: The order filled partially
* `full_fill`: The order filled fully and removed
* `cancelled_by_user`: The order cancelled by the user and removed
* `contract_expired`: The order contract expired. All open orders of that contract removed
* `not_enough_margin`: The order removed due to insufficient margin
* `market_inactive`: The order removed because market became inactive
* `cancelled_by_admin`: The order removed by administrator's action
* `dead_man_switch`: The order removed because dead man's switch was triggered
* `ioc_order_failed_because_it_would_not_be_executed`: The immediate or cancel order was rejected due to insufficient liquidity
* `post_order_failed_because_it_would_filled`: The post only order was rejected as it crosses the spread and would be immediately filled
* `would_execute_self`: The order was rejected as it would execute against another order from the same account
* `would_not_reduce_position`: The order was rejected as the reduce-only option was selected and it would not reduce the position
* `order_for_edit_not_found`: The order edit was rejected as the order to be edited could not be found

```json Example: New Order theme={null}
{
  "feed": "open_orders",
  "order": {
    "instrument": "PF_XBTUSD",
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
```

```json Example: Cancelled Order theme={null}
{
  "feed": "open_orders",
  "order_id": "660c6b23-8007-48c1-a7c9-4893f4572e8c",
  "is_cancel": true,
  "reason": "cancelled_by_user"
}
```

***

## Response Error

**event** `string`

Value: `error`

**message** `string`

One of: `Invalid feed`, `Json Error`

An error message.

```json Example theme={null}
{
  "event": "error",
  "message": "Invalid feed"
}
```
