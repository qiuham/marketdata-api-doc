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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/list-vaults'
updated_at: 2026-11-13
---

# List vaults

> Returns the vaults the authenticated user can access within an organization, each valued in the quote asset. Initiator and Reviewer API users see only the vaults they are a member of.

`quote_value` on each vault is a single aggregate valuation in the quote asset. It is not a substitute for per-asset holdings and does not carry asset codes or quantities. For the assets a vault holds and their spot, hold, available, staked, and pledged quantities, call `GET /v0/insto/custody/vaults/{vault_id}/assets/balances`.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml get /v0/insto/custody/vaults
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
  /v0/insto/custody/vaults:
    get:
      tags:
        - Custody External API
      summary: List vaults
      description: >-
        Returns the vaults the authenticated user can access within an
        organization, each valued in the quote asset. Initiator and Reviewer API
        users see only the vaults they are a member of.


        `quote_value` on each vault is a single aggregate valuation in the quote
        asset. It is not a substitute for per-asset holdings and does not carry
        asset codes or quantities. For the assets a vault holds and their spot,
        hold, available, staked, and pledged quantities, call `GET
        /v0/insto/custody/vaults/{vault_id}/assets/balances`.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: getV0InstoCustodyVaults
      parameters:
        - in: query
          name: org_iiban
          description: >-
            Restrict the result set to vaults owned by the specified
            organization, identified by its 16-char IIBAN. Defaults to the
            caller's organization when omitted.
          schema:
            type: string
          example: ABCD EFGH IJKL MNOP
          style: form
        - in: query
          name: quote_asset
          description: >-
            Asset code used to value each vault's fiat balance (e.g. USD, EUR).
            Defaults to USD when omitted.
          schema:
            type: string
          example: USD
          style: form
        - in: query
          name: limit
          description: >-
            Maximum number of vaults to return in the page. Defaults to 100 when
            omitted.
          schema:
            type: integer
            format: int32
          example: 100
          style: form
        - in: query
          name: offset
          description: >-
            Number of vaults to skip before the page begins, used together with
            `limit` for offset-based pagination. Defaults to 0 when omitted.
          schema:
            type: integer
            format: int32
          example: 0
          style: form
        - in: query
          name: id
          description: >-
            Restrict the result set to the supplied vault IDs. Each value is a
            `V`-prefixed 14-char base32 identifier with a final check character.
          schema:
            type: array
            items:
              type: string
          style: form
        - in: query
          name: iiban
          description: >-
            Restrict the result set to vaults whose IIBAN matches one of the
            supplied values. Each value is a 16-char alphanumeric IIBAN in 4x4
            groups.
          schema:
            type: array
            items:
              type: string
          style: form
        - in: query
          name: member
          description: >-
            Restrict the result set to vaults that include the supplied
            member(s), each identified by their 16-char user IIBAN.
          schema:
            type: array
            items:
              type: string
          style: form
        - in: query
          name: name
          description: >-
            Filter vaults by name. Combined with `name_match` and `name_case` to
            control how the term is matched.
          schema:
            type: string
          example: My Vault 1
          style: form
        - in: query
          name: name_match
          description: >-
            How the `name` term is matched against vault names. One of `equals`,
            `starts_with`, `contains`.
          schema:
            type: string
          example: contains
          style: form
        - in: query
          name: name_case
          description: >-
            Case sensitivity of the `name` match. One of `sensitive`,
            `insensitive`.
          schema:
            type: string
          example: insensitive
          style: form
        - in: query
          name: default_approvals_left
          description: >-
            Lower bound (inclusive) for the vault's default required-approvals
            count.
          schema:
            type: integer
            format: int32
          example: 1
          style: form
        - in: query
          name: default_approvals_right
          description: >-
            Upper bound (inclusive) for the vault's default required-approvals
            count.
          schema:
            type: integer
            format: int32
          example: 3
          style: form
        - in: query
          name: created_at_from
          description: >-
            Include only vaults created at or after this RFC 3339 UTC timestamp
            (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset is
            required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: created_at_to
          description: >-
            Include only vaults created at or before this RFC 3339 UTC timestamp
            (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset is
            required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: updated_at_from
          description: >-
            Include only vaults last updated at or after this RFC 3339 UTC
            timestamp (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset
            is required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: updated_at_to
          description: >-
            Include only vaults last updated at or before this RFC 3339 UTC
            timestamp (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset
            is required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: sort
          description: >-
            Ordering as a comma-separated list of `field:direction` tokens
            (direction optional, defaults to `desc`). Multiple columns are
            applied in order. Allowed fields: `id`, `name`, `created_at`,
            `updated_at`. Defaults to `id:desc`.
          schema:
            type: string
          example: name:asc,created_at:desc
          style: form
        - in: query
          name: resolve_policies
          description: >-
            When set to `true`, include each vault's `otc_enabled` policy flag
            in the response. Omitted otherwise.
          schema:
            type: string
          example: 'true'
          style: form
      responses:
        '200':
          description: >-
            OK. Returns the page of vaults the caller can access, with
            pagination total and the resolved quote asset.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    description: Page of vaults matching the request filters.
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          description: >-
                            Vault identifier, a `V`-prefixed 14-char base32
                            string with a final check character. This is the
                            canonical ID used in vault-scoped endpoints (the
                            `{vault_id}` path parameter); store this to address
                            the vault in subsequent API calls.
                          type: string
                          example: VW44KPQC4C62K6
                        iiban:
                          description: >-
                            Vault IIBAN, 16-char alphanumeric in 4x4 groups. A
                            funding account number for the same vault as `id`,
                            used for deposit and withdrawal routing and
                            references. It is not interchangeable with `id` in
                            path parameters.
                          type: string
                          example: AA88 N84G AET3 RAOA
                        name:
                          description: Human-readable vault name.
                          type: string
                          example: My Vault 1
                        status:
                          description: Vault lifecycle status.
                          type: string
                          example: created
                        quote_value:
                          description: >-
                            Total vault balance valued in the quote asset, as a
                            fixed-precision decimal string. Null when no balance
                            is available.
                          nullable: true
                          type: string
                          example: '1000.0000'
                        quote_value_change_24h:
                          description: >-
                            24h percentage change of the vault's quote-valued
                            spot balance versus the prior day, as a percentage
                            string (not a quote-currency amount).
                          type: string
                          example: '1.50'
                        missing_rates:
                          description: >-
                            Assets the service could not price into the quote
                            asset. Empty when every held asset was priced.
                          type: array
                          items:
                            type: object
                            properties:
                              asset:
                                description: Code of the asset that could not be priced.
                                type: string
                                example: XBT
                              asset_class:
                                description: Class of the asset that could not be priced.
                                type: string
                                example: currency
                            required:
                              - asset
                              - asset_class
                        deposit_lock_rekeying_only:
                          description: >-
                            Whether the vault's deposits are restricted to
                            rekeying only. Null when not set.
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
                        otc_enabled:
                          description: >-
                            Whether OTC trading is enabled for the vault.
                            Present only when `resolve_policies=true`.
                          type: boolean
                          example: true
                      required:
                        - id
                        - iiban
                        - name
                        - status
                        - quote_value_change_24h
                        - missing_rates
                        - attributes
                  total:
                    description: >-
                      Total number of vaults matching the filters, ignoring
                      pagination.
                    type: integer
                    format: int32
                    example: 1
                  quote_asset:
                    description: Quote asset code used to value the fiat balances.
                    type: string
                    example: USD
                required:
                  - result
                  - total
                  - quote_asset
        '400':
          description: Bad Request. One or more query parameters failed validation.
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
                    example: Request failed validation.
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
                        example: Request failed validation.
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '403':
          description: >-
            Forbidden. The caller is not authorized to list vaults for the
            requested organization.
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
                        example: Failed to read response from upstream service.
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
                        example: Failed to read response from upstream service.
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
                        example: Failed to read response from upstream service.
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
                        example: Failed to write response to the client.
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
                        example: Failed to connect to upstream service.
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
                        example: Failed to read response from upstream service.
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
                        example: Failed to read response from upstream service.
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
                        example: Failed to read response from upstream service.
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
                        example: Failed to write response to the client.
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
                        example: Fatal error encountered while processing the request.
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
                        example: An unexpected error occurred.
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
                            description: >-
                              Human-readable description of the unexpected
                              error.
                            type: string
                            example: An unexpected error occurred.
                          core_error:
                            description: Internal error identifier captured at the source.
                            type: string
                            example: internal_error
                        required:
                          - message
                          - core_error
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
  schemas:
    google.protobuf.Timestamp:
      type: string
      format: date-time
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
