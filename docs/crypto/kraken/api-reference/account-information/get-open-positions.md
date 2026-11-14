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
source_url: 'https://docs.kraken.com/api-reference/account-information/get-open-positions'
updated_at: 2026-11-13
---

# Get open positions

> This endpoint returns the size and average entry price of all open positions in Futures
contracts. This includes Futures contracts that have matured but have not yet been settled.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /openpositions
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
  /openpositions:
    get:
      tags:
        - Account Information
      summary: Get open positions
      description: >-
        This endpoint returns the size and average entry price of all open
        positions in Futures

        contracts. This includes Futures contracts that have matured but have
        not yet been settled.
      operationId: getOpenPositions
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
                          openPositions:
                            type: array
                            items:
                              $ref: '#/components/schemas/OpenPositionJson'
                            description: >-
                              A list containing structures with information on
                              open positions.


                              The list is sorted descending by fillTime.
                        required:
                          - openPositions
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/OpenPositionsSuccessExample'
                failure:
                  $ref: '#/components/examples/OpenPositionsFailureExample'
        '409':
          $ref: '#/components/responses/CancelOnly'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    OpenPositionJson:
      type: object
      properties:
        symbol:
          type: string
          description: The symbol of the Futures.
        side:
          type: string
          enum:
            - long
            - short
          x-exhaustive: true
          description: The direction of the position.
        size:
          format: double
          type: number
          description: The size of the position.
        price:
          format: double
          type: number
          description: The average price at which the position was entered into.
        unrealizedPnl:
          type: number
          format: double
          description: Unrealised profit and loss on the position.
        unrealizedFunding:
          type:
            - number
            - 'null'
          format: double
          description: Unrealised funding on the position.
        pnlCurrency:
          x-kfOnly: true
          type:
            - string
            - 'null'
          enum:
            - USD
            - EUR
            - GBP
            - USDC
            - USDT
            - BTC
            - ETH
          description: 'Selected pnl currency for the position (default: USD)'
        maxFixedLeverage:
          x-kfOnly: true
          type:
            - number
            - 'null'
          format: double
          description: Max leverage selected for isolated position.
        crossMaxLeverage:
          x-kfOnly: true
          type:
            - number
            - 'null'
          format: double
          description: >-
            Max leverage selected for a cross position: its initial margin is
            floored at

            `1 / crossMaxLeverage` while it stays cross margined. Absent when
            the position is

            uncapped or isolated.
        greeks:
          $ref: '#/components/schemas/OptionGreeks'
          x-kfOnly: true
          x-internalOnly: true
          description: The position Greeks, if this is an option position.
      required:
        - symbol
        - side
        - size
        - price
        - unrealizedPnl
        - unrealizedFunding
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
    OptionGreeks:
      description: >-
        Option Greeks.


        On ticker REST responses, the ticker websocket feed, and FIX ticker
        market data, each value is

        rounded to 8 decimal places using half-even rounding. Values smaller
        than `1e-8` round to `0`.

        Other resources keep full precision.
      type: object
      properties:
        iv:
          type: number
          format: double
          description: >-
            The implied volatility. Displays an IV of -1.0 whenever the IV is
            impossible to calculate or outside of the bounds allowed.
        delta:
          type: number
          format: double
        gamma:
          format: double
          type:
            - number
            - 'null'
        vega:
          format: double
          type:
            - number
            - 'null'
        theta:
          format: double
          type:
            - number
            - 'null'
        rho:
          format: double
          type:
            - number
            - 'null'
      required:
        - iv
        - delta
        - gamma
        - vega
        - theta
        - rho
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
    OpenPositionsSuccessExample:
      value:
        result: success
        openPositions:
          - side: short
            symbol: PI_XBTUSD
            price: 9392.749993345933
            size: 10000
            unrealizedPnl: -607250.006654067
            unrealizedFunding: 0.00001045432180096817
          - side: long
            symbol: FI_XBTUSD_201225
            price: 9399.749966754434
            size: 20000
            unrealizedPnl: 1199500.664911316
            unrealizedFunding: null
          - side: long
            symbol: PF_DEFIUSD
            price: 570
            size: 1
            unrealizedPnl: 12.34
            unrealizedFunding: -0.0073428045972263895
            pnlCurrency: BTC
            maxFixedLeverage: 5
        serverTime: '2020-07-22T14:39:12.376Z'
    OpenPositionsFailureExample:
      value:
        result: error
        serverTime: '2016-02-25T09:45:53.818Z'
        error: apiLimitExceeded
  responses:
    CancelOnly:
      description: The venue is cancel-only.
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
