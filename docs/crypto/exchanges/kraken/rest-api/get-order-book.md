---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-order-book
api_type: REST
updated_at: 2026-05-27 20:03:57.837106
---

# Get Order Book

**GET** `https://api.kraken.com/0/public/Depth`

Returns level 2 (L2) order book, which describes the individual price levels in the book with aggregated order quantities at each level.

## Request

### Query Parameters

**pair** `string` *required*

Asset pair to get data for

**Example:** XBTUSD

**count** `integer`

**Possible values:** `>= 1` and `<= 500`

Maximum number of asks/bids

**Default value:**`100`

**Example:** 2

**asset_class** `string`

**Possible values:** [`tokenized_asset`]

This parameter is required on requests for non-crypto pairs, i.e. use `tokenized_asset` for xstocks.

## Responses

  * 200

Order book entries retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

**property name*** OrderBook

Asset Pair Order Book Entries

    ↳ **asks** `array[]`

Ask side array of entries `[<price>, <volume>, <timestamp>]`

**Possible values:** `>= 3`, `<= 3`

        ↳ **bids** `array[]`

Bid side array of entries `[<price>, <volume>, <timestamp>]`

**Possible values:** `>= 3`, `<= 3`

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/Depth' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

pair — queryrequired

count — query

asset_class — query

\---tokenized_asset

ResponseClear

Click the `Send API Request` button above and see the response here!