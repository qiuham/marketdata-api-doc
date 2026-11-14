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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-ticker-by-symbol'
updated_at: 2026-11-13
---

# Get ticker by symbol

> Get market data for contract or index by symbol



## OpenAPI

````yaml /openapi/futures-rest.yaml get /tickers/{symbol}
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
  /tickers/{symbol}:
    parameters:
      - $ref: '#/components/parameters/MarketSymbolPath'
    get:
      tags:
        - Market Data
      summary: Get ticker by symbol
      description: Get market data for contract or index by symbol
      operationId: getTicker
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                allOf:
                  - type: object
                    properties:
                      ticker:
                        $ref: '#/components/schemas/AnyTicker'
                        type: object
                    required:
                      - ticker
                  - $ref: '#/components/schemas/SuccessResponse'
              examples:
                success:
                  $ref: '#/components/examples/TickerExample'
        '404':
          description: Contract could not be found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security: []
components:
  parameters:
    MarketSymbolPath:
      description: Market symbol.
      name: symbol
      in: path
      required: true
      schema:
        $ref: '#/components/schemas/MarketSymbol'
  schemas:
    AnyTicker:
      oneOf:
        - $ref: '#/components/schemas/MarketTicker'
        - $ref: '#/components/schemas/IndexTicker'
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
    MarketSymbol:
      description: Market symbol
      type: string
      pattern: '[A-Z0-9_.]+'
      example: PF_BTCUSD
    MarketTicker:
      title: Market Ticker
      type: object
      required:
        - symbol
        - tag
        - pair
        - markPrice
        - vol24h
        - volumeQuote
        - openInterest
        - suspended
        - indexPrice
        - postOnly
        - change24h
      properties:
        symbol:
          $ref: '#/components/schemas/MarketSymbol'
        last:
          $ref: '#/components/schemas/DecimalDouble'
          description: The price of the last fill.
        lastTime:
          description: The date and time at which `last` was observed.
          type: string
        lastSize:
          description: The size of the last fill.
          type: number
        tag:
          type: string
          enum:
            - perpetual
            - day
            - week
            - month
            - quarter
            - semiannual
          description: >-
            Expiry-related grouping.


            Currently can be 'perpetual', 'day', 'week', 'month', 'quarter', or
            'semiannual'. Other

            tags may be added without notice.
        pair:
          description: The currency pair of the instrument.
          type: string
          example: BTC:USD
        markPrice:
          description: >-
            The price to which Kraken Futures currently marks the Futures for
            margining purposes.
          type: number
        bid:
          description: The price of the current best bid.
          type: number
        bidSize:
          description: The size of the current best bid.
          type: number
        ask:
          description: The price of the current best ask.
          type: number
        askSize:
          description: The size of the current best ask.
          type: number
        vol24h:
          description: The sum of the sizes of all fills observed in the last 24 hours.
          type: number
        volumeQuote:
          description: >-
            The sum of the `size * price` of all fills observed in the last 24
            hours.
          type: number
        openInterest:
          description: The current open interest of the market.
          type: number
        open24h:
          description: The price of the fill observed 24 hours ago.
          type: number
        high24h:
          description: The highest fill price observed in the last 24 hours.
          type: number
        low24h:
          description: The lowest fill price observed in the last 24 hours.
          type: number
        extrinsicValue:
          type: number
          description: >-
            The mark price less the how much the option would be worth if
            exercised now, i.e.:
              - For a call: `markPrice - ( max ( Underlying - StrikePrice , 0) )`
              - For a put: `markPrice - ( max ( StrikePrice - Underlying , 0) )`

            Only returned for options markets.
        fundingRate:
          description: |-
            The current absolute funding rate.

            Only returned for perpetual markets.
          type: number
        fundingRatePrediction:
          description: >-
            The predicted absolute funding rate for the next funding period,
            based on the assumption

            that the last recorded market premium will stay constant until the
            next funding

            realisation time. This can be highly inaccurate, especially at the
            start of a funding

            period.


            Only returned for perpetual markets.
          type: number
        relativeFundingRate:
          description: |-
            The current relative funding rate.

            Only returned for perpetual markets when available.
          type: number
        relativeFundingRatePrediction:
          description: >-
            The predicted relative funding rate for the next funding period,
            based on the assumption

            that the last recorded market premium will stay constant until the
            next funding

            realisation time. This can be highly inaccurate, especially at the
            start of a funding

            period.


            Only returned for perpetual markets when available.
          type: number
        suspended:
          description: True if the market is suspended.
          type: boolean
        indexPrice:
          type: number
        postOnly:
          type: boolean
        change24h:
          description: The 24h change in price (%).
          type: number
        greeks:
          $ref: '#/components/schemas/OptionGreeks'
          description: >-
            Current greeks.


            Only returned for options markets. Each greek is rounded to 8
            decimal places using

            half-even rounding.


            Note: This is currently available exclusively in the Kraken pre-prod
            environments.
        isUnderlyingMarketClosed:
          type: boolean
          description: |
            True if the underlying market/index is closed.

            Only returned for tradfi markets.
    IndexTicker:
      title: Index Ticker
      type: object
      properties:
        symbol:
          description: The symbol of the index.
          type: string
          example: rr_ethusd
        last:
          description: The last calculated value.
          type: number
        lastTime:
          description: The date and time at which `last` was observed.
          type: string
          format: date-time
      required:
        - symbol
      additionalProperties: false
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
    DecimalDouble:
      type: number
      format: double
      example: 12.03532
    OptionGreeks:
      description: >-
        Option Greeks.


        On ticker REST responses, the ticker websocket feed, and FIX ticker
        market data, each value is

        rounded to 8 decimal places using half-even rounding. Values smaller
        than `1e-8` round to `0`.

        Other resources keep full precision.
      type: object
      properties:
        iv:
          type: number
          format: double
          description: >-
            The implied volatility. Displays an IV of -1.0 whenever the IV is
            impossible to calculate or outside of the bounds allowed.
        delta:
          type: number
          format: double
        gamma:
          format: double
          type:
            - number
            - 'null'
        vega:
          format: double
          type:
            - number
            - 'null'
        theta:
          format: double
          type:
            - number
            - 'null'
        rho:
          format: double
          type:
            - number
            - 'null'
      required:
        - iv
        - delta
        - gamma
        - vega
        - theta
        - rho
  examples:
    TickerExample:
      value:
        result: success
        ticker:
          tag: perpetual
          pair: XBT:USD
          symbol: pi_xbtusd
          markPrice: 30209.9
          bid: 8634
          bidSize: 1000
          ask: 49289
          askSize: 139984
          vol24h: 15304
          volumeQuote: 40351.34
          change24h: 1.9974017538161748
          openInterest: 149655
          open24h: 49289
          indexPrice: 21087.8
          last: 49289
          lastTime: '2022-06-17T10:46:35.705Z'
          lastSize: 100
          suspended: false
          fundingRate: 1.18588737106e-7
          fundingRatePrediction: 1.1852486794e-7
          postOnly: false
        serverTime: '2022-06-17T11:00:31.335Z'

````
