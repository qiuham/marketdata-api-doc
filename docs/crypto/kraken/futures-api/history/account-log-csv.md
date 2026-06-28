---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/account-log-csv
api_type: REST
updated_at: 2026-05-27 19:45:58.426252
---

# Account log (CSV)

**GET** `https://futures.kraken.com/api/history/v3/accountlogcsv`

Lists recent account log entries in CSV format.

## Request

### Query Parameters

**conversion_details** `boolean`

Include exchange rate, exchange rate from currency, and conversion fee for conversions.

**Default value:**`false`

## Responses

  * 200
  * 401
  * 429

A CSV formatted response of most recent account log entries.

Credentials required.

Rate limited.

**Response Headers**

**rate-limit-reset**

Time remaining (in seconds) until repeat request (i.e., same cost) will be accepted.
* text/plain
* Schema

**Schema**

**string** `string`

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/accountlogcsv' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/history/v3

Auth

general-api-key-read-only

authent

Parameters

conversion_details — query

\---truefalse