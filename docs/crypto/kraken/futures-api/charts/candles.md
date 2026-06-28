---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/charts/candles
api_type: Market Data
updated_at: 2026-05-27 19:45:00.969748
---

# Market Candles

**GET** `https://futures.kraken.com/api/charts/v1/:tick_type/:symbol/:resolution`

Candles for specified tick type, market, and resolution.

List of available tick types can be fetched from the tick types endpoint. List of available markets can be fetched from the markets endpoint. List of available resolutions can be fetched from the resolutions endpoint.

## Request

### Path Parameters

**tick_type** `Tick Types` *required*

**Possible values:** [`spot`, `mark`, `trade`]

**symbol** `string` *required*

Market symbol

**resolution** `Resolution` *required*

**Possible values:** [`1m`, `5m`, `15m`, `30m`, `1h`, `4h`, `12h`, `1d`, `1w`]

### Query Parameters

**from** `number`

From date in epoch seconds

**to** `number`

To date in epoch seconds

**count** `integer`

**Possible values:** `>= 0`

Number of candles to return.

## Responses

  * 200

OHLC candles

  * application/json
* Schema

**Schema**

**candles** `object[]` *required*

OHLC candles

  * Array [

    ↳ **time** `integer<int64>` *required*

Epoch in ms

**Example:**`1620816960000`

    ↳ **high** `string<big-decimal>` *required*

**Example:**`56475.00000000000`

    ↳ **low** `string<big-decimal>` *required*

**Example:**`55935.00000000000`

    ↳ **open** `string<big-decimal>` *required*

**Example:**`56294.00000000000`

    ↳ **close** `string<big-decimal>` *required*

**Example:**`56250.00000000000`

    ↳ **volume** `number<int64>` *required*

**Example:**`10824`

  * ]

    ↳ **more_candles** `boolean` *required*

True if there are more candles in time range
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/charts/v1/:tick_type/:symbol/:resolution' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/charts/v1

Parameters

tick_type — pathrequired

\---spotmarktrade

symbol — pathrequired

resolution — pathrequired

\---1m5m15m30m1h4h12h1d1w

from — query

to — query

count — query

ResponseClear

Click the `Send API Request` button above and see the response here!