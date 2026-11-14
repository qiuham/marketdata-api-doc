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
source_url: 'https://docs.kraken.com/api-reference/order-management/cancel-order'
updated_at: 2026-11-13
---

# Cancel order

> This endpoint allows cancelling an open order for a Futures contract.

A cancel of an order held for the market's maker protection window is answered when the
hold releases: the order first takes the liquidity it committed to, and the cancel then
removes whatever would have rested (`cancelled`), or finds nothing left of the order
(`notFound`).



## OpenAPI

````yaml /openapi/futures-rest.yaml post /cancelorder
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
  /cancelorder:
    post:
      tags:
        - Order Management
      summary: Cancel order
      description: >-
        This endpoint allows cancelling an open order for a Futures contract.


        A cancel of an order held for the market's maker protection window is
        answered when the

        hold releases: the order first takes the liquidity it committed to, and
        the cancel then

        removes whatever would have rested (`cancelled`), or finds nothing left
        of the order

        (`notFound`).
      operationId: cancelOrder
      parameters:
        - $ref: '#/components/parameters/AlgoId'
        - $ref: '#/components/parameters/ProcessBefore'
        - name: order_id
          in: query
          schema:
            type: string
            description: The unique identifier of the order to be cancelled.
        - name: cliOrdId
          in: query
          schema:
            type: string
            description: The client unique identifier of the order to be cancelled.
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
                          cancelStatus:
                            $ref: '#/components/schemas/CancelOrderStatusJson'
                            description: >-
                              A structure containing information on the
                              cancellation request.
                        required:
                          - cancelStatus
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/CancelOrderExample'
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
    CancelOrderStatusJson:
      type: object
      properties:
        cliOrdId:
          type:
            - string
            - 'null'
          description: The client order ID. Shown only if client specified one.
        orderEvents:
          type: array
          items:
            $ref: '#/components/schemas/OrderEvent'
        order_id:
          type: string
          format: uuid
          description: The cancelled order UID
        receivedTime:
          type: string
          description: The date and time the order cancellation was received.
        status:
          type: string
          enum:
            - cancelled
            - filled
            - notFound
          description: >-
            The status of the order cancellation:


            - `cancelled` - The order has been cancelled. This may only be part
            of the order as part may have been filled. Check open_orders
            websocket feed for status of the order.

            - `filled` - The order was found completely filled and could not be
            cancelled

            - `notFound` - The order was not found, either because it had
            already been cancelled or it never existed
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
    CancelOrderExample:
      value:
        result: success
        cancelStatus:
          status: cancelled
          order_id: cb4e34f6-4eb3-4d4b-9724-4c3035b99d47
          receivedTime: '2020-07-22T13:26:20.806Z'
          orderEvents:
            - type: CANCEL
              uid: cb4e34f6-4eb3-4d4b-9724-4c3035b99d47
              order:
                orderId: cb4e34f6-4eb3-4d4b-9724-4c3035b99d47
                cliOrdId: '1234568'
                type: lmt
                symbol: PI_XBTUSD
                side: buy
                quantity: 5500
                filled: 0
                limitPrice: 8000
                reduceOnly: false
                timestamp: '2020-07-22T13:25:56.366Z'
                lastUpdateTimestamp: '2020-07-22T13:25:56.366Z'
        serverTime: '2020-07-22T13:26:20.806Z'
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
