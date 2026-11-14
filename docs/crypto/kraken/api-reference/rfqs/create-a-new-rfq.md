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
source_url: 'https://docs.kraken.com/api-reference/rfqs/create-a-new-rfq'
updated_at: 2026-11-13
---

# Create a new RFQ

> Create a new RFQ for the authenticated account.

The `json` query or form parameter is a JSON-encoded object with:
- `legs` (required): array of `{ "tradeable", "size" }` (max 100). Duplicate tradeables
  are rejected.
- `expiry` (optional): RFC 3339 datetime. The server applies a default duration if omitted.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /rfqs/open-rfqs
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
  /rfqs/open-rfqs:
    post:
      tags:
        - RFQs
      summary: Create a new RFQ
      description: >-
        Create a new RFQ for the authenticated account.


        The `json` query or form parameter is a JSON-encoded object with:

        - `legs` (required): array of `{ "tradeable", "size" }` (max 100).
        Duplicate tradeables
          are rejected.
        - `expiry` (optional): RFC 3339 datetime. The server applies a default
        duration if omitted.
      operationId: createUserRfq
      parameters:
        - description: >-
            JSON-encoded RFQ creation request. Required `legs` is an array of
            objects with

            `tradeable` (contract symbol) and `size`. Optional `expiry` is an
            RFC 3339 datetime.
          name: json
          in: query
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RfqCreationRequest'
      responses:
        '200':
          description: RFQ creation result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RfqCreationResponse'
        '403':
          $ref: '#/components/responses/ContractAccessForbidden'
        '404':
          description: RFQ feature is not enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key: []
          authent: []
components:
  schemas:
    RfqCreationRequest:
      type: object
      required:
        - legs
      properties:
        legs:
          type: array
          maxItems: 100
          items:
            $ref: '#/components/schemas/RfqLeg'
          description: >-
            The legs of the RFQ. Each entry is a contract symbol and size.
            Duplicate `tradeable`

            values are rejected.
        expiry:
          type: string
          format: date-time
          description: >-
            The requested expiry time for the RFQ. Defaults to a server-defined
            duration if omitted.
      example:
        legs:
          - tradeable: PI_XBTUSD
            size: 1
        expiry: '2026-09-14T15:00:00Z'
    RfqCreationResponse:
      oneOf:
        - $ref: '#/components/schemas/RfqCreationSuccessResponse'
        - $ref: '#/components/schemas/RfqCreationFailureResponse'
      discriminator:
        propertyName: status
        mapping:
          placed: '#/components/schemas/RfqCreationSuccessResponse'
          failed: '#/components/schemas/RfqCreationFailureResponse'
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
    RfqLeg:
      type: object
      required:
        - tradeable
        - size
      properties:
        tradeable:
          type: string
          description: The symbol of the derivatives contract
        size:
          type: number
          format: double
          description: The size of the leg
    RfqCreationSuccessResponse:
      allOf:
        - $ref: '#/components/schemas/ResponseJson'
        - type: object
          properties:
            rfqUid:
              type: string
              format: uuid
          required:
            - rfqUid
    RfqCreationFailureResponse:
      allOf:
        - $ref: '#/components/schemas/ResponseJson'
        - type: object
          properties:
            reason:
              type: string
              enum:
                - insufficientMargin
                - maxPositionExceeded
                - wouldCauseLiquidation
                - fixedLeverageTooHigh
                - orderError
                - symbolNotFound
                - invalidExpiry
                - invalidQuantity
                - marketRestricted
                - noLegsSpecified
                - accountNotFound
                - mixedCurrencyPairs
                - tooManyNonOptionLegs
                - noOptionLegs
                - tooManyOpenRfqs
                - tooManyLegs
                - expiryTooShort
                - duplicateLegs
                - accountAuctioning
          required:
            - reason
    _schemas_ErrorResponse:
      type: object
      properties:
        result:
          type: string
          enum:
            - error
        serverTime:
          type: string
          format: date-time
        errors:
          type: array
          items:
            $ref: '#/components/schemas/_schemas_Error'
      required:
        - result
        - serverTime
        - errors
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
    _schemas_Error:
      type: object
      properties:
        code:
          type:
            - number
            - 'null'
        message:
          type: string
      required:
        - code
        - message
  responses:
    ContractAccessForbidden:
      x-summary: Contract access forbidden
      description: |-
        Account is not permitted to perform the requested trading operation.

        - Error `code`: 95
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/_schemas_ErrorResponse'
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
