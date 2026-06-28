---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/charts/tick-types
api_type: REST
updated_at: 2026-05-27 19:45:37.428373
---

# Tick Types

**GET** `https://futures.kraken.com/api/charts/v1/`

Returns all available tick types to use with the markets endpoint.

## Responses

  * 200

Tick types list

  * application/json
* Schema

**Schema**

  * Array [

****Tick Types (string)

**Possible values:** [`spot`, `mark`, `trade`]

  * ]
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/charts/v1/' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/charts/v1

ResponseClear

Click the `Send API Request` button above and see the response here!