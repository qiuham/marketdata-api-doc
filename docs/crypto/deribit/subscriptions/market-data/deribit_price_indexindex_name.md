---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/deribit_price_indexindex_name
api_type: WebSocket
updated_at: 2026-11-26 19:02:01.971272
---

# deribit_price_index.(index_name)

> Deribit index price updates for the given `index_name` (current index value).

Use this channel to track the real-time value of a Deribit index (e.g., `btc_usd`), which is used across pricing, margining, and settlement-related calculations.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json deribit_price_index.(index_name)
id: deribit_price_index.(index_name)
title: 'deribit_price_index.(index_name) '
description: >
  Deribit index price updates for the given `index_name` (current index value).


  Use this channel to track the real-time value of a Deribit index (e.g.,
  `btc_usd`), which is used across pricing, margining, and settlement-related
  calculations.
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
address: deribit_price_index.(index_name)
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
    id: send_subscribe_deribit_price_index_index_name
    title: Send subscribe request for deribit_price_index
    description: Client sends subscription request for deribit_price_index updates
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
                    required: true
                  - name: price
                    type: number
                    description: Current index price
                    required: true
                  - name: index_name
                    type: string
                    description: >-
                      Index identifier, matches (base) cryptocurrency with quote
                      currency
                    enumValues:
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
                    required: true
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
                  x-parser-schema-id: <anonymous-schema-371>
                price:
                  description: Current index price
                  type: number
                  example: 8247.27
                  x-parser-schema-id: <anonymous-schema-372>
                index_name:
                  description: >-
                    Index identifier, matches (base) cryptocurrency with quote
                    currency
                  type: string
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
                  x-parser-schema-id: <anonymous-schema-373>
              required:
                - timestamp
                - price
                - index_name
              type: object
              x-parser-schema-id: <anonymous-schema-370>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-369>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "index_name": "btc_usd",
              "price": 3937.89,
              "timestamp": 1550588002899
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: deribit_price_index.(index_name)
  - &ref_1
    id: receive_deribit_price_index_index_name_updates
    title: Receive deribit_price_index updates
    description: Client receives deribit_price_index update notifications
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
              x-parser-schema-id: <anonymous-schema-363>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-364>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-365>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-368>
                  x-parser-schema-id: <anonymous-schema-367>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-366>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-362>
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
                "deribit_price_index.btc_usd"
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
    value: deribit_price_index.(index_name)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [Starbase Reference Data and Instrument Definitions](https://docs.deribit.com/starbase/reference-data.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)
- [deribit_price_ranking.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_rankingindex_name.md)