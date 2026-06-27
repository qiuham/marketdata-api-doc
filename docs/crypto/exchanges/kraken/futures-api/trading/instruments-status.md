---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/instruments-status
api_type: REST
updated_at: 2026-05-27 19:52:27.515811
---

# Get instrument status list

**GET** `https://futures.kraken.com/derivatives/api/v3/instruments/status`

Returns price dislocation and volatility details for all markets.

## Request

### Query Parameters

**contractType** string[]

**Possible values:** [`futures_inverse`, `futures_vanilla`, `flexible_futures`, `options`, `all`]

Contract type(s) to return statuses for.

By default, includes all futures instrument types.

Multi-value example: `?contractType=futures_inverse&contractType=futures_vanilla`

## Responses

  * 200
* application/json
* Schema

**Schema**

oneOf
* Success Response
* ErrorResponse

**instrumentStatus** object[]required

  * Array [

**tradeable** `MarketSymbol (string)` *required*

Market symbol

**Possible values:** Value must match regular expression `[A-Z0-9_.]+`

**Example:**`PF_BTCUSD`

**experiencingDislocation** booleanrequired

**priceDislocationDirection** string | nullnullablerequired

**Possible values:** [`ABOVE_UPPER_BOUND`, `BELOW_LOWER_BOUND`]

**experiencingExtremeVolatility** booleanrequired

**extremeVolatilityInitialMarginMultiplier** integerrequired

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
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/instruments/status' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Parameters

contractType — query

futures_inversefutures_vanillaflexible_futuresoptionsall

ResponseClear

Click the `Send API Request` button above and see the response here!