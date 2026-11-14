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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/ticker'
updated_at: 2026-11-13
---

# Ticker

> Subscribe to ticker information on currency pairs

WSS
ws.kraken.com
ticker

Ticker information on currency pair. On subscription, a snapshot of the current ticker data is sent, followed by updates on every trade event.

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
> Value: `ticker`
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

**\[1] ticker** `object`

**properties**

**a** `array`

Best Ask

**elements**

**\[0] price** `string`

Best ask price.

**\[1] whole\_lot\_volume** `integer`

Whole lot volume.

**\[2] decimal** `string`

Lot volume.

**b** `array`

Best Bid

**elements**

**\[0] price** `string`

Best bid price.

**\[1] whole\_lot\_volume** `integer`

Whole lot volume.

**\[2] decimal** `string`

Lot volume.

**c** `array`

Close

**elements**

**\[0] price** `string`

Price.

**\[1] lot\_volume** `string`

Lot volume.

**v** `array`

Volume

**elements**

**\[0] today** `string`

Value today.

**\[1] last\_24h** `string`

Value over last 24 hours.

**p** `array`

Volume Weighted Average Price

**elements**

**\[0] today** `string`

Value today.

**\[1] last\_24h** `string`

Value over last 24 hours.

**t** `array`

Number of trades

**elements**

**\[0] today** `integer`

Value today.

**\[1] last\_24h** `integer`

Value over last 24 hours.

**l** `array`

Low price

**elements**

**\[0] today** `string`

Value today.

**\[1] last\_24h** `string`

Value over last 24 hours.

**h** `array`

High price

**elements**

**\[0] today** `string`

Value today.

**\[1] last\_24h** `string`

Value over last 24 hours.

**o** `array`

Open Price

**elements**

**\[0] today** `string`

Value today.

**\[1] last\_24h** `string`

Value over last 24 hours.

**\[2] pair** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**\[3] channel\_name** `string`

Value: `ticker`

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
> Value: `ticker`

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
    "name": "ticker"
  }
}
```

```json Snapshot / Update theme={null}
[
  0,
  {
    "a": [
      "5525.40000",
      1,
      "1.000"
    ],
    "b": [
      "5525.10000",
      1,
      "1.000"
    ],
    "c": [
      "5525.10000",
      "0.00398963"
    ],
    "h": [
      "5783.00000",
      "5783.00000"
    ],
    "l": [
      "5505.00000",
      "5505.00000"
    ],
    "o": [
      "5760.70000",
      "5763.40000"
    ],
    "p": [
      "5631.44067",
      "5653.78939"
    ],
    "t": [
      11493,
      16267
    ],
    "v": [
      "2634.11501494",
      "3591.17907851"
    ]
  },
  "ticker",
  "XBT/USD"
]
```

```json Unsubscribe theme={null}
{
  "event": "unsubscribe",
  "pair": [
    "XBT/EUR",
    "XBT/USD"
  ],
  "subscription": {
    "name": "ticker"
  }
}
```
