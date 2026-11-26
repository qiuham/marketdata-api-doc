---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/orderbook/bookinstrument_nameinterval
api_type: WebSocket
updated_at: 2026-11-26 19:02:01.882702
---

# book.(instrument_name).(interval)

> Real-time order book updates for a specific instrument.

- The first notification contains a full snapshot of the book (bids and asks for **all price levels** — no depth limit).
- Subsequent notifications contain only incremental changes to individual price levels.
- Updates are tuples in the form `[action, price, amount]`, where `action` is one of: `new`, `change`, `delete`.

Each notification includes a `change_id`. Every message except the first also contains `prev_change_id`. If `prev_change_id` equals the `change_id` of the previous message, it indicates that no messages were missed.

For Starbase-routed instruments, the published price levels include accepted mass-quote liquidity.

**Depth:** This channel delivers the complete order book with no depth restriction. If you need a depth-limited, price-grouped snapshot, use `book.{instrument_name}.{group}.{depth}.{interval}` instead.

**Units:** For perpetuals and futures, `amount` is in USD units. For options, `amount` is in the corresponding cryptocurrency contracts (e.g., BTC or ETH).

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json book.(instrument_name).(interval)
id: book.(instrument_name).(interval)
title: 'book.(instrument_name).(interval) '
description: >
  Real-time order book updates for a specific instrument.


  - The first notification contains a full snapshot of the book (bids and asks
  for **all price levels** — no depth limit).

  - Subsequent notifications contain only incremental changes to individual
  price levels.

  - Updates are tuples in the form `[action, price, amount]`, where `action` is
  one of: `new`, `change`, `delete`.


  Each notification includes a `change_id`. Every message except the first also
  contains `prev_change_id`. If `prev_change_id` equals the `change_id` of the
  previous message, it indicates that no messages were missed.


  For Starbase-routed instruments, the published price levels include accepted
  mass-quote liquidity.


  **Depth:** This channel delivers the complete order book with no depth
  restriction. If you need a depth-limited, price-grouped snapshot, use
  `book.{instrument_name}.{group}.{depth}.{interval}` instead.


  **Units:** For perpetuals and futures, `amount` is in USD units. For options,
  `amount` is in the corresponding cryptocurrency contracts (e.g., BTC or ETH).


  **📖 Related Article:** [Options Data Collection Best
  Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)
servers:
  - id: production
    protocol: wss
    host: deribit.com/ws/api/v2
    bindings: []
    variables: []
  - id: testnet
    protocol: wss
    host: test.deribit.com/ws/api/v2
    bindings: []
    variables: []
