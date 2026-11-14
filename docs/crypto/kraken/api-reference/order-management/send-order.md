---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/api-reference/order-management/send-order'
updated_at: 2026-11-13
---

# Send order

> This endpoint allows sending a limit, stop, take profit or immediate-or-cancel order for a
currently listed Futures contract.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /sendorder
openapi: 3.1.0
info:
  title: Kraken Futures Trading API
  version: v3
  description: Market data and order management endpoints.
servers:
  - url: https://futures.kraken.com/derivatives/api/v3
    description: Kraken Futures
    x-kfOnly: true
security: []
tags:
  - name: Multi-Collateral
    description: Endpoints pertaining to the multi-collateral (MC) futures markets.
  - name: Instrument Details
    description: >-
      - The `/instruments/status` endpoint provides a list of statuses for all
      instruments.

      - The `/instruments/{symbol}/status` endpoint provides the status of a
      single instrument.
  - name: Account Information
  - name: Assignment Program
  - name: Fee Schedules
    description: >-
      **DEPRECATED** — Effective 2026-06-22, the fee values returned by these

      endpoints no longer reflect the fees actually charged on Futures trades.

      Futures fee calculation has been migrated to a centralised Kraken fee

      service.


      To determine the fee rate applied to your trades, use the Spot

      [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)

      endpoint authenticated with a Spot API key.
  - name: General
  - name: Historical Data
  - name: Historical Funding Rates
  - name: Market Data
  - name: Order Management
  - name: Trading Settings
  - name: Subaccounts
  - name: Transfers
  - name: RFQs
paths:
  /sendorder:
    post:
      tags:
        - Order Management
      summary: Send order
      description: >-
        This endpoint allows sending a limit, stop, take profit or
        immediate-or-cancel order for a

        currently listed Futures contract.
      operationId: sendOrder
      parameters:
        - $ref: '#/components/parameters/AlgoId'
        - $ref: '#/components/parameters/ProcessBefore'
        - $ref: '#/components/parameters/OrderTypeQuery'
        - name: symbol
          in: query
          required: true
          schema:
            type: string
            description: The symbol of the Futures
        - $ref: '#/components/parameters/OrderSideQuery'
        - name: size
          in: query
          required: true
          schema:
            type: number
            description: >-
              The size associated with the order. Note that different Futures
              have different

              contract sizes.
        - name: limitPrice
          in: query
          schema:
            type: number
            description: >-
              The limit price associated with the order. Note that for stop
              orders, limitPrice denotes the worst price at

              which the `stp` or `take_profit` order can get filled at. If no
              `limitPrice` is

              provided the `stp` or `take_profit` order will trigger a market
              order. If placing a `trailing_stop` order then leave undefined.
        - name: stopPrice
          in: query
          schema:
            type: number
            description: >-
              The stop price associated with a stop or take profit order.


              Required if orderType is `stp` or `take_profit`, but if placing a
              `trailing_stop` then

              leave undefined. Note that for stop orders, limitPrice denotes the
              worst price at

              which the `stp` or `take_profit` order can get filled at. If no
              `limitPrice` is

              provided the `stp` or `take_profit` order will trigger a market
              order.
        - name: cliOrdId
          in: query
          schema:
            type: string
            description: >-
              The order identity that is specified from the user. It must be
              globally unique.
            maxLength: 100
        - name: triggerSignal
          in: query
          schema:
            type: string
            enum:
              - mark
              - index
              - last
            description: >-
              If placing a `stp`, `take_profit` or `trailing_stop`, the signal
              used for trigger.


              - `mark` - the mark price

              - `index` - the index price

              - `last` - the last executed trade
        - name: reduceOnly
          in: query
          schema:
            type: boolean
            description: >-
              Set as true if you wish the order to only reduce an existing
              position.


              Any order which increases an existing position will be rejected.
              Default false.
        - name: trailingStopMaxDeviation
          in: query
          schema:
            type: number
            description: >-
              Required if the order type is `trailing_stop`. Maximum value of
              50%, minimum value of 0.1% for 'PERCENT' 'maxDeviationUnit'.


              Is the maximum distance the trailing stop's trigger price may
              trail behind the

              requested trigger signal. It defines the threshold at which the
              trigger price updates.
            minimum: 0.1
            maximum: 50
        - name: trailingStopDeviationUnit
          in: query
          schema:
            type: string
            enum:
              - PERCENT
              - QUOTE_CURRENCY
            description: >-
              Required if the order type is `trailing_stop`.


              This defines how the trailing trigger price is calculated from the
              requested trigger

              signal. For example, if the max deviation is set to 10, the unit
              is 'PERCENT', and the

              underlying order is a sell, then the trigger price will never be
              more then 10% below

              the trigger signal. Similarly, if the deviation is 100, the unit
              is 'QUOTE_CURRENCY',

              the underlying order is a sell, and the contract is quoted in USD,
              then the trigger

              price will never be more than $100 below the trigger signal.
        - name: limitPriceOffsetValue
          in: query
          schema:
            type: number
            description: >-
              Can only be set for triggers, e.g. order types `take_profit`,
              `stop` and `trailing_stop`.

              If set, `limitPriceOffsetUnit` must be set as well.

              This defines a relative limit price depending on the trigger
              `stopPrice`. The price is determined

              when the trigger is activated by the `triggerSignal`. The offset
              can be positive or negative, there

              might be restrictions on the value depending on the
              `limitPriceOffsetUnit`.
        - name: limitPriceOffsetUnit
          in: query
          schema:
            type: string
            enum:
              - QUOTE_CURRENCY
              - PERCENT
            description: >-
              Can only be set together with `limitPriceOffsetValue`.

              This defines the unit for the relative limit price distance from
              the trigger's `stopPrice`.
        - name: broker
          in: query
          schema:
            type: string
            format: iiban
            description: >-
              Valid Broker IIBAN on whose behalf the order is sent. The format
              must follow the

              usual IIBAN pattern `XXXX YYYY ZZZZ WWWW` or machine pattern
              `XXXXYYYYZZZZWWWW`.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success Response
                    allOf:
                      - type: object
                        properties:
                          sendStatus:
                            $ref: '#/components/schemas/SendOrderJson'
                            description: >-
                              A structure containing information on the send
                              order request.
                        required:
                          - sendStatus
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                placed:
                  $ref: '#/components/examples/PlacedOrderExample'
                rejected:
                  $ref: '#/components/examples/RejectedOrderExample'
                executed:
                  $ref: '#/components/examples/ExecutedOrderExample'
        '403':
          $ref: '#/components/responses/ContractAccessForbidden'
      security:
        - general-api-key: []
          authent: []
