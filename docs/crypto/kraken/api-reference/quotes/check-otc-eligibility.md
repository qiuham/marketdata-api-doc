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
source_url: 'https://docs.kraken.com/api-reference/quotes/check-otc-eligibility'
updated_at: 2026-11-13
---

# Check OTC Eligibility

> Retrieves the client permissions for the OTC Portal.

**API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/CheckOtcClient
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
  /private/CheckOtcClient:
    post:
      tags:
        - Quotes
      summary: Check OTC Eligibility
      description: >
        Retrieves the client permissions for the OTC Portal.


        **API Key Permissions Required:** `Funds permissions - Query` and `Funds
        permissions - Deposit`
      operationId: checkOtcClient
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/check-otc-client'
      responses:
        '200':
          description: OTC client check result.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/check-otc-client-2'
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
    check-otc-client:
      title: Check OTC Client Request Body
      description: >
        This schema represents the request body for checking an OTC client's
        status.

        No request body is required as the client information is typically
        passed through

        authentication headers.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
      additionalProperties: false
      required:
        - nonce
    check-otc-client-2:
      type: object
      description: Response schema for checking OTC client permissions
      properties:
        result:
          type: object
          description: Contains the successful response data
          properties:
            permissions:
              type: array
              items:
                type: string
              description: OTC permissions assigned to the client.
          required:
            - permissions
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
