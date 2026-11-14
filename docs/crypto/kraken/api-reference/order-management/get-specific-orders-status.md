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
source_url: 'https://docs.kraken.com/api-reference/order-management/get-specific-orders-status'
updated_at: 2026-11-13
---

# Get Specific Orders' Status

> Returns information on specified orders which are open or were filled/cancelled in the last
5 seconds.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /orders/status
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
  /orders/status:
    post:
      tags:
        - Order Management
      summary: Get Specific Orders' Status
      description: >-
        Returns information on specified orders which are open or were
        filled/cancelled in the last

        5 seconds.
      operationId: getOrderStatus
      parameters:
        - description: UIDs associated with orders or triggers.
          name: orderIds
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
              format: uuid
        - description: Client Order IDs associated with orders or triggers.
          name: cliOrdIds
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          example:
            - testOrder1
            - testOrder2
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
                          orders:
                            type: array
                            items:
                              $ref: '#/components/schemas/OrderStatusDetailsJson'
                        required:
                          - orders
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key: []
          authent: []
components:
  schemas:
    OrderStatusDetailsJson:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/CachedOrderJson'
        status:
          $ref: '#/components/schemas/OrderStatusJson'
        updateReason:
          oneOf:
            - $ref: '#/components/schemas/OrderUpdateReason'
            - type: 'null'
        error:
          oneOf:
            - $ref: '#/components/schemas/OrderError'
            - type: 'null'
      required:
        - order
        - status
        - updateReason
        - error
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
    CachedOrderJson:
      type: object
      properties:
        type:
          type: string
          enum:
            - TRIGGER_ORDER
            - ORDER
        orderId:
          type: string
          format: uuid
        cliOrdId:
          type:
            - string
            - 'null'
        symbol:
          type: string
        side:
          type: string
        quantity:
          type:
            - number
            - 'null'
        filled:
          type:
            - number
            - 'null'
        limitPrice:
          type:
            - number
            - 'null'
        reduceOnly:
          type: boolean
        timestamp:
          type: string
        lastUpdateTimestamp:
          type: string
        algoId:
          type:
            - string
            - 'null'
          description: ID of the algorithm that placed the order.
          x-cfOnly: true
        priceTriggerOptions:
          oneOf:
            - $ref: '#/components/schemas/TriggerOptions'
            - type: 'null'
        triggerTime:
          type:
            - string
            - 'null'
      required:
        - type
        - orderId
        - cliOrdId
        - symbol
        - side
        - quantity
        - filled
        - limitPrice
        - reduceOnly
        - timestamp
        - lastUpdateTimestamp
        - algoId
        - priceTriggerOptions
        - triggerTime
    OrderStatusJson:
      type: string
      enum:
        - ENTERED_BOOK
        - FULLY_EXECUTED
        - REJECTED
        - CANCELLED
        - TRIGGER_PLACED
        - TRIGGER_ACTIVATION_FAILURE
    OrderUpdateReason:
      type: string
      enum:
        - LOADING_MARKET
        - NEW_USER_ORDER
        - LIQUIDATION_ORDER
        - STOP_ORDER_TRIGGERED
        - LIMIT_FROM_STOP
        - PARTIAL_FILL
        - FULL_FILL
        - CANCELLED_BY_USER
        - CONTRACT_EXPIRED
        - NOT_ENOUGH_MARGIN
        - MARKET_INACTIVE
        - DEAD_MAN_SWITCH
        - CANCELLED_BY_ADMIN
        - POST_WOULD_EXECUTE_REASON
        - IOC_WOULD_NOT_EXECUTE_REASON
        - WOULD_EXECUTE_SELF_REASON
        - WOULD_NOT_REDUCE_POSITION
        - EDITED_BY_USER
        - ORDER_FOR_EDIT_NOT_FOUND_REASON
        - EXPIRED
        - TRAILING_STOP_PRICE_UPDATED
        - TRAILING_STOP_CANCELLED_AND_REPLACED_BY_ADMIN
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
    TriggerOptions:
      type: object
      properties:
        triggerPrice:
          type: number
        triggerSide:
          type: string
          enum:
            - TRIGGER_ABOVE
            - TRIGGER_BELOW
        triggerSignal:
          type: string
          enum:
            - MARK_PRICE
            - LAST_PRICE
            - SPOT_PRICE
        trailingStopOptions:
          oneOf:
            - $ref: '#/components/schemas/TrailingStopOptions'
            - type: 'null'
          x-internalOnly: true
      required:
        - triggerPrice
        - triggerSide
        - triggerSignal
    TrailingStopOptions:
      type: object
      x-internalOnly: true
      properties:
        maxDeviation:
          type: number
          description: >-
            The maximum distance the trailing stop's trigger price may trail
            behind the requested trigger signal.

            It defines the threshold at which the trigger price updates.
        unit:
          enum:
            - PERCENT
            - QUOTE_CURRENCY
          type: string
          description: >-
            This defines how the trailing trigger price is calculated from the
            requested trigger

            signal. For example, if the max deviation is set to 10, the unit is
            'PERCENT', and the

            underlying order is a sell, then the trigger price will never be
            more then 10% below

            the trigger signal. Similarly, if the deviation is 100, the unit is
            'QUOTE_CURRENCY',

            the underlying order is a sell, and the contract is quoted in USD,
            then the trigger

            price will never be more than $100 below the trigger signal.
      required:
        - maxDeviation
        - unit
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
