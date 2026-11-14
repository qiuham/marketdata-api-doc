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
source_url: 'https://docs.kraken.com/api-reference/trades/get-otc-options-trade-history'
updated_at: 2026-11-13
---

# Get OTC Options Trade History

> Retrieves the API key owner's booked OTC options trades for an inclusive date range.
Deleted records and records that do not represent a client trade are excluded.
Results are returned newest first.

Request `start_date`, `end_date`, and `updated_after` values use Unix epoch seconds.
Response `order_date`, `expiry_date`, and the settlement time fields use Unix epoch milliseconds.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/GetOtcOptionsTradeHistory
openapi: 3.0.0
info:
  title: REST API
  version: 1.1.0
  description: ''
servers:
  - url: https://api.kraken.com/0
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Quotes
  - name: Trades
paths:
  /private/GetOtcOptionsTradeHistory:
    post:
      tags:
        - Trades
      summary: Get OTC Options Trade History
      description: >
        Retrieves the API key owner's booked OTC options trades for an inclusive
        date range.

        Deleted records and records that do not represent a client trade are
        excluded.

        Results are returned newest first.


        Request `start_date`, `end_date`, and `updated_after` values use Unix
        epoch seconds.

        Response `order_date`, `expiry_date`, and the settlement time fields use
        Unix epoch milliseconds.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOtcOptionsTradeHistory
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/get-otc-options-trade-history'
      responses:
        '200':
          description: OTC options trades retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-otc-options-trade-history-2'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    '500':
      title: 500 Internal Server Error
      description: Internal error response
      type: object
      properties:
        error:
          $ref: '#/components/schemas/error'
    get-otc-options-trade-history:
      title: Get OTC Options Trade History Request Body
      description: >
        Request body for retrieving the API key owner's OTC options trades.

        `start_date`, `end_date`, and `updated_after` are Unix epoch seconds.
        `end_date` must be greater than `start_date`.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        start_date:
          type: integer
          format: int64
          description: Inclusive start of the trade window, Unix epoch seconds.
          example: 1785542400
        end_date:
          type: integer
          format: int64
          description: >-
            Inclusive end of the trade window, Unix epoch seconds. Must be
            strictly after `start_date`.
          example: 1788220800
        offset:
          type: integer
          format: int32
          minimum: 0
          default: 0
          description: 0-based index of the first result to return.
          example: 0
        limit:
          type: integer
          format: int32
          minimum: 0
          default: 100
          maximum: 1000
          description: >-
            Maximum number of results to return. Defaults to 100 when omitted or
            set to 0. Values above 1000 are capped to 1000.
          example: 100
        open_only:
          type: boolean
          default: false
          description: >-
            When true, return only unexpired opening trades that have not been
            closed.
          example: false
        updated_after:
          type: integer
          format: int64
          minimum: 0
          description: >
            When non-zero, return only trades whose trade, settlement, or close
            record was updated at or after this time (inclusive).

            `start_date` and `end_date` still apply.

            Omit the field, or send 0, to leave the trade-date window as the
            only time filter.

            Unix epoch seconds.
          example: 1785542400
      additionalProperties: false
      required:
        - nonce
        - start_date
        - end_date
    get-otc-options-trade-history-2:
      description: >-
        Response schema for retrieving OTC options trade history. The result
        contains an array of trades, newest first.
      type: object
      properties:
        result:
          title: Options trades
          type: array
          items:
            $ref: '#/components/schemas/options-trade'
        error:
          $ref: '#/components/schemas/error'
      required:
        - error
      additionalProperties: false
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    options-trade:
      type: object
      description: >
        An OTC options trade. Settlement result, collateral asset, refund, and
        exercise fields are returned only when applicable.

        Booked means actually settled or recorded, as opposed to the contractual
        scheduled time.

        Booked premium and expiry settlement times, and `reference_index`, are
        omitted when they do not apply.

        The two scheduled settlement times are always present.
      properties:
        txid:
          type: string
          description: Unique trade identifier.
          example: O_ABCD1234
        order_date:
          type: number
          format: double
          description: Trade time, Unix epoch milliseconds.
          example: 1786406400000
        direction:
          type: string
          description: Client-side direction.
          enum:
            - buy
            - sell
          example: buy
        contract_type:
          type: string
          description: Option contract type.
          enum:
            - call
            - put
          example: call
        asset:
          type: string
          description: Underlying asset symbol.
          example: BTC
        strike:
          type: string
          description: Strike price.
          example: '100000.00'
        expiry_date:
          type: number
          format: double
          description: Option expiry time, Unix epoch milliseconds.
          example: 1787904000000
        quantity:
          type: string
          description: Number of contracts.
          example: '10.00'
        currency:
          type: string
          description: Strike and premium currency.
          example: USD
        price:
          type: string
          description: Premium price per contract.
          example: '3.50'
        total_premium:
          type: string
          description: Total premium (quantity times price).
          example: '35.00'
        premium_asset:
          type: string
          description: Asset the premium is denominated in.
          example: USD
        collateral_qty:
          type: string
          description: Collateral quantity. May be "0.00" when no collateral is required.
          example: '3.00'
        collateral_asset:
          type: string
          description: Collateral asset. Omitted when no collateral asset applies.
          example: BTC
        timezone:
          type: string
          description: Timezone for the expiry time of day.
          example: UTC
        style:
          type: string
          description: Option style.
          enum:
            - american
            - european
          example: european
        open:
          type: boolean
          description: True when the trade opened a position, false when it closed one.
          example: true
        settlement_type:
          type: string
          description: Settlement type.
          enum:
            - CASH
            - PHYSICAL
          example: CASH
        settlement_result:
          type: string
          description: |
            Human-readable settlement outcome, matching the client options trade
            export. Examples include "Opened by trade O_ABCD1234",
            "Closed by trade O_EFGH5678",
            "Partially closed by trade O_ABCD1234 O_EFGH5678", "OTM Expired",
            and "ITM Exercised".
          example: Partially closed by trade O_ABCD1234 O_EFGH5678
        collateral_refund_qty:
          type: string
          description: Collateral quantity returned after settlement.
          example: '3.00'
        collateral_refund_asset:
          type: string
          description: Asset returned as collateral after settlement.
          example: BTC
        exercise_base_qty:
          type: string
          description: Base asset quantity recorded for exercise settlement.
          example: '1.00'
        exercise_base_asset:
          type: string
          description: Base asset recorded for exercise settlement.
          example: BTC
        exercise_quote_qty:
          type: string
          description: Quote asset quantity recorded for exercise settlement.
          example: '100000.00'
        exercise_quote_asset:
          type: string
          description: Quote asset recorded for exercise settlement.
          example: USD
        symbol:
          type: string
          description: >
            Contract name, provided so callers do not need to construct it
            themselves.

            Shape: BASE/QUOTE-DDMONYYTHH:MM-STRIKE-C for calls and
            BASE/QUOTE-DDMONYYTHH:MM-STRIKE-P for puts.

            If the trade has a settlement asset, it is included as
            BASE/QUOTE/SETTLEMENT-...

            The strike keeps a real fraction and drops trailing zeros, so 2.60
            prints as 2.6.

            A whole number stays a whole number (90000).

            Examples: BTC/USD-25DEC26T08:00-90000-C,
            XRP/USD-25DEC26T08:00-2.6-C.
          example: XRP/USD-25DEC26T08:00-2.6-C
        premium_settlement_time:
          type: number
          format: double
          description: >-
            When the premium was actually settled, Unix epoch milliseconds.
            Absent until that settlement is booked.
          example: 1775290320000
        expiry_settlement_time:
          type: number
          format: double
          description: >
            When expiry settlement was actually booked, Unix epoch milliseconds.

            Cash options use the cash settlement time.

            For physical options, the later of the base and quote settlement
            times; if only one is booked, that one.

            Absent until that settlement is booked.
          example: 1777622820000
        scheduled_premium_settlement_time:
          type: number
          format: double
          description: >
            Contractual premium settlement time, Unix epoch milliseconds. Always
            present.

            UTC calendar date of the trade (order_date), plus one day, at
            08:00:00 UTC.

            The time of day on the trade is ignored. This is not the booked
            premium time.

            A trade at 2026-04-03 13:15:41 UTC schedules premium settlement at
            2026-04-04 08:00:00 UTC (1775289600000).
          example: 1775289600000
        scheduled_expiry_settlement_time:
          type: number
          format: double
          description: >
            Contractual expiry settlement time, Unix epoch milliseconds. Always
            present.

            UTC calendar date of expiry, plus one day, at 08:00:00 UTC.

            An expiry that is already 08:00 UTC still moves to the next calendar
            day.

            This is not the booked expiry time.

            An expiry of 2026-04-30 08:00:00 UTC schedules expiry settlement at
            2026-05-01 08:00:00 UTC (1777622400000).
          example: 1777622400000
        reference_index:
          $ref: '#/components/schemas/options-reference-index'
      required:
        - txid
        - order_date
        - direction
        - contract_type
        - asset
        - strike
        - expiry_date
        - quantity
        - currency
        - price
        - total_premium
        - premium_asset
        - timezone
        - style
        - open
        - settlement_type
        - symbol
        - scheduled_premium_settlement_time
        - scheduled_expiry_settlement_time
      additionalProperties: false
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
    options-reference-index:
      type: object
      description: >
        For a cash option, the venue and that venue's symbol for the index the
        option expires against.

        Absent for physical settlement, and absent when no source was booked.
      properties:
        venue:
          type: string
          description: Venue that publishes the index.
          enum:
            - Deribit
            - Kraken
            - CF Benchmarks
          example: Deribit
        index:
          type: string
          description: |
            That venue's symbol for the index.
            Deribit uses lowercase base_quote (btc_usd).
            Kraken and CF Benchmarks use BASE/QUOTE (BTC/USD).
            XBT is normalized to BTC.
          example: btc_usd
      required:
        - venue
        - index
      additionalProperties: false
  responses:
    '500':
      description: Internal Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/500'
          example:
            errors:
              - field: null
                value: null
                type: Internal Error
                msg: Internal error
                severity: E
                errorClass: General
  securitySchemes:
    API-Key:
      type: apiKey
      description: The "API-Key" header should contain your API key.
      name: API-Key
      in: header
    API-Sign:
      type: apiKey
      description: >-
        Authenticated requests should be signed with the "API-Sign" header,
        using a signature generated with your private key, nonce, encoded
        payload, and URI path.
      name: API-Sign
      in: header

````
