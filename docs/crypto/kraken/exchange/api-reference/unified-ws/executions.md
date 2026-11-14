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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/executions'
updated_at: 2026-11-13
---

# Executions

> Subscribe to order status and execution events for your account

UWS
uws.kraken.com/v2/private
executions

The `executions` channel streams order status and execution events for this account.

It corresponds to a combination of the following Websockets v1 channels: `openOrders` and `ownTrades`.

This channel contains account specific data, an authentication token is required in the request.

## Subscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `executions`
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **snap\_trades** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> If `true`, the last 50 order fills will be included in snapshot.
>
> **snap\_orders** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> If `true`, open orders will be included in snapshot.
>
> **order\_status** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> If `true`, all possible status transitions will be sent. Otherwise, only open / close transitions will be streamed: `new`, `filled`, `canceled`, `expired`.
>
> **ratecounter** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> If `true`, the rate-limit counter is included in the stream.
>
> **snapshot\_trades** `boolean` *deprecated*
>
> One of: `true`, `false`\\
>
> Deprecated: Use 'snap\_trades' field
>
> If `true`, snapshot provides only trade events. Otherwise, open orders and trades will be included in snapshot.
>
> **snapshot** `boolean` *deprecated*
>
> One of: `true`, `false`\\
>
> Deprecated: Use 'snap\_orders' or 'snap\_trades' field
>
> Request a snapshot after subscribing.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `executions`
>
> **snap\_orders** `boolean`
>
> One of: `true`, `false`
>
> Indicates if a snapshot of orders is requested.
>
> **snap\_trades** `boolean`
>
> One of: `true`, `false`
>
> Indicates if a snapshot of trades is requested.
>
> **maxratecount** `integer`
>
> Specifies the max rate counter value for the user transaction rate. It is based on user tier.
>
> **snapshot** `boolean` *deprecated*
>
> Deprecated: Use 'snap\_trades' and 'snap\_orders'
>
> Indicates if a snapshot is requested.
>
> **warnings** `string[]`
>
> An advisory message, highlighting deprecated fields or upcoming changes to the channel.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot / Update

The snapshot and update stream share the same data schema. The fields included depend on the asset class and `exec_type`.

By default, the snapshot response contains all open orders and latest 50 trades.

The snapshot message content can be adjusted with the subscription parameters.

### Order lifecycle by asset class

`exec_type` describes the event; `order_status` describes the order's state. The examples below are grouped by asset class because the event sequences differ.

* **Spot:** `pending_new` acknowledges a validated order before it becomes live, followed by `new` when it is live. A `trade` event can report `order_status: partially_filled` even when that trade fills the entire order. A separate `exec_type: filled` update reports completion; do not infer remaining quantity from that intermediate status alone.
* **Derivatives:** there is no `pending_new` event. A live order is reported with `exec_type: new`. Trade events use `order_status: partially_filled` while quantity remains and `order_status: filled` when `remaining_qty` reaches zero. A single full fill therefore reports `filled` directly, without an intermediate `partially_filled` event or a separate `exec_type: filled` event.

`new` and the `filled` order status apply to both asset classes. Examples illustrate ordinary limit orders, not a mandatory sequence for every order type.

**channel** `string`

Value: `executions`

**type** `string`

One of: `snapshot`, `update`

**data** `object[]`

A list of execution reports: order status and fills.

**properties**

**amended** `boolean`

One of: `true`, `false`

Indicates if the order has been amended, the modification history can be extracted from the REST `OrderAmends` endpoint. This field is present in the snapshot and the `amended`, `restated` event types.

**avg\_price** `float`

Order's average fill price.

**cash\_order\_qty** `float`

Order volume expressed in quote currency (if specified on the original order).

**cl\_ord\_id** `string`

Optional client identifier associated with the order.

**contingent** `object`

The contingent object describes the template for generating the secondary close orders when the primary order fills.

**properties**

**order\_type** `string`

