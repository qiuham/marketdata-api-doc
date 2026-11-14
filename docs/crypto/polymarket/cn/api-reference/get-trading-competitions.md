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
source_url: 'https://docs.polymarket.com/cn/api-reference/get-trading-competitions'
updated_at: 2026-11-13
---

# 获取交易竞赛

> List trading competitions for the carousel, newest first, with the live
competition's ID (for "Back to live") and the one the Competitions tab
should open on: the live competition, else the next upcoming one, else
the most recently ended one.

Internal competitions are listed only when `address` is on their
allowlist. This is a display filter, not access control: the info API is
unauthenticated, and an internal competition can be read by ID.




## OpenAPI

````yaml api-spec/perps-openapi.json GET /v1/info/competitions
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
  /v1/info/competitions:
    get:
      summary: Get Trading Competitions
      description: |
        List trading competitions for the carousel, newest first, with the live
        competition's ID (for "Back to live") and the one the Competitions tab
        should open on: the live competition, else the next upcoming one, else
        the most recently ended one.

        Internal competitions are listed only when `address` is on their
        allowlist. This is a display filter, not access control: the info API is
        unauthenticated, and an internal competition can be read by ID.
      operationId: getCompetitions
      parameters:
        - name: address
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/address'
      responses:
        '200':
          description: Competition list.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompetitionList'
        '400':
          $ref: '#/components/responses/CompetitionRead_Error400Response'
        '429':
          $ref: '#/components/responses/CompetitionRead_Error429Response'
        '500':
          $ref: '#/components/responses/CompetitionRead_Error500Response'
        '503':
          $ref: '#/components/responses/CompetitionRead_Error503Response'
      security: []
components:
  schemas:
    address:
      type: string
      description: Address
      example: '0x1234567890abcdef1234567890abcdef12345678'
    CompetitionList:
      type: object
      required:
        - timestamp
        - competitions
      properties:
        timestamp:
          $ref: '#/components/schemas/update_timestamp'
        live_competition_id:
          $ref: '#/components/schemas/competition_id'
        landing_competition_id:
          $ref: '#/components/schemas/competition_id'
        competitions:
          type: array
          description: Newest first.
          items:
            $ref: '#/components/schemas/CompetitionSummary'
    update_timestamp:
      type: integer
      description: Update timestamp in milliseconds
      example: 1767225600000
    competition_id:
      type: integer
      minimum: 1
      description: Trading competition ID
      example: 3
    CompetitionSummary:
      type: object
      description: One competition in the carousel.
      required:
        - competition_id
        - number
        - name
        - sector_label
        - status
        - start_time
        - end_time
        - prize_pool
        - prize_asset_id
        - internal
      properties:
        competition_id:
          $ref: '#/components/schemas/competition_id'
        number:
          type: integer
          description: Sequential number shown as "Competition
        name:
          type: string
        sector_label:
          type: string
          description: Theme or sector label, e.g. "Semis"; empty when none
        status:
          $ref: '#/components/schemas/competition_status'
        start_time:
          type: integer
          description: Start, inclusive, in Unix milliseconds
        end_time:
          type: integer
          description: End, exclusive, in Unix milliseconds
        prize_pool:
          type: string
          description: Total prize pool as a numeric string
          example: '50000'
        prize_asset_id:
          type: integer
          description: Asset prizes are paid in
        internal:
          type: boolean
          description: Visible only to its allowlist (internal test competitions)
    CompetitionRead_Error400:
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
          $ref: '#/components/schemas/CompetitionRead_error'
        arts:
          $ref: '#/components/schemas/arts'
        ts:
          $ref: '#/components/schemas/CompetitionRead_timestamp'
          description: Server rejection timestamp in Unix milliseconds.
        ref:
          $ref: '#/components/schemas/ref'
    CompetitionRead_Error429:
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
          $ref: '#/components/schemas/CompetitionRead_error'
    CompetitionRead_Error500:
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
          $ref: '#/components/schemas/CompetitionRead_error'
    CompetitionRead_Error503:
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
          $ref: '#/components/schemas/CompetitionRead_error'
    competition_status:
      type: string
      description: >-
        Competition lifecycle status. `upcoming` before start, `live` while
        running, `in_review` from the end until every prize is paid (ranks can
        still change after disqualifications), `ended` once results are final
        and every prize is paid.
      enum:
        - upcoming
        - live
        - in_review
        - ended
    CompetitionRead_error:
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
        `settlement_invalid_state`, `settlement_close_only_required`,
        `unauthorized`, `not_found`. `instrument_close_only` means user orders
        must reduce an existing position; `instrument_settled` is permanent.
        Settlement readiness errors leave the instrument and accounts unchanged.
        For `400` it is a human-readable validation detail whose wording may
        change. See the Error handling guide for the domain identifiers.
        (Post-only / Fill-or-Kill outcomes are order statuses such as
        `post_only_rejected`, not rejections.)
      example: insufficient_margin
    arts:
      type: integer
      description: >-
        Gateway arrival timestamp captured at handler entry, in Unix
        milliseconds.
      example: 1767225600000
    CompetitionRead_timestamp:
      type: integer
      description: >-
        decision time in Unix milliseconds: terminal event time for event-backed
        outcomes, gateway decision time otherwise
      example: 1767225600000
    ref:
      type: string
      description: >-
        Unique server-generated rejection reference. Include this value when
        asking support to locate the corresponding structured rejection trace.
      example: g-0011223344556
  responses:
    CompetitionRead_Error400Response:
      description: |
        Bad request — the request was malformed or failed validation (bad query
        parameters, unparseable body, invalid signature, or a domain pre-check).
        The `error` field is a human-readable validation detail. Rejections also
        carry the server `ts` in Unix milliseconds and a `ref` that support can
        use to locate the matching structured trace.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/CompetitionRead_Error400'
    CompetitionRead_Error429Response:
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
            $ref: '#/components/schemas/CompetitionRead_Error429'
    CompetitionRead_Error500Response:
      description: |
        Internal server error. `error` is `internal_error`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/CompetitionRead_Error500'
    CompetitionRead_Error503Response:
      description: |
        Service unavailable — safe to retry with backoff, honoring
        `Retry-After` when present. `error` is `service_unavailable`.

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
            $ref: '#/components/schemas/CompetitionRead_Error503'

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
