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
source_url: 'https://docs.polymarket.com/cn/api-reference/get-authenticated-builder-receipts'
updated_at: 2026-11-13
---

# 查询构建者收益明细

> Returns this account's builder credits only. The time window is inclusive,
defaults to the last seven days, and is bounded to 90 days. Supply the same
start_timestamp, end_timestamp and as_of_sequence to compare list and summary.
Older receipts remain queryable by selecting a past window. Zero-fee eligible
fills count toward volume. Each receipt identifies only the attributed trader's
main wallet and own order details, including its signed platform fee and total_fee.
client_order_id is omitted when the order did not supply one. Credits are ordinary
collateral, not a claim balance. Recover a disconnected builder fill feed through
this endpoint using overlapping windows and earning_id deduplication. The live
feed can precede indexing. Retry REST until as_of_sequence covers the event.




## OpenAPI

````yaml api-spec/perps-openapi.json GET /v1/account/builder-earnings
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
  /v1/account/builder-earnings:
    get:
      summary: Get authenticated builder receipts
      description: >
        Returns this account's builder credits only. The time window is
        inclusive,

        defaults to the last seven days, and is bounded to 90 days. Supply the
        same

        start_timestamp, end_timestamp and as_of_sequence to compare list and
        summary.

        Older receipts remain queryable by selecting a past window. Zero-fee
        eligible

        fills count toward volume. Each receipt identifies only the attributed
        trader's

        main wallet and own order details, including its signed platform fee and
        total_fee.

        client_order_id is omitted when the order did not supply one. Credits
        are ordinary

        collateral, not a claim balance. Recover a disconnected builder fill
        feed through

        this endpoint using overlapping windows and earning_id deduplication.
        The live

        feed can precede indexing. Retry REST until as_of_sequence covers the
        event.
      operationId: getBuilderEarnings
      parameters:
        - in: query
          name: start_timestamp
          required: false
          schema:
            $ref: '#/components/schemas/timestamp'
        - in: query
          name: end_timestamp
          required: false
          schema:
            $ref: '#/components/schemas/timestamp'
        - in: query
          name: as_of_sequence
          required: false
          schema:
            $ref: '#/components/schemas/sequence'
        - name: cursor
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/cursor'
      responses:
        '200':
          description: Complete-prefix builder accounting response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BuilderEarnings'
        '400':
          $ref: '#/components/responses/Error400Response'
        '401':
          $ref: '#/components/responses/Error401Response'
        '408':
          $ref: '#/components/responses/Error408Response'
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
    timestamp:
      type: integer
      description: Timestamp in milliseconds
      example: 1767225600000
    sequence:
      type: integer
      description: Sequence number
      example: 1234567890
    cursor:
      type: string
      description: >-
        Pagination cursor. Pass the opaque `cursor` returned by the previous
        page to fetch the next page. Paging follows the `sort` direction
        (strictly older fills when `sort=desc`, strictly newer when `sort=asc`).
        The trade ID of the last fill from the previous page is also accepted
        for backwards compatibility, except on instrument-filtered
        `/v1/info/fills`, which requires the returned keyset cursor.
      example: eyJ0cyI6MTc2NzIyNTYwMDAwMDAwMDAwMCwiaWQiOjF9
    BuilderEarnings:
      type: object
      required:
        - data
        - more
        - start_timestamp
        - end_timestamp
        - as_of_sequence
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/BuilderEarning'
        more:
          type: boolean
        cursor:
          type: string
          description: >-
            Opaque continuation preserving account, time window and fully
            indexed cutoff. Reuse unchanged.
        start_timestamp:
          $ref: '#/components/schemas/timestamp'
        end_timestamp:
          $ref: '#/components/schemas/timestamp'
        as_of_sequence:
          type: integer
          description: >-
            Complete indexed event prefix shared with the summary. Never the
            largest row seen.
    BuilderEarning:
      type: object
      required:
        - earning_id
        - trade_id
        - order_id
        - instrument_id
        - trader
        - buy
        - price
        - quantity
        - side
        - timestamp
        - sequence
        - notional
        - fee_asset
        - fee
        - builder_fee
        - total_fee
        - fee_rate
      properties:
        earning_id:
          type: string
          description: >-
            Stable side-specific receipt identity, unique for this builder. Use
            this to deduplicate, not sequence or trade_id alone.
        trade_id:
          $ref: '#/components/schemas/tid'
        order_id:
          $ref: '#/components/schemas/oid'
        instrument_id:
          $ref: '#/components/schemas/iid'
        side:
          type: string
          enum:
            - maker
            - taker
        timestamp:
          $ref: '#/components/schemas/timestamp'
        sequence:
          type: integer
        notional:
          type: string
        fee_asset:
          $ref: '#/components/schemas/fea'
        builder_fee:
          $ref: '#/components/schemas/builder_fee'
        fee_rate:
          $ref: '#/components/schemas/builder_fee_rate'
        trader:
          allOf:
            - $ref: '#/components/schemas/address'
          description: >-
            Main address of the attributed trading account, not its signing
            proxy or the counterparty.
        buy:
          $ref: '#/components/schemas/buy'
        price:
          $ref: '#/components/schemas/price'
        quantity:
          $ref: '#/components/schemas/quantity'
        client_order_id:
          allOf:
            - $ref: '#/components/schemas/coid'
          description: Included only when the attributed order supplied a client_order_id.
        fee:
          $ref: '#/components/schemas/fee'
        total_fee:
          $ref: '#/components/schemas/total_fee'
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
    tid:
      type: integer
      description: Trade ID
      example: 1
    oid:
      type: integer
      description: Order ID
      example: 1234567890
    iid:
      type: integer
      description: Instrument ID
      example: 1
    fea:
      type: string
      description: Fee asset name
      example: USDC
    builder_fee:
      type: string
      description: >-
        Actual additional builder fee in the same asset as fee, floored
        independently for each execution to that asset's token decimals (six for
        pUSD), with discarded dust and no carry. The fee is non-negative and is
        zero for older or untagged fills and excluded forced liquidation legs.
      example: '20.00'
    builder_fee_rate:
      type: string
      description: >-
        Additional builder fee as a decimal fraction of executed notional, from
        0 through 0.001 (10 basis points). Zero approval revokes future
        admission. Never a percentage string.
      example: '0.001'
    address:
      type: string
      description: Address
      example: '0x1234567890abcdef1234567890abcdef12345678'
    buy:
      type: boolean
      description: Is buy
      example: true
    price:
      type: string
      description: Price
      example: '100.00'
    quantity:
      type: string
      description: Quantity in number of contracts
      example: '10.00'
    coid:
      type: string
      description: Client order ID
      minLength: 32
      maxLength: 32
      pattern: ^[0-9a-f]{32}$
      example: 550e8400e29b41d4a716446655440000
    fee:
      type: string
      description: >-
        Signed exchange fee for this trade side, excluding builder_fee. Negative
        values are rebates
      example: '1.25'
    total_fee:
      type: string
      description: >-
        Exact signed sum of exchange fee and builder_fee in the same asset. May
        be negative when exchange rebates exceed the builder charge.
      example: '24.00'
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
