---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-notifications
api_type: REST
updated_at: 2026-05-27 19:49:48.769869
---

# Get notifications

**GET** `https://futures.kraken.com/derivatives/api/v3/notifications`

This endpoint provides the platform's notifications.

## Responses

  * 200
* application/json
* Schema
  * success
  * failure

**Schema**

oneOf
* Success Response
* ErrorResponse

**notifications** `object[]` *required*

A list containing the notifications.

  * Array [

**effectiveTime** stringrequired

The time that notification is taking effect.

    ↳ **note** `string` *required*

The notification note.

A short description about the specific notification.

    ↳ **priority** `string` *required*

The notification priorities:
* `low`
* `medium`
* `high`

If priority == "high" then it implies downtime will occur at `effective_time` when type == "maintenance".

**Possible values:** [`low`, `medium`, `high`]

    ↳ **type** `string` *required*

The notification types:
* `market`
* `general`
* `new_feature`
* `bug_fix`
* `maintenance`
* `settlement`

If type == "maintenance" then it implies downtime will occur at `effective_time` if priority == "high".

**Possible values:** [`new_feature`, `bug_fix`, `settlement`, `general`, `maintenance`, `market`]

**expectedDowntimeMinutes** integer

The expected downtime in minutes or absent if no downtime is expected.

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
      "notifications": [  
        {  
          "type": "general",  
          "priority": "low",  
          "note": "We've launched a new Telegram group.",  
          "effectiveTime": "2022-03-31T20:38:52.677Z"  
        },  
        {  
          "type": "settlement",  
          "priority": "medium",  
          "note": "Week contracts with maturity 29/Jun/2018 expire and settle.",  
          "effectiveTime": "2018-06-29T15:00:00Z"  
        }  
      ],  
      "serverTime": "2018-06-29T15:22:05.187Z"  
    }  
    
    
    
    {  
      "result": "error",  
      "serverTime": "2016-02-25T09:45:53.818Z",  
      "error": "apiLimitExceeded"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/notifications' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent