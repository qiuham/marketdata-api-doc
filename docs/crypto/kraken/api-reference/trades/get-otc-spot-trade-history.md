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
source_url: 'https://docs.kraken.com/api-reference/trades/get-otc-spot-trade-history'
updated_at: 2026-11-13
---

# Get OTC Spot Trade History

> Retrieves the API key owner's booked OTC spot trades for an inclusive date range.
Deleted records and records that do not represent a client trade are excluded.
Results are returned newest first.

Request `start_date` and `end_date` values use Unix epoch seconds.
Response `order_date` values use Unix epoch milliseconds.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/GetOtcSpotTradeHistory
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
  /private/GetOtcSpotTradeHistory:
    post:
      tags:
        - Trades
      summary: Get OTC Spot Trade History
      description: >
        Retrieves the API key owner's booked OTC spot trades for an inclusive
        date range.

        Deleted records and records that do not represent a client trade are
        excluded.

        Results are returned newest first.


        Request `start_date` and `end_date` values use Unix epoch seconds.

        Response `order_date` values use Unix epoch milliseconds.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOtcSpotTradeHistory
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/get-otc-spot-trade-history'
      responses:
        '200':
          description: OTC spot trades retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-otc-spot-trade-history-2'
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
    get-otc-spot-trade-history:
      title: Get OTC Spot Trade History Request Body
      description: >
        Request body for retrieving the API key owner's OTC spot trades.

        `start_date` and `end_date` are Unix epoch seconds. `end_date` must be
        greater than `start_date`.
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
      additionalProperties: false
      required:
        - nonce
        - start_date
        - end_date
    get-otc-spot-trade-history-2:
      description: >-
        Response schema for retrieving OTC spot trade history. The result
        contains an array of trades, newest first.
      type: object
      properties:
        result:
          title: Spot trades
          type: array
          items:
            $ref: '#/components/schemas/spot-trade'
        error:
          $ref: '#/components/schemas/error'
      required:
        - error
      additionalProperties: false
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    spot-trade:
      type: object
      description: An OTC spot trade.
      properties:
        txid:
          type: string
          description: Unique trade identifier.
          example: ABCD1234
        order_date:
          type: number
          format: double
          description: Trade time, Unix epoch milliseconds.
          example: 1786406400000
        base_asset:
          type: string
          description: Base asset symbol.
          example: BTC
        quote_asset:
          type: string
          description: Quote asset symbol.
          example: USD
        direction:
          type: string
          description: Client-side direction.
          enum:
            - buy
            - sell
          example: buy
        amount:
          type: string
          description: Base quantity.
          example: '0.0025'
        price:
          type: string
          description: Unit price.
          example: '80000.00'
        total:
          type: string
          description: Notional total.
          example: '200.00'
        amount_usd:
          type: string
          description: USD notional. Omitted when no USD value is available.
          example: '200.00'
        base_settle_method:
          type: string
          description: Settlement method for the base asset.
          enum:
            - undefined
            - on_chain
            - wire
            - internal_transfer
          example: internal_transfer
        quote_settle_method:
          type: string
          description: Settlement method for the quote asset.
          enum:
            - undefined
            - on_chain
            - wire
            - internal_transfer
          example: internal_transfer
      required:
        - txid
        - order_date
        - base_asset
        - quote_asset
        - direction
        - amount
        - price
        - total
        - base_settle_method
        - quote_settle_method
      additionalProperties: false
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
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
