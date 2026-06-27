---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/cancel-all-orders
api_type: REST
updated_at: 2026-05-27 19:47:32.139368
---

# Cancel all orders

**POST** `https://futures.kraken.com/derivatives/api/v3/cancelallorders`

This endpoint allows cancelling orders which are associated with a future's contract or a margin account. If no arguments are specified all open orders will be cancelled.

## Request

### Query Parameters

**symbol** `string`

A futures product to cancel all open orders.

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**cancelStatus** objectrequired

A structure containing information on the cancellation request.

**cancelOnly** stringrequired

The symbol of the futures or all.

**cancelledOrders** object[]required

A list of structures containing all the successfully cancelled orders.

  * Array [

**cliOrdId** string | nullnullable

Unique client order identifier.

**Possible values:** `<= 100 characters`

**order_id** `string<uuid>` *required*

Order ID.

  * ]

**orderEvents** object[]required

  * Array [

**type** `string` *required*

Always `CANCEL`.

**Possible values:** [`CANCEL`]

**uid** `string` *required*

The UID associated with the order.

**order** `object` *required*

oneOf
* OrderJson
* MOD2

**orderId** stringrequired

The UID associated with the order.

**cliOrdId** string | nullnullablerequired

The client order id or null if order does not have one.

    ↳ **type** `string` *required*

The order type

**Possible values:** [`lmt`, `ioc`, `post`, `liquidation`, `assignment`, `stp`, `unwind`, `block`, `fok`]

    ↳ **symbol** `string` *required*

The symbol of the Futures.

    ↳ **side** `string` *required*

The side associated with the order

**Possible values:** [`buy`, `sell`]

    ↳ **quantity** `number` *required*

The quantity (size) associated with the order.

    ↳ **filled** `number` *required*

The total amount of the order that has been filled.

**limitPrice** numberrequired

The limit price associated with a limit order.

**reduceOnly** booleanrequired

Is the order a reduce only order or not.

    ↳ **timestamp** `string` *required*

The date and time the order was placed.

**lastUpdateTimestamp** stringrequired

The date and time the order was edited.

  * ]

**receivedTime** stringrequired

The date and time the order cancellation was received.

    ↳ **status** `string` *required*

The status of the order cancellation:
* `cancelled` \- successful cancellation
* `noOrdersToCancel` \- no open orders for cancellation

**Possible values:** [`noOrdersToCancel`, `cancelled`]

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
      "cancelStatus": {  
        "receivedTime": "2019-08-01T15:57:37.518Z",  
        "cancelOnly": "all",  
        "status": "cancelled",  
        "cancelledOrders": [  
          {  
            "order_id": "6180adfa-e4b1-4a52-adac-ea5417620dbd"  
          },  
          {  
            "order_id": "89e3edbe-d739-4c52-b866-6f5a8407ff6e"  
          },  
          {  
            "order_id": "0cd37a77-1644-4960-a7fb-9a1f6e0e46f7"  
          }  
        ],  
        "orderEvents": [  
          {  
            "type": "CANCEL",  
            "uid": "89e3edbe-d739-4c52-b866-6f5a8407ff6e",  
            "order": {  
              "orderId": "89e3edbe-d739-4c52-b866-6f5a8407ff6e",  
              "type": "post",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 890,  
              "filled": 0,  
              "limitPrice": 10040,  
              "reduceOnly": false,  
              "timestamp": "2019-08-01T15:57:08.508Z",  
              "lastUpdateTimestamp": "2019-08-01T15:57:08.508Z"  
            }  
          },  
          {  
            "type": "CANCEL",  
            "uid": "0cd37a77-1644-4960-a7fb-9a1f6e0e46f7",  
            "order": {  
              "orderId": "0cd37a77-1644-4960-a7fb-9a1f6e0e46f7",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "sell",  
              "quantity": 900,  
              "filled": 0,  
              "limitPrice": 10145,  
              "reduceOnly": true,  
              "timestamp": "2019-08-01T15:57:14.003Z",  
              "lastUpdateTimestamp": "2019-08-01T15:57:14.003Z"  
            }  
          }  
        ]  
      },  
      "serverTime": "2019-08-01T15:57:37.520Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/cancelallorders' \  
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

symbol — query