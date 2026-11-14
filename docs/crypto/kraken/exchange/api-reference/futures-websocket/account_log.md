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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/account_log'
updated_at: 2026-11-13
---

# Account Log

> Subscribe to account log information

WSS
futures.kraken.com/ws/v1
account\_log

> [!WARNING]
>
> **Derivatives WebSocket is being deprecated.** For new integrations, use the
> [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket), which streams
> Spot and Derivatives over a single connection. Existing integrations continue
> to work until **1 March 2027**, when the Derivatives WebSocket will no
> longer be available. Migrate to the Unified WebSocket before then.
>
> To use private channels or trade on the Unified WebSocket, you need a
> Kraken API key, not a Derivatives API key. Use it to get a token from
> [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token). See
> [Unified WebSocket authentication](https://docs.kraken.com/exchange/api-reference/unified-websocket#authentication).

This subscription feed publishes account information.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `account_log`

**api\_key** `string` *required*

The user API key.

**original\_challenge** `string` *required*

The message that is received from a challenge request.

**signed\_challenge** `string` *required*

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "account_log",
  "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",
  "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",
  "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `account_log`

**api\_key** `string`

The user API key.

**original\_challenge** `string`

The message that is received from a challenge request.

**signed\_challenge** `string`

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "account_log",
  "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",
  "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",
  "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="
}
```

***

## Response Snapshot & Delta

**feed** `string`

The subscribed feed.

**logs** `list of structures`

A list containing the account logs.

**properties**

**id** `positive integer`

The identifier of the log.

**date** `ISO8601 datetime`

The creation time of the log according to server date and time.

**asset** `string`

The asset related to the booking.

**contract** `string`

The futures contract (symbol) associated with the log entry, if applicable.

**info** `string`

A description of the booking.

**booking\_uid** `string`

The unique id of the booking.

**margin\_account** `string`

The name of the account associated with the entry.

**old\_balance** `float`

The account balance before the action described in `info`.

**new\_balance** `float`

The new balance of wallet or new size of the position after the action described in `info`.

**old\_average\_entry\_price** `positive float`

The average entry price of the position prior to this trade.

**new\_average\_entry\_price** `positive float`

The average entry price of the position after this trade.

**trade\_price** `positive float`

The price the trade was executed at.

**mark\_price** `positive float`

The mark price at the time the trade was executed.

**realized\_pnl** `float`

The pnl that is realized by reducing the position.

**fee** `float`

The fee paid.

**execution** `string`

The uid of the associated execution.

**collateral** `string`

The currency of the associated entry.

**funding\_rate** `float`

The absolute funding rate.

**realized\_funding** `float`

The funding rate realized due to change in position size or end of funding rate period.

**conversion\_spread\_percentage** `float`

The percentage conversion spread used in a currency conversion.

**liquidation\_fee** `float`

The liquidation fee associated with a liquidation/assignment entry. Not applicable for inverse futures.

```json Example: Snapshot theme={null}
{
  "feed": "account_log_snapshot",
  "logs": [
    {
      "id": 1690,
      "date": "2019-07-11T08:00:00.000Z",
      "asset": "bch",
      "info": "funding rate change",
      "booking_uid": "86fdc252-1b6e-40ec-ac1d-c7bd46ddeebf",
      "margin_account": "f-bch:usd",
      "old_balance": 0.01215667051,
      "new_balance": 0.01215736653,
      "old_average_entry_price": 0.0,
      "new_average_entry_price": 0.0,
      "trade_price": 0.0,
      "mark_price": 0.0,
      "realized_pnl": 0.0,
      "fee": 0.0,
      "execution": "",
      "collateral": "bch",
      "funding_rate": -8.7002552653e-8,
      "realized_funding": 6.9602e-7,
      "conversion_spread_percentage": 0.0,
      "liquidation_fee": 0.0
    },
    {
      "id": 1689,
      "date": "2019-07-11T04:00:00.000Z",
      "asset": "bch",
      "info": "funding rate change",
      "booking_uid": "680d3973-5774-4a9d-b807-ab8aa73f95c3",
      "margin_account": "f-bch:usd",
      "old_balance": 0.01215715298,
      "new_balance": 0.01215667051,
      "old_average_entry_price": 0.0,
      "new_average_entry_price": 0.0,
      "trade_price": 0.0,
      "mark_price": 0.0,
      "realized_pnl": 0.0,
      "fee": 0.0,
      "execution": "",
      "collateral": "bch",
      "funding_rate": 6.0309345058e-8,
      "realized_funding": -4.8247e-7,
      "conversion_spread_percentage": 0.0,
      "liquidation_fee": 0.0
    }
  ]
}
```

```json Example: Delta theme={null}
{
  "feed": "account_log",
  "new_entry": {
    "id": 1697,
    "date": "2019-07-11T13:00:27.632Z",
    "asset": "pi_bchusd",
    "info": "futures trade",
    "booking_uid": "55a02b5b-2c90-4d43-b0eb-eb3801d50e3f",
    "margin_account": "f-bch:usd",
    "old_balance": 1.0,
    "new_balance": 2.0,
    "old_average_entry_price": 413.3,
    "new_average_entry_price": 374.3445326979084,
    "trade_price": 342.1,
    "mark_price": 342.4,
    "realized_pnl": 0.0,
    "fee": 0.0,
    "execution": "fc49fea9-8827-4a2e-8e36-c047523ddc30",
    "collateral": "bch",
    "funding_rate": 1.64955714332e-7,
    "realized_funding": -1.31965e-6,
    "conversion_spread_percentage": 0.0,
    "liquidation_fee": 0.0
  }
}
```

***

## Response Error

**event** `string`

Value: `error`

**message** `string`

One of: `Invalid feed`, `Json Error`

An error message.

```json Example theme={null}
{
  "event": "error",
  "message": "Invalid feed"
}
```