components:
  parameters:
    AlgoId:
      description: ID of the algorithm that is making the request.
      name: algoId
      in: header
      required: false
      schema:
        type: string
      x-cfOnly: true
    ProcessBefore:
      description: >-
        The time before which the request should be processed, otherwise it is
        rejected.
      name: processBefore
      in: query
      required: false
      schema:
        type: string
        format: date-time
      example: '2023-11-08T19:56:35.441899Z'
    OrderTypeQuery:
      description: |-
        The order type:

        - `lmt` - a limit order
        - `post` - a post-only limit order
        - `mkt` - an immediate-or-cancel order with 1% price protection
        - `stp` - a stop order
        - `take_profit` - a take profit order
        - `ioc` - an immediate-or-cancel order
        - `trailing_stop` - a trailing stop order
        - `fok` - fill or kill order
      name: orderType
      in: query
      required: true
      schema:
        $ref: '#/components/schemas/OrderType'
    OrderSideQuery:
      description: The direction of the order.
      name: side
      in: query
      required: true
      schema:
        $ref: '#/components/schemas/OrderDirection'
  schemas:
    SendOrderJson:
      type: object
      properties:
        cliOrdId:
          type: string
          description: |-
            The unique client order identifier.

            This field is returned only if the order has a client order ID.
        orderEvents:
          type: array
          items:
            $ref: '#/components/schemas/OrderEvent'
        order_id:
          type: string
          format: uuid
          description: The unique identifier of the order
        receivedTime:
          description: The date and time the order was received.
          type: string
          format: date-time
        status:
          type: string
          enum:
            - placed
            - partiallyFilled
            - filled
            - cancelled
            - edited
            - marketSuspended
            - marketInactive
            - invalidPrice
            - invalidSize
            - tooManySmallOrders
            - insufficientAvailableFunds
            - wouldCauseLiquidation
            - clientOrderIdAlreadyExist
            - clientOrderIdTooBig
            - maxPositionViolation
            - outsidePriceCollar
            - wouldIncreasePriceDislocation
            - notFound
            - orderForEditNotAStop
            - orderForEditNotFound
            - postWouldExecute
            - iocWouldNotExecute
            - selfFill
            - wouldNotReducePosition
            - marketIsPostOnly
            - tooManyOrders
            - makerProtectionOrderLimitExceeded
            - fixedLeverageTooHigh
            - clientOrderIdInvalid
            - cannotEditTriggerPriceOfTrailingStop
            - cannotEditLimitPriceOfTrailingStop
            - wouldProcessAfterSpecifiedTime
            - invalidDomainConfiguration
            - editAlreadyHeld
            - marketIsCancelOnly
          description: >-
            The status of the order, either of:


            - `placed` - the order was placed successfully

            - `cancelled` - the order was cancelled successfully

            - `invalidOrderType` - the order was not placed because orderType is
            invalid

            - `invalidSide` - the order was not placed because side is invalid

            - `invalidSize` - the order was not placed because size is invalid

            - `invalidPrice` - the order was not placed because limitPrice
            and/or stopPrice are invalid

            - `insufficientAvailableFunds` - the order was not placed because
            available funds are insufficient

            - `selfFill` - the order was not placed because it would be filled
            against an existing order belonging to the same account

            - `tooManySmallOrders` - the order was not placed because the number
            of small open orders would exceed the permissible limit

            - `maxPositionViolation` - Order would cause you to exceed your
            maximum position in this contract.

            - `marketSuspended` - the order was not placed because the market is
            suspended

            - `marketInactive` - the order was not placed because the market is
            inactive

            - `clientOrderIdAlreadyExist` - the specified client id already
            exist

            - `clientOrderIdTooLong` - the client id is longer than the
            permissible limit

            - `outsidePriceCollar` - the order would have executed outside of
            the price collar for its order type

            - `postWouldExecute` - the post-only order would be filled upon
            placement, thus is cancelled

            - `iocWouldNotExecute` - the immediate-or-cancel order would not
            execute.

            - `wouldCauseLiquidation` - returned when a new order would fill at
            a worse price than the mark price, causing the portfolio value to
            fall below maintenance margin and triggering a liquidation.

            - `wouldNotReducePosition` - the reduce only order would not reduce
            position.

            - `makerProtectionOrderLimitExceeded` - the order was not placed
            because accepting it would exceed the maker protection live-hold
            limit.

            - `wouldProcessAfterSpecifiedTime` - order would be processed after
            the time specified in `processBefore` parameter.

            - `invalidDomainConfiguration` - the order was not placed because
            the account's domain is not configured to permit it.

            - `editAlreadyHeld` - the edit was refused because an earlier edit
            of the order is still held for the market's maker protection window.

            - `marketIsCancelOnly` - the request was refused because the venue
            is in cancel-only mode: only cancellations are accepted until it is
            lifted.
      required:
        - status
    SuccessResponse:
      allOf:
        - $ref: '#/components/schemas/ResultSuccess'
        - $ref: '#/components/schemas/ServerTime'
    ErrorResponse:
      allOf:
        - title: Errors
          type: object
          properties:
            errors:
              type: array
              items:
                $ref: '#/components/schemas/Error'
            error:
              $ref: '#/components/schemas/Error'
          required:
            - error
        - $ref: '#/components/schemas/ResultError'
        - $ref: '#/components/schemas/ServerTime'
    OrderType:
      description: |-
        The order type:

        - `lmt` - a limit order
        - `post` - a post-only limit order
        - `mkt` - an immediate-or-cancel order with 1% price protection
        - `stp` - a stop order
        - `take_profit` - a take profit order
        - `ioc` - an immediate-or-cancel order
        - `trailing_stop` - a trailing stop order
        - `fok` - fill-or-kill order
      type: string
      enum:
        - lmt
        - post
        - ioc
        - mkt
        - stp
        - take_profit
        - trailing_stop
        - fok
    OrderDirection:
      description: The direction of the order.
      type: string
      enum:
        - buy
        - sell
      x-exhaustive: true
    OrderEvent:
      oneOf:
        - $ref: '#/components/schemas/PlaceEvent'
        - $ref: '#/components/schemas/CancelEvent'
        - $ref: '#/components/schemas/EditEvent'
        - $ref: '#/components/schemas/RejectEvent'
        - $ref: '#/components/schemas/ExecuteEvent'
        - $ref: '#/components/schemas/PlaceTriggerEvent'
        - $ref: '#/components/schemas/CancelTriggerEvent'
        - $ref: '#/components/schemas/RejectTriggerEvent'
    ResultSuccess:
      type: object
      properties:
        result:
          type: string
          enum:
            - success
          example: success
      required:
        - result
    ServerTime:
      type: object
      properties:
        serverTime:
          description: Server time in Coordinated Universal Time (UTC)
          type: string
          format: date-time
          example: '2020-08-27T17:03:33.196Z'
      required:
        - serverTime
    Error:
      type: string
      description: |-
        Error description.

          - `accountInactive`: The Futures account the request refers to is inactive
          - `accountNotFound`: The account the transfer request refers to could not be found
          - `apiLimitExceeded`: The API limit for the calling IP address has been exceeded
          - `authenticationError`: The request could not be authenticated
          - `cancelOnly`: The venue is in cancel-only mode and accepts only cancellations until it is lifted
          - `cannotTransferBonusCurrency`: Deprecated and no longer returned, since bonus currency has been removed
          - `cashAccountTypeAccessForbidden`: The account's platform does not give access to the requested wallet
          - `cashAccountTypeNotFound`: The requested wallet does not exist
          - `insufficientFunds`: The amount requested for transfer is below the amount of funds available
          - `invalidAccount`: The Futures account the transfer request refers to is invalid
          - `invalidAmount`: The amount the transfer request refers to is invalid
          - `invalidArgument`: One or more arguments provided are invalid
          - `invalidCurrency`: The currency cannot be transferred between the requested wallets
          - `invalidUnit`: The unit the transfer request refers to is invalid
          - `Json Parse Error`: The request failed to pass valid JSON as an argument
          - `marketUnavailable`: The market is currently unavailable
          - `nonceBelowThreshold`: The provided nonce is below the threshold
          - `nonceDuplicate`: The provided nonce is a duplicate as it has been used in a previous request
          - `notFound`: The requested information could not be found
          - `requiredArgumentMissing`: One or more required arguments are missing
          - `Server Error`: There was an error processing the request
          - `transferFailed`: The transfer was refused for a reason the venue does not disclose
          - `Unavailable`: The endpoint being called is unavailable
          - `unknownError`: An unknown error has occurred
      enum:
        - accountInactive
        - accountNotFound
        - apiLimitExceeded
        - authenticationError
        - cancelOnly
        - cannotTransferBonusCurrency
        - cashAccountTypeAccessForbidden
        - cashAccountTypeNotFound
        - insufficientFunds
        - invalidAccount
        - invalidAmount
        - invalidArgument
        - invalidCurrency
        - invalidUnit
        - Json Parse Error
        - marketUnavailable
        - nonceBelowThreshold
        - nonceDuplicate
        - notFound
        - requiredArgumentMissing
        - Server Error
        - transferFailed
        - Unavailable
        - unknownError
    ResultError:
      type: object
      properties:
        result:
          type: string
          enum:
            - error
          example: error
      required:
        - result
    _schemas_ErrorResponse:
      type: object
      properties:
        result:
          type: string
          enum:
            - error
        serverTime:
          type: string
          format: date-time
        errors:
          type: array
          items:
            $ref: '#/components/schemas/_schemas_Error'
      required:
        - result
        - serverTime
        - errors
    PlaceEvent:
      type: object
      properties:
        type:
          description: Always `PLACE`.
          type: string
          enum:
            - PLACE
        order:
          $ref: '#/components/schemas/OrderJson'
          description: The placed order.
        reducedQuantity:
          type:
            - number
            - 'null'
          description: >-
            The amount of quantity that was removed before placement or null if
            the order is not a

            reduce only.
      required:
        - type
        - order
        - reducedQuantity
    CancelEvent:
      type: object
      properties:
        type:
          description: Always `CANCEL`.
          type: string
          enum:
            - CANCEL
        uid:
          type: string
          description: The UID associated with the order.
        order:
          oneOf:
            - $ref: '#/components/schemas/OrderJson'
              description: The cancelled order.
            - type: 'null'
      required:
        - type
        - uid
        - order
    EditEvent:
      type: object
      properties:
        type:
          description: Always `EDIT`.
          type: string
          enum:
            - EDIT
        old:
          $ref: '#/components/schemas/OrderJson'
          description: The order before the edit was applied.
        new:
          $ref: '#/components/schemas/OrderJson'
          description: The order after the edit was applied.
        reducedQuantity:
          type:
            - number
            - 'null'
          description: >-
            The amount of quantity that was removed from the edited order or
            null if the order is

            not a reduce only.
      required:
        - type
        - old
        - new
        - reducedQuantity
    RejectEvent:
      type: object
      properties:
        type:
          description: Always `REJECT`.
          type: string
          enum:
            - REJECT
        uid:
          type: string
          description: The UID associated with the order.
        order:
          oneOf:
            - $ref: '#/components/schemas/OrderJson'
              description: The rejected order.
            - type: 'null'
        reason:
          type: string
          enum:
            - POST_WOULD_EXECUTE
            - IOC_WOULD_NOT_EXECUTE
          description: >-
            The rejection reason:


            - `POST_WOULD_EXECUTE` - The post-only order would be filled upon
            placement, thus is cancelled.

            - `IOC_WOULD_NOT_EXECUTE` - The immediate-or-cancel order would not
            execute.
          x-codeReference: OrderError.toApiString()
      required:
        - type
        - uid
        - order
        - reason
    ExecuteEvent:
      type: object
      properties:
        type:
          description: Always `EXECUTION`.
          type: string
          enum:
            - EXECUTION
        executionId:
          type: string
          format: uuid
          description: The UID associated with the execution.
        price:
          type: number
          description: The price of the execution.
        amount:
          type: number
          description: The executed amount.
        orderPriorEdit:
          oneOf:
            - $ref: '#/components/schemas/OrderJson'
              description: >-
                The order before the edit was applied (if the execution is a
                result of an order

                edit).
            - type: 'null'
        orderPriorExecution:
          $ref: '#/components/schemas/OrderJson'
          description: The order before it executes.
        takerReducedQuantity:
          type:
            - number
            - 'null'
          description: >-
            The amount of quantity that was removed from the order before
            execution or null if the

            order is not a reduce only.
      required:
        - type
        - executionId
        - price
        - amount
        - orderPriorEdit
        - orderPriorExecution
        - takerReducedQuantity
    PlaceTriggerEvent:
      type: object
      properties:
        type:
          description: Always `PLACE`.
          type: string
          enum:
            - PLACE
        orderTrigger:
          $ref: '#/components/schemas/OrderTriggerJson'
      required:
        - type
        - orderTrigger
    CancelTriggerEvent:
      type: object
      properties:
        type:
          description: Always `CANCEL`.
          type: string
          enum:
            - CANCEL
        uid:
          type: string
        orderTrigger:
          oneOf:
            - $ref: '#/components/schemas/OrderTriggerJson'
            - type: 'null'
      required:
        - type
        - uid
        - orderTrigger
    RejectTriggerEvent:
      type: object
      properties:
        type:
          description: Always `REJECT`.
          type: string
          enum:
            - REJECT
        uid:
          type: string
        orderTrigger:
          oneOf:
            - $ref: '#/components/schemas/OrderTriggerJson'
            - type: 'null'
        reason:
          $ref: '#/components/schemas/OrderError'
      required:
        - type
        - uid
        - orderTrigger
        - reason
    _schemas_Error:
      type: object
      properties:
        code:
          type:
            - number
            - 'null'
        message:
          type: string
      required:
        - code
        - message
    OrderJson:
      type: object
      properties:
        orderId:
          type: string
          description: The UID associated with the order.
        cliOrdId:
          type:
            - string
            - 'null'
          description: The client order id or null if order does not have one.
        type:
          type: string
          enum:
            - lmt
            - ioc
            - post
            - liquidation
            - assignment
            - stp
            - unwind
            - block
            - fok
          description: The order type
        symbol:
          type: string
          description: The symbol of the Futures.
        side:
          type: string
          enum:
            - buy
            - sell
          description: The side associated with the order
        quantity:
          type: number
          description: The quantity (size) associated with the order.
        filled:
          type: number
          description: The total amount of the order that has been filled.
        limitPrice:
          type: number
          description: The limit price associated with a limit order.
        reduceOnly:
          type: boolean
          description: Is the order a reduce only order or not.
        timestamp:
          type: string
          description: The date and time the order was placed.
        lastUpdateTimestamp:
          type: string
          description: The date and time the order was edited.
        algoId:
          type:
            - string
            - 'null'
          x-cfOnly: true
      required:
        - orderId
        - cliOrdId
        - type
        - symbol
        - side
        - quantity
        - filled
        - limitPrice
        - reduceOnly
        - timestamp
        - lastUpdateTimestamp
    OrderTriggerJson:
      type: object
      properties:
        uid:
          type: string
          description: The UID associated with the order.
        clientId:
          type:
            - string
            - 'null'
          description: The client order id or null if order does not have one.
        type:
          type: string
          enum:
            - lmt
            - ioc
            - post
            - liquidation
            - assignment
            - stp
            - unwind
            - fok
          description: The order type
        symbol:
          type: string
          description: The symbol of the Futures.
        side:
          type: string
          enum:
            - buy
            - sell
          description: The side associated with the order
        quantity:
          type:
            - number
            - 'null'
          description: The quantity (size) associated with the order.
        limitPrice:
          type:
            - number
            - 'null'
          description: The limit price associated with a limit order.
        triggerPrice:
          type:
            - number
            - 'null'
        triggerSide:
          type:
            - string
            - 'null'
          enum:
            - trigger_above
            - trigger_below
        triggerSignal:
          type:
            - string
            - 'null'
          enum:
            - mark_price
            - last_price
            - spot_price
        reduceOnly:
          type: boolean
          description: Is the order a reduce only order or not.
        timestamp:
          type: string
          description: The date and time the order was placed.
        lastUpdateTimestamp:
          type: string
          description: The date and time the order was edited.
        startTime:
          type:
            - string
            - 'null'
      required:
        - uid
        - clientId
        - type
        - symbol
        - side
        - quantity
        - limitPrice
        - triggerPrice
        - triggerSide
        - triggerSignal
        - reduceOnly
        - timestamp
        - lastUpdateTimestamp
    OrderError:
      type: string
      enum:
        - MARKET_SUSPENDED
        - MARKET_NOT_FOUND
        - INVALID_PRICE
        - INVALID_QUANTITY
        - SMALL_ORDER_LIMIT_EXCEEDED
        - INSUFFICIENT_MARGIN
        - WOULD_CAUSE_LIQUIDATION
        - CLIENT_ORDER_ID_IN_USE
        - CLIENT_ORDER_ID_TOO_LONG
        - MAX_POSITION_EXCEEDED
        - PRICE_COLLAR
        - PRICE_DISLOCATION
        - EDIT_HAS_NO_EFFECT
        - ORDER_FOR_CANCELLATION_NOT_FOUND
        - ORDER_FOR_EDIT_NOT_FOUND
        - ORDER_CANNOT_HAVE_TRIGGER_PRICE
        - POST_WOULD_EXECUTE
        - IOC_WOULD_NOT_EXECUTE
        - WOULD_EXECUTE_SELF
        - WOULD_NOT_REDUCE_POSITION
        - REJECTED_AFTER_EXECUTION
        - MARKET_IS_POST_ONLY
        - ORDER_LIMIT_EXCEEDED
        - MAKER_PROTECTION_ORDER_LIMIT_EXCEEDED
        - FIXED_LEVERAGE_TOO_HIGH
        - CANNOT_EDIT_TRIGGER_PRICE_OF_TRAILING_STOP
        - CANNOT_EDIT_LIMIT_PRICE_OF_TRAILING_STOP
        - TRAILING_STOP_ORDER_LIMIT_EXCEEDED
        - TRAILING_STOP_PERCENT_DEVIATION_EXCEEDS_MAX_DECIMAL_PLACES
        - TRAILING_STOP_QUOTE_DEVIATION_NOT_MULTIPLE_OF_TICK_SIZE
        - TRAILING_STOP_MAX_DEVIATION_TOO_LARGE
        - TRAILING_STOP_MAX_DEVIATION_TOO_SMALL
        - INSUFFICIENT_HEADROOM_AROUND_CURRENT_PRICE_TO_EDIT_TRAILING_STOP
        - >-
          NO_REFERENCE_PRICE_AVAILABLE_FOR_CALCULATING_TRAILING_STOP_TRIGGER_PRICE
        - INSUFFICIENT_CLOSING_MARGIN
        - LIMIT_PRICE_SET_AS_ABSOLUTE_AND_RELATIVE
        - LIMIT_PRICE_OFFSET_VALUE_INVALID
        - LIMIT_PRICE_OFFSET_UNIT_INVALID
        - LIMIT_PRICE_OFFSET_MUST_HAVE_VALUE_AND_UNIT
        - LIMIT_PRICE_OFFSET_QUOTE_CURRENCY_VALUE_MUST_BE_MULTIPLE_OF_TICK_SIZE
        - LIMIT_PRICE_OFFSET_PERCENT_VALUE_TOO_MANY_DECIMAL_PLACES
        - LIMIT_PRICE_OFFSET_TOO_HIGH
        - LIMIT_PRICE_OFFSET_TOO_LOW
  examples:
    PlacedOrderExample:
      value:
        result: success
        sendStatus:
          order_id: 179f9af8-e45e-469d-b3e9-2fd4675cb7d0
          status: placed
          receivedTime: '2019-09-05T16:33:50.734Z'
          orderEvents:
            - type: PLACE
              order:
                orderId: 179f9af8-e45e-469d-b3e9-2fd4675cb7d0
                cliOrdId: null
                type: lmt
                symbol: PI_XBTUSD
                side: buy
                quantity: 10000
                filled: 0
                limitPrice: 9400
                reduceOnly: false
                timestamp: '2019-09-05T16:33:50.734Z'
                lastUpdateTimestamp: '2019-09-05T16:33:50.734Z'
              reducedQuantity: null
        serverTime: '2019-09-05T16:33:50.734Z'
    RejectedOrderExample:
      value:
        result: success
        sendStatus:
          order_id: 614a5298-0071-450f-83c6-0617ce8c6bc4
          status: iocWouldNotExecute
          receivedTime: '2019-09-05T16:32:54.076Z'
          orderEvents:
            - type: REJECT
              uid: 614a5298-0071-450f-83c6-0617ce8c6bc4
              reason: IOC_WOULD_NOT_EXECUTE
              order:
                orderId: 614a5298-0071-450f-83c6-0617ce8c6bc4
                cliOrdId: null
                type: lmt
                symbol: PI_XBTUSD
                side: buy
                quantity: 10000
                filled: 0
                limitPrice: 9400
                reduceOnly: true
                timestamp: '2019-09-05T16:32:54.076Z'
                lastUpdateTimestamp: '2019-09-05T16:32:54.076Z'
        serverTime: '2019-09-05T16:32:54.077Z'
    ExecutedOrderExample:
      value:
        result: success
        sendStatus:
          order_id: 61ca5732-3478-42fe-8362-abbfd9465294
          status: placed
          receivedTime: '2019-12-11T17:17:33.888Z'
          orderEvents:
            - type: EXECUTION
              executionId: e1ec9f63-2338-4c44-b40a-43486c6732d7
              price: 7244.5
              amount: 10
              orderPriorEdit: null
              orderPriorExecution:
                orderId: 61ca5732-3478-42fe-8362-abbfd9465294
                cliOrdId: null
                type: lmt
                symbol: PI_XBTUSD
                side: buy
                quantity: 10
                filled: 0
                limitPrice: 7500
                reduceOnly: false
                timestamp: '2019-12-11T17:17:33.888Z'
                lastUpdateTimestamp: '2019-12-11T17:17:33.888Z'
              takerReducedQuantity: null
        serverTime: '2019-12-11T17:17:33.888Z'
  responses:
    ContractAccessForbidden:
      x-summary: Contract access forbidden
      description: |-
        Account is not permitted to perform the requested trading operation.

        - Error `code`: 95
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/_schemas_ErrorResponse'
  securitySchemes:
    general-api-key:
      type: apiKey
      description: General API key with **full** access
      in: header
      name: APIKey
      x-inlineDescription: true
    authent:
      type: apiKey
      description: Authentication string
      in: header
      name: Authent
      x-inlineDescription: true

````
