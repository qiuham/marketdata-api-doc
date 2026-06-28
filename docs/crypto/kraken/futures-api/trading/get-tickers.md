---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-tickers
api_type: REST
updated_at: 2026-05-27 19:51:30.103701
---

# Get tickers

**GET** `https://futures.kraken.com/derivatives/api/v3/tickers`

This endpoint returns current market data for all currently listed Futures contracts and indices.

## Request

### Query Parameters

**contractType** string[]

**Possible values:** [`futures_inverse`, `futures_vanilla`, `flexible_futures`, `options`, `all`]

Contract type(s) to return statuses for.

By default, includes all futures instrument types.

Multi-value example: `?contractType=futures_inverse&contractType=futures_vanilla`

**symbol** `MarketSymbol[]`

**Possible values:** Value must match regular expression `[A-Z0-9_.]+`

Market symbol(s) to filter tickers by.

Symbols are case-insensitive. Multi-value example: `?symbol=PF_BTCUSD&symbol=pf_ethusd`

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**tickers** `object[]` *required*

A list containing a structures for each available instrument. The list is in no particular order.

  * Array [

oneOf
* Market Ticker
* Index Ticker

    ↳ **symbol** `MarketSymbol (string)` *required*

Market symbol

**Possible values:** Value must match regular expression `[A-Z0-9_.]+`

**Example:**`PF_BTCUSD`

    ↳ **last** `number<double>`

The price of the last fill.

**Example:**`12.03532`

**lastTime** string

The date and time at which `last` was observed.

**lastSize** number

The size of the last fill.

    ↳ **tag** `string` *required*

Expiry-related grouping.

Currently can be 'perpetual', 'month', 'quarter', or 'semiannual'. Other tags may be added without notice.

**Possible values:** [`perpetual`, `month`, `quarter`, `semiannual`]

    ↳ **pair** `string` *required*

The currency pair of the instrument.

**Example:**`BTC:USD`

**markPrice** numberrequired

The price to which Kraken Futures currently marks the Futures for margining purposes.

    ↳ **bid** `number`

The price of the current best bid.

**bidSize** number

The size of the current best bid.

    ↳ **ask** `number`

The price of the current best ask.

**askSize** number

The size of the current best ask.

**vol24h** numberrequired

The sum of the sizes of all fills observed in the last 24 hours.

**volumeQuote** numberrequired

The sum of the `size * price` of all fills observed in the last 24 hours.

**openInterest** numberrequired

The current open interest of the market.

**open24h** number

The price of the fill observed 24 hours ago.

**high24h** number

The highest fill price observed in the last 24 hours.

**low24h** number

The lowest fill price observed in the last 24 hours.

**extrinsicValue** number

The mark price less the how much the option would be worth if exercised now, i.e.:
* For a call: `markPrice - ( max ( Underlying - StrikePrice , 0) )`
* For a put: `markPrice - ( max ( StrikePrice - Underlying , 0) )`

Only returned for options markets.

**fundingRate** number

The current absolute funding rate.

Only returned for perpetual markets.

**fundingRatePrediction** number

The estimated next absolute funding rate.

Only returned for perpetual markets.

    ↳ **suspended** `boolean` *required*

True if the market is suspended.

**indexPrice** numberrequired

**postOnly** booleanrequired

**change24h** numberrequired

The 24h change in price (%).

    ↳ **greeks** `object`

Current greeks.

Only returned for options markets.

Note: This is currently available exclusively in the Kraken pre-prod environments.

        ↳ **iv** `number<double>` *required*

The implied volatility. Displays an IV of -1.0 whenever the IV is impossible to calculate or outside of the bounds allowed.

        ↳ **delta** `number<double>` *required*

        ↳ **gamma** `number,null<double>nullable` *required*

        ↳ **vega** `number,null<double>nullable` *required*

        ↳ **theta** `number,null<double>nullable` *required*

        ↳ **rho** `number,null<double>nullable` *required*

**isUnderlyingMarketClosed** boolean

True if the underlying market/index is closed.

Only returned for tradfi markets.

        ↳ **symbol** `string` *required*

The symbol of the index.

**Example:**`rr_ethusd`

        ↳ **last** `number`

The last calculated value.

**lastTime** string<date-time>

The date and time at which `last` was observed.

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
      "tickers": [  
        {  
          "tag": "perpetual",  
          "pair": "XBT:USD",  
          "symbol": "PI_XBTUSD",  
          "markPrice": 30209.9,  
          "bid": 8634,  
          "bidSize": 1000,  
          "ask": 49289,  
          "askSize": 139984,  
          "vol24h": 15304,  
          "volumeQuote": 7305.2,  
          "openInterest": 149655,  
          "open24h": 49289,  
          "indexPrice": 21087.8,  
          "last": 49289,  
          "lastTime": "2022-06-17T10:46:35.705Z",  
          "lastSize": 100,  
          "suspended": false,  
          "fundingRate": 1.18588737106e-7,  
          "fundingRatePrediction": 1.1852486794e-7,  
          "postOnly": false,  
          "change24h": 1.9974017538161748  
        },  
        {  
          "tag": "month",  
          "pair": "XBT:USD",  
          "symbol": "FI_XBTUSD_211231",  
          "markPrice": 20478.5,  
          "bid": 28002,  
          "bidSize": 900,  
          "vol24h": 100,  
          "volumeQuote": 843.9,  
          "openInterest": 10087,  
          "open24h": 28002,  
          "indexPrice": 21087.8,  
          "last": 28002,  
          "lastTime": "2022-06-17T10:45:57.177Z",  
          "lastSize": 100,  
          "suspended": false,  
          "postOnly": false,  
          "change24h": 1.9974017538161748  
        },  
        {  
          "symbol": "in_xbtusd",  
          "last": 21088,  
          "lastTime": "2022-06-17T11:00:30.000Z"  
        },  
        {  
          "symbol": "rr_xbtusd",  
          "last": 20938,  
          "lastTime": "2022-06-16T15:00:00.000Z"  
        }  
      ],  
      "serverTime": "2022-06-17T11:00:31.335Z"  
    }  
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/tickers' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Parameters

contractType — query

futures_inversefutures_vanillaflexible_futuresoptionsall

symbol — query

ResponseClear

Click the `Send API Request` button above and see the response here!