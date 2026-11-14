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
source_url: 'https://docs.polymarket.com/cn/api-reference/update-leverage-for-multiple-instruments'
updated_at: 2026-11-13
---

# 批量更新杠杆

> Update leverage for up to 100 unique instruments. Updates are processed
sequentially and are not atomic. If only some responses arrive before the
gateway deadline, missing item results use `internal_error`; whether those
updates applied is unknown. If no responses arrive, the request returns
503 — retryable, since each update is an idempotent leverage/margin-type
set that converges to the same value whether or not the original attempt
was admitted.

Each setting resolves independently: explicit per-instrument setting, then
exchange-managed account-group default, then instrument maximum leverage and
isolated margin. Group leverage is capped at the instrument maximum; a group
cross default resolves to isolated on isolated-only instruments. Group defaults
apply to new listings and never overwrite explicit settings.
This operation sets both settings explicitly; GET /v1/account/config reports
resolved values. Submit the current resolved pair to preserve it against later
group changes. Leverage bounds and BLP locks also apply to unchanged values.
Set your preferred leverage and margin mode after listing and before placing
your first order. An unknown instrument ID (never listed) is rejected with
`instrument_not_found`; a disabled instrument is not rejected merely because
it is disabled.

Margin mode can change only when the account has no position and no open
orders in that instrument, including orders awaiting risk approval or execution.
Close the position and cancel all orders before switching between isolated
and cross margin. A position blocks a mode change with `position_exists`;
open orders block it with `open_orders_exist`. Leverage changes within the
same mode remain subject to leverage limits and margin checks. Leverage must
be positive (`lev: 0` returns 400); exceeding the instrument maximum returns
`invalid_leverage`. BLP-subscribed instruments reject leverage or mode updates
with `blp_leverage_locked`; unsubscribe before changing the configuration.

