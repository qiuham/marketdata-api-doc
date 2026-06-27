---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/cancel-order
api_type: REST
updated_at: 2026-05-27 19:47:46.821013
---

# Cancel order

**POST** `https://futures.kraken.com/derivatives/api/v3/cancelorder`

This endpoint allows cancelling an open order for a Futures contract.

## Request

### Query Parameters

**processBefore** date-time

The time before which the request should be processed, otherwise it is rejected.

**Example:** 2023-11-08T19:56:35.441899Z

**order_id** `string`

The unique identifier of the order to be cancelled.

**cliOrdId** string

The client unique identifier of the order to be cancelled.

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

**cliOrdId** string | nullnullable

The client order ID. Shown only if client specified one.

**orderEvents** object[]

  * Array [

oneOf
* PlaceEvent
* CancelEvent
* EditEvent
* RejectEvent
* ExecuteEvent
* PlaceTriggerEvent
* CancelTriggerEvent
* RejectTriggerEvent

**type** `string` *required*

Always `PLACE`.

**Possible values:** [`PLACE`]

**order** `object` *required*

The placed order.

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

**reducedQuantity** number | nullnullablerequired

The amount of quantity that was removed before placement or null if the order is not a reduce only.

    ↳ **type** `string` *required*

Always `CANCEL`.

**Possible values:** [`CANCEL`]

    ↳ **uid** `string` *required*

The UID associated with the order.

    ↳ **order** `object` *required*

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

        ↳ **type** `string` *required*

Always `EDIT`.

**Possible values:** [`EDIT`]

        ↳ **old** `object` *required*

The order before the edit was applied.

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

            ↳ **new** `object` *required*

The order after the edit was applied.

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

**reducedQuantity** number | nullnullablerequired

The amount of quantity that was removed from the edited order or null if the order is not a reduce only.

                ↳ **type** `string` *required*

Always `REJECT`.

**Possible values:** [`REJECT`]

                ↳ **uid** `string` *required*

The UID associated with the order.

                ↳ **order** `object` *required*

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

                    ↳ **reason** `string` *required*

The rejection reason:
* `POST_WOULD_EXECUTE` \- The post-only order would be filled upon placement, thus is cancelled.
* `IOC_WOULD_NOT_EXECUTE` \- The immediate-or-cancel order would not execute.

**Possible values:** [`POST_WOULD_EXECUTE`, `IOC_WOULD_NOT_EXECUTE`]

                    ↳ **type** `string` *required*

Always `EXECUTION`.

**Possible values:** [`EXECUTION`]

**executionId** string<uuid>required

The UID associated with the execution.

                    ↳ **price** `number` *required*

The price of the execution.

                    ↳ **amount** `number` *required*

The executed amount.

**orderPriorEdit** objectrequired

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

**orderPriorExecution** objectrequired

The order before it executes.

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

**takerReducedQuantity** number | nullnullablerequired

The amount of quantity that was removed from the order before execution or null if the order is not a reduce only.

                    ↳ **type** `string` *required*

Always `PLACE`.

**Possible values:** [`PLACE`]

**orderTrigger** objectrequired

                    ↳ **uid** `string` *required*

The UID associated with the order.

**clientId** string | nullnullablerequired

The client order id or null if order does not have one.

                    ↳ **type** `string` *required*

The order type

**Possible values:** [`lmt`, `ioc`, `post`, `liquidation`, `assignment`, `stp`, `unwind`, `fok`]

                    ↳ **symbol** `string` *required*

The symbol of the Futures.

                    ↳ **side** `string` *required*

The side associated with the order

**Possible values:** [`buy`, `sell`]

                    ↳ **quantity** `number | nullnullable` *required*

The quantity (size) associated with the order.

**limitPrice** number | nullnullablerequired

The limit price associated with a limit order.

**triggerPrice** number | nullnullablerequired

**triggerSide** string | nullnullablerequired

**Possible values:** [`trigger_above`, `trigger_below`]

**triggerSignal** string | nullnullablerequired

**Possible values:** [`mark_price`, `last_price`, `spot_price`]

**reduceOnly** booleanrequired

Is the order a reduce only order or not.

                    ↳ **timestamp** `string` *required*

The date and time the order was placed.

**lastUpdateTimestamp** stringrequired

The date and time the order was edited.

**startTime** string | nullnullable

                    ↳ **type** `string` *required*

Always `CANCEL`.

**Possible values:** [`CANCEL`]

                    ↳ **uid** `string` *required*

**orderTrigger** objectrequired

oneOf
* OrderTriggerJson
* MOD2

                    ↳ **uid** `string` *required*

The UID associated with the order.

**clientId** string | nullnullablerequired

The client order id or null if order does not have one.

                    ↳ **type** `string` *required*

The order type

**Possible values:** [`lmt`, `ioc`, `post`, `liquidation`, `assignment`, `stp`, `unwind`, `fok`]

                    ↳ **symbol** `string` *required*

The symbol of the Futures.

                    ↳ **side** `string` *required*

The side associated with the order

**Possible values:** [`buy`, `sell`]

                    ↳ **quantity** `number | nullnullable` *required*

The quantity (size) associated with the order.

**limitPrice** number | nullnullablerequired

The limit price associated with a limit order.

**triggerPrice** number | nullnullablerequired

**triggerSide** string | nullnullablerequired

**Possible values:** [`trigger_above`, `trigger_below`]

**triggerSignal** string | nullnullablerequired

**Possible values:** [`mark_price`, `last_price`, `spot_price`]

**reduceOnly** booleanrequired

Is the order a reduce only order or not.

                    ↳ **timestamp** `string` *required*

The date and time the order was placed.

**lastUpdateTimestamp** stringrequired

The date and time the order was edited.

**startTime** string | nullnullable

                    ↳ **type** `string` *required*

Always `REJECT`.

**Possible values:** [`REJECT`]

                    ↳ **uid** `string` *required*

**orderTrigger** objectrequired

oneOf
* OrderTriggerJson
* MOD2

                    ↳ **uid** `string` *required*

The UID associated with the order.

**clientId** string | nullnullablerequired

The client order id or null if order does not have one.

                    ↳ **type** `string` *required*

The order type

**Possible values:** [`lmt`, `ioc`, `post`, `liquidation`, `assignment`, `stp`, `unwind`, `fok`]

                    ↳ **symbol** `string` *required*

The symbol of the Futures.

                    ↳ **side** `string` *required*

The side associated with the order

**Possible values:** [`buy`, `sell`]

                    ↳ **quantity** `number | nullnullable` *required*

The quantity (size) associated with the order.

**limitPrice** number | nullnullablerequired

The limit price associated with a limit order.

**triggerPrice** number | nullnullablerequired

**triggerSide** string | nullnullablerequired

**Possible values:** [`trigger_above`, `trigger_below`]

**triggerSignal** string | nullnullablerequired

**Possible values:** [`mark_price`, `last_price`, `spot_price`]

**reduceOnly** booleanrequired

Is the order a reduce only order or not.

                    ↳ **timestamp** `string` *required*

The date and time the order was placed.

**lastUpdateTimestamp** stringrequired

The date and time the order was edited.

**startTime** string | nullnullable

                    ↳ **reason** `OrderError (string)` *required*

**Possible values:** [`MARKET_SUSPENDED`, `MARKET_NOT_FOUND`, `INVALID_PRICE`, `INVALID_QUANTITY`, `SMALL_ORDER_LIMIT_EXCEEDED`, `INSUFFICIENT_MARGIN`, `WOULD_CAUSE_LIQUIDATION`, `CLIENT_ORDER_ID_IN_USE`, `CLIENT_ORDER_ID_TOO_LONG`, `MAX_POSITION_EXCEEDED`, `PRICE_COLLAR`, `PRICE_DISLOCATION`, `EDIT_HAS_NO_EFFECT`, `ORDER_FOR_CANCELLATION_NOT_FOUND`, `ORDER_FOR_EDIT_NOT_FOUND`, `ORDER_CANNOT_HAVE_TRIGGER_PRICE`, `POST_WOULD_EXECUTE`, `IOC_WOULD_NOT_EXECUTE`, `WOULD_EXECUTE_SELF`, `WOULD_NOT_REDUCE_POSITION`, `REJECTED_AFTER_EXECUTION`, `MARKET_IS_POST_ONLY`, `ORDER_LIMIT_EXCEEDED`, `FIXED_LEVERAGE_TOO_HIGH`, `CANNOT_EDIT_TRIGGER_PRICE_OF_TRAILING_STOP`, `CANNOT_EDIT_LIMIT_PRICE_OF_TRAILING_STOP`, `TRAILING_STOP_ORDER_LIMIT_EXCEEDED`, `TRAILING_STOP_PERCENT_DEVIATION_EXCEEDS_MAX_DECIMAL_PLACES`, `TRAILING_STOP_QUOTE_DEVIATION_NOT_MULTIPLE_OF_TICK_SIZE`, `TRAILING_STOP_MAX_DEVIATION_TOO_LARGE`, `TRAILING_STOP_MAX_DEVIATION_TOO_SMALL`, `INSUFFICIENT_HEADROOM_AROUND_CURRENT_PRICE_TO_EDIT_TRAILING_STOP`, `NO_REFERENCE_PRICE_AVAILABLE_FOR_CALCULATING_TRAILING_STOP_TRIGGER_PRICE`, `INSUFFICIENT_CLOSING_MARGIN`, `LIMIT_PRICE_SET_AS_ABSOLUTE_AND_RELATIVE`, `LIMIT_PRICE_OFFSET_VALUE_INVALID`, `LIMIT_PRICE_OFFSET_UNIT_INVALID`, `LIMIT_PRICE_OFFSET_MUST_HAVE_VALUE_AND_UNIT`, `LIMIT_PRICE_OFFSET_QUOTE_CURRENCY_VALUE_MUST_BE_MULTIPLE_OF_TICK_SIZE`, `LIMIT_PRICE_OFFSET_PERCENT_VALUE_TOO_MANY_DECIMAL_PLACES`, `LIMIT_PRICE_OFFSET_TOO_HIGH`, `LIMIT_PRICE_OFFSET_TOO_LOW`]

  * ]

                    ↳ **order_id** `string<uuid>`

