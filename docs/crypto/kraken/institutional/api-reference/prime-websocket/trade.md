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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/trade'
updated_at: 2026-11-13
---

# Trade

> Authenticated channel for streaming real-time trade fill updates.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request stream of Trade messages. Upon subscription, the server will return all Trade for this client as long as the optional constraints are satisfied. Server will also send a Trade update when the order receives more fills or new fills arrive on a new order.

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
> Array containing the Trade stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Trade`
>
> **StartDate** `string`
>
> If provided, the subscription will return trades that were executed after this time. An ISO-8601 UTC string of the form 2019-02-13T05:17:32.000000Z.
>
> **EndDate** `string`
>
> If provided, the subscription will return trades that were executed before this time.
>
> **Symbol** `string`
>
> If provided, Symbol of the security to get the orders for.
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
>   "reqid": 8,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Trade",
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
> Array of Trade data.
>
> **properties**
>
> **Timestamp** `string` *required*
>
> Timestamp of the message.
>
> **Symbol** `string` *required*
>
> Security symbol for this trade (e.g. `BTC-USD`).
>
> **OrderID** `string` *required*
>
> Server assigned Order ID, will be a UUID.
>
> **TradeID** `string` *required*
>
> Server assigned Trade ID, will be a UUID.
>
> **Side** `string` *required*
>
> Trade side. Possible values: `Buy`, `Sell`
>
> **TransactTime** `string` *required*
>
> Transaction time.
>
> **ExecType** `string` *required*
>
> Describes the specific execution (e.g. Pending Cancel) while OrdStatus will always identify the current order status (e.g. Partially Filled).
>
> **Currency** `string` *required*
>
> Currency of Quantity.
>
> **Price** `string`
>
> Order limit price, required when OrdType=Limit.
>
> **Quantity** `string` *required*
>
> Trade quantity.
>
> **Amount** `string` *required*
>
> Trade amount.
>
> **Fee** `string`
>
> Trade fee.
>
> **FeeCurrency** `string`
>
> Fee currency.
>
> **TradeStatus** `string` *required*
>
> Status of the trade. Possible values: `Pending`, `Confirmed`, `Canceled`
>
> **AggressorSide** `string` *required*
>
> Side of the aggressing order. Possible values: `Buy`, `Sell`
>
> **QuoteID** `string`
>
> Server assigned QuoteID for RFQ Orders.
>
> **AmountCurrency** `string` *required*
>
> Currency of Amount.
>
> **DealtCurrency** `string` *required*
>
> Currency in which the trade was dealt.
>
> **MarketAccount** `string`
>
> Market account associated with this trade.
>
> **Revision** `number`
>
> Revision number for this trade update.
>
> **TradeSource** `string`
>
> Source of the trade (e.g. `Dealer`).
>
> **TradeAction** `string`
>
> Action for this trade update (e.g. `New`).
>
> **RFQID** `string`
>
> Server assigned RFQID for RFQ Orders.
>
> **CustomerUser** `string`
>
> The customer user associated with this trade.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 8,
>   "type": "Trade",
>   "ts": "2021-09-14T22:29:32.255949Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "Timestamp": "2021-09-14T22:23:11.989845Z",
>       "Symbol": "BTC-USD",
>       "OrderID": "1b6b882b-e2fc-4774-ad2d-9db4df536f29",
>       "TradeID": "a0ec46f2-6d0e-451a-a4f1-2a0be7d32d26",
>       "Side": "Buy",
>       "TransactTime": "2021-09-14T22:23:11.964531Z",
>       "ExecType": "Trade",
>       "Currency": "BTC",
>       "Price": "47085.090668824440",
>       "Quantity": "0.20000000",
>       "Amount": "9417.02",
>       "Fee": "0",
>       "CustomerUser": "tom@company.com",
>       "TradeStatus": "Confirmed",
>       "AggressorSide": "Buy",
>       "AmountCurrency": "USD",
>       "DealtCurrency": "BTC"
>     }
>   ]
> }
> ```
