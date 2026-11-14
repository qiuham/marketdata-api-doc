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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/batch_add'
updated_at: 2026-11-13
---

# Batch Add

> Submit a batch of orders in a single request

UWS
uws.kraken.com/v2/private
batch\_add

Sends a collection of orders (minimum of 2 and maximum 15):

* Validation is performed on the whole batch prior to submission to the engine. If an order fails validation, the whole batch will be rejected.
* On submission to the engine, if an order fails pre-match checks (i.e. funding), then the individual order will be rejected and remainder of the batch will be processed.
* All orders in batch are limited to a single pair.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `batch_add`
>
> **params** `object`
>
> **properties**
>
> **asset\_class** `string` *required*
>
> One of: `spot`, `derivatives`
>
> The asset class for the request.
>
> **deadline** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123Z`
>
> Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The symbol of the currency pair.
>
> **validate** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> If set to `true` the order will be validated only, it will not trade in the matching engine.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **orders** `object[]` *required*
>
> A list of 2 to 15 orders in the batch. Conditional close orders are not supported in batches.
>
> **properties**
>
> **cash\_order\_qty** `float`
>
> Condition: Not available for derivatives
>
> Order volume expressed in quote currency.
>
> **display\_qty** `float`
>
> Condition: Not available for derivatives
>
> Defines the quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of `order_qty`.
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
> Expiration time of the order (precision to seconds). GTD orders can have an expiry time up to one month in future.
>
> **fee\_preference** `string`
>
> One of: `base`, `quote`\\
>
> Condition: Not available for derivatives (fee currency is fixed per contract)
>
> Fee preference base or quote currency. `quote` is the default for buy orders, `base` is the default for sell orders.
>
> **limit\_price** `float`
>
> Limit price for order types that support limit price restriction.
>
> **limit\_price\_type** `string`
>
> One of: `static`\\
>
> Condition: Only available on trailing-stop orders
>
> The units for the limit price. Only `static` is supported for derivatives.
>
> * `static`: a static market price for the asset, i.e. limit price at 29000.5 BTC/USD, use price=29000.5 and price\_type=static.
>
> **margin** `boolean`
>
> One of: `false`, `true`\\
>
> Default: `false`\\
>
> Condition: Not available for derivatives
>
> Funds the order on margin using the maximum leverage for the pair (maximum is leverage of 5).
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
> Disables Market Price Protection (MPP) if set to `true`. MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market. See [MPP support article](https://support.kraken.com/hc/en-us/articles/201648183-Market-Price-Protection).
>
> **cl\_ord\_id** `string`
>
> Adds an alphanumeric client order identifier which uniquely identifies an open order for each client. This field is mutually exclusive with `order_userref` parameter. The `cl_ord_id` parameter can be one of the following formats:
>
> * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
> * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
> * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.
>
> For derivatives, only UUIDv4 format (long or short) is supported.
>
> **order\_userref** `integer`
>
> Condition: Not available for derivatives (use `cl_ord_id` instead)
>
> This is an optional non-unique, numeric identifier which can be associated with a number of orders by the client. This field is mutually exclusive with `cl_ord_id` parameter. Many clients choose a unique integer value generated by their systems (i.e. a timestamp). However, because we don't enforce uniqueness on our side, it can also be used to easily tag a group of orders for querying or cancelling.
>
> **order\_qty** `float` *required*
>
> Order quantity in terms of the base asset.
>
> **order\_type** `string` *required*
>
> One of: `limit`, `market`, `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`
>
> The execution model of the order.
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
> **side** `string` *required*
>
> One of: `buy`, `sell`
>
> Side of the order.
>
> **stp\_type** `string`
>
> One of: `cancel_newest`\\
>
> Default: `cancel_newest`
>
> Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves. Only `cancel_newest` is supported for derivatives.
>
> * `cancel_newest`: arriving order will be canceled.
>
> **time\_in\_force** `string`
>
> One of: `gtc`, `ioc`, `gtd`\\
>
> Default: `gtc`
>
> Time-in-force specifies how long an order remains in effect before being expired. Derivatives support `gtc`, `ioc`, and `gtd`; `gtd` requires `expire_time`.
>
> * `gtc`: Good Till Canceled - until user has cancelled.
> * `ioc`: Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.
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
> Note, for `trailing-stop` and `trailing-stop-limit` order types, the price represents the reversion from the peak. It is always a positive offset value.
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
> **sender\_sub\_id** `string`
>
> Condition: Not available for derivatives
>
> Adds an alphanumeric sub-account/trader identifier which enables STP to be performed at a more granular level. For institutional accounts with enhanced Self Trade Prevention (STP).
>
> * Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
> * Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
> * Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.
>
> **broker** `string`
>
> Format: 16 alphanumeric characters (`A-Z`, `0-9`) in 4 groups of 4\\
>
> Example: `AA16N84GV574COOQ`\\
>
> Condition: Must be the same for every order in the batch
>
> Broker IIBAN (Partner's Kraken IIBAN). Attributes the order to the broker placing it on behalf of their client, so partner commission can be paid.
>
> Available to qualified partners in Kraken's API Partner Program. Both spellings are accepted and are equivalent:
>
> * Grouped: `AA16 N84G V574 COOQ` with a single space between each group of 4 characters.
> * Unspaced: `AA16N84GV574COOQ` 16 characters with no separators.
>
> A batch is attributed to a single broker. You may set `broker` on one, some or all of the orders, but every order that sets it must use the same value, and that value applies to the whole batch. The entire batch is rejected if two orders name different brokers, if the value is not a well-formed IIBAN, or if your account is not entitled to trade on behalf of the specified broker.
>
> **stop\_price** `float` *deprecated*
>
> Deprecated: Use `triggers` object
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
> Deprecated: Use `triggers` object
>
> The reference price to trigger the order.
>
> * `index`: the index price for the broader market for this symbol.
> * `last`: the last traded price in the order book for this symbol.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> The order of returned txid's in the response array is the same as the order of the order list sent in request.
>
> **method** `string`
>
> Value: `batch_add`
>
> **result** `object[]` *required*
>
> Condition: if `success` is `true`
>
> **properties**
>
> **order\_id** `string`
>
> Unique order identifier generated by Kraken.
>
> **cl\_ord\_id** `string`
>
> An optional, alphanumeric identifier specified by the client in the `batch_add` parameters.
>
> **order\_userref** `integer`
>
> An optional order identifier specified by the client in the `batch_add` parameters.
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

```json Request theme={null}
{
    "method": "batch_add",
    "params": {
        "asset_class": "derivatives",
        "deadline": "2022-06-13T08:09:10.123456Z",
        "orders": [
            {
                "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
                "limit_price": 1010.10,
                "order_qty": 0.123456789,
                "order_type": "limit",
                "side": "buy"
            },
            {
                "cl_ord_id": "a1c2d3e4-5678-90ab-cdef-1234567890ab",
                "limit_price": 2020.20,
                "order_qty": 0.987654321,
                "order_type": "limit",
                "side": "sell"
            }
        ],
        "symbol": "BTC/USD",
        "token": "TxxxxxxxxxOxxxxxxxxxxKxxxxxxxExxxxxxxxN",
        "validate": false
    },
    "req_id": 1234567890
}
```

```json Response theme={null}
{
    "method": "batch_add",
    "req_id": 1234567890,
    "result": [
        {
            "order_id": "629bf97e-1abb-5c81-9eda-21fac5b7d405",
            "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876"
        },
        {
            "order_id": "c7d8d7f4-4bc6-5cf9-b6ec-95ea7e1aff51",
            "cl_ord_id": "a1c2d3e4-5678-90ab-cdef-1234567890ab"
        }
    ],
    "success": true,
    "time_in": "2022-06-13T08:09:10.123456Z",
    "time_out": "2022-06-13T08:09:10.7890123"
}
```