The cancelled order UID

**receivedTime** string

The date and time the order cancellation was received.

                    ↳ **status** `string` *required*

The status of the order cancellation:
* `cancelled` \- The order has been cancelled. This may only be part of the order as part may have been filled. Check open_orders websocket feed for status of the order.
* `filled` \- The order was found completely filled and could not be cancelled
* `notFound` \- The order was not found, either because it had already been cancelled or it never existed

**Possible values:** [`cancelled`, `filled`, `notFound`]

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
        "status": "cancelled",  
        "order_id": "cb4e34f6-4eb3-4d4b-9724-4c3035b99d47",  
        "receivedTime": "2020-07-22T13:26:20.806Z",  
        "orderEvents": [  
          {  
            "type": "CANCEL",  
            "uid": "cb4e34f6-4eb3-4d4b-9724-4c3035b99d47",  
            "order": {  
              "orderId": "cb4e34f6-4eb3-4d4b-9724-4c3035b99d47",  
              "cliOrdId": "1234568",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 5500,  
              "filled": 0,  
              "limitPrice": 8000,  
              "reduceOnly": false,  
              "timestamp": "2020-07-22T13:25:56.366Z",  
              "lastUpdateTimestamp": "2020-07-22T13:25:56.366Z"  
            }  
          }  
        ]  
      },  
      "serverTime": "2020-07-22T13:26:20.806Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/cancelorder' \  
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

processBefore — query

order_id — query

cliOrdId — query