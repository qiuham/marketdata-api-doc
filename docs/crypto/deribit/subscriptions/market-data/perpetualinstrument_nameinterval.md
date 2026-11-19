---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/perpetualinstrument_nameinterval
api_type: WebSocket
updated_at: 2026-11-19 19:05:33.597229
---

# perpetual.(instrument_name).(interval)

> Provide current interest rate - but only for **perpetual** instruments. Other types won't generate any notification.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json perpetual.(instrument_name).(interval)
id: perpetual.(instrument_name).(interval)
title: 'perpetual.(instrument_name).(interval) '
description: >-
  Provide current interest rate - but only for **perpetual** instruments. Other
  types won't generate any notification.
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
address: perpetual.(instrument_name).(interval)
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
        Notification interval. The raw interval selects unaggregated updates and
        is available only to authorized users.
      enum:
        - agg2
        - 100ms
        - raw
    description: >-
      Notification interval. The raw interval selects unaggregated updates and
      is available only to authorized users.
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_perpetual_instrument_name_interval
    title: Send subscribe request for perpetual
    description: Client sends subscription request for perpetual updates
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
                  - name: interest
                    type: number
                    description: Current interest
                    required: true
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
                  - name: index_price
                    type: number
                    description: Current index price
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                interest:
                  description: Current interest
                  type: number
                  x-parser-schema-id: <anonymous-schema-211>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-212>
                index_price:
                  description: Current index price
                  type: number
                  example: 8247.27
                  x-parser-schema-id: <anonymous-schema-213>
              required:
                - interest
                - timestamp
                - index_price
              type: object
              x-parser-schema-id: <anonymous-schema-210>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-209>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "interest": 0.004999511380756577,
              "timestamp": 1571386349530,
              "index_price": 7872.88
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: perpetual.(instrument_name).(interval)
  - &ref_1
    id: receive_perpetual_instrument_name_interval_updates
    title: Receive perpetual updates
    description: Client receives perpetual update notifications
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
              x-parser-schema-id: <anonymous-schema-203>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-204>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-205>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-208>
                  x-parser-schema-id: <anonymous-schema-207>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-206>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-202>
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
                "perpetual.BTC-PERPETUAL.100ms"
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
    value: perpetual.(instrument_name).(interval)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [book.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_nameinterval.md)
- [ticker.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/market-data/tickerinstrument_nameinterval.md)
- [book.(instrument_name).(group).(depth).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_namegroupdepthinterval.md)
- [trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/trades/tradesinstrument_nameinterval.md)