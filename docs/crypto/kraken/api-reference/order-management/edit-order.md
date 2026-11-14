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
source_url: 'https://docs.kraken.com/api-reference/order-management/edit-order'
updated_at: 2026-11-13
---

# Edit order

> This endpoint allows editing an existing order for a currently listed Futures contract.

When editing an order, if the `trailingStopMaxDeviation` and `trailingStopDeviationUnit`
parameters are sent unchanged, the system will recalculate a new stop price upon successful
order modification.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /editorder
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
  /editorder:
    post:
      tags:
        - Order Management
      summary: Edit order
      description: >-
        This endpoint allows editing an existing order for a currently listed
        Futures contract.


        When editing an order, if the `trailingStopMaxDeviation` and
        `trailingStopDeviationUnit`

        parameters are sent unchanged, the system will recalculate a new stop
        price upon successful

        order modification.
      operationId: editOrderSpring
      parameters:
        - $ref: '#/components/parameters/AlgoId'
        - $ref: '#/components/parameters/ProcessBefore'
        - description: >-
            ID of the order you wish to edit. (Required if CliOrdId is not
            included)
          name: orderId
          in: query
          schema:
            type: string
        - description: >-
            The order identity that is specified from the user. It must be
            globally unique (Required

            if orderId is not included)
          name: cliOrdId
          in: query
          schema:
            type: string
        - description: The size associated with the order
          name: size
          in: query
          schema:
            type: number
        - description: >-
            The limit price associated with the order. Must not exceed the tick
            size of the contract.
          name: limitPrice
          in: query
          schema:
            type: number
        - description: >-
            The stop price associated with a stop order. Must not exceed tick
            size of the contract.

            Cannot be edited on trailing stop orders. If `limitPrice` is not
            sent, the order keeps

            its current limit price.
          name: stopPrice
          in: query
          schema:
            type: number
        - name: trailingStopMaxDeviation
          in: query
          schema:
            type: number
            description: >-
              Only relevant for trailing stop orders. Maximum value of 50%,
              minimum value of 0.1% for 'PERCENT' 'maxDeviationUnit'.


              Is the maximum distance the trailing stop's trigger price may
              trail behind the requested trigger signal.

              It defines the threshold at which the trigger price updates.
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
              Only relevant for trailing stop orders.


              This defines how the trailing trigger price is calculated from the
              requested trigger signal.

              For example, if the max deviation is set to 10, the unit is
              'PERCENT', and the underlying order is a sell,

              then the trigger price will never be more then 10% below the
              trigger signal.

              Similarly, if the deviation is 100, the unit is 'QUOTE_CURRENCY',
              the underlying order is a sell, and the

              contract is quoted in USD, then the trigger price will never be
              more than $100 below the trigger signal.
        - name: qtyMode
          in: query
          schema:
            type: string
            enum:
              - ABSOLUTE
              - RELATIVE
            description: >-
              Determines how the updated size is interpreted, defaulting to
              'RELATIVE'.


              'ABSOLUTE' means that the total order size, including past fills,
              is set to `size`.

              'RELATIVE' means that the current open order size is set to
              `size`.
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
                          editStatus:
                            $ref: '#/components/schemas/EditOrderStatus'
                            description: >-
                              A structure containing information on the send
                              order request
                        required:
                          - editStatus
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/EditOrderExample'
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
  schemas:
    EditOrderStatus:
      type: object
      properties:
        orderId:
          type:
            - string
            - 'null'
          description: The unique identifier of the order
        cliOrdId:
          type:
            - string
            - 'null'
          description: |-
            The unique client order identifier.

            This field is returned only if the order has a client order ID.
        orderEvents:
          type: array
          items:
            $ref: '#/components/schemas/OrderEvent'
        receivedTime:
          type:
            - string
            - 'null'
          description: The date and time the order was received
        status:
          type: string
          enum:
            - edited
            - filled
            - invalidSize
            - invalidPrice
            - insufficientAvailableFunds
            - makerProtectionOrderLimitExceeded
            - selfFill
            - tooManySmallOrders
            - outsidePriceCollar
            - postWouldExecute
            - iocWouldNotExecute
            - wouldNotReducePosition
            - orderForEditNotFound
            - orderForEditNotAStop
            - editAlreadyHeld
            - marketIsCancelOnly
          description: >-
            The status of the order, either of:


            - `edited` - The order was edited successfully

            - `filled` - The edit caused the order to fill completely

            - `invalidSize` - The order was not placed because size is invalid

            - `invalidPrice` - The order was not placed because limitPrice
            and/or stopPrice are invalid

            - `insufficientAvailableFunds` - The order was not placed because
            available funds are insufficient

            - `makerProtectionOrderLimitExceeded` - The edit was refused because
            it would exceed the market's maker protection live-hold limit

            - `selfFill` - The order was not placed because it would be filled
            against an existing order belonging to the same account

            - `tooManySmallOrders` - The order was not placed because the number
            of small open orders would exceed the permissible limit

            - `outsidePriceCollar` - The limit order crosses the spread but is
            an order of magnitude away from the mark price - fat finger control

            - `postWouldExecute` - The post-only order would be filled upon
            placement, thus is cancelled

            - `iocWouldNotExecute` - The edit made the order
            immediate-or-cancel, and the part that did not fill was removed from
            the book

            - `wouldNotReducePosition` - The edit cannot be applied because the
            reduce only policy is violated. (Only for reduceOnly orders)

            - `orderForEditNotFound` - The requested order for edit has not been
            found

            - `orderForEditNotAStop` - The supplied stopPrice cannot be applied
            because order is not a stop order

            - `editAlreadyHeld` - The edit was refused because an earlier edit
            of the order is still held for the market's maker protection window

            - `marketIsCancelOnly` - The edit was refused because the venue is
            in cancel-only mode: only cancellations are accepted until it is
            lifted
      required:
        - status
        - orderEvents
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
    EditOrderExample:
      value:
        result: success
        editStatus:
          status: edited
          orderId: 022774bc-2c4a-4f26-9317-436c8d85746d
          receivedTime: '2019-09-05T16:47:47.521Z'
          orderEvents:
            - type: EDIT
              old:
                orderId: 022774bc-2c4a-4f26-9317-436c8d85746d
                cliOrdId: null
                type: lmt
                symbol: PI_XBTUSD
                side: buy
                quantity: 1000
                filled: 0
                limitPrice: 9400
                reduceOnly: false
                timestamp: '2019-09-05T16:41:35.173Z'
                lastUpdateTimestamp: '2019-09-05T16:41:35.173Z'
              new:
                orderId: 022774bc-2c4a-4f26-9317-436c8d85746d
                cliOrdId: null
                type: lmt
                symbol: PI_XBTUSD
                side: buy
                quantity: 1501
                filled: 0
                limitPrice: 7200
                reduceOnly: false
                timestamp: '2019-09-05T16:41:35.173Z'
                lastUpdateTimestamp: '2019-09-05T16:47:47.519Z'
              reducedQuantity: null
        serverTime: '2019-09-05T16:47:47.521Z'
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
