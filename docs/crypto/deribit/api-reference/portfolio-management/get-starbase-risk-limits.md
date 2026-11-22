---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/portfolio-management/get-starbase-risk-limits
api_type: JSON-RPC
updated_at: 2026-11-22 18:59:25.017730
---

# Get Starbase Risk Limits

> Returns the effective position ("risk") limits for the authenticated portfolio, one entry per underlying (currency pair).

Each numeric field is resolved per field: a portfolio override wins when that field is set, otherwise the currency-pair default is used. A field unset at both levels is omitted. `-1` means the limit is explicitly unlimited (distinct from unset). The call is read-only and does not change limits.

Only underlyings that have a currency-pair default or an override for this portfolio are included. Overrides that belong to other portfolios do not create an entry.

Pass `currency` to select one underlying. The value is the currency-pair name returned in `currency` (for example `BTC_USDC`). Matching is case-insensitive and ignores separators, so `btc-usdc` and `BTCUSDC` resolve to the same pair. An unknown name returns HTTP 400. A known pair with no configured limit for this portfolio returns an empty list.

The portfolio is resolved from the authenticated session. There is no parameter to query another portfolio.

This endpoint is rate-limited to 1 request per minute per portfolio on each REST gateway. The A and B gateways enforce this cap independently. Exceeding the limit returns HTTP 429.


## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/private/get_starbase_risk_limits
openapi: 3.0.3
info:
  title: Starbase REST API
  version: '2.0'
  description: Portfolio-scoped REST API for the Starbase direct-access trading platform.
servers:
  - url: http://195.138.37.5:4410
    description: Production (Gateway A, rest-order)
  - url: http://195.138.37.6:4410
    description: Production (Gateway B, rest-order)
  - url: http://195.138.37.137:4410
    description: Test (Gateway A, rest-order)
  - url: http://195.138.37.138:4410
    description: Test (Gateway B, rest-order)
security: []
tags:
  - name: Portfolio Management
    description: Endpoints that operate on the authenticated portfolio.
  - name: Trading
    description: Authenticated trading endpoints scoped to the caller's portfolio.
  - name: Market Data
    description: >-
      Unauthenticated Starbase reference and market data endpoints. No API
      credentials are required, but the Starbase REST gateway is reachable only
      through private Starbase connectivity.
paths:
  /api/v2/private/get_starbase_risk_limits:
    get:
      tags:
        - Portfolio Management
      summary: Get Starbase Risk Limits
      description: >-
        Returns the effective position ("risk") limits for the authenticated
        portfolio, one entry per underlying (currency pair).


        Each numeric field is resolved per field: a portfolio override wins when
        that field is set, otherwise the currency-pair default is used. A field
        unset at both levels is omitted. `-1` means the limit is explicitly
        unlimited (distinct from unset). The call is read-only and does not
        change limits.


        Only underlyings that have a currency-pair default or an override for
        this portfolio are included. Overrides that belong to other portfolios
        do not create an entry.


        Pass `currency` to select one underlying. The value is the currency-pair
        name returned in `currency` (for example `BTC_USDC`). Matching is
        case-insensitive and ignores separators, so `btc-usdc` and `BTCUSDC`
        resolve to the same pair. An unknown name returns HTTP 400. A known pair
        with no configured limit for this portfolio returns an empty list.


        The portfolio is resolved from the authenticated session. There is no
        parameter to query another portfolio.


        This endpoint is rate-limited to 1 request per minute per portfolio on
        each REST gateway. The A and B gateways enforce this cap independently.
        Exceeding the limit returns HTTP 429.
      operationId: get_starbase_risk_limits
      parameters:
        - name: currency
          in: query
          required: false
          description: >-
            Currency-pair name to return (for example `BTC_USDC`).
            Case-insensitive; separators such as `_`, `-`, and spaces are
            ignored. Omit to return every underlying that has a configured limit
            for this portfolio.
          schema:
            type: string
          example: BTC_USDC
      responses:
        '200':
          description: >-
            Effective position limits for the authenticated portfolio. May be
            empty.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetStarbaseRiskLimitsResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result:
                  - currency: BTC_USDC
                    sm_max_future_position_size: 10
                    pm_max_future_open_order_size: 200
                    pm_max_option_open_contracts: 300
                    max_open_orders: 11
                    sm_max_open_orders_per_instrument: 20
                    pm_max_future_open_orders: 30
                    pm_max_option_open_orders: 40
        '400':
          description: 'Unknown `currency`. The message is `unknown currency: <value>`.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '401':
          description: Missing or invalid `Authorization` header.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '429':
          description: >-
            Per-portfolio rate limit for this endpoint exceeded. Default is 1
            request per minute
            (`portfolio-rate-limit.get_starbase_risk_limits`). The response
            includes `Retry-After` (seconds until the next one-minute window).
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '500':
          description: Internal server error while resolving position limits.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
      security:
        - BearerAuth: []
