---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/user/userlock
api_type: WebSocket
updated_at: 2026-11-25 19:00:45.130641
---

# user.lock

> Notifications when the account is locked or unlocked.

Use this channel to react to account lock events (e.g., pause trading workflows) and to detect when access is restored.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.lock
id: user.lock
title: 'user.lock '
description: >
  Notifications when the account is locked or unlocked.


  Use this channel to react to account lock events (e.g., pause trading
  workflows) and to detect when access is restored.
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
address: user.lock
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_lock
    title: Send subscribe request
    description: Client sends subscription request for user
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
                  - name: currency
                    type: string
                    description: >-
                      Currency on which account lock has changed, `ALL` if
                      changed for all currencies
                    required: true
                  - name: locked
                    type: boolean
                    description: >-
                      Value is set to 'true' when user account is locked in
                      currency
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                currency:
                  type: string
                  example: BTC, ALL
                  description: >-
                    Currency on which account lock has changed, `ALL` if changed
                    for all currencies
                  x-parser-schema-id: <anonymous-schema-1487>
                locked:
                  type: boolean
                  example: false
                  description: >-
                    Value is set to 'true' when user account is locked in
                    currency
                  x-parser-schema-id: <anonymous-schema-1488>
              required:
                - currency
                - locked
              type: object
              x-parser-schema-id: <anonymous-schema-1486>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1485>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "locked": true,
              "currency": "ALL"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: user.lock
  - &ref_1
    id: receive_user_lock
    title: Receive user
    description: Client receives user notifications
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
              x-parser-schema-id: <anonymous-schema-1479>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1480>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1481>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1484>
                  x-parser-schema-id: <anonymous-schema-1483>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1482>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1478>
        title: Subscription Request
        description: >-
          Client sends subscription request to subscribe to notification
          channel. Please refer to [Notification
          page](https://docs.deribit.com/articles/notifications) for more
          information.
        example: |-
          {
            "jsonrpc": "2.0",
            "method": "private/subscribe",
            "id": 42,
            "params": {
              "channels": [
                "user.lock"
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
    value: user.lock
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [private/get_user_locks](https://docs.deribit.com/api-reference/account-management/private-get_user_locks.md)
- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md)
- [Voice Broker Trading API](https://docs.deribit.com/articles/voice-broker-trading-api.md)
- [user.lsp ](https://docs.deribit.com/subscriptions/user/userlsp.md)