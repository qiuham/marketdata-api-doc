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
source_url: 'https://docs.kraken.com/api-reference/paylink/get-paylink-configuration'
updated_at: 2026-11-13
---

# Get paylink configuration

> Get paylink configuration

**API Key Permissions Required:** `Funds permissions - Query`




## OpenAPI

````yaml /openapi/pay-rest.yaml post /private/Pay/paylink/config
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
  - name: Request
  - name: Transfer
  - name: Paylink
paths:
  /private/Pay/paylink/config:
    post:
      tags:
        - Paylink
      summary: Get paylink configuration
      description: |
        Get paylink configuration

        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: getPaylinkConfig
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/getPaylinkConfig'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/getPaylinkConfig-2'
          description: ''
components:
  schemas:
    getPaylinkConfig:
      type: object
      required:
        - nonce
      properties:
        nonce:
          description: Nonce used in construction of `API-Sign` header
          type: string
    getPaylinkConfig-2:
      type: object
      required:
        - error
      properties:
        error:
          type: array
          items:
            description: General API error.
            type: object
            properties:
              severity:
                description: API error severity.
                type: string
                enum:
                  - E
                  - W
              errorClass:
                type: string
              type:
                type: string
              errorMessage:
                nullable: true
                type: string
            required:
              - errorClass
              - severity
              - type
        result:
          nullable: true
          properties:
            expire_time:
              description: Paylink expiration time (in seconds)
              format: uint64
              minimum: 0
              type: integer
          required:
            - expire_time
          type: object
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
