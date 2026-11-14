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
source_url: 'https://docs.kraken.com/api-reference/api-keys/check-v3-api-key'
updated_at: 2026-11-13
---

# Check v3 API key

> Verify API key access and return the authenticated key's details.



## OpenAPI

````yaml /openapi/futures-auth-rest.yaml get /api-keys/v3/check
openapi: 3.1.0
info:
  title: Ancile (Authentication Service) Public API
  version: '1'
  description: Public auth APIs.
servers:
  - url: https://futures.kraken.com/api/auth/v1
    description: Kraken Futures Production
security: []
tags:
  - name: PoW
  - name: Authentication
  - name: MFA
  - name: Verify
  - name: Account
  - name: API Keys
  - name: Regions
paths:
  /api-keys/v3/check:
    get:
      tags:
        - API Keys
      summary: Check v3 API key
      description: Verify API key access and return the authenticated key's details.
      operationId: checkV3ApiKey
      responses:
        '200':
          $ref: '#/components/responses/CheckV3ApiKey'
        '401':
          $ref: '#/components/responses/Error'
          description: API key is not found or request signature is invalid.
      security:
        - api-key-any: []
          request-signature: []
components:
  responses:
    CheckV3ApiKey:
      description: API key authentication is valid and details have been returned.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/CheckedV3ApiKeyDetails'
    Error:
      description: Error descriptor
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorDescriptor'
  schemas:
    CheckedV3ApiKeyDetails:
      type: object
      properties:
        apiKey:
          description: API key that signed the request.
          type: string
          format: base64
          example: Gom9BsP75m41c9fuY6oJk/unMWaDZjYIcTP4/5kqPvtzdbj5JU5/Fyeb
        accountUid:
          description: UID of the account that the API key belongs to.
          type: string
          format: uuid
        iiban:
          description: IIBAN of the account that the API key belongs to.
          oneOf:
            - $ref: '#/components/schemas/Iiban'
            - type: 'null'
        createdAt:
          $ref: '#/components/schemas/Rfc3339DateTime'
          description: Date-time that the API key was created.
        permissions:
          $ref: '#/components/schemas/ApiKeyPermissionMap'
          description: Permissions of the API key.
        allowedCidrBlock:
          oneOf:
            - $ref: '#/components/schemas/ApiKeyAllowedCidrBlock'
            - type: 'null'
        allowedCidrBlocks:
          description: Ranges of IP addresses that may use the API key.
          type: array
          items:
            $ref: '#/components/schemas/ApiKeyAllowedCidrBlock'
      required:
        - apiKey
        - accountUid
        - iiban
        - createdAt
        - permissions
        - allowedCidrBlock
        - allowedCidrBlocks
    ErrorDescriptor:
      type: object
      properties:
        error:
          type: string
        message:
          type: string
        suberror:
          type:
            - string
            - 'null'
      required:
        - error
        - message
        - suberror
    Iiban:
      description: Account IIBAN, if Kraken customer.
      type: string
      example: AA08 N84G CPAR UN7A
      pattern: ^AA[A-Z0-9]{2}[ -][A-Z0-9]{4}[ -][A-Z0-9]{4}[ -][A-Z0-9]{4}$
      x-rust:
        type: iiban::Iiban
        traits:
          - Clone
          - Copy
          - Debug
          - Eq
          - Hash
          - PartialEq
    Rfc3339DateTime:
      description: RFC 3339 formatted date-time
      type: string
      format: date-time
      example: '2019-08-24T14:15:22Z'
    ApiKeyPermissionMap:
      type: object
      properties:
        general:
          $ref: '#/components/schemas/ApiKeyV3AccessLevel'
        transfer:
          $ref: '#/components/schemas/ApiKeyV3AccessLevel'
      required:
        - general
        - transfer
    ApiKeyAllowedCidrBlock:
      description: Range of IP addresses that may use the API key.
      type: string
      format: cidr
      example: 192.168.0.0/16
      x-rust:
        type: ipnetwork::IpNetwork
        traits:
          - Clone
          - Copy
          - Debug
          - Eq
          - Hash
          - Ord
          - PartialEq
          - PartialOrd
    ApiKeyV3AccessLevel:
      description: Tier of access granted to an API key.
      type: string
      enum:
        - NO_ACCESS
        - READ_ONLY
        - FULL_ACCESS
      x-exhaustive: true
  securitySchemes:
    api-key-any:
      type: apiKey
      description: API Key with any permissions.
      in: header
      name: apikey
      x-inlineDescription: true
    request-signature:
      type: apiKey
      description: Request signature.
      in: header
      name: authent
      x-inlineDescription: true

````
