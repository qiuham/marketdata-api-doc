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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/open_orders_verbose'
updated_at: 2026-11-13
---

# Open Orders (Verbose)

> Subscribe to verbose open orders information including failed post-only orders

WSS
futures.kraken.com/ws/v1
open\_orders\_verbose

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

This subscription feed publishes information about user open orders. This feed adds extra information about all the post-only orders that failed to cross the book.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `open_orders_verbose`

**api\_key** `string` *required*

The user API key.

**original\_challenge** `string` *required*

The message that is received from a challenge request.

**signed\_challenge** `string` *required*

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "open_orders_verbose",
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

The requested subscription feed. Value: `open_orders_verbose`

**api\_key** `string`

The user API key.

**original\_challenge** `string`

The message that is received from a challenge request.

**signed\_challenge** `string`

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "open_orders_verbose",
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

The total amount of the order that has been filled.

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

```json Example theme={null}
{
  "feed": "open_orders_verbose_snapshot",
  "account": "0f9c23b8-63e2-40e4-9592-6d5aa57c12ba",
  "orders": [
    {
      "instrument": "PF_XBTUSD",
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
      "instrument": "PF_XBTUSD",
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
      "instrument": "PF_XBTUSD",
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

The amount of the order that is filled.

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

```json Example: Post-Only Rejected theme={null}
{
  "feed": "open_orders_verbose",
  "order": {
    "instrument": "PF_XBTUSD",
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
```

```json Example: Cancelled Order theme={null}
{
  "feed": "open_orders_verbose",
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