Requires proxy signature, see [Update Leverage](/perps/trading#update-leverage).




## OpenAPI

````yaml api-spec/perps-openapi.json PATCH /v1/trade/leverage/batch
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
  /v1/trade/leverage/batch:
    patch:
      summary: Update Leverage for Multiple Instruments
      description: >
        Update leverage for up to 100 unique instruments. Updates are processed

        sequentially and are not atomic. If only some responses arrive before
        the

        gateway deadline, missing item results use `internal_error`; whether
        those

        updates applied is unknown. If no responses arrive, the request returns

        503 — retryable, since each update is an idempotent leverage/margin-type

        set that converges to the same value whether or not the original attempt

        was admitted.


        Each setting resolves independently: explicit per-instrument setting,
        then

        exchange-managed account-group default, then instrument maximum leverage
        and

        isolated margin. Group leverage is capped at the instrument maximum; a
        group

        cross default resolves to isolated on isolated-only instruments. Group
        defaults

        apply to new listings and never overwrite explicit settings.

        This operation sets both settings explicitly; GET /v1/account/config
        reports

        resolved values. Submit the current resolved pair to preserve it against
        later

        group changes. Leverage bounds and BLP locks also apply to unchanged
        values.

        Set your preferred leverage and margin mode after listing and before
        placing

        your first order. An unknown instrument ID (never listed) is rejected
        with

        `instrument_not_found`; a disabled instrument is not rejected merely
        because

        it is disabled.


        Margin mode can change only when the account has no position and no open

        orders in that instrument, including orders awaiting risk approval or
        execution.

        Close the position and cancel all orders before switching between
        isolated

        and cross margin. A position blocks a mode change with
        `position_exists`;

        open orders block it with `open_orders_exist`. Leverage changes within
        the

        same mode remain subject to leverage limits and margin checks. Leverage
        must

        be positive (`lev: 0` returns 400); exceeding the instrument maximum
        returns

        `invalid_leverage`. BLP-subscribed instruments reject leverage or mode
        updates

        with `blp_leverage_locked`; unsubscribe before changing the
        configuration.


        Requires proxy signature, see [Update
        Leverage](/perps/trading#update-leverage).
      operationId: updateLeverages
      requestBody:
        description: Batch leverage request.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LeverageBatchRequest'
            examples:
              updateLeverages:
                summary: Update leverage for multiple instruments
                value:
                  op:
                    type: updateLeverages
                    args:
                      - iid: 1
                        lev: 5
                        cross: false
                      - iid: 2
                        lev: 10
                        cross: true
                  sig: >-
                    0x59ed57f6dce8d15aa01e774ef53d9957c84801fb34ec655f6a2ea344af8a58843095314730a3f1bd8f0f4560f6dc6f8de69d3f2d0a6f3365fc877f7f4845d40b1c
                  salt: 333333333
                  ts: 1767000012000
      responses:
        '200':
          description: Ordered result for each requested instrument.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/LeverageBatchResponse'
              examples:
                mixedResult:
                  summary: One update succeeds and one is rejected
                  value:
                    - status: ok
                      instrument_id: 1
                      leverage: 5
                      cross: false
                    - status: err
                      instrument_id: 2
                      error: insufficient_margin
        '400':
          $ref: '#/components/responses/BatchError400Response'
        '429':
          $ref: '#/components/responses/BatchError429Response'
        '500':
          $ref: '#/components/responses/BatchError500Response'
        '503':
          $ref: '#/components/responses/BatchError503Response'
      security: []
components:
  schemas:
    LeverageBatchRequest:
      allOf:
        - type: object
          required:
            - op
          properties:
            op:
              $ref: '#/components/schemas/OpUpdateLeverages'
        - $ref: '#/components/schemas/BaseOp'
    LeverageBatchResponse:
      oneOf:
        - $ref: '#/components/schemas/LeverageResponse'
        - $ref: '#/components/schemas/LeverageRejected'
    OpUpdateLeverages:
      type: object
      required:
        - type
        - args
      properties:
        type:
          type: string
          enum:
            - updateLeverages
        args:
          type: array
          minItems: 1
          maxItems: 100
          items:
            $ref: '#/components/schemas/OpUpdateLeveragesArgsItem'
    BaseOp:
      type: object
      required:
        - sig
        - salt
        - ts
      properties:
        sig:
          $ref: '#/components/schemas/sig'
        salt:
          $ref: '#/components/schemas/salt'
        ts:
          $ref: '#/components/schemas/ts'
    LeverageResponse:
      description: The instrument's effective leverage configuration after the update.
      type: object
      required:
        - status
        - instrument_id
        - leverage
        - cross
      properties:
        status:
          type: string
          enum:
            - ok
        instrument_id:
          $ref: '#/components/schemas/iid'
        leverage:
          $ref: '#/components/schemas/lev'
        cross:
          $ref: '#/components/schemas/cross'
    LeverageRejected:
      type: object
      required:
        - status
        - instrument_id
        - error
      properties:
        status:
          type: string
          enum:
            - err
        instrument_id:
          $ref: '#/components/schemas/iid'
        error:
          $ref: '#/components/schemas/error'
    GenericRejected:
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
    OpUpdateLeveragesArgsItem:
      type: object
      required:
        - iid
        - lev
        - cross
      properties:
        iid:
          $ref: '#/components/schemas/iid'
        lev:
          $ref: '#/components/schemas/lev'
        cross:
          $ref: '#/components/schemas/cross'
    sig:
      type: string
      description: Signature in hex format
      example: 0x1234567890...
    salt:
      type: integer
      description: Salt
      example: 1234567890
    ts:
      type: integer
      description: >-
        Request timestamp. Unix milliseconds for most operations; Unix seconds
        for withdrawals (must match the on-chain EIP-712 struct verified against
        block.timestamp).
      example: 1767225600000
    iid:
      type: integer
      description: Instrument ID
      example: 1
    lev:
      type: integer
      description: Leverage
      example: 10
    cross:
      type: boolean
      description: Whether to use cross margin mode
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
    BatchError400Response:
      description: >
        Bad request — the batch request was malformed or failed validation

        (unparseable body, invalid signature, or a domain pre-check).
        Request-level

        failures are returned as a single rejected item so batch endpoints

        always return an array. The `error` field is a human-readable validation

        detail.
      content:
        application/json:
          schema:
            type: array
            minItems: 1
            maxItems: 1
            items:
              $ref: '#/components/schemas/GenericRejected'
    BatchError429Response:
      description: |
        Too Many Requests. Request-level failures are returned as a single
        rejected item so batch endpoints always return an array. `error`
        distinguishes the limit that was hit: `ip_rate_limited` (per-IP token
        bucket), `action_rate_limited` (per-account action rate), or
        `open_orders_limit` (resting open-order cap).
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
            type: array
            minItems: 1
            maxItems: 1
            items:
              $ref: '#/components/schemas/GenericRejected'
    BatchError500Response:
      description: |
        Internal server error. Request-level failures are returned as a single
        rejected item so batch endpoints always return an array. `error` is
        `internal_error`.
      content:
        application/json:
          schema:
            type: array
            minItems: 1
            maxItems: 1
            items:
              $ref: '#/components/schemas/GenericRejected'
    BatchError503Response:
      description: |
        Service unavailable — safe to retry with backoff, honoring
        `Retry-After` when present. Request-level failures are returned as a
        single rejected item so batch endpoints always return an array.
        `error` is `service_unavailable`.

        Most causes are the replica shedding the request at its pod-level
        in-flight cap before dispatch — the request definitely did not
        execute, and the shed is transient by design.

        On a subset of routes, this status is also returned when the engine
        round-trip itself times out with zero responses observed. That is
        retryable engine backpressure, but it does not prove non-execution:
        the command may already have been admitted, with its response simply
        not reaching the gateway before the deadline. This status is only
        used for that case on routes that are safe to retry regardless
        (idempotent state-setting); routes where a bare retry cannot safely
        resolve the ambiguity keep the outcome a non-retryable 500 instead.
      headers:
        Retry-After:
          description: |
            Whole seconds to wait before retrying. The shed is a transient
            overload signal, so the hint is short and constant.
          schema:
            type: integer
            example: 1
      content:
        application/json:
          schema:
            type: array
            minItems: 1
            maxItems: 1
            items:
              $ref: '#/components/schemas/GenericRejected'

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
