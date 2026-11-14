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
source_url: 'https://docs.kraken.com/api-reference/rfqs/list-open-offers-on-open-rfqs'
updated_at: 2026-11-13
---

# List open offers on open RFQs

> Retrieve all open offers for the account on currently open RFQs



## OpenAPI

````yaml /openapi/futures-rest.yaml get /rfqs/open-offers
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
  /rfqs/open-offers:
    get:
      tags:
        - RFQs
      summary: List open offers on open RFQs
      description: Retrieve all open offers for the account on currently open RFQs
      operationId: getOpenRfqOffers
      responses:
        '200':
          description: Open Offers
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OpenRfqOffersResponse'
        '404':
          description: RFQ feature is not enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    OpenRfqOffersResponse:
      allOf:
        - $ref: '#/components/schemas/ResponseJson'
        - type: object
          properties:
            offers:
              type: array
              items:
                $ref: '#/components/schemas/OpenRfqOffer'
          required:
            - offers
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
    OpenRfqOffer:
      type: object
      properties:
        uid:
          type: string
          format: uuid
          description: Unique identifier for the offer
        rfqUid:
          type: string
          format: uuid
          description: Unique identifier for the RFQ
        placementDate:
          type: string
          format: date-time
          description: The date and time when the offer was placed
        lastUpdateDate:
          type: string
          format: date-time
          description: The last update date and time of the offer
        bid:
          type: string
          format: decimal
          description: The bid price, if available
        ask:
          type: string
          format: decimal
          description: The ask price, if available
        bidSide:
          type: array
          items:
            $ref: '#/components/schemas/RfqLegOffer'
          description: Per-leg bid pricing. Null when using package-level pricing.
        askSide:
          type: array
          items:
            $ref: '#/components/schemas/RfqLegOffer'
          description: Per-leg ask pricing. Null when using package-level pricing.
        status:
          type: string
          enum:
            - open
            - expired
            - cancelled
            - filled_bid_side
            - filled_ask_side
          description: >-
            Lifecycle status of the parent RFQ at the time this offer is being
            read. `open` is returned from the `/open-offers` endpoint. The other
            values are returned from `/closed-offers`.
      required:
        - uid
        - rfqUid
        - placementDate
        - lastUpdateDate
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
    RfqLegOffer:
      type: object
      properties:
        tradeable:
          type: string
          description: The symbol of the derivatives contract
        price:
          type: number
          format: double
          description: The price for this leg
      required:
        - tradeable
        - price
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
