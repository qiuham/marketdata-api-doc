---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/markpriceoptionsindex_name
api_type: WebSocket
updated_at: 2026-11-18 18:59:00.212418
---

# markprice.options.(index_name)

> Options mark price updates for the given `index_name`.

Use this channel to receive mark prices for options under the given index, useful for valuation, risk monitoring, and P&L calculations.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json markprice.options.(index_name)
id: markprice.options.(index_name)
title: 'markprice.options.(index_name) '
description: >
  Options mark price updates for the given `index_name`.


  Use this channel to receive mark prices for options under the given index,
  useful for valuation, risk monitoring, and P&L calculations.


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
address: markprice.options.(index_name)
parameters:
  - id: index_name
    jsonSchema:
      type: string
      description: Index identifier, matches (base) cryptocurrency with quote currency
      enum:
        - btc_usd
        - eth_usd
        - ada_usdc
        - algo_usdc
        - avax_usdc
        - bch_usdc
        - bnb_usdc
        - btc_usdc
        - btcdvol_usdc
        - buidl_usdc
        - doge_usdc
        - dot_usdc
        - eurr_usdc
        - eth_usdc
        - ethdvol_usdc
        - hype_usdc
        - link_usdc
        - ltc_usdc
        - near_usdc
        - paxg_usdc
        - shib_usdc
        - sol_usdc
        - steth_usdc
        - ton_usdc
        - trump_usdc
        - trx_usdc
        - uni_usdc
        - usde_usdc
        - usyc_usdc
        - xrp_usdc
        - btc_usdt
        - eth_usdt
        - eurr_usdt
        - sol_usdt
        - steth_usdt
        - usdc_usdt
        - usde_usdt
        - btc_eurr
        - btc_usde
        - btc_usyc
        - eth_btc
        - eth_eurr
        - eth_usde
        - eth_usyc
        - steth_eth
        - paxg_btc
        - drbfix-btc_usdc
        - drbfix-eth_usdc
    description: Index identifier, matches (base) cryptocurrency with quote currency
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_markprice_options_index_name
    title: Send subscribe request for markprice
    description: Client sends subscription request for markprice updates
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
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: false
                  - name: mark_price
                    type: number
                    description: The mark price for the instrument
                    required: false
                  - name: iv
                    type: number
                    description: Value of the volatility of the underlying instrument
                    required: false
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
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
                  instrument_name:
                    type: string
                    description: Unique instrument identifier
                    example: BTC-PERPETUAL
                    x-parser-schema-id: <anonymous-schema-430>
                  mark_price:
                    description: The mark price for the instrument
                    type: number
                    x-parser-schema-id: <anonymous-schema-431>
                  iv:
                    description: Value of the volatility of the underlying instrument
                    type: number
                    x-parser-schema-id: <anonymous-schema-432>
                  timestamp:
                    type: integer
                    example: 1536569522277
                    description: The timestamp (milliseconds since the Unix epoch)
                    x-parser-schema-id: <anonymous-schema-433>
                x-parser-schema-id: <anonymous-schema-429>
              x-parser-schema-id: <anonymous-schema-428>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-427>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": [
              {
                "timestamp": 1622470378005,
                "mark_price": 0.0333,
                "iv": 0.9,
                "instrument_name": "BTC-2JUN21-37000-P"
              },
              {
                "timestamp": 1622470378005,
                "mark_price": 0.117,
                "iv": 0.9,
                "instrument_name": "BTC-4JUN21-40500-P"
              },
              {
                "timestamp": 1622470378005,
                "mark_price": 0.0177,
                "iv": 0.9,
                "instrument_name": "BTC-4JUN21-38250-C"
              },
              {
                "timestamp": 1622470378005,
                "mark_price": 0.0098,
                "iv": 0.9,
                "instrument_name": "BTC-1JUN21-37000-C"
              },
              {
                "timestamp": 1622470378005,
                "mark_price": 0.0371,
                "iv": 0.9,
                "instrument_name": "BTC-4JUN21-36500-P"
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: markprice.options.(index_name)
  - &ref_1
    id: receive_markprice_options_index_name_updates
    title: Receive markprice updates
    description: Client receives markprice update notifications
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
              x-parser-schema-id: <anonymous-schema-421>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-422>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-423>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-426>
                  x-parser-schema-id: <anonymous-schema-425>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-424>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-420>
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
                "markprice.options.btc_usd"
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
    value: markprice.options.(index_name)
securitySchemes: []

````

## Related topics

- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [deribit_volatility_index.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_volatility_indexindex_name.md)
- [estimated_expiration_price.(index_name) ](https://docs.deribit.com/subscriptions/market-data/estimated_expiration_priceindex_name.md)