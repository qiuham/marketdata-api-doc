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
source_url: 'https://docs.kraken.com/api-reference/api-user-keys/delete-prime-api-user-key'
updated_at: 2026-11-13
---

# Delete Prime API User Key

> Permanently deletes an API key for a Prime API user. This action cannot be undone.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`. API keys that belong to an
organization also need `Prime Ops`; an organization key without it is rejected with
`EGeneral:Permission denied:prime ops`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/DeletePrimeApiUserKey
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
  /0/private/DeletePrimeApiUserKey:
    post:
      tags:
        - API User Keys
      summary: Delete Prime API User Key
      description: >
        Permanently deletes an API key for a Prime API user. This action cannot
        be undone.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`. API keys that belong to an

        organization also need `Prime Ops`; an organization key without it is
        rejected with

        `EGeneral:Permission denied:prime ops`.
      operationId: deletePrimeApiUserKey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeletePrimeApiUserKey'
      responses:
        '200':
          description: API user key deleted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeletePrimeApiUserKey1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    DeletePrimeApiUserKey:
      title: Delete Prime API User Key Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        user_id:
          type: string
          description: The unique identifier of the API user who owns the key.
          example: 2T0RXL9B8K5D6
        key_id:
          type: string
          description: The unique identifier of the API key to delete.
          example: 3RM9K4ZTC0C00
      additionalProperties: false
      required:
        - nonce
        - user_id
        - key_id
    DeletePrimeApiUserKey1:
      description: Response confirming deletion of a Prime API user key.
      type: object
      properties:
        result:
          type: object
          properties:
            deleted:
              type: boolean
              description: Whether the key was successfully deleted.
              example: true
          required:
            - deleted
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
