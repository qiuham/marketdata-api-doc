---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/add-order
api_type: REST
updated_at: 2026-07-23 19:20:23.061187
---

# Add Order

{
        "method": "add_order",
        "params": {
            "order_type": "limit",
            "side": "buy",
            "limit_price": 26500.4,
            "order_userref": 100054,
            "order_qty": 1.2,
            "symbol": "BTC/USD",
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
        },
        "req_id": 123456789
    }
    
    
    
    {
        "method": "add_order",
        "params": {
            "order_type": "stop-loss",
            "side": "sell",
            "order_qty": 100,
            "symbol": "MATIC/USD",
            "triggers": {
                "reference": "last",
                "price": -2.0,
                "price_type": "pct"
            },
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
        }
    }
    
    
    
    {
        "method": "add_order",
        "params": {
            "order_type": "limit",
            "side": "buy",
            "order_qty": 1.2,
            "symbol": "BTC/USD",
            "limit_price": 28440,
            "conditional": {
                "order_type": "stop-loss-limit",
                "trigger_price": 28410,
                "limit_price": 28400
            },
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
        }
    }
    
    
    
    {
        "method": "add_order",
        "req_id": 123456789,
        "result": {
            "order_id": "AA5JGQ-SBMRC-SCJ7J7",
            "order_userref": 100054
        },
        "success": true,
        "time_in": "2023-09-21T14:15:07.197274Z",
        "time_out": "2023-09-21T14:15:07.205301Z"
    }
    
    
    
    {
        "error": "EOrder:Insufficient funds",
        "method": "add_order",
        "req_id": 123456789,
        "success": false,
        "time_in": "2023-09-21T14:15:07.197274Z",
        "time_out": "2023-09-21T14:15:07.205301Z"
    }
    
    
    
    {
        "method": "add_order",
        "params": {
            "order_type": "limit",
            "side": "buy",
            "limit_price": 26500.4,
            "order_userref": 100054,
            "order_qty": 1.2,
            "symbol": "BTC/USD",
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
        },
        "req_id": 123456789
    }
    
    
    
    {
        "method": "add_order",
        "params": {
            "order_type": "stop-loss",
            "side": "sell",
            "order_qty": 100,
            "symbol": "MATIC/USD",
            "triggers": {
                "reference": "last",
                "price": -2.0,
                "price_type": "pct"
            },
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
        }
    }
    
    
    
    {
        "method": "add_order",
        "params": {
            "order_type": "limit",
            "side": "buy",
            "order_qty": 1.2,
            "symbol": "BTC/USD",
            "limit_price": 28440,
            "conditional": {
                "order_type": "stop-loss-limit",
                "trigger_price": 28410,
                "limit_price": 28400
            },
            "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
        }
    }
    
    
    
    {
        "method": "add_order",
        "req_id": 123456789,
        "result": {
            "order_id": "AA5JGQ-SBMRC-SCJ7J7",
            "order_userref": 100054
        },
        "success": true,
        "time_in": "2023-09-21T14:15:07.197274Z",
        "time_out": "2023-09-21T14:15:07.205301Z"
    }
    
    
    
    {
        "error": "EOrder:Insufficient funds",
        "method": "add_order",
        "req_id": 123456789,
        "success": false,
        "time_in": "2023-09-21T14:15:07.197274Z",
        "time_out": "2023-09-21T14:15:07.205301Z"
    }
    

WSSws-auth.kraken.com/v2add_order

Sends a single, new order into the exchange. A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below. For triggered order types (`stop-loss`, `take-profit`, `trailing-stop`), the `triggers` section contains the parameters for price tracking and trigger thresholds. For One-Triggers-Other (OTO) orders, the `conditional` section contains the parameters to add a secondary close order to the primary order.

  * Request

  * Response

string

required

Value: `add_order`

object

required

Hide properties

string

required

