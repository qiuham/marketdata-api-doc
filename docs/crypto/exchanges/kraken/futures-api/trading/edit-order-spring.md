---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/edit-order-spring
api_type: REST
updated_at: 2026-05-27 19:48:22.754896
---

# Edit order

**POST** `https://futures.kraken.com/derivatives/api/v3/editorder`

This endpoint allows editing an existing order for a currently listed Futures contract.

When editing an order, if the `trailingStopMaxDeviation` and `trailingStopDeviationUnit` parameters are sent unchanged, the system will recalculate a new stop price upon successful order modification.

## Request

### Query Parameters

**processBefore** date-time

The time before which the request should be processed, otherwise it is rejected.

**Example:** 2023-11-08T19:56:35.441899Z

**orderId** string

ID of the order you wish to edit. (Required if CliOrdId is not included)

**cliOrdId** string

The order identity that is specified from the user. It must be globally unique (Required if orderId is not included)

**size** `number`

The size associated with the order

**limitPrice** number

The limit price associated with the order. Must not exceed the tick size of the contract.

**stopPrice** number

The stop price associated with a stop order. Required if old orderType is stp. Must not exceed tick size of the contract. Note that for stp orders, limitPrice is also required and denotes the worst price at which the stp order can get filled.

**trailingStopMaxDeviation** number

**Possible values:** `>= 0.1` and `<= 50`

Only relevant for trailing stop orders. Maximum value of 50%, minimum value of 0.1% for 'PERCENT' 'maxDeviationUnit'.

Is the maximum distance the trailing stop's trigger price may trail behind the requested trigger signal. It defines the threshold at which the trigger price updates.

**trailingStopDeviationUnit** string

**Possible values:** [`PERCENT`, `QUOTE_CURRENCY`]

Only relevant for trailing stop orders.

This defines how the trailing trigger price is calculated from the requested trigger signal. For example, if the max deviation is set to 10, the unit is 'PERCENT', and the underlying order is a sell, then the trigger price will never be more then 10% below the trigger signal. Similarly, if the deviation is 100, the unit is 'QUOTE_CURRENCY', the underlying order is a sell, and the contract is quoted in USD, then the trigger price will never be more than $100 below the trigger signal.

**qtyMode** string

**Possible values:** [`ABSOLUTE`, `RELATIVE`]

Determines how the updated size is interpreted, defaulting to 'RELATIVE'.

'ABSOLUTE' means that the total order size, including past fills, is set to `size`. 'RELATIVE' means that the current open order size is set to `size`.

## Responses

  * 200
* application/json
* Schema
  * success

**Schema**

oneOf
* Success Response
* ErrorResponse

**editStatus** objectrequired

A structure containing information on the send order request

**orderId** string | nullnullable

The unique identifier of the order

**cliOrdId** string | nullnullable

The unique client order identifier.

This field is returned only if the order has a client order ID.

**orderEvents** object[]required

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

**receivedTime** string | nullnullable

The date and time the order was received

                    ↳ **status** `string` *required*

The status of the order, either of:
* `edited` \- The order was edited successfully
* `invalidSize` \- The order was not placed because size is invalid
* `invalidPrice` \- The order was not placed because limitPrice and/or stopPrice are invalid
* `insufficientAvailableFunds` \- The order was not placed because available funds are insufficient
* `selfFill` \- The order was not placed because it would be filled against an existing order belonging to the same account
* `tooManySmallOrders` \- The order was not placed because the number of small open orders would exceed the permissible limit
* `outsidePriceCollar` \- The limit order crosses the spread but is an order of magnitude away from the mark price - fat finger control
* `postWouldExecute` \- The post-only order would be filled upon placement, thus is cancelled
* `wouldNotReducePosition` \- The edit cannot be applied because the reduce only policy is violated. (Only for reduceOnly orders)
* `orderForEditNotFound` \- The requested order for edit has not been found
* `orderForEditNotAStop` \- The supplied stopPrice cannot be applied because order is not a stop order

**Possible values:** [`edited`, `invalidSize`, `invalidPrice`, `insufficientAvailableFunds`, `selfFill`, `tooManySmallOrders`, `outsidePriceCollar`, `postWouldExecute`, `wouldNotReducePosition`, `orderForEditNotFound`, `orderForEditNotAStop`]

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
      "editStatus": {  
        "status": "edited",  
        "orderId": "022774bc-2c4a-4f26-9317-436c8d85746d",  
        "receivedTime": "2019-09-05T16:47:47.521Z",  
        "orderEvents": [  
          {  
            "type": "EDIT",  
            "old": {  
              "orderId": "022774bc-2c4a-4f26-9317-436c8d85746d",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 1000,  
              "filled": 0,  
              "limitPrice": 9400,  
              "reduceOnly": false,  
              "timestamp": "2019-09-05T16:41:35.173Z",  
              "lastUpdateTimestamp": "2019-09-05T16:41:35.173Z"  
            },  
            "new": {  
              "orderId": "022774bc-2c4a-4f26-9317-436c8d85746d",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 1501,  
              "filled": 0,  
              "limitPrice": 7200,  
              "reduceOnly": false,  
              "timestamp": "2019-09-05T16:41:35.173Z",  
              "lastUpdateTimestamp": "2019-09-05T16:47:47.519Z"  
            }  
          }  
        ]  
      },  
      "serverTime": "2019-09-05T16:47:47.521Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/editorder' \  
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

orderId — query

cliOrdId — query

size — query

limitPrice — query

stopPrice — query

trailingStopMaxDeviation — query

trailingStopDeviationUnit — query

\---PERCENTQUOTE_CURRENCY

qtyMode — query

\---ABSOLUTERELATIVE