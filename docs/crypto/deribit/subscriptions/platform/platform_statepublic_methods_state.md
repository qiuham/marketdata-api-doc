---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/platform/platform_statepublic_methods_state
api_type: WebSocket
updated_at: 2026-11-20 19:00:10.069641
---

# platform_state.public_methods_state

> Notifications indicating whether unauthenticated (public) requests are currently allowed.

This is useful for monitoring service availability for public endpoints (e.g., market data) without authentication.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json platform_state.public_methods_state
id: platform_state.public_methods_state
title: 'platform_state.public_methods_state '
description: >
  Notifications indicating whether unauthenticated (public) requests are
  currently allowed.


  This is useful for monitoring service availability for public endpoints (e.g.,
  market data) without authentication.
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
address: platform_state.public_methods_state
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_platform_state_public_methods_state
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
                  - name: allow_unauthenticated_public_requests
                    type: boolean
                    description: >-
                      Value is set to 'true' when unauthorized public requests
                      are allowed
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                allow_unauthenticated_public_requests:
                  type: boolean
                  description: >-
                    Value is set to 'true' when unauthorized public requests are
                    allowed
                  x-parser-schema-id: <anonymous-schema-22>
              required:
                - allow_unauthenticated_public_requests
              type: object
              x-parser-schema-id: <anonymous-schema-21>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-20>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "allow_unauthenticated_public_requests": true
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: platform_state.public_methods_state
  - &ref_1
    id: receive_platform_state_public_methods_state
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
              x-parser-schema-id: <anonymous-schema-14>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-15>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-16>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-19>
                  x-parser-schema-id: <anonymous-schema-18>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-17>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-13>
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
                "platform_state.public_methods_state"
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
    value: platform_state.public_methods_state
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [platform_state ](https://docs.deribit.com/subscriptions/platform/platform_state.md)
- [public/get_combos](https://docs.deribit.com/api-reference/combo-books/public-get_combos.md)
- [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details.md)
- [public/get_combo_ids](https://docs.deribit.com/api-reference/combo-books/public-get_combo_ids.md)