---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-open-positions
api_type: REST
updated_at: 2026-05-27 19:50:03.303847
---

# Get open positions

**GET** `https://futures.kraken.com/derivatives/api/v3/openpositions`

This endpoint returns the size and average entry price of all open positions in Futures contracts. This includes Futures contracts that have matured but have not yet been settled.

## Responses

  * 200
* application/json
* Schema
  * success
  * failure

**Schema**

oneOf
* Success Response
* ErrorResponse

**openPositions** object[]required

A list containing structures with information on open positions.

The list is sorted descending by fillTime.

  * Array [

**symbol** `string` *required*

The symbol of the Futures.

**side** `string` *required*

The direction of the position.

**Possible values:** [`long`, `short`]

**size** `number<double>` *required*

The size of the position.

**price** `number<double>` *required*

The average price at which the position was entered into.

**unrealizedPnl** number<double>required

Unrealised profit and loss on the position.

**unrealizedFunding** number,null<double>nullablerequired

Unrealised funding on the position.

**pnlCurrency** string | nullnullable

Selected pnl currency for the position (default: USD)

**Possible values:** [`USD`, `EUR`, `GBP`, `USDC`, `USDT`, `BTC`, `ETH`]

**maxFixedLeverage** number,null<double>nullable

Max leverage selected for isolated position.

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
      "openPositions": [  
        {  
          "side": "short",  
          "symbol": "PI_XBTUSD",  
          "price": 9392.749993345933,  
          "size": 10000,  
          "unrealizedPnl": -607250.006654067,  
          "unrealizedFunding": 0.00001045432180096817  
        },  
        {  
          "side": "long",  
          "symbol": "FI_XBTUSD_201225",  
          "price": 9399.749966754434,  
          "size": 20000,  
          "unrealizedPnl": 1199500.664911316  
        },  
        {  
          "side": "long",  
          "symbol": "PF_DEFIUSD",  
          "price": 570,  
          "size": 1,  
          "unrealizedPnl": 12.34,  
          "unrealizedFunding": -0.0073428045972263895,  
          "pnlCurrency": "BTC",  
          "maxFixedLeverage": 5  
        }  
      ],  
      "serverTime": "2020-07-22T14:39:12.376Z"  
    }  
    
    
    
    {  
      "result": "error",  
      "serverTime": "2016-02-25T09:45:53.818Z",  
      "error": "apiLimitExceeded"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/openpositions' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent