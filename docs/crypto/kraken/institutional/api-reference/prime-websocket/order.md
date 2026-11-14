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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/order'
updated_at: 2026-11-13
---

# Order Updates

> Authenticated channel for streaming real-time order status updates.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request stream of Order updates. An Order update having a data field containing an array that has a similar structure to ExecutionReport.

## Subscribe Request

> [tab] Subscribe Schema
>
> **reqid** `number` *required*
>
> Request ID - will be echoed back in the response structure.
>
> **type** `string` *required*
>
> Request type. Value: `subscribe`
>
> **streams** `array` *required*
>
> Array containing the Order stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Order`
>
> **StartDate** `string`
>
> If provided, the subscription will return orders that were submitted after this time. An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **EndDate** `string`
>
> If provided, the subscription will return orders that were submitted before this time.
>
> **Symbol** `string`
>
> If provided, Symbol of the security to get the orders for.
>
> **Statuses** `array`
>
> If provided, comma-separated Statuses of orders to include e.g. New,Filled.
>
> **OrderID** `string`
>
> If provided, filter by OrderID.
>
> **RFQID** `string`
>
> If provided, filter by RFQID.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 7,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Order",
>       "StartDate": "2021-09-14T00:00:00.000000Z"
>     }
>   ]
> }
> ```

## Response

> [tab] Response Schema
>
> **reqid** `number` *required*
>
> A number that relates this response to a request.
>
> **type** `string` *required*
>
> The type of message sent.
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **initial** `boolean`
>
> If this is initial data for a request, the initial flag will be set.
>
> **seqNum** `number` *required*
>
> The sequence number for this response per request.
>
> **action** `string`
>
> "Update" or "Remove" - tells the client if the given entity should be removed or added/updated.
>
> **data** `array` *required*
>
> Array of Order data with a similar structure to ExecutionReport.
>
> **properties**
>
> **Timestamp** `string` *required*
>
> Timestamp of the message.
>
> **Symbol** `string` *required*
>
> Symbol of the order security.
>
> **OrderID** `string` *required*
>
> Server assigned Order ID, will be a UUID.
>
> **ClOrdID** `string` *required*
>
> Client assigned Order ID for the last request.
>
> **Side** `string` *required*
>
> "Buy" or "Sell".
>
> **ExecType** `string` *required*
>
> Describes the specific execution.
>
> **OrdStatus** `string` *required*
>
> Identifies current status of order.
>
> **OrderQty** `string` *required*
>
> Order quantity.
>
> **OrdType** `string` *required*
>
> Order type.
>
> **Currency** `string` *required*
>
> Currency of Quantity.
>
> **CustomerUser** `string`
>
> The customer user associated with this order.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 7,
>   "type": "Order",
>   "ts": "2021-09-14T22:26:44.518538Z",
>   "initial": false,
>   "seqNum": 3,
>   "data": [
>     {
>       "Timestamp": "2021-09-14T22:26:44.505519Z",
>       "Symbol": "BTC-USD",
>       "OrderID": "b35b1c3b-a304-4224-919f-9db1319de188",
>       "ClOrdID": "d7635e40-15aa-11ec-b0a2-2554a9e1e7a4",
>       "SubmitTime": "2021-09-14T22:26:44.457050Z",
>       "ExecID": "c73fcf77-aaa1-46e7-9260-f625d6416646",
>       "Side": "Buy",
>       "ExecType": "New",
>       "OrdStatus": "New",
>       "OrderQty": "0.10000000",
>       "OrdType": "Market",
>       "Currency": "BTC",
>       "LeavesQty": "0.10000000",
>       "CumQty": "0",
>       "AvgPx": "0",
>       "TimeInForce": "FillOrKill",
>       "LastPx": "0",
>       "LastQty": "0",
>       "LastAmt": "0",
>       "LastFee": "0",
>       "CumAmt": "0",
>       "DecisionStatus": "Active",
>       "AmountCurrency": "USD",
>       "CustomerUser": "tom@company.com"
>     }
>   ]
> }
> ```
