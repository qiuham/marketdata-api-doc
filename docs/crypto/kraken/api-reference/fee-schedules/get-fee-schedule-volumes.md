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
source_url: 'https://docs.kraken.com/api-reference/fee-schedules/get-fee-schedule-volumes'
updated_at: 2026-11-13
---

# Get fee schedule volumes

> **DEPRECATED** — Effective 2026-06-22, the volumes and fee schedule
associations returned by this endpoint no longer reflect the fees
actually charged on Futures trades. Futures fee calculation has been
migrated to a centralised Kraken fee service.

To determine the fee rate applied to your trades, use the Spot
[`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)
endpoint authenticated with a Spot API key.

---

Returns your fee schedule volumes for each fee schedule.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /feeschedules/volumes
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
  /feeschedules/volumes:
    get:
      tags:
        - Fee Schedules
      summary: Get fee schedule volumes
      description: >-
        **DEPRECATED** — Effective 2026-06-22, the volumes and fee schedule

        associations returned by this endpoint no longer reflect the fees

        actually charged on Futures trades. Futures fee calculation has been

        migrated to a centralised Kraken fee service.


        To determine the fee rate applied to your trades, use the Spot

        [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)

        endpoint authenticated with a Spot API key.


        ---


        Returns your fee schedule volumes for each fee schedule.
      operationId: getUserFeeScheduleVolumesV3
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
                          volumesByFeeSchedule:
                            $ref: '#/components/schemas/FeeScheduleVolumes'
                            description: List containing the 30-day volume.
                        required:
                          - volumesByFeeSchedule
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/FeeSchedulesValuesExample'
      deprecated: true
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    FeeScheduleVolumes:
      type: object
      deprecated: true
      description: >-
        **DEPRECATED** — Effective 2026-06-22, fee schedule volumes are no

        longer authoritative for fees charged on Futures trades. See the Spot

        [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)

        endpoint.


        The 30-day volume for your account.
      additionalProperties:
        type: number
      example:
        d46c2190-81e3-4370-a333-424f24387829: 10
        7fc4d7c0-464f-4029-a9bb-55856d0c5247: 10
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
    FeeSchedulesValuesExample:
      value:
        result: success
        serverTime: '2016-02-25T09:45:53.818Z'
        volumesByFeeSchedule:
          eef90775-995b-4596-9257-0917f6134766: 53823
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
