---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/trading/send-order
api_type: REST
updated_at: 2026-05-27 19:53:25.444233
---

# Send order

**POST** `https://futures.kraken.com/derivatives/api/v3/sendorder`

This endpoint allows sending a limit, stop, take profit or immediate-or-cancel order for a currently listed Futures contract.

## Request

### Query Parameters

**processBefore** date-time

The time before which the request should be processed, otherwise it is rejected.

**Example:** 2023-11-08T19:56:35.441899Z

**orderType** OrderTyperequired

**Possible values:** [`lmt`, `post`, `ioc`, `mkt`, `stp`, `take_profit`, `trailing_stop`, `fok`]

The order type:
* `lmt` \- a limit order
* `post` \- a post-only limit order
* `mkt` \- an immediate-or-cancel order with 1% price protection
* `stp` \- a stop order
* `take_profit` \- a take profit order
* `ioc` \- an immediate-or-cancel order
* `trailing_stop` \- a trailing stop order
* `fok` \- fill or kill order

**symbol** `string` *required*

The symbol of the Futures

**side** `OrderDirection` *required*

**Possible values:** [`buy`, `sell`]

The direction of the order.

**size** `number` *required*

The size associated with the order. Note that different Futures have different contract sizes.

**limitPrice** number

The limit price associated with the order. Note that for stop orders, limitPrice denotes the worst price at which the `stp` or `take_profit` order can get filled at. If no `limitPrice` is provided the `stp` or `take_profit` order will trigger a market order. If placing a `trailing_stop` order then leave undefined.

**stopPrice** number

The stop price associated with a stop or take profit order.

Required if orderType is `stp` or `take_profit`, but if placing a `trailing_stop` then leave undefined. Note that for stop orders, limitPrice denotes the worst price at which the `stp` or `take_profit` order can get filled at. If no `limitPrice` is provided the `stp` or `take_profit` order will trigger a market order.

**cliOrdId** string

**Possible values:** `<= 100 characters`

The order identity that is specified from the user. It must be globally unique.

**triggerSignal** string

**Possible values:** [`mark`, `index`, `last`]

If placing a `stp`, `take_profit` or `trailing_stop`, the signal used for trigger.
* `mark` \- the mark price
* `index` \- the index price
* `last` \- the last executed trade

**reduceOnly** boolean

Set as true if you wish the order to only reduce an existing position.

Any order which increases an existing position will be rejected. Default false.

**trailingStopMaxDeviation** number

**Possible values:** `>= 0.1` and `<= 50`

Required if the order type is `trailing_stop`. Maximum value of 50%, minimum value of 0.1% for 'PERCENT' 'maxDeviationUnit'.

Is the maximum distance the trailing stop's trigger price may trail behind the requested trigger signal. It defines the threshold at which the trigger price updates.

**trailingStopDeviationUnit** string

**Possible values:** [`PERCENT`, `QUOTE_CURRENCY`]

Required if the order type is `trailing_stop`.

This defines how the trailing trigger price is calculated from the requested trigger signal. For example, if the max deviation is set to 10, the unit is 'PERCENT', and the underlying order is a sell, then the trigger price will never be more then 10% below the trigger signal. Similarly, if the deviation is 100, the unit is 'QUOTE_CURRENCY', the underlying order is a sell, and the contract is quoted in USD, then the trigger price will never be more than $100 below the trigger signal.

**limitPriceOffsetValue** number

Can only be set for triggers, e.g. order types `take_profit`, `stop` and `trailing_stop`. If set, `limitPriceOffsetUnit` must be set as well. This defines a relative limit price depending on the trigger `stopPrice`. The price is determined when the trigger is activated by the `triggerSignal`. The offset can be positive or negative, there might be restrictions on the value depending on the `limitPriceOffsetUnit`.

**limitPriceOffsetUnit** string

**Possible values:** [`QUOTE_CURRENCY`, `PERCENT`]

Can only be set together with `limitPriceOffsetValue`. This defines the unit for the relative limit price distance from the trigger's `stopPrice`.

**broker** `iiban`

Valid Broker IIBAN on whose behalf the order is sent. The format must follow the usual IIBAN pattern `XXXX YYYY ZZZZ WWWW` or machine pattern `XXXXYYYYZZZZWWWW`.

Note: This is currently available exclusively in the Kraken pre-prod environments.

## Responses

  * 200
* application/json
* Schema
  * placed
  * rejected
  * executed

**Schema**

oneOf
* Success Response
* ErrorResponse

**sendStatus** objectrequired

A structure containing information on the send order request.

**cliOrdId** string

The unique client order identifier.

This field is returned only if the order has a client order ID.

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

The unique identifier of the order

**receivedTime** string<date-time>

The date and time the order was received.

                    ↳ **status** `string` *required*

