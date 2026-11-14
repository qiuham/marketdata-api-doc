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
source_url: 'https://docs.kraken.com/api-reference/quotes/get-otc-active-quotes'
updated_at: 2026-11-13
---

# Get OTC Active Quotes

> Retrieves a list of active OTC quotes.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/GetOtcActiveQuotes
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
  /private/GetOtcActiveQuotes:
    post:
      tags:
        - Quotes
      summary: Get OTC Active Quotes
      description: >
        Retrieves a list of active OTC quotes.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOtcActiveQuotes
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/get-otc-active-quotes'
      responses:
        '200':
          description: Active quotes retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-otc-active-quotes-2'
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
    get-otc-active-quotes:
      title: Get OTC Active Quotes Request Body
      description: >
        Request body for retrieving active OTC quotes. This endpoint allows
        filtering of active quotes

        based on specific criteria. All parameters are optional and can be used
        to refine the search results.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        vault_id:
          type: string
          description: >
            The unique identifier of the vault associated with the OTC trade.
            This parameter is specifically used

            for custody OTC trades to filter quotes related to a particular
            vault.
          example: 456TR123
      additionalProperties: false
      required:
        - nonce
    get-otc-active-quotes-2:
      description: Response schema for retrieving active OTC quotes.
      type: object
      properties:
        result:
          title: Active quotes
          type: array
          items:
            $ref: '#/components/schemas/active-quote'
        error:
          $ref: '#/components/schemas/error'
      required:
        - error
      additionalProperties: false
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    active-quote:
      type: object
      description: An active OTC quote.
      properties:
        expires:
          description: Expiration time of the quote.
          type: object
          properties:
            time:
              description: Unix timestamp in milliseconds.
              type: integer
              format: int64
              example: 1715155200000
          required:
            - time
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
        - settlement
        - expires
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
