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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/edit_order'
updated_at: 2026-11-13
---

# Edit Order

> Edit the parameters of a live order

WSS
ws-auth.kraken.com/v2
edit\_order

Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be created with the adjusted parameters a new `order_id` will be returned in the response.

> [!NOTE]
>
> The new [amend\_order](https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/amend_order.md) endpoint resolves the caveats listed below and has additional performance gains.
>
> There are a number of caveats for `edit_order`:
>
> * triggered stop loss or profit take profit orders are not supported.
> * orders with conditional close terms attached are not supported.
> * orders where the executed volume is greater than the newly supplied volume will be rejected.
> * `cl_ord_id` is not supported.
> * existing executions will are associated with the original order and not copied to the amended order.
> * queue position will not be maintained.

> [tab] Request
>
> **method** `string` *required*
>
> Value: `edit_order`
>
> **params** `object`
>
> **properties**
>
> **deadline** `string`
>
> Format: RFC3339\\
>
> Example: `2022-12-25T09:30:59.123Z`
>
> Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond. The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
>
> **display\_qty** `float`
>
> Condition: Iceberg orders only
>
> Defines the quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of `order_qty`.
>
> **fee\_preference** `string`
>
> One of: `base`, `quote`
>
> Fee preference base or quote currency. `quote` is the default for buy orders, `base` is the default for sell orders.
>
> **limit\_price** `float`
>
> Limit price for order types that support limit price restriction.
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
> **order\_id** `string` *required*
>
> Example: `OFGKYQ-FHPCQ-HUQFEK`
>
> The Kraken identifier for the order to be amended.
>
> **order\_qty** `float`
>
> Order quantity in terms of the base asset.
>
> **order\_userref** `integer`
>
> User defined reference to be placed on the amended order. It does not identify the order to be amended, use `order_id`.
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
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The original symbol identifier for the pair. Note, the `symbol` cannot be amended.
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
> **price** `float`
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
> One of: `static`, `pct`, `quote`\\
>
> Default: `static`
>
> The units for the trigger price.
>
> * `static`: a static market price for the asset, i.e. 30000 for BTC/USD.
> * `pct`: a percentage offset from the reference price, i.e. -10% from index price.
> * `quote`: a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price.
>
> **validate** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `false`
>
> If set to `true` the order will be validated only, it will not trade in the matching engine.
>
> **price** `float` *deprecated*
>
> Deprecated: Use `limit_price` parameter
>
> **trigger** `string` *deprecated*
>
> Deprecated: Use `triggers.reference` parameter
>
> **stop\_price** `float` *deprecated*
>
> Deprecated: Use `triggers.price` parameter
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
> Value: `edit_order`
>
> **result** `object`
>
> Condition: if `success` is `true`
>
> **properties**
>
> **order\_id** `string`
>
> Unique ID of the order
>
> **original\_order\_id** `string`
>
> ID of the order that have been edited
>
> **warnings** `array of string`
>
> Non-fatal warnings about the edit, if any.
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
  "method": "edit_order",
  "params": {
    "order_id": "ORDERX-IDXXX-XXXXX1",
    "order_qty": 0.2123456789,
    "symbol": "BTC/USD",
    "token": "TxxxxxxxxxOxxxxxxxxxxKxxxxxxxExxxxxxxxN"
  },
  "req_id": 1234567890
}
```

```json Response theme={null}
{
  "method": "edit_order",
  "req_id": 1234567890,
  "result": {
    "order_id": "ORDERX-IDXXX-XXXXX2",
    "original_order_id": "ORDERX-IDXXX-XXXXX1"
  },
  "success": true,
  "time_in": "2022-07-15T12:56:09.876488Z",
  "time_out": "2022-07-15T12:56:09.923422Z"
}
```
