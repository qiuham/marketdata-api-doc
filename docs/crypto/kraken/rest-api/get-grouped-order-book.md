---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-grouped-order-book
api_type: REST
updated_at: 2026-05-27 20:02:58.609657
---

# Get Grouped Order Book

**GET** `https://api.kraken.com/0/public/GroupedBook`

The GroupedBook endpoint aggregates the volume in the order book over a specified tick range. It provides a summary of liquidity deep into the book, useful for user interface display.

Bids and asks between grouped price levels are accumulated to the nearest passive level (asks rounded up, bids down).

## Request

  * application/json

### Body**required**

**pair** `string` *required*

Asset pair to get order book for

**Example:**`BTC/USD`

**depth** `integer`

The number of price levels to return per side (bids/asks).

**Possible values:** [`10`, `25`, `100`, `250`, `1000`]

**Default value:**`10`

**Example:**`10`

**grouping** `integer<int32>nullable`

Specifies how many tick levels should be within each price level. Bids and asks between grouped price levels are accumulated to the nearest passive level (asks rounded up, bids down).

**Possible values:** [`1`, `5`, `10`, `25`, `50`, `100`, `250`, `500`, `1000`]

**Default value:**`1`

**Example:**`1000`

## Responses

  * 200

Grouped order book data retrieved.

  * application/json
* Schema
  * Example

**Schema**

**result** `object`

    ↳ **pair** `string`

Asset pair

    ↳ **grouping** `integer`

The grouping value used

    ↳ **bids** `object[]`

Aggregated bid levels

  * Array [

        ↳ **price** `string`

Grouped price level

        ↳ **qty** `string`

Aggregated quantity at this price level

  * ]

        ↳ **asks** `object[]`

Aggregated ask levels

  * Array [

            ↳ **price** `string`

Grouped price level

            ↳ **qty** `string`

Aggregated quantity at this price level

  * ]

**error** `array[]`

    
    
    {  
      "error": [],  
      "result": {  
        "pair": "BTC/USD",  
        "grouping": 1000,  
        "bids": [  
          {  
            "price": "90400.00000",  
            "qty": "19.83057746"  
          },  
          {  
            "price": "90300.00000",  
            "qty": "45.35073006"  
          },  
          {  
            "price": "90200.00000",  
            "qty": "35.33199856"  
          },  
          {  
            "price": "90100.00000",  
            "qty": "32.40807838"  
          },  
          {  
            "price": "90000.00000",  
            "qty": "46.00445468"  
          },  
          {  
            "price": "89900.00000",  
            "qty": "22.71486458"  
          },  
          {  
            "price": "89800.00000",  
            "qty": "11.55482018"  
          },  
          {  
            "price": "89700.00000",  
            "qty": "13.77715743"  
          },  
          {  
            "price": "89600.00000",  
            "qty": "27.72185770"  
          },  
          {  
            "price": "89500.00000",  
            "qty": "14.09383330"  
          }  
        ],  
        "asks": [  
          {  
            "price": "90500.00000",  
            "qty": "38.96185061"  
          },  
          {  
            "price": "90600.00000",  
            "qty": "55.96402032"  
          },  
          {  
            "price": "90700.00000",  
            "qty": "34.64783055"  
          },  
          {  
            "price": "90800.00000",  
            "qty": "25.26797469"  
          },  
          {  
            "price": "90900.00000",  
            "qty": "20.48922196"  
          },  
          {  
            "price": "91000.00000",  
            "qty": "14.87773628"  
          },  
          {  
            "price": "91100.00000",  
            "qty": "18.99740224"  
          },  
          {  
            "price": "91200.00000",  
            "qty": "19.00592802"  
          },  
          {  
            "price": "91300.00000",  
            "qty": "4.05573682"  
          },  
          {  
            "price": "91400.00000",  
            "qty": "1.60667017"  
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

    
    
    curl -L -X GET 'https://api.kraken.com/0/public/GroupedBook' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -d '{  
      "pair": "BTC/USD",  
      "depth": 10,  
      "grouping": 1000  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Body required
    
    
    {
      "pair": "BTC/USD",
      "depth": 10,
      "grouping": 1000
    }
    

ResponseClear

Click the `Send API Request` button above and see the response here!