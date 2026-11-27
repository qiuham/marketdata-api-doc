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
source_url: 'https://docs.polymarket.com/api-reference/wallet/snapshot-a-wallets-positions-at-the-end-of-a-day'
updated_at: 2026-11-27
---

# Snapshot a wallet's positions at the end of a day

> Every position of one wallet at the end of a closed UTC day, for tax and
accounting exports: each token it holds above 0.1 share at the cut, open,
won and unredeemed, or resolved to 0 and still held (priced 0). Size, cost
basis, the price at the cut and the value, with the day's totals on the
first page. The cut is the next day at 00:00:00Z: every block with an
earlier timestamp counts. A served day never changes, so a `200` is
cacheable for a day.

The price at the cut, first match wins: `settlement` when the market
resolved before the cut (its payout; a combo pays 0 once a leg pays 0, the
product of its legs' payouts once every leg resolved, and its No side 1
minus that), `mark` when a market price was recorded on or before the
day (the latest one, clamped to [0, 1]), else `basis` (the average price,
so `value` equals `cost_basis`). Positions of 0.1 share or less are dust
and not served. Every contract family is included, combos too; `title`,
`slug` and `event_slug` are the market's current Gamma metadata and are
null for combos. `size` is the wallet's on-chain balance at the cut;
`cost_basis` is the native cost basis as `/v2/positions` serves it (size
times the average price, or a structural market's entry cost), as
`/v2/positions/combos` serves it for a combo, frozen at resolution for a
position resolved to 0, and 0 for a balance with no native basis.

`date` must lie in the servable range: the days closed since the snapshot
history began, through yesterday once the writer has passed midnight
(about an hour after it). Any other day is a `400` whose message names the
range. Pages are in a stable order (not `asset` order); follow `next_cursor` with the same
`user` (`date` may be omitted; restated, it must agree).

A new walk (a first page: `date` and no `cursor`) is limited to one per
client every 30 seconds; a second one inside that window is a `429` whose
`Retry-After` is the rest of the window. Cursor pages are not counted,
nor is a walk that fails. A cold first page of a very large wallet can
take several seconds.

Responses are served gzip-compressed: a request must send
`Accept-Encoding: gzip`, as browsers and most HTTP clients do by default
(with curl, pass `--compressed`). A request that does not is a `406`.



## OpenAPI

````yaml https://data-api.polymarket.com/v2/openapi.json get /v2/positions/snapshot
openapi: 3.1.0
info:
  title: Polymarket Data API v2
  description: >-
    The Polymarket Data API: wallet portfolios, trade and activity feeds, market
    state and ranked boards.


    ## Conventions every endpoint shares


    - **Envelope**: every response wraps its payload in `data` (paged routes add
    `pagination`). A documented miss is `data: null` or an empty list, never an
    error.

    - **Pagination is cursor-only**: follow `pagination.next_cursor` until
    `null`; `has_more` is exact, and there is no `offset` query parameter
    (sending one is a `400`). Cursors are signed, typed per endpoint, and
    opaque. The feeds (`trades`, `activity`, combo activity) are keyset walks,
    stable across concurrent writes; the boards, `holders` and most
    combo-position sorts are offset walks behind the opaque token, so a page
    taken across a data refresh can skip or repeat rows. Where a cursor binds
    its cohort (the boards, positions, combo positions), resuming bare is fine,
    restating the same values is fine, and contradicting them is a `400`. The
    `trades`/`activity` feed cursors carry only the seek anchor and page size
    (plus the sort direction on activity): re-send identical filters on every
    page, because changing one mid-walk re-anchors silently.

    - **Rate limiting**: `429` with `Retry-After` is the busy signal for heavy
    queries. A heavy query may first be queued briefly for a capacity slot; the
    `429` arrives only if that short wait ends unserved. Each caller also has a
    per-client request allowance, and bursts past it get the same `429` with
    `Retry-After` sized to the remaining wait. Retry after the given delay. A
    request that could not get a database connection within its budget is NOT a
    `429`: it is a `503` `request_timeout` with `Retry-After`, because the
    shortage is on the server side, not in the caller's rate.

    - **Identifiers**: `condition` (aliases `condition_id`, `conditionId`) is
    the unified query key for on-chain 0x condition ids; `market_id` fields
    carry Gamma's own market ids; `event_id` takes Gamma event ids; `token_id`
    is the CLOB asset id (the key on `/v2/prices-history`).

    - **Params** accept both snake_case and camelCase spellings.

    - **Units**: bare `volume`/`size` values are **shares**; `_usdc` suffixed
    fields are USD; `taker_` prefixed volumes are one-side.

    - **Sentinels**: `outcome_index: 999` means the outcome could not be
    labeled; a missing or `null` numeric field means unavailable, never zero.

    - **Windows on `/v2/trades?user=` and `/v2/activity`**: an omitted or `0`
    `start` floors to three years back (`start=1` asks for full history); an
    omitted or `0` `end` is now plus one day. The other `/v2/trades` shapes
    ignore `start`/`end`: `condition`/`event_id` serve a fixed three-year window
    and the bare feed serves the rolling current-plus-previous month. Other
    windowed routes treat omitted/`0` bounds as unbounded; each documents its
    own rule. `/v2/prices-history` is the strict one, where a `0` bound is a
    `400`.

    - **Errors**: every unsuccessful response is JSON with a human-readable
    `error`, stable `code`, `retryable` flag, and opaque `trace_id`; validation
    failures may also name `parameter`. Codes map to statuses as follows:
    `invalid_request` = `400`, `not_found` = `404`, `method_not_allowed` =
    `405`, `rate_limited` = `429`, `internal` = `500`, and both
    `request_timeout` (the request deadline, the datastore's statement timeout,
    or the connection pool's acquire budget) and `dependency_unavailable` =
    `503`. A `429` or `503` that is worth retrying carries `Retry-After` in
    seconds. Every response, successful or not, echoes the same id in the
    `x-trace-id` header; supply it when reporting a failure so operators can
    correlate it with telemetry.

    - **Auth**: none. All data routes are public; no API key or token is
    required.
  contact:
    name: Polymarket
  license:
    name: MIT
    identifier: MIT
  version: 0.1.0
servers:
  - url: https://data-api.polymarket.com
    description: Production
  - url: https://data-api-rs.stage.pmd.use1.polymarket.sh
    description: Staging
security: []
tags:
  - name: wallet
    description: >-
      Everything anchored on one wallet: positions (base and combos), portfolio
      value, PnL history, the profile card, trading volume, and token approvals.
      Pass the proxy wallet as `user`. One exception cuts across sections:
      `/v2/positions` with `condition` alone (no `user`) answers the market-wide
      holders question.
  - name: feeds
    description: >-
      The high-traffic keyset feeds: trades, activity and combo activity. Filter
      by `user`, `condition` or `event_id`; page with `next_cursor`.
  - name: markets
    description: >-
      Market and event state, keyed by on-chain `condition` ids, Gamma
      `event_id`s or a CLOB `token_id`: open interest, holders, per-event taker
      volume, resolution lifecycle, and price history.
  - name: boards
    description: >-
      Ranked, windowed boards: the PnL/volume leaderboard, biggest single wins,
      and the builder standings and volume buckets. Cursors pin the board they
      were minted on.
  - name: service
    description: >-
      Service metadata: data freshness: the serving watermark, its lag, and
      per-stream ingestion cursors.
paths:
  /v2/positions/snapshot:
    get:
      tags:
        - wallet
      summary: Snapshot a wallet's positions at the end of a day
      description: >-
        Every position of one wallet at the end of a closed UTC day, for tax and

        accounting exports: each token it holds above 0.1 share at the cut,
        open,

        won and unredeemed, or resolved to 0 and still held (priced 0). Size,
        cost

        basis, the price at the cut and the value, with the day's totals on the

        first page. The cut is the next day at 00:00:00Z: every block with an

        earlier timestamp counts. A served day never changes, so a `200` is

        cacheable for a day.


        The price at the cut, first match wins: `settlement` when the market

        resolved before the cut (its payout; a combo pays 0 once a leg pays 0,
        the

        product of its legs' payouts once every leg resolved, and its No side 1

        minus that), `mark` when a market price was recorded on or before the

        day (the latest one, clamped to [0, 1]), else `basis` (the average
        price,

        so `value` equals `cost_basis`). Positions of 0.1 share or less are dust

        and not served. Every contract family is included, combos too; `title`,

        `slug` and `event_slug` are the market's current Gamma metadata and are

        null for combos. `size` is the wallet's on-chain balance at the cut;

        `cost_basis` is the native cost basis as `/v2/positions` serves it (size

        times the average price, or a structural market's entry cost), as

        `/v2/positions/combos` serves it for a combo, frozen at resolution for a

        position resolved to 0, and 0 for a balance with no native basis.


        `date` must lie in the servable range: the days closed since the
        snapshot

        history began, through yesterday once the writer has passed midnight

        (about an hour after it). Any other day is a `400` whose message names
        the

        range. Pages are in a stable order (not `asset` order); follow
        `next_cursor` with the same

        `user` (`date` may be omitted; restated, it must agree).


        A new walk (a first page: `date` and no `cursor`) is limited to one per

        client every 30 seconds; a second one inside that window is a `429`
        whose

        `Retry-After` is the rest of the window. Cursor pages are not counted,

        nor is a walk that fails. A cold first page of a very large wallet can

        take several seconds.


        Responses are served gzip-compressed: a request must send

        `Accept-Encoding: gzip`, as browsers and most HTTP clients do by default

        (with curl, pass `--compressed`). A request that does not is a `406`.
      operationId: get_positions_snapshot
      parameters:
        - name: user
          in: query
          description: |-
            Proxy wallet, `0x` followed by 40 hex digits. The `user_address`
            spelling is accepted as an alias.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: date
          in: query
          description: >-
            The UTC day, `YYYY-MM-DD`: the positions held at its end, the cut

            being the next day at 00:00:00Z. It must be a closed, servable day;
            a

            day outside the servable range is a `400` that names the range.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: limit
          in: query
          description: >-
            Page size, 0 to 1000 (default 100). Ignored when `cursor` is
            supplied

            (the cursor's size wins).
          required: false
          schema:
            type:
              - integer
              - 'null'
            format: int32
            maximum: 1000
            minimum: 0
        - name: cursor
          in: query
          description: Opaque pagination cursor from a prior response's `next_cursor`.
          required: false
          schema:
            type:
              - string
              - 'null'
      responses:
        '200':
          description: >-
            A page of the wallet's positions at the end of the day; `summary` on
            the first page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PositionsSnapshotPage'
        '400':
          description: >-
            A missing or malformed 'user' or 'date', a day outside the servable
            range (the message names it), an invalid 'limit' or 'cursor', or a
            'user' that is a known protocol contract address
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '406':
          description: 'The request does not accept gzip; send `Accept-Encoding: gzip`'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '429':
          description: >-
            A new walk within 30 seconds of the client's last one, or the
            service is at heavy-query capacity; retry after `Retry-After`
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '503':
          description: >-
            Timed out (the request deadline, the datastore statement timeout, or
            the connection pool's acquire budget) or a serving dependency is
            unavailable; retry after `Retry-After`
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    PositionsSnapshotPage:
      type: object
      description: |-
        `{ data, summary, pagination }`: `summary` is present on the first page
        only.
      required:
        - data
        - pagination
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/SnapshotPosition'
          description: >-
            The page's positions, in the walk's stable order (not `asset`
            order).
        pagination:
          $ref: '#/components/schemas/Pagination'
          description: >-
            Page size, display offset, `has_more` and the `next_cursor` to
            follow.
        summary:
          oneOf:
            - type: 'null'
            - $ref: '#/components/schemas/SnapshotSummary'
              description: The day's totals; present on the first page only.
    ErrorResponse:
      type: object
      description: Error body returned by Data API endpoints for unsuccessful requests.
      required:
        - error
        - code
        - retryable
        - trace_id
      properties:
        code:
          $ref: '#/components/schemas/ErrorCode'
          description: Stable classification suitable for programmatic branching.
        error:
          type: string
          description: Human-readable error message.
        parameter:
          type:
            - string
            - 'null'
          description: Query or body parameter associated with a validation failure.
        retryable:
          type: boolean
          description: Whether an automated consumer may retry the request unchanged.
        trace_id:
          type: string
          description: Opaque identifier shared with structured logs and error telemetry.
    SnapshotPosition:
      type: object
      description: One position held at the end of the day, valued at the cut.
      required:
        - asset
        - module
        - size
        - avg_price
        - cost_basis
        - price
        - price_source
        - value
      properties:
        asset:
          type: string
          description: The ERC-1155 token id, decimal.
        avg_price:
          type: number
          format: double
          description: >-
            `cost_basis / size`, entry fees included (`/v2/positions` reports
            its

            `avg_price` without fees).
        condition_id:
          type:
            - string
            - 'null'
          description: |-
            The market's condition id (66 characters), or the combo condition id
            of a combo position; null when the token is unknown.
        cost_basis:
          type: number
          format: double
          description: |-
            The remaining cost basis of the shares in USDC, entry fees included
            (the `total_cost_usdc` of the same position on `/v2/positions`).
        event_slug:
          type:
            - string
            - 'null'
          description: The slug of the market's Gamma event; null for combos.
        module:
          type: integer
          format: int32
          description: |-
            The contract family: 0 ConditionalTokens, 1 and 2 polymarket-v2
            binary and neg-risk, 3 combo, 4 directional.
        outcome:
          type:
            - string
            - 'null'
          description: The outcome label; `Yes` or `No` for a combo.
        price:
          type: number
          format: double
          description: |-
            The price at the cut: the payout for `settlement`, the mark (0 to 1)
            for `mark`, and `avg_price` for `basis`, which can exceed 1.
        price_source:
          type: string
          description: >-
            Where `price` came from: `settlement` (the market resolved before
            the

            cut: its payout), `mark` (the last market price recorded at a

            midnight on or before the day), or `basis` (no price: the average
            price, so `value`

            equals `cost_basis`).
        size:
          type: number
          format: double
          description: Shares held at the end of the day.
        slug:
          type:
            - string
            - 'null'
          description: The current Gamma market slug; null for combos.
        title:
          type:
            - string
            - 'null'
          description: The current Gamma market question; null for combos.
        value:
          type: number
          format: double
          description: '`size * price`.'
    Pagination:
      type: object
      required:
        - limit
        - offset
        - has_more
      properties:
        has_more:
          type: boolean
          description: |-
            Exact: `true` iff another page exists; probe-based, never inferred
            from page fullness.
        limit:
          type: integer
          format: int32
          description: Page size this page was served with.
          minimum: 0
        next_cursor:
          type:
            - string
            - 'null'
          description: Opaque, signed cursor for the next page; `null` on the last page.
        offset:
          type: integer
          format: int32
          description: |-
            Running item offset for display continuity across keyset pages (the
            cursor drives the actual seek; this is cosmetic; there is no total).
          minimum: 0
    SnapshotSummary:
      type: object
      description: The totals of every position of the day; on the first page only.
      required:
        - date
        - cut
        - closed_block
        - positions
        - cost_basis
        - value
        - value_by_source
      properties:
        closed_block:
          type: integer
          format: int64
          description: The highest block of the day's recorded moves.
        cost_basis:
          type: number
          format: double
          description: The remaining cost basis of every position, in USDC.
        cut:
          type: string
          description: The cut, `date + 1 day` at 00:00:00Z (RFC 3339).
        date:
          type: string
          description: The requested day, `YYYY-MM-DD`.
        positions:
          type: integer
          format: int64
          description: Positions held at the end of the day (every page together).
        value:
          type: number
          format: double
          description: The value of every position at the cut, in USDC.
        value_by_source:
          $ref: '#/components/schemas/SnapshotValueBySource'
          description: '`value` split by `price_source`.'
    ErrorCode:
      type: string
      description: Stable machine-readable classification for Data API failures.
      enum:
        - invalid_request
        - unauthorized
        - not_found
        - method_not_allowed
        - request_timeout
        - rate_limited
        - dependency_unavailable
        - internal
    SnapshotValueBySource:
      type: object
      description: '`value` split by `price_source`.'
      required:
        - settlement
        - mark
        - basis
      properties:
        basis:
          type: number
          format: double
          description: Value of the positions with no price (their cost basis).
        mark:
          type: number
          format: double
          description: Value of the positions priced at a recorded midnight market price.
        settlement:
          type: number
          format: double
          description: Value of the positions whose market resolved before the cut.

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
