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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/trade'
updated_at: 2026-11-13
---

# Trade

> Subscribe to trade feed for currency pairs

WSS
ws.kraken.com
trade

Trade feed for a currency pair. On subscription, the last 50 trades are sent as a snapshot, followed by real-time trade updates.

## Subscribe

> [tab] Request
>
> **event** `string` *required*
>
> Value: `subscribe`
>
> **pair** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> The currency pairs for this request.
>
> **subscription** `object`
>
> **properties**
>
> **name** `string` *required*
>
> Value: `trade`
>
> **reqid** `string`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> The subscription status is returned via the [subscriptionStatus](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus.md) message.

## Snapshot / Update

**elements**

**\[0] channel\_id** `integer` *deprecated*

Deprecated: use `channelName` and `pair`

Channel identifier.

**\[1] trades** `array`

A list of trades.

**elements**

**trade** `array`

**elements**

**\[0] price** `string`

Price.

**\[1] volume** `string`

Volume.

**\[2] time** `string`

Time, seconds since epoch.

**\[3] side** `string`

One of: `buy`, `sell`

Taker side.

**\[4] order\_type** `string`

One of: `market`, `limit`

Taker order type.

**\[5] misc** `string`

Miscellaneous.

**\[2] pair** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**\[3] channel\_name** `string`

Value: `trade`

## Unsubscribe

> [tab] Request
>
> **event** `string` *required*
>
> Value: `unsubscribe`
>
> **pair** `string[]`
>
> Example: `["BTC/USD", "MATIC/GBP"]`\\
>
> Condition: All channels which support pair subscriptions
>
> The currency pairs to unsubscribe.
>
> **reqid** `string`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **subscription** `object`
>
> **properties**
>
> **name** `string` *required*
>
> Value: `trade`

> [tab] Response
>
> The unsubscription status is returned via the [subscriptionStatus](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus.md) message.

```json Subscribe theme={null}
{
  "event": "subscribe",
  "pair": [
    "XBT/EUR"
  ],
  "subscription": {
    "name": "trade"
  }
}
```

```json Snapshot / Update theme={null}
[
  0,
  [
    [
      "5541.20000",
      "0.15850568",
      "1534614057.321597",
      "s",
      "l",
      ""
    ],
    [
      "6060.00000",
      "0.02455000",
      "1534614057.324998",
      "b",
      "l",
      ""
    ]
  ],
  "trade",
  "XBT/USD"
]
```

```json Unsubscribe theme={null}
{
  "event": "unsubscribe",
  "pair": [
    "XBT/EUR"
  ],
  "subscription": {
    "name": "trade"
  }
}
```
