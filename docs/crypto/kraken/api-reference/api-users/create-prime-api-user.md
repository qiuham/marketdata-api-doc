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
source_url: 'https://docs.kraken.com/api-reference/api-users/create-prime-api-user'
updated_at: 2026-11-13
---

# Create Prime API User

> Creates a new Prime API user with the specified role. Valid roles are `Viewer` and `Trader`.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`. API keys that belong to an
organization also need `Prime Ops`; an organization key without it is rejected with
`EGeneral:Permission denied:prime ops`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/CreatePrimeApiUser
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
  /0/private/CreatePrimeApiUser:
    post:
      tags:
        - API Users
      summary: Create Prime API User
      description: >
        Creates a new Prime API user with the specified role. Valid roles are
        `Viewer` and `Trader`.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`. API keys that belong to an

        organization also need `Prime Ops`; an organization key without it is
        rejected with

        `EGeneral:Permission denied:prime ops`.
      operationId: createPrimeApiUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePrimeApiUser'
      responses:
        '200':
          description: API user created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatePrimeApiUser1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    CreatePrimeApiUser:
      title: Create Prime API User Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        name:
          type: string
          description: Display name for the new API user.
          example: Test User
        role:
          type: string
          description: Role to assign to the new API user.
          enum:
            - Trader
            - Viewer
          example: Trader
      additionalProperties: false
      required:
        - nonce
        - name
        - role
    CreatePrimeApiUser1:
      description: Response containing the newly created Prime API user.
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
