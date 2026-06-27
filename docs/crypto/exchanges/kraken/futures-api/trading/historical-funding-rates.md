---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/historical-funding-rates
api_type: REST
updated_at: 2026-05-27 19:52:06.158016
---

# Historical funding rates

**GET** `https://futures.kraken.com/derivatives/api/v3/historical-funding-rates`

Returns list of historical funding rates for given market.

## Request

### Query Parameters

**symbol** `MarketSymbol` *required*

**Possible values:** Value must match regular expression `[A-Z0-9_.]+`

Market symbol.

## Responses

  * 200
  * 400

Historical funding rates for given market.

  * application/json
* Schema
  * success

**Schema**

**rates** `object[]` *required*

A list containing structures with historical funding rate information. The list is sorted ascending by timestamp.

  * Array [

**fundingRate** number<double>required

The absolute funding rate for the listed time period

**Example:**`12.03532`

**relativeFundingRate** number<double>required

The relative funding rate for the listed time period

**Example:**`12.03532`

    ↳ **timestamp** `string<date-time>` *required*

Start of the period to which the funding rate applies.

  * ]

**result** `string` *required*

**Possible values:** [`success`]

**Example:**`success`

**serverTime** string<date-time>required

Server time in Coordinated Universal Time (UTC)

**Example:**`2020-08-27T17:03:33.196Z`

    
    
    {  
      "result": "success",  
      "serverTime": "2022-06-28T09:29:04.243Z",  
      "rates": [  
        {  
          "timestamp": "2022-06-28T00:00:00.000Z",  
          "fundingRate": -8.15861558e-10,  
          "relativeFundingRate": -0.000016898883333333  
        },  
        {  
          "timestamp": "2022-06-28T04:00:00.000Z",  
          "fundingRate": -2.6115278e-11,  
          "relativeFundingRate": -5.40935416667e-7  
        },  
        {  
          "timestamp": "2022-06-28T08:00:00.000Z",  
          "fundingRate": -4.08356853e-10,  
          "relativeFundingRate": -0.000008521190625  
        }  
      ]  
    }  
    

Symbol is invalid or does not reference a perpetual market.

  * application/json
* Schema

**Schema**

**errors** `Error (string)[]`

**Possible values:** [`accountInactive`, `apiLimitExceeded`, `authenticationError`, `insufficientFunds`, `invalidAccount`, `invalidAmount`, `invalidArgument`, `invalidUnit`, `Json Parse Error`, `marketUnavailable`, `nonceBelowThreshold`, `nonceDuplicate`, `notFound`, `requiredArgumentMissing`, `Server Error`, `Unavailable`, `unknownError`]

**error** `Error (string)` *required*

Error description.
* `accountInactive`: The Futures account the request refers to is inactive
* `apiLimitExceeded`: The API limit for the calling IP address has been exceeded
* `authenticationError`: The request could not be authenticated
* `insufficientFunds`: The amount requested for transfer is below the amount of funds available
* `invalidAccount`: The Futures account the transfer request refers to is invalid
* `invalidAmount`: The amount the transfer request refers to is invalid
* `invalidArgument`: One or more arguments provided are invalid
* `invalidUnit`: The unit the transfer request refers to is invalid
* `Json Parse Error`: The request failed to pass valid JSON as an argument
* `marketUnavailable`: The market is currently unavailable
* `nonceBelowThreshold`: The provided nonce is below the threshold
* `nonceDuplicate`: The provided nonce is a duplicate as it has been used in a previous request
* `notFound`: The requested information could not be found
* `requiredArgumentMissing`: One or more required arguments are missing
* `Server Error`: There was an error processing the request
* `Unavailable`: The endpoint being called is unavailable
* `unknownError`: An unknown error has occurred

**Possible values:** [`accountInactive`, `apiLimitExceeded`, `authenticationError`, `insufficientFunds`, `invalidAccount`, `invalidAmount`, `invalidArgument`, `invalidUnit`, `Json Parse Error`, `marketUnavailable`, `nonceBelowThreshold`, `nonceDuplicate`, `notFound`, `requiredArgumentMissing`, `Server Error`, `Unavailable`, `unknownError`]

**result** `string` *required*

**Possible values:** [`error`]

**Example:**`error`

**serverTime** string<date-time>required

Server time in Coordinated Universal Time (UTC)

**Example:**`2020-08-27T17:03:33.196Z`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/historical-funding-rates' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Parameters

symbol — queryrequired

ResponseClear

Click the `Send API Request` button above and see the response here!