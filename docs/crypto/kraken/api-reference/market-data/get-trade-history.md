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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-trade-history'
updated_at: 2026-11-13
---

# Get trade history

> This endpoint returns the most recent 100 trades prior to the specified `lastTime` value up
to past 7 days or recent trading engine restart (whichever is sooner).

If no `lastTime` specified, it will return 100 most recent trades.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /history
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
  /history:
    get:
      tags:
        - Market Data
      summary: Get trade history
      description: >-
        This endpoint returns the most recent 100 trades prior to the specified
        `lastTime` value up

        to past 7 days or recent trading engine restart (whichever is sooner).


        If no `lastTime` specified, it will return 100 most recent trades.
      operationId: getHistory
      parameters:
        - description: The symbol of the Futures.
          name: symbol
          in: query
          required: true
          schema:
            type: string
        - description: Returns the last 100 trades from the specified lastTime value.
          name: lastTime
          in: query
          required: false
          schema:
            type: string
        - name: includeMTFData
          in: query
          required: false
          schema:
            default: true
            type: boolean
          x-cfOnly: true
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
                          history:
                            type: array
                            items:
                              $ref: '#/components/schemas/HistoryJson'
                            description: >-
                              A list containing structures with historical price
                              information. The

                              list is sorted descending by time.
                        required:
                          - history
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
      security: []
components:
  schemas:
    HistoryJson:
      type: object
      properties:
        price:
          type: number
          description: |-
            For futures: The price of a fill

            For indices: The calculated value
        side:
          type: string
          description: >-
            The classification of the taker side in the matched trade: "buy" if
            the taker is a buyer, "sell" if the taker is a seller.
        size:
          type: string
          description: |-
            For futures: The size of a fill
            For indices: Not returned because N/A
        time:
          type: string
          description: >-
            The date and time of a trade or an index computation


            For futures: The date and time of a trade. Data is not aggregated

            For indices: The date and time of an index computation. For
            real-time indices, data is aggregated to the last computation of
            each full hour. For reference rates, data is not aggregated
        trade_id:
          type: integer
          format: int32
          description: >-
            For futures: A continuous index starting at 1 for the first fill in
            a Futures contract maturity

            For indices: Not returned because N/A
        type:
          type: string
          enum:
            - fill
            - liquidation
            - partial liquidation
            - assignment
            - unwind
            - rfq
            - termination
            - block
          description: >-
            The classification of the matched trade in an orderbook:


            - `fill` - it is a normal buyer and seller

            - `liquidation` - it is a result of a user being liquidated from
            their position. Covered liquidations are also reported as
            `liquidation`; there is no separate `covered liquidation` value

            - `partial liquidation` - it is a result of a position being reduced
            in steps by a partial liquidation, before a full liquidation becomes
            necessary

            - `assignment` - the fill is the result of a users position being
            assigned to a marketmaker

            - `unwind` - it is a result of a bankrupt account's position being
            unwound against a counterparty position to keep open interest
            balanced, including positions closed as part of an account
            termination

            - `rfq` - it is the execution of a request for quote

            - `termination` - not returned. Fills from an account termination
            are reported as `unwind`. Retained for backwards compatibility

            - `block` - not returned. Block trades are not supported. Retained
            for backwards compatibility
        uid:
          type: string
        sequence_id:
          type: string
          description: >-
            Per-market monotonic sequential trade id, starting at 1 for each
            market and

            incrementing by 1 per execution, for downstream gap detection and
            trade sequencing.

            Encoded as a string because the value is a 64-bit unsigned integer,
            which is unsafe

            as a JSON number. Omitted for trades recorded before sequential
            trade ids were

            introduced.
        instrument_identification_type:
          type: string
        isin:
          type: string
        execution_venue:
          type: string
        price_notation:
          type: string
        price_currency:
          type: string
        notional_amount:
          type: number
        notional_currency:
          type: string
        publication_time:
          type: string
        publication_venue:
          type: string
        transaction_identification_code:
          type: string
        to_be_cleared:
          type: boolean
      required:
        - time
        - price
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

````
