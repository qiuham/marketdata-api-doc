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
source_url: 'https://docs.polymarket.com/cn/api-reference/get-position-share-card-snapshots'
updated_at: 2026-11-13
---

# 批量获取仓位分享卡快照

> Build share-card numbers, candles and trade markers for a registered account.
Supply up to 20 active instruments and 4 historical fills, with at least one selection.
History keys use instrument_id, trade_id and the public fill timestamp in milliseconds.
Trade IDs are UInt64 decimal strings; returned IDs omit leading zeroes.
Duplicates and explicit null arrays are rejected. Weight is max(10, active + 7 × history).

Responses use Cache-Control: private, no-store. The route is public; valid owner
authentication reveals leverage and pnl_percent. Both fields are null for anonymous
callers and other accounts. Invalid supplied credentials return 401.

Active snapshots use captured state; history ends after the selected fill. A fill
that closes a cycle, fully or by crossing, returns that closed cycle's card.
The cycle it opens is served by the active card or by its later fills.
PositionCardSnapshot defines valuation, PnL and leverage availability.

Results preserve order within active and history. Only ok items contain snapshot.
not_found means no current position or owned fill within history_as_of_at; gateways
may have different horizons. history_pending means a known fill or a position needing
bootstrap is ahead of completed history, or the self-match index coverage gate is not
armed for historical cards; retry with backoff. history_limit means the
reconstruction window lacks the opener. resource_limit means a row, memory or chart
bound was exceeded. temporarily_unavailable includes deadlines and transient pricing
or dependency failures. unavailable includes unsafe accounting, self-matches, backstop
transfers, non-fill repairs and legacy multi-leg selections with unknowable fill order.

Candles include the selected minute's aggregate, without a per-fill cutoff inside it.
Charts retain the left boundary bucket and at least one hour of context, with at most
22 candles and 256 markers. Unknown accounts and malformed input return 400.
Admission and shared dependency failures return 503; retry with backoff.
HTTP 413 is reserved for an oversized request body.




## OpenAPI

````yaml api-spec/perps-openapi.json POST /v1/info/position-snapshots
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
  /v1/info/position-snapshots:
    post:
      summary: Get Position Share Card Snapshots
      description: >
        Build share-card numbers, candles and trade markers for a registered
        account.

        Supply up to 20 active instruments and 4 historical fills, with at least
        one selection.

        History keys use instrument_id, trade_id and the public fill timestamp
        in milliseconds.

        Trade IDs are UInt64 decimal strings; returned IDs omit leading zeroes.

        Duplicates and explicit null arrays are rejected. Weight is max(10,
        active + 7 × history).


        Responses use Cache-Control: private, no-store. The route is public;
        valid owner

        authentication reveals leverage and pnl_percent. Both fields are null
        for anonymous

        callers and other accounts. Invalid supplied credentials return 401.


        Active snapshots use captured state; history ends after the selected
        fill. A fill

        that closes a cycle, fully or by crossing, returns that closed cycle's
        card.

        The cycle it opens is served by the active card or by its later fills.

        PositionCardSnapshot defines valuation, PnL and leverage availability.


        Results preserve order within active and history. Only ok items contain
        snapshot.

        not_found means no current position or owned fill within
        history_as_of_at; gateways

        may have different horizons. history_pending means a known fill or a
        position needing

        bootstrap is ahead of completed history, or the self-match index
        coverage gate is not

        armed for historical cards; retry with backoff. history_limit means the

        reconstruction window lacks the opener. resource_limit means a row,
        memory or chart

        bound was exceeded. temporarily_unavailable includes deadlines and
        transient pricing

        or dependency failures. unavailable includes unsafe accounting,
        self-matches, backstop

        transfers, non-fill repairs and legacy multi-leg selections with
        unknowable fill order.


        Candles include the selected minute's aggregate, without a per-fill
        cutoff inside it.

        Charts retain the left boundary bucket and at least one hour of context,
        with at most

        22 candles and 256 markers. Unknown accounts and malformed input return
        400.

        Admission and shared dependency failures return 503; retry with backoff.

        HTTP 413 is reserved for an oversized request body.
      operationId: getPublicPositionSnapshots
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PositionSnapshotsRequest'
      responses:
        '200':
          description: Share-card snapshots with independent item statuses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PositionSnapshots'
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
        - {}
        - polymarket_proxy: []
          polymarket_secret: []
