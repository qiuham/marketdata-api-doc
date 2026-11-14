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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/get-vault'
updated_at: 2026-11-13
---

# Get vault

> Returns metadata for a single vault the authenticated user can access. Initiator and Reviewer API users must be a member of the vault.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml get /v0/insto/custody/vaults/{vault_id}
openapi: 3.0.0
info:
  title: Insto Custody External REST API
  version: 1.0.0
  description: ''
servers:
  - url: https://api.kraken.com
    description: Production Server
security: []
tags:
  - name: Custody External API
paths:
  /v0/insto/custody/vaults/{vault_id}:
    get:
      tags:
        - Custody External API
      summary: Get vault
      description: >-
        Returns metadata for a single vault the authenticated user can access.
        Initiator and Reviewer API users must be a member of the vault.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: getV0InstoCustodyVaultsVaultId
      parameters:
        - in: path
          name: vault_id
          required: true
          description: >-
            Vault identifier, a `V`-prefixed 14-char base32 string with a final
            check character.
          schema:
            type: string
            example: VABCDEF234567A
          style: simple
      responses:
        '200':
          description: OK. Returns vault metadata for the requested vault.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    description: >-
                      Vault identifier, a `V`-prefixed 14-char base32 string
                      with a final check character. This is the canonical ID
                      used in vault-scoped endpoints (the `{vault_id}` path
                      parameter).
                    type: string
                    example: VW44KPQC4C62K6
                  iiban:
                    description: >-
                      Vault IIBAN, 16-char alphanumeric in 4x4 groups. A funding
                      account number for the same vault as `id`. It is not
                      interchangeable with `id` in path parameters.
                    type: string
                    example: AA88 N84G AET3 RAOA
                  name:
                    description: Human-readable vault name.
                    type: string
                    example: My Vault 1
                  description:
                    description: Optional vault description.
                    nullable: true
                    type: string
                    example: Primary cold vault
                  status:
                    description: Vault lifecycle status.
                    type: string
                    example: created
                  created_at:
                    description: >-
                      Vault creation time as an RFC 3339 UTC timestamp (Z offset
                      required), e.g. `2026-01-15T12:34:56Z`.
                    type: string
                    format: date-time
                    example: '2026-01-15T12:34:56Z'
                  deposit_lock_rekeying_only:
                    description: >-
                      Whether the vault's deposits are restricted to rekeying
                      only. Null when not set.
                    nullable: true
                    type: boolean
                    example: false
                  attributes:
                    description: Vault attribute labels (e.g. `token_vesting`).
                    type: array
                    items:
                      type: string
                    example:
                      - token_vesting
                required:
                  - id
                  - iiban
                  - name
                  - status
                  - created_at
                  - attributes
        '400':
          description: Bad Request. The request failed validation.
          content:
            application/problem+json:
              schema:
                description: >-
                  Error responses follow `Problem Details for HTTP APIs`
                  ([rfc7807]).


                  [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                type: object
                properties:
                  type:
                    description: >-
                      URL uniquely identifying the error type relative to an
                      operation
                    type: string
                    enum:
                      - tag:kraken.com,2025:BadRequest
                    example: tag:kraken.com,2025:BadRequest
                  status:
                    description: HTTP status (provided for convenience)
                    type: integer
                    format: uint16
                    minimum: 0
                    example: 400
                  title:
                    description: Short human-readable summary
                    type: string
                    example: Bad Request
                  detail:
                    nullable: true
                    description: Help to solve the problem
                    type: string
                    example: Invalid request parameter.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    description: Error-specific payload.
                    type: object
                    properties:
                      message:
                        description: Human-readable description of the validation failure.
                        type: string
                        example: Invalid request parameter.
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '403':
          description: >-
            Forbidden. The caller lacks access to the requested vault, or the
            vault identifier is malformed or unknown.
          content:
            application/problem+json:
              schema:
                description: >-
                  Error responses follow `Problem Details for HTTP APIs`
                  ([rfc7807]).


                  [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                type: object
                properties:
                  type:
                    description: >-
                      URL uniquely identifying the error type relative to an
                      operation
                    type: string
                    enum:
                      - tag:kraken.com,2025:PermissionDenied
                    example: tag:kraken.com,2025:PermissionDenied
                  status:
                    description: HTTP status (provided for convenience)
                    type: integer
                    format: uint16
                    minimum: 0
                    example: 403
                  title:
                    description: Short human-readable summary
                    type: string
                    example: Forbidden
                  detail:
                    nullable: true
                    description: Help to solve the problem
                    type: string
                    example: The caller is not authorized to perform this action.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    description: Error-specific payload.
                    type: object
                    properties:
                      message:
                        description: Human-readable description of why access was denied.
                        type: string
                        example: Permission denied.
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '500':
          description: >-
            Internal Server Error. An unhandled exception occurred while serving
            the request.
          content:
            application/problem+json:
              schema:
                oneOf:
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/WriteResponse
                        example: tag:kraken.com,2025:gateway/WriteResponse
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to write response to upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/Connect
                        example: tag:kraken.com,2025:gateway/Connect
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to connect to upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/WriteResponse
                        example: tag:kraken.com,2025:gateway/WriteResponse
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to write response to upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/Fatal
                        example: tag:kraken.com,2025:gateway/Fatal
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: >-
                          A fatal gateway error occurred while serving the
                          request.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:Unknown
                        example: tag:kraken.com,2025:Unknown
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: >-
                          An unexpected error occurred while serving the
                          request.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        type: object
                        properties:
                          message:
                            type: string
                            description: >-
                              Human-readable description of the underlying
                              failure.
                            example: Unhandled exception while servicing the request.
                          core_error:
                            type: string
                            description: Identifier for the originating error.
                            example: InternalError
                        required:
                          - message
                          - core_error
                        description: >-
                          Error-specific payload returned for an unhandled
                          exception.
                    required:
                      - data
                      - status
                      - title
                      - type
        '503':
          description: >-
            Service Unavailable. The custody service could not connect to a
            downstream dependency.
          content:
            application/problem+json:
              schema:
                description: >-
                  Error responses follow `Problem Details for HTTP APIs`
                  ([rfc7807]).


                  [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                type: object
                properties:
                  type:
                    description: >-
                      URL uniquely identifying the error type relative to an
                      operation
                    type: string
                    enum:
                      - tag:kraken.com,2025:gateway/Connect
                    example: tag:kraken.com,2025:gateway/Connect
                  status:
                    description: HTTP status (provided for convenience)
                    type: integer
                    format: uint16
                    minimum: 0
                    example: 503
                  title:
                    description: Short human-readable summary
                    type: string
                    example: Service Unavailable
                  detail:
                    nullable: true
                    description: Help to solve the problem
                    type: string
                    example: >-
                      Downstream custody service is temporarily unreachable;
                      retry with backoff.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    description: Custom data attached to this problem
                    example: {}
                required:
                  - data
                  - status
                  - title
                  - type
      security:
        - API Key Auth (key): []
          API Key Auth (signature): []
          API Key Auth (nonce): []
components:
  securitySchemes:
    API Key Auth (key):
      type: apiKey
      in: header
      name: api-key
    API Key Auth (signature):
      type: apiKey
      in: header
      name: api-sign
    API Key Auth (nonce):
      type: apiKey
      in: header
      name: api-nonce

````
