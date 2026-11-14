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
source_url: 'https://docs.kraken.com/api-reference/trading-settings/set-the-off-book-max-leverage-cap'
updated_at: 2026-11-13
---

# Set the off-book max leverage cap

> Sets the account-level off-book maximum leverage cap for the authenticated master account
and returns the stored value.

The cap limits the effective leverage (gross open-position notional / margin equity) the
account is willing to reach through off-book fills — liquidation assignments and RFQ offer
fills. Book (maker/taker) orders are never affected.

Setting the cap to `0` leaves no leverage budget, so the account takes no
exposure-increasing off-book fill at all: it is the single switch to opt out of assignments
and RFQ fills without withdrawing each assignment preference individually. Fills that
reduce the account's gross open-position notional still go through, so opting out never
traps the account in its existing exposure.

Only master accounts may call this endpoint. Calling it can result in the following error
codes:


  invalidArgument: `maxLeverage` is missing or not a number


  rfqAssignmentMaxLeverageOutOfBounds: `maxLeverage` is outside `[0, 100]`, or has more than 2 decimal places


  rfqAssignmentMaxLeverageDisabled: the off-book max leverage feature is not enabled



## OpenAPI

````yaml /openapi/futures-rest.yaml put /rfq-assignment/max-leverage
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
  /rfq-assignment/max-leverage:
    put:
      tags:
        - Trading Settings
      summary: Set the off-book max leverage cap
      description: >-
        Sets the account-level off-book maximum leverage cap for the
        authenticated master account

        and returns the stored value.


        The cap limits the effective leverage (gross open-position notional /
        margin equity) the

        account is willing to reach through off-book fills — liquidation
        assignments and RFQ offer

        fills. Book (maker/taker) orders are never affected.


        Setting the cap to `0` leaves no leverage budget, so the account takes
        no

        exposure-increasing off-book fill at all: it is the single switch to opt
        out of assignments

        and RFQ fills without withdrawing each assignment preference
        individually. Fills that

        reduce the account's gross open-position notional still go through, so
        opting out never

        traps the account in its existing exposure.


        Only master accounts may call this endpoint. Calling it can result in
        the following error

        codes:


          invalidArgument: `maxLeverage` is missing or not a number


          rfqAssignmentMaxLeverageOutOfBounds: `maxLeverage` is outside `[0, 100]`, or has more than 2 decimal places


          rfqAssignmentMaxLeverageDisabled: the off-book max leverage feature is not enabled
      operationId: updateRfqAssignmentMaxLeverage
      parameters:
        - description: >-
            The off-book max leverage cap to set. Must be at least 0 and at most
            100, with at most

            2 decimal places. `0` blocks all exposure-increasing off-book fills.
          name: maxLeverage
          in: query
          required: true
          schema:
            type: number
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success Response
                    allOf:
                      - type: object
                        properties:
                          maxLeverage:
                            type:
                              - number
                              - 'null'
                            description: The stored off-book max leverage cap.
                        required:
                          - maxLeverage
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/GetRfqAssignmentMaxLeverageExample'
      security:
        - general-api-key: []
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
  examples:
    GetRfqAssignmentMaxLeverageExample:
      x-kfOnly: true
      value:
        result: success
        serverTime: '2022-06-28T15:01:12.762Z'
        maxLeverage: 10
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
