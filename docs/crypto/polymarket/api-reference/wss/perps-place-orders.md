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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-place-orders'
updated_at: 2026-11-13
---

# Place Orders

> Perps WebSocket order placement.



## AsyncAPI

````yaml asyncapi-perps.json placeOrders
id: placeOrders
title: Create Orders
description: |
  Create new orders.
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
  - &ref_1
    id: PlaceOrdersSend
    title: Place orders send
    description: Submit new orders
    type: receive
    messages:
      - &ref_3
        id: Request
        contentType: application/json
        payload:
          - name: Create Orders Request
            description: Client submits a signed order placement request
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
                      - createOrders
                    required: true
                  - name: args
                    type: object
                    description: Array of orders to create
                    required: true
                    properties:
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
                        required: false
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
                        required: false
                      - name: po
                        type: boolean
                        description: Post only
                        required: false
                      - name: ro
                        type: boolean
                        description: Reduce only
                        required: false
                      - name: c
                        type: string
                        description: Client order ID
                        required: false
                      - name: tr
                        type: object
                        description: Optional trigger attached to this order.
                        required: false
                        properties:
                          - name: market
                            type: boolean
                            description: Whether the trigger executes as a market order
                            required: false
                          - name: trp
                            type: string
                            description: Trigger price
                            required: false
                          - name: tpsl
                            type: string
                            description: Trigger type
                            enumValues:
                              - tp
                              - sl
                            required: false
                      - name: builder
                        type: object
                        description: >-
                          Saved builder terms. Address is the registered Perps
                          account, and fee_rate is an additional fraction of
                          executed notional. Terms survive approval revocation
                          for existing orders.
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
                              points). Zero approval revokes future admission.
                              Never a percentage string.
                            required: true
                  - name: grp
                    type: string
                    description: TPSL grouping
                    enumValues:
                      - order
                      - position
                    required: false
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
              x-parser-schema-id: <anonymous-schema-13>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-14>
            op:
              type: object
              required:
                - type
                - args
              properties:
                type:
                  type: string
                  enum:
                    - createOrders
                  x-parser-schema-id: <anonymous-schema-16>
                args:
                  description: Array of orders to create
                  type: object
                  required:
                    - iid
                    - buy
                    - qty
                  properties:
                    iid:
                      type: integer
                      description: Instrument ID
                      example: 1
                      x-parser-schema-id: <anonymous-schema-18>
                    buy:
                      type: boolean
                      description: Is buy
                      example: true
                      x-parser-schema-id: <anonymous-schema-19>
                    p:
                      type: string
                      description: Price
                      example: '100.00'
                      x-parser-schema-id: <anonymous-schema-20>
                    qty:
                      type: string
                      description: Quantity in no. of contracts
                      example: '10.00'
                      x-parser-schema-id: <anonymous-schema-21>
                    tif:
                      type: string
                      description: Time in force
                      enum:
                        - gtc
                        - ioc
                        - fok
                      x-parser-schema-id: <anonymous-schema-22>
                    po:
                      type: boolean
                      description: Post only
                      default: false
                      example: false
                      x-parser-schema-id: <anonymous-schema-23>
                    ro:
                      type: boolean
                      description: Reduce only
                      example: false
                      default: false
                      x-parser-schema-id: <anonymous-schema-24>
                    c:
                      type: string
                      description: Client order ID
                      minLength: 32
                      maxLength: 32
                      pattern: ^[0-9a-f]{32}$
                      example: 550e8400e29b41d4a716446655440000
                      x-parser-schema-id: <anonymous-schema-25>
                    tr:
                      type: object
                      description: Optional trigger attached to this order.
                      properties:
                        market:
                          type: boolean
                          description: Whether the trigger executes as a market order
                          x-parser-schema-id: <anonymous-schema-27>
                        trp:
                          type: string
                          description: Trigger price
                          example: '110.00'
                          x-parser-schema-id: <anonymous-schema-28>
                        tpsl:
                          type: string
                          description: Trigger type
                          enum:
                            - tp
                            - sl
                          x-parser-schema-id: <anonymous-schema-29>
                      x-parser-schema-id: <anonymous-schema-26>
                    builder:
                      type: object
                      description: >-
                        Saved builder terms. Address is the registered Perps
                        account, and fee_rate is an additional fraction of
                        executed notional. Terms survive approval revocation for
                        existing orders.
                      required:
                        - address
                        - fee_rate
                      properties:
                        address:
                          type: string
                          description: Address
                          example: '0x1234567890abcdef1234567890abcdef12345678'
                          x-parser-schema-id: <anonymous-schema-31>
                        fee_rate:
                          type: string
                          description: >-
                            Additional builder fee as a decimal fraction of
                            executed notional, from 0 through 0.001 (10 basis
                            points). Zero approval revokes future admission.
                            Never a percentage string.
                          example: '0.001'
                          x-parser-schema-id: <anonymous-schema-32>
                      x-parser-schema-id: <anonymous-schema-30>
                  x-parser-schema-id: <anonymous-schema-17>
                grp:
                  type: string
                  description: TPSL grouping
                  enum:
                    - order
                    - position
                  x-parser-schema-id: <anonymous-schema-33>
              x-parser-schema-id: <anonymous-schema-15>
            sig:
              type: string
              description: Signature in hex format
              example: 0x1234567890...
              x-parser-schema-id: <anonymous-schema-34>
            salt:
              type: integer
              description: Salt
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-35>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-36>
            exp:
              type: integer
              description: >-
                Command-processing deadline in Unix milliseconds, not an order
                auto-cancel time; the server caps it at now + 5 s, clamps larger
                values to that cap, and uses that 5 s default when omitted.
                Values at or before the server's clock are rejected with HTTP
                400 (command expired).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-37>
          required:
            - req
            - op
            - sig
            - salt
            - ts
          x-parser-schema-id: <anonymous-schema-12>
        title: Create Orders Request
        description: Client submits a signed order placement request
        example: |-
          {
            "req": "post",
            "op": {
              "type": "createOrders",
              "args": [
                {
                  "iid": 1,
                  "buy": true,
                  "p": "100.00",
                  "qty": "10.00",
                  "tif": "gtc",
                  "po": false,
                  "ro": false,
                  "c": "550e8400e29b41d4a716446655440000",
                  "tr": {
                    "trp": "110.00",
                    "tpsl": "tp"
                  },
                  "builder": {
                    "address": "0x1234567890abcdef1234567890abcdef12345678",
                    "fee_rate": "0.001"
                  }
                }
              ],
              "grp": "order"
            },
            "sig": "0x1234567890...",
            "salt": 1234567890,
            "ts": 1767225600000,
            "exp": 1767225600000
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Request
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: placeOrders
  - &ref_2
    id: PlaceOrdersReceive
    title: Place orders receive
    description: Order ACK response
    type: send
    messages:
      - &ref_4
        id: Response
        contentType: application/json
        payload:
          - name: Create Orders Response
            description: Server responds with order ACK for each submitted order
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: array
                description: Array of order results
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
                      - name: oid
                        type: integer
                        description: Order ID
                        required: true
                      - name: coid
                        type: string
                        description: Client order ID
                        required: false
                      - name: ts
                        type: integer
                        description: >-
                          Sequenced order decision timestamp in Unix
                          milliseconds.
                        required: true
                      - name: arts
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        required: false
                      - name: builder
                        type: object
                        description: >-
                          Saved builder terms. Address is the registered Perps
                          account, and fee_rate is an additional fraction of
                          executed notional. Terms survive approval revocation
                          for existing orders.
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
                              points). Zero approval revokes future admission.
                              Never a percentage string.
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
                          `account_liquidating`, `unauthorized`, `not_found`.
                          For `400` it is a human-readable validation detail
                          whose wording may change. See the Error handling guide
                          for the domain identifiers. (Post-only / Fill-or-Kill
                          outcomes are order statuses such as
                          `post_only_rejected`, not rejections.)
                        required: true
                      - name: oid
                        type: integer
                        description: Order ID
                        required: false
                      - name: coid
                        type: string
                        description: Client order ID
                        required: false
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
              x-parser-schema-id: <anonymous-schema-39>
            data:
              type: array
              description: Array of order results
              items:
                oneOf:
                  - type: object
                    required:
                      - status
                      - oid
                      - ts
                    properties:
                      status:
                        type: string
                        enum:
                          - ok
                        x-parser-schema-id: <anonymous-schema-43>
                      oid:
                        type: integer
                        description: Order ID
                        example: 1234567890
                        x-parser-schema-id: <anonymous-schema-44>
                      coid:
                        type: string
                        description: Client order ID
                        minLength: 32
                        maxLength: 32
                        pattern: ^[0-9a-f]{32}$
                        example: 550e8400e29b41d4a716446655440000
                        x-parser-schema-id: <anonymous-schema-45>
                      ts:
                        description: >-
                          Sequenced order decision timestamp in Unix
                          milliseconds.
                        type: integer
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-46>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-47>
                      builder:
                        type: object
                        description: >-
                          Saved builder terms. Address is the registered Perps
                          account, and fee_rate is an additional fraction of
                          executed notional. Terms survive approval revocation
                          for existing orders.
                        required:
                          - address
                          - fee_rate
                        properties:
                          address:
                            type: string
                            description: Address
                            example: '0x1234567890abcdef1234567890abcdef12345678'
                            x-parser-schema-id: <anonymous-schema-49>
                          fee_rate:
                            type: string
                            description: >-
                              Additional builder fee as a decimal fraction of
                              executed notional, from 0 through 0.001 (10 basis
                              points). Zero approval revokes future admission.
                              Never a percentage string.
                            example: '0.001'
                            x-parser-schema-id: <anonymous-schema-50>
                        x-parser-schema-id: <anonymous-schema-48>
                    x-parser-schema-id: <anonymous-schema-42>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-52>
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
                          `account_liquidating`, `unauthorized`, `not_found`.
                          For `400` it is a human-readable validation detail
                          whose wording may change. See the Error handling guide
                          for the domain identifiers. (Post-only / Fill-or-Kill
                          outcomes are order statuses such as
                          `post_only_rejected`, not rejections.)
                        example: insufficient_margin
                        x-parser-schema-id: <anonymous-schema-53>
                      oid:
                        type: integer
                        description: Order ID
                        example: 1234567890
                        x-parser-schema-id: <anonymous-schema-54>
                      coid:
                        type: string
                        description: Client order ID
                        minLength: 32
                        maxLength: 32
                        pattern: ^[0-9a-f]{32}$
                        example: 550e8400e29b41d4a716446655440000
                        x-parser-schema-id: <anonymous-schema-55>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-56>
                      ts:
                        description: Server rejection timestamp in Unix milliseconds.
                        type: integer
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-57>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-58>
                    x-parser-schema-id: <anonymous-schema-51>
                x-parser-schema-id: <anonymous-schema-41>
              x-parser-schema-id: <anonymous-schema-40>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-38>
        title: Create Orders Response
        description: Server responds with order ACK for each submitted order
        example: |-
          {
            "id": 1,
            "data": [
              {
                "status": "ok",
                "oid": 1234567890
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Response
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
    value: placeOrders
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
