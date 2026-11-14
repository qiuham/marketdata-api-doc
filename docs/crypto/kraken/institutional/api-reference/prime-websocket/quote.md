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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/quote'
updated_at: 2026-11-13
---

# Quote Updates

> Authenticated channel for streaming real-time quote responses from RFQ requests.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request stream of Quotes. All quote responses are sent as Quote updates. To request a quote, send a QuoteRequest message. The server responds with one or many Quote messages as the streaming prices update.

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
> Array containing the Quote stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `Quote`
>
> **StartDate** `string`
>
> If provided, the subscription will return quotes for rfqs that were submitted after this time.
>
> **EndDate** `string`
>
> If provided, the subscription will return quotes for rfqs that were submitted before this time.
>
> **Symbol** `string`
>
> If provided, Symbol of the security to filter quotes for.
>
> **RFQID** `string`
>
> If provided, filter by RFQID.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 6,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "Quote",
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
> Array of Quote data.
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
> **Currency** `string` *required*
>
> Currency of Quantity.
>
> **RFQID** `string`
>
> Server-assigned RFQID. Present from `PendingNew` onward.
>
> **QuoteReqID** `string` *required*
>
> Client assigned Quote Req ID for the quote request.
>
> **QuoteStatus** `string` *required*
>
> Status of the quote. Possible values: `PendingNew`, `Open`, `PendingCancel`, `Canceled`, `PendingFill`, `Filled`, `Rejected`
>
> **QuoteID** `string` *required*
>
> Server assigned ID for this quote update.
>
> **QuoteRequestRejectReason** `string`
>
> Quote request reject reason, specified when `QuoteStatus` is `Rejected`.
>
> **SubmitTime** `string` *required*
>
> Time of original quote request submission.
>
> **OrderQty** `string` *required*
>
> Order quantity.
>
> **AmountCurrency** `string` *required*
>
> Currency of Amount.
>
> **EndTime** `string` *required*
>
> End time of RFQ.
>
> **Side** `string`
>
> Quote side. Possible values: `Buy`, `Sell`
>
> **TradedPx** `string`
>
> The price of the trade if the quote is filled.
>
> **TradedQty** `string`
>
> The quantity of the trade if the quote is filled.
>
> **TradedAmt** `string`
>
> The amount of the trade if the quote is filled.
>
> **BidPx** `string`
>
> Bid quote price.
>
> **BidAmt** `string`
>
> Bid quote amount in units of AmountCurrency.
>
> **OfferPx** `string`
>
> Offer quote price.
>
> **OfferAmt** `string`
>
> Offer quote amount in units of AmountCurrency.
>
> **ValidUntilTime** `string`
>
> Expire time for the current streaming quote. Present on `Open` updates with live bid/offer prices.
>
> **CustomerUser** `string`
>
> The customer user associated with this quote.
>
> **MarketAccount** `string`
>
> Market account associated with this quote.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 9,
>   "type": "Quote",
>   "ts": "2021-09-14T22:31:27.214025Z",
>   "initial": false,
>   "seqNum": 3,
>   "data": [
>     {
>       "Timestamp": "2021-09-14T22:31:27.204209Z",
>       "Symbol": "BTC-USD",
>       "Currency": "BTC",
>       "RFQID": "8688ceab-ea67-416c-8ce1-9b63d6c0fe4e",
>       "QuoteReqID": "7feb22f0-15ab-11ec-b0a2-2554a9e1e7a4",
>       "QuoteStatus": "Open",
>       "QuoteID": "20e240c5-9a82-4731-809e-91b3a2bf2f49",
>       "SubmitTime": "2021-09-14T22:31:27.183751Z",
>       "OrderQty": "0.30000000",
>       "AmountCurrency": "USD",
>       "EndTime": "2021-09-14T22:31:42.183751Z",
>       "BidPx": "46836.27",
>       "BidAmt": "14050.88",
>       "OfferPx": "46879.47",
>       "OfferAmt": "14063.85",
>       "ValidUntilTime": "2021-09-14T22:31:28.204209Z",
>       "CustomerUser": "tom@company.com"
>     }
>   ]
> }
> ```

## RFQ workflow

A typical RFQ flow looks like this:

1. Subscribe to the [Quote](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote.md) stream.
2. Send a [Quote Request](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote-request.md) to open an RFQ and receive streaming prices.
3. When ready to trade, send a [New Order Single](https://docs.kraken.com/institutional/api-reference/prime-websocket/new-order-single.md) with `OrdType` set to `RFQ` and `QuoteID` and `RFQID` from the latest `Open` quote update. See the **RFQ Example** tab on that page.
4. Monitor fills on the [Execution Report](https://docs.kraken.com/institutional/api-reference/prime-websocket/execution-report.md) and [Trade](https://docs.kraken.com/institutional/api-reference/prime-websocket/trade.md) streams.

To cancel an open quote without trading, use [Quote Cancel Request](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote-cancel-request.md).
