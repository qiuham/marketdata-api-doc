---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/market-data/list-instruments
api_type: JSON-RPC
updated_at: 2026-11-18 18:59:11.503564
---

# List Instruments

> Returns the list of tradeable instruments, including `index_id` and `product_group`, optionally filtered by base currency, instrument kind, expiration status, instrument id, product group, and lifecycle state.

This endpoint requires no authentication, but it is served by the Starbase REST gateway and is reachable only through hosted colocation, a cross-connect, or AWS Private Link. The internet-accessible [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview) `public/get_instruments` method also documents `index_id` and `product_group`; backend rollout of those fields may temporarily differ between the two endpoints.

This endpoint does not return `contract_size`, `min_trade_amount`, `settlement_period`, `settlement_currency`, or commission rates. `settlement_currency` was removed in June 2026; it always equalled `quote_currency`, so read `quote_currency` instead. For contract size, use classic JSON-RPC [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments), [`public/get_instrument`](https://docs.deribit.com/api-reference/market-data/public-get_instrument), or [`public/get_contract_size`](https://docs.deribit.com/api-reference/market-data/public-get_contract_size). Starbase does not use contract size for matching; the quantity increment on this endpoint is `qty_tick_size`.

Filter semantics (supplied filters are combined):
- `currency` filters by the **base** currency of the instrument's currency pair (case-insensitive exact match, for example `BTC` or `ETH`). Omit `currency` to return instruments for every base currency. A value that is not a listed base currency, including `any`, matches no instrument: the call succeeds and `result` is an empty array. `any` is compared as a base-currency name.
- `kind` filters by instrument type (case-insensitive match against the `kind` value enum).
- `expired = true` returns only instruments whose `expiration_timestamp` is in the past; `expired = false` returns only non-expired instruments. Omit the parameter to get both.
- `instrument_id` returns the instrument with that numeric id.
- `product_group` filters by Starbase product group (case-insensitive match against `BTC`, `ETH`, `TIER_2`, `TIER_3`).
- `state` filters by instrument lifecycle state (case-insensitive). Values match SBE `InstrumentStatus`: `open`, `inactive`, `settlement`, `delivered`, `locked`, `halted`.


## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/public/get_instruments
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
  /api/v2/public/get_instruments:
    get:
      tags:
        - Market Data
      summary: List Instruments
      description: >-
        Returns the list of tradeable instruments, including `index_id` and
        `product_group`, optionally filtered by base currency, instrument kind,
        expiration status, instrument id, product group, and lifecycle state.


        This endpoint requires no authentication, but it is served by the
        Starbase REST gateway and is reachable only through hosted colocation, a
        cross-connect, or AWS Private Link. The internet-accessible [classic
        JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview)
        `public/get_instruments` method also documents `index_id` and
        `product_group`; backend rollout of those fields may temporarily differ
        between the two endpoints.


        This endpoint does not return `contract_size`, `min_trade_amount`,
        `settlement_period`, `settlement_currency`, or commission rates.
        `settlement_currency` was removed in June 2026; it always equalled
        `quote_currency`, so read `quote_currency` instead. For contract size,
        use classic JSON-RPC
        [`public/get_instruments`](https://docs.deribit.com/api-reference/market-data/public-get_instruments),
        [`public/get_instrument`](https://docs.deribit.com/api-reference/market-data/public-get_instrument),
        or
        [`public/get_contract_size`](https://docs.deribit.com/api-reference/market-data/public-get_contract_size).
        Starbase does not use contract size for matching; the quantity increment
        on this endpoint is `qty_tick_size`.


        Filter semantics (supplied filters are combined):

        - `currency` filters by the **base** currency of the instrument's
        currency pair (case-insensitive exact match, for example `BTC` or
        `ETH`). Omit `currency` to return instruments for every base currency. A
        value that is not a listed base currency, including `any`, matches no
        instrument: the call succeeds and `result` is an empty array. `any` is
        compared as a base-currency name.

        - `kind` filters by instrument type (case-insensitive match against the
        `kind` value enum).

        - `expired = true` returns only instruments whose `expiration_timestamp`
        is in the past; `expired = false` returns only non-expired instruments.
        Omit the parameter to get both.

        - `instrument_id` returns the instrument with that numeric id.

        - `product_group` filters by Starbase product group (case-insensitive
        match against `BTC`, `ETH`, `TIER_2`, `TIER_3`).

        - `state` filters by instrument lifecycle state (case-insensitive).
        Values match SBE `InstrumentStatus`: `open`, `inactive`, `settlement`,
        `delivered`, `locked`, `halted`.
      operationId: get_instruments
      parameters:
        - name: currency
          in: query
          required: false
          description: >-
            Filter by the base currency of the instrument's currency pair (for
            example `BTC`, `ETH`, `AVAX`). Case-insensitive exact match. Omit
            this parameter to return instruments for every base currency. A
            value that is not a listed base currency, including `any`, matches
            no instrument, so the call succeeds with an empty `result`. `any` is
            compared as a base-currency name.
          schema:
            type: string
          example: BTC
        - name: kind
          in: query
          required: false
          description: Filter by instrument kind. Case-insensitive.
          schema:
            type: string
            enum:
              - perp_future
              - option
              - spot
              - future_combo
              - option_combo
              - dated_future
          example: perp_future
        - name: expired
          in: query
          required: false
          description: >-
            When `true`, return only expired instruments. When `false`, return
            only currently-active (non-expired) instruments. Omit to return
            both.
          schema:
            type: boolean
          example: false
        - name: instrument_id
          in: query
          required: false
          description: Return the instrument with this numeric id.
          schema:
            type: integer
            format: int64
          example: 124942
        - name: product_group
          in: query
          required: false
          description: Filter by Starbase product group. Case-insensitive.
          schema:
            type: string
            enum:
              - BTC
              - ETH
              - TIER_2
              - TIER_3
          example: BTC
        - name: state
          in: query
          required: false
          description: >-
            Filter by instrument lifecycle state. Case-insensitive. Values match
            SBE `InstrumentStatus`.
          schema:
            type: string
            enum:
              - open
              - inactive
              - settlement
              - delivered
              - locked
              - halted
          example: open
      responses:
        '200':
          description: List of instruments matching the supplied filters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetInstrumentsResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result:
                  - instrument_id: 124942
                    instrument_name: ETH-PERPETUAL
                    kind: perp_future
                    product_group: ETH
                    base_currency: ETH
                    quote_currency: USDC
                    tick_size: 0.01
                    qty_tick_size: 1
                    state: open
                    creation_timestamp: 1747500000000000000
                  - instrument_id: 200001
                    instrument_name: BTC-30MAY26-70000-C
                    kind: option
                    product_group: BTC
                    base_currency: BTC
                    quote_currency: USDC
                    tick_size: 0.5
                    qty_tick_size: 0.1
                    strike: 70000
                    option_type: call
                    state: open
                    expiration_timestamp: 1779148800000000000
                    creation_timestamp: 1748400000000000000
        '500':
          description: Internal server error while building the instrument list.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
      security: []
components:
  schemas:
    GetInstrumentsResponse:
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
          description: Array of instruments matching the supplied filters. May be empty.
          items:
            $ref: '#/components/schemas/Instrument'
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
    Instrument:
      type: object
      description: A tradeable instrument's reference data.
      required:
        - instrument_id
        - instrument_name
        - kind
      properties:
        instrument_id:
          type: integer
          format: int64
          description: Stable numeric identifier for the instrument.
          example: 124942
        instrument_name:
          type: string
          description: >-
            Human-readable instrument symbol (e.g. `ETH-PERPETUAL`,
            `BTC-30MAY26-70000-C`).
          example: ETH-PERPETUAL
        kind:
          type: string
          enum:
            - perp_future
            - option
            - spot
            - future_combo
            - option_combo
            - dated_future
          description: Instrument category.
        index_id:
          type: integer
          format: int64
          nullable: true
          description: Numeric identifier for the index associated with the instrument.
        product_group:
          type: string
          nullable: true
          description: >-
            Starbase routing group resolved from the base symbol of the
            instrument's currency pair (for example `BTC`, `ETH`, `TIER_2`, or
            `TIER_3`).
          example: ETH
        base_currency:
          type: string
          nullable: true
          description: Base currency of the instrument's currency pair.
          example: ETH
        quote_currency:
          type: string
          nullable: true
          description: Quote currency of the instrument's currency pair.
          example: USDC
        tick_size:
          type: number
          description: Minimum price increment for the instrument.
          example: 0.01
        qty_tick_size:
          type: number
          description: >-
            Minimum quantity increment (step size) for order amounts on this
            instrument, expressed in the instrument's amount units. This is the
            same value the SBE `InstrumentDefinition` (10) message carries as
            `minOrderQuantity × 10^quantityExponent`. For example `qty_tick_size
            = 0.1` corresponds to `minOrderQuantity = 1` with `quantityExponent
            = -1`. Not a contract size: this endpoint does not return
            `contract_size`. Classic JSON-RPC `public/get_instruments` does not
            return this field; the equivalent classic JSON-RPC name is
            `min_trade_amount`. See [JSON-RPC
            overview](https://docs.deribit.com/articles/json-rpc-overview).
          example: 0.1
        strike:
          type: number
          nullable: true
          description: Strike price (options only). `null` for non-option instruments.
          example: 70000
        option_type:
          type: string
          enum:
            - call
            - put
          nullable: true
          description: Option type (options only). `null` for non-option instruments.
        state:
          type: string
          enum:
            - open
            - inactive
            - settlement
            - delivered
            - locked
            - halted
          description: >-
            Instrument lifecycle state, the lowercase SBE `InstrumentStatus`
            value. `open` means the instrument is enabled for trading. Accepted
            by the `state` filter.
          example: open
        expiration_timestamp:
          type: integer
          format: int64
          nullable: true
          description: >-
            Instrument expiration time in nanoseconds since the Unix epoch.
            `null` for perpetuals and other non-expiring instruments.
          example: 1779148800000000000
        creation_timestamp:
          type: integer
          format: int64
          nullable: true
          description: >-
            Instrument creation/listing time in nanoseconds since the Unix
            epoch.
          example: 1747500000000000000

````

## Related topics

- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Security List(y) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-list.md)
- [public/get_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments.md)
- [Security List Request(x) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-list-request.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)