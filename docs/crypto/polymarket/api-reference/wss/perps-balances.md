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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-balances'
updated_at: 2026-11-13
---

# Balances

> Perps WebSocket private balance updates.



## AsyncAPI

````yaml asyncapi-perps.json balances
id: balances
title: Balances
description: >-
  Real-time balance updates. Pushed every 5 seconds. Requires authentication,
  see [Auth](/ws/auth).
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
    id: BalancesSubscribe
    title: Balances subscribe
    description: Subscribe to balances
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: Subscribe to private balance updates (requires prior auth)
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
                description: 'Balances private channel: "balances"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - balances
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-666>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-667>
            chs:
              type: array
              description: 'Balances private channel: "balances"'
              items:
                type: string
                enum:
                  - balances
                x-parser-schema-id: <anonymous-schema-669>
              example:
                - balances
              x-parser-schema-id: <anonymous-schema-668>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-665>
        title: Subscribe
        description: Subscribe to private balance updates (requires prior auth)
        example: |-
          {
            "req": "sub",
            "chs": [
              "balances"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: balances
  - &ref_3
    id: BalancesSubscribeResponse
    title: Balances subscribe response
    description: Balances subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to balances subscribe request
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
              x-parser-schema-id: <anonymous-schema-671>
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
                        x-parser-schema-id: <anonymous-schema-675>
                    x-parser-schema-id: <anonymous-schema-674>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-677>
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
                        x-parser-schema-id: <anonymous-schema-678>
                    x-parser-schema-id: <anonymous-schema-676>
                x-parser-schema-id: <anonymous-schema-673>
              x-parser-schema-id: <anonymous-schema-672>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-670>
        title: Subscribe Response
        description: Response to balances subscribe request
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
    id: BalancesUnsubscribe
    title: Balances unsubscribe
    description: Unsubscribe from balances
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from private balance updates
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
                description: 'Balances private channel: "balances"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - balances
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-680>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-681>
            chs:
              type: array
              description: 'Balances private channel: "balances"'
              items:
                type: string
                enum:
                  - balances
                x-parser-schema-id: <anonymous-schema-683>
              example:
                - balances
              x-parser-schema-id: <anonymous-schema-682>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-679>
        title: Unsubscribe
        description: Unsubscribe from private balance updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "balances"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: BalancesUnsubscribeResponse
    title: Balances unsubscribe response
    description: Balances unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to balances unsubscribe request
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
              x-parser-schema-id: <anonymous-schema-685>
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
                        x-parser-schema-id: <anonymous-schema-689>
                    x-parser-schema-id: <anonymous-schema-688>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-691>
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
                        x-parser-schema-id: <anonymous-schema-692>
                    x-parser-schema-id: <anonymous-schema-690>
                x-parser-schema-id: <anonymous-schema-687>
              x-parser-schema-id: <anonymous-schema-686>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-684>
        title: Unsubscribe Response
        description: Response to balances unsubscribe request
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
    id: BalancesUpdate
    title: Balances update
    description: Receive balance updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: Balance updates pushed every 5 seconds
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
                description: Balance object
                required: true
                properties:
                  - name: asset
                    type: string
                    description: Asset name
                    required: true
                  - name: balance
                    type: string
                    description: Total balance
                    required: true
                  - name: value
                    type: string
                    description: USD value
                    required: true
        headers: []
        jsonPayloadSchema:
          title: Balances Update
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
              x-parser-schema-id: <anonymous-schema-694>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-695>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-696>
            data:
              type: object
              description: Balance object
              properties:
                asset:
                  type: string
                  description: Asset name
                  example: USDC
                  x-parser-schema-id: <anonymous-schema-698>
                balance:
                  type: string
                  description: Total balance
                  example: '10000.00'
                  x-parser-schema-id: <anonymous-schema-699>
                value:
                  type: string
                  description: USD value
                  example: '10000.00'
                  x-parser-schema-id: <anonymous-schema-700>
              required:
                - asset
                - balance
                - value
              x-parser-schema-id: <anonymous-schema-697>
          required:
            - ch
            - ts
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-693>
        title: Update
        description: Balance updates pushed every 5 seconds
        example: |-
          {
            "ch": "balances",
            "ts": 1767225600000,
            "sq": 1234567890,
            "data": {
              "asset": "USDC",
              "balance": "10000.00",
              "value": "10000.00"
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
    value: balances
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