One of: `limit`, `market`, `iceberg`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`, `settle-position`The execution model of the order.

  * `limit`: The full order quantity is placed immediately with a limit price restriction to only trade at this price or better.
  * `market`: The full order quantity executes immediately at the best available price in the order book.
  * `iceberg`: Hides the full order size by only showing your chosen display size in the book at your limit price.
  * `stop-loss`: A market order is triggered when the reference price reaches the stop price (from an unfavourable direction).
  * `stop-loss-limit`: A limit order is triggered when the reference price reaches the stop price (from an unfavourable direction).
  * `take-profit`: A market order is triggered when the reference price reaches the stop price (from a favourable direction).
  * `take-profit-limit`: A limit order is triggered when the reference price reaches the stop price (from a favourable direction).
  * `trailing-stop`: A market order is triggered when the market reverts a specified distance from the peak price.
  * `trailing-stop-limit`: A limit order is triggered when the market reverts a specified distance from the peak price.
  * `settle-position`: Settles an open leveraged position at the current market price.

string

required

One of: `buy`, `sell`Side of the order.

float

required

Order quantity in terms of the base asset.

string

required

Example: `"BTC/USD"`The symbol of the currency pair.

float

Limit price for order types that support limit price restriction.

string

One of: `static`, `pct`, `quote`  
Default: `quote`  
Condition: Only available on trailing-stop-limit ordersThe units for the limit price.

  * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
  * `pct`: a percentage offset from the reference price, i.e. -10% from index price.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

Note, for `trailing-stop-limit` order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.

object

Condition: Required for triggered order types onlyThe parameters for setting the trigger price conditions.

Hide properties

string

One of: `index`, `last`  
Default: `last`The reference price to track for triggering orders.

  * `index`: the index price in the broader market (for this pair). Note, to keep triggers serviceable during connectivity issues with external index feeds, the last price will be used as the reference price.
  * `last`: the last traded price in the Kraken order book (for this pair).

float

required

Specifies the amount for the trigger price - it supports both static market prices and relative prices. This field is used in combination with the `price_type` field below to determine the effective trigger price.**Examples:**

  * To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
  * To trigger when price rises by 5%, use price=5, price_type=pct.
  * To trigger when price drops by 150 USD, use price=-150, price_type=quote.

string

One of: `static`, `pct`, `quote`  
Default: `static`The units for the trigger price.

  * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
  * `pct`: a percentage offset from the reference price, i.e. -10% from index price.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

Note, for `trailing-stop` and `trailing-stop-limit` order types, the price represents the reversion from the peak. It is always a positive value with `pct` or `quote` offset.

string

One of: `gtc`, `gtd`, `ioc`, `fok`  
Default: `gtc`Time-in-force specifies how long an order remains in effect before being expired.

  * `gtc`: Good Till Canceled - until user has cancelled.
  * `gtd`: Good Till Date - until `expire_time` parameter.
  * `ioc`: Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.
  * `fok`: Fill Or Kill - immediately fills the full order quantity or cancels it entirely. Available for `limit` orders only.

boolean

One of: `false`, `true`  
Default: `false`Funds the order on margin using the maximum leverage for the pair (maximum is leverage of 5).

boolean

One of: `true`, `false`  
Default: `false`  
Condition: Orders with limit price onlyCancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.

boolean

One of: `true`, `false`  
Default: `false`Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.

string

Format: RFC3339  
Example: `2022-12-25T09:30:59Z`Scheduled start time (precision to seconds).

string

Format: RFC3339  
Example: `2022-12-25T09:30:59Z`  
Condition: GTD orders onlyExpiration time of the order (precision to seconds). GTD orders can have an expiry time up to one month in future.

string

Format: RFC3339  
Example: `2022-12-25T09:30:59.123Z`Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.

string

Adds a alphanumeric client order identifier which uniquely identifies an open order for each client. This field is mutually exclusive with `order_userref` parameter.The `cl_ord_id` parameter can be one of the following formats:

  * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
  * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
  * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.

integer

This is an optional non-unique, numeric identifier which can associated with a number of orders by the client. This field is mutually exclusive with `cl_ord_id` parameter.Many clients choose a unique integer value generated by their systems (i.e. a timestamp). However, because we don’t enforce uniqueness on our side, it can also be used to easily tag a group of orders for querying or cancelling.

object

The conditional parameters are used as a template for generating the secondary close orders when the primary order fills. Each fill on the primary order will generate a new secondary order. The size of the secondary order will be the same size as the executed quantity and have the opposite side.

Hide properties

string

One of: `limit`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`Defines the order type of the secondary close orders which will be created on each fill.

