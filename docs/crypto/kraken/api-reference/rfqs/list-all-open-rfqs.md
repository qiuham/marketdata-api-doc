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
source_url: 'https://docs.kraken.com/api-reference/rfqs/list-all-open-rfqs'
updated_at: 2026-11-13
---

# List all open RFQs

> Retrieve all currently open RFQs



## OpenAPI

````yaml /openapi/futures-rest.yaml get /rfqs
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
  /rfqs:
    get:
      tags:
        - RFQs
      summary: List all open RFQs
      description: Retrieve all currently open RFQs
      operationId: getOpenRfqs
      responses:
        '200':
          description: All open RFQs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OpenRfqsResponse'
        '404':
          description: RFQ feature is not enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    OpenRfqsResponse:
      allOf:
        - $ref: '#/components/schemas/ResponseJson'
        - type: object
          properties:
            rfqs:
              type: array
              items:
                $ref: '#/components/schemas/OpenRfq'
          required:
            - rfqs
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
    ResponseJson:
      type: object
      properties:
        result:
          type: string
          enum:
            - success
        serverTime:
          type: string
          format: date-time
      required:
        - result
        - serverTime
    OpenRfq:
      type: object
      properties:
        uid:
          type: string
          format: uuid
          description: The unique identifier for this RFQ
        expiry:
          type: string
          format: date-time
          description: The time at which this RFQ expires
        markPrice:
          type: number
          format: double
          description: The reference price of the RFQ
        legs:
          type: array
          items:
            $ref: '#/components/schemas/OpenRfqPosition'
          description: The positions associated with the RFQ
        status:
          type: string
          enum:
            - open
            - expired
            - cancelled
            - filled_bid_side
            - filled_ask_side
          description: >-
            Lifecycle status of the RFQ. `open` means the RFQ is still accepting
            offers. `expired` and `cancelled` indicate it closed without a
            trade. `filled_bid_side` and `filled_ask_side` indicate the
            requestor accepted an offer on the corresponding side.
      required:
        - uid
        - expiry
        - markPrice
        - legs
        - status
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
    OpenRfqPosition:
      type: object
      properties:
        symbol:
          type: string
          description: The symbol of the derivatives contract
        size:
          type: number
          format: double
          description: The size of the position
        markPrice:
          type: number
          format: double
          description: The current mark price of the market
      required:
        - symbol
        - size
        - markPrice

````
