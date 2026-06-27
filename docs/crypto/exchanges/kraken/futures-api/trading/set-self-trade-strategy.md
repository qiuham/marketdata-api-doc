---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/set-self-trade-strategy
api_type: REST
updated_at: 2026-05-27 19:53:47.256088
---

# Update self trade strategy

**PUT** `https://futures.kraken.com/derivatives/api/v3/self-trade-strategy`

Updates account-wide self-trade matching behavior to given strategy.

## Request

### Query Parameters

**strategy** `SelfTradeStrategy` *required*

**Possible values:** [`REJECT_TAKER`, `CANCEL_MAKER_SELF`, `CANCEL_MAKER_CHILD`, `CANCEL_MAKER_ANY`]

Defines self trade behaviour

## Responses

  * 200

Self trade strategy was successfully updated

  * application/json
* Schema

**Schema**

oneOf
* Success Response
* ErrorResponse

**strategy** `SelfTradeStrategy (string)` *required*

Self trade matching behaviour:
* `REJECT_TAKER` \- default behaviour, rejects the taker order that would match against a maker order from any sub-account
* `CANCEL_MAKER_SELF` \- only cancels the maker order if it is from the same account that sent the taker order
* `CANCEL_MAKER_CHILD` \- only allows master to cancel its own maker orders and orders from its sub-account
* `CANCEL_MAKER_ANY` \- allows both master accounts and their subaccounts to cancel maker orders

**Possible values:** [`REJECT_TAKER`, `CANCEL_MAKER_SELF`, `CANCEL_MAKER_CHILD`, `CANCEL_MAKER_ANY`]

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
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X PUT 'https://futures.kraken.com/derivatives/api/v3/self-trade-strategy' \  
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

strategy — queryrequired

\---REJECT_TAKERCANCEL_MAKER_SELFCANCEL_MAKER_CHILDCANCEL_MAKER_ANY