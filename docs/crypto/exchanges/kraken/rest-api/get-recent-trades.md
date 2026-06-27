---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-recent-trades
api_type: REST
updated_at: 2026-05-27 20:04:34.571865
---

# Get Recent Trades

**GET** `https://api.kraken.com/0/public/Trades`

Returns the last 1000 trades by default

## Request

### Query Parameters

**pair** `string` *required*

Asset pair to get data for

**Example:** XBTUSD

**since** `string`

Return trade data since given timestamp

**Example:** 1616663618

**count** `integer`

**Possible values:** `>= 1` and `<= 1000`

Return specific number of trades, up to 1000

**Default value:**`1000`

**Example:** 2

**asset_class** `string`

**Possible values:** [`tokenized_asset`]

This parameter is required on requests for non-crypto pairs, i.e. use `tokenized_asset` for xstocks.

## Responses

  * 200

Trade data retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **last** `string`

ID to be used as since when polling for new trade data

**property name*** TickData

Array of trade entries `[<price>, <volume>, <time>, <buy/sell>, <market/limit>, <miscellaneous>, <trade_id>]`

  * Array [

**type**

    ↳ **items** `object`

oneOf
* string
* number

****string

****number

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/Trades' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

pair — queryrequired

since — query

count — query

asset_class — query

\---tokenized_asset

ResponseClear

Click the `Send API Request` button above and see the response here!