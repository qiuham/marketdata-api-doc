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
source_url: 'https://docs.kraken.com/api-reference/transfers/initiate-withdrawal-to-spot-wallet'
updated_at: 2026-11-13
---

# Initiate withdrawal to Spot wallet

> Deprecated: use `POST /transfer` with `toAccount=spot` instead.

This endpoint allows you to request to withdraw digital assets to your Kraken Spot wallet.

Wallet names can be found in the 'accounts' structure in the Get Wallets /accounts response.

A withdrawal the trading engine rejects returns an error response with `insufficientFunds`,
`invalidAmount`, or `invalidUnit`.

Once the venue settles withdrawals as immediate balance transfers, the funds have reached
the Spot wallet when the response is sent and there is no transfer to poll: `uid` is then
the nil UUID `00000000-0000-0000-0000-000000000000`.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /withdrawal
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
  /withdrawal:
    post:
      tags:
        - Transfers
      summary: Initiate withdrawal to Spot wallet
      description: >-
        Deprecated: use `POST /transfer` with `toAccount=spot` instead.


        This endpoint allows you to request to withdraw digital assets to your
        Kraken Spot wallet.


        Wallet names can be found in the 'accounts' structure in the Get Wallets
        /accounts response.


        A withdrawal the trading engine rejects returns an error response with
        `insufficientFunds`,

        `invalidAmount`, or `invalidUnit`.


        Once the venue settles withdrawals as immediate balance transfers, the
        funds have reached

        the Spot wallet when the response is sent and there is no transfer to
        poll: `uid` is then

        the nil UUID `00000000-0000-0000-0000-000000000000`.
      operationId: withdrawal
      parameters:
        - description: The digital asset that shall be withdrawn back to spot wallet.
          name: currency
          in: query
          required: true
          schema:
            type: string
            example: eth
        - description: The amount of currency that shall be withdrawn back to spot wallet.
          name: amount
          in: query
          required: true
          schema:
            type: number
            format: decimal
            exclusiveMinimum: 0
            example: 0.1
        - description: >-
            The wallet from which the funds shall be withdrawn back to spot
            wallet. Default is

            "cash" wallet.
          name: sourceWallet
          in: query
          required: false
          schema:
            type: string
            example: flex
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: '#/components/schemas/WithdrawalResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  value:
                    uid: 9053db5f-0d5e-48dd-b606-a5c92576b706
                    result: success
                    serverTime: '2022-06-28T14:48:58.711Z'
                failure:
                  $ref: '#/components/examples/WithdrawalFailureExample'
                insufficientFunds:
                  value:
                    result: error
                    serverTime: '2022-06-28T14:48:58.711Z'
                    error: insufficientFunds
      deprecated: true
      security:
        - withdrawal-api-key: []
          authent: []
components:
  schemas:
    WithdrawalResponse:
      description: Withdrawal initiated
      allOf:
        - type: object
          properties:
            uid:
              description: >-
                Withdrawal/transfer reference while withdrawals go through the
                legacy

                cross-exchange transfer system; the nil UUID once they settle as
                immediate balance

                transfers, which leave nothing to poll
              type: string
          required:
            - uid
        - $ref: '#/components/schemas/SuccessResponse'
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
    SuccessResponse:
      allOf:
        - $ref: '#/components/schemas/ResultSuccess'
        - $ref: '#/components/schemas/ServerTime'
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
  examples:
    WithdrawalFailureExample:
      value:
        result: error
        serverTime: '2019-05-15T09:24:16.968Z'
        error: Unavailable
  securitySchemes:
    withdrawal-api-key:
      type: apiKey
      description: |
        **Withdrawal** API key with **full** access
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
