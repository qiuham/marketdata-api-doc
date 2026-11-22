---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/instrumentstatekindcurrency
api_type: WebSocket
updated_at: 2026-11-22 18:59:22.490619
---

# instrument.state.(kind).(currency)

> Notifications about new or terminated instruments of a given kind in a given currency.

Use this channel to track instrument lifecycle events (new listings, expirations/terminations) without polling.

**Note:** Our system does not send notifications when currencies are locked. Users are advised to subscribe to the [platform_state](https://docs.deribit.com/subscriptions/platform/platform_state) channel to monitor the state of currencies actively.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json instrument.state.(kind).(currency)
id: instrument.state.(kind).(currency)
title: 'instrument.state.(kind).(currency) '
description: >
  Notifications about new or terminated instruments of a given kind in a given
  currency.


  Use this channel to track instrument lifecycle events (new listings,
  expirations/terminations) without polling.


  **Note:** Our system does not send notifications when currencies are locked.
  Users are advised to subscribe to the
  [platform_state](https://docs.deribit.com/subscriptions/platform/platform_state)
  channel to monitor the state of currencies actively.


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
address: instrument.state.(kind).(currency)
parameters:
  - id: kind
    jsonSchema:
      type: string
      description: Instrument kind or `"any"` for all
      enum:
        - future
        - option
        - spot
        - future_combo
        - option_combo
        - any
    description: Instrument kind or `"any"` for all
    type: string
    required: true
    deprecated: false
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
    id: send_subscribe_instrument_state_kind_currency
    title: Send subscribe request for instrument
    description: Client sends subscription request for instrument updates
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
                    required: false
                  - name: state
                    type: string
                    description: >
                      The state of the order book. Represents the current
                      lifecycle stage of the instrument.


                      **State Lifecycle and Meanings:**


                      - `open`: Default state for running books. In this state
                      book is accepting new orders, edits, cancels; prices
                      should be updated, trading is live.

                      - `settlement`: Books enters to this state during
                      settlement/delivery. New orders, edits, cancels are not
                      accepted. After this state normally next state should be
                      `open` if it was settlement, or `delivered` if it was
                      delivery. On enter to this state good till day orders in
                      book are canceled.

                      - `delivered`: Final state of book that has been
                      delivered. New orders, edits, cancels are not accepted.
                      After some time book process will be terminated and,
                      instrument moved to `expired_instruments` and its
                      `instrument_state` will become archivized. On enter to
                      this all open orders in book are canceled.

                      - `inactive`: After a book is deactivated, this state is
                      set on book. New orders, edits, cancels are not accepted.
                      On enter to this all open orders in book are canceled.
                      Book in this state is not considered as open. This can be
                      also final state for book.

                      - `locked`: New orders, edits, are not accepted, only
                      cancels ARE accepted. In some cases when configured books
                      can start as locked or it may become locked on admin
                      request. Settlement is possible on locked books.

                      - `halted`: The state that books enter as a result of an
                      error. Settlement is not possible when there is at least
                      one book in this state.

                      - `archivized`: Set when instrument is moved to
                      `expired_instruments` table, final state.
                    enumValues:
                      - open
                      - settlement
                      - delivered
                      - inactive
                      - locked
                      - halted
                      - archivized
                    required: false
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
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
                  x-parser-schema-id: <anonymous-schema-868>
                state:
                  description: >
                    The state of the order book. Represents the current
                    lifecycle stage of the instrument.


                    **State Lifecycle and Meanings:**


                    - `open`: Default state for running books. In this state
                    book is accepting new orders, edits, cancels; prices should
                    be updated, trading is live.

                    - `settlement`: Books enters to this state during
                    settlement/delivery. New orders, edits, cancels are not
                    accepted. After this state normally next state should be
                    `open` if it was settlement, or `delivered` if it was
                    delivery. On enter to this state good till day orders in
                    book are canceled.

                    - `delivered`: Final state of book that has been delivered.
                    New orders, edits, cancels are not accepted. After some time
                    book process will be terminated and, instrument moved to
                    `expired_instruments` and its `instrument_state` will become
                    archivized. On enter to this all open orders in book are
                    canceled.

                    - `inactive`: After a book is deactivated, this state is set
                    on book. New orders, edits, cancels are not accepted. On
                    enter to this all open orders in book are canceled. Book in
                    this state is not considered as open. This can be also final
                    state for book.

                    - `locked`: New orders, edits, are not accepted, only
                    cancels ARE accepted. In some cases when configured books
                    can start as locked or it may become locked on admin
                    request. Settlement is possible on locked books.

                    - `halted`: The state that books enter as a result of an
                    error. Settlement is not possible when there is at least one
                    book in this state.

                    - `archivized`: Set when instrument is moved to
                    `expired_instruments` table, final state.
                  type: string
                  enum:
                    - open
                    - settlement
                    - delivered
                    - inactive
                    - locked
                    - halted
                    - archivized
                  x-parser-schema-id: <anonymous-schema-869>
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-870>
              type: object
              x-parser-schema-id: <anonymous-schema-867>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-866>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "timestamp": 1553080940000,
              "state": "open",
              "instrument_name": "BTC-22MAR19"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: instrument.state.(kind).(currency)
  - &ref_1
    id: receive_instrument_state_kind_currency_updates
    title: Receive instrument updates
    description: Client receives instrument update notifications
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
              x-parser-schema-id: <anonymous-schema-860>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-861>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-862>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-865>
                  x-parser-schema-id: <anonymous-schema-864>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-863>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-859>
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
                "instrument.state.future.BTC"
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
    value: instrument.state.(kind).(currency)
securitySchemes: []

````

## Related topics

- [public/get_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)