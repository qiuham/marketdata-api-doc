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
source_url: 'https://docs.polymarket.com/api-reference/get-leaderboard'
updated_at: 2026-11-13
---

# Get Leaderboard

> Get the global perpetuals leaderboard, ranked by PnL, notional volume,
current account value, or ROI across all instruments.

Windows are anchored to calendar UTC boundaries: `day` starts at 00:00 UTC
today, `week` at Monday 00:00 UTC, `month` at the first of the month
00:00 UTC, and `all` at exchange launch.

PnL is realized PnL minus trading fees plus funding payments, consistent
with the account PnL endpoint; unrealized PnL is excluded. Notional is the
USD value of all fills in the window. Every entry carries both metrics;
`rank` is the position under the requested `sort_by`.

ROI sorting uses the served, rounded window ROI in descending order, with
ties broken by higher PnL, higher notional, then the older account. It uses
the same eligible accounts as PnL and notional, with no additional minimum
equity or volume requirement. The optional `address` row reports its rank
under the same ordering, including ranks beyond the pageable top 1000.

PnL, notional, and account value are raw numeric strings from the engine.
Account value is current equity (collateral value plus unrealized PnL).
The background census advances by at most 8,192 accounts on each 60-second
poller tick, so a full publication can span multiple ticks as the account
population grows. For account-value sorting, `timestamp` is the earlier of
the published census start and the historical window's computation time,
so stale membership and PnL remain observable if a historical rebuild fails.
When sorting by account value, the requested window still determines which
accounts and historical PnL/notional metrics are included, while the
ranking uses their current equity. Accounts whose equity cannot be computed
are excluded from that ranking. When unrealized PnL is unavailable (for
example, due to stale marks), the display field falls back to collateral
value on PnL/notional entries and address lookups; it does not establish an
equity rank. `total` counts accounts with published equity in that window.
`sort_by=account_value` returns 503 while the first completed census is
warming. PnL and notional rankings remain available during that warm-up.
Clients are responsible for decimal and currency presentation formatting.

Rankings are recomputed periodically; `timestamp` is the computation time.
Returns 25 entries by default and at most 100 per request; only the top
1000 ranks are pageable (`offset + limit` must not exceed 1000).

Provide `address` to additionally return that account's row regardless of
rank. An address with no activity in the window returns zero metrics and
no rank.


Request Weight: **5**

Cached 5s — a request served from cache costs **1**


## OpenAPI

````yaml /api-spec/perps-openapi.json get /v1/info/leaderboard
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
  /v1/info/leaderboard:
    get:
      summary: Get Leaderboard
      description: >
        Get the global perpetuals leaderboard, ranked by PnL, notional volume,

        current account value, or ROI across all instruments.


        Windows are anchored to calendar UTC boundaries: `day` starts at 00:00
        UTC

        today, `week` at Monday 00:00 UTC, `month` at the first of the month

        00:00 UTC, and `all` at exchange launch.


        PnL is realized PnL minus trading fees plus funding payments, consistent

        with the account PnL endpoint; unrealized PnL is excluded. Notional is
        the

        USD value of all fills in the window. Every entry carries both metrics;

        `rank` is the position under the requested `sort_by`.


        ROI sorting uses the served, rounded window ROI in descending order,
        with

        ties broken by higher PnL, higher notional, then the older account. It
        uses

        the same eligible accounts as PnL and notional, with no additional
        minimum

        equity or volume requirement. The optional `address` row reports its
        rank

        under the same ordering, including ranks beyond the pageable top 1000.


        PnL, notional, and account value are raw numeric strings from the
        engine.

        Account value is current equity (collateral value plus unrealized PnL).

        The background census advances by at most 8,192 accounts on each
        60-second

        poller tick, so a full publication can span multiple ticks as the
        account

        population grows. For account-value sorting, `timestamp` is the earlier
        of

        the published census start and the historical window's computation time,

        so stale membership and PnL remain observable if a historical rebuild
        fails.

        When sorting by account value, the requested window still determines
        which

        accounts and historical PnL/notional metrics are included, while the

        ranking uses their current equity. Accounts whose equity cannot be
        computed

        are excluded from that ranking. When unrealized PnL is unavailable (for

        example, due to stale marks), the display field falls back to collateral

        value on PnL/notional entries and address lookups; it does not establish
        an

        equity rank. `total` counts accounts with published equity in that
        window.

        `sort_by=account_value` returns 503 while the first completed census is

        warming. PnL and notional rankings remain available during that warm-up.

        Clients are responsible for decimal and currency presentation
        formatting.


        Rankings are recomputed periodically; `timestamp` is the computation
        time.

        Returns 25 entries by default and at most 100 per request; only the top

        1000 ranks are pageable (`offset + limit` must not exceed 1000).


        Provide `address` to additionally return that account's row regardless
        of

        rank. An address with no activity in the window returns zero metrics and

        no rank.
      operationId: getLeaderboard
      parameters:
        - name: window
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/window'
        - name: sort_by
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/sort_by'
        - name: limit
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/limit'
        - name: offset
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/offset'
        - name: address
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/address'
      responses:
        '200':
          description: Leaderboard response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Leaderboard'
        '400':
          $ref: '#/components/responses/Error400Response'
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
      security: []
