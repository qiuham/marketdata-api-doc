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
source_url: 'https://docs.polymarket.com/api-reference/get-registration'
updated_at: 2026-11-13
---

# Get Registration

> Check whether an address has a Perps account. Registration is permanent,
so a `true` answer never changes; a `false` answer flips as soon as the
address registers.


Request Weight: **1**

Cached — `true` up to 1 day at the edge, `false` up to 10s


## OpenAPI

````yaml /api-spec/perps-openapi.json get /v1/info/registered
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
  /v1/info/registered:
    get:
      summary: Get Registration
      description: |
        Check whether an address has a Perps account. Registration is permanent,
        so a `true` answer never changes; a `false` answer flips as soon as the
        address registers.
      operationId: getRegistered
      parameters:
        - name: address
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/address'
      responses:
        '200':
          description: Registration status for the address.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RegisteredResponse'
        '400':
          $ref: '#/components/responses/Error400Response'
        '429':
          $ref: '#/components/responses/Error429Response'
        '500':
          $ref: '#/components/responses/Error500Response'
      security: []
components:
  schemas:
    address:
      type: string
      description: Address
      example: '0x1234567890abcdef1234567890abcdef12345678'
    RegisteredResponse:
      type: object
      required:
        - registered
      properties:
        registered:
          type: boolean
          description: Whether the address has a Perps account.
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
