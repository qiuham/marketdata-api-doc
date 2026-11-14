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
source_url: 'https://docs.polymarket.com/api-reference/update-leverage'
updated_at: 2026-11-13
---

# Update Leverage

> Update leverage for an instrument.

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

Requires proxy signature, see [proxy signing](/http/signing#2-proxy-signing).


Request Weight: **1**Action Weight: **1**


## OpenAPI

````yaml /api-spec/perps-openapi.json patch /v1/trade/leverage
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
  /v1/trade/leverage:
    patch:
      summary: Update Leverage
      description: >
        Update leverage for an instrument.


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


        Requires proxy signature, see [proxy
        signing](/http/signing#2-proxy-signing).
      operationId: updateLeverage
      requestBody:
        description: Leverage request.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LeverageRequest'
            examples:
              updateLeverage:
                summary: Update leverage for one instrument
                value:
                  op:
                    type: updateLeverage
                    args:
                      iid: 1
                      lev: 5
                      cross: false
                  sig: >-
                    0x59ed57f6dce8d15aa01e774ef53d9957c84801fb34ec655f6a2ea344af8a58843095314730a3f1bd8f0f4560f6dc6f8de69d3f2d0a6f3365fc877f7f4845d40b1c
                  salt: 333333333
                  ts: 1767000012000
      responses:
        '200':
          description: The instrument's effective leverage configuration after the update.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LeverageResponse'
        '400':
          $ref: '#/components/responses/Error400Response'
        '422':
          $ref: '#/components/responses/Error422Response'
        '429':
          $ref: '#/components/responses/Error429Response'
        '500':
          $ref: '#/components/responses/Error500Response'
      security: []
components:
  schemas:
    LeverageRequest:
      allOf:
        - type: object
          required:
            - op
          properties:
            op:
              $ref: '#/components/schemas/OpUpdateLeverage'
        - $ref: '#/components/schemas/BaseOp'
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
    OpUpdateLeverage:
      type: object
      required:
        - type
        - args
      properties:
        type:
          type: string
          enum:
            - updateLeverage
        args:
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
    Error422Response:
      description: |
        Unprocessable Entity — the request was well-formed but a domain rule
        rejected it on its merits (insufficient balance, invalid leverage,
        proxy already exists, …). The body is the discriminated rejection
        (`status: err`) with the engine error identifier in `error`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/GenericRejected'
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

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
