---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/set-leverage-setting
api_type: REST
updated_at: 2026-05-27 19:53:32.682879
---

# Set leverage settings

**PUT** `https://futures.kraken.com/derivatives/api/v3/leveragepreferences`

Sets a contract's margin mode, either "isolated" or "cross" margin.

When specifying a max leverage, the contract's margin mode will be isolated.

Calling this endpoint can result in the following error codes:

  * 87: Contract does not exist
  * 88: Contract not a multi-collateral futures contract
  * 41: Would cause liquidation

## Request

### Query Parameters

**symbol** `string` *required*

Symbol for the leverage preference.

**maxLeverage** number

Max leverage to set.

When present, the symbol's margin mode will be set to "isolated". When missing, the symbol's margin mode will be set to "cross".

## Responses

  * 200

OK

  * application/json
* Schema
  * success

**Schema**

oneOf
* SuccessResponse
* ErrorResponse

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
      "serverTime": "2022-06-28T14:48:58.711Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X PUT 'https://futures.kraken.com/derivatives/api/v3/leveragepreferences' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key

authent

Parameters

symbol — queryrequired

maxLeverage — query