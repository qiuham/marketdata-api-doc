---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/trade
api_type: WebSocket
updated_at: 2026-05-27 19:56:19.557463
---

# Trade

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    trade

The trade feed returns information about executed trades

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `trade`

**product_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.
    
    
    {  
      "event": "subscribe",  
      "feed": "trade",  
      "product_ids": ["PI_XBTUSD"]  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `trade`

**product_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.
    
    
    {  
      "event": "subscribed ",  
      "feed": "trade",  
      "product_ids": ["PI_XBTUSD"]  
    }  
    

## Response Snapshot

  * Response Fields
  * Subscription Snapshot Data

### MESSAGE BODY

**feed** `string`

The subscribed feed.

**product_id** `string`

The subscribed product (referred also as instrument or symbol).

**trades** `list of structures`

**uid** `string`

Unique identifier for the matched trade.

**side** `string`

The classification of the taker side in the matched trade: `buy` if the taker is a buyer, `sell` if the taker is a seller.

**type** `string`

The classification of the matched trade in an orderbook: `fill`if it is a normal buyer and seller, `liquidation` if it is a result of a user being liquidated from their position, `termination` if it is a result of a user being terminated, or block if it is a component of a `block` trade.

**seq** `positive integer`

The subscription message sequence number.

**time** `positive integer`

The UTC or GMT time of the trade in milliseconds

**qty** `positive float`

The quantity of the traded product.

**price** `positive float`

The price that the product got traded.
    
    
    {  
      "feed": "trade_snapshot",  
      "product_id": "PI_XBTUSD",  
      "trades": [  
        {  
          "feed": "trade",  
          "product_id": "PI_XBTUSD",  
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
          "product_id": "PI_XBTUSD",  
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
    

## Response Delta

  * Response Fields
  * Subscription Delta Data

### MESSAGE BODY

**feed** `string`

The subscribed feed.

**product_id** `string`

The subscribed product (referred also as instrument or symbol).

**uid** `string`

Unique identifier for the matched trade.

**side** `string`

The classification of the taker side in the matched trade: `buy` if the taker is a buyer, `sell` if the taker is a seller.

**type** `string`

The classification of the matched trade in an orderbook: `fill`if it is a normal buyer and seller, `liquidation` if it is a result of a user being liquidated from their position, `termination` if it is a result of a user being terminated, or block if it is a component of a `block` trade.

**seq** `positive integer`

The subscription message sequence number.

**time** `positive integer`

The UTC or GMT time of the trade in milliseconds

**qty** `positive float`

The quantity of the traded product.

**price** `positive float`

The price that the product got traded.
    
    
    {  
      "feed": "trade",  
      "product_id": "PI_XBTUSD",  
      "uid": "05af78ac-a774-478c-a50c-8b9c234e071e",  
      "side": "sell",  
      "type": "fill",  
      "seq": 653355,  
      "time": 1612266317519,  
      "qty": 15000,  
      "price": 34969.5  
    }  
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

An error message out of:  
`Invalid product id`  
`Invalid feed`  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Invalid product id"  
    }