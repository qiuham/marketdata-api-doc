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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/open_position'
updated_at: 2026-11-13
---

# Open Positions

> Subscribe to open positions for your account

WSS
futures.kraken.com/ws/v1
open\_positions

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

This subscription feed publishes the open positions of the user account.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `open_positions`

**api\_key** `string` *required*

The user API key.

**original\_challenge** `string` *required*

The message that is received from a challenge request.

**signed\_challenge** `string` *required*

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "open_positions",
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

The requested subscription feed. Value: `open_positions`

**api\_key** `string`

The user API key.

**original\_challenge** `string`

The message that is received from a challenge request.

**signed\_challenge** `string`

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "open_positions",
  "api_key": "CMl2SeSn09Tz+2tWuzPiPUjaXEQRGq6qv5UaexXuQ3SnahDQU/gO3aT+",
  "original_challenge": "226aee50-88fc-4618-a42a-34f7709570b2",
  "signed_challenge": "RE0DVOc7vS6pzcEjGWd/WJRRBWb54RkyvV+AZQSRl4+rap8Rlk64diR+Z9DQILm7qxncswMmJyvP/2vgzqqh+g=="
}
```

***

## Response Snapshot

**feed** `string`

The subscribed feed.

**account** `string`

The user account.

**seq** `positive integer`

The subscription message sequence number.

**timestamp** `positive integer`

The UTC time in milliseconds.

**positions** `list of structures`

A list containing the user open positions.

**properties**

**instrument** `string`

The instrument (referred also as symbol or product\_id) of the order.

**balance** `float`

The size of the position.

**entry\_price** `positive float`

The average entry price of the instrument.

**mark\_price** `positive float`

The market price of the position instrument.

**index\_price** `positive float`

The index price of the position instrument.

**pnl** `float`

The profit and loss of the position.

**liquidation\_threshold** `float`

The mark price of the contract at which the position will be liquidated.

**return\_on\_equity** `float`

The percentage gain or loss relative to the initial margin used in the position. Formula: PnL/IM.

**unrealized\_funding** `float`

Unrealised funding from funding rate.

**effective\_leverage** `float`

How leveraged the net position is in a given margin account. Formula: Position Value at Market / Portfolio Value.

**initial\_margin** `float`

The initial margin for the open position.

**initial\_margin\_with\_orders** `float`

The initial margin for the open position and open orders of the same instrument.

**maintenance\_margin** `float`

The maintenance margin for the open position.

**pnl\_currency** `string`

The profit currency for the position, not returned for inverse positions.

**max\_fixed\_leverage** `positive float`

The maximum allowed fixed leverage for the position's instrument.

**fill\_time** `ISO8601 datetime`

The time the most recent fill occurred for this position.

**iv** `float`

The option's implied volatility.

**delta** `float`

Delta, the option value's sensitivity to change in the underlying price.

**theta** `float`

Theta, the option value's sensitivity to the passage of time.

**gamma** `float`

Gamma, delta's sensitivity to change in the underlying price.

**vega** `float`

Vega, the option value's sensitivity to change in volatility.

**rho** `float`

Rho, the option value's sensitivity to the interest rate.

```json Example theme={null}
{
  "feed": "open_positions",
  "account": "DemoUser",
  "positions": [
    {
      "instrument": "PF_XRPUSD",
      "balance": 500.0,
      "pnl": -239.6506683474764,
      "entry_price": 0.3985,
      "mark_price": 0.4925844,
      "index_price": 0.49756,
      "liquidation_threshold": 0.0,
      "effective_leverage": 0.17404676894304316,
      "return_on_equity": -2.3609636135508127,
      "initial_margin": 101.5054475943615,
      "initial_margin_with_orders": 101.5054475943615,
      "maintenance_margin": 50.75272379718075
    },
    {
      "instrument": "PF_XBTUSD",
      "balance": 0.04,
      "pnl": 119.56244985549435,
      "entry_price": 26911.75,
      "mark_price": 29900.81124638736,
      "index_price": 29900.47,
      "liquidation_threshold": 9572.804662403718,
      "effective_leverage": 0.31865408963748215,
      "return_on_equity": 5.553450159107747,
      "unrealized_funding": 0.0004114160669590132,
      "initial_margin": 21.529400000000003,
      "initial_margin_with_orders": 21.529400000000003,
      "maintenance_margin": 10.764700000000001,
      "pnl_currency": "USD"
    },
    {
      "instrument": "OF_ETHUSD_240101_1000_C",
      "balance": 0.04,
      "pnl": 119.56244985549435,
      "entry_price": 26911.75,
      "mark_price": 29900.81124638736,
      "index_price": 29900.47,
      "return_on_equity": 5.553450159107747,
      "iv": 0.3,
      "delta": 0.5,
      "gamma": 0.5,
      "vega": 0.5,
      "theta": 0.5,
      "rho": 0.5
    }
  ],
  "seq": 4,
  "timestamp": 1687383625330
}
```

***

## Response Error

**event** `string`

Value: `error`

**message** `string`

One of: `Invalid product id`, `Invalid feed`, `Json Error`

An error message.

```json Example theme={null}
{
  "event": "error",
  "message": "Invalid product id"
}
```
