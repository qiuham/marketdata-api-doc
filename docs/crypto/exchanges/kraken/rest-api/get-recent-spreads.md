---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-recent-spreads
api_type: REST
updated_at: 2026-05-27 20:04:27.326420
---

# Get Recent Spreads

**GET** `https://api.kraken.com/0/public/Spread`

Returns the last ~200 top-of-book spreads for a given pair

## Request

### Query Parameters

**pair** `string` *required*

Asset pair to get data for

**Example:** XBTUSD

**since** `integer`

Returns spread data since given timestamp. Optional, intended for incremental updates within available dataset (does not contain all historical spreads).

**Example:** 1678219570

**asset_class** `string`

**Possible values:** [`tokenized_asset`]

This parameter is required on requests for non-crypto pairs, i.e. use `tokenized_asset` for xstocks.

## Responses

  * 200

Spread data retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **last** `integer`

ID to be used as since when polling for new spread data

**property name*** SpreadData

Array of spread entries `[int <time>, string <bid>, string <ask>]`

  * Array [

**type**

    ↳ **items** `object`

oneOf
* string
* integer

****string

****integer

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/Spread' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

pair — queryrequired

since — query

asset_class — query

\---tokenized_asset

ResponseClear

Click the `Send API Request` button above and see the response here!