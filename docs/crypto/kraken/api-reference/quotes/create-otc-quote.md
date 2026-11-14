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
source_url: 'https://docs.kraken.com/api-reference/quotes/create-otc-quote'
updated_at: 2026-11-13
---

# Create OTC Quote

> Creates a new OTC request for quote.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/CreateOtcQuoteRequest
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
  /private/CreateOtcQuoteRequest:
    post:
      tags:
        - Quotes
      summary: Create OTC Quote
      description: >
        Creates a new OTC request for quote.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`
      operationId: createOtcQuoteRequest
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/create-otc-quote-request'
      responses:
        '200':
          description: Create OTC quote result.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/create-otc-quote-request-2'
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
    create-otc-quote-request:
      title: Create OTC Quote Request Body
      description: >-
        Request to create a new OTC quote. You must specify either the amount of
        base asset you want to trade or the total amount of quote asset you want
        to spend/receive, but not both.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        base:
          type: string
          description: The asset you want to buy or sell (e.g., BTC, ETH).
          example: BTC
        quote:
          type: string
          description: The asset used to price the base asset (e.g., USD, USDT).
          example: USD
        amount:
          type: string
          description: >-
            The quantity of base asset you want to trade. Cannot be used
            together with the total field.
          example: '2.5'
        total:
          type: string
          description: >-
            The total amount of quote asset you want to spend (for buy orders)
            or receive (for sell orders). Cannot be used together with the
            amount field.
          example: '200000.5'
        type:
          type: string
          description: >-
            The direction of the trade. Use 'buy' to purchase the base asset
            with the quote asset, or 'sell' to sell the base asset for the quote
            asset.
          enum:
            - buy
            - sell
      additionalProperties: false
      required:
        - nonce
        - base
        - quote
        - type
    create-otc-quote-request-2:
      title: createOtcQuoteRequest
      description: Response schema for creating an OTC quote request.
      type: object
      properties:
        result:
          type: object
          title: OTC Request for Quote
          properties:
            quote:
              $ref: '#/components/schemas/quote-props'
              type: object
              description: Quote created
              required:
                - base
                - quote
                - type
                - amount
                - settlement
              additionalProperties: false
          required:
            - quote
          additionalProperties: false
        error:
          $ref: '#/components/schemas/error'
      required:
        - error
      additionalProperties: false
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    quote-props:
      type: object
      properties:
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
