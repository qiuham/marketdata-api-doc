---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/deribit_volatility_indexindex_name
api_type: WebSocket
updated_at: 2026-11-23 19:00:30.388181
---

# deribit_volatility_index.(index_name)

> Volatility index updates for the given `index_name`.

Use this channel to receive volatility index values (e.g., DVOL-like measures) as they update.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json deribit_volatility_index.(index_name)
id: deribit_volatility_index.(index_name)
title: 'deribit_volatility_index.(index_name) '
description: >
  Volatility index updates for the given `index_name`.


  Use this channel to receive volatility index values (e.g., DVOL-like measures)
  as they update.


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
address: deribit_volatility_index.(index_name)
parameters:
  - id: index_name
    jsonSchema:
      type: string
      description: Index identifier supported for DVOL
      enum:
        - btc_usd
        - eth_usd
    description: Index identifier supported for DVOL
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_deribit_volatility_index_index_name
    title: Send subscribe request for deribit_volatility_index
    description: Client sends subscription request for deribit_volatility_index updates
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
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
                  - name: volatility
                    type: number
                    description: Value of the corresponding volatility
                    required: true
                  - name: index_name
                    type: string
                    description: Index identifier supported for DVOL
                    enumValues:
                      - btc_usd
                      - eth_usd
                    required: true
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
                  x-parser-schema-id: <anonymous-schema-416>
                volatility:
                  description: Value of the corresponding volatility
                  type: number
                  x-parser-schema-id: <anonymous-schema-417>
                index_name:
                  description: Index identifier supported for DVOL
                  type: string
                  enum:
                    - btc_usd
                    - eth_usd
                  x-parser-schema-id: <anonymous-schema-418>
              required:
                - timestamp
                - volatility
                - index_name
              type: object
              x-parser-schema-id: <anonymous-schema-415>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-414>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "volatility": 129.36,
              "timestamp": 1619777946007,
              "index_name": "btc_usd"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: deribit_volatility_index.(index_name)
  - &ref_1
    id: receive_deribit_volatility_index_index_name_updates
    title: Receive deribit_volatility_index updates
    description: Client receives deribit_volatility_index update notifications
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
              x-parser-schema-id: <anonymous-schema-408>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-409>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-410>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-413>
                  x-parser-schema-id: <anonymous-schema-412>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-411>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-407>
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
                "deribit_volatility_index.btc_usd"
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
    value: deribit_volatility_index.(index_name)
securitySchemes: []

````

## Related topics

- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [deribit_price_index.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_indexindex_name.md)
- [deribit_price_statistics.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_statisticsindex_name.md)
- [deribit_price_ranking.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_rankingindex_name.md)