components:
  schemas:
    PositionSnapshotsRequest:
      type: object
      additionalProperties: false
      required:
        - address
      properties:
        address:
          $ref: '#/components/schemas/address'
        active_instrument_ids:
          type: array
          maxItems: 20
          uniqueItems: true
          items:
            type: integer
            minimum: 0
            maximum: 4294967295
        history_fills:
          type: array
          maxItems: 4
          uniqueItems: true
          description: >-
            Selected public AccountTrade fill keys, in response order.
            Deduplicated by (instrument_id, trade_id).
          items:
            $ref: '#/components/schemas/PositionSnapshotFill'
    PositionSnapshots:
      type: object
      required:
        - active
        - history
        - history_as_of_at
      properties:
        history_as_of_at:
          type: integer
          minimum: 0
          description: >-
            Event time of the serving gateway's captured state and
            completed-history prefix, in Unix milliseconds. Missing trades are
            not_found at this horizon; horizons can differ by gateway.
        active:
          type: array
          items:
            $ref: '#/components/schemas/PositionSnapshotResult'
        history:
          type: array
          items:
            $ref: '#/components/schemas/PositionSnapshotResult'
    address:
      type: string
      description: Address
      example: '0x1234567890abcdef1234567890abcdef12345678'
    PositionSnapshotFill:
      type: object
      additionalProperties: false
      required:
        - instrument_id
        - trade_id
        - timestamp
      properties:
        instrument_id:
          type: integer
          minimum: 0
          maximum: 4294967295
        trade_id:
          type: string
          pattern: ^[0-9]+$
          minLength: 1
          maxLength: 20
          description: Decimal UInt64 trade ID from the public fills API.
        timestamp:
          type: integer
          minimum: 0
          maximum: 18446744073709
          description: Public fill timestamp in Unix milliseconds.
    PositionSnapshotResult:
      type: object
      required:
        - status
      properties:
        instrument_id:
          $ref: '#/components/schemas/iid'
        trade_id:
          type: string
        status:
          $ref: '#/components/schemas/PositionSnapshotStatus'
        snapshot:
          $ref: '#/components/schemas/PositionCardSnapshot'
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
    iid:
      type: integer
      description: Instrument ID
      example: 1
    PositionSnapshotStatus:
      type: string
      enum:
        - ok
        - not_found
        - history_pending
        - history_limit
        - resource_limit
        - temporarily_unavailable
        - unavailable
    PositionCardSnapshot:
      type: object
      required:
        - position_cycle_id
        - side
        - started_at
        - as_of_at
        - is_closed
        - size_after
        - entry_price
        - as_of_price
        - pnl
        - pnl_percent
        - leverage
        - chart
      properties:
        position_cycle_id:
          type: string
          description: Opaque stable cycle identity; a flip creates a new identity.
        side:
          type: string
          enum:
            - long
            - short
        started_at:
          type: integer
          minimum: 0
          description: Cycle opening timestamp in Unix milliseconds.
        as_of_at:
          type: integer
          minimum: 0
          description: >-
            Captured state time for active positions; selected fill time for
            history. Unix milliseconds.
        is_closed:
          type: boolean
        size_after:
          type: string
          description: Absolute remaining quantity; side provides its direction.
        entry_price:
          type: string
          description: >-
            Remaining position's weighted entry; last entry before closing when
            flat. Formatted to instrument price precision.
        as_of_price:
          type: string
          description: >-
            Captured mark for active positions; selected fill price for
            historical snapshots.
        pnl:
          type: string
          description: >-
            Gross unrealized PnL on remaining size while open; gross realized
            cycle PnL when closed. Excludes fees, funding and previous cycles.
        pnl_percent:
          type: string
          nullable: true
          description: >-
            PnL times leverage divided by entry notional, times 100. Open cycles
            use unrealized PnL and entry notional on remaining size, excluding
            realized partial closes. Closed cycles use total opening/add
            notional, including re-additions after partial closes. Only returned
            to the authenticated owner; otherwise null. Uses nominal entry
            margin; portfolio return_on_equity uses actual initial margin and
            may differ.
        leverage:
          type: integer
          minimum: 0
          nullable: true
          description: >-
            Only returned to the authenticated account owner; otherwise null.
            Current leverage for active positions; captured selected-fill
            leverage for history, never today's setting. Uncaptured values are
            null, including fills from older, mixed-version or rollback writers.
            Replaying a fill without leverage capture can turn a previously
            captured value to null.
        chart:
          $ref: '#/components/schemas/PositionSnapshotChart'
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
    PositionSnapshotChart:
      type: object
      required:
        - candles
        - markers
      properties:
        candles:
          type: array
          maxItems: 22
          items:
            $ref: '#/components/schemas/PositionSnapshotCandle'
        markers:
          type: array
          maxItems: 256
          items:
            $ref: '#/components/schemas/PositionSnapshotMarker'
    PositionSnapshotCandle:
      type: object
      required:
        - position
        - open
        - high
        - low
        - close
      properties:
        position:
          type: number
          description: Normalized horizontal chart coordinate from 0 to 1.
        open:
          type: number
        high:
          type: number
        low:
          type: number
        close:
          type: number
    PositionSnapshotMarker:
      type: object
      required:
        - position
        - kind
      properties:
        position:
          type: number
        kind:
          type: string
          enum:
            - increase
            - decrease
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
