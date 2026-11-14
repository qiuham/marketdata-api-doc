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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/add_order'
updated_at: 2026-11-13
---

# Add Order

> Send a new order into the exchange via WebSocket

UWS
uws.kraken.com/v2/private
add\_order

Sends a single, new order into the exchange. A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below.

For triggered order types (`stop-loss`, `take-profit`, `trailing-stop`), the `triggers` section contains the parameters for price tracking and trigger thresholds.

For One-Triggers-Other (OTO) orders, the `conditional` section contains the parameters to add a secondary close order to the primary order.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `add_order`
>
> **params** `object` *required*
>
> **properties**
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **order\_type** `string` *required*
>
> One of: `limit`, `market`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`
>
> The execution model of the order.
>
> * `limit`: The full order quantity is placed immediately with a limit price restriction to only trade at this price or better.
> * `market`: The full order quantity executes immediately at the best available price in the order book.
> * `stop-loss`: A market order is triggered when the reference price reaches the stop price (from an unfavourable direction).
> * `stop-loss-limit`: A limit order is triggered when the reference price reaches the stop price (from an unfavourable direction).
> * `take-profit`: A market order is triggered when the reference price reaches the stop price (from a favourable direction).
> * `take-profit-limit`: A limit order is triggered when the reference price reaches the stop price (from a favourable direction).
> * `trailing-stop`: A market order is triggered when the market reverts a specified distance from the peak price.
> * `trailing-stop-limit`: A limit order is triggered when the market reverts a specified distance from the peak price.
>
> **side** `string` *required*
>
> One of: `buy`, `sell`
>
> Side of the order.
>
> **order\_qty** `float` *required*
>
> Order quantity in terms of the base asset.
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The symbol of the currency pair.
>
> **limit\_price** `float`
>
> Limit price for order types that support limit price restriction.
>
> **limit\_price\_type** `string`
>
> One of: `static`\\
>
> Default: `static`\\
>
> Condition: Only available on trailing-stop-limit orders
>
> The units for the limit price. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
>
> Note, for `trailing-stop-limit` order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.
>
> **triggers** `object`
>
> Condition: Required for triggered order types only
>
> The parameters for setting the trigger price conditions.
>
> **properties**
>
> **reference** `string`
>
> One of: `index`, `last`\\
>
> Default: `last`
>
> The reference price to track for triggering orders.
>
> * `index`: the index price in the broader market (for this pair). Note, to keep triggers serviceable during connectivity issues with external index feeds, the last price will be used as the reference price.
> * `last`: the last traded price in the Kraken order book (for this pair).
>
> **price** `float` *required*
>
> Specifies the amount for the trigger price - it supports both static market prices and relative prices. This field is used in combination with the `price_type` field below to determine the effective trigger price.
>
> **Examples:**
>
> * To trigger at 29000.5 BTC/USD, use price=29000.5, price\_type=static.
> * To trigger when price rises by 5%, use price=5, price\_type=pct.
> * To trigger when price drops by 150 USD, use price=-150, price\_type=quote.
>
> **price\_type** `string`
>
> One of: `static`\\
>
> Default: `static`
>
> The units for the trigger price. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
>
> **time\_in\_force** `string`
>
> One of: `gtc`, `ioc`\\
>
> Default: `gtc`
>
> Time-in-force specifies how long an order remains in effect before being expired.
>
> * `gtc`: Good Till Canceled - until user has cancelled.
> * `ioc`: Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.
>
> **margin** `boolean`
>
> One of: `false`, `true`\\
>
> Default: `false`\\
>
> Condition: Not available for derivatives (futures are inherently margined)
>
> Funds the order on margin using the maximum leverage for the pair (maximum is leverage of 5).
>
> **post\_only** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`\\
>
> Condition: Orders with limit price only
>
> Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.
>
> **reduce\_only** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.
>
> **effective\_time** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59Z`\\
>
> Condition: Not available for derivatives
>
> Scheduled start time (precision to seconds).
>
> **expire\_time** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59Z`\\
>
> Condition: Not available for derivatives
>
> Expiration time of the order (precision to seconds).
>
> **deadline** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123Z`
>
> Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
>
> **cl\_ord\_id** `string`
>
> Adds a client order identifier which uniquely identifies an open order for each client.
>
> For derivatives, `cl_ord_id` must be in UUIDv4 format:
>
> * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
>
> **order\_userref** `integer`
>
> Condition: Not available for derivatives (use `cl_ord_id` instead)
>
> This is an optional non-unique, numeric identifier which can associated with a number of orders by the client. This field is mutually exclusive with `cl_ord_id` parameter.
>
> Many clients choose a unique integer value generated by their systems (i.e. a timestamp). However, because we don't enforce uniqueness on our side, it can also be used to easily tag a group of orders for querying or cancelling.
>
> **conditional** `object`
>
> The conditional parameters are used as a template for generating the secondary close orders when the primary order fills. Each fill on the primary order will generate a new secondary order. The size of the secondary order will be the same size as the executed quantity and have the opposite side.
>
> **properties**
>
> **order\_type** `string`
>
> One of: `limit`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`
>
> Defines the order type of the secondary close orders which will be created on each fill.
>
> **limit\_price** `float`
>
> Defines the limit price on the secondary close orders. Only required on secondary order types that support limit price: `limit`, `stop-loss-limit`, `take-profit-limit`.
>
> **limit\_price\_type** `string`
>
> One of: `static`\\
>
> Default: `static`\\
>
> Condition: Only available on trailing-stop-limit orders
>
> The units for the limit price on the secondary order. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
>
> Note, for `trailing-stop-limit` order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.
>
> **trigger\_price** `float`
>
> Specifies the amount for the trigger price - it supports both static market prices and relative prices. This field is used in combination with the `price_type` field below to determine the effective trigger price.
>
> **Examples:**
>
> * To trigger at 29000.5 BTC/USD, use price=29000.5, price\_type=static.
> * To trigger when price rises by 5%, use price=5, price\_type=pct.
> * To trigger when price drops by 150 USD, use price=-150, price\_type=quote.
>
> Note, for `trailing-stop` and `trailing-stop-limit` order types, the price represents the reversion from the peak. It is always a positive offset value.
>
> **trigger\_price\_type** `string`
>
> One of: `static`\\
>
> Default: `static`
>
> The units for the trigger price. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
>
> **stop\_price** `float` *deprecated*
>
> Deprecated: Use trigger\_price
>
> Defines the trigger price on the secondary close orders. Only required on triggered secondary order types: `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`.
>
> **display\_qty** `float`
>
> Condition: Not available for derivatives
>
> Defines the quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of `order_qty`.
>
> **fee\_preference** `string`
>
> One of: `base`, `quote`\\
>
> Condition: Not available for derivatives (fee currency is fixed per contract)
>
> Fee preference base or quote currency. `quote` is the default for buy orders, `base` is the default for sell orders.
>
> **no\_mpp** `boolean` *deprecated*
>
> One of: `true`, `false`\\
>
> Default: `false`\\
>
> Condition: Market orders only\\
>
> Deprecated: If supplied, the flag is accepted but ignored
>
> Disables Market Price Protection (MPP) if set to `true`. MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market.
>
> **stp\_type** `string`
>
> One of: `cancel_newest`\\
>
> Default: `cancel_newest`
>
> Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves. Only `cancel_newest` is available for derivatives.
>
> * `cancel_newest`: arriving order will be canceled.
>
> **cash\_order\_qty** `float`
>
> Condition: Not available for derivatives
>
> Order volume expressed in quote currency.
>
> **validate** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> If set to `true` the order will be validated only, it will not trade in the matching engine.
>
> **sender\_sub\_id** `string`
>
> Condition: Not available for derivatives
>
> Adds a alphanumeric sub-account/trader identifier which enables STP to be performed at a more granular level.
>
> The `sender_sub_id` parameter can be one of the following formats:
>
> * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
> * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
> * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.
>
> **broker** `string`
>
> Format: 16 alphanumeric characters (`A-Z`, `0-9`) in 4 groups of 4\\
>
> Example: `AA16N84GV574COOQ`
>
> Broker IIBAN (Partner's Kraken IIBAN). Attributes the order to the broker placing it on behalf of their client, so partner commission can be paid.
>
> Available to qualified partners in Kraken's API Partner Program. Both spellings are accepted and are equivalent:
>
> * Grouped: `AA16 N84G V574 COOQ` with a single space between each group of 4 characters.
> * Unspaced: `AA16N84GV574COOQ` 16 characters with no separators.
>
> The order is rejected if the value is not a well-formed IIBAN, or if your account is not entitled to trade on behalf of the specified broker.
>
> **stop\_price** `float` *deprecated*
>
> Deprecated: Use 'triggers' object
>
> The stop price for trigger order types.
>
> **trigger** `string` *deprecated*
>
> One of: `last`, `index`\\
>
> Default: `last`\\
>
> Condition: Triggered order types only\\
>
> Deprecated: Use 'triggers' object
>
> The reference price to trigger the order.
>
> * `index`: the index price for the broader market for this symbol.
> * `last`: the last traded price in the order book for this symbol.
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
> **method** `string`
>
> Value: `add_order`
>
> **result** `object`
>
> **properties**
>
> **order\_id** `string`
>
> Unique order identifier generated by Kraken.
>
> **cl\_ord\_id** `string`
>
> An optional, alphanumeric identifier specified by the client in the `add_order` parameters.
>
> **order\_userref** `integer`
>
> An optional non-unique, numeric identifier specified by the client in the `add_order` parameters.
>
> **warnings** `array of string`
>
> Non-fatal warnings about the order, if any.
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **time\_in** `string`
>
> The timestamp when the request was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the response was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`

```json Limit theme={null}
{
    "method": "add_order",
    "params": {
        "asset_class": "derivatives",
        "order_type": "limit",
        "side": "buy",
        "limit_price": 26500.4,
        "order_qty": 1.2,
        "symbol": "PF_XBTUSD",
        "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    },
    "req_id": 123456789
}
```

```json Stop Loss theme={null}
{
    "method": "add_order",
    "params": {
        "asset_class": "derivatives",
        "order_type": "stop-loss",
        "side": "sell",
        "order_qty": 100,
        "symbol": "PF_XBTUSD",
        "triggers": {
            "reference": "last",
            "price": 29000.0,
            "price_type": "static"
        },
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json OTO theme={null}
{
    "method": "add_order",
    "params": {
        "asset_class": "derivatives",
        "order_type": "limit",
        "side": "buy",
        "order_qty": 1.2,
        "symbol": "PF_XBTUSD",
        "limit_price": 28440,
        "conditional": {
            "order_type": "stop-loss-limit",
            "trigger_price": 28410,
            "limit_price": 28400
        },
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Response theme={null}
{
    "method": "add_order",
    "req_id": 123456789,
    "result": {
        "order_id": "AA5JGQ-SBMRC-SCJ7J7",
        "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876"
    },
    "success": true,
    "time_in": "2023-09-21T14:15:07.197274Z",
    "time_out": "2023-09-21T14:15:07.205301Z"
}
```

```json Error theme={null}
{
    "error": "EOrder:Insufficient funds",
    "method": "add_order",
    "req_id": 123456789,
    "success": false,
    "time_in": "2023-09-21T14:15:07.197274Z",
    "time_out": "2023-09-21T14:15:07.205301Z"
}
```
