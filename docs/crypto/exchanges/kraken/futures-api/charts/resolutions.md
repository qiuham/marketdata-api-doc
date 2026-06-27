---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/charts/resolutions
api_type: REST
updated_at: 2026-05-27 19:45:22.960688
---

# Resolutions

**GET** `https://futures.kraken.com/api/charts/v1/:tick_type/:symbol`

Candle resolutions available for specified tick type and market.

List of available tick types can be fetched from the tick types endpoint. List of available markets can be fetched from the markets endpoint.

## Request

### Path Parameters

**tick_type** `Tick Types` *required*

**Possible values:** [`spot`, `mark`, `trade`]

**symbol** `string` *required*

Market symbol

## Responses

  * 200

All resolutions for the given `tick_type` and `symbol`

  * application/json
* Schema

**Schema**

  * Array [

****Resolution (string)

**Possible values:** [`1m`, `5m`, `15m`, `30m`, `1h`, `4h`, `12h`, `1d`, `1w`]

  * ]
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/charts/v1/:tick_type/:symbol' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/charts/v1

Parameters

tick_type — pathrequired

\---spotmarktrade

symbol — pathrequired

ResponseClear

Click the `Send API Request` button above and see the response here!