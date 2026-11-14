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
source_url: 'https://docs.polymarket.com/api-reference/get-trading-competition-account'
updated_at: 2026-11-13
---

# Get Trading Competition Account

> One account's standing: rank and score once qualified, otherwise its
volume so far and how much more it needs to rank; projected or won prize;
places and score from the prize zone; every position it held when the
competition started, by market, and whether it has since been closed.
An address with no activity returns zero figures and no rank.


Request Weight: **1**


## OpenAPI

````yaml /api-spec/perps-openapi.json get /v1/info/competition/account
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
  /v1/info/competition/account:
    get:
      summary: Get Trading Competition Account
      description: >
        One account's standing: rank and score once qualified, otherwise its

        volume so far and how much more it needs to rank; projected or won
        prize;

        places and score from the prize zone; every position it held when the

        competition started, by market, and whether it has since been closed.

        An address with no activity returns zero figures and no rank.
      operationId: getCompetitionAccount
      parameters:
        - name: competition_id
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/competition_id'
        - name: address
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/address'
      responses:
        '200':
          description: Account standing.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompetitionAccount'
        '400':
          $ref: '#/components/responses/CompetitionRead_Error400Response'
        '404':
          $ref: '#/components/responses/CompetitionRead_Error404Response'
        '429':
          $ref: '#/components/responses/CompetitionRead_Error429Response'
        '500':
          $ref: '#/components/responses/CompetitionRead_Error500Response'
        '503':
          $ref: '#/components/responses/CompetitionRead_Error503Response'
      security: []
components:
  schemas:
    competition_id:
      type: integer
      minimum: 1
      description: Trading competition ID
      example: 3
    address:
      type: string
      description: Address
      example: '0x1234567890abcdef1234567890abcdef12345678'
    CompetitionAccount:
      type: object
      required:
        - competition_id
        - status
        - account
        - qualified
        - score
        - pnl
        - realized_pnl
        - unrealized_pnl
        - fees
        - funding
        - volume
        - boosted_volume
        - min_volume
        - volume_to_qualify
        - qualification_progress
        - row_state
        - locked_positions
      properties:
        competition_id:
          $ref: '#/components/schemas/competition_id'
        status:
          $ref: '#/components/schemas/competition_status'
        updated_at:
          $ref: '#/components/schemas/update_timestamp'
        account:
          $ref: '#/components/schemas/account'
        rank:
          $ref: '#/components/schemas/rank'
        qualified:
          type: boolean
          description: Reached the minimum volume and is ranked
        score:
          $ref: '#/components/schemas/competition_score'
        pnl:
          type: string
        realized_pnl:
          type: string
        unrealized_pnl:
          type: string
        fees:
          type: string
          description: Fees paid net of rebates
        funding:
          type: string
          description: Funding received net of funding paid
        volume:
          type: string
        boosted_volume:
          type: string
        first_fill_at:
          $ref: '#/components/schemas/competition_first_fill_at'
        min_volume:
          type: string
        volume_to_qualify:
          type: string
          description: Unboosted volume still needed to rank; "0" once qualified
        qualification_progress:
          type: string
          description: Fraction of the minimum reached, from "0" to "1"
        prize:
          type: string
        spots_from_prize_zone:
          type: integer
          description: >-
            Places between this rank and the last paid place; 0 inside the prize
            zone; absent when unranked
        score_to_prize_zone:
          type: string
          description: >-
            Score still needed to reach the prize zone; "0" inside it; absent
            when unranked
        row_state:
          $ref: '#/components/schemas/competition_row_state'
        payout_tx_hash:
          type: string
        paid_at:
          type: integer
        locked_positions:
          type: array
          description: >-
            Positions open at the start, by market, including ones since
            released.
          items:
            $ref: '#/components/schemas/CompetitionLockedPosition'
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
    update_timestamp:
      type: integer
      description: Update timestamp in milliseconds
      example: 1767225600000
    account:
      type: string
      description: Account address in hex format
      example: '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
    rank:
      type: integer
      description: Leaderboard rank under the requested ranking metric, starting at 1
      example: 1
    competition_score:
      type: string
      description: >-
        Competition score, PnL × √(boosted volume), as a numeric string rounded
        to 6 decimal places. Can be negative.
      example: '1264911.064067'
    competition_first_fill_at:
      type: integer
      x-js-safe-integer: true
      description: >-
        Time of the account's first counted fill in this competition, in Unix
        milliseconds; absent when unavailable or the account has no counted
        fills. Ranked ties use the configured tie-breaks, normally boosted
        volume then first fill order. Fill order can distinguish fills within
        the same millisecond.
      example: 1793001234567
    competition_row_state:
      type: string
      description: >-
        How a leaderboard row is shown. `live` while running (prize is
        projected), `provisional` while in review, `disqualified` for a rule
        violation, `final` once results are finalized, `paid` once the prize is
        paid.
      enum:
        - live
        - provisional
        - disqualified
        - final
        - paid
    CompetitionLockedPosition:
      type: object
      description: >-
        A position open when the competition started. Its market does not count
        until it is fully closed.
      required:
        - instrument_id
        - size_at_start
      properties:
        instrument_id:
          $ref: '#/components/schemas/instrument_id'
        size_at_start:
          type: string
          description: Signed position size at the start (positive long, negative short)
        released_at:
          type: integer
          description: >-
            When it was fully closed and the market started counting, in Unix
            milliseconds; absent while still locked
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
    CompetitionRead_Error404:
      title: Error404
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
    instrument_id:
      type: integer
      description: Instrument ID
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
    CompetitionRead_Error404Response:
      description: |
        Not found — the endpoint is disabled on this venue (e.g. auto-cancel) or
        the route does not exist. `error` is `not_found`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/CompetitionRead_Error404'
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
