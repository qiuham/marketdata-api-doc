---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/platform/platform_state
api_type: WebSocket
updated_at: 2026-11-24 18:59:42.291853
---

# platform_state

> Platform state notifications.

Use this channel to monitor whether the Deribit platform is operational and to detect maintenance periods or partial outages that may affect trading, authentication, or market data.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json platform_state
id: platform_state
title: 'platform_state '
description: >
  Platform state notifications.


  Use this channel to monitor whether the Deribit platform is operational and to
  detect maintenance periods or partial outages that may affect trading,
  authentication, or market data.
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
address: platform_state
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_platform_state
    title: Send subscribe request
    description: Client sends subscription request for platform_state
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
                  - name: price_index
                    type: string
                    description: >-
                      Name of index that is locked or unlocked, sent only with
                      `locked` field
                    required: false
                  - name: locked
                    type: boolean
                    description: >-
                      Value is set to 'true' when index is locked on platform,
                      sent only with `price_index` field
                    required: false
                  - name: maintenance
                    type: boolean
                    description: Value is set to `true` when the maintenance break begins
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                price_index:
                  type: string
                  example: btc_usdc
                  description: >-
                    Name of index that is locked or unlocked, sent only with
                    `locked` field
                  x-parser-schema-id: <anonymous-schema-10>
                locked:
                  type: boolean
                  example: false
                  description: >-
                    Value is set to 'true' when index is locked on platform,
                    sent only with `price_index` field
                  x-parser-schema-id: <anonymous-schema-11>
                maintenance:
                  type: boolean
                  example: true
                  description: Value is set to `true` when the maintenance break begins
                  x-parser-schema-id: <anonymous-schema-12>
              required: []
              type: object
              x-parser-schema-id: <anonymous-schema-9>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-8>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "price_index": "sol_usdc",
              "locked": true
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: platform_state
  - &ref_1
    id: receive_platform_state
    title: Receive platform_state
    description: Client receives platform_state notifications
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
              x-parser-schema-id: <anonymous-schema-2>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-3>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-4>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-7>
                  x-parser-schema-id: <anonymous-schema-6>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-5>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1>
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
                "platform_state"
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
    value: platform_state
securitySchemes: []

````

## Related topics

- [platform_state.public_methods_state ](https://docs.deribit.com/subscriptions/platform/platform_statepublic_methods_state.md)
- [instrument.state.(kind).(currency) ](https://docs.deribit.com/subscriptions/market-data/instrumentstatekindcurrency.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [Security Status Request(e) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-status-request.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)