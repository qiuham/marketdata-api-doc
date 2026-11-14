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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/ohlc'
updated_at: 2026-11-13
---

# Candles (OHLC)

> Subscribe to Open High Low Close candle feed for currency pairs

WSS
ws.kraken.com
ohlc

Open High Low Close (Candle) feed for a currency pair and interval period. When subscribed, a snapshot of the last valid candle (irrespective of the endtime) is sent, followed by updates to the running candle.

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
> Value: `ohlc`
>
> **interval** `integer`
>
> One of: `1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600`\\
>
> Default: `1`
>
> Time interval associated with ohlc subscription in minutes.
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

**\[1] ohlc** `array`

The candle detail for a specific interval period.

**elements**

**\[0] epoc\_last** `string`

Candle last update time, in seconds since epoch.

**\[1] epoc\_end** `string`

End time of interval, in seconds since epoch.

**\[2] open** `string`

Open price of interval.

**\[3] high** `string`

High price within interval.

**\[4] low** `string`

Low price within interval.

**\[5] close** `string`

Close price of interval.

**\[6] vwap** `string`

Volume weighted average price within interval.

**\[7] volume** `string`

Accumulated volume within interval.

**\[8] count** `string`

Number of trades within interval.

**\[2] pair** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**\[3] channel\_name** `string`

Value: `ohlc-[depth]`

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
> Value: `ohlc`
>
> **interval** `integer`
>
> Condition: 'ohlc' channel only
>
> Unsubscribe to a specific interval.

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
    "interval": 5,
    "name": "ohlc"
  }
}
```

```json Snapshot / Update theme={null}
[
  42,
  [
    "1542057314.748456",
    "1542057360.435743",
    "3586.70000",
    "3586.70000",
    "3586.60000",
    "3586.60000",
    "3586.68894",
    "0.03373000",
    2
  ],
  "ohlc-5",
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
    "name": "ohlc"
  }
}
```