float

Defines the limit price on the secondary close orders. Only required on secondary order types that support limit price: `limit`, `stop-loss-limit`, `take-profit-limit`.

string

One of: `static`, `pct`, `quote`  
Default: `quote`  
Condition: Only available on trailing-stop-limit ordersThe units for the limit price on the secondary order.

  * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
  * `pct`: a percentage offset from the reference price, i.e. -10% from index price.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

Note, for `trailing-stop-limit` order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.

float

Specifies the amount for the trigger price - it supports both static market prices and relative prices. This field is used in combination with the `price_type` field below to determine the effective trigger price.**Examples:**

  * To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
  * To trigger when price rises by 5%, use price=5, price_type=pct.
  * To trigger when price drops by 150 USD, use price=-150, price_type=quote.

Note, for `trailing-stop` and `trailing-stop-limit` order types, the price represents the reversion from the peak. It is always a positive offset value.

string

One of: `static`, `pct`, `quote`  
Default: `static`The units for the trigger price.

  * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
  * `pct`: a percentage offset from the reference price, i.e. -10% from index price.
  * `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.

float

deprecated

Deprecated: Use trigger_priceDefines the trigger price on the secondary close orders. Only required on triggered secondary order types: `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`.

float

Condition: iceberg orders onlyDefines the quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of `order_qty`.

string

One of: `base`, `quote`Fee preference base or quote currency. `quote` is the default for buy orders, `base` is the default for sell orders.

boolean

deprecated

One of: `true`, `false`  
Default: `false`  
Condition: Market orders only  
Deprecated: If supplied, the flag is accepted but ignoredDisables Market Price Protection (MPP) if set to `true`. MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market.

string

One of: `cancel_newest`, `cancel_oldest`, `cancel_both`  
Default: `cancel_newest`Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves.

  * `cancel_newest`: arriving order will be canceled.
  * `cancel_oldest`: resting order will be canceled.
  * `cancel_both`: both arriving and resting orders will be canceled.

float

Condition: Buy market orders without margin fundingOrder volume expressed in quote currency.

boolean

One of: `true`, `false`  
Default: `false`If set to `true` the order will be validated only, it will not trade in the matching engine.

string

Condition: For institutional accounts with enhanced Self Trade Prevention (STP)Adds a alphanumeric sub-account/trader identifier which enables STP to be performed at a more granular level.The `sender_sub_id` parameter can be one of the following formats:

  * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
  * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
  * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.

float

deprecated

Deprecated: Use ‘triggers’ objectThe stop price for trigger order types.

string

deprecated

One of: `last`, `index`  
Default: `last`  
Condition: Triggered order types only  
Deprecated: Use ‘triggers’ objectThe reference price to trigger the order.

  * `index`: the index price for the broader market for this symbol.
  * `last`: the last traded price in the order book for this symbol.

string

required

Authentication token. See [authentication guide](/exchange/guides/websockets/authentication) for details.

integer

Optional client originated request identifier sent as acknowledgment in the response.

string

Value: `add_order`

object

Hide properties

string

Unique order identifier generated by Kraken.

string

An optional, alphanumeric identifier specified by the client in the `add_order` parameters.

integer

An optional non-unique, numeric identifier specified by the client in the `add_order` parameters.

array of string

Non-fatal warnings about the order, if any.

string

Error message. Condition: if `success` is `false`.

boolean

Indicates if the request was successfully processed by the engine. One of: `true`, `false`

integer

Optional client originated request identifier sent as acknowledgment in the response.

string

The timestamp when the request was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`

string

The timestamp when the response was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`

Was this page helpful?

[Heartbeat](/exchange/api-reference/spot-websocket-v2/heartbeat)[Edit Order](/exchange/api-reference/spot-websocket-v2/edit_order)

Ctrl+I