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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-book'
updated_at: 2026-11-13
---

# Book

> Perps WebSocket order book updates.

The book channel pushes a full snapshot every 100 ms for each subscribed
instrument. Subscribe to `book::{iid}` for the top 20 bid and ask levels, or
opt in to `book::{iid}::50` for the top 50 levels per side. The 50-level form
provides deeper order book visibility than the default snapshot.

Each push replaces the prior state; it is not a delta. Levels in `data.b` are
sorted from highest to lowest price, and levels in `data.a` are sorted from
lowest to highest price. If a side has fewer levels than the selected depth,
the snapshot includes all available levels on that side.

> [!NOTE]
>
> Allowed depths are exactly 20 and 50. `book::{iid}::20` is an alias of
> `book::{iid}`; updates for either subscription use the canonical
> `ch: "book::{iid}"`. Updates for `book::{iid}::50` use
> `ch: "book::{iid}::50"`. Other suffixes are rejected like any unknown channel
> with `{"status":"err","error":"invalid channel"}` in the response `data`
> array. You can subscribe to both depths on one connection, and each counts as
> one subscription toward the per-connection limit.


## AsyncAPI

````yaml asyncapi-perps.json book
id: book
title: Book
description: >-
  Order book snapshot updates (top 20 or, with the ::50 suffix, top 50 levels
  per side). Pushed every 100ms.
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
    id: BookSubscribe
    title: Book subscribe
    description: Subscribe to book
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: Subscribe to order book updates for an instrument
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
                description: >-
                  Book subscription in format "book::{iid}" or
                  "book::{iid}::{depth}". Omitted depth and "20" select the top
                  20 levels per side; "50" selects the top 50. Allowed depths
                  are exactly 20 and 50.
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
              description: Client-supplied identifier used to correlate the response.
              type: integer
              x-parser-schema-id: <anonymous-schema-314>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-315>
            chs:
              type: array
              description: >-
                Book subscription in format "book::{iid}" or
                "book::{iid}::{depth}". Omitted depth and "20" select the top 20
                levels per side; "50" selects the top 50. Allowed depths are
                exactly 20 and 50.
              items:
                type: string
                pattern: ^book::\d+(::(20|50))?$
                x-parser-schema-id: <anonymous-schema-317>
              example:
                - book::1
                - book::1::50
              x-parser-schema-id: <anonymous-schema-316>
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
          x-parser-schema-id: <anonymous-schema-313>
        title: Subscribe
        description: Subscribe to order book updates for an instrument
        example: |-
          {
            "req": "sub",
            "chs": [
              "book::1",
              "book::1::50"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: book
  - &ref_3
    id: BookSubscribeResponse
    title: Book subscribe response
    description: Book subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to book subscribe request
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
              x-parser-schema-id: <anonymous-schema-319>
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
                        x-parser-schema-id: <anonymous-schema-323>
                    x-parser-schema-id: <anonymous-schema-322>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-325>
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
                        x-parser-schema-id: <anonymous-schema-326>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-327>
                      ts:
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-328>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-329>
                    x-parser-schema-id: <anonymous-schema-324>
                x-parser-schema-id: <anonymous-schema-321>
              x-parser-schema-id: <anonymous-schema-320>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-318>
        title: Subscribe Response
        description: Response to book subscribe request
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
    id: BookUnsubscribe
    title: Book unsubscribe
    description: Unsubscribe from book
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from order book updates
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
                description: >-
                  Book subscription in format "book::{iid}" or
                  "book::{iid}::{depth}". Omitted depth and "20" select the top
                  20 levels per side; "50" selects the top 50. Allowed depths
                  are exactly 20 and 50.
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
              description: Client-supplied identifier used to correlate the response.
              type: integer
              x-parser-schema-id: <anonymous-schema-331>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-332>
            chs:
              type: array
              description: >-
                Book subscription in format "book::{iid}" or
                "book::{iid}::{depth}". Omitted depth and "20" select the top 20
                levels per side; "50" selects the top 50. Allowed depths are
                exactly 20 and 50.
              items:
                type: string
                pattern: ^book::\d+(::(20|50))?$
                x-parser-schema-id: <anonymous-schema-334>
              example:
                - book::1
                - book::1::50
              x-parser-schema-id: <anonymous-schema-333>
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
          x-parser-schema-id: <anonymous-schema-330>
        title: Unsubscribe
        description: Unsubscribe from order book updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "book::1",
              "book::1::50"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: BookUnsubscribeResponse
    title: Book unsubscribe response
    description: Book unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to book unsubscribe request
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
              x-parser-schema-id: <anonymous-schema-336>
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
                        x-parser-schema-id: <anonymous-schema-340>
                    x-parser-schema-id: <anonymous-schema-339>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-342>
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
                        x-parser-schema-id: <anonymous-schema-343>
                      arts:
                        type: integer
                        description: >-
                          Gateway arrival timestamp captured at handler entry,
                          in Unix milliseconds.
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-344>
                      ts:
                        type: integer
                        description: >-
                          decision time in Unix milliseconds: terminal event
                          time for event-backed outcomes, gateway decision time
                          otherwise
                        example: 1767225600000
                        x-parser-schema-id: <anonymous-schema-345>
                      ref:
                        type: string
                        description: >-
                          Unique server-generated rejection reference. Include
                          this value when asking support to locate the
                          corresponding structured rejection trace.
                        example: g-0011223344556
                        x-parser-schema-id: <anonymous-schema-346>
                    x-parser-schema-id: <anonymous-schema-341>
                x-parser-schema-id: <anonymous-schema-338>
              x-parser-schema-id: <anonymous-schema-337>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-335>
        title: Unsubscribe Response
        description: Response to book unsubscribe request
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
    id: BookUpdate
    title: Book update
    description: Receive book updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: Real-time order book updates for subscribed instruments
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
                  - name: b
                    type: array
                    description: Bid levels
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: |
                          - `"100.00"` - Price
                          - `"10.00"` - Quantity
                        required: false
                        properties:
                          - name: item
                            type: string
                            required: false
                  - name: a
                    type: array
                    description: Ask levels
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: |
                          - `"100.00"` - Price
                          - `"10.00"` - Quantity
                        required: false
                        properties:
                          - name: item
                            type: string
                            required: false
        headers: []
        jsonPayloadSchema:
          title: Book Update
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
              x-parser-schema-id: <anonymous-schema-348>
            ts:
              description: Server send time, Unix milliseconds
              type: integer
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-349>
            ets:
              type: integer
              description: >-
                Event timestamp — the newest event this update reflects, in Unix
                milliseconds. Distinct from `ts`, which is the server send time;
                `ts - ets` is time spent inside the exchange after the event.
                `ets=0` means no event horizon is attested, and consumers must
                treat the horizon as unknown.
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-350>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-351>
            data:
              type: object
              required:
                - b
                - a
              properties:
                b:
                  type: array
                  items:
                    type: array
                    items:
                      type: string
                      x-parser-schema-id: <anonymous-schema-355>
                    maxItems: 2
                    description: |
                      - `"100.00"` - Price
                      - `"10.00"` - Quantity
                    example:
                      - '100.00'
                      - '10.00'
                    x-parser-schema-id: <anonymous-schema-354>
                  description: Bid levels
                  x-parser-schema-id: <anonymous-schema-353>
                a:
                  type: array
                  items:
                    type: array
                    items:
                      type: string
                      x-parser-schema-id: <anonymous-schema-358>
                    maxItems: 2
                    description: |
                      - `"100.00"` - Price
                      - `"10.00"` - Quantity
                    example:
                      - '100.00'
                      - '10.00'
                    x-parser-schema-id: <anonymous-schema-357>
                  description: Ask levels
                  x-parser-schema-id: <anonymous-schema-356>
              x-parser-schema-id: <anonymous-schema-352>
          required:
            - ch
            - ts
            - ets
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-347>
        title: Update
        description: Real-time order book updates for subscribed instruments
        example: |-
          {
            "ch": "book::1",
            "ts": 1767225600000,
            "ets": 1767225600000,
            "sq": 1234567890,
            "data": {
              "b": [
                [
                  "100.00",
                  "10.00"
                ]
              ],
              "a": [
                [
                  "100.00",
                  "10.00"
                ]
              ]
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
    value: book
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
