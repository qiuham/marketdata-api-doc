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
source_url: 'https://docs.kraken.com/api-reference/assignment-program/add-assignment-preference'
updated_at: 2026-11-13
---

# Add assignment preference

> This endpoint adds an assignment program preference



## OpenAPI

````yaml /openapi/futures-rest.yaml post /assignmentprogram/add
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
  /assignmentprogram/add:
    post:
      tags:
        - Assignment Program
      summary: Add assignment preference
      description: This endpoint adds an assignment program preference
      operationId: addAssignmentProgram
      parameters:
        - description: >-
            Type of contract for the assignment program preference. Options can
            be found in the 'accounts' structure in the Get Wallets /accounts
            response
          name: contractType
          in: query
          required: true
          schema:
            type: string
        - description: >-
            A specific contract for this assignment program preference. Required
            for "flex" contracts if base/quote currencies are not included.
          name: contract
          in: query
          required: false
          schema:
            type: string
          x-kfOnly: true
        - description: The maximum size for an assignment
          name: maxSize
          in: query
          required: false
          schema:
            type: number
        - description: The maximum position
          name: maxPosition
          in: query
          required: false
          schema:
            type: number
        - description: Accept to take long positions
          name: acceptLong
          in: query
          required: true
          schema:
            type: boolean
        - description: Accept to take short positions
          name: acceptShort
          in: query
          required: true
          schema:
            type: boolean
        - description: When is the program preference valid
          name: timeFrame
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/AssignmentPreferenceTimeFrame'
        - description: enabled assignment
          name: enabled
          in: query
          required: true
          schema:
            type: boolean
        - description: >-
            If creating a currency pair level assignment participant, this
            specifies the base currency. \

            Must be specified alongside the quote currency.
          name: baseCurrency
          in: query
          required: false
          schema:
            type: string
          x-internalOnly: true
        - description: >-
            If creating a currency pair level assignment participant, this
            specifies the quote currency. \

            Must be specified alongside the base currency.
          name: quoteCurrency
          in: query
          required: false
          schema:
            type: string
          x-internalOnly: true
        - description: Specify max open position notional for wallet type
          name: cashAccountOpenPositionMaxNotional
          in: query
          required: false
          schema:
            type: number
          x-internalOnly: true
          x-kfOnly: true
        - description: >-
            The minimum profitability per assignment for long positions, in
            integer basis points. \

            Participants with a lower minimum receive assignments first. If
            omitted, the platform

            default applies.
          name: minimumProfitabilityPerAssignmentLongBps
          in: query
          required: false
          schema:
            type: integer
        - description: >-
            The minimum profitability per assignment for short positions, in
            integer basis points. \

            Participants with a lower minimum receive assignments first. If
            omitted, the platform

            default applies.
          name: minimumProfitabilityPerAssignmentShortBps
          in: query
          required: false
          schema:
            type: integer
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success Response
                    allOf:
                      - $ref: '#/components/schemas/AssignmentParticipantDetails'
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    AssignmentPreferenceTimeFrame:
      type: string
      enum:
        - WEEKDAYS
        - WEEKEND
        - ALL
      x-exhaustive: true
    AssignmentParticipantDetails:
      type: object
      properties:
        id:
          type: number
        participant:
          $ref: '#/components/schemas/AssignmentParticipantJson'
      required:
        - id
        - participant
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
    AssignmentParticipantJson:
      type: object
      properties:
        contractType:
          type: string
        contract:
          type:
            - string
            - 'null'
        maxSize:
          format: double
          type:
            - number
            - 'null'
        maxPosition:
          format: double
          type:
            - number
            - 'null'
        acceptLong:
          type: boolean
        acceptShort:
          type: boolean
        timeFrame:
          $ref: '#/components/schemas/AssignmentPreferenceTimeFrame'
        enabled:
          type: boolean
        cashAccountOpenPositionMaxNotional:
          format: double
          type:
            - number
            - 'null'
          x-internalOnly: true
        baseCurrency:
          type:
            - string
            - 'null'
          x-internalOnly: true
        quoteCurrency:
          type:
            - string
            - 'null'
          x-internalOnly: true
        minimumProfitabilityPerAssignmentLongBps:
          description: >-
            Minimum profitability per assignment for long positions, in integer
            basis points.

            Participants with a lower minimum receive assignments first. If
            omitted, the platform

            default applies.
          format: int32
          type:
            - integer
            - 'null'
        minimumProfitabilityPerAssignmentShortBps:
          description: >-
            Minimum profitability per assignment for short positions, in integer
            basis points.

            Participants with a lower minimum receive assignments first. If
            omitted, the platform

            default applies.
          format: int32
          type:
            - integer
            - 'null'
      required:
        - contractType
        - acceptLong
        - acceptShort
        - timeFrame
        - enabled
      example:
        contractType: flex
        contract: PF_BTCUSD
        maxPosition: 10
        maxSize: 10
        acceptLong: true
        acceptShort: true
        timeFrame: WEEKDAYS
        enabled: true
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
