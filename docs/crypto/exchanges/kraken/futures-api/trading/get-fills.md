---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-fills
api_type: REST
updated_at: 2026-05-27 19:49:19.942980
---

# Get your fills

**GET** `https://futures.kraken.com/derivatives/api/v3/fills`

This endpoint returns information on your filled orders for all futures contracts.

## Request

### Query Parameters

**lastFillTime** string

If not provided, returns the last 100 fills in any futures contract. If provided, returns the 100 entries before lastFillTime.

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**fills** `object[]` *required*

A list containing structures with information on filled orders. The list is sorted descending by `fillTime`.

  * Array [

**cliOrdId** string | nullnullable

The unique client order identifier.

This field is returned only if the order has a client order ID.

**fillTime** stringrequired

The date and time the order was filled.

**Example:**`2021-11-18T02:39:41.826Z`

**fillType** stringrequired

The classification of the fill:
* `maker` \- user has a limit order that gets filled
* `taker` \- the user makes an execution that crosses the spread
* `liquidation` \- execution is result of a liquidation
* `partialLiquidation` \- execution is part of a partial liquidation to gradually reduce a position before full liquidation
* `assignee` \- execution is a result of a counterparty receiving an Assignment in PAS
* `assignor` \- execution is a result of user assigning their position due to failed liquidation

**Possible values:** [`maker`, `taker`, `liquidation`, `partialLiquidation`, `assignor`, `assignee`, `takerAfterEdit`, `unwindBankrupt`, `unwindCounterparty`]

**Example:**`maker`

    ↳ **fill_id** `string<uuid>` *required*

The unique identifier of the fill. Note that several `fill_id` can pertain to one `order_id` (but not vice versa)

    ↳ **order_id** `string<uuid>` *required*

The unique identifier of the order.

    ↳ **price** `number` *required*

The price of the fill.

**Example:**`47000`

    ↳ **side** `string` *required*

The direction of the order.

**Possible values:** [`buy`, `sell`]

**Example:**`buy`

    ↳ **size** `number` *required*

The size of the fill.

**Example:**`10`

    ↳ **symbol** `string` *required*

The symbol of the futures the fill occurred in.

**Example:**`PI_XBTUSD`

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
      "fills": [  
        {  
          "fill_id": "3d57ed09-fbd6-44f1-8e8b-b10e551c5e73",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "order_id": "693af756-055e-47ef-99d5-bcf4c456ebc5",  
          "size": 5490,  
          "price": 9400,  
          "fillTime": "2020-07-22T13:37:27.077Z",  
          "fillType": "maker"  
        },  
        {  
          "fill_id": "56b86ada-73b0-454d-a95a-e29e3e85b349",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "order_id": "3f513c4c-683d-44ab-a73b-d296abbea201",  
          "size": 5000,  
          "price": 9456,  
          "fillTime": "2020-07-21T12:41:52.790Z",  
          "fillType": "taker"  
        }  
      ],  
      "serverTime": "2020-07-22T13:44:24.311Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/fills' \  
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

lastFillTime — query