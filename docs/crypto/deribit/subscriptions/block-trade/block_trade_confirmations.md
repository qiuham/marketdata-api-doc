---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmations
api_type: WebSocket
updated_at: 2026-11-19 19:05:37.288063
---

# block_trade_confirmations

> Provides notifications regarding Block Trade approval. Subscribe to this channel to receive notifications about pending Block Trades that require your approval.

**📖 Related Article:** [Block Trading](https://docs.deribit.com/articles/block-trading-api)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json block_trade_confirmations
id: block_trade_confirmations
title: 'block_trade_confirmations '
description: >
  Provides notifications regarding Block Trade approval. Subscribe to this
  channel to receive notifications about pending Block Trades that require your
  approval.


  **📖 Related Article:** [Block
  Trading](https://docs.deribit.com/articles/block-trading-api)
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
address: block_trade_confirmations
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_block_trade_confirmations
    title: Send subscribe request
    description: Client sends subscription request for block_trade_confirmations
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
                  - name: nonce
                    type: string
                    description: >-
                      Nonce that can be used to approve or reject pending Block
                      Trade.
                    required: true
                  - name: timestamp
                    type: integer
                    description: >-
                      Timestamp that can be used to approve or reject pending
                      Block Trade.
                    required: true
                  - name: trades
                    type: array
                    required: true
                    properties:
                      - name: instrument_name
                        type: string
                        description: Unique instrument identifier
                        required: true
                      - name: direction
                        type: string
                        description: Trade direction of the maker
                        enumValues:
                          - buy
                          - sell
                        required: true
                      - name: price
                        type: number
                        description: The price of the trade
                        required: true
                      - name: amount
                        type: number
                        description: >-
                          Trade amount. For perpetual and inverse futures the
                          amount is in USD units. For options and linear futures
                          it is the underlying base currency coin.
                        required: true
                  - name: app_name
                    type: string
                    description: >-
                      The name of the application that executed the Block Trade
                      on behalf of the user (optional).
                    required: true
                  - name: username
                    type: string
                    description: Username of the user who initiated the Block Trade.
                    required: false
                  - name: role
                    type: string
                    description: 'Trade role of the user: `maker` or `taker`'
                    enumValues:
                      - maker
                      - taker
                    required: true
                  - name: user_id
                    type: integer
                    description: Unique user identifier
                    required: true
                  - name: broker_code
                    type: string
                    description: Broker code associated with the broker Block Trade.
                    required: false
                  - name: broker_name
                    type: string
                    description: Name of the broker associated with the Block Trade.
                    required: false
                  - name: state
                    type: object
                    description: State of the pending Block Trade for current user.
                    required: true
                    properties:
                      - name: value
                        type: string
                        description: State value.
                        enumValues:
                          - initial
                          - accepted
                          - rejected
                          - executed
                        required: true
                      - name: timestamp
                        type: integer
                        description: State timestamp.
                        required: true
                  - name: counterparty_state
                    type: object
                    description: >-
                      State of the pending Block Trade for the other party
                      (optional).
                    required: false
                    properties:
                      - name: value
                        type: string
                        description: State value.
                        enumValues:
                          - initial
                          - accepted
                          - rejected
                          - executed
                        required: true
                      - name: timestamp
                        type: integer
                        description: State timestamp.
                        required: true
                  - name: combo_id
                    type: string
                    description: Combo instrument identifier
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              type: object
              properties:
                nonce:
                  description: >-
                    Nonce that can be used to approve or reject pending Block
                    Trade.
                  type: string
                  example: bF1_gfgcsd
                  x-parser-schema-id: <anonymous-schema-273>
                timestamp:
                  description: >-
                    Timestamp that can be used to approve or reject pending
                    Block Trade.
                  type: integer
                  x-parser-schema-id: <anonymous-schema-274>
                trades:
                  type: array
                  items:
                    properties:
                      instrument_name:
                        type: string
                        description: Unique instrument identifier
                        example: BTC-PERPETUAL
                        x-parser-schema-id: <anonymous-schema-277>
                      direction:
                        type: string
                        description: Trade direction of the maker
                        enum:
                          - buy
                          - sell
                        x-parser-schema-id: <anonymous-schema-278>
                      price:
                        description: The price of the trade
                        type: number
                        x-parser-schema-id: <anonymous-schema-279>
                      amount:
                        description: >-
                          Trade amount. For perpetual and inverse futures the
                          amount is in USD units. For options and linear futures
                          it is the underlying base currency coin.
                        type: number
                        x-parser-schema-id: <anonymous-schema-280>
                    required:
                      - instrument_name
                      - direction
                      - price
                      - amount
                    type: object
                    x-parser-schema-id: <anonymous-schema-276>
                  x-parser-schema-id: <anonymous-schema-275>
                app_name:
                  description: >-
                    The name of the application that executed the Block Trade on
                    behalf of the user (optional).
                  type: string
                  example: Example Application
                  x-parser-schema-id: <anonymous-schema-281>
                username:
                  description: Username of the user who initiated the Block Trade.
                  type: string
                  example: Trader
                  x-parser-schema-id: <anonymous-schema-282>
                role:
                  description: 'Trade role of the user: `maker` or `taker`'
                  type: string
                  enum:
                    - maker
                    - taker
                  x-parser-schema-id: <anonymous-schema-283>
                user_id:
                  description: Unique user identifier
                  type: integer
                  example: 57874
                  x-parser-schema-id: <anonymous-schema-284>
                broker_code:
                  description: Broker code associated with the broker Block Trade.
                  type: string
                  example: jpqYKgg1
                  x-parser-schema-id: <anonymous-schema-285>
                broker_name:
                  description: Name of the broker associated with the Block Trade.
                  type: string
                  example: Test Broker
                  x-parser-schema-id: <anonymous-schema-286>
                state:
                  description: State of the pending Block Trade for current user.
                  type: object
                  properties:
                    value:
                      description: State value.
                      type: string
                      enum:
                        - initial
                        - accepted
                        - rejected
                        - executed
                      x-parser-schema-id: <anonymous-schema-288>
                    timestamp:
                      description: State timestamp.
                      type: integer
                      x-parser-schema-id: <anonymous-schema-289>
                  required:
                    - value
                    - timestamp
                  x-parser-schema-id: <anonymous-schema-287>
                counterparty_state:
                  description: >-
                    State of the pending Block Trade for the other party
                    (optional).
                  type: object
                  properties:
                    value:
                      description: State value.
                      type: string
                      enum:
                        - initial
                        - accepted
                        - rejected
                        - executed
                      x-parser-schema-id: <anonymous-schema-291>
                    timestamp:
                      description: State timestamp.
                      type: integer
                      x-parser-schema-id: <anonymous-schema-292>
                  required:
                    - value
                    - timestamp
                  x-parser-schema-id: <anonymous-schema-290>
                combo_id:
                  description: Combo instrument identifier
                  type: string
                  example: BTC-CS-27JUN25-80000_85000
                  x-parser-schema-id: <anonymous-schema-293>
              required:
                - nonce
                - timestamp
                - trades
                - app_name
                - role
                - user_id
                - state
              x-parser-schema-id: <anonymous-schema-272>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-271>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "nonce": "bt-jdqv98",
              "role": "maker",
              "user_id": 7,
              "state": {
                "value": "rejected",
                "timestamp": 1711468632693
              },
              "trades": [
                {
                  "instrument_name": "BTC-PERPETUAL",
                  "price": 70246.66,
                  "direction": "buy",
                  "amount": 10
                }
              ],
              "timestamp": 1711468468131
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: block_trade_confirmations
  - &ref_1
    id: receive_block_trade_confirmations
    title: Receive block_trade_confirmations
    description: Client receives block_trade_confirmations notifications
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
              x-parser-schema-id: <anonymous-schema-265>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-266>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-267>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-270>
                  x-parser-schema-id: <anonymous-schema-269>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-268>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-264>
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
                "block_trade_confirmations"
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
    value: block_trade_confirmations
securitySchemes: []

````

## Related topics

- [block_trade_confirmations.(currency) ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmationscurrency.md)
- [Voice Broker Trading API](https://docs.deribit.com/articles/voice-broker-trading-api.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Block Trading](https://docs.deribit.com/articles/block-trading-api.md)