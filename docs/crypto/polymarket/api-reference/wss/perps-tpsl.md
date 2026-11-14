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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-tpsl'
updated_at: 2026-11-13
---

# TP/SL

> Perps WebSocket private TP/SL lifecycle updates.



## AsyncAPI

````yaml asyncapi-perps.json tpsl
id: tpsl
title: TP/SL
description: >-
  Real-time TP/SL lifecycle transitions. Requires authentication, see
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
    id: TpslSubscribe
    title: Tpsl subscribe
    description: Subscribe to TP/SL updates
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: Subscribe to private TP/SL updates (requires prior auth)
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
                description: 'TP/SL private channel: "tpsl"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - tpsl
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              description: Client-supplied identifier used to correlate the response.
              type: integer
              x-parser-schema-id: <anonymous-schema-1094>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-1095>
            chs:
              type: array
              description: 'TP/SL private channel: "tpsl"'
              items:
                type: string
                enum:
                  - tpsl
                x-parser-schema-id: <anonymous-schema-1097>
              example:
                - tpsl
              x-parser-schema-id: <anonymous-schema-1096>
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
          x-parser-schema-id: <anonymous-schema-1093>
        title: Subscribe
        description: Subscribe to private TP/SL updates (requires prior auth)
        example: |-
          {
            "req": "sub",
            "chs": [
              "tpsl"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: tpsl
  - &ref_3
    id: TpslSubscribeResponse
    title: Tpsl subscribe response
    description: TP/SL subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to TP/SL subscribe request
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
                          `settlement_invalid_state`,
                          `settlement_close_only_required`, `unauthorized`,
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
              x-parser-schema-id: <anonymous-schema-1099>
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
                        x-parser-schema-id: <anonymous-schema-1103>
                    x-parser-schema-id: <anonymous-schema-1102>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-1105>
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
                          `settlement_invalid_state`,
                          `settlement_close_only_required`, `unauthorized`,
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
                        x-parser-schema-id: <anonymous-schema-1106>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1107>
                      ts:
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1108>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-1109>
                    x-parser-schema-id: <anonymous-schema-1104>
                x-parser-schema-id: <anonymous-schema-1101>
              x-parser-schema-id: <anonymous-schema-1100>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-1098>
        title: Subscribe Response
        description: Response to TP/SL subscribe request
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
    id: TpslUnsubscribe
    title: Tpsl unsubscribe
    description: Unsubscribe from TP/SL updates
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from private TP/SL updates
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
                description: 'TP/SL private channel: "tpsl"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - tpsl
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              description: Client-supplied identifier used to correlate the response.
              type: integer
              x-parser-schema-id: <anonymous-schema-1111>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-1112>
            chs:
              type: array
              description: 'TP/SL private channel: "tpsl"'
              items:
                type: string
                enum:
                  - tpsl
                x-parser-schema-id: <anonymous-schema-1114>
              example:
                - tpsl
              x-parser-schema-id: <anonymous-schema-1113>
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
          x-parser-schema-id: <anonymous-schema-1110>
        title: Unsubscribe
        description: Unsubscribe from private TP/SL updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "tpsl"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: TpslUnsubscribeResponse
    title: Tpsl unsubscribe response
    description: TP/SL unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to TP/SL unsubscribe request
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
                          `settlement_invalid_state`,
                          `settlement_close_only_required`, `unauthorized`,
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
              x-parser-schema-id: <anonymous-schema-1116>
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
                        x-parser-schema-id: <anonymous-schema-1120>
                    x-parser-schema-id: <anonymous-schema-1119>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-1122>
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
                          `settlement_invalid_state`,
                          `settlement_close_only_required`, `unauthorized`,
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
                        x-parser-schema-id: <anonymous-schema-1123>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1124>
                      ts:
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-1125>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-1126>
                    x-parser-schema-id: <anonymous-schema-1121>
                x-parser-schema-id: <anonymous-schema-1118>
              x-parser-schema-id: <anonymous-schema-1117>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-1115>
        title: Unsubscribe Response
        description: Response to TP/SL unsubscribe request
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
    id: TpslUpdate
    title: Tpsl update
    description: Receive TP/SL updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: TP/SL lifecycle transitions for authenticated users
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
                description: Server send time, Unix milliseconds
                required: true
              - name: ets
                type: integer
                description: >-
                  Event timestamp — the newest event this update reflects, in
                  Unix milliseconds. Distinct from `ts`, which is the server
                  send time; `ts - ets` is time spent inside the exchange after
                  the event. `ets=0` means no event horizon is attested, and
                  consumers must treat the horizon as unknown.
                required: true
              - name: sq
                type: integer
                description: Sequence number
                required: true
              - name: data
                type: object
                required: true
                properties:
                  - name: oid
                    type: integer
                    description: Order ID
                    required: true
                  - name: st
                    type: string
                    description: >-
                      New state of the leg. `untriggered`: accepted and waiting
                      for its parent order to fill. `armed`: live and watching
                      its trigger. `activated`: a trailing stop reached its
                      activation price and started trailing. `cancelled`:
                      cancelled by the account. `expired`: left the book for any
                      other reason, including firing; `reason` says which.
                    enumValues:
                      - untriggered
                      - armed
                      - activated
                      - cancelled
                      - expired
                    required: true
                  - name: reason
                    type: string
                    description: >-
                      Why the leg left the book. Present only when `st` is
                      `expired`. One of `triggered`, `parent_cancelled`,
                      `position_closed`, `position_flipped`,
                      `good_til_time_elapsed`, `reduce_only_invalid_at_trigger`,
                      `instrument_close_only`, `instrument_settled` or
                      `unknown`. Treat other values as `unknown`.
                    required: false
        headers: []
        jsonPayloadSchema:
          title: TP/SL Update
          description: >-
            A lifecycle transition for one of the authenticated account's TP/SL
            legs, one frame per transition. The frame carries only the new
            state; read the leg's full order, including its live trigger price,
            from open orders.
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
              x-parser-schema-id: <anonymous-schema-1128>
            ts:
              description: Server send time, Unix milliseconds
              type: integer
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-1129>
            ets:
              type: integer
              description: >-
                Event timestamp — the newest event this update reflects, in Unix
                milliseconds. Distinct from `ts`, which is the server send time;
                `ts - ets` is time spent inside the exchange after the event.
                `ets=0` means no event horizon is attested, and consumers must
                treat the horizon as unknown.
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-1130>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-1131>
            data:
              type: object
              required:
                - oid
                - st
              properties:
                oid:
                  type: integer
                  description: Order ID
                  example: 1234567890
                  x-parser-schema-id: <anonymous-schema-1133>
                st:
                  type: string
                  enum:
                    - untriggered
                    - armed
                    - activated
                    - cancelled
                    - expired
                  description: >-
                    New state of the leg. `untriggered`: accepted and waiting
                    for its parent order to fill. `armed`: live and watching its
                    trigger. `activated`: a trailing stop reached its activation
                    price and started trailing. `cancelled`: cancelled by the
                    account. `expired`: left the book for any other reason,
                    including firing; `reason` says which.
                  x-parser-schema-id: <anonymous-schema-1134>
                reason:
                  type: string
                  description: >-
                    Why the leg left the book. Present only when `st` is
                    `expired`. One of `triggered`, `parent_cancelled`,
                    `position_closed`, `position_flipped`,
                    `good_til_time_elapsed`, `reduce_only_invalid_at_trigger`,
                    `instrument_close_only`, `instrument_settled` or `unknown`.
                    Treat other values as `unknown`.
                  x-parser-schema-id: <anonymous-schema-1135>
              x-parser-schema-id: <anonymous-schema-1132>
          required:
            - ch
            - ts
            - ets
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-1127>
        title: Update
        description: TP/SL lifecycle transitions for authenticated users
        example: |-
          {
            "ch": "tpsl::12345",
            "ts": 1767225600002,
            "ets": 1767225600000,
            "sq": 1234567890,
            "data": {
              "oid": 1234567890,
              "st": "armed"
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
    value: tpsl
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
