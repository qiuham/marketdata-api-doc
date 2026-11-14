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
source_url: 'https://docs.polymarket.com/api-reference/get-account-backstop-transfers'
updated_at: 2026-11-13
---

# Get Account Backstop Transfers

> Get exact quote cash transfers for backstops of the authenticated account.
Defaults to the last 90 days. Rows are ordered newest first.
If no end time is provided, the current time will be used.
Maximum of 100 entries returned per request.


Request Weight: **10**

Cached 2s — a request served from cache costs **1**


## OpenAPI

````yaml /api-spec/perps-openapi.json get /v1/account/backstops
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
  /v1/account/backstops:
    get:
      summary: Get Account Backstop Transfers
      description: >
        Get exact quote cash transfers for backstops of the authenticated
        account.

        Defaults to the last 90 days. Rows are ordered newest first.

        If no end time is provided, the current time will be used.

        Maximum of 100 entries returned per request.
      operationId: getAccountBackstops
      parameters:
        - name: start_timestamp
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/start_timestamp'
        - name: end_timestamp
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/end_timestamp'
        - name: cursor
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/account_backstops_cursor'
      responses:
        '200':
          description: Account backstop history response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountBackstops'
        '400':
          $ref: '#/components/responses/Error400Response'
        '401':
          $ref: '#/components/responses/Error401Response'
        '408':
          $ref: '#/components/responses/Error408Response'
        '413':
          $ref: '#/components/responses/Error413Response'
        '429':
          $ref: '#/components/responses/Error429Response'
        '500':
          $ref: '#/components/responses/Error500Response'
        '503':
          $ref: '#/components/responses/Error503Response'
      security:
        - polymarket_proxy: []
          polymarket_secret: []