components:
  schemas:
    window:
      type: string
      description: >-
        Leaderboard window, anchored to calendar UTC boundaries. `day` starts at
        00:00 UTC today, `week` at Monday 00:00 UTC, `month` at the first of the
        month 00:00 UTC, `all` at exchange launch.
      default: day
      enum:
        - day
        - week
        - month
        - all
    sort_by:
      type: string
      description: Leaderboard ranking metric
      default: pnl
      enum:
        - pnl
        - notional
        - account_value
        - roi
    limit:
      type: integer
      description: Maximum number of entries to return
      example: 100
    offset:
      type: integer
      description: Number of entries to skip
      default: 0
      example: 0
    address:
      type: string
      description: Address
      example: '0x1234567890abcdef1234567890abcdef12345678'
    Leaderboard:
      type: object
      required:
        - window
        - sort_by
        - timestamp
        - total
        - entries
      properties:
        window:
          $ref: '#/components/schemas/window'
        sort_by:
          $ref: '#/components/schemas/sort_by'
        timestamp:
          $ref: '#/components/schemas/update_timestamp'
        total:
          $ref: '#/components/schemas/total'
        entries:
          type: array
          items:
            $ref: '#/components/schemas/LeaderboardEntry'
          maxItems: 100
        account:
          $ref: '#/components/schemas/LeaderboardAccount'
    update_timestamp:
      type: integer
      description: Update timestamp in milliseconds
      example: 1767225600000
    total:
      type: integer
      description: Total number of ranked accounts
      example: 15234
    LeaderboardEntry:
      type: object
      required:
        - rank
        - account
        - pnl
        - notional
        - account_value
        - roi
      properties:
        rank:
          $ref: '#/components/schemas/rank'
        account:
          $ref: '#/components/schemas/account'
        pnl:
          $ref: '#/components/schemas/pnl'
        notional:
          $ref: '#/components/schemas/notional'
        account_value:
          $ref: '#/components/schemas/account_value'
        roi:
          $ref: '#/components/schemas/roi'
    LeaderboardAccount:
      type: object
      description: >-
        Leaderboard row for the requested address. `rank` is absent when the
        account has no activity in the window, or when sorting by account value
        and that account has no computed equity in the published census. A
        collateral-only display fallback does not establish an equity rank.
      required:
        - account
        - pnl
        - notional
        - account_value
        - roi
      properties:
        rank:
          $ref: '#/components/schemas/rank'
        account:
          $ref: '#/components/schemas/account'
        pnl:
          $ref: '#/components/schemas/pnl'
        notional:
          $ref: '#/components/schemas/notional'
        account_value:
          $ref: '#/components/schemas/account_value'
        roi:
          $ref: '#/components/schemas/roi'
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
    rank:
      type: integer
      description: Leaderboard rank under the requested ranking metric, starting at 1
      example: 1
    account:
      type: string
      description: Account address in hex format
      example: '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
    pnl:
      type: string
      description: PnL in USD
      example: '100.00'
    notional:
      type: string
      description: Trading volume in USD notional as an unformatted numeric string
      example: '10164976'
    account_value:
      type: string
      description: Current account equity in USD as an unformatted numeric string
      example: '9238345.12'
    roi:
      type: string
      description: >-
        Return on investment over the window as a fraction, not a percentage
        ("0.4527" is 45.27%): `pnl / max(100, starting_equity +
        max_net_deposits)`. `pnl` is this row's `pnl`. `starting_equity` is the
        account equity sampled last before the window start (0 for `all`, and 0
        for accounts with no earlier sample). `max_net_deposits` is the running
        maximum, over the window, of cumulative credited deposits minus
        withdrawals plus transfers in minus transfers out, starting from 0 at
        the window start; it is never negative. The 100 USD floor keeps tiny
        accounts from producing extreme ratios. Rounded half-even to 6 decimal
        places with trailing zeros removed; "0" when `pnl` is 0.
      example: '0.4527'
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

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
