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
source_url: 'https://docs.kraken.com/api-reference/historical-data/get-your-fills'
updated_at: 2026-11-13
---

# Get your fills

> This endpoint returns information on your filled orders for all futures contracts.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /fills
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
  /fills:
    get:
      tags:
        - Historical Data
      summary: Get your fills
      description: >-
        This endpoint returns information on your filled orders for all futures
        contracts.
      operationId: getFills
      parameters:
        - description: >-
            If not provided, returns the last 100 fills in any futures contract.
            If provided,

            returns the 100 entries before lastFillTime.
          name: lastFillTime
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
                          fills:
                            type: array
                            items:
                              $ref: '#/components/schemas/FillJson'
                            description: >-
                              A list containing structures with information on
                              filled orders. The

                              list is sorted descending by `fillTime`.
                        required:
                          - fills
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/FillsExample'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    FillJson:
      type: object
      properties:
        cliOrdId:
          type:
            - string
            - 'null'
          description: |-
            The unique client order identifier.

            This field is returned only if the order has a client order ID.
        fillTime:
          type: string
          description: The date and time the order was filled.
          example: '2021-11-18T02:39:41.826Z'
        fillType:
          type: string
          enum:
            - maker
            - taker
            - liquidation
            - partialLiquidation
            - assignor
            - assignee
            - takerAfterEdit
            - unwindBankrupt
            - unwindCounterparty
          description: >-
            The classification of the fill:


            - `maker` - user has a limit order that gets filled

            - `taker` - the user makes an execution that crosses the spread

            - `liquidation` - execution is result of a liquidation

            - `partialLiquidation` - execution is part of a partial liquidation
            to gradually reduce a position before full liquidation

            - `assignee` - execution is a result of a counterparty receiving an
            Assignment in PAS

            - `assignor` - execution is a result of user assigning their
            position due to failed liquidation
          example: maker
        fill_id:
          type: string
          format: uuid
          description: >-
            The unique identifier of the fill. Note that several `fill_id` can
            pertain to one

            `order_id` (but not vice versa)
        order_id:
          type: string
          format: uuid
          description: The unique identifier of the order.
        price:
          type: number
          description: The price of the fill.
          example: 47000
        side:
          type: string
          enum:
            - buy
            - sell
          description: The direction of the order.
          example: buy
        size:
          type: number
          description: The size of the fill.
          example: 10
        symbol:
          type: string
          description: The symbol of the futures the fill occurred in.
          example: PI_XBTUSD
        realized_pnl:
          type:
            - number
            - 'null'
          description: >-
            Realised PnL for this fill, signed from the requesting account's
            perspective

            (positive = gain, negative = loss). `0` when the fill opens or
            increases a position.


            Null when the fill was recorded before this field was introduced, or
            when the request

            uses `lastFillTime` (the historical query path does not currently
            carry realised PnL).
          example: 12.5
        sequence_id:
          type: string
          description: >-
            Per-market monotonic sequential trade id, starting at 1 for each
            market and

            incrementing by 1 per execution, for downstream gap detection and
            trade sequencing.

            Encoded as a string because the value is a 64-bit unsigned integer,
            which is unsafe

            as a JSON number. Omitted for fills recorded before sequential trade
            ids were

            introduced.
          example: '42'
      required:
        - fill_id
        - symbol
        - side
        - order_id
        - size
        - price
        - fillTime
        - fillType
      example:
        fill_id: 98e3deeb-0385-4b25-b15e-7e8453512cb2
        fillTime: '2021-11-18T02:39:41.826Z'
        fillType: maker
        order_id: 06b9d509-965c-4788-b317-0e5ca11d56fb
        price: 47000
        side: buy
        size: 10
        symbol: PI_XBTUSD
        realized_pnl: 12.5
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
    FillsExample:
      value:
        result: success
        fills:
          - fill_id: 3d57ed09-fbd6-44f1-8e8b-b10e551c5e73
            symbol: PI_XBTUSD
            side: buy
            order_id: 693af756-055e-47ef-99d5-bcf4c456ebc5
            size: 5490
            price: 9400
            fillTime: '2020-07-22T13:37:27.077Z'
            fillType: maker
          - fill_id: 56b86ada-73b0-454d-a95a-e29e3e85b349
            symbol: PI_XBTUSD
            side: buy
            order_id: 3f513c4c-683d-44ab-a73b-d296abbea201
            size: 5000
            price: 9456
            fillTime: '2020-07-21T12:41:52.790Z'
            fillType: taker
        serverTime: '2020-07-22T13:44:24.311Z'
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
