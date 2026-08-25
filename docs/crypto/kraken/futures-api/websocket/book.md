---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/book
api_type: WebSocket
updated_at: 2026-08-25 19:14:57.346399
---

# Book

WSSfutures.kraken.com/ws/v1book

The `book` feed returns information about the order book.

* * *

## 

Request

string

required

`subscribe` or `unsubscribe`

string

required

The requested subscription feed. Value: `book`

list of strings

required

A list of strings which represent the products that user will receive information upon.
    
    
    {
      "event": "subscribe",
      "feed": "book",
      "product_ids": ["PF_XBTUSD"]
    }
* * *

## 

Response Success

string

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`The result.

string

The requested subscription feed. Value: `book`

list of strings

required

A list of strings which represent the products that user will receive information upon.
    
    
    {
      "event": "subscribed",
      "feed": "book",
      "product_ids": ["PF_XBTUSD"]
    }
* * *

## 

Response Snapshot

string

The subscribed feed.

string

The subscribed product (referred also as instrument or symbol).

positive integer

The subscription message sequence number.

positive integer

Timestamp in milliseconds.

string

Always null.

list of structures

Show properties

positive float

The quantity of the entry.

positive float

The price of the entry.

list of structures

Show properties

positive float

The quantity of the entry.

positive float

The price of the entry.
    
    
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
* * *

## 

Response Delta

string

The subscribed feed.

string

The subscribed product (referred also as instrument or symbol).

positive integer

The subscription message sequence number.

positive integer

Timestamp in milliseconds.

string

The side of the entry.

positive float

The price of the entry.

positive float

The quantity of the entry.
    
    
    {
      "feed": "book",
      "product_id": "PF_XBTUSD",
      "side": "sell",
      "seq": 326094134,
      "price": 34981,
      "qty": 0,
      "timestamp": 1612269953629
    }
* * *

## 

Response Error

string

Value: `error`

string

One of: `Invalid product id`, `Invalid feed`, `Json Error`An error message.
    
    
    {
      "event": "error",
      "message": "Invalid product id"
    }
    

Was this page helpful?

Ctrl+I