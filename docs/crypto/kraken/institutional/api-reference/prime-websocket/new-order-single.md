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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/new-order-single'
updated_at: 2026-11-13
---

# New Order Single

> Authenticated command to submit a new order against available liquidity or an open RFQ.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to submit a new order either against any provided liquidity or an open RFQ. Results of this command will be visible in the ExecutionReport and Trade streams which will track the lifecycle of the order.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `NewOrderSingle`
>
> **data** `array` *required*
>
> Order data array.
>
> **properties**
>
> **Symbol** `string` *required*
>
> Symbol of the security to submit an order on (e.g. `BTC-USD`).
>
> **ClOrdID** `string` *required*
>
> Unique Client Order ID for this request. Format: UUID
>
> **Side** `string` *required*
>
> Side of the order. Possible values: `Buy`, `Sell`
>
> **OrderQty** `string` *required*
>
> Order quantity in units of Currency.
>
> **OrdType** `string` *required*
>
> Order type. Possible values: `Market`, `Limit`, `RFQ`
>
> **Price** `string`
>
> Order limit price. Required when `OrdType` is `Limit`. Optional when `OrdType` is `RFQ` — include it only to validate against a limit price; if omitted, the order executes at the quoted price.
>
> **Currency** `string`
>
> The currency that the quantity is specified in. If not specified, defaults to the base currency for the symbol.
>
> **TimeInForce** `string` *required*
>
> Specifies how long the order remains in effect. Possible values: `GoodTillCancel`, `FillAndKill`, `FillOrKill`. RFQ orders are always executed as `FillOrKill`; you may omit this field and the platform applies that behavior.
>
> **Strategy** `string`
>
> Optional order strategy to use for algorithmic orders. Possible values: `SteadyPace`, `StopLimit`
>
> **QuoteID** `string`
>
> Optional QuoteID to trade on. Must be specified when OrdType=RFQ.
>
> **RFQID** `string`
>
> Optional RFQID to trade on. Must be specified when OrdType=RFQ.
>
> **AllowedSlippage** `string`
>
> Optional allowed price slippage for Limit order placed against RFQ.
>
> **TransactTime** `string`
>
> Transaction timestamp. Format: ISO-8601 UTC (e.g. `2019-02-13T05:17:32.000000Z`)
>
> **Parameters** `object`
>
> Strategy-specific parameters. Required keys depend on `Strategy` — see [Supported Order Strategies](#supported-order-strategies) below. For `SteadyPace`, `ClipSize` and `ClipInterval` are required.

> [tab] Limit Example
>
> Use this for a standard resting limit order with no algorithmic strategy:
>
> ```json theme={null}
> {
>   "reqid": 12,
>   "type": "NewOrderSingle",
>   "data": [
>     {
>       "Symbol": "BTC-USD",
>       "ClOrdID": "4d489920-15da-11ec-b5e7-7f4881f01b7d",
>       "Side": "Buy",
>       "TransactTime": "2021-09-15T04:06:28.530000Z",
>       "OrderQty": "0.01",
>       "OrdType": "Limit",
>       "Price": "43000",
>       "Currency": "BTC",
>       "TimeInForce": "GoodTillCancel"
>     }
>   ]
> }
> ```

> [tab] SteadyPace Example
>
> When `Strategy` is `SteadyPace`, include the required clip parameters in `Parameters`. `ErrorAction` is optional and controls behavior when a clip fails.
>
> ```json theme={null}
> {
>   "reqid": 12,
>   "type": "NewOrderSingle",
>   "data": [
>     {
>       "Symbol": "BTC-USD",
>       "ClOrdID": "4d489920-15da-11ec-b5e7-7f4881f01b7d",
>       "Side": "Buy",
>       "TransactTime": "2021-09-15T04:06:28.530000Z",
>       "OrderQty": "0.01",
>       "OrdType": "Limit",
>       "Price": "43000",
>       "Currency": "BTC",
>       "TimeInForce": "GoodTillCancel",
>       "Strategy": "SteadyPace",
>       "Parameters": {
>         "ClipSize": "0.001",
>         "ClipInterval": "1m",
>         "ErrorAction": "Pause"
>       }
>     }
>   ]
> }
> ```

> [tab] RFQ Example
>
> Accept an open quote by sending `NewOrderSingle` with `OrdType` set to `RFQ`. Use `QuoteID` and `RFQID` from the latest `Open` update on the [Quote](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote.md) stream. `Price` is optional — omit it to trade at the quoted price, or set it to enforce a limit.
>
> ```json theme={null}
> {
>   "reqid": 41,
>   "type": "NewOrderSingle",
>   "data": [
>     {
>       "Symbol": "BTC-USD",
>       "ClOrdID": "4d489920-15da-11ec-b5e7-7f4881f01b7d",
>       "Side": "Buy",
>       "TransactTime": "2021-09-15T04:06:28.530000Z",
>       "OrderQty": "0.30000000",
>       "OrdType": "RFQ",
>       "QuoteID": "20e240c5-9a82-4731-809e-91b3a2bf2f49",
>       "RFQID": "8688ceab-ea67-416c-8ce1-9b63d6c0fe4e"
>     }
>   ]
> }
> ```

## Accepting a quote (RFQ)

To trade against an open RFQ:

1. Subscribe to [Quote](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote.md), [Execution Report](https://docs.kraken.com/institutional/api-reference/prime-websocket/execution-report.md), and [Trade](https://docs.kraken.com/institutional/api-reference/prime-websocket/trade.md).
2. Send a [Quote Request](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote-request.md) and wait for `QuoteStatus` `Open`.
3. Send `NewOrderSingle` with `OrdType` `RFQ`, `QuoteID` and `RFQID` from the `Open` quote, matching `Side`/`Symbol`/`OrderQty`, and optional `Price` if you need limit validation. RFQ orders are always executed as `FillOrKill` — you may omit `TimeInForce`.
4. Monitor execution and trade streams for fill or reject. The quote moves to `Filled` when accepted.

Command requests do not return a direct ack; results arrive on the subscribed streams. Quotes expire at `ValidUntilTime` unless you accept them with `NewOrderSingle` or cancel the quote with [Quote Cancel Request](https://docs.kraken.com/institutional/api-reference/prime-websocket/quote-cancel-request.md).

## Supported Order Strategies

The **Limit Example** tab above omits `Strategy` entirely — suitable for a single resting limit order. Set `Strategy` when you need algorithmic execution; each strategy requires its own `Parameters` fields.

### SteadyPace

A schedule-based algorithm that divides an order into suborders (clips) and submits them at equal, user-defined intervals.

**Required parameters:**

| Parameter | Type | Description |
| - | - | - |
| `ClipSize` | Qty | Quantity sent on each clip (must be less than total `OrderQty`). |
| `ClipInterval` | string | Interval between clips (e.g. `1m`, `30s`). |

**Optional parameters:**

| Parameter | Type | Description |
| - | - | - |
| `StartTime` | string | ISO-8601 UTC time when the schedule begins sending clips. |
| `EndTime` | string | ISO-8601 UTC expire time for the order. |
| `Variance` | decimal | Randomization factor applied to clip sizes. |
| `ErrorAction` | string | Behavior when a clip fails (e.g. `Pause`). |

> [!NOTE]
>
> Omitting `ClipSize` or `ClipInterval` while `Strategy` is `SteadyPace` produces an incomplete request. Use the **SteadyPace Example** tab above for a copy-paste-ready payload.

### StopLimit

This strategy will only place the order once the specified stop price has been met.

**Parameters:**

* `TriggerPrice` (Price, required): The price that must be met to trigger execution of the order.
* `EndTime` (string, optional): Optional expire time for the order.
