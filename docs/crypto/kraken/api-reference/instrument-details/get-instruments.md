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
source_url: 'https://docs.kraken.com/api-reference/instrument-details/get-instruments'
updated_at: 2026-11-13
---

# Get instruments

> Returns specifications for all currently listed markets and indices.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /instruments
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
  /instruments:
    get:
      tags:
        - Instrument Details
      summary: Get instruments
      description: Returns specifications for all currently listed markets and indices.
      operationId: getInstruments
      parameters:
        - $ref: '#/components/parameters/ContractTypesQuery'
        - $ref: '#/components/parameters/ExpiredQuery'
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
                              $ref: '#/components/schemas/Instrument'
                            description: >-
                              A list containing structures for each available
                              instrument. The list

                              is in no particular order.
                        required:
                          - instruments
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/InstrumentsExample'
      security: []
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
    ExpiredQuery:
      description: >-
        If `true`, return only expired instruments


        Defaults to `false`, in which case only non-expired instruments are
        returned
      name: expired
      in: query
      required: false
      schema:
        type: boolean
        default: false
  schemas:
    Instrument:
      type: object
      properties:
        makerProtectionMillis:
          type: integer
          format: int64
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
            appears. Absent

            when no maker protection is configured for this market.
        category:
          type: string
          description: >-
            'Category of the contract: "Layer 1", "Layer 2", "DeFi", or
            "Privacy" (multi-collateral

            contracts only).'
        contractSize:
          type: number
          description: The contract size of the Futures.
        contractValueTradePrecision:
          type: number
          description: >-
            Trade precision for the contract (e.g. trade precision of 2 means
            trades are precise to

            the hundredth decimal place 0.01).
        description:
          type: string
          description: >-
            Free-text description of the market for display and search; absent
            when not

            configured.
        fundingRateCoefficient:
          type: number
        impactMidSize:
          type: number
          description: >-
            Amount of contract used to calculated the mid price for the mark
            price.
        isin:
          type: string
          description: International Securities Identification Number (ISIN)
        lastTradingTime:
          type: string
          format: date-time
        marginSchedules:
          description: A map containing margin schedules by platform.
          type: object
          additionalProperties:
            $ref: '#/components/schemas/MarginSchedule'
        retailMarginLevels:
          description: Margin levels for retail clients.
          type: array
          items:
            $ref: '#/components/schemas/MarginLevel'
        marginLevels:
          description: Margin levels for professional clients.
          type: array
          items:
            $ref: '#/components/schemas/MarginLevel'
        maxPositionSize:
          type: number
          description: Maximum number of contracts that one can hold in a position
        maxOpenInterestUsd:
          type: number
          description: >-
            USD-denominated hard cap on market-wide open interest; absent when
            uncapped
        maxOpenInterestShare:
          type: number
          description: >-
            Largest share of market-wide open interest one user (master plus
            every subaccount)

            may hold on either side; absent when no share applies
        maxRelativeFundingRate:
          type: number
          description: >-
            Perpetuals only: the absolute value of the maximum permissible
            funding rate
        minRelativeFundingRate:
          type: number
          description: >-
            Pre-IPO perpetuals only: the minimum permissible funding rate
            (funding-rate

            floor). May be negative. Equal minimum and maximum rates mean the
            funding rate

            is fixed.
        openingDate:
          format: date-time
          type: string
          description: When the contract was first available for trading
        postOnly:
          type: boolean
          description: True if the instrument is in post-only mode, false otherwise.
        suspended:
          description: >-
            True if the market is not accepting orders (suspended, pending
            settlement or

            inactive). False for active and post-only markets.
          type: boolean
        feeScheduleUid:
          type: string
          deprecated: true
          description: >-
            **DEPRECATED** — Effective 2026-06-22, this field no longer

            corresponds to the fee schedule used for fee calculation on this

            instrument. Use the Spot

            [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)

            endpoint authenticated with a Spot API key to determine your fee

            rate.


            Unique identifier of fee schedule associated with the instrument
        symbol:
          description: Market symbol.
          type: string
          example: PF_BTCUSD
        pair:
          description: Asset pair.
          type: string
          example: BTC:USD
        base:
          description: Base asset.
          type: string
          example: BTC
        quote:
          description: Quote asset.
          type: string
          example: USD
        tags:
          type: array
          items:
            type: string
          description: Tag for the contract (currently does not return a value).
        tickSize:
          type: number
          description: Tick size of the contract being traded.
        tradeable:
          type: boolean
          description: >-
            True if this instrument is, or has ever been, a tradable instrument
            (i.e. a market).


            Always `true` for instruments returned by this endpoint —
            historical/expired

            instruments retain `tradeable=true`
        type:
          type: string
          enum:
            - flexible_futures
            - futures_inverse
            - futures_vanilla
            - options
          description: The type of the instrument
        underlying:
          type: string
          description: The underlying of the Futures.
        underlyingFuture:
          type: string
          description: 'For options: The underlying future of the option. Otherwise null.'
        tradfi:
          description: True if this is a non-crypto market.
          type: boolean
        mtf:
          type: boolean
          description: True if currently has MTF status.
        platformsPermitted:
          description: Platforms permitted to trade on this market.
          type: array
          items:
            $ref: '#/components/schemas/PlatformName'
        countriesBanned:
          description: Alpha-2 country codes banned from trading on this market.
          type: array
          items:
            $ref: '#/components/schemas/CountryCodeAlpha2'
        isExpired:
          type: boolean
          description: True if the instrument has expired.
      required:
        - tradeable
        - symbol
        - tradfi
        - isExpired
        - platformsPermitted
        - countriesBanned
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
    MarginSchedule:
      type: object
      properties:
        retail:
          type: array
          items:
            $ref: '#/components/schemas/MarginLevel'
        professional:
          type: array
          items:
            $ref: '#/components/schemas/MarginLevel'
      required:
        - retail
        - professional
    MarginLevel:
      type: object
      properties:
        contracts:
          type:
            - integer
            - 'null'
          format: int64
          description: >-
            For futures: The lower limit of the number of contracts to which
            this margin level applies


            For indices: Not returned because N/A
        numNonContractUnits:
          type:
            - number
            - 'null'
          format: double
          description: >
            For futures: The lower limit of the number of non-contract units
            (i.e. quote currency

            units for linear futures) to which this margin level applies


            For indices: Not returned because N/A.
        initialMargin:
          type: number
          description: |-
            For futures: The initial margin requirement for this level

            For indices: Not returned because N/A
        maintenanceMargin:
          type: number
          description: |-
            For futures: The maintenance margin requirement for this level

            For indices: Not returned because N/A
      required:
        - initialMargin
        - maintenanceMargin
    PlatformName:
      type: string
      minLength: 3
      maxLength: 30
      pattern: '[a-z_]+'
      example: mtf
    CountryCodeAlpha2:
      description: Alpha-2 country code, upper case.
      type: string
      example: GB
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
    InstrumentsExample:
      value:
        instruments:
          - symbol: PI_XBTUSD
            pair: XBT:USD
            base: XBT
            quote: USD
            type: futures_inverse
            underlying: rr_xbtusd
            tickSize: 0.5
            contractSize: 1
            tradeable: true
            impactMidSize: 1
            maxPositionSize: 1000000
            openingDate: '2022-01-01T00:00:00.000Z'
            marginLevels:
              - contracts: 0
                initialMargin: 0.02
                maintenanceMargin: 0.01
              - contracts: 500000
                initialMargin: 0.04
                maintenanceMargin: 0.02
              - contracts: 1000000
                initialMargin: 0.06
                maintenanceMargin: 0.03
              - contracts: 3000000
                initialMargin: 0.1
                maintenanceMargin: 0.05
            fundingRateCoefficient: 8
            maxRelativeFundingRate: 0.001
            isin: GB00J62YGL67
            contractValueTradePrecision: 0
            postOnly: false
            feeScheduleUid: eef90775-995b-4596-9257-0917f6134766
            retailMarginLevels:
              - contracts: 0
                initialMargin: 0.5
                maintenanceMargin: 0.25
            category: ''
            tags: []
            tradfi: false
            mtf: true
            platformsPermitted: []
            countriesBanned: []
            isExpired: false
          - symbol: FI_XBTUSD_220930
            pair: XBT:USD
            base: XBT
            quote: USD
            type: futures_inverse
            underlying: rr_xbtusd
            lastTradingTime: '2022-09-30T15:00:00.000Z'
            tickSize: 0.5
            contractSize: 1
            tradeable: true
            impactMidSize: 1
            maxPositionSize: 1000000
            openingDate: '2022-01-01T00:00:00.000Z'
            marginLevels:
              - contracts: 0
                initialMargin: 0.02
                maintenanceMargin: 0.01
              - contracts: 500000
                initialMargin: 0.04
                maintenanceMargin: 0.02
              - contracts: 1000000
                initialMargin: 0.06
                maintenanceMargin: 0.03
              - contracts: 3000000
                initialMargin: 0.1
                maintenanceMargin: 0.05
            isin: GB00JVMLP260
            contractValueTradePrecision: 0
            postOnly: false
            feeScheduleUid: eef90775-995b-4596-9257-0917f6134766
            retailMarginLevels:
              - contracts: 0
                initialMargin: 0.5
                maintenanceMargin: 0.25
            category: ''
            tags: []
            tradfi: false
            mtf: false
            platformsPermitted: []
            countriesBanned: []
            isExpired: false
          - symbol: PF_XBTUSD
            pair: XBT:USD
            base: XBT
            quote: USD
            type: flexible_futures
            tickSize: 1
            contractSize: 1
            tradeable: true
            impactMidSize: 1
            maxPositionSize: 1000000
            openingDate: '2022-01-01T00:00:00.000Z'
            marginLevels:
              - numNonContractUnits: 0
                initialMargin: 0.02
                maintenanceMargin: 0.01
              - numNonContractUnits: 500000
                initialMargin: 0.04
                maintenanceMargin: 0.02
              - numNonContractUnits: 2000000
                initialMargin: 0.1
                maintenanceMargin: 0.05
              - numNonContractUnits: 5000000
                initialMargin: 0.2
                maintenanceMargin: 0.1
              - numNonContractUnits: 10000000
                initialMargin: 0.3
                maintenanceMargin: 0.15
              - numNonContractUnits: 30000000
                initialMargin: 0.5
                maintenanceMargin: 0.25
            fundingRateCoefficient: 8
            maxRelativeFundingRate: 0.001
            contractValueTradePrecision: 4
            feeScheduleUid: 5b755fea-c5b0-4307-a66e-b392cd5bd931
            postOnly: false
            retailMarginLevels:
              - numNonContractUnits: 0
                initialMargin: 0.02
                maintenanceMargin: 0.01
              - numNonContractUnits: 500000
                initialMargin: 0.04
                maintenanceMargin: 0.02
              - numNonContractUnits: 2000000
                initialMargin: 0.1
                maintenanceMargin: 0.05
              - numNonContractUnits: 5000000
                initialMargin: 0.2
                maintenanceMargin: 0.1
              - numNonContractUnits: 10000000
                initialMargin: 0.3
                maintenanceMargin: 0.15
              - numNonContractUnits: 30000000
                initialMargin: 0.5
                maintenanceMargin: 0.25
            category: Layer 1
            tags: []
            tradfi: false
            mtf: false
            platformsPermitted: []
            countriesBanned: []
            isExpired: false
        result: success
        serverTime: '2022-06-28T09:29:04.243Z'

````
