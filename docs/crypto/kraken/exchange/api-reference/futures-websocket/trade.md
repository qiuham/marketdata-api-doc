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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/trade'
updated_at: 2026-11-13
---

# Trade

> Subscribe to information about executed trades

WSS
futures.kraken.com/ws/v1
trade

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

The `trade` feed returns information about executed trades.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `trade`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "trade",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `trade`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "trade",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Snapshot

**feed** `string`

The subscribed feed.

**product\_id** `string`

The subscribed product (referred also as instrument or symbol).

**trades** `list of structures`

**properties**

**feed** `string`

Always `trade`.

**product\_id** `string`

The product symbol.

**uid** `string`

Unique identifier for the matched trade.

**side** `string`

The classification of the taker side in the matched trade: `buy` if the taker is a buyer, `sell` if the taker is a seller.

**type** `string`

The classification of the matched trade in an orderbook: `fill` if it is a normal buyer and seller, `liquidation` if it is a result of a user being liquidated from their position, `termination` if it is a result of a user being terminated, or `block` if it is a component of a block trade.

**seq** `positive integer`

The subscription message sequence number.

**time** `positive integer`

The UTC or GMT time of the trade in milliseconds.

**qty** `positive float`

The quantity of the traded product.

**price** `positive float`

The price that the product got traded.

```json Example theme={null}
{
  "feed": "trade_snapshot",
  "product_id": "PF_XBTUSD",
  "trades": [
    {
      "feed": "trade",
      "product_id": "PF_XBTUSD",
      "uid": "caa9c653-420b-4c24-a9f1-462a054d86f1",
      "side": "sell",
      "type": "fill",
      "seq": 655508,
      "time": 1612269657781,
      "qty": 440,
      "price": 34893
    },
    {
      "feed": "trade",
      "product_id": "PF_XBTUSD",
      "uid": "45ee9737-1877-4682-bc68-e4ef818ef88a",
      "side": "sell",
      "type": "fill",
      "seq": 655507,
      "time": 1612269656839,
      "qty": 9643,
      "price": 34891
    }
  ]
}
```

***

## Response Delta

**feed** `string`

The subscribed feed.

**product\_id** `string`

The subscribed product (referred also as instrument or symbol).

**uid** `string`

Unique identifier for the matched trade.

**side** `string`

The classification of the taker side in the matched trade: `buy` if the taker is a buyer, `sell` if the taker is a seller.

**type** `string`

The classification of the matched trade in an orderbook: `fill` if it is a normal buyer and seller, `liquidation` if it is a result of a user being liquidated from their position, `termination` if it is a result of a user being terminated, or `block` if it is a component of a block trade.

**seq** `positive integer`

The subscription message sequence number.

**time** `positive integer`

The UTC or GMT time of the trade in milliseconds.

**qty** `positive float`

The quantity of the traded product.

**price** `positive float`

The price that the product got traded.

```json Example theme={null}
{
  "feed": "trade",
  "product_id": "PF_XBTUSD",
  "uid": "05af78ac-a774-478c-a50c-8b9c234e071e",
  "side": "sell",
  "type": "fill",
  "seq": 653355,
  "time": 1612266317519,
  "qty": 15000,
  "price": 34969.5
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
