---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/book
api_type: WebSocket
updated_at: 2026-05-27 19:55:06.599886
---

# Book

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    book

The book feed returns information about the order book.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `book`

**product_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.
    
    
    {  
      "event": "subscribe",  
      "feed": "book",  
      "product_ids": ["PI_XBTUSD"]  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `book`

**product_ids** `list of strings` *required*

A list of strings which represent the products that user will receive information upon.
    
    
    {  
      "event": "subscribed",  
      "feed": "book",  
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

**seq** `positive integer`

The subscription message sequence number.

**timestamp** `positive integer`

Timestamp in milliseconds

**tickSize** string

Always null.

**bids** `list of structures`

**qty** `positive float`

The quantity of the entry

**price** `positive float`

The price of the entry

**asks** `list of structures`

**qty** `positive float`

The quantity of the entry

**price** `positive float`

The price of the entry
    
    
    {  
      "feed": "book_snapshot",  
      "product_id": "PI_XBTUSD",  
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
    

## Response Delta

  * Response Fields
  * Subscription Delta Data

### MESSAGE BODY

**feed** `string`

The subscribed feed.

**product_id** `string`

The subscribed product (referred also as instrument or symbol).

**seq** `positive integer`

The subscription message sequence number.

**timestamp** `positive integer`

Timestamp in milliseconds

**side** `string`

The side of the entry.

**price** `positive float`

The price of the entry

**qty** `positive float`

The quantity of the entry
    
    
    {  
      "feed": "book",  
      "product_id": "PI_XBTUSD",  
      "side": "sell",  
      "seq": 326094134,  
      "price": 34981,  
      "qty": 0,  
      "timestamp": 1612269953629  
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