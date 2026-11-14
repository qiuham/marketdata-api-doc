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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/er'
updated_at: 2026-11-13
---

# Execution Report

> FIX message used to acknowledge or reject orders, and to relay order status and fill updates.

The ExecutionReport message is used to acknowledge/reject an order or changes to an order, and to relay order status and fill updates.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `8`
>
> **11 - ClOrdID** `string` *required*
>
> Unique identifier for Order as assigned by the client. Must be `<= 36 characters`. UUIDs are recommended.
>
> **41 - OrigClordid** `string`
>
> Set to the ClOrdID of the previous accepted order when responding to a Cancel or Cancel/Replace request. Required when exectype=Cancel.
>
> **37 - OrderID** `string` *required*
>
> Unique identifier of most recent order as assigned by Customer.
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
> **38 - OrderQty** `float` *required*
>
> Size of the order.
>
> **44 - Price** `float`
>
> Price of the order. Required when OrderType=Limit/LimitAllIn.
>
> **60 - TransactTime** `string`
>
> Time of event expressed in UTC. Format: YYYYMMDD-HH:MM:SS.uuu
>
> **17 - ExecId** `string` *required*
>
> Unique identifier of most recent order as assigned by Customer.
>
> **527 - SecondaryExecID** `integer`
>
> Sequence number for every ExecType=Trade. This ID unique by pair. Required when ExecType=Trade.
>
> **150 - ExecType** `char` *required*
>
> Describes the type of order event and determines the set of fields in the message.
>
> <ul>
>   **Possible Values:**
>   <li>`0` : New</li>
>   <li>`3` : Done for day</li>
>   <li>`4` : Canceled</li>
>   <li>`5` : Replaced</li>
>   <li>`6` : Pending Cancel</li>
>   <li>`8` : Rejected</li>
>   <li>`A` : Pending New</li>
>   <li>`E` : Pending Replace</li>
>   <li>`F` : Trade</li>
> </ul>
>
> **59 - TimeInForce** `string` *required*
>
> <ul>
>   **Possible Values:**
>   <li>`1` : GTC (Good till canceled)</li>
>   <li>`3` : IOC (Immediate or Cancel)</li>
>   <li>`4` : Fill Or Kill (FOK)</li>
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
> </ul>
>
> **39 - OrdStatus** `char` *required*
>
> Describes the status of the order.
>
> <ul>
>   **Possible Values:**
>   <li>`0` : New</li>
>   <li>`1` : Partially Filled</li>
>   <li>`2` : Filled</li>
>   <li>`3` : Done for day</li>
>   <li>`4` : Canceled</li>
>   <li>`5` : Replaced</li>
>   <li>`6` : Pending Cancel</li>
>   <li>`8` : Rejected</li>
>   <li>`A` : Pending New</li>
>   <li>`E` : Pending Replace</li>
> </ul>
>
> **151 - LeavesQty** `float` *required*
>
> Quantity open for further execution. If OrdStatus(39) is 4 (Canceled), 3 (Done For Day), or 8 (Rejected) then LeavesQty(151) could be 0, otherwise LeavesQty(151) = OrderQty(38) - CumQty(14).
>
> **14 - CumQty** `float` *required*
>
> Currently executed quantity for chain of orders.
>
> **6 - AvgPx** `float`
>
> Calculated average price of all fills on this order. Required when ExecType=Trade.
>
> **103 - OrdRejReason** `char`
>
> Reason for rejection. Required when ExecType=Rejected.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : Broker / exchange option</li>
>   <li>`1` : Unknown symbol</li>
>   <li>`2` : Exchange closed</li>
>   <li>`3` : Order exceeds limit</li>
>   <li>`5` : Unknown order</li>
>   <li>`6` : Duplicate of an existing order</li>
>   <li>`7` : Duplicate of a verbally communicated order</li>
>   <li>`8` : Stale order</li>
> </ul>
>
> **31 - LastPx** `float`
>
> Price of the last trade. Required when ExecType=Trade.
>
> **32 - LastQty** `float`
>
> Quantity bought or sold on the last trade. Required when ExecType=Trade.
>
> **381 - GrossTradeAmt** `float`
>
> Last amount traded (i.e. quantity \* price) expressed in units of counter currency. Required when ExecType=Trade.
>
> **4015 - CumAmt** `float`
>
> Cumulative amount traded (i.e. quantity \* price) expressed in units of counter currency. Required when ExecType=Trade.
>
> **4016 - CumFee** `float`
>
> Cumulative fee amount expressed in units of fee currency. Required when ExecType=Trade.
>
> **4033 - LastFee** `float`
>
> Fee amount for the last trade expressed in units of fee currency. Required when ExecType=Trade.
>
> **4034 - LastFeeCurrency** `string`
>
> Currency of the fee for the last trade. Required when ExecType=Trade.
>
> **20030 - CancelOnDisconnect** `char`
>
> Whether or not the order is canceled on disconnect. Required when ExecType=Trade.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`N` : No</li>
>   <li>`Y` : Yes</li>
> </ul>
>
> **20032 - DecisionStatus** `char`
>
> The current decision status of the order. Required when ExecType=Trade. Default: A
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`A` : Active</li>
>   <li>`P` : Paused</li>
>   <li>`U` : Pending Pause</li>
>   <li>`R` : Pending Resume</li>
>   <li>`W` : Waiting for StartTime</li>
>   <li>`T` : Waiting for Trigger</li>
> </ul>
>
> Paused or staged orders can be edited or resumed from the Customer UI. Pending statuses are intermediate states.
>
> **58 - Text** `string`
>
> Full description for Cancellations or status of the order.
>
> **trailer** *required*

> [tab] Example
>
> ```text theme={null}
> 8=FIX.4.4|9=366|35=8|34=2|49={{ Customer }}|52=20220915-18:30:01.393|56=CUSTOMER|1=default|6=0|11=id-220912164936074-1152|14=0|17=ba22dbe1-cb33-4fcb-9613-921006afdebd|37=94869628-b862-43e4-bd2d-be85e4295bd4|38=1.00000000|39=8|40=2|44=1630.123|54=2|55=ETH-USD|58=Unable to submit market order - please try again later.|59=1|60=20220915-14:30:01.000|103=0|150=8|151=1.00000000|20030=N|20032=A|10=205|
> ```
