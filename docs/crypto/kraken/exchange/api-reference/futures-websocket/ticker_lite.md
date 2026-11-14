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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/ticker_lite'
updated_at: 2026-11-13
---

# Ticker Lite

> Subscribe to lightweight ticker information about listed products

WSS
futures.kraken.com/ws/v1
ticker\_lite

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

The `ticker_lite` feed returns ticker information about listed products. Delta messages are throttled such that they are published every 1s.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `ticker_lite`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "ticker_lite",
  "product_ids": ["PF_XBTUSD", "PF_ETHUSD"]
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `ticker_lite`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "ticker_lite",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Snapshot

**feed** `string`

The subscribed feed.

**product\_id** `string`

The subscribed product (referred also as instrument or symbol).

**bid** `positive float`

The price of the current best bid.

**ask** `positive float`

The price of the current best ask.

**change** `float`

The 24h change in price.

**premium** `float`

The premium associated with the product.

**volume** `positive float`

The sum of the sizes of all fills observed in the last 24 hours.

**tag** `string`

Currently can be `perpetual`, `month`, `quarter`, or `semiannual`. Other tags may be added without notice.

**pair** `string`

The currency pair of the instrument.

**dtm** `integer`

The days until maturity.

**maturityTime** `positive integer`

Maturity time in milliseconds.

**volumeQuote** `positive float`

The same as `volume` except that, for multi-collateral futures, it is converted to the non-base currency.

**greeks** `structure`

The current Greeks, if this is an option.

**properties**

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

```json Example: Perpetual theme={null}
{
  "feed": "ticker_lite",
  "product_id": "PF_XBTUSD",
  "bid": 34932,
  "ask": 34949.5,
  "change": 3.3705205220015966,
  "premium": 0.1,
  "volume": 264126741,
  "tag": "perpetual",
  "pair": "XBT:USD",
  "dtm": 0,
  "maturityTime": 0,
  "volumeQuote": 264126741
}
```

```json Example: Perpetual (ETH) theme={null}
{
  "feed": "ticker_lite",
  "product_id": "PF_ETHUSD",
  "bid": 1753.45,
  "ask": 1760.35,
  "change": 13.448175559936647,
  "premium": 0.1,
  "volume": 6899673.0,
  "tag": "perpetual",
  "pair": "ETH:USD",
  "dtm": 0,
  "maturityTime": 0,
  "volumeQuote": 6899673.0
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
