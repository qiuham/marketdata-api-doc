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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/fills'
updated_at: 2026-11-13
---

# Fills

> Subscribe to fills information for your account

WSS
futures.kraken.com/ws/v1
fills

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

This subscription feed publishes fills information.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `fills`

**product\_ids** `list`

Optionally, the `product_ids` field can be used to subscribe only to specific products.

**api\_key** `string` *required*

The user API key.

**original\_challenge** `string` *required*

The message that is received from a challenge request.

**signed\_challenge** `string` *required*

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "fills",
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

The requested subscription feed. Value: `fills`

**product\_ids** `list`

List of product identifiers to subscribe for. Other products are ignored.

**api\_key** `string`

The user API key.

**original\_challenge** `string`

The message that is received from a challenge request.

**signed\_challenge** `string`

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "fills",
  "product_ids": ["PF_XBTUSD"],
  "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",
  "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",
  "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="
}
```

***

## Response Snapshot & Delta

**feed** `string`

The subscribed feed.

**account** `string`

The user account.

**fills** `list of structures`

A list containing fill elements of the user account.

**properties**

**instrument** `string`

The fill instrument (referred also as symbol or product\_id).

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

**remaining\_order\_qty** `positive float`

The remaining unfilled quantity in the order.

**order\_id** `UUID`

The order id that was filled.

**cli\_ord\_id** `UUID`

The unique client order identifier. This field is returned only if the order has a client order id.

**fill\_id** `UUID`

The fill id.

**fill\_type** `string`

The classification of the fill: `maker` if the user has a limit order that gets filled, `taker` if the user makes an execution that crosses the spread, `liquidation` if an execution is the result of a liquidation, `assignee` if an execution is a result of a counterparty receiving an Assignment in PAS, `assignor` if an execution is a result of the user assigning their position due to a failed liquidation, `unwindBankrupt` any portion of a liquidated position cannot be filled or assigned the remaining contracts are unwound, `unwindCounterparty` any portion of your counterparty's position is liquidated and cannot be filled or assigned the remaining contracts are unwound, `takerAfterEdit` if the user edits the order and it is instantly executed.

**fee\_paid** `positive float`

Fee paid on fill.

**fee\_currency** `string`

Currency in which the fee was charged.

**taker\_order\_type** `string`

The order type of the taker execution: `lmt`, `ioc`, `post`, `liquidation`, `assignment`, `stp`, `unwind`, `market`, `block`, `coveredLiquidation`, `hedgeImmediateOrCancel`, `hedgeAssignment`, `fillOrKill`.

**order\_type** `string`

The order type associated with the fill: `lmt`, `ioc`, `post`, `liquidation`, `assignment`, `stp`, `unwind`, `market`, `block`, `coveredLiquidation`, `hedgeImmediateOrCancel`, `hedgeAssignment`, `fillOrKill`.

```json Example: Snapshot theme={null}
{
  "feed": "fills_snapshot",
  "account": "DemoUser",
  "fills": [
    {
      "instrument": "PF_XBTUSD",
      "time": 1600256910739,
      "price": 10937.5,
      "seq": 36,
      "buy": true,
      "qty": 5000.0,
      "remaining_order_qty": 0.0,
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
      "remaining_order_qty": 0.0,
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
