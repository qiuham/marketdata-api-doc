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
source_url: 'https://docs.kraken.com/api-reference/quotes/get-otc-pairs'
updated_at: 2026-11-13
---

# Get OTC Pairs

> Retrieves the list of OTC trading pairs.

**API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/GetOtcPairs
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
  /private/GetOtcPairs:
    post:
      tags:
        - Quotes
      summary: Get OTC Pairs
      description: >
        Retrieves the list of OTC trading pairs.


        **API Key Permissions Required:** `Funds permissions - Query` and `Funds
        permissions - Deposit`
      operationId: getOtcPairs
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/get-otc-pairs'
      responses:
        '200':
          description: Available OTC pairs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-otc-pairs-2'
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
    get-otc-pairs:
      title: Get OTC Pairs Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
      additionalProperties: false
      required:
        - nonce
    get-otc-pairs-2:
      description: >-
        Response containing available OTC spot trading pairs and their
        specifications including decimal precision, size limits, and notional
        value constraints.
      type: object
      properties:
        result:
          type: object
          properties:
            spot_pairs:
              type: array
              title: OTC Spot pairs
              items:
                type: object
                properties:
                  base:
                    type: string
                    description: Base asset for the pair.
                    example: BTC
                  quote:
                    type: string
                    description: Quote asset for the pair.
                    example: USD
                  pair_name:
                    type: string
                    description: Pair name.
                    example: BTCUSD
                  pair_decimals:
                    $ref: '#/components/schemas/decimals'
                    description: Decimal precision for this pair.
                    example: '8'
                  lot_decimals:
                    $ref: '#/components/schemas/decimals'
                    description: >-
                      Decimal precision for the quantity that can be requested
                      for this pair.
                    example: '8'
                  cost_decimals:
                    $ref: '#/components/schemas/decimals'
                    description: Decimal precision for costs related to this pair.
                    example: '8'
                  max_base_amount:
                    type: string
                    description: >-
                      Max size in base asset that a quote can be requested for
                      this pair.
                    example: '100000'
                  max_notional:
                    type: string
                    description: >-
                      Max notional amount that a quote can be requested for this
                      pair.
                    example: '1000000'
                  min_base_amount:
                    type: string
                    description: >-
                      Min size in base asset that a quote can be requested for
                      this pair.
                    example: '0.1'
                  min_notional:
                    type: string
                    description: >-
                      Min notional amount that a quote can be requested for this
                      pair.
                    example: '100'
                required:
                  - base
                  - quote
                  - pair_name
                  - pair_decimals
                  - lot_decimals
                  - cost_decimals
                  - max_base_amount
          required:
            - spot_pairs
          additionalProperties: false
        error:
          $ref: '#/components/schemas/error'
      required:
        - result
        - error
      additionalProperties: false
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    decimals:
      type: number
      description: Unsigned byte (u8)
      minimum: 0
      maximum: 255
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
