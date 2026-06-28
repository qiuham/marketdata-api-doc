---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-closed-rfq-offers
api_type: REST
updated_at: 2026-05-27 19:49:05.462994
---

# List offers placed by the account on closed RFQs

**GET** `https://demo-futures.kraken.com/derivatives/api/v3/rfqs/closed-offers`

Retrieve all offers the account placed on RFQs that have since closed. The `status` field on each offer indicates how the parent RFQ closed (`expired`, `cancelled`, `filled_bid_side`, or `filled_ask_side`).

Closed RFQs are tracked in an in-memory cache only and are not persisted; offers may be evicted by the cache eviction policy or wiped on service restart.

Note: This is currently available exclusively in the Kraken pre-prod environments.

## Responses

  * 200
  * 404

Closed Offers

  * application/json
* Schema

**Schema**

**result** `string` *required*

**Possible values:** [`success`]

**serverTime** string<date-time>required

**offers** `object[]` *required*

  * Array [

    ↳ **uid** `string<uuid>` *required*

Unique identifier for the offer

**rfqUid** string<uuid>required

Unique identifier for the RFQ

**placementDate** string<date-time>required

The date and time when the offer was placed

**lastUpdateDate** string<date-time>required

The last update date and time of the offer

    ↳ **bid** `string<decimal>`

The bid price, if available

    ↳ **ask** `string<decimal>`

The ask price, if available

**bidSide** object[]

Per-leg bid pricing. Null when using package-level pricing.

  * Array [

    ↳ **tradeable** `string` *required*

The symbol of the derivatives contract

    ↳ **price** `number<double>` *required*

The price for this leg

  * ]

**askSide** object[]

Per-leg ask pricing. Null when using package-level pricing.

  * Array [

    ↳ **tradeable** `string` *required*

The symbol of the derivatives contract

    ↳ **price** `number<double>` *required*

The price for this leg

  * ]

    ↳ **status** `string` *required*

Lifecycle status of the parent RFQ at the time this offer is being read. `open` is returned from the `/open-offers` endpoint. The other values are returned from `/closed-offers`.

**Possible values:** [`open`, `expired`, `cancelled`, `filled_bid_side`, `filled_ask_side`]

  * ]

RFQ feature is not enabled.

  * application/json
* Schema

**Schema**

    ↳ **errors** `Error (string)[]`

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
  * php
* CURL

    
    
    curl -L 'https://demo-futures.kraken.com/derivatives/api/v3/rfqs/closed-offers' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://demo-futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent