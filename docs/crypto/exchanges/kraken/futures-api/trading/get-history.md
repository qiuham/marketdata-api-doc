---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-history
api_type: REST
updated_at: 2026-05-27 19:49:27.173723
---

# Get trade history

**GET** `https://futures.kraken.com/derivatives/api/v3/history`

This endpoint returns the most recent 100 trades prior to the specified `lastTime` value up to past 7 days or recent trading engine restart (whichever is sooner).

If no `lastTime` specified, it will return 100 most recent trades.

## Request

### Query Parameters

**symbol** `string` *required*

The symbol of the Futures.

**lastTime** string

Returns the last 100 trades from the specified lastTime value.

## Responses

  * 200
* application/json
* Schema

**Schema**

oneOf
* Success Response
* ErrorResponse

**history** `object[]` *required*

A list containing structures with historical price information. The list is sorted descending by time.

  * Array [

    ↳ **price** `number` *required*

For futures: The price of a fill

For indices: The calculated value

    ↳ **side** `string`

The classification of the taker side in the matched trade: "buy" if the taker is a buyer, "sell" if the taker is a seller.

    ↳ **size** `string`

For futures: The size of a fill For indices: Not returned because N/A

    ↳ **time** `string` *required*

The date and time of a trade or an index computation

For futures: The date and time of a trade. Data is not aggregated For indices: The date and time of an index computation. For real-time indices, data is aggregated to the last computation of each full hour. For reference rates, data is not aggregated

    ↳ **trade_id** `integer<int32>`

For futures: A continuous index starting at 1 for the first fill in a Futures contract maturity For indices: Not returned because N/A

    ↳ **type** `string`

The classification of the matched trade in an orderbook:
* `fill` \- it is a normal buyer and seller
* `liquidation` \- it is a result of a user being liquidated from their position
* `assignment` \- the fill is the result of a users position being assigned to a marketmaker
* `termination` \- it is a result of a user being terminated
* `block` \- it is an element of a block trade

**Possible values:** [`fill`, `liquidation`, `assignment`, `termination`, `block`]

    ↳ **uid** `string`

    ↳ **instrument_identification_type** `string`

    ↳ **isin** `string`

    ↳ **execution_venue** `string`

    ↳ **price_notation** `string`

    ↳ **price_currency** `string`

    ↳ **notional_amount** `number`

    ↳ **notional_currency** `string`

    ↳ **publication_time** `string`

    ↳ **publication_venue** `string`

    ↳ **transaction_identification_code** `string`

    ↳ **to_be_cleared** `boolean`

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

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/history' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Parameters

symbol — queryrequired

lastTime — query

ResponseClear

Click the `Send API Request` button above and see the response here!