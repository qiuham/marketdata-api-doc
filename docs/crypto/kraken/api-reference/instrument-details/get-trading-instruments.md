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
source_url: 'https://docs.kraken.com/api-reference/instrument-details/get-trading-instruments'
updated_at: 2026-11-13
---

# Get trading instruments

> Returns specifications for all currently accessible markets and indices.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /trading/instruments
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
  /trading/instruments:
    get:
      tags:
        - Instrument Details
      summary: Get trading instruments
      description: Returns specifications for all currently accessible markets and indices.
      operationId: getTradingInstruments
      parameters:
        - $ref: '#/components/parameters/ContractTypesQuery'
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
                          instruments:
                            type: array
                            items:
                              $ref: '#/components/schemas/InstrumentAuthenticated'
                            description: >-
                              A list containing structures for each available
                              instrument. The list

                              is in no particular order.
                        required:
                          - instruments
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  parameters:
    ContractTypesQuery:
      description: >-
        Contract type(s) to return statuses for.


        By default, includes all futures instrument types.


        Multi-value example:
        `?contractType=futures_inverse&contractType=futures_vanilla`
      name: contractType
      in: query
      required: false
      style: form
      explode: true
      schema:
        type: array
        items:
          type: string
          enum:
            - futures_inverse
            - futures_vanilla
            - flexible_futures
            - options
            - all
  schemas:
    InstrumentAuthenticated:
      type: object
      properties:
        fundingRateCoefficient:
          $ref: '#/components/schemas/DecimalDouble'
          description: |-
            Funding rate coefficient.

            Only present for perpetual markets.
        lastTradingTime:
          description: |-
            Market expiry date-time (UTC).

            Only present for fixed maturity markets.
          type: string
          format: date-time
        minimumTradeSize:
          $ref: '#/components/schemas/DecimalDouble'
          description: >-
            TODO: Not populated for any markets (at time of writing in Apr
            2025).
        impactMidSize:
          $ref: '#/components/schemas/DecimalDouble'
          description: Book depth used to calculate (impact) mid prices.
        maxPositionSize:
          $ref: '#/components/schemas/DecimalDouble'
          description: Market-wide position size limit.
        maxOpenInterestUsd:
          $ref: '#/components/schemas/DecimalDouble'
          description: >-
            USD-denominated hard cap on market-wide open interest. Only present
            when the

            market has a cap configured.
        maxOpenInterestShare:
          $ref: '#/components/schemas/DecimalDouble'
          description: >-
            Largest share of market-wide open interest one user (master plus
            every subaccount)

            may hold on either side, resolved from the market's own limit or the
            platform default.

            Only present when a share applies to the market: a market with
            neither a

            maxOpenInterestUsd nor a maxPositionSize is unlimited.
        openingDate:
          description: Date-time (UTC) that market was created.
          type: string
          format: date-time
        marginLevels:
          description: |-
            Margin schedule applicable to logged-in account.

            Only present for futures markets.
          type: array
          items:
            $ref: '#/components/schemas/_schemas_MarginLevel'
        maxRelativeFundingRate:
          $ref: '#/components/schemas/DecimalDouble'
          description: |-
            Maximum relative funding rate.

            Only present for perpetual markets.
        minRelativeFundingRate:
          $ref: '#/components/schemas/DecimalDouble'
          description: >-
            Minimum relative funding rate (funding-rate floor). May be negative.


            Only present for pre-IPO perpetual markets that have a floor
            configured. Equal minimum

            and maximum rates mean the funding rate is fixed.
        symbol:
          $ref: '#/components/schemas/MarketSymbol'
        pair:
          description: Asset pair (uppercase, colon separated).
          type: string
          example: BTC:USD
        base:
          description: Base asset (uppercase).
          type: string
          example: BTC
        quote:
          description: Quote asset (uppercase).
          type: string
          example: USD
        tickSize:
          $ref: '#/components/schemas/DecimalDouble'
          description: Minimum order price increment.
        type:
          description: Market type.
          type: string
          enum:
            - futures_inverse
            - futures_vanilla
            - flexible_futures
            - options
        underlying:
          description: |-
            Underlying index code.

            Only present for single-collateral markets.
          type: string
        isin:
          description: International Securities Identification Number (ISIN).
          type:
            - string
            - 'null'
        contractValueTradePrecision:
          description: >-
            Minimum order quantity increment.


            E.g., a trade precision of 2 means order quantities are not allowed
            to be more precise

            than the hundredth decimal place (0.01).


            These values can be negative to specify quantity increments of 10
            (-1), 100 (-2), etc.
          type: integer
        description:
          description: |-
            Free-text market description for display and search.

            Only present when configured for the market.
          type: string
        makerProtectionMillis:
          description: >-
            Maker protection window in milliseconds configured for this market:
            order placements

            and edits that would take liquidity from the book as they arrive are
            held for this long

            before matching, giving resting maker orders time to react. A
            placement or edit that

            would rest, and any post-only order, is processed at once.


            Within a batch order each liquidity-taking instruction is held on
            its own; every other

            instruction, cancels included, is processed immediately wherever it
            appears.


            Only present when maker protection is configured for this market.
          type: integer
          format: int64
        postOnly:
          description: True if market is in post-only mode.
          type: boolean
        suspended:
          description: >-
            True if the market is not accepting orders (suspended, pending
            settlement or

            inactive). False for active and post-only markets.
          type: boolean
        feeScheduleUid:
          deprecated: true
          description: >-
            **DEPRECATED** — Effective 2026-06-22, this field no longer
            corresponds

            to the fee schedule used for fee calculation. Use the Spot

            [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)

            endpoint authenticated with a Spot API key to determine your fee
            rate.


            Fee schedule UID.
          type: string
          format: uuid
        optionType:
          description: |-
            Option type.

            Only present for options markets.
          type: string
          enum:
            - call
            - put
        strikePrice:
          $ref: '#/components/schemas/DecimalDouble'
          description: |-
            Strike price.

            Only present for options markets.
        underlyingFuture:
          description: |-
            Underlying futures market.

            Only present for options markets.
          type: string
        rebateLevels:
          $ref: '#/components/schemas/RebateLevelsMap'
        mtf:
          description: True if this market is provided under the MTF license.
          type: boolean
        tradfi:
          description: True if this is a non-crypto market.
          type: boolean
        restricted:
          description: >-
            True if the account is restricted (to position-reducing orders) on
            this market.
          type: boolean
        isExpired:
          description: True if the instrument has expired
          type: boolean
      required:
        - contractSize
        - minimumTradeSize
        - impactMidSize
        - maxPositionSize
        - openingDate
        - symbol
        - pair
        - base
        - quote
        - tickSize
        - tradeable
        - type
        - isin
        - contractValueTradePrecision
        - postOnly
        - suspended
        - feeScheduleUid
        - rebateLevels
        - mtf
        - tradfi
        - restricted
        - isExpired
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
    _schemas_MarginLevel:
      description: >-
        A component level of a margin schedule.


        The `contracts` and `numNonContractUnits` fields are mutually-exclusive
        and are present only

        for single-collateral and multi-collateral markets, respectively.
      type: object
      properties:
        contracts:
          description: >-
            Position size/level to apply IM/MM rules within a single-collateral
            margin schedule.
          type: integer
          format: uint64
        numNonContractUnits:
          $ref: '#/components/schemas/NonNegativeDecimalDouble'
          description: >-
            Position size/level to apply IM/MM rules within a multi-collateral
            margin schedule.
        initialMargin:
          $ref: '#/components/schemas/NonNegativeDecimalDouble'
          description: Initial margin (IM) rate.
        maintenanceMargin:
          $ref: '#/components/schemas/NonNegativeDecimalDouble'
          description: Maintenance margin (MM) rate.
      required:
        - initialMargin
        - maintenanceMargin
    MarketSymbol:
      description: Market symbol
      type: string
      pattern: '[A-Z0-9_.]+'
      example: PF_BTCUSD
    RebateLevelsMap:
      description: |
        Maps market share percentage levels to rebate percentages.

        Keys and values are decimal strings.
      type: object
      additionalProperties:
        $ref: '#/components/schemas/DecimalDouble'
      x-additionalPropertiesKeyFormat: decimal
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
    NonNegativeDecimalDouble:
      type: number
      format: double
      example: 12.03532
      minimum: 0
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
