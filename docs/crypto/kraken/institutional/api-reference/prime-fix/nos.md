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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/nos'
updated_at: 2026-11-13
---

# New Order Single

> Submit a new order to the Kraken order book via FIX.

To submit a new order, the client needs to send a NewOrderSingle message. All orders are submitted from the client's perspective to Kraken exchange to place bid/offer on the Kraken Order book.
A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below.

The supported order types are:

* `market`: The full order quantity executes immediately at the best available price in the order book.
* `limit`: The full order quantity is placed immediately with a limit price restriction to only trade at this price or better.
* `limitallin`: The limit order price and quantity includes the fees.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `D`
>
> **1 - Account** `string`
>
> The specific account for this order. Required if multiple accounts are enabled.
>
> **11 - ClOrdID** `string` *required*
>
> Unique identifier for Order as assigned by the client. Must be `<= 36 characters`. UUIDs are recommended.
>
> **55 - Symbol** `string` *required*
>
> The symbol of the currency pair to place an order on in the format `BASE-QUOTE`.
>
> **54 - Side** `integer` *required*
>
> Side of the order.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`1` : Buy</li>
>   <li>`2` : Sell</li>
> </ul>
>
> **40 - OrdType** `char` *required*
>
> The execution model of the order.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`1` : market</li>
>   <li>`2` : Limit</li>
>   <li>`A` : LimitAllIn</li>
> </ul>
>
> **38 - OrderQty** `float` *required*
>
> Order quantity in terms of the base asset.
>
> **15 - Currency** `string`
>
> The currency the quantity is specified in. If not
> specified, defaults to the base currency for the
> symbol.
>
> **44 - Price** `float`
>
> Limit price of the order to be placed in the Order Book. Required when OrderType=Limit/LimitAllIn.
>
> **59 - TimeInForce** `string` *required*
>
> Specifies how long the order remains in effect.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`1` : GTC (Good till canceled)</li>
>   <li>`3` : IOC (Immediate or Cancel)</li>
>   <li>`4` : Fill Or Kill (FOK) </li>
> </ul>
>
> **60 - TransactTime** `string` *required*
>
> Business timestamp for this request. Format: YYYYMMDD-HH:MM:SS.uuu
>
> **126 - ExpireTime** `string`
>
> Optional expiration time for the order. Only valid on orders with TimeInForce=1 (GTC). Required when TimeinForce=GTD. Format: YYYYMMDD-HH:MM:SS
>
> **168 - EffectiveTime** `string`
>
> Time at which this order will activate and begin sending orders to the market. Format: YYYYMMDD-HH:MM:SS.uuu
>
> **847 - TargetStrategy** `string`
>
> Allows Specifying an Order Strategy Type.
>
> <ul>
>   **Possible values:**
>   <li>`StopLimit` : This strategy will only place the order once the specified stop price has been met. For a Buy StopLimit order, the stop price must be *above* the current market price. For a Sell StopLimit order, the stop price must be *below* the current market price. </li>
>   <li>`TakeProfitLimit` : This strategy will only place the order once the specified take profit price has been met. For a Buy TakeProfitLimit order, the take profit price must be *below* the current market price. For a Sell TakeProfitLimit order, the take profit price must be *above* the current market price.</li>
> </ul>
>
> **957 - NoStrategyParams** `integer`
>
> The number of strategy parameter repeating groups
>
> **958 - StrategyParameterName** `string`
>
> The name of the StrategyParameter being set
>
> **960 - StrategyParameterValue** `string`
>
> The value for the StrategyParameter being set
>
> **20030 - CancelOnDisconnect** `string`
>
> Whether or not this order should be canceled when this session is disconnected. Possible values: Y, N. Default: Y
>
> **trailer** *required*

> [tab] Example
>
> ```text theme={null}
> 8=FIX.4.4|9=147|35=D|34=2|49=CUSTOMER|52=20220915-18:30:01.335|56={{ Customer }}|11=id-220912164936074-1152|38=1|40=2|44=1630.123|54=2|55=ETH-USD|59=1|60=20220915-14:30:01|10=228|
> ```
