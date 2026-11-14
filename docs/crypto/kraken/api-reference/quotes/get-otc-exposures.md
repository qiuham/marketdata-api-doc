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
source_url: 'https://docs.kraken.com/api-reference/quotes/get-otc-exposures'
updated_at: 2026-11-13
---

# Get OTC Exposures

> Retrieves the max and used OTC exposures.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/GetOtcExposures
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
  /private/GetOtcExposures:
    post:
      tags:
        - Quotes
      summary: Get OTC Exposures
      description: >
        Retrieves the max and used OTC exposures.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOtcExposures
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/get-otc-exposures'
      responses:
        '200':
          description: OTC Exposures retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-otc-exposures-2'
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
    get-otc-exposures:
      title: Get OTC Exposures Request Body
      description: >-
        Request schema for retrieving OTC exposures data. This endpoint does not
        require any request body parameters.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
      additionalProperties: false
      required:
        - nonce
    get-otc-exposures-2:
      title: getOtcExposures
      description: >-
        Response schema for retrieving OTC exposure limits and usage information
        for a client.
      type: object
      properties:
        result:
          type: object
          properties:
            max_otc:
              type: string
              description: Max OTC exposure assigned to the client.
              example: '1500000'
            max_rfq:
              type: string
              description: Max RFQ exposure assigned to the client.
              example: '1500000'
            used_otc:
              type: string
              description: Used OTC Exposure (chat + RFQ).
              example: '100000'
            used_rfq:
              type: string
              description: Used RFQ exposure (RFQ only).
              example: '50000'
          required:
            - max_otc
            - max_rfq
            - used_otc
            - used_rfq
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
