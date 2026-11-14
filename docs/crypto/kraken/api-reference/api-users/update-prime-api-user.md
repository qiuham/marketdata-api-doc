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
source_url: 'https://docs.kraken.com/api-reference/api-users/update-prime-api-user'
updated_at: 2026-11-13
---

# Update Prime API User

> Updates the name or status of a Prime API user.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`. API keys that belong to an
organization also need `Prime Ops`; an organization key without it is rejected with
`EGeneral:Permission denied:prime ops`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/UpdatePrimeApiUser
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
  /0/private/UpdatePrimeApiUser:
    post:
      tags:
        - API Users
      summary: Update Prime API User
      description: >
        Updates the name or status of a Prime API user.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`. API keys that belong to an

        organization also need `Prime Ops`; an organization key without it is
        rejected with

        `EGeneral:Permission denied:prime ops`.
      operationId: updatePrimeApiUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdatePrimeApiUser'
      responses:
        '200':
          description: API user updated.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdatePrimeApiUser1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    UpdatePrimeApiUser:
      title: Update Prime API User Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        user_id:
          type: string
          description: The unique identifier of the API user to update.
          example: 2T0RXL9B8K5D6
        name:
          type: string
          description: New display name for the API user.
          example: Updated User Name
        status:
          type: string
          description: New status for the API user.
          enum:
            - Enabled
            - Disabled
          example: Enabled
      additionalProperties: false
      required:
        - nonce
        - user_id
    UpdatePrimeApiUser1:
      description: Response containing the updated Prime API user.
      type: object
      properties:
        result:
          $ref: '#/components/schemas/ApiUserInfo'
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
    ApiUserInfo:
      description: Prime API user information.
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the API user.
          example: 2T0RXL9B8K5D6
        name:
          type: string
          description: Name of the API user.
          example: Test User
        status:
          type: string
          description: Current status of the API user.
          enum:
            - Enabled
            - Disabled
          example: Enabled
        roles:
          type: array
          description: Roles assigned to the API user.
          items:
            type: string
            enum:
              - Trader
              - Viewer
          example:
            - Trader
      required:
        - id
        - name
        - status
        - roles
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
