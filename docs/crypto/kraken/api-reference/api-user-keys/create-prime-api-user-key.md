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
source_url: 'https://docs.kraken.com/api-reference/api-user-keys/create-prime-api-user-key'
updated_at: 2026-11-13
---

# Create Prime API User Key

> Creates a new API key for a Prime API user. The API secret is only returned in this response and cannot be
retrieved later.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`. API keys that belong to an
organization also need `Prime Ops`; an organization key without it is rejected with
`EGeneral:Permission denied:prime ops`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/CreatePrimeApiUserKey
openapi: 3.0.0
info:
  title: Prime REST API
  version: 1.0.0
  description: >
    Kraken Prime REST API — institutional-grade settlement and API-user
    management. Companion REST surface to the Prime FIX and Prime WebSocket
    APIs.


    **Authentication.** These endpoints use the standard Kraken REST
    authentication (`API-Key` and `API-Sign` headers, with a `nonce` in the
    request body). Use a standard Kraken API key with the permissions listed on
    each endpoint. Keys created for Prime API users with `CreatePrimeApiUserKey`
    are for the Prime WebSocket API only.
servers:
  - url: https://api.kraken.com
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Settlement
  - name: API Users
  - name: API User Keys
paths:
  /0/private/CreatePrimeApiUserKey:
    post:
      tags:
        - API User Keys
      summary: Create Prime API User Key
      description: >
        Creates a new API key for a Prime API user. The API secret is only
        returned in this response and cannot be

        retrieved later.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`. API keys that belong to an

        organization also need `Prime Ops`; an organization key without it is
        rejected with

        `EGeneral:Permission denied:prime ops`.
      operationId: createPrimeApiUserKey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePrimeApiUserKey'
      responses:
        '200':
          description: API user key created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatePrimeApiUserKey1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    CreatePrimeApiUserKey:
      title: Create Prime API User Key Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        user_id:
          type: string
          description: The unique identifier of the API user to create a key for.
          example: 2T0RXL9B8K5D6
      additionalProperties: false
      required:
        - nonce
        - user_id
    CreatePrimeApiUserKey1:
      description: >-
        Response containing the newly created Prime API user key, including the
        secret (only shown once).
      type: object
      properties:
        result:
          type: object
          properties:
            id:
              type: string
              description: Unique identifier for the API key.
              example: 3RM9K4ZTC0C00
            api_key:
              type: string
              description: The API key value.
              example: KRA5L19LAW8Z
            api_secret:
              type: string
              description: The API secret. Only returned at creation time.
              example: 6xq8p1mvk9r3n7swt2l5cj4eaydhzbf
            permissions:
              type: array
              description: Permissions associated with this key.
              items:
                type: string
              example:
                - read::marketdata
            user_id:
              type: string
              description: ID of the user who owns this key.
              example: 2T0RXL9B8K5D6
            whitelisted_ips:
              type: array
              description: IP addresses whitelisted for this key.
              items:
                type: string
              example:
                - 192.168.1.1
          required:
            - id
            - api_key
            - api_secret
            - user_id
          additionalProperties: false
        error:
          $ref: '#/components/schemas/Error'
      required:
        - result
        - error
      additionalProperties: false
    Nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    Error:
      type: array
      description: Empty on success. On failure, contains one or more error strings.
      items:
        description: Kraken API error string
        type: string
        example: EOTC:Invalid arguments
  responses:
    '500':
      description: Internal Server Error
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: array
                items:
                  type: string
            required:
              - error
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