The status of the order, either of:
* `placed` \- the order was placed successfully
* `cancelled` \- the order was cancelled successfully
* `invalidOrderType` \- the order was not placed because orderType is invalid
* `invalidSide` \- the order was not placed because side is invalid
* `invalidSize` \- the order was not placed because size is invalid
* `invalidPrice` \- the order was not placed because limitPrice and/or stopPrice are invalid
* `insufficientAvailableFunds` \- the order was not placed because available funds are insufficient
* `selfFill` \- the order was not placed because it would be filled against an existing order belonging to the same account
* `tooManySmallOrders` \- the order was not placed because the number of small open orders would exceed the permissible limit
* `maxPositionViolation` \- Order would cause you to exceed your maximum position in this contract.
* `marketSuspended` \- the order was not placed because the market is suspended
* `marketInactive` \- the order was not placed because the market is inactive
* `clientOrderIdAlreadyExist` \- the specified client id already exist
* `clientOrderIdTooLong` \- the client id is longer than the permissible limit
* `outsidePriceCollar` \- the order would have executed outside of the price collar for its order type
* `postWouldExecute` \- the post-only order would be filled upon placement, thus is cancelled
* `iocWouldNotExecute` \- the immediate-or-cancel order would not execute.
* `wouldCauseLiquidation` \- returned when a new order would fill at a worse price than the mark price, causing the portfolio value to fall below maintenance margin and triggering a liquidation.
* `wouldNotReducePosition` \- the reduce only order would not reduce position.
* `wouldProcessAfterSpecifiedTime` \- order would be processed after the time specified in `processBefore` parameter.

**Possible values:** [`placed`, `partiallyFilled`, `filled`, `cancelled`, `edited`, `marketSuspended`, `marketInactive`, `invalidPrice`, `invalidSize`, `tooManySmallOrders`, `insufficientAvailableFunds`, `wouldCauseLiquidation`, `clientOrderIdAlreadyExist`, `clientOrderIdTooBig`, `maxPositionViolation`, `outsidePriceCollar`, `wouldIncreasePriceDislocation`, `notFound`, `orderForEditNotAStop`, `orderForEditNotFound`, `postWouldExecute`, `iocWouldNotExecute`, `selfFill`, `wouldNotReducePosition`, `marketIsPostOnly`, `tooManyOrders`, `fixedLeverageTooHigh`, `clientOrderIdInvalid`, `cannotEditTriggerPriceOfTrailingStop`, `cannotEditLimitPriceOfTrailingStop`, `wouldProcessAfterSpecifiedTime`]

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
      "sendStatus": {  
        "order_id": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",  
        "status": "placed",  
        "receivedTime": "2019-09-05T16:33:50.734Z",  
        "orderEvents": [  
          {  
            "type": "PLACE",  
            "order": {  
              "orderId": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 10000,  
              "filled": 0,  
              "limitPrice": 9400,  
              "reduceOnly": false,  
              "timestamp": "2019-09-05T16:33:50.734Z",  
              "lastUpdateTimestamp": "2019-09-05T16:33:50.734Z"  
            }  
          }  
        ]  
      },  
      "serverTime": "2019-09-05T16:33:50.734Z"  
    }  
    
    
    
    {  
      "result": "success",  
      "sendStatus": {  
        "order_id": "614a5298-0071-450f-83c6-0617ce8c6bc4",  
        "status": "iocWouldNotExecute",  
        "receivedTime": "2019-09-05T16:32:54.076Z",  
        "orderEvents": [  
          {  
            "type": "REJECT",  
            "uid": "614a5298-0071-450f-83c6-0617ce8c6bc4",  
            "reason": "IOC_WOULD_NOT_EXECUTE",  
            "order": {  
              "orderId": "614a5298-0071-450f-83c6-0617ce8c6bc4",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 10000,  
              "filled": 0,  
              "limitPrice": 9400,  
              "reduceOnly": true,  
              "timestamp": "2019-09-05T16:32:54.076Z",  
              "lastUpdateTimestamp": "2019-09-05T16:32:54.076Z"  
            }  
          }  
        ]  
      },  
      "serverTime": "2019-09-05T16:32:54.077Z"  
    }  
    
    
    
    {  
      "result": "success",  
      "sendStatus": {  
        "order_id": "61ca5732-3478-42fe-8362-abbfd9465294",  
        "status": "placed",  
        "receivedTime": "2019-12-11T17:17:33.888Z",  
        "orderEvents": [  
          {  
            "type": "EXECUTION",  
            "executionId": "e1ec9f63-2338-4c44-b40a-43486c6732d7",  
            "price": 7244.5,  
            "amount": 10,  
            "orderPriorExecution": {  
              "orderId": "61ca5732-3478-42fe-8362-abbfd9465294",  
              "type": "lmt",  
              "symbol": "PI_XBTUSD",  
              "side": "buy",  
              "quantity": 10,  
              "filled": 0,  
              "limitPrice": 7500,  
              "reduceOnly": false,  
              "timestamp": "2019-12-11T17:17:33.888Z",  
              "lastUpdateTimestamp": "2019-12-11T17:17:33.888Z"  
            }  
          }  
        ]  
      },  
      "serverTime": "2019-12-11T17:17:33.888Z"  
    }  
    

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** General API key with **full** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/trading/kraken-futures-trading-api#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L -X POST 'https://futures.kraken.com/derivatives/api/v3/sendorder' \  
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

orderType — queryrequired

\---lmtpostiocmktstptake_profittrailing_stopfok

symbol — queryrequired

side — queryrequired

\---buysell

size — queryrequired

processBefore — query

limitPrice — query

stopPrice — query

cliOrdId — query

triggerSignal — query

\---markindexlast

reduceOnly — query

\---truefalse

trailingStopMaxDeviation — query

trailingStopDeviationUnit — query

\---PERCENTQUOTE_CURRENCY

limitPriceOffsetValue — query

limitPriceOffsetUnit — query

\---QUOTE_CURRENCYPERCENT

broker — query