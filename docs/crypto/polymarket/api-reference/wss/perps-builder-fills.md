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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-builder-fills'
updated_at: 2026-11-13
---

# Builder Fills

> Live attributed fills for an authenticated Perps builder.



## AsyncAPI

````yaml asyncapi-perps.json builderFills
id: builderFills
title: BuilderFills
description: >-
  Real-time attributed fills for the authenticated builder account. Requires
  prior authentication.
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
    id: BuilderFillsSubscribe
    title: Builder fills subscribe
    description: Subscribe to fills
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: >-
              Subscribe to attributed fill updates for the authenticated builder
              (requires prior auth)
            type: object
            properties:
              - name: id
                type: integer
                description: Client-supplied identifier used to correlate the response.
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
                description: 'BuilderFills private channel: "builderFills"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - builderFills
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              description: Client-supplied identifier used to correlate the response.
              type: integer
              x-parser-schema-id: <anonymous-schema-1035>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-1036>
            chs:
              type: array
              description: 'BuilderFills private channel: "builderFills"'
              items:
                type: string
                enum:
                  - builderFills
                x-parser-schema-id: <anonymous-schema-1038>
              example:
                - builderFills
              x-parser-schema-id: <anonymous-schema-1037>
          required:
            - req
            - chs
          description: >
            Each inbound request consumes a weighted WebSocket message token.
            Before

            authentication the budget is per client IP. After authentication all
            of

            the account's sockets share its tier budget across IPs. The first
            valid

            signed write also binds an unauthenticated socket to its recovered
            account.

            Later signed writes must resolve that same account. A breach returns

            `message_rate_limited` and leaves the socket open.


            Signed write posts carrying an `id` are dispatched concurrently (up
            to 16

            in flight per connection) and may execute and respond out of request

            order, matching the semantics of concurrent HTTP requests. Ordering
            is

            kept per connection for posts that name the same client order id or

            order id, and `cancelAll`, leverage and margin updates wait for
            every

            earlier post on the connection while later posts wait for them.
            Posts

            without an `id` are dispatched one at a time but are not ordered
            after

            earlier `id`-carrying posts still in flight. For strict ordering,
            await

            each response before sending the next request, or omit `id` on every

            post. Use a unique `id` for every in-flight request on a connection.

            Uniqueness is not enforced and duplicate in-flight IDs are
            ambiguous.
          x-parser-schema-id: <anonymous-schema-1034>
        title: Subscribe
        description: >-
          Subscribe to attributed fill updates for the authenticated builder
          (requires prior auth)
        example: |-
          {
            "req": "sub",
            "chs": [
              "builderFills"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: builderFills
  - &ref_3
    id: BuilderFillsSubscribeResponse
    title: Builder fills subscribe response
    description: BuilderFills subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to fills subscribe request
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
                          `account_liquidating`, `unauthorized`, `not_found`.
                          For `400` it is a human-readable validation detail
                          whose wording may change. See the Error handling guide
                          for the domain identifiers. (Post-only / Fill-or-Kill
                          outcomes are order statuses such as
                          `post_only_rejected`, not rejections.)
                        required: true
                      - name: arts
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        required: false
                      - name: ts
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
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
              x-parser-schema-id: <anonymous-schema-1040>
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
                        x-parser-schema-id: <anonymous-schema-1044>
                    x-parser-schema-id: <anonymous-schema-1043>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-1046>
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
                        x-parser-schema-id: <anonymous-schema-1047>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1048>
                      ts:
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1049>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-1050>
                    x-parser-schema-id: <anonymous-schema-1045>
                x-parser-schema-id: <anonymous-schema-1042>
              x-parser-schema-id: <anonymous-schema-1041>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-1039>
        title: Subscribe Response
        description: Response to fills subscribe request
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
    id: BuilderFillsUnsubscribe
    title: Builder fills unsubscribe
    description: Unsubscribe from fills
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: >-
              Unsubscribe from attributed fill updates for the authenticated
              builder
            type: object
            properties:
              - name: id
                type: integer
                description: Client-supplied identifier used to correlate the response.
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
                description: 'BuilderFills private channel: "builderFills"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - builderFills
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              description: Client-supplied identifier used to correlate the response.
              type: integer
              x-parser-schema-id: <anonymous-schema-1052>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-1053>
            chs:
              type: array
              description: 'BuilderFills private channel: "builderFills"'
              items:
                type: string
                enum:
                  - builderFills
                x-parser-schema-id: <anonymous-schema-1055>
              example:
                - builderFills
              x-parser-schema-id: <anonymous-schema-1054>
          required:
            - req
            - chs
          description: >
            Each inbound request consumes a weighted WebSocket message token.
            Before

            authentication the budget is per client IP. After authentication all
            of

            the account's sockets share its tier budget across IPs. The first
            valid

            signed write also binds an unauthenticated socket to its recovered
            account.

            Later signed writes must resolve that same account. A breach returns

            `message_rate_limited` and leaves the socket open.


            Signed write posts carrying an `id` are dispatched concurrently (up
            to 16

            in flight per connection) and may execute and respond out of request

            order, matching the semantics of concurrent HTTP requests. Ordering
            is

            kept per connection for posts that name the same client order id or

            order id, and `cancelAll`, leverage and margin updates wait for
            every

            earlier post on the connection while later posts wait for them.
            Posts

            without an `id` are dispatched one at a time but are not ordered
            after

            earlier `id`-carrying posts still in flight. For strict ordering,
            await

            each response before sending the next request, or omit `id` on every

            post. Use a unique `id` for every in-flight request on a connection.

            Uniqueness is not enforced and duplicate in-flight IDs are
            ambiguous.
          x-parser-schema-id: <anonymous-schema-1051>
        title: Unsubscribe
        description: Unsubscribe from attributed fill updates for the authenticated builder
        example: |-
          {
            "req": "unsub",
            "chs": [
              "builderFills"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: BuilderFillsUnsubscribeResponse
    title: Builder fills unsubscribe response
    description: BuilderFills unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to fills unsubscribe request
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
                          `account_liquidating`, `unauthorized`, `not_found`.
                          For `400` it is a human-readable validation detail
                          whose wording may change. See the Error handling guide
                          for the domain identifiers. (Post-only / Fill-or-Kill
                          outcomes are order statuses such as
                          `post_only_rejected`, not rejections.)
                        required: true
                      - name: arts
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        required: false
                      - name: ts
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
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
              x-parser-schema-id: <anonymous-schema-1057>
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
                        x-parser-schema-id: <anonymous-schema-1061>
                    x-parser-schema-id: <anonymous-schema-1060>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-1063>
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
                        x-parser-schema-id: <anonymous-schema-1064>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1065>
                      ts:
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1066>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-1067>
                    x-parser-schema-id: <anonymous-schema-1062>
                x-parser-schema-id: <anonymous-schema-1059>
              x-parser-schema-id: <anonymous-schema-1058>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-1056>
        title: Unsubscribe Response
        description: Response to fills unsubscribe request
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
    id: BuilderFillsUpdate
    title: Builder fills update
    description: Receive fill updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: Real-time fill updates for authenticated users
            type: object
            properties:
              - name: ch
                type: string
                description: >-
                  Channel name for push data. Parameterized channels include the
                  instrument ID (e.g. "trades::1", "book::1", "klines::1::1m",
                  "tickers::all"). Private channels use plain names (e.g.
                  "fills", "orders").
                required: true
              - name: ts
                type: integer
                description: Server send time, Unix milliseconds
                required: true
              - name: ets
                type: integer
                description: >-
                  Timestamp of the newest event this update reflects, in Unix
                  milliseconds. Distinct from `ts`, which is the server send
                  time. `ts - ets` is time spent inside the exchange after the
                  event. `ets=0` means no event horizon is attested, and
                  consumers must treat the horizon as unknown.
                required: true
              - name: sq
                type: integer
                description: Sequence number
                required: true
              - name: data
                type: array
                required: true
                properties:
                  - name: earning_id
                    type: string
                    description: >-
                      Stable side-specific receipt identity, unique for this
                      builder. Use this to deduplicate, not sequence or trade_id
                      alone.
                    required: true
                  - name: trade_id
                    type: integer
                    description: Trade ID
                    required: true
                  - name: order_id
                    type: integer
                    description: Order ID
                    required: true
                  - name: instrument_id
                    type: integer
                    description: Instrument ID
                    required: true
                  - name: trader
                    type: string
                    description: >-
                      Main address of the attributed trading account, not its
                      signing proxy or the counterparty.
                    required: true
                  - name: buy
                    type: boolean
                    description: Is buy
                    required: true
                  - name: price
                    type: string
                    description: Price
                    required: true
                  - name: quantity
                    type: string
                    description: Quantity in number of contracts
                    required: true
                  - name: client_order_id
                    type: string
                    description: >-
                      Included only when the attributed order supplied a
                      client_order_id.
                    required: false
                  - name: side
                    type: string
                    enumValues:
                      - maker
                      - taker
                    required: true
                  - name: timestamp
                    type: integer
                    description: >-
                      decision time in Unix milliseconds: terminal event time
                      for event-backed outcomes, gateway decision time otherwise
                    required: true
                  - name: sequence
                    type: integer
                    required: true
                  - name: notional
                    type: string
                    required: true
                  - name: fee_asset
                    type: string
                    description: Fee asset name
                    required: true
                  - name: fee
                    type: string
                    description: >-
                      Signed exchange fee for this trade side, excluding
                      builder_fee. Negative values are rebates
                    required: true
                  - name: builder_fee
                    type: string
                    description: >-
                      Actual additional builder fee in the same asset as fee,
                      floored independently for each execution to that asset's
                      token decimals (six for pUSD), with discarded dust and no
                      carry. The fee is non-negative and is zero for older or
                      untagged fills and excluded forced liquidation legs.
                    required: true
                  - name: total_fee
                    type: string
                    description: >-
                      Exact signed sum of exchange fee and builder_fee in the
                      same asset. May be negative when exchange rebates exceed
                      the builder charge.
                    required: true
                  - name: fee_rate
                    type: string
                    description: >-
                      Additional builder fee as a decimal fraction of executed
                      notional, from 0 through 0.001 (10 basis points). Zero
                      approval revokes future admission. Never a percentage
                      string.
                    required: true
        headers: []
        jsonPayloadSchema:
          title: Builder Fills Update
          description: >-
            Attributed fill sides for the authenticated builder, including zero
            builder fees. Each receipt uses the same fields and earning_id as
            GET /v1/account/builder-earnings. The trader is the main account
            wallet, never a delegated trading key. There is no initial history
            snapshot and delivery is not exactly once. After reconnecting,
            subscribe first, buffer live receipts, then page REST history over
            an overlapping time window. History can lag the live feed. Use its
            complete as_of_sequence cutoff, repeat recovery until indexing
            catches up, and deduplicate by earning_id.
          type: object
          properties:
            ch:
              type: string
              description: >-
                Channel name for push data. Parameterized channels include the
                instrument ID (e.g. "trades::1", "book::1", "klines::1::1m",
                "tickers::all"). Private channels use plain names (e.g. "fills",
                "orders").
              example: builderFills
              x-parser-schema-id: <anonymous-schema-1069>
            ts:
              description: Server send time, Unix milliseconds
              type: integer
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-1070>
            ets:
              type: integer
              description: >-
                Timestamp of the newest event this update reflects, in Unix
                milliseconds. Distinct from `ts`, which is the server send time.
                `ts - ets` is time spent inside the exchange after the event.
                `ets=0` means no event horizon is attested, and consumers must
                treat the horizon as unknown.
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-1071>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-1072>
            data:
              type: array
              items:
                type: object
                required:
                  - earning_id
                  - trade_id
                  - order_id
                  - instrument_id
                  - trader
                  - buy
                  - price
                  - quantity
                  - side
                  - timestamp
                  - sequence
                  - notional
                  - fee_asset
                  - fee
                  - builder_fee
                  - total_fee
                  - fee_rate
                properties:
                  earning_id:
                    type: string
                    description: >-
                      Stable side-specific receipt identity, unique for this
                      builder. Use this to deduplicate, not sequence or trade_id
                      alone.
                    x-parser-schema-id: <anonymous-schema-1075>
                  trade_id:
                    type: integer
                    description: Trade ID
                    example: 1
                    x-parser-schema-id: <anonymous-schema-1076>
                  order_id:
                    type: integer
                    description: Order ID
                    example: 1234567890
                    x-parser-schema-id: <anonymous-schema-1077>
                  instrument_id:
                    type: integer
                    description: Instrument ID
                    example: 1
                    x-parser-schema-id: <anonymous-schema-1078>
                  trader:
                    description: >-
                      Main address of the attributed trading account, not its
                      signing proxy or the counterparty.
                    type: string
                    example: '0x1234567890abcdef1234567890abcdef12345678'
                    x-parser-schema-id: <anonymous-schema-1079>
                  buy:
                    type: boolean
                    description: Is buy
                    example: true
                    x-parser-schema-id: <anonymous-schema-1080>
                  price:
                    type: string
                    description: Price
                    example: '100.00'
                    x-parser-schema-id: <anonymous-schema-1081>
                  quantity:
                    type: string
                    description: Quantity in number of contracts
                    example: '10.00'
                    x-parser-schema-id: <anonymous-schema-1082>
                  client_order_id:
                    description: >-
                      Included only when the attributed order supplied a
                      client_order_id.
                    type: string
                    minLength: 32
                    maxLength: 32
                    pattern: ^[0-9a-f]{32}$
                    example: 550e8400e29b41d4a716446655440000
                    x-parser-schema-id: <anonymous-schema-1083>
                  side:
                    type: string
                    enum:
                      - maker
                      - taker
                    x-parser-schema-id: <anonymous-schema-1084>
                  timestamp:
                    type: integer
                    description: >-
                      decision time in Unix milliseconds: terminal event time
                      for event-backed outcomes, gateway decision time otherwise
                    example: 1767225600000
                    x-parser-schema-id: <anonymous-schema-1085>
                  sequence:
                    type: integer
                    x-parser-schema-id: <anonymous-schema-1086>
                  notional:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1087>
                  fee_asset:
                    type: string
                    description: Fee asset name
                    example: pUSD
                    x-parser-schema-id: <anonymous-schema-1088>
                  fee:
                    type: string
                    description: >-
                      Signed exchange fee for this trade side, excluding
                      builder_fee. Negative values are rebates
                    example: '0.125'
                    x-parser-schema-id: <anonymous-schema-1089>
                  builder_fee:
                    type: string
                    description: >-
                      Actual additional builder fee in the same asset as fee,
                      floored independently for each execution to that asset's
                      token decimals (six for pUSD), with discarded dust and no
                      carry. The fee is non-negative and is zero for older or
                      untagged fills and excluded forced liquidation legs.
                    example: '1.00'
                    x-parser-schema-id: <anonymous-schema-1090>
                  total_fee:
                    type: string
                    description: >-
                      Exact signed sum of exchange fee and builder_fee in the
                      same asset. May be negative when exchange rebates exceed
                      the builder charge.
                    example: '1.125'
                    x-parser-schema-id: <anonymous-schema-1091>
                  fee_rate:
                    type: string
                    description: >-
                      Additional builder fee as a decimal fraction of executed
                      notional, from 0 through 0.001 (10 basis points). Zero
                      approval revokes future admission. Never a percentage
                      string.
                    example: '0.001'
                    x-parser-schema-id: <anonymous-schema-1092>
                x-parser-schema-id: <anonymous-schema-1074>
              x-parser-schema-id: <anonymous-schema-1073>
          required:
            - ch
            - ts
            - ets
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-1068>
        title: Update
        description: Real-time fill updates for authenticated users
        example: |-
          {
            "ch": "builderFills",
            "ts": 1767225600000,
            "ets": 1767225600000,
            "sq": 1234567890,
            "data": [
              {
                "earning_id": "1:1:0",
                "trade_id": 1,
                "order_id": 1234567890,
                "instrument_id": 1,
                "trader": "0x1234567890abcdef1234567890abcdef12345678",
                "buy": true,
                "price": "100.00",
                "quantity": "10.00",
                "client_order_id": "550e8400e29b41d4a716446655440000",
                "side": "maker",
                "sequence": 1234567890,
                "notional": "1000.00",
                "timestamp": 1767225600000,
                "fee_asset": "pUSD",
                "fee": "0.125",
                "builder_fee": "1.00",
                "total_fee": "1.125",
                "fee_rate": "0.001"
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
    value: builderFills
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
