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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/list-vault-asset-balances'
updated_at: 2026-11-13
---

# List vault asset balances

> Returns per-asset balances for a vault, including spot, hold, available, staked, and pledged components for each asset. Each row includes asset metadata and optional quote-currency valuations. Use `quote_asset` to select the valuation currency (defaults to USD). Numeric strings are always returned at full upstream precision.

This is the endpoint to use whenever you need asset codes and quantities. The `quote_value` on `GET /v0/insto/custody/vaults` and `GET /v0/insto/custody/vaults/{vault_id}/balances` is a single aggregate valuation and cannot be decomposed into holdings.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml get /v0/insto/custody/vaults/{vault_id}/assets/balances
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
  /v0/insto/custody/vaults/{vault_id}/assets/balances:
    get:
      tags:
        - Custody External API
      summary: List vault asset balances
      description: >-
        Returns per-asset balances for a vault, including spot, hold, available,
        staked, and pledged components for each asset. Each row includes asset
        metadata and optional quote-currency valuations. Use `quote_asset` to
        select the valuation currency (defaults to USD). Numeric strings are
        always returned at full upstream precision.


        This is the endpoint to use whenever you need asset codes and
        quantities. The `quote_value` on `GET /v0/insto/custody/vaults` and `GET
        /v0/insto/custody/vaults/{vault_id}/balances` is a single aggregate
        valuation and cannot be decomposed into holdings.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: getV0InstoCustodyVaultsVaultIdAssetsBalances
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
        - in: query
          name: quote_asset
          description: >-
            Currency code used to value quote fields on each row. Defaults to
            USD when omitted; only USD is currently accepted.
          schema:
            type: string
          example: USD
          style: form
      responses:
        '200':
          description: >-
            OK. Returns per-asset balances for the vault as an envelope. The
            `result` field is the array of balance rows; `quote_asset` carries
            the quote currency once for the whole response.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    description: Per-asset balance rows for the vault.
                    type: array
                    items:
                      type: object
                      properties:
                        asset:
                          description: Asset code (e.g. `BTC`, `USD`, `AAPLX`).
                          type: string
                          example: BTC
                        asset_class:
                          description: >-
                            Asset class wire label for the row asset (e.g.
                            `currency`, `tokenized_asset`).
                          type: string
                          example: currency
                        name:
                          description: Short display name of the asset.
                          type: string
                          example: Bitcoin
                        name_full:
                          description: Full display name of the asset.
                          type: string
                          example: Bitcoin
                        symbol:
                          description: Trading or display symbol for the asset.
                          type: string
                          example: BTC
                        decimals:
                          description: Maximum decimal precision for the asset.
                          type: integer
                          format: int32
                          example: 8
                        display_decimals:
                          description: >-
                            Decimal places used when displaying the asset in the
                            UI.
                          type: integer
                          format: int32
                          example: 8
                        rate_decimals:
                          description: >-
                            Decimal places used for exchange rates involving the
                            asset.
                          type: integer
                          format: int32
                          example: 8
                        funding_decimals:
                          description: Decimal places used for funding amounts.
                          type: integer
                          format: int32
                          example: 8
                        min_lot:
                          description: >-
                            Minimum tradable or transferable lot size as a
                            fixed-precision decimal string.
                          type: string
                          example: '0.00010000'
                        reserve:
                          description: Whether the asset is a reserve asset.
                          type: boolean
                          example: false
                        virtual:
                          description: >-
                            Whether the asset is crypto/virtual (`true`) or fiat
                            (`false`).
                          type: boolean
                          example: true
                        launch_time:
                          nullable: true
                          description: >-
                            RFC 3339 UTC timestamp when the asset launched, when
                            applicable.
                          type: string
                          format: date-time
                          example: '2024-11-14T22:13:20Z'
                        metadata:
                          description: Asset-specific display metadata.
                          type: object
                          properties:
                            color_code:
                              description: >-
                                Hex color code used when rendering the asset in
                                the UI.
                              type: string
                              example: '#F7931A'
                          required:
                            - color_code
                        balance:
                          description: >-
                            Total balance for this asset in the vault (spot +
                            staked + pledged), as a fixed-precision decimal
                            string.
                          type: string
                          example: '1.50000000'
                        quote_value_change_24h:
                          nullable: true
                          description: >-
                            24h percentage change of this asset's quote-valued
                            spot balance versus the prior day, as a percentage
                            string (not a quote-currency amount); `null` when no
                            prior reference exists.
                          type: string
                          example: '1.25'
                        spot_balance:
                          description: >-
                            Spot balance component for this asset, in native
                            units, as a fixed-precision decimal string.
                          type: string
                          example: '1.50000000'
                        hold_balance:
                          description: >-
                            Balance on hold (e.g. pending withdrawals), in
                            native units, as a fixed-precision decimal string.
                          type: string
                          example: '0.00000000'
                        available_balance:
                          description: >-
                            Available balance for this asset, in native units,
                            as a fixed-precision decimal string.
                          type: string
                          example: '1.50000000'
                        staked_balance:
                          description: >-
                            Aggregated staked and earn balance for this asset,
                            in native units, as a fixed-precision decimal
                            string. Zero when none is staked.
                          type: string
                          example: '0.00000000'
                        pledged_balance:
                          nullable: true
                          description: >-
                            Pledged balance component, in native units, when
                            applicable; otherwise `null`.
                          type: string
                          example: '0.00000000'
                        quote_value:
                          nullable: true
                          description: >-
                            Total balance valued in the quote currency; `null`
                            when no quote rate is available.
                          type: string
                          example: '97500.00'
                        quote_spot_value:
                          nullable: true
                          description: >-
                            Spot balance valued in the quote currency; `null`
                            when no quote rate is available.
                          type: string
                          example: '97500.00'
                        quote_available_value:
                          nullable: true
                          description: >-
                            Available balance valued in the quote currency;
                            `null` when no quote rate is available.
                          type: string
                          example: '97500.00'
                        quote_price:
                          nullable: true
                          description: >-
                            Price of one unit of the asset in the quote
                            currency; `null` when no quote rate is available.
                          type: string
                          example: '65000.00'
                      required:
                        - asset
                        - asset_class
                        - name
                        - name_full
                        - symbol
                        - decimals
                        - display_decimals
                        - rate_decimals
                        - funding_decimals
                        - min_lot
                        - reserve
                        - virtual
                        - metadata
                        - balance
                        - spot_balance
                        - hold_balance
                        - available_balance
                        - staked_balance
                  quote_asset:
                    description: >-
                      Quote asset code the quote fields are valued in (e.g.
                      `USD`). Defaults to USD when the `quote_asset` parameter
                      is omitted. Currency-only by contract.
                    type: string
                    example: USD
                required:
                  - result
                  - quote_asset
              examples:
                vaultAssetBalances:
                  summary: Sample vault asset balances
                  value:
                    result:
                      - asset: BTC
                        asset_class: currency
                        name: Bitcoin
                        name_full: Bitcoin
                        symbol: BTC
                        decimals: 8
                        display_decimals: 8
                        rate_decimals: 8
                        funding_decimals: 8
                        min_lot: '0.00010000'
                        reserve: false
                        virtual: true
                        metadata:
                          color_code: '#F7931A'
                        balance: '1.50000000'
                        quote_value_change_24h: '1.25'
                        spot_balance: '1.50000000'
                        hold_balance: '0.00000000'
                        available_balance: '1.50000000'
                        staked_balance: '0.00000000'
                        pledged_balance: '0.00000000'
                        quote_value: '97500.00'
                        quote_spot_value: '97500.00'
                        quote_available_value: '97500.00'
                        quote_price: '65000.00'
                      - asset: USD
                        asset_class: currency
                        name: US Dollar
                        name_full: US Dollar
                        symbol: USD
                        decimals: 4
                        display_decimals: 2
                        rate_decimals: 4
                        funding_decimals: 4
                        min_lot: '0.0100'
                        reserve: false
                        virtual: false
                        metadata:
                          color_code: '#85BB65'
                        balance: '10000.0000'
                        spot_balance: '10000.0000'
                        hold_balance: '0.0000'
                        available_balance: '10000.0000'
                        staked_balance: '0.0000'
                        quote_value: '10000.00'
                        quote_spot_value: '10000.00'
                        quote_available_value: '10000.00'
                        quote_price: '1.0000'
                    quote_asset: USD
        '400':
          description: >-
            Bad Request. The request failed validation, or quote_asset is not a
            supported quote currency.
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
                    example: Invalid quote parameter.
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
                        example: Invalid quote parameter.
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '403':
          description: Forbidden. The caller lacks access to the requested vault.
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
