---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/trading/get-open-orders
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:41.670783
---

# Get Open Orders

> Returns all currently-open orders belonging to the authenticated portfolio. Orders are returned regardless of instrument or order type; filtering by instrument kind and order type is not currently supported.

Each order includes `instrument_id`, `product_group`, and the `post_only`, `reject_post_only`, and `reduce_only` flags. `instrument_id` is the numeric instrument id. `product_group` is the Starbase routing group (`BTC`, `ETH`, `TIER_2`, or `TIER_3`). `post_only` and `reject_post_only` correspond to the SBE `postOnly` and `postOnlyReject` bits and are mutually exclusive. `reduce_only` reflects per-order reduce-only from [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview) or FIX (it cannot be set per order in SBE).

The portfolio is resolved from the authenticated session. There is no parameter to query another portfolio's orders. MMP-flagged orders are visible via this endpoint. Orders placed via Mass Quote (MassQuoteRequest) are included.

This endpoint is rate-limited to 10 requests per minute per portfolio on each REST gateway. The A and B gateways enforce this cap independently. Exceeding the limit returns HTTP 429. Because this limit is heavily restrictive relative to typical order-book activity, this endpoint is best used for periodic reconciliation rather than to maintain live order state. To track open orders in real time, maintain a dedicated [FIX Drop Copy](/starbase/fix-drop-copy-api) session instead of polling this endpoint.


## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/private/get_open_orders
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
  /api/v2/private/get_open_orders:
    get:
      tags:
        - Trading
      summary: Get Open Orders
      description: >-
        Returns all currently-open orders belonging to the authenticated
        portfolio. Orders are returned regardless of instrument or order type;
        filtering by instrument kind and order type is not currently supported.


        Each order includes `instrument_id`, `product_group`, and the
        `post_only`, `reject_post_only`, and `reduce_only` flags.
        `instrument_id` is the numeric instrument id. `product_group` is the
        Starbase routing group (`BTC`, `ETH`, `TIER_2`, or `TIER_3`).
        `post_only` and `reject_post_only` correspond to the SBE `postOnly` and
        `postOnlyReject` bits and are mutually exclusive. `reduce_only` reflects
        per-order reduce-only from [classic
        JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview) or FIX
        (it cannot be set per order in SBE).


        The portfolio is resolved from the authenticated session. There is no
        parameter to query another portfolio's orders. MMP-flagged orders are
        visible via this endpoint. Orders placed via Mass Quote
        (MassQuoteRequest) are included.


        This endpoint is rate-limited to 10 requests per minute per portfolio on
        each REST gateway. The A and B gateways enforce this cap independently.
        Exceeding the limit returns HTTP 429. Because this limit is heavily
        restrictive relative to typical order-book activity, this endpoint is
        best used for periodic reconciliation rather than to maintain live order
        state. To track open orders in real time, maintain a dedicated [FIX Drop
        Copy](/starbase/fix-drop-copy-api) session instead of polling this
        endpoint.
      operationId: get_open_orders
      responses:
        '200':
          description: List of open orders for the authenticated portfolio. May be empty.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOpenOrdersResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result:
                  - order_id: 1cc1c718-49e0-4ea5-8902-f3f22968c350
                    instrument_id: 310001
                    instrument_name: TREE-USD
                    product_group: TIER_3
                    side: sell
                    price: 0.0717
                    amount: 83698
                    filled_amount: 0
                    average_price: 0
                    order_state: open
                    order_type: limit
                    post_only: true
                    reject_post_only: false
                    reduce_only: false
                    creation_timestamp: 1778270370643
                    last_update_timestamp: 1778270370643
        '401':
          description: Missing or invalid `Authorization` header.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '429':
          description: >-
            Per-portfolio rate limit for this endpoint exceeded on this REST
            gateway. The cap is 10 requests per minute
            (`portfolio-rate-limit.get_open_orders`). The A and B gateways each
            keep their own counter. The response includes `Retry-After` (seconds
            until the next one-minute window).
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '500':
          description: Internal server error while reading the active-order set.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
      security:
        - BearerAuth: []
