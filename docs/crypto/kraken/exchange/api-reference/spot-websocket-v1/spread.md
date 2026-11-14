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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/spread'
updated_at: 2026-11-13
---

# Spread

> Subscribe to spread feed for currency pairs

WSS
ws.kraken.com
spread

Spread feed for a currency pair. Provides the best bid and ask prices along with their volumes.

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
> Value: `spread`
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

**\[1] spread** `array`

**elements**

**\[0] bid** `string`

Bid price.

**\[1] ask** `string`

Ask price.

**\[2] timestamp** `string`

Time of the current top-of-book quote, in seconds since epoch. This reflects the creation time of the best bid/ask order(s) currently resting at the top of book, not the time the message was generated. Because of this, the value is not monotonic: when the top of book changes to an order that was already resting in the book (for example after a trade), this timestamp may move backwards relative to the previous message. This is expected and does not indicate stale or dropped data.

**\[3] bid\_volume** `string`

Bid Volume.

**\[4] ask\_volume** `string`

Ask Volume.

**\[2] pair** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**\[3] channel\_name** `string`

Value: `spread`

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
> Value: `spread`

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
    "name": "spread"
  }
}
```

```json Snapshot / Update theme={null}
[
  0,
  [
    "5698.40000",
    "5700.00000",
    "1542057299.545897",
    "1.01234567",
    "0.98765432"
  ],
  "spread",
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
    "name": "spread"
  }
}
```