components:
  schemas:
    start_timestamp:
      type: integer
      description: Start timestamp in milliseconds
      example: 1767225600000
    end_timestamp:
      type: integer
      description: End timestamp in milliseconds
      example: 1767229200000
    account_backstops_cursor:
      type: string
      description: >-
        Pass the last row id from the previous page as a decimal string. The
        server resolves its exact timestamp within the authenticated account. An
        opaque URL-safe unpadded base64 JSON cursor with ts (native nanoseconds)
        and id is also accepted. Keep the timestamp window unchanged when
        paging.
    AccountBackstops:
      type: object
      required:
        - data
        - more
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/AccountBackstop'
        more:
          $ref: '#/components/schemas/more'
        coverage:
          type: object
          description: >-
            Present when backstop history is unavailable because its schema is
            pending.
          required:
            - notes
          properties:
            notes:
              type: array
              items:
                type: string
    AccountBackstop:
      type: object
      required:
        - id
        - cross
        - instrument_id
        - asset
        - transferred
        - cash_before
        - cash_after
        - timestamp
        - sequence
      properties:
        id:
          $ref: '#/components/schemas/lid'
        cross:
          $ref: '#/components/schemas/cross'
        instrument_id:
          type: integer
          nullable: true
          description: Absorbed instrument ID, or null for a cross-margin absorption.
        asset:
          $ref: '#/components/schemas/fua'
        transferred:
          $ref: '#/components/schemas/backstop_transferred'
        cash_before:
          $ref: '#/components/schemas/backstop_cash_before'
        cash_after:
          $ref: '#/components/schemas/backstop_cash_after'
        timestamp:
          $ref: '#/components/schemas/ts'
        sequence:
          $ref: '#/components/schemas/history_sequence'
    more:
      type: boolean
      description: More data available
    Error400:
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
          $ref: '#/components/schemas/error'
    Error401:
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
          $ref: '#/components/schemas/error'
    Error408:
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
          $ref: '#/components/schemas/error'
    Error413:
      title: Error413
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
          $ref: '#/components/schemas/error'
    Error429:
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
          $ref: '#/components/schemas/error'
    Error500:
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
          $ref: '#/components/schemas/error'
    Error503:
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
          $ref: '#/components/schemas/error'
    lid:
      type: integer
      description: >-
        Liquidation ID. Identifies one absorption of an account's positions by
        the insurance fund. Probabilistically unique (same guarantees as trade
        IDs).
      example: 1234567890
    cross:
      type: boolean
      description: Whether to use cross margin mode
    fua:
      type: string
      description: Funding asset name
      example: USDC
    backstop_transferred:
      type: string
      description: Signed raw quote margin allocated by the absorption, without rounding.
    backstop_cash_before:
      type: string
      description: Raw quote cash bucket immediately before the absorption.
    backstop_cash_after:
      type: string
      description: >-
        Raw quote cash bucket immediately after the absorption. The difference
        from cash_before is the authoritative wallet delta.
    ts:
      type: integer
      description: >-
        Request timestamp. Unix milliseconds for most operations; Unix seconds
        for withdrawals (must match the on-chain EIP-712 struct verified against
        block.timestamp).
      example: 1767225600000
    history_sequence:
      type: integer
      description: Engine sequence of the history event.
    error:
      type: string
      description: >-
        Error identifier. For domain rejections and transport errors
        (`401`/`404`/`429`/`500`) this is a stable, machine-readable snake_case
        identifier that is part of the API contract and safe to branch on, e.g.
        `insufficient_margin`, `insufficient_balance`, `order_not_found`,
        `reduce_only_invalid`, `price_outside_bounds`, `position_not_found`,
        `position_exists`, `open_orders_exist`, `invalid_margin_mode`,
        `invalid_margin_amount`, `margin_below_required_initial`,
        `account_liquidating`, `instrument_close_only`, `instrument_settled`,
        `settlement_price_unavailable`, `settlement_insurance_insufficient`,
        `settlement_invalid_state`, `unauthorized`, `not_found`.
        `instrument_close_only` means user orders must reduce an existing
        position; `instrument_settled` is permanent. Settlement readiness errors
        leave the instrument and accounts unchanged. For `400` it is a
        human-readable validation detail whose wording may change. See the Error
        handling guide for the domain identifiers. (Post-only / Fill-or-Kill
        outcomes are order statuses such as `post_only_rejected`, not
        rejections.)
      example: insufficient_margin
  responses:
    Error400Response:
      description: |
        Bad request — the request was malformed or failed validation (bad query
        parameters, unparseable body, invalid signature, or a domain pre-check).
        The `error` field is a human-readable validation detail.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error400'
    Error401Response:
      description: >
        Unauthorized — missing or invalid `POLYMARKET-PROXY` /
        `POLYMARKET-SECRET`

        credentials. `error` is `unauthorized`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error401'
    Error408Response:
      description: |
        Request Timeout — the request body was not delivered within the
        gateway's read deadline. Protects against slow uploads holding
        connections open; send the complete body promptly and retry.
        `error` is `request_body_timeout`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error408'
    Error413Response:
      description: |
        Content Too Large — the request body exceeds the gateway's size cap,
        judged on the declared `Content-Length` or the actual stream. Split
        oversized batches into smaller requests. `error` is
        `payload_too_large`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error413'
    Error429Response:
      description: >
        Too Many Requests. `error` distinguishes the limit that was hit:

        `ip_rate_limited` (per-IP token bucket), `action_rate_limited`
        (per-account

        action rate), or `open_orders_limit` (resting open-order cap).
      headers:
        Retry-After:
          description: >
            Whole seconds to wait before retrying. Present only on token-bucket

            rate-limit rejections (`ip_rate_limited` and `action_rate_limited`);
            a

            conservative estimate of when enough capacity will have refilled to

            admit the request. Absent on `open_orders_limit`, which is a
            capacity

            limit, not a rate limit — waiting does not free order slots; cancel

            resting orders or wait for fills instead.
          schema:
            type: integer
            example: 2
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error429'
    Error500Response:
      description: |
        Internal server error. `error` is `internal_error`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error500'
    Error503Response:
      description: |
        Service unavailable — safe to retry with backoff, honoring
        `Retry-After` when present. `error` is
        `service_unavailable`.

        Most causes are a request deliberately shed before it reached the
        engine, so the request definitely did not execute: the replica's
        pod-level in-flight cap (shed before dispatch, with `Retry-After`), a
        database read shed as backpressure under overload (by the local read
        gate or by the database server's concurrency cap — the query never
        executed), a required internal cache that is stale or not yet primed
        and would return wrong data, or a full bounded deferred-write queue.

        On a subset of order/state-mutating routes, this status is also
        returned when the engine round-trip itself times out with zero
        responses observed. That is retryable engine backpressure, but —
        unlike the sheds above — it does not prove non-execution: the command
        may already have been admitted, with its response simply not reaching
        the gateway before the deadline. This status is only used for that
        case on routes that are safe to retry regardless (idempotent
        state-setting, or an engine-side replay guard); routes where a bare
        retry cannot safely resolve the ambiguity keep the outcome a
        non-retryable 500 instead.
      headers:
        Retry-After:
          description: |
            Whole seconds to wait before retrying. Present on pre-dispatch
            in-flight-cap sheds — a transient overload signal, so the hint is
            short and constant.
          schema:
            type: integer
            example: 1
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error503'
  securitySchemes:
    polymarket_proxy:
      type: apiKey
      name: POLYMARKET-PROXY
      in: header
      description: Proxy address
    polymarket_secret:
      type: apiKey
      name: POLYMARKET-SECRET
      in: header
      description: Correponding proxy secret

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
