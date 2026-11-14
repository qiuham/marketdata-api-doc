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
source_url: 'https://docs.kraken.com/api-reference/quotes/update-otc-quote'
updated_at: 2026-11-13
---

# Update OTC Quote

> Accepts or rejects an OTC quote.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`




## OpenAPI

````yaml /openapi/otc-rest.yaml post /private/UpdateOtcQuote
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
  /private/UpdateOtcQuote:
    post:
      tags:
        - Quotes
      summary: Update OTC Quote
      description: >
        Accepts or rejects an OTC quote.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`
      operationId: updateOtcQuote
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/update-otc-quote'
      responses:
        '200':
          description: Update OTC quote result.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/update-otc-quote-2'
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
    update-otc-quote:
      title: Update OTC Quote Request Body
      description: Request body for updating the status of an existing OTC quote.
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        quote_id:
          type: string
          description: The unique identifier of the quote to update.
          example: 00001c47-8f59-4099-b6f8-b637437ef1ab
          format: uuid
        status:
          type: string
          description: The status of the quote, accepted or rejected.
          enum:
            - accepted
            - rejected
          example: accepted
      additionalProperties: false
      required:
        - nonce
        - quote_id
        - status
    update-otc-quote-2:
      title: Update OTC Quote Request Body
      description: >-
        Response schema for updating an OTC quote. Contains either a successful
        result with the quote ID or an error object.
      type: object
      properties:
        result:
          type: object
          properties:
            quote_id:
              type: string
              description: The id of the updated quote.
              example: 00001c47-8f59-4099-b6f8-b637437ef1ab
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
