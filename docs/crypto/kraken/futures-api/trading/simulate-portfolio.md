---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/simulate-portfolio
api_type: REST
updated_at: 2026-05-27 19:53:54.539881
---

# Calculate portfolio margin, pnl and greeks

**POST** `https://demo-futures.kraken.com/derivatives/api/v3/portfolio-margining/simulate`

For a given portfolio of balances and positions (futures and options), calculate the margin requirements, pnl and option greeks.

Note: This is currently available exclusively in the Kraken pre-prod environments.

## Request

### Query Parameters

**json** `any` *required*

Request body as a JSON string

## Responses

  * 200

Simulated portfolio calculations

  * application/json
* Schema

**Schema**

oneOf
* Success Response
* ErrorResponse

**maintenanceMargin** number<double>required

**initialMargin** number<double>required

**pnl** `number<double>` *required*

**portfolioMarginBreakdown** objectrequired

Breakdown of components that make up the portfolio margin calculation.

**totalCrossAssetNettedMarketRisk** number<double>required

**totalMarketRisk** number<double>required

**totalScenarioPnls** number<double>[]

**totalAbsoluteOptionPositionDeltaNotional** number<double>required

**netPortfolioDelta** number<double>required

**totalPremium** number<double>required

**isBuyOnly** booleanrequired

**futuresMaintenanceMargin** number<double>required

**greeks** `object` *required*

**property name*** OptionGreeks

Option Greeks

    ↳ **iv** `number<double>` *required*

The implied volatility. Displays an IV of -1.0 whenever the IV is impossible to calculate or outside of the bounds allowed.

    ↳ **delta** `number<double>` *required*

    ↳ **gamma** `number,null<double>nullable` *required*

    ↳ **vega** `number,null<double>nullable` *required*

    ↳ **theta** `number,null<double>nullable` *required*

    ↳ **rho** `number,null<double>nullable` *required*

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

    
    
    curl -L -X POST 'https://demo-futures.kraken.com/derivatives/api/v3/portfolio-margining/simulate' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://demo-futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent

Parameters

json — queryrequired