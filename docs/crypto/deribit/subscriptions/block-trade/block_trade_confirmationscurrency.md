---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmationscurrency
api_type: WebSocket
updated_at: 2026-11-22 18:59:22.628856
---

# block_trade_confirmations.(currency)

> Provides notifications regarding Block Trade approval. Supports filtering by currency. Subscribe to this channel to receive notifications about pending Block Trades that require your approval, filtered by a specific currency.

**📖 Related Article:** [Block Trading](https://docs.deribit.com/articles/block-trading-api)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json block_trade_confirmations.(currency)
id: block_trade_confirmations.(currency)
title: 'block_trade_confirmations.(currency) '
description: >
  Provides notifications regarding Block Trade approval. Supports filtering by
  currency. Subscribe to this channel to receive notifications about pending
  Block Trades that require your approval, filtered by a specific currency.


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
address: block_trade_confirmations.(currency)
parameters:
  - id: currency
    jsonSchema:
      type: string
      description: >
        The currency symbol or `"any"` for all.


        **📖 Related Article:** [Using the currency
        Parameter](https://docs.deribit.com/articles/currency-parameter)
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
        - any
    description: >
      The currency symbol or `"any"` for all.


      **📖 Related Article:** [Using the currency
      Parameter](https://docs.deribit.com/articles/currency-parameter)
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_block_trade_confirmations_currency
    title: Send subscribe request for block_trade_confirmations
    description: Client sends subscription request for block_trade_confirmations updates
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
                  x-parser-schema-id: <anonymous-schema-304>
                timestamp:
                  description: >-
                    Timestamp that can be used to approve or reject pending
                    Block Trade.
                  type: integer
                  x-parser-schema-id: <anonymous-schema-305>
                trades:
                  type: array
                  items:
                    properties:
                      instrument_name:
                        type: string
                        description: Unique instrument identifier
                        example: BTC-PERPETUAL
                        x-parser-schema-id: <anonymous-schema-308>
                      direction:
                        type: string
                        description: Trade direction of the maker
                        enum:
                          - buy
                          - sell
                        x-parser-schema-id: <anonymous-schema-309>
                      price:
                        description: The price of the trade
                        type: number
                        x-parser-schema-id: <anonymous-schema-310>
                      amount:
                        description: >-
                          Trade amount. For perpetual and inverse futures the
                          amount is in USD units. For options and linear futures
                          it is the underlying base currency coin.
                        type: number
                        x-parser-schema-id: <anonymous-schema-311>
                    required:
                      - instrument_name
                      - direction
                      - price
                      - amount
                    type: object
                    x-parser-schema-id: <anonymous-schema-307>
                  x-parser-schema-id: <anonymous-schema-306>
                app_name:
                  description: >-
                    The name of the application that executed the Block Trade on
                    behalf of the user (optional).
                  type: string
                  example: Example Application
                  x-parser-schema-id: <anonymous-schema-312>
                username:
                  description: Username of the user who initiated the Block Trade.
                  type: string
                  example: Trader
                  x-parser-schema-id: <anonymous-schema-313>
                role:
                  description: 'Trade role of the user: `maker` or `taker`'
                  type: string
                  enum:
                    - maker
                    - taker
                  x-parser-schema-id: <anonymous-schema-314>
                user_id:
                  description: Unique user identifier
                  type: integer
                  example: 57874
                  x-parser-schema-id: <anonymous-schema-315>
                broker_code:
                  description: Broker code associated with the broker Block Trade.
                  type: string
                  example: jpqYKgg1
                  x-parser-schema-id: <anonymous-schema-316>
                broker_name:
                  description: Name of the broker associated with the Block Trade.
                  type: string
                  example: Test Broker
                  x-parser-schema-id: <anonymous-schema-317>
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
                      x-parser-schema-id: <anonymous-schema-319>
                    timestamp:
                      description: State timestamp.
                      type: integer
                      x-parser-schema-id: <anonymous-schema-320>
                  required:
                    - value
                    - timestamp
                  x-parser-schema-id: <anonymous-schema-318>
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
                      x-parser-schema-id: <anonymous-schema-322>
                    timestamp:
                      description: State timestamp.
                      type: integer
                      x-parser-schema-id: <anonymous-schema-323>
                  required:
                    - value
                    - timestamp
                  x-parser-schema-id: <anonymous-schema-321>
                combo_id:
                  description: Combo instrument identifier
                  type: string
                  example: BTC-CS-27JUN25-80000_85000
                  x-parser-schema-id: <anonymous-schema-324>
              required:
                - nonce
                - timestamp
                - trades
                - app_name
                - role
                - user_id
                - state
              x-parser-schema-id: <anonymous-schema-303>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-302>
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
        value: block_trade_confirmations.(currency)
  - &ref_1
    id: receive_block_trade_confirmations_currency_updates
    title: Receive block_trade_confirmations updates
    description: Client receives block_trade_confirmations update notifications
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
              x-parser-schema-id: <anonymous-schema-296>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-297>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-298>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-301>
                  x-parser-schema-id: <anonymous-schema-300>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-299>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-295>
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
                "block_trade_confirmations.BTC"
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
    value: block_trade_confirmations.(currency)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [block_trade_confirmations ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmations.md)
- [block_rfq.trades.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqtradescurrency.md)
- [Block Trading](https://docs.deribit.com/articles/block-trading-api.md)