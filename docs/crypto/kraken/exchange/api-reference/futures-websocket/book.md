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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/book'
updated_at: 2026-11-13
---

# Book

> Subscribe to order book data

WSS
futures.kraken.com/ws/v1
book

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

The `book` feed returns information about the order book.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `book`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "book",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `book`

**product\_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "book",
  "product_ids": ["PF_XBTUSD"]
}
```

***

## Response Snapshot

**feed** `string`

The subscribed feed.

**product\_id** `string`

The subscribed product (referred also as instrument or symbol).

**seq** `positive integer`

The subscription message sequence number.

**timestamp** `positive integer`

Timestamp in milliseconds.

**tickSize** `string`

Always null.

**bids** `list of structures`

**properties**

**qty** `positive float`

The quantity of the entry.

**price** `positive float`

The price of the entry.

**asks** `list of structures`

**properties**

**qty** `positive float`

The quantity of the entry.

**price** `positive float`

The price of the entry.

```json Example theme={null}
{
  "feed": "book_snapshot",
  "product_id": "PF_XBTUSD",
  "timestamp": 1612269825817,
  "seq": 326072249,
  "tickSize": null,
  "bids": [
    {
      "price": 34892.5,
      "qty": 6385
    },
    {
      "price": 34892,
      "qty": 10924
    }
  ],
  "asks": [
    {
      "price": 34911.5,
      "qty": 20598
    },
    {
      "price": 34912,
      "qty": 2300
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

**seq** `positive integer`

The subscription message sequence number.

**timestamp** `positive integer`

Timestamp in milliseconds.

**side** `string`

The side of the entry.

**price** `positive float`

The price of the entry.

**qty** `positive float`

The quantity of the entry.

```json Example theme={null}
{
  "feed": "book",
  "product_id": "PF_XBTUSD",
  "side": "sell",
  "seq": 326094134,
  "price": 34981,
  "qty": 0,
  "timestamp": 1612269953629
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
