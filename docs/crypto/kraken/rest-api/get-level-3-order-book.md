---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-level-3-order-book
api_type: REST
updated_at: 2026-05-27 20:03:21.335461
---

# Query L3 Order Book

**POST** `https://api.kraken.com/0/private/Level3`

Retrieve Level3 order book data, which provides individual order information at each price level. This includes order IDs and timestamps for each order in the book.

The Level3 endpoint requires authentication.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**pair** `string` *required*

Asset pair to get order book for

**Example:**`YFI/EUR`

**depth** `integer`

Number of price levels to return per side (bids/asks). Use 0 to return the full book.

**Possible values:** [`0`, `10`, `25`, `100`, `250`, `1000`]

**Default value:**`100`

**Example:**`10`

## Responses

  * 200

Level 3 order book data retrieved.

  * application/json
* Schema
  * Example

**Schema**

**result** `object`

    ↳ **pair** `string`

Asset pair

    ↳ **bids** `object[]`

Bid orders

  * Array [

        ↳ **price** `string`

Bid price

        ↳ **qty** `string`

Bid quantity

        ↳ **order_id** `string`

Order ID

        ↳ **timestamp** `integer`

Order timestamp (nanoseconds)

  * ]

        ↳ **asks** `object[]`

Ask orders

  * Array [

            ↳ **price** `string`

Ask price

            ↳ **qty** `string`

Ask quantity

            ↳ **order_id** `string`

Order ID

            ↳ **timestamp** `integer`

Order timestamp (nanoseconds)

  * ]

**error** `array[]`

    
    
    {  
      "error": [],  
      "result": {  
        "pair": "YFI/EUR",  
        "bids": [  
          {  
            "price": "3062.00000",  
            "qty": "0.29665800",  
            "order_id": "O5KJU4-IEQTM-NDMS6W",  
            "timestamp": 1765622008594292000  
          },  
          {  
            "price": "3062.00000",  
            "qty": "0.13917400",  
            "order_id": "OERRY6-MXYER-6EQKNY",  
            "timestamp": 1765622011396903000  
          }  
        ],  
        "asks": [  
          {  
            "price": "3066.00000",  
            "qty": "0.00278335",  
            "order_id": "ORAWGV-N5L4J-LBA3WH",  
            "timestamp": 1765622008499456000  
          },  
          {  
            "price": "3067.00000",  
            "qty": "0.13902210",  
            "order_id": "OZWNZS-QE3G6-ZPKZUT",  
            "timestamp": 1765622021013826600  
          }  
        ]  
      }  
    }  
* curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Level3' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "pair": "YFI/EUR",  
      "depth": 10  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 0,
      "pair": "YFI/EUR",
      "depth": 10
    }