One of: `limit`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`

Describes the order type of the secondary orders which will be created on each fill.

**trigger\_price** `float`

Condition: Only on triggered secondary order types

Describes the trigger price amount on the secondary orders. This field is used in combination with the `contingent.trigger_price_type` field to determine the effective trigger price.

**trigger\_price\_type** `string`

One of: `static`, `pct`, `quote`\\

Condition: Only on triggered secondary order types

Describes trigger price units on the secondary orders.

* `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
* `pct`: a percentage offset from the reference price, i.e. -10% from index price.
* `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

**limit\_price** `float`

Condition: Only on secondary order types that support limit price

Describes limit price amount on the secondary orders. This field is used in combination with the `contingent.limit_price_type` field to determine the effective limit price.

**limit\_price\_type** `string`

One of: `static`, `pct`, `quote`\\

Condition: Only on secondary order types that support limit price

Describes limit price units on the secondary orders.

* `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
* `pct`: a percentage offset from the reference price, i.e. -10% from index price.
* `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

**cost** `float`

Condition: trade events only

Value of an individual execution.

**cum\_cost** `float`

The order cumulative value executed.

**cum\_qty** `float`

The order cumulative executed quantity.

**display\_qty** `float`

Display quantity for iceberg order types.

**display\_qty\_remain** `float`

Condition: Iceberg Order

Indicates next display\_qty in Iceberg order.

**effective\_time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

Scheduled start time of the order.

**exec\_id** `string`

Condition: trade events only

Execution identifier.

**exec\_type** `string`

One of: `pending_new`, `new`, `trade`, `filled`, `iceberg_refill`, `canceled`, `expired`, `amended`, `restated`, `status`

Describes the type of order event and determines the set of fields in the message.

* `pending_new`: Spot only. Order request has been received and validated but the order is not live yet.
* `new`: Order has been created and is live in the engine.
* `trade`: The order has received a fill.
* `filled`: Spot completion event. Derivatives report completion as `exec_type: trade` with `order_status: filled`.
* `canceled`: The order has been cancelled.
* `iceberg_refill`: Indicates an Iceberg order refill.
* `expired`: The order has expired.
* `amended`: There is a user initiated amend on the order, i.e. limit price change.
* `restated`: There is a engine initiated amend on the order for maintenance of position or book, see `reason` field, i.e. reduce non-tradable liquidity.
* `status`: The order has a status update, i.e. trigger price has been updated.

**expire\_time** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

Scheduled expiration time of the order.

**ext\_ord\_id** `string`

Format: UUID

An optional, external partner order identifier shown on order events.

**ext\_exec\_id** `string`

Format: UUID

An optional, external partner execution identifier shown on trade events.

**fees** `object[]`

Condition: trade events only

The fees paid on this trade event. Currently, the fees are expressed in the quote currency only.

**properties**

**asset** `string`

The fee currency.

**qty** `float`

The fee amount.

**fee\_ccy\_pref** `string`

The preferred currency for paying fees.

* `fcib`: prefer fee in base currency.
* `fciq`: prefer fee in quote currency.

**fee\_usd\_equiv** `float`

The total fee paid in USD.

**limit\_price** `float`

Limit price for order types that support limit price restriction.

**liquidated** `boolean`

Indicates if the order has been liquidated by the engine.

**liquidity\_ind** `string`

One of: `m`, `t`

The liquidity indicator: `t` taker, `m` maker.

**last\_price** `float`

Condition: trade events only

The average price in this trade event.

**last\_qty** `float`

Condition: trade events only

The quantity filled in this trade event.

**margin** `boolean`

Indicates if the order can be funded on margin.

**margin\_borrow** `boolean`

Indicates if an execution is on margin, i.e. if the trade increased or reduced size of margin borrowing. On trade events only.

**no\_mpp** `boolean`

Indicates if the order has market price protection.

**ord\_ref\_id** `string`

Referral order transaction id that created this order.

**order\_id** `string`

Unique order identifier generated by Kraken.

**order\_qty** `float`

The client order quantity.

**order\_type** `string`

One of: `limit`, `market`, `iceberg`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`, `settle-position`, `rfq`

