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
source_url: 'https://docs.kraken.com/api-reference/quotes/get-otc-historical-quotes'
updated_at: 2026-11-13
---

# Get OTC Historical Quotes

> Retrieves OTC quotes history.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/GetOtcHistoricalQuotes
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
  /private/GetOtcHistoricalQuotes:
    post:
      tags:
        - Quotes
      summary: Get OTC Historical Quotes
      description: >
        Retrieves OTC quotes history.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOtcHistoricalQuotes
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/get-otc-historical-quotes'
      responses:
        '200':
          description: Historical quotes retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-otc-historical-quotes-2'
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
    get-otc-historical-quotes:
      title: Get OTC Historical Quotes Request Body
      description: >-
        Request body schema for retrieving historical quotes for OTC
        instruments. This endpoint does not require any request body parameters.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
      additionalProperties: false
      required:
        - nonce
    get-otc-historical-quotes-2:
      description: Response schema for retrieving historical OTC quotes.
      type: object
      properties:
        result:
          title: Historical quotes
          type: array
          items:
            $ref: '#/components/schemas/historical-quote'
        error:
          $ref: '#/components/schemas/error'
      required:
        - error
      additionalProperties: false
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    historical-quote:
      type: object
      description: A historical OTC quote.
      properties:
        trade_id:
          type: string
          description: >-
            The Trade ID of the quote. Only present once the associated trade
            has been booked for an accepted quote
          example: TR123ABS
          nullable: true
        status:
          type: string
          description: The status of the quote
          enum:
            - Modified
            - Deleted
          example: null
          nullable: true
        acceptance:
          description: Acceptance
          type: object
          properties:
            status:
              type: string
              description: The acceptance status of the quote.
              enum:
                - accepted
                - rejected
                - expired
              example: accepted
            time:
              description: Unix timestamp in milliseconds.
              type: integer
              format: int64
              example: 1736257135382
          required:
            - status
            - time
        settlement_status:
          type: string
          description: The settlement status of the quote.
          enum:
            - settled
            - unsettled
          example: settled
        quote_id:
          description: The id of the quote.
          type: string
          example: 00001c47-8f59-4099-b6f8-b637437ef1ab
        client_order_id:
          description: >-
            The client order ID when quote was requested by an external partner
            client.
          type: string
          example: '7264675290025181184'
          nullable: true
        base:
          description: Base (amount) asset of the pair.
          type: string
          example: BTC
        quote:
          description: Quote asset of the pair.
          type: string
          example: USD
        type:
          description: Buy or sell.
          type: string
          enum:
            - buy
            - sell
        price:
          description: The unit price.
          type: string
          example: '100000.25'
        amount:
          description: Quantity of the base asset.
          type: string
          example: '2.5'
        total:
          description: Quantity of the quote asset.
          type: string
          example: '250000.625'
        settlement:
          description: >-
            If the settlement is automated or flexible. Only automated is
            currently supported through the API.
          type: string
          enum:
            - automated
            - flexible
      required:
        - quote_id
        - base
        - quote
        - type
        - amount
        - price
        - total
        - acceptance
        - settlement
        - settlement_status
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
