---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-open-rfqs
api_type: REST
updated_at: 2026-05-27 19:50:17.820074
---

# List all open RFQs

**GET** `https://demo-futures.kraken.com/derivatives/api/v3/rfqs`

Retrieve all currently open RFQs

Note: This is currently available exclusively in the Kraken pre-prod environments.

## Responses

  * 200
  * 404

All open RFQs

  * application/json
* Schema

**Schema**

**result** `string` *required*

**Possible values:** [`success`]

**serverTime** string<date-time>required

**rfqs** `object[]` *required*

  * Array [

    ↳ **uid** `string<uuid>` *required*

The unique identifier for this RFQ

    ↳ **expiry** `string<date-time>` *required*

The time at which this RFQ expires

**markPrice** number<double>required

The reference price of the RFQ

    ↳ **legs** `object[]` *required*

The positions associated with the RFQ

  * Array [

        ↳ **symbol** `string` *required*

The symbol of the derivatives contract

        ↳ **size** `number<double>` *required*

The size of the position

**markPrice** number<double>required

The current mark price of the market

**bestBid** number<double>

The best per-leg bid price across all offers

**bestAsk** number<double>

The best per-leg ask price across all offers

  * ]

        ↳ **status** `string` *required*

Lifecycle status of the RFQ. `open` means the RFQ is still accepting offers. `expired` and `cancelled` indicate it closed without a trade. `filled_bid_side` and `filled_ask_side` indicate the requestor accepted an offer on the corresponding side.

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
* curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://demo-futures.kraken.com/derivatives/api/v3/rfqs' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://demo-futures.kraken.com/derivatives/api/v3