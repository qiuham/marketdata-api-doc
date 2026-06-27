---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/add-assignment-program
api_type: REST
updated_at: 2026-05-27 19:47:17.664176
---

# Add assignment preference

**POST** `https://futures.kraken.com/derivatives/api/v3/assignmentprogram/add`

This endpoint adds an assignment program preference

## Request

### Query Parameters

**contractType** stringrequired

Type of contract for the assignment program preference. Options can be found in the 'accounts' structure in the Get Wallets /accounts response

**contract** `string`

A specific contract for this assignment program preference. Required for "flex" contracts if base/quote currencies are not included.

**maxSize** number

The maximum size for an assignment

**maxPosition** number

The maximum position

**acceptLong** booleanrequired

Accept to take long positions

**acceptShort** booleanrequired

Accept to take short positions

**timeFrame** AssignmentPreferenceTimeFramerequired

**Possible values:** [`WEEKDAYS`, `WEEKEND`, `ALL`]

When is the program preference valid

**enabled** `boolean` *required*

enabled assignment

## Responses

  * 200
* application/json
* Schema

**Schema**

oneOf
* Success Response
* ErrorResponse

**id** `number` *required*

**participant** `object` *required*

**contractType** stringrequired

    ↳ **contract** `string | nullnullable`

**maxSize** number,null<double>nullable

**maxPosition** number,null<double>nullable

**acceptLong** booleanrequired

**acceptShort** booleanrequired

**timeFrame** AssignmentPreferenceTimeFrame (string)required

**Possible values:** [`WEEKDAYS`, `WEEKEND`, `ALL`]

    ↳ **enabled** `boolean` *required*

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

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/assignmentprogram/add' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent

Parameters

contractType — queryrequired

acceptLong — queryrequired

\---truefalse

acceptShort — queryrequired

\---truefalse

timeFrame — queryrequired

\---WEEKDAYSWEEKENDALL

enabled — queryrequired

\---truefalse

contract — query

maxSize — query

maxPosition — query