---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/charts/symbols
api_type: Market Data
updated_at: 2026-05-27 19:45:30.204770
---

# Markets

**GET** `https://futures.kraken.com/api/charts/v1/:tick_type`

Markets available for specified tick type.

List of available tick types can be fetched from the tick types endpoint.

## Request

### Path Parameters

**tick_type** `Tick Types` *required*

**Possible values:** [`spot`, `mark`, `trade`]

## Responses

  * 200

Markets list

  * application/json
* Schema
  * Example

**Schema**

  * Array [

****string

  * ]

    
    
    [  
      "PI_XRPUSD",  
      "FI_XRPUSD_210625",  
      "FI_XBTUSD_210528",  
      "PI_XBTUSD"  
    ]  
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/charts/v1/:tick_type' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/charts/v1

Parameters

tick_type — pathrequired

\---spotmarktrade

ResponseClear

Click the `Send API Request` button above and see the response here!