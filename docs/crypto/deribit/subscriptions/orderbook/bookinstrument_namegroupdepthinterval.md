---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/orderbook/bookinstrument_namegroupdepthinterval
api_type: WebSocket
updated_at: 2026-11-28 18:58:38.573472
---

# book.(instrument_name).(group).(depth).(interval)

> Aggregated order book updates for a specific instrument.

Notifications are sent once per specified `interval`, with prices grouped (rounded) according to `group`, and the book truncated to the specified `depth` (number of price levels).

The `asks` and `bids` fields are both lists of `[price, amount]` pairs.

- `price`: price level, rounded according to `group` (USD per BTC)
- `amount`: total amount at that price level

For Starbase-routed instruments, the published price levels include accepted mass-quote liquidity.

**Units:** For perpetual and inverse futures the amount is in USD units. For options and linear futures it is in the underlying base currency coin.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json book.(instrument_name).(group).(depth).(interval)
id: book.(instrument_name).(group).(depth).(interval)
title: 'book.(instrument_name).(group).(depth).(interval) '
description: >
  Aggregated order book updates for a specific instrument.


  Notifications are sent once per specified `interval`, with prices grouped
  (rounded) according to `group`, and the book truncated to the specified
  `depth` (number of price levels).


  The `asks` and `bids` fields are both lists of `[price, amount]` pairs.


  - `price`: price level, rounded according to `group` (USD per BTC)

  - `amount`: total amount at that price level


  For Starbase-routed instruments, the published price levels include accepted
  mass-quote liquidity.


  **Units:** For perpetual and inverse futures the amount is in USD units. For
  options and linear futures it is in the underlying base currency coin.


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
address: book.(instrument_name).(group).(depth).(interval)
parameters:
  - id: instrument_name
    jsonSchema:
      type: string
      description: Instrument name
    description: Instrument name
    type: string
    required: true
    deprecated: false
  - id: group
    jsonSchema:
      type: string
      description: >
        Group prices (by rounding). Use `none` for no grouping.


        For ETH cryptocurrency, the real `group` is divided by `100.0`. Example:
        a value of `5` means using `0.05`.


        Allowed values:


        - BTC: `none`, `1`, `2`, `5`, `10`

        - ETH: `none`, `5`, `10`, `25`, `100`, `250`
      enum:
        - none
        - '1'
        - '2'
        - '5'
        - '10'
        - '25'
        - '100'
        - '250'
    description: >
      Group prices (by rounding). Use `none` for no grouping.


      For ETH cryptocurrency, the real `group` is divided by `100.0`. Example: a
      value of `5` means using `0.05`.


      Allowed values:


      - BTC: `none`, `1`, `2`, `5`, `10`

      - ETH: `none`, `5`, `10`, `25`, `100`, `250`
    type: string
    required: true
    deprecated: false
  - id: depth
    jsonSchema:
      type: string
      description: Number of price levels to be included.
      enum:
        - '1'
        - '10'
        - '20'
    description: Number of price levels to be included.
    type: string
    required: true
    deprecated: false
  - id: interval
    jsonSchema:
      type: string
      description: >-
        Frequency of notifications. Events will be aggregated over this
        interval.


        Allowed values: `100ms`, `agg2`. The `raw` interval is not supported on
        this channel. For raw order book updates, use
        `book.{instrument_name}.raw` instead.
      enum:
        - 100ms
        - agg2
    description: >-
      Frequency of notifications. Events will be aggregated over this interval.


      Allowed values: `100ms`, `agg2`. The `raw` interval is not supported on
      this channel. For raw order book updates, use `book.{instrument_name}.raw`
      instead.
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_book_instrument_name_group_depth_interval
    title: Send subscribe request for order book
    description: Client sends subscription request for order book updates
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
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: true
                  - name: change_id
                    type: integer
                    description: id of the notification
                    required: true
                  - name: bids
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: List of bids (price-amount pairs)
                        required: false
                        properties:
                          - name: item
                            type: number
                            required: false
                  - name: asks
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: array
                        description: List of asks (price-amount pairs)
                        required: false
                        properties:
                          - name: item
                            type: number
                            required: false
                  - name: timestamp
                    type: integer
                    description: >-
                      The timestamp of last change (milliseconds since the Unix
                      epoch)
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-79>
                change_id:
                  description: id of the notification
                  type: integer
                  x-parser-schema-id: <anonymous-schema-80>
                bids:
                  type: array
                  items:
                    type: array
                    items:
                      type: number
                      x-parser-schema-id: <anonymous-schema-83>
                    minItems: 2
                    maxItems: 2
                    description: List of bids (price-amount pairs)
                    x-parser-schema-id: <anonymous-schema-82>
                  x-parser-schema-id: <anonymous-schema-81>
                asks:
                  type: array
                  items:
                    type: array
                    items:
                      type: number
                      x-parser-schema-id: <anonymous-schema-86>
                    minItems: 2
                    maxItems: 2
                    description: List of asks (price-amount pairs)
                    x-parser-schema-id: <anonymous-schema-85>
                  x-parser-schema-id: <anonymous-schema-84>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: >-
                    The timestamp of last change (milliseconds since the Unix
                    epoch)
                  x-parser-schema-id: <anonymous-schema-87>
              required:
                - instrument_name
                - change_id
                - asks
                - bids
              type: object
              x-parser-schema-id: <anonymous-schema-78>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-77>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "timestamp": 1554375447971,
              "instrument_name": "ETH-PERPETUAL",
              "change_id": 109615,
              "bids": [
                [
                  160,
                  40
                ]
              ],
              "asks": [
                [
                  161,
                  20
                ]
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: book.(instrument_name).(group).(depth).(interval)
  - &ref_1
    id: receive_book_instrument_name_group_depth_interval_updates
    title: Receive order book updates
    description: Client receives order book update notifications
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
              x-parser-schema-id: <anonymous-schema-71>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-72>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-73>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-76>
                  x-parser-schema-id: <anonymous-schema-75>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-74>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-70>
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
                "book.BTC-PERPETUAL.10.20.100ms"
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
    value: book.(instrument_name).(group).(depth).(interval)
securitySchemes: []

````

## Related topics

- [book.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_nameinterval.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [quote.(instrument_name) ](https://docs.deribit.com/subscriptions/market-data/quoteinstrument_name.md)