The execution model of the order. `rfq` marks a trade from an accepted RFQ offer; see the [`quotes`](https://docs.kraken.com/exchange/api-reference/unified-ws/quotes) channel.

**order\_status** `string`

Describes current state of the order.

* `pending_new`: Spot only. Order has been received but not yet created by the engine.
* `new`: Order is live but has no fills.
* `partially_filled`: The order has fills. For derivatives, quantity remains; Spot trade events may also use this status for the final fill before the completion update.
* `filled`: The order has been fully filled.
* `canceled`: The order has been cancelled.
* `expired`: The order has expired.

**order\_userref** `integer`

Optional numeric, client identifier associated with one or more orders.

**post\_only** `boolean`

One of: `true`, `false`

Indicates a post only order.

**position\_status** `string`

One of: `opened`, `closing`, `closed`

Indicates status of the position on a margin order.

**ratecount** `integer`

Condition: Published when request parameters have 'ratecounter=true'

The value of the user's trading rate-limit counter at the time of the event, as evaluated by the trading engine.

**reason** `string`

The reason associated with an event, if applicable.

**reduce\_only** `boolean`

One of: `true`, `false`

Indicates a reduce only order.

**sender\_sub\_id** `string`

For institutional accounts, identifies underlying sub-account/trader for Self Trade Prevention (STP).

**sequence\_id** `string`

Condition: `derivatives` trade events only\\

Example: `"987654321"`

Per-market monotonic sequential trade identifier assigned by the matching engine, sent as a decimal string to preserve full 64-bit precision.

Both sides of a fill carry the same `sequence_id`, so the maker and taker events for one execution share a value. Use it to order fills within a single `symbol`; values are not comparable across symbols and are not guaranteed to be contiguous. A value of `"0"` means the engine did not assign a sequence to the fill.

**side** `string`

One of: `buy`, `sell`

Side of the order.

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**time\_in\_force** `string`

One of: `GTC`, `GTD`, `IOC`, `FOK`

Time-in-force specifies how long an order remains in effect before being expired.

* `GTC`: Good Till Canceled
* `GTD`: Good Till Date
* `IOC`: Immediate Or Cancel
* `FOK`: Fill Or Kill

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

Time of the event.

**trade\_id** `integer`

The trade identifier.

**triggers** `object`

Describes the parameters and status of the price trigger for triggered order types.

**properties**

**reference** `string`

One of: `index`, `last`

The reference price tracked for triggering orders.

**price** `float`

Specifies the amount for the trigger price - it supports both static market prices and relative prices. This field is used in combination with the `price_type` field below to determine the effective trigger price.

**price\_type** `string`

One of: `static`, `pct`, `quote`

The units for the trigger price.

* `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
* `pct`: a percentage offset from the reference price, i.e. -10% from index price.
* `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

**actual\_price** `float`

The current value of the effective trigger price, this is useful if the trigger was entered using a relative price or the trigger price changes over time.

**peak\_price** `float`

The peak / trough price on `trailing-stop` and `trailing-stop-limit` orders.

**last\_price** `float`

On trigger activation, the value of the reference last price that triggered the order.

**status** `string`

One of: `triggered`, `untriggered`

The status is set to `triggered` when the trigger conditions are met and the order becomes active.

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

On trigger activation, the timestamp of the trigger event.

**cancel\_reason** `string` *deprecated*

Deprecated: Use 'reason' field

Cancellation reason.

**stop\_price** `float` *deprecated*

Deprecated: Use 'triggers' object

The stop price for triggered order types.

**trigger** `string` *deprecated*

One of: `index`, `last`\\

Deprecated: Use 'triggers' object

Reference price for triggered order types.

**triggered\_price** `float` *deprecated*

Deprecated: Use 'triggers' object

Price which triggered the order.

**sequence** `integer`

The subscription message sequence number.

## Unsubscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `executions`
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `executions`
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

```json Subscribe Request theme={null}
{
    "method": "subscribe",
    "params": {
        "channel": "executions",
        "asset_class": "derivatives",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY",
        "snap_orders": true,
        "snap_trades": true
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "executions",
        "maxratecount": 125,
        "snap_orders": true,
        "snap_trades": true
    },
    "success": true,
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```

> [tab] Spot
>
> ```json Pending theme={null}
> {
>     "channel": "executions",
>     "type": "update",
>     "data": [
>         {
>             "order_id": "OK4GJX-KSTLS-7DZZO5",
>             "order_userref": 3,
>             "symbol": "BTC/USD",
>             "order_qty": 0.005,
>             "cum_cost": 0.0,
>             "time_in_force": "GTC",
>             "exec_type": "pending_new",
>             "side": "sell",
>             "order_type": "limit",
>             "limit_price_type": "static",
>             "limit_price": 26500.0,
>             "stop_price": 0.0,
>             "order_status": "pending_new",
>             "fee_usd_equiv": 0.0,
>             "fee_ccy_pref": "fciq",
>             "timestamp": "2023-09-22T10:33:05.709950Z"
>         }
>     ],
>     "sequence": 8,
>     "asset_class": "spot"
> }
> ```
>
> ```json Live order theme={null}
> {
>     "channel": "executions",
>     "type": "update",
>     "data": [
>         {
>             "timestamp": "2023-09-22T10:33:05.709982Z",
>             "order_status": "new",
>             "exec_type": "new",
>             "order_userref": 3,
>             "order_id": "OK4GJX-KSTLS-7DZZO5"
>         }
>     ],
>     "sequence": 9,
>     "asset_class": "spot"
> }
> ```
>
> ```json Trade (full quantity) theme={null}
> {
>     "channel": "executions",
>     "type": "update",
>     "data": [
>         {
>             "order_id": "OK4GJX-KSTLS-7DZZO5",
>             "order_userref": 3,
>             "exec_id": "TGBB7L-HT5LX-J3BZ4A",
>             "exec_type": "trade",
>             "trade_id": 62887576,
>             "symbol": "BTC/USD",
>             "side": "sell",
>             "last_qty": 0.005,
>             "last_price": 26599.9,
>             "liquidity_ind": "t",
>             "cost": 132.9995,
>             "order_type": "limit",
>             "timestamp": "2023-09-22T10:33:05.709993Z",
>             "order_status": "partially_filled",
>             "cum_qty": 0.005,
>             "cum_cost": 132.9995,
>             "avg_price": 26599.9,
>             "fee_usd_equiv": 0.3458,
>             "fees": [
>                 {
>                     "asset": "USD",
>                     "qty": 0.3458
>                 }
>             ]
>         }
>     ],
>     "sequence": 10,
>     "asset_class": "spot"
> }
> ```
>
> ```json Filled theme={null}
> {
>     "channel": "executions",
>     "asset_class": "spot",
>     "type": "update",
>     "data": [
>         {
>             "order_id": "OK4GJX-KSTLS-7DZZO5",
>             "exec_type": "filled",
>             "order_status": "filled",
>             "timestamp": "2023-09-22T10:33:05.710000Z"
>         }
>     ],
>     "sequence": 11
> }
> ```

> [tab] Derivatives
>
> ```json Live order theme={null}
> {
>     "channel": "executions",
>     "asset_class": "derivatives",
>     "type": "update",
>     "data": [
>         {
>             "exec_type": "new",
>             "order_status": "new",
>             "order_id": "1c2d3e4f-5a6b-7c8d-9e0f-1a2b3c4d5e6f",
>             "symbol": "PF_XBTUSD",
>             "side": "buy",
>             "order_type": "limit",
>             "time_in_force": "GTC",
>             "order_qty": 0.8,
>             "remaining_qty": 0.8,
>             "cum_qty": 0,
>             "limit_price": 50000,
>             "timestamp": "2024-03-31T15:46:39.000000Z"
>         }
>     ]
> }
> ```
>
> ```json Partial fill theme={null}
> {
>     "channel": "executions",
>     "asset_class": "derivatives",
>     "type": "update",
>     "data": [
>         {
>             "exec_type": "trade",
>             "order_status": "partially_filled",
>             "trade_id": "8f1a2b3c-4d5e-6f70-8192-a3b4c5d6e7f8",
>             "order_id": "1c2d3e4f-5a6b-7c8d-9e0f-1a2b3c4d5e6f",
>             "sequence_id": "987654321",
>             "symbol": "PF_XBTUSD",
>             "side": "buy",
>             "last_qty": 0.5,
>             "last_price": 50000.0,
>             "remaining_qty": 0.3,
>             "cum_qty": 0.5,
>             "liquidity_ind": "m",
>             "order_type": "limit",
>             "fee": 1.25,
>             "timestamp": "2024-03-31T15:46:40.000000Z",
>             "order_qty": 0.8,
>             "time_in_force": "GTC"
>         }
>     ]
> }
> ```
>
> ```json Final fill theme={null}
> {
>     "channel": "executions",
>     "asset_class": "derivatives",
>     "type": "update",
>     "data": [
>         {
>             "exec_type": "trade",
>             "order_status": "filled",
>             "trade_id": "9f1a2b3c-4d5e-4f70-8192-a3b4c5d6e7f8",
>             "order_id": "1c2d3e4f-5a6b-7c8d-9e0f-1a2b3c4d5e6f",
>             "sequence_id": "987654322",
>             "symbol": "PF_XBTUSD",
>             "side": "buy",
>             "last_qty": 0.3,
>             "last_price": 50000.0,
>             "remaining_qty": 0,
>             "cum_qty": 0.8,
>             "liquidity_ind": "m",
>             "order_type": "limit",
>             "fee": 0.75,
>             "timestamp": "2024-03-31T15:46:41.000000Z",
>             "order_qty": 0.8,
>             "time_in_force": "GTC"
>         }
>     ]
> }
> ```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "executions",
        "asset_class": "derivatives",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "executions"
    },
    "success": true,
    "time_in": "2023-10-16T13:18:35.303171Z",
    "time_out": "2023-10-16T13:18:35.318297Z"
}
```
