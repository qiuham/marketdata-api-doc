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
source_url: 'https://docs.kraken.com/api-reference/order-management/batch-order-management'
updated_at: 2026-11-13
---

# Batch order management

> This endpoint allows sending limit or stop order(s) and/or cancelling open order(s) and/or
editing open order(s) for a currently listed Futures contract in batch.

When editing an order, if the `trailingStopMaxDeviation` and `trailingStopDeviationUnit`
parameters are sent unchanged, the system will recalculate a new stop price upon successful
order modification.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /batchorder
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
  /batchorder:
    post:
      tags:
        - Order Management
      summary: Batch order management
      description: >-
        This endpoint allows sending limit or stop order(s) and/or cancelling
        open order(s) and/or

        editing open order(s) for a currently listed Futures contract in batch.


        When editing an order, if the `trailingStopMaxDeviation` and
        `trailingStopDeviationUnit`

        parameters are sent unchanged, the system will recalculate a new stop
        price upon successful

        order modification.
      operationId: sendBatchOrder
      parameters:
        - $ref: '#/components/parameters/AlgoId'
        - $ref: '#/components/parameters/ProcessBefore'
        - description: Contains the request body as a String
          name: json
          in: query
          required: true
          content:
            application/json:
              schema:
                title: Batch Order
                type: object
                additionalProperties: false
                required:
                  - batchOrder
                properties:
                  batchOrder:
                    type: array
                    maxItems: 500
                    items:
                      title: Batch Instruction
                      discriminator:
                        propertyName: order
                        mapping:
                          send: '#/components/schemas/BatchOrderSend'
                          edit: '#/components/schemas/BatchOrderEdit'
                          cancel: '#/components/schemas/BatchOrderCancel'
                      oneOf:
                        - $ref: '#/components/schemas/BatchOrderSend'
                        - $ref: '#/components/schemas/BatchOrderEdit'
                        - $ref: '#/components/schemas/BatchOrderCancel'
                    description: >-
                      A list containing structures of order sending and order
                      cancellation

                      instructions. Instructions are applied in the order given,
                      except that on

                      markets with a maker protection window each
                      liquidity-taking instruction is

                      held on its own for the window while every other
                      instruction, cancels

                      included, is processed immediately wherever it appears.
                examples:
                  - batchOrder:
                      - order: send
                        order_tag: '1'
                        orderType: lmt
                        symbol: PI_XBTUSD
                        side: buy
                        size: 1
                        limitPrice: 1
                        cliOrdId: my_another_client_id
                      - order: send
                        order_tag: '2'
                        orderType: stp
                        symbol: PI_XBTUSD
                        side: buy
                        size: 1
                        limitPrice: 2
                        stopPrice: 3
                      - order: cancel
                        order_id: e35d61dd-8a30-4d5f-a574-b5593ef0c050
                      - order: cancel
                        cliOrdId: my_client_id
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
                        required:
                          - batchStatus
                        properties:
                          batchStatus:
                            type: array
                            items:
                              $ref: '#/components/schemas/BatchInstructionResult'
                            description: >-
                              A structure containing information on the send
                              order request.
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/BatchOrderExample'
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
    BatchOrderSend:
      type: object
      required:
        - symbol
        - order_tag
        - side
        - size
        - orderType
      properties:
        order:
          type: string
          description: Always `send`.
          enum:
            - send
        order_tag:
          type: string
          description: >-
            An arbitrary string provided client-side to tag the order for the
            purpose of

            mapping order sending instructions to the API's response.
        orderType:
          $ref: '#/components/schemas/OrderType'
        symbol:
          type: string
          description: The symbol of the Futures.
        side:
          $ref: '#/components/schemas/OrderDirection'
        size:
          type: number
          description: The size associated with the order.
        limitPrice:
          type: number
          description: >-
            The limit price associated with the order. If placing a
            `trailing_stop` order then leave

            undefined.
        stopPrice:
          type: number
          description: >-
            The stop price associated with a stop order. Required if `orderType`
            is `stp`.

            For `stp` orders, `limitPrice` denotes the worst price at which the
            order can get

            filled. If no `limitPrice` is provided, the `stp` order will trigger
            a market order.
        cliOrdId:
          type: string
          description: >-
            The order identity that is specified from the user. It must be
            globally unique.
          maxLength: 100
        triggerSignal:
          type: string
          enum:
            - mark
            - index
            - last
        reduceOnly:
          type: boolean
          description: >-
            Set as 'true' if you wish the order to only reduce an existing
            position. Any order which

            increases an existing position will be rejected. Default 'false'.
          default: false
        trailingStopMaxDeviation:
          type: number
          description: >-
            Required if the order type is `trailing_stop`.


            Is the maximum distance the trailing stop's trigger price may trail
            behind the requested trigger signal.

            It defines the threshold at which the trigger price updates.
        trailingStopDeviationUnit:
          type: string
          enum:
            - PERCENT
            - QUOTE_CURRENCY
          description: >-
            Required if the order type is `trailing_stop`.


            This defines how the trailing trigger price is calculated from the
            requested trigger

            signal. For example, if the max deviation is set to 10, the unit is
            'PERCENT', and the

            underlying order is a sell, then the trigger price will never be
            more then 10% below the

            trigger signal. Similarly, if the deviation is 100, the unit is
            'QUOTE_CURRENCY', the

            underlying order is a sell, and the contract is quoted in USD, then
            the trigger price

            will never be more than $100 below the trigger signal.
      example:
        order: send
        order_tag: '1'
        orderType: lmt
        symbol: PI_XBTUSD
        side: buy
        size: 1
        limitPrice: 1
        cliOrdId: my_another_client_id
    BatchOrderEdit:
      allOf:
        - $ref: '#/components/schemas/OrderIdElement'
        - type: object
          properties:
            order:
              type: string
              description: Always `edit`.
              enum:
                - edit
            size:
              type: number
              description: The size associated with the order.
            limitPrice:
              type: number
              description: The limit price associated with the order.
            stopPrice:
              type: number
              description: >-
                The stop price associated with a stop order. Cannot be edited on
                trailing stop

                orders. If `limitPrice` is not sent, the order keeps its current
                limit price.
            trailingStopMaxDeviation:
              type: number
              description: >-
                Only relevant for trailing stop orders. Maximum value of 50%,
                minimum value of 0.1%

                for 'PERCENT' 'maxDeviationUnit'.


                Is the maximum distance the trailing stop's trigger price may
                trail behind the

                requested trigger signal. It defines the threshold at which the
                trigger price

                updates.
              minimum: 0.1
              maximum: 50
            trailingStopDeviationUnit:
              type: string
              enum:
                - PERCENT
                - QUOTE_CURRENCY
              description: >-
                Only relevant for trailing stop orders.


                This defines how the trailing trigger price is calculated from
                the requested trigger

                signal. For example, if the max deviation is set to 10, the unit
                is 'PERCENT', and

                the underlying order is a sell, then the trigger price will
                never be more then 10%

                below the trigger signal. Similarly, if the deviation is 100,
                the unit is

                'QUOTE_CURRENCY', the underlying order is a sell, and the
                contract is quoted in USD,

                then the trigger price will never be more than $100 below the
                trigger signal.
            qtyMode:
              type: string
              enum:
                - ABSOLUTE
                - RELATIVE
              description: >-
                Determines how the updated size is interpreted, defaulting to
                'RELATIVE'.


                'ABSOLUTE' means that the total order size, including past
                fills, is set to `size`.

                'RELATIVE' means that the current open order size is set to
                `size`.
    BatchOrderCancel:
      example:
        order: cancel
        order_id: e35d61dd-8a30-4d5f-a574-b5593ef0c050
      allOf:
        - type: object
          properties:
            order:
              description: Always `cancel`.
              type: string
              enum:
                - cancel
          required:
            - order
        - $ref: '#/components/schemas/CancelInstruction'
    BatchInstructionResult:
      type: object
      properties:
        cliOrdId:
          type: string
          description: >-
            The unique client order identifier. This field is returned only if
            the order has a

            client order ID.
        dateTimeReceived:
          type:
            - string
            - 'null'
          description: The date and time the order was received.
        orderEvents:
          type: array
          items:
            $ref: '#/components/schemas/OrderEvent'
        order_id:
          type:
            - string
            - 'null'
          description: The unique identifier of the order.
        order_tag:
          type:
            - string
            - 'null'
          description: >-
            The arbitrary string provided client-side when the order was sent
            for the purpose of

            mapping order sending instructions to the API's response.
        status:
          type: string
          enum:
            - placed
            - edited
            - cancelled
            - invalidOrderType
            - invalidSide
            - invalidSize
            - invalidPrice
            - insufficientAvailableFunds
            - selfFill
            - tooManySmallOrders
            - marketSuspended
            - marketInactive
            - clientOrderIdAlreadyExist
            - clientOrderIdTooLong
            - outsidePriceCollar
            - postWouldExecute
            - iocWouldNotExecute
            - tooManyOrders
            - makerProtectionOrderLimitExceeded
            - marketIsCancelOnly
          description: >-
            The status of the order:


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

            - `marketSuspended` - the order was not placed because the market is
            suspended

            - `marketInactive` - the order was not placed because the market is
            inactive

            - `clientOrderIdAlreadyExist` - the specified client ID already
            exist

            - `clientOrderIdTooLong` - the client ID is longer than the
            permissible limit

            - `outsidePriceCollar` - the limit order crosses the spread but is
            an order of magnitude away from the mark price - fat finger control

            - `postWouldExecute` - the post-only order would be filled upon
            placement, thus is  cancelled

            - `iocWouldNotExecute` - the immediate-or-cancel order would not
            execute

            - `tooManyOrders` - the order was not placed because it would exceed
            a limit on how many orders the account may have outstanding at once

            - `makerProtectionOrderLimitExceeded` - the order was not placed
            because accepting it would exceed the maker protection live-hold
            limit

            - `marketIsCancelOnly` - the order was not placed because the venue
            is in cancel-only mode: only cancellations are accepted until it is
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
    OrderIdElement:
      type: object
      description: Provide either `order_id` or `cliOrdId`.
      properties:
        cliOrdId:
          type:
            - string
            - 'null'
          description: Unique client order identifier.
          maxLength: 100
        order_id:
          description: Order ID.
          type: string
          format: uuid
      required:
        - order_id
    CancelInstruction:
      type: object
      description: Provide either `order_id` or `cliOrdId`.
      properties:
        order_id:
          description: Order ID.
          type: string
          format: uuid
        cliOrdId:
          description: Unique client order identifier.
          type: string
          maxLength: 100
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
    BatchOrderExample:
      value:
        result: success
        batchStatus:
          - status: placed
            order_tag: '1'
            order_id: 022774bc-2c4a-4f26-9317-436c8d85746d
            dateTimeReceived: '2019-09-05T16:41:35.173Z'
            orderEvents:
              - type: PLACE
                order:
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
                reducedQuantity: null
          - status: edited
            order_id: 9c2cbcc8-14f6-42fe-a020-6e395babafd1
            orderEvents:
              - type: EDIT
                old:
                  orderId: 9c2cbcc8-14f6-42fe-a020-6e395babafd1
                  cliOrdId: null
                  type: lmt
                  symbol: PI_XBTUSD
                  side: buy
                  quantity: 102
                  filled: 0
                  limitPrice: 8500
                  reduceOnly: false
                  timestamp: '2019-09-04T11:45:48.884Z'
                  lastUpdateTimestamp: '2019-09-04T11:45:48.884Z'
                new:
                  orderId: 9c2cbcc8-14f6-42fe-a020-6e395babafd1
                  cliOrdId: null
                  type: lmt
                  symbol: PI_XBTUSD
                  side: buy
                  quantity: 1000
                  filled: 0
                  limitPrice: 9400
                  reduceOnly: false
                  timestamp: '2019-09-04T11:45:48.884Z'
                  lastUpdateTimestamp: '2019-09-05T16:41:40.996Z'
                reducedQuantity: null
          - status: cancelled
            order_id: 566942c8-a3b5-4184-a451-622b09493129
            orderEvents:
              - type: CANCEL
                uid: 566942c8-a3b5-4184-a451-622b09493129
                order:
                  orderId: 566942c8-a3b5-4184-a451-622b09493129
                  cliOrdId: null
                  type: lmt
                  symbol: PI_XBTUSD
                  side: buy
                  quantity: 100
                  filled: 0
                  limitPrice: 8500
                  reduceOnly: false
                  timestamp: '2019-09-02T12:54:08.005Z'
                  lastUpdateTimestamp: '2019-09-02T12:54:08.005Z'
        serverTime: '2019-09-05T16:41:40.996Z'
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
