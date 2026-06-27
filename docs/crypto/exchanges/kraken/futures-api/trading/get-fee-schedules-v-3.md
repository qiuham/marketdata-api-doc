---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-fee-schedules-v-3
api_type: REST
updated_at: 2026-05-27 19:49:12.712607
---

# Get fee schedules

**GET** `https://futures.kraken.com/derivatives/api/v3/feeschedules`

deprecated

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

**DEPRECATED** — Effective 2026-06-22, the fee values returned by this endpoint no longer reflect the fees actually charged on Futures trades. Futures fee calculation has been migrated to a centralised Kraken fee service.

To determine the fee rate applied to your trades, use the Spot [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume) endpoint authenticated with a Spot API key.

* * *

This endpoint lists all fee schedules.

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**feeSchedules** object[]required

  * Array [

**tiers** `object[]` *required*

A list containing a structures for each fee tier, see below.

  * Array [

**makerFee** numberrequired

Percentage value of maker fee in the tier.

**Example:**`0.015`

**takerFee** numberrequired

Percentage value of taker fee in the tier.

**Example:**`0.04`

**usdVolume** numberrequired

Minimum 30-day USD volume for fee tier to be applicable.

**Example:**`100000`

  * ]

    ↳ **name** `string` *required*

Name of schedule.

**Example:**`PGTMainFees`

    ↳ **uid** `string` *required*

Unique identifier of fee schedule.

**Example:**`7fc4d7c0-464f-4029-a9bb-55856d0c5247`

  * ]

**result** `string` *required*

**Possible values:** [`success`]

**Example:**`success`

**serverTime** string<date-time>required

Server time in Coordinated Universal Time (UTC)

**Example:**`2020-08-27T17:03:33.196Z`

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

    
    
    {  
      "result": "success",  
      "serverTime": "2022-03-31T20:38:53.677Z",  
      "feeSchedules": [  
        {  
          "uid": "7fc4d7c0-464f-4029-a9bb-55856d0c5247",  
          "name": "PGTMainFees",  
          "tiers": [  
            {  
              "makerFee": 0.02,  
              "takerFee": 0.05,  
              "usdVolume": 0  
            },  
            {  
              "makerFee": 0.015,  
              "takerFee": 0.04,  
              "usdVolume": 100000  
            },  
            {  
              "makerFee": 0.0125,  
              "takerFee": 0.03,  
              "usdVolume": 1000000  
            },  
            {  
              "makerFee": 0.01,  
              "takerFee": 0.025,  
              "usdVolume": 5000000  
            },  
            {  
              "makerFee": 0.0075,  
              "takerFee": 0.02,  
              "usdVolume": 10000000  
            },  
            {  
              "makerFee": 0.005,  
              "takerFee": 0.015,  
              "usdVolume": 20000000  
            },  
            {  
              "makerFee": 0.0025,  
              "takerFee": 0.0125,  
              "usdVolume": 50000000  
            },  
            {  
              "makerFee": 0,  
              "takerFee": 0.01,  
              "usdVolume": 100000000  
            }  
          ]  
        },  
        {  
          "uid": "d46c2190-81e3-4370-a333-424f24387829",  
          "name": "mainfees",  
          "tiers": [  
            {  
              "makerFee": 0.02,  
              "takerFee": 0.05,  
              "usdVolume": 0  
            },  
            {  
              "makerFee": 0.015,  
              "takerFee": 0.04,  
              "usdVolume": 100000  
            },  
            {  
              "makerFee": 0.0125,  
              "takerFee": 0.03,  
              "usdVolume": 1000000  
            },  
            {  
              "makerFee": 0.01,  
              "takerFee": 0.025,  
              "usdVolume": 5000000  
            },  
            {  
              "makerFee": 0.0075,  
              "takerFee": 0.02,  
              "usdVolume": 10000000  
            },  
            {  
              "makerFee": 0.005,  
              "takerFee": 0.015,  
              "usdVolume": 20000000  
            },  
            {  
              "makerFee": 0.0025,  
              "takerFee": 0.0125,  
              "usdVolume": 50000000  
            },  
            {  
              "makerFee": 0,  
              "takerFee": 0.01,  
              "usdVolume": 100000000  
            }  
          ]  
        }  
      ]  
    }  
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/feeschedules' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

ResponseClear

Click the `Send API Request` button above and see the response here!