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
source_url: 'https://docs.polymarket.com/cn/api-reference/wss/perps-modify-orders'
updated_at: 2026-11-13
---

# 修改订单

> 通过永续合约 WebSocket 按订单 ID 修改订单。



## AsyncAPI

````yaml asyncapi-perps.json modifyOrders
id: modifyOrders
title: Modify Orders
description: |
  Modify existing orders by exchange order ID. Only price and total quantity
  are mutable.
  Requires proxy signature, see [proxy signing](/http/signing#2-proxy-signing).

  <Badge color="gray" size="md">Action Weight: **1 / order**</Badge>
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
  - &ref_2
    id: ModifyOrdersReceive
    title: Modify orders receive
    description: Modify order response
    type: send
    messages:
      - &ref_4
        id: Response
        contentType: application/json
        payload:
          - name: Modify Orders Response
            description: Server responds with modify result for each order
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: array
                description: >
                  Array of modify results. A request-level failure is returned
                  as

                  a single rejected item.
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
                      - name: order
                        type: object
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
                              Order status, such as `open` for a resting order.
                              See [Handle Terminal Order
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
                              Saved builder terms. Address is the registered
                              Perps account, and fee_rate is an additional
                              fraction of executed notional. Terms survive
                              approval revocation for existing orders.
                            required: false
                            properties:
                              - name: address
                                type: string
                                description: Address
                                required: true
                              - name: fee_rate
                                type: string
                                description: >-
                                  Additional builder fee as a decimal fraction
                                  of executed notional, from 0 through 0.001 (10
                                  basis points). Zero approval revokes future
                                  admission. Never a percentage string.
                                required: true
                      - name: status
                        type: string
                        enumValues:
                          - err
                        required: true
                      - name: oid
                        type: integer
                        description: Order ID
                        required: false
                      - name: coid
                        type: string
                        description: Client order ID
                        required: false
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
                      - name: arts
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        required: false
                      - name: ts
                        type: integer
                        description: Server rejection timestamp in Unix milliseconds.
                        required: false
                      - name: ref
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Response
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-957>
            data:
              type: array
              description: |
                Array of modify results. A request-level failure is returned as
                a single rejected item.
              items:
                oneOf:
                  - type: object
                    required:
                      - status
                      - order
                    properties:
                      status:
                        type: string
                        enum:
                          - ok
                        x-parser-schema-id: <anonymous-schema-961>
                      order:
                        type: object
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
                        properties:
                          oid:
                            type: integer
                            description: Order ID
                            example: 1234567890
                            x-parser-schema-id: <anonymous-schema-963>
                          iid:
                            type: integer
                            description: Instrument ID
                            example: 1
                            x-parser-schema-id: <anonymous-schema-964>
                          buy:
                            type: boolean
                            description: Is buy
                            example: true
                            x-parser-schema-id: <anonymous-schema-965>
                          p:
                            type: string
                            description: Price
                            example: '100.00'
                            x-parser-schema-id: <anonymous-schema-966>
                          qty:
                            type: string
                            description: Quantity in no. of contracts
                            example: '10.00'
                            x-parser-schema-id: <anonymous-schema-967>
                          tif:
                            type: string
                            description: Time in force
                            enum:
                              - gtc
                              - ioc
                              - fok
                            x-parser-schema-id: <anonymous-schema-968>
                          po:
                            type: boolean
                            description: Post only
                            default: false
                            example: false
                            x-parser-schema-id: <anonymous-schema-969>
                          ro:
                            type: boolean
                            description: Reduce only
                            example: false
                            default: false
                            x-parser-schema-id: <anonymous-schema-970>
                          rest:
                            type: string
                            description: Resting quantity
                            example: '9.00'
                            x-parser-schema-id: <anonymous-schema-971>
                          fill:
                            type: string
                            description: Filled quantity
                            example: '1.00'
                            x-parser-schema-id: <anonymous-schema-972>
                          cts:
                            type: integer
                            description: Create timestamp in milliseconds
                            example: 1767225600000
                            x-parser-schema-id: <anonymous-schema-973>
                          uts:
                            type: integer
                            description: Update timestamp in milliseconds
                            example: 1767225600000
                            x-parser-schema-id: <anonymous-schema-974>
                          status:
                            type: string
                            description: >-
                              Order status, such as `open` for a resting order.
                              See [Handle Terminal Order
                              Outcomes](/perps/trading#handle-terminal-order-outcomes)
                              for the statuses that end an order.
                            example: open
                            x-parser-schema-id: <anonymous-schema-975>
                          coid:
                            type: string
                            description: Client order ID
                            minLength: 32
                            maxLength: 32
                            pattern: ^[0-9a-f]{32}$
                            example: 550e8400e29b41d4a716446655440000
                            x-parser-schema-id: <anonymous-schema-976>
                          builder:
                            type: object
                            description: >-
                              Saved builder terms. Address is the registered
                              Perps account, and fee_rate is an additional
                              fraction of executed notional. Terms survive
                              approval revocation for existing orders.
                            required:
                              - address
                              - fee_rate
                            properties:
                              address:
                                type: string
                                description: Address
                                example: '0x1234567890abcdef1234567890abcdef12345678'
                                x-parser-schema-id: <anonymous-schema-978>
                              fee_rate:
                                type: string
                                description: >-
                                  Additional builder fee as a decimal fraction
                                  of executed notional, from 0 through 0.001 (10
                                  basis points). Zero approval revokes future
                                  admission. Never a percentage string.
                                example: '0.001'
                                x-parser-schema-id: <anonymous-schema-979>
                            x-parser-schema-id: <anonymous-schema-977>
                        x-parser-schema-id: <anonymous-schema-962>
                    x-parser-schema-id: <anonymous-schema-960>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-981>
                      oid:
                        type: integer
                        description: Order ID
                        example: 1234567890
                        x-parser-schema-id: <anonymous-schema-982>
                      coid:
                        type: string
                        description: Client order ID
                        minLength: 32
                        maxLength: 32
                        pattern: ^[0-9a-f]{32}$
                        example: 550e8400e29b41d4a716446655440000
                        x-parser-schema-id: <anonymous-schema-983>
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
                        x-parser-schema-id: <anonymous-schema-984>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-985>
                      ts:
                        description: Server rejection timestamp in Unix milliseconds.
                        type: integer
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-986>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-987>
                    x-parser-schema-id: <anonymous-schema-980>
                x-parser-schema-id: <anonymous-schema-959>
              x-parser-schema-id: <anonymous-schema-958>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-956>
        title: Modify Orders Response
        description: Server responds with modify result for each order
        example: |-
          {
            "id": 2,
            "data": [
              {
                "status": "ok",
                "order": {
                  "oid": 1234567890,
                  "iid": 1,
                  "buy": true,
                  "p": "100.25",
                  "qty": "8",
                  "tif": "gtc",
                  "po": false,
                  "ro": false,
                  "rest": "8",
                  "fill": "0",
                  "status": "open",
                  "cts": 1767225600000,
                  "uts": 1767225601000
                }
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Response
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: modifyOrders
  - &ref_1
    id: ModifyOrdersSend
    title: Modify orders send
    description: Modify existing orders
    type: receive
    messages:
      - &ref_3
        id: Request
        contentType: application/json
        payload:
          - name: Modify Orders Request
            description: Client submits a signed order modification request
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
              - name: op
                type: object
                required: true
                properties:
                  - name: type
                    type: string
                    enumValues:
                      - modifyOrders
                    required: true
                  - name: args
                    type: array
                    description: Array of orders to modify
                    required: true
                    properties:
                      - name: oid
                        type: integer
                        description: Order ID
                        required: true
                      - name: p
                        type: string
                        description: Price
                        required: true
                      - name: qty
                        type: string
                        description: Quantity in no. of contracts
                        required: true
              - name: sig
                type: string
                description: Signature in hex format
                required: true
              - name: salt
                type: integer
                description: Salt
                required: true
              - name: ts
                type: integer
                description: >-
                  Request timestamp. Unix milliseconds for most operations; Unix
                  seconds for withdrawals (must match the on-chain EIP-712
                  struct verified against block.timestamp).
                required: true
              - name: exp
                type: integer
                description: >-
                  Command-processing deadline in Unix milliseconds, not an order
                  auto-cancel time; the server caps it at now + 5 s, clamps
                  larger values to that cap, and uses that 5 s default when
                  omitted. Values at or before the server's clock are rejected
                  with HTTP 400 (command expired).
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-943>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-944>
            op:
              type: object
              required:
                - type
                - args
              properties:
                type:
                  type: string
                  enum:
                    - modifyOrders
                  x-parser-schema-id: <anonymous-schema-946>
                args:
                  type: array
                  minItems: 1
                  description: Array of orders to modify
                  items:
                    type: object
                    additionalProperties: false
                    required:
                      - oid
                      - p
                      - qty
                    properties:
                      oid:
                        type: integer
                        description: Order ID
                        example: 1234567890
                        x-parser-schema-id: <anonymous-schema-949>
                      p:
                        type: string
                        description: Price
                        example: '100.00'
                        x-parser-schema-id: <anonymous-schema-950>
                      qty:
                        type: string
                        description: Quantity in no. of contracts
                        example: '10.00'
                        x-parser-schema-id: <anonymous-schema-951>
                    x-parser-schema-id: <anonymous-schema-948>
                  x-parser-schema-id: <anonymous-schema-947>
              x-parser-schema-id: <anonymous-schema-945>
            sig:
              type: string
              description: Signature in hex format
              example: 0x1234567890...
              x-parser-schema-id: <anonymous-schema-952>
            salt:
              type: integer
              description: Salt
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-953>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-954>
            exp:
              type: integer
              description: >-
                Command-processing deadline in Unix milliseconds, not an order
                auto-cancel time; the server caps it at now + 5 s, clamps larger
                values to that cap, and uses that 5 s default when omitted.
                Values at or before the server's clock are rejected with HTTP
                400 (command expired).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-955>
          required:
            - req
            - op
            - sig
            - salt
            - ts
          x-parser-schema-id: <anonymous-schema-942>
        title: Modify Orders Request
        description: Client submits a signed order modification request
        example: |-
          {
            "id": 2,
            "req": "post",
            "op": {
              "type": "modifyOrders",
              "args": [
                {
                  "oid": 1234567890,
                  "p": "100.25",
                  "qty": "8"
                }
              ]
            },
            "sig": "0x1234567890...",
            "salt": 1234567890,
            "ts": 1767225600000,
            "exp": 1767225660000
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Request
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
receiveOperations:
  - *ref_2
sendMessages:
  - *ref_3
receiveMessages:
  - *ref_4
extensions:
  - id: x-parser-unique-object-id
    value: modifyOrders
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
