---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/get-open-orders
api_type: REST
updated_at: 2026-05-27 19:49:56.077181
---

# Get open orders

**GET** `https://futures.kraken.com/derivatives/api/v3/openorders`

This endpoint returns information on all open orders for all Futures contracts.

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**openOrders** object[]required

A list containing structures with information on open orders. The list is sorted descending by receivedTime.

  * Array [

**order_id** `string<uuid>` *required*

The unique identifier of the order.

**cliOrdId** string

The unique client order identifier. This field is returned only if the order has a client order ID.

**status** `string` *required*

The status of the order:
* `untouched` \- the entire size of the order is unfilled
* `partiallyFilled` \- the size of the order is partially but not entirely filled

**Possible values:** [`untouched`, `partiallyFilled`]

**side** `string` *required*

The direction of the order.

**Possible values:** [`buy`, `sell`]

**orderType** stringrequired

The order type:
* `lmt` \- limit order
* `stp` \- stop order
* `take_profit` \- take profit order

**Possible values:** [`lmt`, `stop`, `take_profit`]

**symbol** `string` *required*

The symbol of the futures to which the order refers.

**limitPrice** number

The limit price associated with the order.

**stopPrice** number

If orderType is `stp`: The stop price associated with the order

If orderType is `lmt`: Not returned because N/A

**filledSize** numberrequired

The filled size associated with the order.

**unfilledSize** number

The unfilled size associated with the order.

**reduceOnly** booleanrequired

Is the order a reduce only order or not.

**triggerSignal** string

The trigger signal for the stop or take profit order.

**Possible values:** [`mark`, `last`, `spot`]

**lastUpdateTime** string<date-time>required

The date and time the order was 
**receivedTime** string<date-time>required

The date and time the order was received.

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
      "openOrders": [  
        {  
          "order_id": "59302619-41d2-4f0b-941f-7e7914760ad3",  
          "symbol": "PI_XBTUSD",  
          "side": "sell",  
          "orderType": "lmt",  
          "limitPrice": 10640,  
          "unfilledSize": 304,  
          "receivedTime": "2019-09-05T17:01:17.410Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": true,  
          "lastUpdateTime": "2019-09-05T17:01:17.410Z"  
        },  
        {  
          "order_id": "022774bc-2c4a-4f26-9317-436c8d85746d",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "orderType": "lmt",  
          "limitPrice": 7200,  
          "unfilledSize": 1501,  
          "receivedTime": "2019-09-05T16:41:35.173Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": false,  
          "lastUpdateTime": "2019-09-05T16:47:47.519Z"  
        },  
        {  
          "order_id": "d08021f7-58cb-4f2c-9c86-da4c60de46bb",  
          "symbol": "PI_XBTUSD",  
          "side": "sell",  
          "orderType": "lmt",  
          "limitPrice": 10640,  
          "unfilledSize": 10000,  
          "receivedTime": "2019-09-05T16:38:43.651Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": true,  
          "lastUpdateTime": "2019-09-05T16:38:43.651Z"  
        },  
        {  
          "order_id": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "orderType": "lmt",  
          "limitPrice": 9400,  
          "unfilledSize": 10000,  
          "receivedTime": "2019-09-05T16:33:50.734Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": false,  
          "lastUpdateTime": "2019-09-05T16:33:50.734Z"  
        },  
        {  
          "order_id": "9c2cbcc8-14f6-42fe-a020-6e395babafd1",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "orderType": "lmt",  
          "limitPrice": 9400,  
          "unfilledSize": 1000,  
          "receivedTime": "2019-09-04T11:45:48.884Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": false,  
          "lastUpdateTime": "2019-09-05T16:41:40.996Z"  
        },  
        {  
          "order_id": "3deea5c8-0274-4d33-988c-9e5a3895ccf8",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "orderType": "lmt",  
          "limitPrice": 8500,  
          "unfilledSize": 102,  
          "receivedTime": "2019-09-03T12:52:17.945Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": false,  
          "lastUpdateTime": "2019-09-03T12:52:17.945Z"  
        },  
        {  
          "order_id": "fcbb1459-6ed2-4b3c-a58c-67c4df7412cf",  
          "symbol": "PI_XBTUSD",  
          "side": "buy",  
          "orderType": "lmt",  
          "limitPrice": 7200,  
          "unfilledSize": 1501,  
          "receivedTime": "2019-09-02T12:54:34.347Z",  
          "status": "untouched",  
          "filledSize": 0,  
          "reduceOnly": false,  
          "lastUpdateTime": "2019-09-02T12:54:34.347Z"  
        }  
      ],  
      "serverTime": "2019-09-05T17:08:18.138Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/derivatives/api/v3/openorders' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/derivatives/api/v3

Auth

general-api-key-read-only

authent