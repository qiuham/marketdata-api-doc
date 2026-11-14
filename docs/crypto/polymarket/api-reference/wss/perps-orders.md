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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-orders'
updated_at: 2026-11-13
---

# Orders

> Perps WebSocket private order updates.



## AsyncAPI

````yaml asyncapi-perps.json orders
id: orders
title: Orders
description: Real-time order updates. Requires authentication, see [Auth](/ws/auth).
servers:
  - id: production
    protocol: wss
    host: ws.perpetuals.polymarket.com
    bindings: []
    variables: []
address: /v1/ws
parameters: []
bindings: []
operations:
  - &ref_1
    id: OrdersSubscribe
    title: Orders subscribe
    description: Subscribe to orders
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: Subscribe to private order updates (requires prior auth)
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: req
                type: string
                description: Request type
                enumValues:
                  - post
                  - sub
                  - unsub
                required: true
              - name: chs
                type: array
                description: 'Orders private channel: "orders"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - orders
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-576>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-577>
            chs:
              type: array
              description: 'Orders private channel: "orders"'
              items:
                type: string
                enum:
                  - orders
                x-parser-schema-id: <anonymous-schema-579>
              example:
                - orders
              x-parser-schema-id: <anonymous-schema-578>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-575>
        title: Subscribe
        description: Subscribe to private order updates (requires prior auth)
        example: |-
          {
            "req": "sub",
            "chs": [
              "orders"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: orders
  - &ref_3
    id: OrdersSubscribeResponse
    title: Orders subscribe response
    description: Orders subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to orders subscribe request
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: array
                title: Subscribe Response
                required: true
                properties:
                  - name: item
                    type: object
                    required: false
                    properties:
                      - name: status
                        type: string
                        enumValues:
                          - ok
                        required: true
                      - name: status
                        type: string
                        enumValues:
                          - err
                        required: true
                      - name: error
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Response
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-581>
            data:
              title: Subscribe Response
              type: array
              items:
                oneOf:
                  - type: object
                    required:
                      - status
                    properties:
                      status:
                        type: string
                        enum:
                          - ok
                        x-parser-schema-id: <anonymous-schema-585>
                    x-parser-schema-id: <anonymous-schema-584>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-587>
                      error:
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        example: insufficient_margin
                        x-parser-schema-id: <anonymous-schema-588>
                    x-parser-schema-id: <anonymous-schema-586>
                x-parser-schema-id: <anonymous-schema-583>
              x-parser-schema-id: <anonymous-schema-582>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-580>
        title: Subscribe Response
        description: Response to orders subscribe request
        example: |-
          {
            "data": []
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeResponse
    bindings: []
    extensions: *ref_0
  - &ref_2
    id: OrdersUnsubscribe
    title: Orders unsubscribe
    description: Unsubscribe from orders
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from private order updates
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: req
                type: string
                description: Request type
                enumValues:
                  - post
                  - sub
                  - unsub
                required: true
              - name: chs
                type: array
                description: 'Orders private channel: "orders"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - orders
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-590>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-591>
            chs:
              type: array
              description: 'Orders private channel: "orders"'
              items:
                type: string
                enum:
                  - orders
                x-parser-schema-id: <anonymous-schema-593>
              example:
                - orders
              x-parser-schema-id: <anonymous-schema-592>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-589>
        title: Unsubscribe
        description: Unsubscribe from private order updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "orders"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: OrdersUnsubscribeResponse
    title: Orders unsubscribe response
    description: Orders unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to orders unsubscribe request
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: array
                title: Subscribe Response
                required: true
                properties:
                  - name: item
                    type: object
                    required: false
                    properties:
                      - name: status
                        type: string
                        enumValues:
                          - ok
                        required: true
                      - name: status
                        type: string
                        enumValues:
                          - err
                        required: true
                      - name: error
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Response
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-595>
            data:
              title: Subscribe Response
              type: array
              items:
                oneOf:
                  - type: object
                    required:
                      - status
                    properties:
                      status:
                        type: string
                        enum:
                          - ok
                        x-parser-schema-id: <anonymous-schema-599>
                    x-parser-schema-id: <anonymous-schema-598>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-601>
                      error:
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        example: insufficient_margin
                        x-parser-schema-id: <anonymous-schema-602>
                    x-parser-schema-id: <anonymous-schema-600>
                x-parser-schema-id: <anonymous-schema-597>
              x-parser-schema-id: <anonymous-schema-596>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-594>
        title: Unsubscribe Response
        description: Response to orders unsubscribe request
        example: |-
          {
            "data": []
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeResponse
    bindings: []
    extensions: *ref_0
  - &ref_5
    id: OrdersUpdate
    title: Orders update
    description: Receive order updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: Real-time order updates for authenticated users
            type: object
            properties:
              - name: ch
                type: string
                description: >-
                  Channel name for push data. Parameterized channels include the
                  instrument ID (e.g. "trades::1", "book::1", "klines::1::1m",
                  "tickers::all"). Most private channels use plain names (e.g.
                  "fills", "orders"). TP/SL updates are the exception: they are
                  suffixed with the authenticated account's numeric ID (e.g.
                  "tpsl::12345"), so match them on the "tpsl::" prefix.
                  Subscribe and unsubscribe requests still use the bare "tpsl".
                required: true
              - name: ts
                type: integer
                description: >-
                  Request timestamp. Unix milliseconds for most operations; Unix
                  seconds for withdrawals (must match the on-chain EIP-712
                  struct verified against block.timestamp).
                required: true
              - name: sq
                type: integer
                description: Sequence number
                required: true
              - name: data
                type: object
                description: Order object
                required: true
                properties:
                  - name: oid
                    type: integer
                    description: Order ID
                    required: true
                  - name: iid
                    type: integer
                    description: Instrument ID
                    required: true
                  - name: buy
                    type: boolean
                    description: Is buy
                    required: true
                  - name: p
                    type: string
                    description: Price
                    required: true
                  - name: qty
                    type: string
                    description: Quantity in no. of contracts
                    required: true
                  - name: tif
                    type: string
                    description: Time in force
                    enumValues:
                      - gtc
                      - ioc
                      - fok
                    required: true
                  - name: po
                    type: boolean
                    description: Post only
                    required: true
                  - name: ro
                    type: boolean
                    description: Reduce only
                    required: true
                  - name: rest
                    type: string
                    description: Resting quantity
                    required: true
                  - name: fill
                    type: string
                    description: Filled quantity
                    required: true
                  - name: cts
                    type: integer
                    description: Create timestamp in milliseconds
                    required: true
                  - name: uts
                    type: integer
                    description: Update timestamp in milliseconds
                    required: true
                  - name: status
                    type: string
                    description: >-
                      Order status, such as `open` for a resting order. See
                      [Handle Terminal Order
                      Outcomes](/perps/trading#handle-terminal-order-outcomes)
                      for the statuses that end an order.
                    required: true
                  - name: coid
                    type: string
                    description: Client order ID
                    required: false
                  - name: builder
                    type: object
                    description: >-
                      Saved builder terms. Address is the registered Perps
                      account, and fee_rate is an additional fraction of
                      executed notional. Terms survive approval revocation for
                      existing orders.
                    required: false
                    properties:
                      - name: address
                        type: string
                        description: Address
                        required: true
                      - name: fee_rate
                        type: string
                        description: >-
                          Additional builder fee as a decimal fraction of
                          executed notional, from 0 through 0.001 (10 basis
                          points). Zero approval revokes future admission. Never
                          a percentage string.
                        required: true
        headers: []
        jsonPayloadSchema:
          title: Orders Update
          type: object
          properties:
            ch:
              type: string
              description: >-
                Channel name for push data. Parameterized channels include the
                instrument ID (e.g. "trades::1", "book::1", "klines::1::1m",
                "tickers::all"). Most private channels use plain names (e.g.
                "fills", "orders"). TP/SL updates are the exception: they are
                suffixed with the authenticated account's numeric ID (e.g.
                "tpsl::12345"), so match them on the "tpsl::" prefix. Subscribe
                and unsubscribe requests still use the bare "tpsl".
              example: trades::1
              x-parser-schema-id: <anonymous-schema-604>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-605>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-606>
            data:
              type: object
              description: Order object
              properties:
                oid:
                  type: integer
                  description: Order ID
                  example: 1234567890
                  x-parser-schema-id: <anonymous-schema-608>
                iid:
                  type: integer
                  description: Instrument ID
                  example: 1
                  x-parser-schema-id: <anonymous-schema-609>
                buy:
                  type: boolean
                  description: Is buy
                  example: true
                  x-parser-schema-id: <anonymous-schema-610>
                p:
                  type: string
                  description: Price
                  example: '100.00'
                  x-parser-schema-id: <anonymous-schema-611>
                qty:
                  type: string
                  description: Quantity in no. of contracts
                  example: '10.00'
                  x-parser-schema-id: <anonymous-schema-612>
                tif:
                  type: string
                  description: Time in force
                  enum:
                    - gtc
                    - ioc
                    - fok
                  x-parser-schema-id: <anonymous-schema-613>
                po:
                  type: boolean
                  description: Post only
                  default: false
                  example: false
                  x-parser-schema-id: <anonymous-schema-614>
                ro:
                  type: boolean
                  description: Reduce only
                  example: false
                  default: false
                  x-parser-schema-id: <anonymous-schema-615>
                rest:
                  type: string
                  description: Resting quantity
                  example: '9.00'
                  x-parser-schema-id: <anonymous-schema-616>
                fill:
                  type: string
                  description: Filled quantity
                  example: '1.00'
                  x-parser-schema-id: <anonymous-schema-617>
                cts:
                  type: integer
                  description: Create timestamp in milliseconds
                  example: 1767225600000
                  x-parser-schema-id: <anonymous-schema-618>
                uts:
                  type: integer
                  description: Update timestamp in milliseconds
                  example: 1767225600000
                  x-parser-schema-id: <anonymous-schema-619>
                status:
                  type: string
                  description: >-
                    Order status, such as `open` for a resting order. See
                    [Handle Terminal Order
                    Outcomes](/perps/trading#handle-terminal-order-outcomes) for
                    the statuses that end an order.
                  example: open
                  x-parser-schema-id: <anonymous-schema-620>
                coid:
                  type: string
                  description: Client order ID
                  minLength: 32
                  maxLength: 32
                  pattern: ^[0-9a-f]{32}$
                  example: 550e8400e29b41d4a716446655440000
                  x-parser-schema-id: <anonymous-schema-621>
                builder:
                  type: object
                  description: >-
                    Saved builder terms. Address is the registered Perps
                    account, and fee_rate is an additional fraction of executed
                    notional. Terms survive approval revocation for existing
                    orders.
                  required:
                    - address
                    - fee_rate
                  properties:
                    address:
                      type: string
                      description: Address
                      example: '0x1234567890abcdef1234567890abcdef12345678'
                      x-parser-schema-id: <anonymous-schema-623>
                    fee_rate:
                      type: string
                      description: >-
                        Additional builder fee as a decimal fraction of executed
                        notional, from 0 through 0.001 (10 basis points). Zero
                        approval revokes future admission. Never a percentage
                        string.
                      example: '0.001'
                      x-parser-schema-id: <anonymous-schema-624>
                  x-parser-schema-id: <anonymous-schema-622>
              required:
                - oid
                - iid
                - buy
                - p
                - qty
                - tif
                - po
                - ro
                - status
                - rest
                - fill
                - cts
                - uts
              x-parser-schema-id: <anonymous-schema-607>
          required:
            - ch
            - ts
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-603>
        title: Update
        description: Real-time order updates for authenticated users
        example: |-
          {
            "ch": "orders",
            "ts": 1767225600000,
            "ets": 1767225600000,
            "sq": 1234567890,
            "data": {
              "oid": 1234567890,
              "iid": 1,
              "buy": true,
              "p": "100.00",
              "qty": "10.00",
              "tif": "gtc",
              "po": false,
              "ro": false,
              "rest": "9.00",
              "fill": "1.00",
              "cts": 1767225600000,
              "uts": 1767225600000,
              "status": "open",
              "coid": "550e8400e29b41d4a716446655440000",
              "builder": {
                "address": "0x1234567890abcdef1234567890abcdef12345678",
                "fee_rate": "0.001"
              }
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Update
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
  - *ref_2
receiveOperations:
  - *ref_3
  - *ref_4
  - *ref_5
sendMessages:
  - *ref_6
  - *ref_7
receiveMessages:
  - *ref_8
  - *ref_9
  - *ref_10
extensions:
  - id: x-parser-unique-object-id
    value: orders
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
