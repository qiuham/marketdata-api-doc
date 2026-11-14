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
source_url: 'https://docs.kraken.com/api-reference/order-management/cancel-all-orders'
updated_at: 2026-11-13
---

# Cancel all orders

> This endpoint allows cancelling orders which are associated with a future's contract or a
margin account. If no arguments are specified all open orders will be cancelled.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /cancelallorders
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
  /cancelallorders:
    post:
      tags:
        - Order Management
      summary: Cancel all orders
      description: >-
        This endpoint allows cancelling orders which are associated with a
        future's contract or a

        margin account. If no arguments are specified all open orders will be
        cancelled.
      operationId: cancelAllOrders
      parameters:
        - $ref: '#/components/parameters/AlgoId'
        - description: A futures product to cancel all open orders.
          name: symbol
          in: query
          required: false
          schema:
            type: string
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
                            $ref: '#/components/schemas/CancelAllOrdersStatusJson'
                            description: >-
                              A structure containing information on the
                              cancellation request.
                        required:
                          - cancelStatus
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/CancelAllOrdersExample'
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
  schemas:
    CancelAllOrdersStatusJson:
      type: object
      properties:
        cancelOnly:
          type: string
          description: The symbol of the futures or all.
        cancelledOrders:
          type: array
          items:
            $ref: '#/components/schemas/OrderIdElement'
          description: >-
            A list of structures containing all the successfully cancelled
            orders.
        orderEvents:
          type: array
          items:
            $ref: '#/components/schemas/CancelEvent'
        receivedTime:
          type: string
          description: The date and time the order cancellation was received.
        status:
          type: string
          enum:
            - noOrdersToCancel
            - cancelled
          description: |-
            The status of the order cancellation:

            - `cancelled` - successful cancellation
            - `noOrdersToCancel` - no open orders for cancellation
      required:
        - cancelOnly
        - cancelledOrders
        - orderEvents
        - receivedTime
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
  examples:
    CancelAllOrdersExample:
      value:
        result: success
        cancelStatus:
          receivedTime: '2019-08-01T15:57:37.518Z'
          cancelOnly: all
          status: cancelled
          cancelledOrders:
            - order_id: 6180adfa-e4b1-4a52-adac-ea5417620dbd
            - order_id: 89e3edbe-d739-4c52-b866-6f5a8407ff6e
            - order_id: 0cd37a77-1644-4960-a7fb-9a1f6e0e46f7
          orderEvents:
            - type: CANCEL
              uid: 89e3edbe-d739-4c52-b866-6f5a8407ff6e
              order:
                orderId: 89e3edbe-d739-4c52-b866-6f5a8407ff6e
                cliOrdId: null
                type: post
                symbol: PI_XBTUSD
                side: buy
                quantity: 890
                filled: 0
                limitPrice: 10040
                reduceOnly: false
                timestamp: '2019-08-01T15:57:08.508Z'
                lastUpdateTimestamp: '2019-08-01T15:57:08.508Z'
            - type: CANCEL
              uid: 0cd37a77-1644-4960-a7fb-9a1f6e0e46f7
              order:
                orderId: 0cd37a77-1644-4960-a7fb-9a1f6e0e46f7
                cliOrdId: null
                type: lmt
                symbol: PI_XBTUSD
                side: sell
                quantity: 900
                filled: 0
                limitPrice: 10145
                reduceOnly: true
                timestamp: '2019-08-01T15:57:14.003Z'
                lastUpdateTimestamp: '2019-08-01T15:57:14.003Z'
        serverTime: '2019-08-01T15:57:37.520Z'
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
