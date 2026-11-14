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
source_url: 'https://docs.polymarket.com/api-reference/get-instruments'
updated_at: 2026-11-13
---

# Get Instruments

> Get enabled instruments. When instrument_id is supplied, a permanently settled instrument is also returned, including its final settlement record. Other disabled instruments remain excluded. The presence of settlement means the instrument is delisted and cannot trade.

Request Weight: **2**


## OpenAPI

````yaml /api-spec/perps-openapi.json get /v1/info/instruments
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
  /v1/info/instruments:
    get:
      summary: Get Instruments
      description: >-
        Get enabled instruments. When instrument_id is supplied, a permanently
        settled instrument is also returned, including its final settlement
        record. Other disabled instruments remain excluded. The presence of
        settlement means the instrument is delisted and cannot trade.
      operationId: getInstruments
      parameters:
        - name: instrument_id
          in: query
          required: false
          schema:
            type: integer
            format: int64
            minimum: 0
            maximum: 4294967295
            description: Instrument ID
        - name: instrument_type
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/instrument_type'
        - name: category
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/category'
      responses:
        '200':
          description: Instruments response.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Instrument'
        '400':
          $ref: '#/components/responses/Error400Response'
        '429':
          $ref: '#/components/responses/Error429Response'
        '500':
          $ref: '#/components/responses/Error500Response'
      security: []
components:
  schemas:
    instrument_type:
      type: string
      description: Instrument type
      enum:
        - perpetual
    category:
      type: string
      description: Instrument category
      enum:
        - equity
        - commodity
        - index
        - crypto
    Instrument:
      type: object
      required:
        - instrument_id
        - instrument_type
        - category
        - isolated_only
        - close_only
        - symbol
        - base_asset
        - quote_asset
        - funding_interval
        - quantity_decimals
        - price_decimals
        - price_bounds
        - liquidation_fee
        - max_order_count
        - min_notional
        - max_market_notional
        - max_limit_notional
        - max_leverage
        - risk_tiers
        - ui_live_time
      properties:
        instrument_id:
          $ref: '#/components/schemas/instrument_id'
        instrument_type:
          $ref: '#/components/schemas/instrument_type'
        category:
          $ref: '#/components/schemas/category'
        isolated_only:
          $ref: '#/components/schemas/isolated_only'
        symbol:
          $ref: '#/components/schemas/symbol'
        display_symbol:
          $ref: '#/components/schemas/display_symbol'
        base_asset:
          $ref: '#/components/schemas/base_asset'
        quote_asset:
          $ref: '#/components/schemas/quote_asset'
        funding_interval:
          $ref: '#/components/schemas/funding_interval'
        quantity_decimals:
          $ref: '#/components/schemas/quantity_decimals'
        price_decimals:
          $ref: '#/components/schemas/price_decimals'
        price_bounds:
          $ref: '#/components/schemas/price_bounds'
        liquidation_fee:
          $ref: '#/components/schemas/liquidation_fee'
        max_order_count:
          $ref: '#/components/schemas/max_order_count'
        min_notional:
          $ref: '#/components/schemas/min_notional'
        max_market_notional:
          $ref: '#/components/schemas/max_market_notional'
        max_limit_notional:
          $ref: '#/components/schemas/max_limit_notional'
        max_leverage:
          $ref: '#/components/schemas/max_leverage'
        risk_tiers:
          type: array
          items:
            $ref: '#/components/schemas/RiskTier'
        ui_live_time:
          $ref: '#/components/schemas/ui_live_time'
        close_only:
          $ref: '#/components/schemas/close_only'
        settlement:
          $ref: '#/components/schemas/InstrumentSettlement'
    instrument_id:
      type: integer
      description: Instrument ID
    isolated_only:
      type: boolean
      description: >-
        Whether the instrument supports only isolated account margin. When
        false, both cross and isolated account margin modes are supported.
    symbol:
      type: string
      description: Instrument symbol
      example: NVDA-USDC
    display_symbol:
      type: string
      description: >-
        Optional presentation override for the full instrument symbol, such as
        USA500-USD. Use display_symbol when present and fall back to symbol
        otherwise. This is a label, not an identifier; use instrument_id for
        trading and storage. Canonical symbol, base_asset, and price-feed
        identifiers are unchanged. Metadata normally refreshes once per minute;
        HTTP caching can add delay.
      example: USA500-USD
    base_asset:
      type: string
      description: Base asset name
      example: NVDA
    quote_asset:
      type: string
      description: Quote asset name
      example: USDC
    funding_interval:
      type: string
      description: Funding interval
      example: 1h
    quantity_decimals:
      type: integer
      description: Number of decimal places for quantity.
      example: 2
    price_decimals:
      type: integer
      description: >-
        Number of decimal places for price. Non-integer prices have a maximum of
        5 significant figures; integer prices are allowed regardless of
        significant figures.
      example: 2
    price_bounds:
      type: string
      description: Price bounds percentage
      example: '0.05'
    liquidation_fee:
      type: string
      description: Liquidation fee rate
      example: '0.025'
    max_order_count:
      type: integer
      description: Maximum open order count
      example: 200
    min_notional:
      type: string
      description: Minimum notional value in USD
      example: '1.00'
    max_market_notional:
      type: string
      description: Maximum market order notional value in USD
      example: '1000000.00'
    max_limit_notional:
      type: string
      description: Maximum limit order notional value in USD
      example: '10000000.00'
    max_leverage:
      type: integer
      description: Maximum leverage
      example: 20
    RiskTier:
      type: object
      required:
        - lower_bound
        - max_leverage
      properties:
        lower_bound:
          $ref: '#/components/schemas/lower_bound'
        max_leverage:
          $ref: '#/components/schemas/max_leverage'
    ui_live_time:
      type: integer
      nullable: true
      minimum: 0
      maximum: 253402300799000
      description: >-
        Unix timestamp in milliseconds when first-party interfaces may display
        the instrument. A null value means hidden. This advisory field does not
        affect trading availability.
      example: 1786032000000
    close_only:
      type: boolean
      description: >-
        Whether user orders must be reduce-only. Pricing, funding, and risk
        management continue until settlement.
    InstrumentSettlement:
      type: object
      description: >-
        Permanent settlement record. Its sequence and timestamp are the cutoff
        after which all unapplied funding is waived. Previously applied funding
        is preserved. An instrument with this record is delisted and cannot
        resume trading.
      required:
        - sequence
        - timestamp
        - price
        - insurance_debit
      properties:
        sequence:
          $ref: '#/components/schemas/settlement_sequence'
        timestamp:
          $ref: '#/components/schemas/settlement_timestamp'
        price:
          $ref: '#/components/schemas/settlement_price'
        insurance_debit:
          $ref: '#/components/schemas/settlement_insurance_debit'
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
    lower_bound:
      type: string
      description: Position size lower bound
      example: '0'
    settlement_sequence:
      type: integer
      format: int64
      minimum: 0
      description: Engine sequence of the accepted instrument settlement event.
    settlement_timestamp:
      type: integer
      format: int64
      minimum: 0
      description: >-
        Settlement cutoff as integer Unix milliseconds. The trailing 30-minute
        index average ends at this time.
    settlement_price:
      type: string
      description: >-
        Final settlement price from the trailing 30-minute time-weighted index
        average. Every remaining position closes at this price with no
        settlement fee.
    settlement_insurance_debit:
      type: string
      description: >-
        Total quote asset amount debited from the insurance fund to cover
        eligible settlement deficits.
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
