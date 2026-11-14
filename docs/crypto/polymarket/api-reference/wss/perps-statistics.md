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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-statistics'
updated_at: 2026-11-13
---

# Statistics

> Perps WebSocket 24-hour statistics updates.



## AsyncAPI

````yaml asyncapi-perps.json statistics
id: statistics
title: Statistics
description: 24-hour statistics updates. Pushed every 1 second.
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
    id: StatisticsSubscribe
    title: Statistics subscribe
    description: Subscribe to statistics
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: >-
              Subscribe to 24-hour statistics updates for all instruments or a
              specific one
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
                description: >
                  Statistics subscription: `statistics::all` for every active
                  instrument,

                  or `statistics::{iid}` (e.g. `statistics::1`) for a specific
                  one.
                required: true
                properties:
                  - name: item
                    type: string
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-435>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-436>
            chs:
              type: array
              description: >
                Statistics subscription: `statistics::all` for every active
                instrument,

                or `statistics::{iid}` (e.g. `statistics::1`) for a specific
                one.
              items:
                type: string
                pattern: ^statistics::(\d+|all)$
                x-parser-schema-id: <anonymous-schema-438>
              example:
                - statistics::all
              x-parser-schema-id: <anonymous-schema-437>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-434>
        title: Subscribe
        description: >-
          Subscribe to 24-hour statistics updates for all instruments or a
          specific one
        example: |-
          {
            "req": "sub",
            "chs": [
              "statistics::all"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: statistics
  - &ref_3
    id: StatisticsSubscribeResponse
    title: Statistics subscribe response
    description: Statistics subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to statistics subscribe request
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
              x-parser-schema-id: <anonymous-schema-440>
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
                        x-parser-schema-id: <anonymous-schema-444>
                    x-parser-schema-id: <anonymous-schema-443>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-446>
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
                        x-parser-schema-id: <anonymous-schema-447>
                    x-parser-schema-id: <anonymous-schema-445>
                x-parser-schema-id: <anonymous-schema-442>
              x-parser-schema-id: <anonymous-schema-441>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-439>
        title: Subscribe Response
        description: Response to statistics subscribe request
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
    id: StatisticsUnsubscribe
    title: Statistics unsubscribe
    description: Unsubscribe from statistics
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from statistics updates
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
                description: >
                  Statistics subscription: `statistics::all` for every active
                  instrument,

                  or `statistics::{iid}` (e.g. `statistics::1`) for a specific
                  one.
                required: true
                properties:
                  - name: item
                    type: string
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-449>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-450>
            chs:
              type: array
              description: >
                Statistics subscription: `statistics::all` for every active
                instrument,

                or `statistics::{iid}` (e.g. `statistics::1`) for a specific
                one.
              items:
                type: string
                pattern: ^statistics::(\d+|all)$
                x-parser-schema-id: <anonymous-schema-452>
              example:
                - statistics::all
              x-parser-schema-id: <anonymous-schema-451>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-448>
        title: Unsubscribe
        description: Unsubscribe from statistics updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "statistics::all"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: StatisticsUnsubscribeResponse
    title: Statistics unsubscribe response
    description: Statistics unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to statistics unsubscribe request
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
              x-parser-schema-id: <anonymous-schema-454>
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
                        x-parser-schema-id: <anonymous-schema-458>
                    x-parser-schema-id: <anonymous-schema-457>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-460>
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
                        x-parser-schema-id: <anonymous-schema-461>
                    x-parser-schema-id: <anonymous-schema-459>
                x-parser-schema-id: <anonymous-schema-456>
              x-parser-schema-id: <anonymous-schema-455>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-453>
        title: Unsubscribe Response
        description: Response to statistics unsubscribe request
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
    id: StatisticsUpdate
    title: Statistics update
    description: Receive statistics updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: 24-hour statistics for subscribed instruments
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
                description: Array of statistics objects
                required: true
                properties:
                  - name: iid
                    type: integer
                    description: Instrument ID
                    required: true
                  - name: vol
                    type: string
                    description: >-
                      24-hour trading volume in quote-asset notional (sum of
                      price times quantity), as a numeric string
                    required: true
                  - name: open
                    type: string
                    description: >-
                      Opening price of the earliest populated candle in the
                      rolling 24-hour window, whose start is rounded down to the
                      minute. Returns "0" when the window has no candles.
                    required: true
                  - name: klines
                    type: array
                    description: Last 24-hour kline data
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: |
                          - `1767225600000` - Open time
                          - `"100.00"` - Open price
                          - `"105.00"` - High price
                          - `"99.00"` - Low price
                          - `"102.00"` - Close price
                          - `"500.00"` - Volume (base unit)
                          - `42` - Number of trades
                        required: false
        headers: []
        jsonPayloadSchema:
          title: Statistics Update
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
              x-parser-schema-id: <anonymous-schema-463>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-464>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-465>
            data:
              type: object
              description: Array of statistics objects
              properties:
                iid:
                  type: integer
                  description: Instrument ID
                  example: 1
                  x-parser-schema-id: <anonymous-schema-467>
                vol:
                  type: string
                  description: >-
                    24-hour trading volume in quote-asset notional (sum of price
                    times quantity), as a numeric string
                  example: '1000.00'
                  x-parser-schema-id: <anonymous-schema-468>
                open:
                  type: string
                  description: >-
                    Opening price of the earliest populated candle in the
                    rolling 24-hour window, whose start is rounded down to the
                    minute. Returns "0" when the window has no candles.
                  example: '100.50'
                  x-parser-schema-id: <anonymous-schema-469>
                klines:
                  type: array
                  items:
                    type: array
                    description: |
                      - `1767225600000` - Open time
                      - `"100.00"` - Open price
                      - `"105.00"` - High price
                      - `"99.00"` - Low price
                      - `"102.00"` - Close price
                      - `"500.00"` - Volume (base unit)
                      - `42` - Number of trades
                    example:
                      - 1767225600000
                      - '100.00'
                      - '105.00'
                      - '99.00'
                      - '102.00'
                      - '500.00'
                      - 42
                    x-parser-schema-id: <anonymous-schema-471>
                  description: Last 24-hour kline data
                  x-parser-schema-id: <anonymous-schema-470>
              required:
                - iid
                - vol
                - open
                - klines
              x-parser-schema-id: <anonymous-schema-466>
          required:
            - ch
            - ts
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-462>
        title: Update
        description: 24-hour statistics for subscribed instruments
        example: |-
          {
            "ch": "statistics::all",
            "ts": 1767225600000,
            "sq": 1234567890,
            "data": [
              {
                "iid": 1,
                "vol": "1000.00",
                "open": "100.50",
                "klines": [
                  [
                    1767225600000,
                    "100.00",
                    "105.00",
                    "99.00",
                    "102.00",
                    "500.00",
                    42
                  ]
                ]
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
    value: statistics
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
