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
source_url: 'https://docs.kraken.com/api-reference/account-information/calculate-portfolio-margin-pnl-and-greeks'
updated_at: 2026-11-13
---

# Calculate portfolio margin, pnl and greeks

> For a given portfolio of balances and positions (futures and options), calculate the
margin requirements, pnl and option greeks.

Note: This is currently available exclusively in the Kraken pre-prod environments.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /portfolio-margining/simulate
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
  /portfolio-margining/simulate:
    post:
      tags:
        - Account Information
      summary: Calculate portfolio margin, pnl and greeks
      description: >-
        For a given portfolio of balances and positions (futures and options),
        calculate the

        margin requirements, pnl and option greeks.


        Note: This is currently available exclusively in the Kraken pre-prod
        environments.
      operationId: simulatePortfolio
      parameters:
        - description: Request body as a JSON string
          name: json
          in: query
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PortfolioSimulationRequest'
      responses:
        '200':
          description: Simulated portfolio calculations
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success Response
                    allOf:
                      - $ref: '#/components/schemas/PortfolioSimulationResponse'
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key-read-only: []
          authent: []
      servers:
        - url: https://demo-futures.kraken.com/derivatives/api/v3
components:
  schemas:
    PortfolioSimulationRequest:
      type: object
      properties:
        positions:
          type: array
          maxItems: 500
          items:
            $ref: '#/components/schemas/PortfolioSimulationPosition'
      required:
        - positions
    PortfolioSimulationResponse:
      type: object
      properties:
        maintenanceMargin:
          type: number
          format: double
        initialMargin:
          type: number
          format: double
        pnl:
          type: number
          format: double
        portfolioMarginBreakdown:
          $ref: '#/components/schemas/PortfolioMarginBreakdown'
        greeks:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/OptionGreeks'
      required:
        - maintenanceMargin
        - initialMargin
        - pnl
        - portfolioMarginBreakdown
        - greeks
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
    PortfolioSimulationPosition:
      type: object
      properties:
        instrument:
          type: string
          example: PF_BTCUSD
        size:
          $ref: '#/components/schemas/DecimalDouble'
        entryPrice:
          $ref: '#/components/schemas/DecimalDouble'
      required:
        - instrument
        - size
        - entryPrice
    PortfolioMarginBreakdown:
      description: Breakdown of components that make up the portfolio margin calculation.
      type: object
      properties:
        totalCrossAssetNettedMarketRisk:
          type: number
          format: double
          deprecated: true
          description: >-
            **DEPRECATED** - Always equal to `totalMarketRisk`. Cross-asset
            netting

            was removed. This field will be removed in a future release.
        totalMarketRisk:
          type: number
          format: double
        totalScenarioPnls:
          oneOf:
            - type: array
              items:
                type: number
                format: double
            - type: 'null'
        totalAbsoluteOptionPositionDeltaNotional:
          type: number
          format: double
        netPortfolioDelta:
          type: number
          format: double
        totalPremium:
          type: number
          format: double
        isBuyOnly:
          type: boolean
        futuresMaintenanceMargin:
          type: number
          format: double
      required:
        - totalCrossAssetNettedMarketRisk
        - totalMarketRisk
        - totalScenarioPnls
        - totalAbsoluteOptionPositionDeltaNotional
        - netPortfolioDelta
        - totalPremium
        - isBuyOnly
        - futuresMaintenanceMargin
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
    DecimalDouble:
      type: number
      format: double
      example: 12.03532
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
