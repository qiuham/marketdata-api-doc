---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-ohlc-data
api_type: REST
updated_at: 2026-05-27 20:03:28.281335
---

# Get OHLC Data

**GET** `https://api.kraken.com/0/public/OHLC`

Retrieve OHLC market data. The last entry in the OHLC array is for the current, not-yet-committed timeframe, and will always be present, regardless of the value of `since`. Returns up to 720 of the most recent entries (older data cannot be retrieved, regardless of the value of `since`).

## Request

### Query Parameters

**pair** `string` *required*

Asset pair to get data for

**Example:** XBTUSD

**interval** `integer`

**Possible values:** [`1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600`]

Time frame interval in minutes

**Default value:**`1`

**Example:** 60

**since** `integer`

Return OHLC entries since the given timestamp (intended for incremental updates)

**Example:** 1688671200

**asset_class** `string`

**Possible values:** [`tokenized_asset`]

This parameter is required on requests for non-crypto pairs, i.e. use `tokenized_asset` for xstocks.

## Responses

  * 200

OHLC data retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **last** `integer`

ID to be used as since when polling for new, committed OHLC data

**property name*** TickData

Array of tick data arrays `[int <time>, string <open>, string <high>, string <low>, string <close>, string <vwap>, string <volume>, int <count>]`

**Possible values:** `>= 8`, `<= 8`

  * Array [

**type**

    ↳ **items** `object`

**Possible values:** `>= 8`, `<= 8`

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

    
    
    curl -L 'https://api.kraken.com/0/public/OHLC' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

pair — queryrequired

interval — query

\---1515306024014401008021600

since — query

asset_class — query

\---tokenized_asset

ResponseClear

Click the `Send API Request` button above and see the response here!