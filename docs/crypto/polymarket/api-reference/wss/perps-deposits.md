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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-deposits'
updated_at: 2026-11-13
---

# Deposits

> Perps WebSocket private deposit updates.



## AsyncAPI

````yaml asyncapi-perps.json deposits
id: deposits
title: Deposits
description: >-
  Real-time deposit status updates. Requires authentication, see
  [Auth](/ws/auth).
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
    id: DepositsSubscribe
    title: Deposits subscribe
    description: Subscribe to deposits
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: Subscribe to private deposit updates (requires prior auth)
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
                description: 'Deposits private channel: "deposits"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - deposits
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-761>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-762>
            chs:
              type: array
              description: 'Deposits private channel: "deposits"'
              items:
                type: string
                enum:
                  - deposits
                x-parser-schema-id: <anonymous-schema-764>
              example:
                - deposits
              x-parser-schema-id: <anonymous-schema-763>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-760>
        title: Subscribe
        description: Subscribe to private deposit updates (requires prior auth)
        example: |-
          {
            "req": "sub",
            "chs": [
              "deposits"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: deposits
  - &ref_3
    id: DepositsSubscribeResponse
    title: Deposits subscribe response
    description: Deposits subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to deposits subscribe request
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
              x-parser-schema-id: <anonymous-schema-766>
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
                        x-parser-schema-id: <anonymous-schema-770>
                    x-parser-schema-id: <anonymous-schema-769>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-772>
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
                        x-parser-schema-id: <anonymous-schema-773>
                    x-parser-schema-id: <anonymous-schema-771>
                x-parser-schema-id: <anonymous-schema-768>
              x-parser-schema-id: <anonymous-schema-767>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-765>
        title: Subscribe Response
        description: Response to deposits subscribe request
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
    id: DepositsUnsubscribe
    title: Deposits unsubscribe
    description: Unsubscribe from deposits
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from private deposit updates
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
                description: 'Deposits private channel: "deposits"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - deposits
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-775>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-776>
            chs:
              type: array
              description: 'Deposits private channel: "deposits"'
              items:
                type: string
                enum:
                  - deposits
                x-parser-schema-id: <anonymous-schema-778>
              example:
                - deposits
              x-parser-schema-id: <anonymous-schema-777>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-774>
        title: Unsubscribe
        description: Unsubscribe from private deposit updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "deposits"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: DepositsUnsubscribeResponse
    title: Deposits unsubscribe response
    description: Deposits unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to deposits unsubscribe request
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
              x-parser-schema-id: <anonymous-schema-780>
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
                        x-parser-schema-id: <anonymous-schema-784>
                    x-parser-schema-id: <anonymous-schema-783>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-786>
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
                        x-parser-schema-id: <anonymous-schema-787>
                    x-parser-schema-id: <anonymous-schema-785>
                x-parser-schema-id: <anonymous-schema-782>
              x-parser-schema-id: <anonymous-schema-781>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-779>
        title: Unsubscribe Response
        description: Response to deposits unsubscribe request
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
    id: DepositsUpdate
    title: Deposits update
    description: Receive deposit updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: Deposit status updates for authenticated users
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
                description: Array of deposit objects
                required: true
                properties:
                  - name: hash
                    type: string
                    description: On-chain transaction hash, "0x" if not yet mined
                    required: true
                  - name: asset
                    type: string
                    description: Asset name
                    required: true
                  - name: amount
                    type: string
                    description: Token amount in decimal units (e.g. "100" for 100 USDC).
                    required: true
                  - name: status
                    type: string
                    description: Deposit status
                    enumValues:
                      - pending
                      - confirmed
                      - removed
                    required: true
        headers: []
        jsonPayloadSchema:
          title: Deposits Update
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
              x-parser-schema-id: <anonymous-schema-789>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-790>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-791>
            data:
              type: object
              description: Array of deposit objects
              properties:
                hash:
                  type: string
                  description: On-chain transaction hash, "0x" if not yet mined
                  default: 0x
                  example: >-
                    0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
                  x-parser-schema-id: <anonymous-schema-793>
                asset:
                  type: string
                  description: Asset name
                  example: USDC
                  x-parser-schema-id: <anonymous-schema-794>
                amount:
                  type: string
                  description: Token amount in decimal units (e.g. "100" for 100 USDC).
                  example: '100'
                  x-parser-schema-id: <anonymous-schema-795>
                status:
                  type: string
                  description: Deposit status
                  enum:
                    - pending
                    - confirmed
                    - removed
                  x-parser-schema-id: <anonymous-schema-796>
              required:
                - hash
                - asset
                - amount
                - status
              x-parser-schema-id: <anonymous-schema-792>
          required:
            - ch
            - ts
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-788>
        title: Update
        description: Deposit status updates for authenticated users
        example: |-
          {
            "ch": "deposits",
            "ts": 1767225600000,
            "sq": 1234567890,
            "data": [
              {
                "hash": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
                "asset": "USDC",
                "amount": "100000000",
                "status": "pending"
              }
            ]
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
    value: deposits
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
