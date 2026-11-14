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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/get-transaction'
updated_at: 2026-11-13
---

# Get transaction

> Returns a single transaction for the given vault. Available only to callers with access to the vault.

Only custody movements are addressable here. Trade and conversion records are not exposed as custody transactions and are not linked through `ref_id`. Use the Kraken Spot and OTC trade history APIs for those.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml get /v0/insto/custody/vaults/{vault_id}/transactions/{transaction_id}
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
  /v0/insto/custody/vaults/{vault_id}/transactions/{transaction_id}:
    get:
      tags:
        - Custody External API
      summary: Get transaction
      description: >-
        Returns a single transaction for the given vault. Available only to
        callers with access to the vault.


        Only custody movements are addressable here. Trade and conversion
        records are not exposed as custody transactions and are not linked
        through `ref_id`. Use the Kraken Spot and OTC trade history APIs for
        those.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: getV0InstoCustodyVaultsVaultIdTransactionsTransactionId
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
        - in: path
          name: transaction_id
          required: true
          description: >-
            Transaction identifier, as returned in the vault's transaction
            history.
          schema:
            type: string
            example: TXABCDE-FGHIJ-KLMNO2
          style: simple
      responses:
        '200':
          description: The requested transaction.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    description: Transaction identifier.
                    type: string
                    example: TXABCDE-FGHIJ-KLMNO2
                  type:
                    description: >-
                      Transaction type (e.g. `deposit`, `withdrawal`,
                      `custody_transfer`).
                    type: string
                    example: deposit
                  status:
                    description: >-
                      Transaction status, resolved per the asset's crypto or
                      fiat classification (e.g. `pending`, `broadcast`,
                      `completed`, `failed`, `settled`, `on_hold`).
                    type: string
                    example: completed
                  asset:
                    description: Asset code of the transaction amount.
                    type: string
                    example: BTC
                  asset_class:
                    description: >-
                      Asset class of the transaction amount (e.g. `currency`,
                      `tokenized_asset`).
                    type: string
                    example: currency
                  amount:
                    description: >-
                      Transaction amount, fixed-precision decimal as string.
                      Spend amounts are negative.
                    type: string
                    example: '1.25'
                  time:
                    description: Transaction time (ISO-8601).
                    type: string
                    example: '2024-05-14T22:13:20.000Z'
                  transaction_hash:
                    description: On-chain transaction hash, when available.
                    type: string
                    example: >-
                      0x4a7d1ed414474e4033ac29ccb8653d9b00d3f1c9a3b7e5d2c8f6a4b1e9d7c5a3
                  ref_id:
                    description: >-
                      Reference identifier of the originating operation, when
                      available. For funding deposits and withdrawals this is
                      the `FT`-prefixed funding transfer reference, the
                      successor to the legacy `details.core.funding_reference`
                      field. Other movements carry other prefixes, such as `CT`
                      for custody transfers, `EL` for earn allocations, and `T`
                      for trade-settlement movements. There is no separate
                      `funding_reference` field on this API.
                    type: string
                    example: FTABCDE-FGHIJ-KLMNO2
                  fee_amount:
                    description: >-
                      Fee amount charged for the transaction, fixed-precision
                      decimal as string. Present when a fee applies.
                    type: string
                    example: '0.01'
                  fee_asset:
                    description: >-
                      Asset code the fee is charged in. Present when a fee
                      applies.
                    type: string
                    example: BTC
                  fee_asset_class:
                    description: >-
                      Asset class of the fee asset (e.g. `currency`,
                      `tokenized_asset`). Present when a fee applies.
                    type: string
                    example: currency
                  extension_type:
                    description: >-
                      Custody extension type for extended transactions (e.g.
                      `post_trade_settlement`), when available.
                    type: string
                    example: post_trade_settlement
                  source_address:
                    description: >-
                      Address or account the funds moved from, when available.
                      The sender address for deposits, the vault's sending
                      address for withdrawals, and the counterparty account
                      identifier (IIBAN) for internal transfers. Omitted when
                      the movement has no source address.
                    type: string
                    example: bc1q9h6yzs4h29m0zqf6l2dv4kv9m8g3xj7t5c0pzr
                  destination_address:
                    description: >-
                      Destination address of the transaction, when available.
                      The vault's receiving address for deposits, the recipient
                      address for withdrawals, and the counterparty account
                      identifier (IIBAN) for internal transfers. Omitted when
                      the movement has no destination address.
                    type: string
                    example: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq
                  task:
                    description: >-
                      Linked custody task that created this transaction. Carries
                      `id` (approval UUID) and optional `initiator`. Omitted
                      when no task is linked. The transaction object does not
                      also return `task_id` or `approval_id`. Approver history
                      remains on `GET /v0/insto/custody/tasks/{task_id}`.
                    type: object
                    properties:
                      id:
                        description: >-
                          Task identifier of the linked custody task, an
                          approval UUID (UUID v4). Use this value with `GET
                          /v0/insto/custody/tasks/{task_id}`, and with the
                          `task_id` filter on List transactions. Responses
                          always emit lowercase. Requests accept any letter
                          case.
                        type: string
                        format: uuid
                        example: 550e8400-e29b-41d4-a716-446655440000
                      initiator:
                        description: >-
                          User or API key that initiated the linked task, when
                          available. Same shape as Get Task `initiator`. Omitted
                          when no usable initiator identity is present.
                        type: object
                        properties:
                          full_name:
                            description: >-
                              Display name of the initiator at the time the task
                              was created.
                            type: string
                            example: Alex Doe
                          role:
                            description: >-
                              Role assigned to the initiator at the time the
                              task was created.
                            type: string
                            example: vault_admin
                          ip_address:
                            description: >-
                              Source IP address recorded when the task was
                              initiated.
                            type: string
                            example: 203.0.113.10
                          iiban:
                            description: >-
                              16-char IIBAN identifying the initiating user or
                              API key.
                            type: string
                            example: ABCD EFGH IJKL MNOP
                    required:
                      - id
                  source_wallet:
                    description: >-
                      Wallet the funds moved out of, when available. Present on
                      withdrawals, and on transfers where the vault holds the
                      sending side. Omitted otherwise. `type` is included when
                      portfolio supplies a non-empty wallet type (for example
                      `spot`, `custody_staking`, `custody_pledged_collateral`).
                    type: object
                    properties:
                      id:
                        description: Wallet identifier of the sending wallet.
                        type: string
                        example: WABCDEF234567A
                      type:
                        description: >-
                          Portfolio wallet type when available (for example
                          `spot`, `custody_staking`, `custody_otc_trading`).
                          Omitted when empty or unknown.
                        type: string
                        example: spot
                    required:
                      - id
                  destination_wallet:
                    description: >-
                      Wallet the funds moved into, when available. Present on
                      deposits, and on transfers where the vault holds the
                      receiving side. Omitted otherwise. `type` is included when
                      portfolio supplies a non-empty wallet type (for example
                      `spot`, `custody_staking`, `custody_pledged_collateral`).
                    type: object
                    properties:
                      id:
                        description: Wallet identifier of the receiving wallet.
                        type: string
                        example: WBCDEFG345678B
                      type:
                        description: >-
                          Portfolio wallet type when available (for example
                          `spot`, `custody_staking`, `custody_otc_trading`).
                          Omitted when empty or unknown.
                        type: string
                        example: custody_staking
                    required:
                      - id
                required:
                  - id
                  - type
                  - status
                  - asset
                  - asset_class
                  - amount
                  - time
        '400':
          description: >-
            Bad Request. The request failed validation. Examples: unknown filter
            value, malformed ID, or invalid date range.
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
                    type: object
                    properties:
                      message:
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
            Forbidden. The caller lacks access to the requested vault, or the
            transaction does not belong to it.
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
                    example: Caller lacks access to the requested resource.
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
                        example: Caller lacks access to the requested resource.
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
                    example: Downstream custody service is temporarily unreachable.
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
