---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/create-user-rfq
api_type: REST
updated_at: 2026-05-27 19:48:08.058194
---

# Create a new RFQ

**POST** `https://demo-futures.kraken.com/derivatives/api/v3/rfqs/open-rfqs`

Create a new RFQ for the authenticated account.

Note: This is currently available exclusively in the Kraken pre-prod environments.

## Request

### Query Parameters

**json** `any` *required*

JSON-encoded RFQ creation request.

## Responses

  * 200
  * 404

RFQ creation result

  * application/json
* Schema

**Schema**

**status**

**Possible values:** [`placed`, `failed`]
* placed
* failed

**result** `string` *required*

**Possible values:** [`success`]

**serverTime** string<date-time>required

**rfqUid** string<uuid>required

**result** `string` *required*

**Possible values:** [`success`]

**serverTime** string<date-time>required

**reason** `string` *required*

**Possible values:** [`insufficientMargin`, `maxPositionExceed`, `wouldCauseLiquidation`, `fixedLeverageTooHigh`, `orderError`, `symbolNotFound`, `invalidExpiry`, `invalidQuantity`, `marketRestricted`, `noLegsSpecified`, `accountNotFound`, `mixedCurrencyPairs`, `tooManyNonOptionLegs`, `noOptionLegs`, `tooManyOpenRfqs`, `tooManyLegs`, `expiryTooShort`]

RFQ feature is not enabled.

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

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L -X POST 'https://demo-futures.kraken.com/derivatives/api/v3/rfqs/open-rfqs' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://demo-futures.kraken.com/derivatives/api/v3

Auth

general-api-key

authent

Parameters

json — queryrequired