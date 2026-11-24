---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/deribit_price_statisticsindex_name
api_type: WebSocket
updated_at: 2026-11-24 18:59:42.624899
---

# deribit_price_statistics.(index_name)

> Basic statistics for the Deribit index.

Provides statistical information related to the given `index_name` (e.g., aggregated stats derived from index updates). Useful for monitoring index behavior over time.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json deribit_price_statistics.(index_name)
id: deribit_price_statistics.(index_name)
title: 'deribit_price_statistics.(index_name) '
description: >
  Basic statistics for the Deribit index.


  Provides statistical information related to the given `index_name` (e.g.,
  aggregated stats derived from index updates). Useful for monitoring index
  behavior over time.
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
address: deribit_price_statistics.(index_name)
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
    id: send_subscribe_deribit_price_statistics_index_name
    title: Send subscribe request for deribit_price_statistics
    description: Client sends subscription request for deribit_price_statistics updates
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
                  - name: low24h
                    type: number
                    description: The lowest recorded price within the last 24 hours
                    required: true
                  - name: high24h
                    type: number
                    description: The highest recorded price within the last 24 hours
                    required: true
                  - name: change24h
                    type: number
                    description: >-
                      The price index change calculated between the first and
                      last point within most recent 24 hours window
                    required: true
                  - name: fast_market
                    type: boolean
                    description: >-
                      Indicates the fast moving prices period on the market. The
                      value `true` is set when the price index value drastically
                      changed within the last 1 hour. This indicator remains
                      active even for 2 more hours after the prices calm down
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
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
                  x-parser-schema-id: <anonymous-schema-401>
                low24h:
                  type: number
                  description: The lowest recorded price within the last 24 hours
                  x-parser-schema-id: <anonymous-schema-402>
                high24h:
                  type: number
                  description: The highest recorded price within the last 24 hours
                  x-parser-schema-id: <anonymous-schema-403>
                change24h:
                  type: number
                  description: >-
                    The price index change calculated between the first and last
                    point within most recent 24 hours window
                  x-parser-schema-id: <anonymous-schema-404>
                fast_market:
                  type: boolean
                  description: >-
                    Indicates the fast moving prices period on the market. The
                    value `true` is set when the price index value drastically
                    changed within the last 1 hour. This indicator remains
                    active even for 2 more hours after the prices calm down
                  x-parser-schema-id: <anonymous-schema-405>
              required:
                - index_name
                - low24h
                - high24h
                - change24h
              type: object
              x-parser-schema-id: <anonymous-schema-400>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-399>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "low24h": 58012.08,
              "index_name": "btc_usd",
              "high24h": 59311.42,
              "change24h": 1009.61,
              "fast_market": false
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: deribit_price_statistics.(index_name)
  - &ref_1
    id: receive_deribit_price_statistics_index_name_updates
    title: Receive deribit_price_statistics updates
    description: Client receives deribit_price_statistics update notifications
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
              x-parser-schema-id: <anonymous-schema-393>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-394>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-395>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-398>
                  x-parser-schema-id: <anonymous-schema-397>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-396>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-392>
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
                "deribit_price_statistics.btc_usd"
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
    value: deribit_price_statistics.(index_name)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [deribit_price_index.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_indexindex_name.md)
- [deribit_price_ranking.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_rankingindex_name.md)
- [estimated_expiration_price.(index_name) ](https://docs.deribit.com/subscriptions/market-data/estimated_expiration_priceindex_name.md)