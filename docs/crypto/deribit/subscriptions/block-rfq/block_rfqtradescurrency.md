---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/block-rfq/block_rfqtradescurrency
api_type: WebSocket
updated_at: 2026-11-22 18:59:23.294616
---

# block_rfq.trades.(currency)

> Get notifications about recent Block RFQ trades. This is a public channel that provides market data about completed Block RFQ trades.

Block RFQs whose trades have delayed publication are sent when they are published.

**📖 Related Article:** [Deribit Block RFQ API walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json block_rfq.trades.(currency)
id: block_rfq.trades.(currency)
title: 'block_rfq.trades.(currency) '
description: >
  Get notifications about recent Block RFQ trades. This is a public channel that
  provides market data about completed Block RFQ trades.


  Block RFQs whose trades have delayed publication are sent when they are
  published.


  **📖 Related Article:** [Deribit Block RFQ API
  walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough)
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
address: block_rfq.trades.(currency)
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
    id: send_subscribe_block_rfq_trades_currency
    title: Send subscribe request for block_rfq
    description: Client sends subscription request for block_rfq updates
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
                type: array
                required: true
                properties:
                  - name: id
                    type: integer
                    description: ID of the Block RFQ
                    required: false
                  - name: timestamp
                    type: integer
                    description: >-
                      The timestamp of the trade (milliseconds since the UNIX
                      epoch)
                    required: false
                  - name: direction
                    type: string
                    description: Trade direction of the taker
                    enumValues:
                      - buy
                      - sell
                    required: false
                  - name: amount
                    type: number
                    description: >-
                      This value multiplied by the ratio of a leg gives trade
                      size on that leg.
                    required: false
                  - name: mark_price
                    type: number
                    description: Mark Price at the moment of trade
                    required: false
                  - name: legs
                    type: array
                    required: false
                    properties:
                      - name: ratio
                        type: integer
                        description: Ratio of amount between legs
                        required: false
                      - name: instrument_name
                        type: string
                        description: Unique instrument identifier
                        required: false
                      - name: direction
                        type: string
                        description: 'Direction: `buy`, or `sell`'
                        enumValues:
                          - buy
                          - sell
                        required: false
                      - name: price
                        type: number
                        description: Price for a leg
                        required: false
                  - name: combo_id
                    type: string
                    description: Unique combo identifier
                    required: false
                  - name: hedge
                    type: object
                    required: false
                    properties:
                      - name: amount
                        type: integer
                        description: >-
                          It represents the requested hedge leg size. For
                          perpetual and inverse futures the amount is in USD
                          units. For options and linear futures it is the
                          underlying base currency coin.
                        required: false
                      - name: instrument_name
                        type: string
                        description: Unique instrument identifier
                        required: false
                      - name: direction
                        type: string
                        description: 'Direction: `buy`, or `sell`'
                        enumValues:
                          - buy
                          - sell
                        required: false
                      - name: price
                        type: number
                        description: Price for a hedge leg
                        required: false
                  - name: trades
                    type: array
                    required: false
                    properties:
                      - name: direction
                        type: string
                        description: 'Direction: `buy`, or `sell`'
                        enumValues:
                          - buy
                          - sell
                        required: false
                      - name: price
                        type: number
                        description: >-
                          Price in the instrument's price units (quote currency
                          for futures and spot).
                        required: false
                      - name: amount
                        type: number
                        description: >-
                          Trade amount. For options, linear futures, linear
                          perpetuals and spots the amount is denominated in the
                          underlying base currency coin. The inverse perpetuals
                          and inverse futures are denominated in USD units.
                        required: false
                      - name: hedge_amount
                        type: number
                        description: >-
                          Amount of the hedge leg. For linear futures, linear
                          perpetuals and spots the amount is denominated in the
                          underlying base currency coin. The inverse perpetuals
                          and inverse futures are denominated in USD units.
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: ID of the Block RFQ
                    x-parser-schema-id: <anonymous-schema-1728>
                  timestamp:
                    description: >-
                      The timestamp of the trade (milliseconds since the UNIX
                      epoch)
                    example: 1517329113791
                    type: integer
                    x-parser-schema-id: <anonymous-schema-1729>
                  direction:
                    type: string
                    description: Trade direction of the taker
                    enum:
                      - buy
                      - sell
                    x-parser-schema-id: <anonymous-schema-1730>
                  amount:
                    description: >-
                      This value multiplied by the ratio of a leg gives trade
                      size on that leg.
                    type: number
                    x-parser-schema-id: <anonymous-schema-1731>
                  mark_price:
                    description: Mark Price at the moment of trade
                    type: number
                    x-parser-schema-id: <anonymous-schema-1732>
                  legs:
                    type: array
                    items:
                      type: object
                      properties:
                        ratio:
                          description: Ratio of amount between legs
                          type: integer
                          x-parser-schema-id: <anonymous-schema-1735>
                        instrument_name:
                          type: string
                          description: Unique instrument identifier
                          example: BTC-PERPETUAL
                          x-parser-schema-id: <anonymous-schema-1736>
                        direction:
                          type: string
                          description: 'Direction: `buy`, or `sell`'
                          enum:
                            - buy
                            - sell
                          x-parser-schema-id: <anonymous-schema-1737>
                        price:
                          description: Price for a leg
                          type: number
                          x-parser-schema-id: <anonymous-schema-1738>
                      x-parser-schema-id: <anonymous-schema-1734>
                    x-parser-schema-id: <anonymous-schema-1733>
                  combo_id:
                    type: string
                    description: Unique combo identifier
                    example: BTC-FS-31DEC21-PERP
                    x-parser-schema-id: <anonymous-schema-1739>
                  hedge:
                    type: object
                    properties:
                      amount:
                        description: >-
                          It represents the requested hedge leg size. For
                          perpetual and inverse futures the amount is in USD
                          units. For options and linear futures it is the
                          underlying base currency coin.
                        type: integer
                        x-parser-schema-id: <anonymous-schema-1741>
                      instrument_name:
                        type: string
                        description: Unique instrument identifier
                        example: BTC-PERPETUAL
                        x-parser-schema-id: <anonymous-schema-1742>
                      direction:
                        type: string
                        description: 'Direction: `buy`, or `sell`'
                        enum:
                          - buy
                          - sell
                        x-parser-schema-id: <anonymous-schema-1743>
                      price:
                        description: Price for a hedge leg
                        type: number
                        x-parser-schema-id: <anonymous-schema-1744>
                    x-parser-schema-id: <anonymous-schema-1740>
                  trades:
                    type: array
                    items:
                      type: object
                      properties:
                        direction:
                          type: string
                          description: 'Direction: `buy`, or `sell`'
                          enum:
                            - buy
                            - sell
                          x-parser-schema-id: <anonymous-schema-1747>
                        price:
                          description: >-
                            Price in the instrument's price units (quote
                            currency for futures and spot).
                          type: number
                          x-parser-schema-id: <anonymous-schema-1748>
                        amount:
                          description: >-
                            Trade amount. For options, linear futures, linear
                            perpetuals and spots the amount is denominated in
                            the underlying base currency coin. The inverse
                            perpetuals and inverse futures are denominated in
                            USD units.
                          type: number
                          x-parser-schema-id: <anonymous-schema-1749>
                        hedge_amount:
                          type: number
                          description: >-
                            Amount of the hedge leg. For linear futures, linear
                            perpetuals and spots the amount is denominated in
                            the underlying base currency coin. The inverse
                            perpetuals and inverse futures are denominated in
                            USD units.
                          x-parser-schema-id: <anonymous-schema-1750>
                      x-parser-schema-id: <anonymous-schema-1746>
                    x-parser-schema-id: <anonymous-schema-1745>
                x-parser-schema-id: <anonymous-schema-1727>
              x-parser-schema-id: <anonymous-schema-1726>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1725>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "id": 939,
              "timestamp": 1739869829823,
              "amount": 50,
              "direction": "sell",
              "combo_id": "BTC-PERPETUAL",
              "legs": [
                {
                  "direction": "buy",
                  "price": 95318.72,
                  "instrument_name": "BTC-PERPETUAL",
                  "ratio": 1
                }
              ],
              "trades": [
                {
                  "amount": 50,
                  "direction": "sell",
                  "price": 95318.72
                }
              ],
              "mark_price": 95318.72
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: block_rfq.trades.(currency)
  - &ref_1
    id: receive_block_rfq_trades_currency_updates
    title: Receive block_rfq updates
    description: Client receives block_rfq update notifications
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
              x-parser-schema-id: <anonymous-schema-1719>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1720>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1721>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1724>
                  x-parser-schema-id: <anonymous-schema-1723>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1722>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1718>
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
                "block_rfq.trades.BTC"
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
    value: block_rfq.trades.(currency)
securitySchemes: []

````

## Related topics

- [Deribit Block RFQ API Walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Trades](https://docs.deribit.com/starbase/trades.md)
- [block_rfq.maker.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakercurrency.md)