components:
  schemas:
    GetOpenOrdersResponse:
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
          description: Array of open orders for the authenticated portfolio. May be empty.
          items:
            $ref: '#/components/schemas/Order'
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
    Order:
      type: object
      description: A single open order from the authenticated portfolio.
      required:
        - order_id
        - instrument_id
        - instrument_name
        - side
        - price
        - amount
        - filled_amount
        - order_state
        - order_type
      properties:
        order_id:
          type: string
          description: >-
            Exchange-assigned order identifier (UUID-style string). Stable for
            the lifetime of the order.
          example: 1cc1c718-49e0-4ea5-8902-f3f22968c350
        instrument_id:
          type: integer
          format: int64
          description: >-
            Numeric identifier of the instrument the order was placed against.
            Same value as `instrument_id` on `get_instruments` and
            `instrumentId` in the SBE schema.
          example: 310001
        instrument_name:
          type: string
          description: Human-readable instrument symbol the order was placed against.
          example: TREE-USD
        product_group:
          type: string
          nullable: true
          description: >-
            Starbase routing group resolved from the base symbol of the
            instrument's currency pair (for example `BTC`, `ETH`, `TIER_2`, or
            `TIER_3`). Same classification as `product_group` on
            `get_instruments`.
          example: TIER_3
        side:
          type: string
          enum:
            - buy
            - sell
          description: Order side.
        price:
          type: number
          description: Limit price of the order (in quote-currency units).
          example: 0.0717
        amount:
          type: number
          description: Original order quantity, in base-currency units.
          example: 83698
        filled_amount:
          type: number
          description: Quantity filled so far, in base-currency units.
          example: 0
        average_price:
          type: number
          description: >-
            Volume-weighted average fill price across all executions on this
            order. Zero if the order has no fills yet.
          example: 0
        order_state:
          type: string
          enum:
            - open
          description: >-
            Order state. Currently always `open` for entries returned by this
            endpoint, since only open orders are listed.
        order_type:
          type: string
          enum:
            - limit
            - market
          description: Order type, derived from the price field.
        time_in_force:
          type: string
          nullable: true
          enum:
            - GTC
            - IOC
            - FOK
            - GTD
          description: Time-in-force policy.
        post_only:
          type: boolean
          description: >-
            Whether the order was submitted as post-only: if it would take
            liquidity, the price is amended to the best bid/ask instead of
            rejecting. Corresponds to SBE `postOnly`. Mutually exclusive with
            `reject_post_only`.
        reject_post_only:
          type: boolean
          description: >-
            Whether the order was submitted as post-only reject: if it would
            take liquidity, the order is rejected rather than price-amended.
            Corresponds to SBE `postOnlyReject`. Mutually exclusive with
            `post_only`.
        reduce_only:
          type: boolean
          description: >-
            Whether the order is reduce-only (intended only to reduce an
            existing position). Per-order reduce-only originates from [classic
            JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview) or
            FIX; it cannot be set per order in SBE.
        creation_timestamp:
          type: integer
          format: int64
          description: Order submission time in milliseconds since the Unix epoch.
          example: 1778270370643
        last_update_timestamp:
          type: integer
          format: int64
          description: >-
            Time of the most recent change to the order, in milliseconds since
            the Unix epoch.
          example: 1778270370643
        label:
          type: string
          nullable: true
          description: Client-supplied label for the order, if any.
        api:
          type: boolean
          nullable: true
          description: Whether the order was placed via API.
        max_show:
          type: number
          nullable: true
          description: Iceberg display quantity, if applicable.
        profit_loss:
          type: number
          nullable: true
          description: Realised profit/loss attributable to this order, if any.
        commission:
          type: number
          nullable: true
          description: Commission accrued by this order so far, if any.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        API key passed as a Bearer token. The authenticated session determines
        the portfolio that operations are applied to.

````

## Related topics

- [private/get_open_orders](https://docs.deribit.com/api-reference/trading/private-get_open_orders.md)
- [private/get_open_orders_by_instrument](https://docs.deribit.com/api-reference/trading/private-get_open_orders_by_instrument.md)
- [private/get_open_orders_by_label](https://docs.deribit.com/api-reference/trading/private-get_open_orders_by_label.md)
- [private/get_open_orders_by_currency](https://docs.deribit.com/api-reference/trading/private-get_open_orders_by_currency.md)
- [Quickstart Guide](https://docs.deribit.com/articles/deribit-quickstart.md)