---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/quoteinstrument_name
api_type: WebSocket
updated_at: 2026-11-18 18:58:58.970774
---

# quote.(instrument_name)

> Best bid/ask price and size for a specific instrument.

This subscription provides top-of-book updates (best bid and best ask) without the full depth of the order book. Use it when you only need the current spread and top sizes.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json quote.(instrument_name)
id: quote.(instrument_name)
title: 'quote.(instrument_name) '
description: >
  Best bid/ask price and size for a specific instrument.


  This subscription provides top-of-book updates (best bid and best ask) without
  the full depth of the order book. Use it when you only need the current spread
  and top sizes.
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
address: quote.(instrument_name)
parameters:
  - id: instrument_name
    jsonSchema:
      type: string
      description: Instrument name
    description: Instrument name
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_6
    id: send_subscribe_quote_instrument_name
    title: Send subscribe request for quote
    description: Client sends subscription request for quote updates
    type: send
    messages:
      - &ref_8
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
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: true
                  - name: best_bid_price
                    type: &ref_0
                      - number
                      - 'null'
                    description: The current best bid price, `0` if the bid side is empty
                    required: true
                  - name: best_bid_amount
                    type: &ref_1
                      - number
                      - 'null'
                    description: It represents the requested order size of all best bids
                    required: true
                  - name: best_ask_price
                    type: &ref_2
                      - number
                      - 'null'
                    description: The current best ask price, `0` if the ask side is empty
                    required: false
                  - name: best_ask_amount
                    type: &ref_3
                      - number
                      - 'null'
                    description: It represents the requested order size of all best asks
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-224>
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-225>
                best_bid_price:
                  description: The current best bid price, `0` if the bid side is empty
                  type: *ref_0
                  x-parser-schema-id: <anonymous-schema-226>
                best_bid_amount:
                  description: It represents the requested order size of all best bids
                  type: *ref_1
                  x-parser-schema-id: <anonymous-schema-227>
                best_ask_price:
                  description: The current best ask price, `0` if the ask side is empty
                  type: *ref_2
                  x-parser-schema-id: <anonymous-schema-228>
                best_ask_amount:
                  description: It represents the requested order size of all best asks
                  type: *ref_3
                  x-parser-schema-id: <anonymous-schema-229>
              required:
                - timestamp
                - instrument_name
                - best_bid_amount
                - best_bid_price
                - best_add_amount
                - best_add_price
              type: object
              x-parser-schema-id: <anonymous-schema-223>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-222>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "best_ask_amount": 50,
              "best_ask_price": 3996.61,
              "best_bid_amount": 40,
              "best_bid_price": 3914.97,
              "instrument_name": "BTC-PERPETUAL",
              "timestamp": 1550658624149
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_4
      - id: x-parser-unique-object-id
        value: quote.(instrument_name)
  - &ref_5
    id: receive_quote_instrument_name_updates
    title: Receive quote updates
    description: Client receives quote update notifications
    type: receive
    messages:
      - &ref_7
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
              x-parser-schema-id: <anonymous-schema-216>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-217>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-218>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-221>
                  x-parser-schema-id: <anonymous-schema-220>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-219>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-215>
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
                "quote.BTC-PERPETUAL"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_4
sendOperations:
  - *ref_5
receiveOperations:
  - *ref_6
sendMessages:
  - *ref_7
receiveMessages:
  - *ref_8
extensions:
  - id: x-parser-unique-object-id
    value: quote.(instrument_name)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [user.trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/usertradesinstrument_nameinterval.md)
- [book.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_nameinterval.md)
- [book.(instrument_name).(group).(depth).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_namegroupdepthinterval.md)
- [perpetual.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/market-data/perpetualinstrument_nameinterval.md)