---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-trading-instruments
api_type: REST
updated_at: 2026-05-27 19:51:37.366344
---

# Get trading instruments

**GET** `https://futures.kraken.com/derivatives/api/v3/trading/instruments`

Returns specifications for all currently accessible markets and indices.

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

**instruments** `object[]` *required*

A list containing structures for each available instrument. The list is in no particular order.

  * Array [

**fundingRateCoefficient** number<double>

Funding rate coefficient.

Only present for perpetual markets.

**Example:**`12.03532`

**lastTradingTime** string<date-time>

Market expiry date-time (UTC).

Only present for fixed maturity markets.

**minimumTradeSize** number<double>required

TODO: Not populated for any markets (at time of writing in Apr 2025).

**Example:**`12.03532`

**impactMidSize** number<double>required

Book depth used to calculate (impact) mid prices.

**Example:**`12.03532`

**maxPositionSize** number<double>required

Market-wide position size limit.

**Example:**`12.03532`

**openingDate** string<date-time>required

Date-time (UTC) that market was created.

**marginLevels** object[]

Margin schedule applicable to logged-in account.

Only present for futures markets.

  * Array [

    ↳ **contracts** `integer<uint64>`

Position size/level to apply IM/MM rules within a single-collateral margin schedule.

**numNonContractUnits** number<double>

Position size/level to apply IM/MM rules within a multi-collateral margin schedule.

**Possible values:** `>= 0`

**Example:**`12.03532`

**initialMargin** number<double>required

Initial margin (IM) rate.

**Possible values:** `>= 0`

**Example:**`12.03532`

**maintenanceMargin** number<double>required

Maintenance margin (MM) rate.

**Possible values:** `>= 0`

**Example:**`12.03532`

  * ]

**maxRelativeFundingRate** number<double>

Maximum relative funding rate.

Only present for perpetual markets.

**Example:**`12.03532`

    ↳ **symbol** `MarketSymbol (string)` *required*

Market symbol

**Possible values:** Value must match regular expression `[A-Z0-9_.]+`

**Example:**`PF_BTCUSD`

    ↳ **pair** `string` *required*

Asset pair (uppercase, colon separated).

**Example:**`BTC:USD`

    ↳ **base** `string` *required*

Base asset (uppercase).

**Example:**`BTC`

    ↳ **quote** `string` *required*

Quote asset (uppercase).

**Example:**`USD`

**tickSize** number<double>required

Minimum order price increment.

**Example:**`12.03532`

    ↳ **type** `string` *required*

Market type.

**Possible values:** [`futures_inverse`, `futures_vanilla`, `flexible_futures`, `options`]

    ↳ **underlying** `string`

Underlying index code.

Only present for single-collateral markets.

    ↳ **isin** `string | nullnullable` *required*

International Securities Identification Number (ISIN).

**contractValueTradePrecision** integerrequired

Minimum order quantity increment.

E.g., a trade precision of 2 means order quantities are not allowed to be more precise than the hundredth decimal place (0.01).

These values can be negative to specify quantity increments of 10 (-1), 100 (-2), etc.

**postOnly** booleanrequired

True if market is in post-only mode.

**feeScheduleUid** string<uuid>requireddeprecated

**DEPRECATED** — Effective 2026-06-22, this field no longer corresponds to the fee schedule used for fee calculation. Use the Spot [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume) endpoint authenticated with a Spot API key to determine your fee rate.

Fee schedule UID.

**optionType** string

Option type.

Only present for options markets.

**Possible values:** [`call`, `put`]

**strikePrice** number<double>

Strike price.

Only present for options markets.

**Example:**`12.03532`

**underlyingFuture** string

Underlying futures market.

Only present for options markets.

**rebateLevels** objectrequired

Maps market share percentage levels to rebate percentages.

Keys and values are decimal strings.

**property name*** number<double>

**Example:**`12.03532`

    ↳ **mtf** `boolean` *required*

True if this market is provided under the MTF license.

    ↳ **tradfi** `boolean` *required*

True if this is a non-crypto market.

    ↳ **restricted** `boolean` *required*

True if the account is restricted (to position-reducing orders) on this market.

**isExpired** booleanrequired

True if the instrument has expired

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

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/trading/instruments' \  
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

contractType — query

futures_inversefutures_vanillaflexible_futuresoptionsall