components:
  schemas:
    GetStarbaseRiskLimitsResponse:
      type: object
      required:
        - jsonrpc
        - result
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          type: array
          description: Effective position limits, one entry per underlying. May be empty.
          items:
            $ref: '#/components/schemas/StarbaseRiskLimit'
    JsonRpcError:
      type: object
      required:
        - jsonrpc
        - error
      description: JSON-RPC 2.0 error envelope returned for failed requests.
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
        id:
          type: integer
          nullable: true
          description: The id that was sent in the request, if any.
        error:
          type: object
          required:
            - code
            - message
          properties:
            code:
              type: integer
              description: Numeric JSON-RPC error code.
            message:
              type: string
              description: Human-readable error description.
            data:
              description: Optional additional error details.
    StarbaseRiskLimit:
      type: object
      description: >-
        Effective position limits for one underlying (currency pair), after
        merging the portfolio override over the currency-pair default. A field
        set on the override replaces the default for that field only. Omitted
        fields are unset at both levels. `-1` means explicitly unlimited.
      required:
        - currency
      properties:
        currency:
          type: string
          description: >-
            Currency-pair name (for example `BTC_USDC`). Pass this value back as
            the `currency` query parameter to read the same underlying.
          example: BTC_USDC
        sm_max_future_position_size:
          type: number
          nullable: true
          description: >-
            Standard Margin: maximum net future position size if filled. USD
            notional for inverse contracts, quantity for linear contracts.
            Omitted when unset. `-1` means unlimited.
          example: 10
        pm_max_future_open_order_size:
          type: number
          nullable: true
          description: >-
            Portfolio Margin: maximum total size of future open orders per side.
            USD notional for inverse contracts, quantity for linear contracts.
            Omitted when unset. `-1` means unlimited. An order or replace that
            would breach it is rejected with `ORDER_SIZE_LIMIT_EXCEEDED` (`28`).
          example: 200
        pm_max_option_open_contracts:
          type: number
          nullable: true
          description: >-
            Portfolio Margin: maximum total size of option open contracts per
            side, in contracts. Omitted when unset. `-1` means unlimited. An
            order or replace that would breach it is rejected with
            `ORDER_SIZE_LIMIT_EXCEEDED` (`28`).
          example: 300
        max_open_orders:
          type: integer
          nullable: true
          description: >-
            Maximum open orders on derivatives across all instruments of this
            currency pair. Applies to both Standard Margin and Portfolio Margin.
            Omitted when unset. `-1` means unlimited.
          example: 11
        sm_max_open_orders_per_instrument:
          type: integer
          nullable: true
          description: >-
            Standard Margin: maximum open orders per instrument. Omitted when
            unset. `-1` means unlimited.
          example: 20
        pm_max_future_open_orders:
          type: integer
          nullable: true
          description: >-
            Portfolio Margin: maximum future open orders per side. Omitted when
            unset. `-1` means unlimited.
          example: 30
        pm_max_option_open_orders:
          type: integer
          nullable: true
          description: >-
            Portfolio Margin: maximum option open orders per side. Omitted when
            unset. `-1` means unlimited.
          example: 40
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        API key passed as a Bearer token. The authenticated session determines
        the portfolio that operations are applied to.

````

## Related topics

- [Starbase API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Portfolio Management](https://docs.deribit.com/starbase/portfolio-management.md)
- [Starbase Market Maker Protection (MMP)](https://docs.deribit.com/starbase/mmp.md)
- [Risk Bypass](https://docs.deribit.com/starbase/risk-bypass.md)