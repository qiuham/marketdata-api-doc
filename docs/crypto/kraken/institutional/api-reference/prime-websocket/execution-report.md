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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/execution-report'
updated_at: 2026-11-13
---

# Execution Report

> Authenticated channel for streaming all order responses and lifecycle updates.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request stream of Execution Reports. All order responses and updates are sent as ExecutionReport messages.

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
> Array containing the ExecutionReport stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `ExecutionReport`
>
> **StartDate** `string`
>
> If provided, the subscription will return execution reports that were published at or after this time. An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **EndDate** `string`
>
> If provided, the subscription will return execution reports that were published before this time.
>
> **Symbol** `string`
>
> If provided, Symbol of the security to get the executions for.
>
> **Statuses** `array`
>
> If provided, comma-separated statuses of orders to include e.g. New,Filled.
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
>   "reqid": 5,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "ExecutionReport",
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
> Array of ExecutionReport data.
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
> **OrigClOrdID** `string`
>
> Original client assigned Order ID.
>
> **SubmitTime** `string` *required*
>
> Time of original order submission.
>
> **ExecID** `string` *required*
>
> Server assigned ID of this update, will be a UUID.
>
> **Side** `string` *required*
>
> Order side. Possible values: `Buy`, `Sell`
>
> **TransactTime** `string`
>
> Transaction time.
>
> **ExecType** `string` *required*
>
> Describes the specific execution. Possible values: `New`, `Trade`, `Canceled`, `Replaced`, `PendingCancel`, `Stopped`, `Rejected`, `PendingNew`, `Restated`, `PendingReplace`, `CancelRejected`, `ReplaceRejected`, `PendingResume`, `Resumed`, `PendingPause`, `Paused`, `Triggered`, `Started`
>
> **OrdStatus** `string` *required*
>
> Identifies current status of order. Possible values: `New`, `PartiallyFilled`, `Filled`, `Canceled`, `PendingCancel`, `Rejected`, `PendingNew`, `PendingReplace`
>
> **OrderQty** `string` *required*
>
> Order quantity.
>
> **OrdType** `string` *required*
>
> Order type. Possible values: `Market`, `Limit`, `RFQ`
>
> **Price** `string`
>
> Order limit price, required when OrdType=Limit.
>
> **Currency** `string` *required*
>
> Currency of Quantity.
>
> **LeavesQty** `string` *required*
>
> Quantity open for further execution.
>
> **CumQty** `string` *required*
>
> Total quantity filled. Always in Currency units.
>
> **AvgPx** `string`
>
> Average filled price of the order. Only valid if CumQty > 0. Does not include fees.
>
> **TimeInForce** `string` *required*
>
> Specifies how long the order remains in effect. Possible values: `GoodTillCancel`, `FillAndKill`, `FillOrKill`
>
> **LastPx** `string`
>
> Last price, specified when ExecType=Trade.
>
> **LastQty** `string`
>
> Last qty, specified when ExecType=Trade.
>
> **LastAmt** `string`
>
> Last amount, specified when ExecType=Trade.
>
> **LastFee** `string`
>
> Last fee, specified when ExecType=Trade.
>
> **CumAmt** `string`
>
> Total amount filled. Always in Amount currency.
>
> **AmountCurrency** `string` *required*
>
> Currency of Amount.
>
> **CustomerUser** `string`
>
> The customer user associated with this execution report.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 6,
>   "type": "ExecutionReport",
>   "ts": "2021-09-14T22:23:11.920903Z",
>   "initial": false,
>   "seqNum": 2,
>   "data": [
>     {
>       "Timestamp": "2021-09-14T22:23:11.903074Z",
>       "Symbol": "BTC-USD",
>       "OrderID": "1b6b882b-e2fc-4774-ad2d-9db4df536f29",
>       "ClOrdID": "58b9adb0-15aa-11ec-b0a2-2554a9e1e7a4",
>       "SubmitTime": "2021-09-14T22:23:11.903074Z",
>       "ExecID": "4b423f54-4a54-4679-9ee7-1f5f417ec5f5",
>       "Side": "Buy",
>       "TransactTime": "2021-09-14T22:23:11.883000Z",
>       "ExecType": "PendingNew",
>       "OrdStatus": "PendingNew",
>       "OrderQty": "0.20000000",
>       "OrdType": "Market",
>       "Currency": "BTC",
>       "LeavesQty": "0.20000000",
>       "CumQty": "0",
>       "AvgPx": "0",
>       "TimeInForce": "FillOrKill",
>       "LastPx": "0",
>       "LastQty": "0",
>       "LastAmt": "0",
>       "LastFee": "0",
>       "CumAmt": "0",
>       "AmountCurrency": "USD",
>       "CustomerUser": "tom@company.com"
>     }
>   ]
> }
> ```
