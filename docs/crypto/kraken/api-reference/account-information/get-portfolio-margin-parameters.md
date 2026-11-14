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
source_url: 'https://docs.kraken.com/api-reference/account-information/get-portfolio-margin-parameters'
updated_at: 2026-11-13
---

# Get portfolio margin parameters

> Retrieve current portfolio margin calculation parameters.

Also includes user specific limits related to options trading.

Note: This is currently available exclusively in the Kraken pre-prod environments.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /portfolio-margining/parameters
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
  /portfolio-margining/parameters:
    get:
      tags:
        - Account Information
      summary: Get portfolio margin parameters
      description: >-
        Retrieve current portfolio margin calculation parameters.


        Also includes user specific limits related to options trading.


        Note: This is currently available exclusively in the Kraken pre-prod
        environments.
      operationId: getPortfolioMarginingParameters
      responses:
        '200':
          description: Portfolio margining parameters
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success Response
                    allOf:
                      - $ref: '#/components/schemas/PortfolioMarginingParameters'
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key-read-only: []
          authent: []
      servers:
        - url: https://demo-futures.kraken.com/derivatives/api/v3
components:
  schemas:
    PortfolioMarginingParameters:
      type: object
      properties:
        crossAssetNettingFactor:
          $ref: '#/components/schemas/DecimalDouble'
          deprecated: true
          description: >-
            **DEPRECATED** - Always 0. Cross-asset netting was removed. This
            field

            will be removed in a future release.
        extremePriceShockMultiplier:
          $ref: '#/components/schemas/DecimalDouble'
        volShockMultiplicationFactor:
          $ref: '#/components/schemas/DecimalDouble'
        volShockExponentFactor:
          $ref: '#/components/schemas/DecimalDouble'
        optionExpiryTimeShockHours:
          type: number
          format: uint64
        optionsInitialMarginFactor:
          $ref: '#/components/schemas/DecimalDouble'
        totalOptionOrdersConsideredInInitialMarginCalc:
          type: number
          format: uint64
        priceShockLevels:
          type: array
          items:
            $ref: '#/components/schemas/DecimalDouble'
        optionsUserLimits:
          $ref: '#/components/schemas/OptionsUserLimits'
      required:
        - crossAssetNettingFactor
        - extremePriceShockMultiplier
        - volShockMultiplicationFactor
        - volShockExponentFactor
        - optionExpiryTimeShockHours
        - optionsInitialMarginFactor
        - totalOptionOrdersConsideredInInitialMarginCalc
        - priceShockLevels
        - optionsUserLimits
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
    DecimalDouble:
      type: number
      format: double
      example: 12.03532
    OptionsUserLimits:
      type: object
      properties:
        maxNetPositionDelta:
          $ref: '#/components/schemas/DecimalDouble'
        limitsPerBaseCurrency:
          description: User limits per option contract base currency
          type: object
          additionalProperties:
            $ref: '#/components/schemas/OptionsUserLimitsPerBaseCurrency'
      required:
        - maxNetPositionDelta
        - limitsPerBaseCurrency
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
    OptionsUserLimitsPerBaseCurrency:
      type: object
      properties:
        maxTotalPositionSize:
          $ref: '#/components/schemas/DecimalDouble'
        maxTotalOpenOrdersSize:
          $ref: '#/components/schemas/DecimalDouble'
      required:
        - maxTotalPositionSize
        - maxTotalOpenOrdersSize
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
