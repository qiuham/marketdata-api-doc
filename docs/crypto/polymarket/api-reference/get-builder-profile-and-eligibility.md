---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/get-builder-profile-and-eligibility'
updated_at: 2026-11-13
---

# Get builder profile and eligibility

> Public builder profile for an address. Returns the saved display name and
current registration, enablement, platform admission and fee-cap fields.
The name is null for unregistered addresses or builders without a saved name.




## OpenAPI

````yaml /api-spec/perps-openapi.json get /v1/info/builder
openapi: 3.0.3
info:
  title: Polymarket Perps HTTP API
  version: 1.0.0
  description: HTTP API for Polymarket perpetual trading system.
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
servers:
  - url: https://api.perpetuals.polymarket.com
    description: Production Perps HTTP API
security: []
paths:
  /v1/info/builder:
    get:
      summary: Get builder profile and eligibility
      description: >
        Public builder profile for an address. Returns the saved display name
        and

        current registration, enablement, platform admission and fee-cap fields.

        The name is null for unregistered addresses or builders without a saved
        name.
      operationId: getBuilder
      parameters:
        - in: query
          name: address
          required: true
          schema:
            type: string
            description: Address
            example: '0x1234567890abcdef1234567890abcdef12345678'
      responses:
        '200':
          description: Builder profile and current eligibility.
          content:
            application/json:
              schema:
                allOf:
                  - type: object
                    required:
                      - address
                      - registered
                      - enabled
                      - admission_enabled
                      - max_fee_rate
                    properties:
                      address:
                        type: string
                        description: Address
                        example: '0x1234567890abcdef1234567890abcdef12345678'
                      registered:
                        type: boolean
                      enabled:
                        type: boolean
                        description: >-
                          Builder is enabled for new requests. Existing saved
                          terms remain valid when disabled.
                      admission_enabled:
                        type: boolean
                        description: >-
                          Platform builder code admission switch. Initially
                          false.
                      max_fee_rate:
                        type: string
                        description: >-
                          Additional builder fee as a decimal fraction of
                          executed notional, from 0 through 0.001 (10 basis
                          points). Zero approval revokes future admission. Never
                          a percentage string.
                        example: '0.001'
                  - type: object
                    required:
                      - name
                    properties:
                      name:
                        type: string
                        nullable: true
                        description: >-
                          Saved builder display name, or null when this address
                          is not a registered builder or has no saved name.
        '400':
          description: >
            Bad request — the request was malformed or failed validation (bad
            query

            parameters, unparseable body, invalid signature, or a domain
            pre-check).

            The `error` field is a human-readable validation detail. Rejections
            also

            carry the server `ts` in Unix milliseconds and a `ref` that support
            can

            use to locate the matching structured trace.
          content:
            application/json:
              schema:
                title: Error400
                type: object
                required:
                  - status
                  - error
                properties:
                  status:
                    type: string
                    enum:
                      - err
                  error:
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`,
                      `settlement_close_only_required`, `unauthorized`,
                      `not_found`. `instrument_close_only` means user orders
                      must reduce an existing position; `instrument_settled` is
                      permanent. Settlement readiness errors leave the
                      instrument and accounts unchanged. For `400` it is a
                      human-readable validation detail whose wording may change.
                      See the Error handling guide for the domain identifiers.
                      (Post-only / Fill-or-Kill outcomes are order statuses such
                      as `post_only_rejected`, not rejections.)
                    example: insufficient_margin
                  arts:
                    type: integer
                    x-js-safe-integer: true
                    description: >-
                      Gateway arrival timestamp captured at handler entry, in
                      Unix milliseconds.
                    example: 1767225600000
                  ts:
                    type: integer
                    x-js-safe-integer: true
                    description: Server rejection timestamp in Unix milliseconds.
                    example: 1767225600000
                  ref:
                    type: string
                    description: >-
                      Unique server-generated rejection reference. Include this
                      value when asking support to locate the corresponding
                      structured rejection trace.
                    example: g-0011223344556
        '401':
          description: >
            Unauthorized — missing or invalid `POLYMARKET-PROXY` /
            `POLYMARKET-SECRET`

            credentials. `error` is `unauthorized`.
          content:
            application/json:
              schema:
                title: Error401
                type: object
                required:
                  - status
                  - error
                properties:
                  status:
                    type: string
                    enum:
                      - err
                  error:
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`,
                      `settlement_close_only_required`, `unauthorized`,
                      `not_found`. `instrument_close_only` means user orders
                      must reduce an existing position; `instrument_settled` is
                      permanent. Settlement readiness errors leave the
                      instrument and accounts unchanged. For `400` it is a
                      human-readable validation detail whose wording may change.
                      See the Error handling guide for the domain identifiers.
                      (Post-only / Fill-or-Kill outcomes are order statuses such
                      as `post_only_rejected`, not rejections.)
                    example: insufficient_margin
        '408':
          description: |
            Request Timeout — the request body was not delivered within the
            gateway's read deadline. Protects against slow uploads holding
            connections open; send the complete body promptly and retry.
            `error` is `request_body_timeout`.
          content:
            application/json:
              schema:
                title: Error408
                type: object
                required:
                  - status
                  - error
                properties:
                  status:
                    type: string
                    enum:
                      - err
                  error:
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`,
                      `settlement_close_only_required`, `unauthorized`,
                      `not_found`. `instrument_close_only` means user orders
                      must reduce an existing position; `instrument_settled` is
                      permanent. Settlement readiness errors leave the
                      instrument and accounts unchanged. For `400` it is a
                      human-readable validation detail whose wording may change.
                      See the Error handling guide for the domain identifiers.
                      (Post-only / Fill-or-Kill outcomes are order statuses such
                      as `post_only_rejected`, not rejections.)
                    example: insufficient_margin
        '429':
          description: >
            Too Many Requests. `error` distinguishes the limit that was hit:

            `ip_rate_limited` (per-IP token bucket), `action_rate_limited`
            (per-account

            action rate), or `open_orders_limit` (resting open-order cap).
          headers:
            Retry-After:
              description: >
                Whole seconds to wait before retrying. Present only on
                token-bucket

                rate-limit rejections (`ip_rate_limited` and
                `action_rate_limited`); a

                conservative estimate of when enough capacity will have refilled
                to

                admit the request. Absent on `open_orders_limit`, which is a
                capacity

                limit, not a rate limit — waiting does not free order slots;
                cancel

                resting orders or wait for fills instead.
              schema:
                type: integer
                x-js-safe-integer: true
                example: 2
          content:
            application/json:
              schema:
                title: Error429
                type: object
                required:
                  - status
                  - error
                properties:
                  status:
                    type: string
                    enum:
                      - err
                  error:
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`,
                      `settlement_close_only_required`, `unauthorized`,
                      `not_found`. `instrument_close_only` means user orders
                      must reduce an existing position; `instrument_settled` is
                      permanent. Settlement readiness errors leave the
                      instrument and accounts unchanged. For `400` it is a
                      human-readable validation detail whose wording may change.
                      See the Error handling guide for the domain identifiers.
                      (Post-only / Fill-or-Kill outcomes are order statuses such
                      as `post_only_rejected`, not rejections.)
                    example: insufficient_margin
        '500':
          description: |
            Internal server error. `error` is `internal_error`.
          content:
            application/json:
              schema:
                title: Error500
                type: object
                required:
                  - status
                  - error
                properties:
                  status:
                    type: string
                    enum:
                      - err
                  error:
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`,
                      `settlement_close_only_required`, `unauthorized`,
                      `not_found`. `instrument_close_only` means user orders
                      must reduce an existing position; `instrument_settled` is
                      permanent. Settlement readiness errors leave the
                      instrument and accounts unchanged. For `400` it is a
                      human-readable validation detail whose wording may change.
                      See the Error handling guide for the domain identifiers.
                      (Post-only / Fill-or-Kill outcomes are order statuses such
                      as `post_only_rejected`, not rejections.)
                    example: insufficient_margin
        '503':
          description: >
            Service unavailable — safe to retry with backoff, honoring

            `Retry-After` when present. `error` is `service_unavailable`.


            Most causes are a request deliberately shed before it reached the

            engine, so the request definitely did not execute: the replica's

            pod-level in-flight cap (shed before dispatch, with `Retry-After`),
            a

            database read shed as backpressure under overload (by the local read

            gate or by the database server's concurrency cap — the query never

            executed), a required internal cache that is stale or not yet primed

            and would return wrong data, or a full bounded deferred-write queue.


            On a subset of order/state-mutating routes, this status is also

            returned when the engine round-trip itself times out with zero

            responses observed. That is retryable engine backpressure, but —

            unlike the sheds above — it does not prove non-execution: the
            command

            may already have been admitted, with its response simply not
            reaching

            the gateway before the deadline. This status is only used for that

            case on routes that are safe to retry regardless (idempotent

            state-setting, or an engine-side replay guard); routes where a bare

            retry cannot safely resolve the ambiguity keep the outcome a

            non-retryable 500 instead.
          headers:
            Retry-After:
              description: >
                Whole seconds to wait before retrying. Present on pre-dispatch

                in-flight-cap sheds — a transient overload signal, so the hint
                is

                short and constant.
              schema:
                type: integer
                x-js-safe-integer: true
                example: 1
          content:
            application/json:
              schema:
                title: Error503
                type: object
                required:
                  - status
                  - error
                properties:
                  status:
                    type: string
                    enum:
                      - err
                  error:
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`,
                      `settlement_close_only_required`, `unauthorized`,
                      `not_found`. `instrument_close_only` means user orders
                      must reduce an existing position; `instrument_settled` is
                      permanent. Settlement readiness errors leave the
                      instrument and accounts unchanged. For `400` it is a
                      human-readable validation detail whose wording may change.
                      See the Error handling guide for the domain identifiers.
                      (Post-only / Fill-or-Kill outcomes are order statuses such
                      as `post_only_rejected`, not rejections.)
                    example: insufficient_margin
      security: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
