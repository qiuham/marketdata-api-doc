---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/announcements/announcements
api_type: WebSocket
updated_at: 2026-11-25 19:00:44.405529
---

# announcements

> General announcements concerning the Deribit platform.

Subscribe to receive operational messages such as maintenance notices, incidents, and important platform updates.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json announcements
id: announcements
title: 'announcements '
description: >
  General announcements concerning the Deribit platform.


  Subscribe to receive operational messages such as maintenance notices,
  incidents, and important platform updates.
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
address: announcements
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_announcements
    title: Send subscribe request
    description: Client sends subscription request for announcements
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
                  - name: id
                    type: integer
                    description: Announcement's identifier
                    required: true
                  - name: title
                    type: string
                    description: Announcement's title
                    required: true
                  - name: body
                    type: string
                    description: HTML-formatted announcement body
                    required: true
                  - name: publication_timestamp
                    type: integer
                    description: >-
                      The timestamp (milliseconds since the Unix epoch) of
                      announcement publication
                    required: true
                  - name: important
                    type: boolean
                    description: Whether the announcement is marked as important
                    required: true
                  - name: confirmation
                    type: boolean
                    description: >-
                      Whether the user confirmation is required for this
                      announcement
                    required: false
                  - name: unread
                    type: integer
                    description: >-
                      The number of previous unread announcements (optional,
                      only for authorized users).
                    required: false
                  - name: action
                    type: string
                    description: >-
                      Action taken by the platform administrators. Published a
                      `new` announcement, or `delete`d the old one
                    enumValues:
                      - new
                      - deleted
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                id:
                  type: integer
                  description: Announcement's identifier
                  example: 1532593832021
                  x-parser-schema-id: <anonymous-schema-32>
                title:
                  type: string
                  description: Announcement's title
                  example: Example announcement
                  x-parser-schema-id: <anonymous-schema-33>
                body:
                  type: string
                  description: HTML-formatted announcement body
                  example: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  x-parser-schema-id: <anonymous-schema-34>
                publication_timestamp:
                  type: integer
                  description: >-
                    The timestamp (milliseconds since the Unix epoch) of
                    announcement publication
                  example: 1532593832021
                  x-parser-schema-id: <anonymous-schema-35>
                important:
                  type: boolean
                  description: Whether the announcement is marked as important
                  x-parser-schema-id: <anonymous-schema-36>
                confirmation:
                  type: boolean
                  description: >-
                    Whether the user confirmation is required for this
                    announcement
                  x-parser-schema-id: <anonymous-schema-37>
                unread:
                  type: integer
                  description: >-
                    The number of previous unread announcements (optional, only
                    for authorized users).
                  x-parser-schema-id: <anonymous-schema-38>
                action:
                  type: string
                  enum:
                    - new
                    - deleted
                  description: >-
                    Action taken by the platform administrators. Published a
                    `new` announcement, or `delete`d the old one
                  x-parser-schema-id: <anonymous-schema-39>
              required:
                - id
                - action
                - title
                - body
                - publication_timestamp
                - important
              type: object
              x-parser-schema-id: <anonymous-schema-31>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-30>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "id": 123,
              "title": "<string>",
              "body": "<string>",
              "publication_timestamp": 123,
              "important": true,
              "confirmation": true,
              "unread": 123,
              "action": "<string>"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: announcements
  - &ref_1
    id: receive_announcements
    title: Receive announcements
    description: Client receives announcements notifications
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
              x-parser-schema-id: <anonymous-schema-24>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-25>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-26>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-29>
                  x-parser-schema-id: <anonymous-schema-28>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-27>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-23>
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
                "announcements"
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
    value: announcements
securitySchemes: []

````

## Related topics

- [public/get_announcements](https://docs.deribit.com/api-reference/account-management/public-get_announcements.md)
- [private/get_new_announcements](https://docs.deribit.com/api-reference/account-management/private-get_new_announcements.md)
- [private/set_announcement_as_read](https://docs.deribit.com/api-reference/account-management/private-set_announcement_as_read.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Block Trading](https://docs.deribit.com/articles/block-trading-api.md)