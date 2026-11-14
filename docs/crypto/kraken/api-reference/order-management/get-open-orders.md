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
source_url: 'https://docs.kraken.com/api-reference/order-management/get-open-orders'
updated_at: 2026-11-13
---

# Get open orders

> This endpoint returns information on all open orders for all Futures contracts.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /openorders
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
  /openorders:
    get:
      tags:
        - Order Management
      summary: Get open orders
      description: >-
        This endpoint returns information on all open orders for all Futures
        contracts.
      operationId: getOpenOrders
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
                          openOrders:
                            type: array
                            items:
                              $ref: '#/components/schemas/OpenOrderJson'
                            description: >-
                              A list containing structures with information on
                              open orders. The list

                              is sorted descending by receivedTime.
                        required:
                          - openOrders
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/OpenOrdersExample'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    OpenOrderJson:
      type: object
      properties:
        order_id:
          type: string
          format: uuid
          description: The unique identifier of the order.
        cliOrdId:
          type: string
          description: >-
            The unique client order identifier. This field is returned only if
            the order has a

            client order ID.
        status:
          type: string
          enum:
            - untouched
            - partiallyFilled
          description: >-
            The status of the order:


            - `untouched` - the entire size of the order is unfilled

            - `partiallyFilled` - the size of the order is partially but not
            entirely filled
        side:
          type: string
          enum:
            - buy
            - sell
          description: The direction of the order.
        orderType:
          type: string
          enum:
            - lmt
            - stop
            - take_profit
          description: |-
            The order type:

            - `lmt` - limit order
            - `stp` - stop order
            - `take_profit` - take profit order
        symbol:
          type: string
          description: The symbol of the futures to which the order refers.
        limitPrice:
          type: number
          description: The limit price associated with the order.
        stopPrice:
          type: number
          description: |-
            If orderType is `stp`: The stop price associated with the order

            If orderType is `lmt`: Not returned because N/A
        filledSize:
          type: number
          description: The filled size associated with the order.
        unfilledSize:
          type: number
          description: The unfilled size associated with the order.
        reduceOnly:
          type: boolean
          description: Is the order a reduce only order or not.
        triggerSignal:
          description: The trigger signal for the stop or take profit order.
          type: string
          enum:
            - mark
            - last
            - spot
        lastUpdateTime:
          description: The date and time the order was last updated.
          type: string
          format: date-time
        receivedTime:
          description: The date and time the order was received.
          type: string
          format: date-time
        algoId:
          description: ID of the algorithm that placed the order.
          type: string
          x-cfOnly: true
      required:
        - receivedTime
        - lastUpdateTime
        - status
        - order_id
        - orderType
        - symbol
        - side
        - filledSize
        - reduceOnly
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
  examples:
    OpenOrdersExample:
      value:
        result: success
        openOrders:
          - order_id: 59302619-41d2-4f0b-941f-7e7914760ad3
            symbol: PI_XBTUSD
            side: sell
            orderType: lmt
            limitPrice: 10640
            unfilledSize: 304
            receivedTime: '2019-09-05T17:01:17.410Z'
            status: untouched
            filledSize: 0
            reduceOnly: true
            lastUpdateTime: '2019-09-05T17:01:17.410Z'
          - order_id: 022774bc-2c4a-4f26-9317-436c8d85746d
            symbol: PI_XBTUSD
            side: buy
            orderType: lmt
            limitPrice: 7200
            unfilledSize: 1501
            receivedTime: '2019-09-05T16:41:35.173Z'
            status: untouched
            filledSize: 0
            reduceOnly: false
            lastUpdateTime: '2019-09-05T16:47:47.519Z'
          - order_id: d08021f7-58cb-4f2c-9c86-da4c60de46bb
            symbol: PI_XBTUSD
            side: sell
            orderType: lmt
            limitPrice: 10640
            unfilledSize: 10000
            receivedTime: '2019-09-05T16:38:43.651Z'
            status: untouched
            filledSize: 0
            reduceOnly: true
            lastUpdateTime: '2019-09-05T16:38:43.651Z'
          - order_id: 179f9af8-e45e-469d-b3e9-2fd4675cb7d0
            symbol: PI_XBTUSD
            side: buy
            orderType: lmt
            limitPrice: 9400
            unfilledSize: 10000
            receivedTime: '2019-09-05T16:33:50.734Z'
            status: untouched
            filledSize: 0
            reduceOnly: false
            lastUpdateTime: '2019-09-05T16:33:50.734Z'
          - order_id: 9c2cbcc8-14f6-42fe-a020-6e395babafd1
            symbol: PI_XBTUSD
            side: buy
            orderType: lmt
            limitPrice: 9400
            unfilledSize: 1000
            receivedTime: '2019-09-04T11:45:48.884Z'
            status: untouched
            filledSize: 0
            reduceOnly: false
            lastUpdateTime: '2019-09-05T16:41:40.996Z'
          - order_id: 3deea5c8-0274-4d33-988c-9e5a3895ccf8
            symbol: PI_XBTUSD
            side: buy
            orderType: lmt
            limitPrice: 8500
            unfilledSize: 102
            receivedTime: '2019-09-03T12:52:17.945Z'
            status: untouched
            filledSize: 0
            reduceOnly: false
            lastUpdateTime: '2019-09-03T12:52:17.945Z'
          - order_id: fcbb1459-6ed2-4b3c-a58c-67c4df7412cf
            symbol: PI_XBTUSD
            side: buy
            orderType: lmt
            limitPrice: 7200
            unfilledSize: 1501
            receivedTime: '2019-09-02T12:54:34.347Z'
            status: untouched
            filledSize: 0
            reduceOnly: false
            lastUpdateTime: '2019-09-02T12:54:34.347Z'
        serverTime: '2019-09-05T17:08:18.138Z'
  securitySchemes:
    general-api-key-read-only:
      type: apiKey
      description: General API key with at least **read-only** access
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
