---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/cancel-all-orders-after
api_type: REST
updated_at: 2026-05-27 19:47:39.389434
---

# Dead man's switch

**POST** `https://futures.kraken.com/derivatives/api/v3/cancelallordersafter`

This endpoint provides a Dead Man's Switch mechanism to protect the user from network malfunctions. The user can send a request with a timeout in seconds which will trigger a countdown timer that will cancel all user orders when timeout expires. The user has to keep sending request to push back the timeout expiration or they can deactivate the mechanism by specifying a timeout of zero (0).

The recommended mechanism usage is making a call every 15 to 20 seconds and provide a timeout of 60 seconds. This allows the user to keep the orders in place on a brief network failure, while keeping them safe in case of a network breakdown.

## Request

### Query Parameters

**timeout** `uint32`

The timeout specified in seconds.

## Responses

  * 200
* application/json
* Schema
  * success
  * cancel
  * failure

**Schema**

oneOf
* Success Response
* ErrorResponse

**status** `object` *required*

The status of the switch.

**currentTime** stringrequired

The server date and time that server received the request.

**triggerTime** stringrequired

The server date and time that the switch will be activated.

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
      "status": {  
        "currentTime": "2018-06-19T16:51:23.839Z",  
        "triggerTime": "2018-06-19T16:52:23.839Z"  
      },  
      "serverTime": "2018-06-19T16:51:23.839Z"  
    }  
    
    
    
    {  
      "result": "success",  
      "status": {  
        "currentTime": "2018-06-19T16:51:23.839Z",  
        "triggerTime": "0"  
      },  
      "serverTime": "2018-06-19T16:51:23.839Z"  
    }  
    
    
    
    {  
      "result": "error",  
      "serverTime": "2016-02-25T09:45:53.818Z",  
      "error": "apiLimitExceeded"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/cancelallordersafter' \  
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

timeout — query