address: book.(instrument_name).(interval)
parameters:
  - id: instrument_name
    jsonSchema:
      type: string
      description: Instrument name
    description: Instrument name
    type: string
    required: true
    deprecated: false
  - id: interval
    jsonSchema:
      type: string
      description: >-
        Frequency of notifications. Events will be aggregated over this
        interval. The value `raw` selects the finest granularity - events are
        aggregated over a 1 millisecond interval **(Please note that `raw`
        interval is only available to authorized users)**
      enum:
        - raw
        - 100ms
        - agg2
    description: >-
      Frequency of notifications. Events will be aggregated over this interval.
      The value `raw` selects the finest granularity - events are aggregated
      over a 1 millisecond interval **(Please note that `raw` interval is only
      available to authorized users)**
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_book_instrument_name_interval
    title: Send subscribe request for order book
    description: Client sends subscription request for order book updates
    type: send
    messages:
      - &ref_4
        id: subscription_message
        contentType: application/json
        payload:
          - name: Subscription Notification Data
            description: Server sends subscription notification data
            type: object
            properties:
              - name: data
                type: object
                required: true
                properties:
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: true
                  - name: change_id
                    type: integer
                    description: Identifier of the notification
                    required: true
                  - name: prev_change_id
                    type: integer
                    description: >-
                      Identifier of the previous notification (it's **not**
                      included for the first notification)
                    required: false
                  - name: asks
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: >-
                          The first notification will contain the amounts for
                          all price levels (a list of ["new", price, amount]
                          tuples). All following notifications will contain a
                          list of tuples with action, price level and new amount
                          ([action, price, amount]). Action can be `new`,
                          `change` or `delete`.
                        required: false
                  - name: bids
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: (See 'asks' above.)
                        required: false
                  - name: timestamp
                    type: integer
                    description: >-
                      The timestamp of last change (milliseconds since the Unix
                      epoch)
                    required: false
                  - name: type
                    type: string
                    description: >-
                      Type of notification: `snapshot` for initial, `change` for
                      others
                    enumValues:
                      - snapshot
                      - change
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-51>
                change_id:
                  description: Identifier of the notification
                  type: integer
                  x-parser-schema-id: <anonymous-schema-52>
                prev_change_id:
                  type: integer
                  description: >-
                    Identifier of the previous notification (it's **not**
                    included for the first notification)
                  x-parser-schema-id: <anonymous-schema-53>
                asks:
                  type: array
                  items:
                    type: array
                    description: >-
                      The first notification will contain the amounts for all
                      price levels (a list of ["new", price, amount] tuples).
                      All following notifications will contain a list of tuples
                      with action, price level and new amount ([action, price,
                      amount]). Action can be `new`, `change` or `delete`.
                    minItems: 3
                    maxItems: 3
                    items:
                      - type: string
                        enum:
                          - new
                          - change
                          - delete
                        x-parser-schema-id: <anonymous-schema-56>
                      - type: number
                        x-parser-schema-id: <anonymous-schema-57>
                      - type: number
                        x-parser-schema-id: <anonymous-schema-58>
                    x-parser-schema-id: <anonymous-schema-55>
                  x-parser-schema-id: <anonymous-schema-54>
                bids:
                  type: array
                  items:
                    type: array
                    description: (See 'asks' above.)
                    minItems: 3
                    maxItems: 3
                    items:
                      - type: string
                        enum:
                          - new
                          - change
                          - delete
                        x-parser-schema-id: <anonymous-schema-61>
                      - type: number
                        x-parser-schema-id: <anonymous-schema-62>
                      - type: number
                        x-parser-schema-id: <anonymous-schema-63>
                    x-parser-schema-id: <anonymous-schema-60>
                  x-parser-schema-id: <anonymous-schema-59>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: >-
                    The timestamp of last change (milliseconds since the Unix
                    epoch)
                  x-parser-schema-id: <anonymous-schema-64>
                type:
                  description: >-
                    Type of notification: `snapshot` for initial, `change` for
                    others
                  type: string
                  enum:
                    - snapshot
                    - change
                  x-parser-schema-id: <anonymous-schema-65>
              required:
                - instrument_name
                - change_id
                - asks
                - bids
              type: object
              x-parser-schema-id: <anonymous-schema-50>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-49>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "type": "snapshot",
              "timestamp": 1554373962454,
              "instrument_name": "BTC-PERPETUAL",
              "change_id": 297217,
              "bids": [
                [
                  "new",
                  5042.34,
                  30
                ],
                [
                  "new",
                  5041.94,
                  20
                ]
              ],
              "asks": [
                [
                  "new",
                  5042.64,
                  40
                ],
                [
                  "new",
                  5043.3,
                  40
                ]
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: book.(instrument_name).(interval)
  - &ref_1
    id: receive_book_instrument_name_interval_updates
    title: Receive order book updates
    description: Client receives order book update notifications
    type: receive
    messages:
      - &ref_3
        id: subscribe_request
        contentType: application/json
        payload:
          - name: Subscription Request
            description: >-
              Client sends subscription request to subscribe to notification
              channel. Please refer to [Notification
              page](https://docs.deribit.com/articles/notifications) for more
              information.
            type: object
            properties:
              - name: jsonrpc
                type: string
                description: '2.0'
                required: true
              - name: id
                type: integer
                required: true
              - name: method
                type: string
                enumValues:
                  - public/subscribe
                  - private/subscribe
                required: true
              - name: params
                type: object
                required: true
                properties:
                  - name: channels
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: string
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            jsonrpc:
              type: string
              const: '2.0'
              x-parser-schema-id: <anonymous-schema-43>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-44>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-45>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-48>
                  x-parser-schema-id: <anonymous-schema-47>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-46>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-42>
        title: Subscription Request
        description: >-
          Client sends subscription request to subscribe to notification
          channel. Please refer to [Notification
          page](https://docs.deribit.com/articles/notifications) for more
          information.
        example: |-
          {
            "jsonrpc": "2.0",
            "method": "public/subscribe",
            "id": 42,
            "params": {
              "channels": [
                "book.BTC-PERPETUAL.100ms"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
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
    value: book.(instrument_name).(interval)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Rate Limits](https://docs.deribit.com/articles/rate-limits.md)
- [book.(instrument_name).(group).(depth).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_namegroupdepthinterval.md)