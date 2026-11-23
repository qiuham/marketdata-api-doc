---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/user/useraccess_log
api_type: WebSocket
updated_at: 2026-11-23 19:00:31.289620
---

# user.access_log

> Security event notifications for the account.

Use this channel to monitor account-related security events (e.g., access log entries) and build alerting around suspicious activity.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.access_log
id: user.access_log
title: 'user.access_log '
description: >
  Security event notifications for the account.


  Use this channel to monitor account-related security events (e.g., access log
  entries) and build alerting around suspicious activity.
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
address: user.access_log
parameters: []
bindings: []
operations:
  - &ref_3
    id: send_subscribe_user_access_log
    title: Send subscribe request
    description: Client sends subscription request for user
    type: send
    messages:
      - &ref_5
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
                    description: Unique identifier
                    required: true
                  - name: ip
                    type: string
                    description: IP address of source that generated action
                    required: true
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
                  - name: country
                    type: string
                    description: Country where the IP address is registered (estimated)
                    required: true
                  - name: city
                    type: string
                    description: City where the IP address is registered (estimated)
                    required: true
                  - name: log
                    type: string
                    description: >
                      Action description. Possible values:


                      - ``changed_email`` - email was changed

                      - ``changed_password`` - password was changed

                      - ``disabled_tfa`` - TFA was disabled

                      - ``enabled_tfa`` - TFA was enabled

                      - ``success`` - successful login

                      - ``failure`` - login failure

                      - ``enabled_subaccount_login`` - login was enabled for
                      subaccount (in `data` - subaccount uid)

                      - ``disabled_subaccount_login`` - login was disabled for
                      subaccount (in `data` - subaccount uid)

                      - ``new_api_key`` - API key was created (in `data` key
                      client id)

                      - ``removed_api_key`` - API key was removed (in `data` key
                      client id)

                      - ``changed_scope`` - scope of API key was changed (in
                      `data` key client id)

                      - ``changed_whitelist`` - whitelist of API key was edited
                      (in `data` key client id)

                      - ``disabled_api_key`` - API key was disabled (in `data`
                      key client id)

                      - ``enabled_api_key`` - API key was enabled (in `data` key
                      client id)

                      - ``reset_api_key`` - API key was reset (in `data` key
                      client id)
                    required: true
                  - name: data
                    type: &ref_0
                      - object
                      - string
                    description: >-
                      Optional, additional information about action, type
                      depends on `log` value
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              type: object
              properties:
                id:
                  description: Unique identifier
                  type: integer
                  example: 5967413
                  x-parser-schema-id: <anonymous-schema-1471>
                ip:
                  description: IP address of source that generated action
                  type: string
                  x-parser-schema-id: <anonymous-schema-1472>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-1473>
                country:
                  description: Country where the IP address is registered (estimated)
                  type: string
                  x-parser-schema-id: <anonymous-schema-1474>
                city:
                  description: City where the IP address is registered (estimated)
                  type: string
                  x-parser-schema-id: <anonymous-schema-1475>
                log:
                  description: >
                    Action description. Possible values:


                    - ``changed_email`` - email was changed

                    - ``changed_password`` - password was changed

                    - ``disabled_tfa`` - TFA was disabled

                    - ``enabled_tfa`` - TFA was enabled

                    - ``success`` - successful login

                    - ``failure`` - login failure

                    - ``enabled_subaccount_login`` - login was enabled for
                    subaccount (in `data` - subaccount uid)

                    - ``disabled_subaccount_login`` - login was disabled for
                    subaccount (in `data` - subaccount uid)

                    - ``new_api_key`` - API key was created (in `data` key
                    client id)

                    - ``removed_api_key`` - API key was removed (in `data` key
                    client id)

                    - ``changed_scope`` - scope of API key was changed (in
                    `data` key client id)

                    - ``changed_whitelist`` - whitelist of API key was edited
                    (in `data` key client id)

                    - ``disabled_api_key`` - API key was disabled (in `data` key
                    client id)

                    - ``enabled_api_key`` - API key was enabled (in `data` key
                    client id)

                    - ``reset_api_key`` - API key was reset (in `data` key
                    client id)
                  type: string
                  x-parser-schema-id: <anonymous-schema-1476>
                data:
                  description: >-
                    Optional, additional information about action, type depends
                    on `log` value
                  type: *ref_0
                  x-parser-schema-id: <anonymous-schema-1477>
              required:
                - id
                - ip
                - timestamp
                - country
                - city
                - log
              x-parser-schema-id: <anonymous-schema-1470>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1469>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "timestamp": 1632488963633,
              "log": "success",
              "ip": "8.9.10.11",
              "id": 243343,
              "country": "China",
              "city": "Pekin"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_1
      - id: x-parser-unique-object-id
        value: user.access_log
  - &ref_2
    id: receive_user_access_log
    title: Receive user
    description: Client receives user notifications
    type: receive
    messages:
      - &ref_4
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
              x-parser-schema-id: <anonymous-schema-1463>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1464>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1465>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1468>
                  x-parser-schema-id: <anonymous-schema-1467>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1466>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1462>
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
                "user.access_log"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_1
sendOperations:
  - *ref_2
receiveOperations:
  - *ref_3
sendMessages:
  - *ref_4
receiveMessages:
  - *ref_5
extensions:
  - id: x-parser-unique-object-id
    value: user.access_log
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [private/get_access_log](https://docs.deribit.com/api-reference/account-management/private-get_access_log.md)
- [Access Scope](https://docs.deribit.com/articles/access-scope.md)
- [user.lock ](https://docs.deribit.com/subscriptions/user/userlock.md)