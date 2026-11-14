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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/create-task'
updated_at: 2026-11-13
---

# Create task

> Creates an approval task from one or more instructions. Each instruction describes a single change, such as a withdrawal, a sub-quorum update, or a user removal. The task is created in a pending state and its instructions take effect asynchronously once the task is approved. The response returns `id`, the approval UUID. It does not return `task_id` or `approval_id`. T-prefixed identifiers are not returned.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml post /v0/insto/custody/tasks
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
  /v0/insto/custody/tasks:
    post:
      tags:
        - Custody External API
      summary: Create task
      description: >-
        Creates an approval task from one or more instructions. Each instruction
        describes a single change, such as a withdrawal, a sub-quorum update, or
        a user removal. The task is created in a pending state and its
        instructions take effect asynchronously once the task is approved. The
        response returns `id`, the approval UUID. It does not return `task_id`
        or `approval_id`. T-prefixed identifiers are not returned.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: postV0InstoCustodyTasks
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                instructions:
                  type: array
                  items:
                    oneOf:
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - update_subquorum
                          version:
                            type: integer
                            format: int32
                          vault_id:
                            type: string
                          groups:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: string
                                required:
                                  type: integer
                                  format: int32
                                members:
                                  type: array
                                  items:
                                    type: string
                              required:
                                - required
                                - members
                        required:
                          - version
                          - vault_id
                          - groups
                          - type
                        title: update_subquorum
                        description: >-
                          Add, remove, or change the sub-quorum groups that
                          approve activity on a vault.
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - update_vault_user
                          version:
                            type: integer
                            format: int32
                          vault_id:
                            type: string
                          operation_type:
                            type: string
                            enum:
                              - add
                              - remove
                          user:
                            type: string
                          reason:
                            type: string
                        required:
                          - version
                          - vault_id
                          - operation_type
                          - user
                          - type
                        title: update_vault_user
                        description: Grant or revoke a user's access to a vault.
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - update_vault_policy
                          version:
                            type: integer
                            format: int32
                          vault_id:
                            type: string
                          policy:
                            type: object
                            properties:
                              type:
                                type: string
                              amount:
                                type: string
                              required:
                                type: integer
                                format: int32
                              available:
                                type: integer
                                format: int32
                              enable:
                                type: boolean
                            required:
                              - type
                        required:
                          - version
                          - vault_id
                          - policy
                          - type
                        title: update_vault_policy
                        description: Change a vault's approval policy.
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - request_withdrawal
                          version:
                            type: integer
                            format: int32
                          vault_id:
                            type: string
                          asset:
                            type: string
                          asset_class:
                            type: string
                          amount:
                            type: string
                          address_name:
                            type: string
                          fee_amount:
                            type: string
                            description: >-
                              Fee amount for the withdrawal, fixed-precision
                              decimal as string.
                            example: '0.00010000'
                          fee_asset:
                            type: string
                            description: Asset code the fee is charged in.
                            example: BTC
                          fee_asset_class:
                            type: string
                            description: >-
                              Asset class of the fee asset (e.g. `currency`,
                              `tokenized_asset`).
                            example: currency
                          fee_included:
                            type: boolean
                            description: >-
                              Whether the fee is included in the withdrawal
                              amount.
                            example: false
                          fee_level:
                            type: string
                            description: Fee tier to apply (e.g. `normal`).
                            example: normal
                          fee_quote_id:
                            type: string
                            description: >-
                              Identifier of the withdrawal fee quote to charge
                              the fee against. Optional; omit for a quote-less
                              withdrawal.
                            example: QABCDEF234567A
                          comment:
                            type: string
                          memo:
                            type: string
                        required:
                          - version
                          - vault_id
                          - asset
                          - asset_class
                          - amount
                          - address_name
                          - fee_amount
                          - fee_asset
                          - fee_asset_class
                          - fee_included
                          - fee_level
                          - type
                        title: request_withdrawal
                        description: >-
                          Withdraw assets from a vault to an allow-listed
                          external address.
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - remove_org_user
                          version:
                            type: integer
                            format: int32
                          org_iiban:
                            type: string
                          user_iiban:
                            type: string
                          reason:
                            type: string
                        required:
                          - version
                          - org_iiban
                          - user_iiban
                          - type
                        title: remove_org_user
                        description: Remove a user from the organization.
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - update_withdrawal_address
                          version:
                            type: integer
                            format: int32
                          vault_id:
                            type: string
                          operation_type:
                            type: string
                            enum:
                              - add
                              - remove
                          address:
                            type: object
                            properties:
                              address_name:
                                type: string
                              asset:
                                type: string
                              asset_class:
                                type: string
                              method:
                                type: string
                              info:
                                type: object
                                properties:
                                  address:
                                    type: string
                                  tag:
                                    type: string
                                  beneficiary:
                                    type: object
                                    properties:
                                      recipient:
                                        type: string
                                      type:
                                        type: string
                                      name:
                                        type: string
                                      last_name:
                                        type: string
                                      country:
                                        type: string
                                      province:
                                        type: string
                                      address_1:
                                        type: string
                                      address_2:
                                        type: string
                                      city:
                                        type: string
                                      postal_code:
                                        type: string
                                      vasp_name:
                                        type: string
                              description:
                                type: string
                              reason:
                                type: string
                            required:
                              - address_name
                        required:
                          - version
                          - vault_id
                          - operation_type
                          - address
                          - type
                        title: update_withdrawal_address
                        description: >-
                          Add, update, or remove an allow-listed withdrawal
                          address for a vault.
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - request_transfer_to_spot
                          version:
                            type: integer
                            format: int32
                          vault_id:
                            type: string
                          asset:
                            type: string
                          asset_class:
                            type: string
                          amount:
                            type: string
                          fee_quote_id:
                            type: string
                            description: >-
                              Identifier of the fee quote the transfer fee is
                              derived from. Required for crypto assets; omit for
                              fiat, which carries no fee.
                            example: QABCDEF234567A
                        required:
                          - version
                          - vault_id
                          - asset
                          - asset_class
                          - amount
                          - type
                        title: request_transfer_to_spot
                        description: >-
                          Transfer assets from a vault to the organization's
                          linked Kraken spot account. The destination is always
                          the organization's instant-transfer (master) address
                          and is not caller-supplied. Crypto transfers settle at
                          the fast fee tier resolved server side from
                          `fee_quote_id`; fiat transfers carry no fee. The
                          create response returns only the task id. Read the
                          funding transfer id from the task details endpoint.
                    description: >-
                      A single atomic instruction. The type field selects the
                      variant and determines which other fields are required.
                  description: >-
                    The atomic instructions to bundle into the task. Each entry
                    describes a single change and is one of the variants below,
                    identified by its type field.
                org_iiban:
                  type: string
                  description: Organization IIBAN the task is created under.
                  example: ABCD EFGH IJKL MNOP
                duration_seconds:
                  type: integer
                  format: int32
                  description: Optional task expiry, in seconds from creation.
                  example: 86400
              required:
                - instructions
        required: true
      responses:
        '200':
          description: >-
            Task created successfully. The instructions take effect
            asynchronously once the task is approved.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: >-
                      Task identifier, an approval UUID (UUID v4). T-prefixed
                      identifiers are not returned. Responses always emit
                      lowercase. Requests accept any letter case.
                    example: 550e8400-e29b-41d4-a716-446655440000
                required:
                  - id
        '400':
          description: >-
            Bad Request. The request failed validation. Examples: empty
            instructions, malformed IIBAN, or unknown vault.
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
                    example: 'Request failed validation: instructions must not be empty.'
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
                        example: instructions must not be empty
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '403':
          description: >-
            Forbidden. The caller lacks access to the requested task, vault, or
            organization scope.
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
                    example: >-
                      Caller lacks access to the requested vault or
                      organization.
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
                        example: api key lacks access to the requested vault
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
                        example: Failed to read upstream response from custody service.
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
                        example: Failed to read upstream response from custody service.
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
                        example: Failed to read upstream response from custody service.
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
                        example: Failed to write the response back to the client.
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
                        example: Failed to read upstream response from custody service.
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
                        example: Failed to read upstream response from custody service.
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
                        example: Failed to read upstream response from custody service.
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
                        example: Failed to write the response back to the client.
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
                        example: Fatal error in the gateway layer.
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
                          An unhandled exception occurred while serving the
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
                            example: unexpected error in create-task handler
                          core_error:
                            type: string
                            example: INTERNAL_ERROR
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
            Service Unavailable. The upstream custody service could not be
            reached.
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
