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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/ticker'
updated_at: 2026-11-13
---

# Ticker

> Subscribe to ticker information about listed products

WSS
futures.kraken.com/ws/v1
ticker

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

The `ticker` feed returns ticker information about listed products. Only tradeable markets are available via individual WebSocket market data feeds. Delta messages are throttled such that they are published every 1s.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `ticker`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "ticker",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `ticker`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "ticker",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Snapshot

The subscription data will return values for all fields even if the value of only a single field has changed since the last payload.

**time** `positive integer`

The UTC time of the server in milliseconds.

**product\_id** `string`

The subscribed product (referred also as instrument or symbol).

**funding\_rate** `float`

The current funding rate. If zero, field is not populated. (Perpetuals only)

**funding\_rate\_prediction** `float`

The predicted funding rate for the next funding period, based on the assumption that the last recorded market premium will stay constant until the next funding realisation time. This can be highly inaccurate, especially at the start of a funding period. If zero, field is not populated. (Perpetuals only)

**relative\_funding\_rate** `float`

The absolute funding rate relative to the spot price at the time of funding rate calculation. If zero, field is not populated. (Perpetuals only)

**relative\_funding\_rate\_prediction** `float`

The predicted absolute funding rate relative to the current spot price for the next funding period, based on the assumption that the last recorded market premium will stay constant until the next funding realisation time. This can be highly inaccurate, especially at the start of a funding period. If zero, field is not populated. (Perpetuals only)

**next\_funding\_rate\_time** `float`

The time until next funding rate in milliseconds. (Perpetuals only)

**feed** `string`

The subscribed feed.

**bid** `positive float`

The price of the current best bid.

**ask** `positive float`

The price of the current best ask.

**bid\_size** `positive float`

The size of the current best bid.

**ask\_size** `positive float`

The size of the current best ask.

**volume** `positive float`

The sum of the sizes of all fills observed in the last 24 hours.

**dtm** `positive integer`

The days until maturity.

**leverage** `string`

The leverage of the product.

**index** `positive float`

The real time index of the product.

**last** `positive float`

The price of the last fill.

**change** `float`

The 24h change in price.

**suspended** `boolean`

True if the market is suspended.

**tag** `string`

Currently can be `perpetual`, `month` or `quarter`. Other tags may be added without notice.

**pair** `string`

The currency pair of the instrument.

**openInterest** `float`

The current open interest of the instrument.

**markPrice** `float`

The market price of the instrument.

**maturityTime** `positive integer`

The UTC time, in milliseconds, at which the contract will stop trading.

**post\_only** `boolean`

True if the market is in post-only.

**volumeQuote** `positive float`

The same as `volume` except that, for multi-collateral futures, it is converted to the non-base currency.

**open** `positive float`

The first traded price in the last 24h.

**high** `positive float`

The highest traded price in the last 24h.

**low** `positive float`

The lowest traded price in the last 24h.

**premium** `float`

The current premium (percentage difference between the futures price and the index price).

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

```json Example: Futures Snapshot theme={null}
{
  "time": 1676393235406,
  "product_id": "PF_XBTUSD",
  "funding_rate": -6.2604214e-11,
  "funding_rate_prediction": -3.65989977e-10,
  "relative_funding_rate": -1.380384722222e-6,
  "relative_funding_rate_prediction": -8.047629166667e-6,
  "next_funding_rate_time": 1676394000000,
  "feed": "ticker",
  "bid": 21978.5,
  "ask": 21987.0,
  "bid_size": 2536.0,
  "ask_size": 13948.0,
  "volume": 31403908.0,
  "dtm": 0,
  "leverage": "50x",
  "index": 21984.54,
  "premium": -0.0,
  "last": 21983.5,
  "change": 1.9974017538161748,
  "suspended": false,
  "tag": "perpetual",
  "pair": "XBT:USD",
  "openInterest": 30072580.0,
  "markPrice": 21979.68641534714,
  "maturityTime": 0,
  "post_only": false,
  "volumeQuote": 31403908.0,
  "open": 21968.5,
  "high": 22123.0,
  "low": 21456.0
}
```

```json Example: Options Snapshot theme={null}
{
  "time": 1676393235406,
  "product_id": "OF_ETHUSD_240101_1000_C",
  "feed": "ticker",
  "bid": 21978.5,
  "ask": 21987.0,
  "bid_size": 2536.0,
  "ask_size": 13948.0,
  "volume": 31403908.0,
  "dtm": 0,
  "index": 21984.54,
  "last": 21983.5,
  "change": 1.9974017538161748,
  "suspended": false,
  "tag": "month",
  "pair": "ETH:USD",
  "openInterest": 30072580.0,
  "markPrice": 100.68641534714,
  "maturityTime": 1676393235406,
  "post_only": false,
  "volumeQuote": 31403908.0,
  "greeks": {
    "iv": 0.3,
    "delta": 0.5,
    "gamma": 0.5,
    "vega": 0.5,
    "theta": 0.5,
    "rho": 0.5
  }
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
