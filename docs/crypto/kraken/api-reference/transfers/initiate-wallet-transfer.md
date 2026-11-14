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
source_url: 'https://docs.kraken.com/api-reference/transfers/initiate-wallet-transfer'
updated_at: 2026-11-13
---

# Initiate wallet transfer

> This endpoint allows you to transfer funds between two margin accounts with the same
collateral currency, between a margin account and your cash account, or between any of
your Futures wallets and your Kraken Spot wallet.

Name the Spot wallet `spot` in `fromAccount` or `toAccount`. A transfer to or from Spot
settles before the response is sent, requires an API key with the withdrawal permission,
costs 100 rate-limit units instead of 10, and is only available to accounts linked to a
Kraken account. The assets it may move, with the minimum and maximum amounts, are listed
by `GET /transfer/assets`.

A transfer the venue rejects returns an error response such as `insufficientFunds`,
`invalidAmount`, `invalidUnit`, `invalidCurrency` or `transferFailed`.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /transfer
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
  /transfer:
    post:
      tags:
        - Transfers
      summary: Initiate wallet transfer
      description: >-
        This endpoint allows you to transfer funds between two margin accounts
        with the same

        collateral currency, between a margin account and your cash account, or
        between any of

        your Futures wallets and your Kraken Spot wallet.


        Name the Spot wallet `spot` in `fromAccount` or `toAccount`. A transfer
        to or from Spot

        settles before the response is sent, requires an API key with the
        withdrawal permission,

        costs 100 rate-limit units instead of 10, and is only available to
        accounts linked to a

        Kraken account. The assets it may move, with the minimum and maximum
        amounts, are listed

        by `GET /transfer/assets`.


        A transfer the venue rejects returns an error response such as
        `insufficientFunds`,

        `invalidAmount`, `invalidUnit`, `invalidCurrency` or `transferFailed`.
      operationId: transfer
      parameters:
        - description: >-
            The wallet (cash or margin account, or `spot` for the Kraken Spot
            wallet) from which

            funds should be debited
          name: fromAccount
          in: query
          required: true
          schema:
            type: string
            example: fi_ethusd
        - description: >-
            The wallet (cash or margin account, or `spot` for the Kraken Spot
            wallet) to which

            funds should be credited
          name: toAccount
          in: query
          required: true
          schema:
            type: string
            example: flex
        - description: The currency unit to transfer
          name: unit
          in: query
          required: true
          schema:
            type: string
            example: eth
        - description: The amount to transfer
          name: amount
          in: query
          required: true
          schema:
            type: number
            format: decimal
            exclusiveMinimum: 0
            example: 0.1
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key: []
          authent: []
        - withdrawal-api-key: []
          authent: []
components:
  schemas:
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
    withdrawal-api-key:
      type: apiKey
      description: |
        **Withdrawal** API key with **full** access
      in: header
      name: APIKey
      x-inlineDescription: true

````
