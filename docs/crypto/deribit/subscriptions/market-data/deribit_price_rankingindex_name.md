---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/deribit_price_rankingindex_name
api_type: WebSocket
updated_at: 2026-11-22 18:59:22.352044
---

# deribit_price_ranking.(index_name)

> Price ranking updates for the component exchanges used to calculate the Deribit index.

Use this channel to see per-exchange price contributions that feed into the index calculation for the given `index_name`.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json deribit_price_ranking.(index_name)
id: deribit_price_ranking.(index_name)
title: 'deribit_price_ranking.(index_name) '
description: >
  Price ranking updates for the component exchanges used to calculate the
  Deribit index.


  Use this channel to see per-exchange price contributions that feed into the
  index calculation for the given `index_name`.
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
address: deribit_price_ranking.(index_name)
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
    id: send_subscribe_deribit_price_ranking_index_name
    title: Send subscribe request for deribit_price_ranking
    description: Client sends subscription request for deribit_price_ranking updates
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
                  - name: identifier
                    type: string
                    description: Stock exchange identifier
                    required: false
                  - name: enabled
                    type: boolean
                    description: Stock exchange status
                    required: false
                  - name: original_price
                    type: number
                    description: Index price retrieved from stock's data
                    required: false
                  - name: price
                    type: number
                    description: >-
                      Adjusted stock exchange index price, used for Deribit
                      price index calculations
                    required: false
                  - name: timestamp
                    type: integer
                    description: >-
                      The timestamp of the last update from stock exchange
                      (milliseconds since the UNIX epoch)
                    required: false
                  - name: weight
                    type: number
                    description: The weight of the ranking given in percent
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              type: array
              items:
                properties:
                  identifier:
                    description: Stock exchange identifier
                    type: string
                    example: binance
                    x-parser-schema-id: <anonymous-schema-385>
                  enabled:
                    description: Stock exchange status
                    type: boolean
                    x-parser-schema-id: <anonymous-schema-386>
                  original_price:
                    description: Index price retrieved from stock's data
                    type: number
                    x-parser-schema-id: <anonymous-schema-387>
                  price:
                    description: >-
                      Adjusted stock exchange index price, used for Deribit
                      price index calculations
                    type: number
                    x-parser-schema-id: <anonymous-schema-388>
                  timestamp:
                    description: >-
                      The timestamp of the last update from stock exchange
                      (milliseconds since the UNIX epoch)
                    type: integer
                    example: 1536569522277
                    x-parser-schema-id: <anonymous-schema-389>
                  weight:
                    description: The weight of the ranking given in percent
                    type: number
                    x-parser-schema-id: <anonymous-schema-390>
                type: object
                x-parser-schema-id: <anonymous-schema-384>
              x-parser-schema-id: <anonymous-schema-383>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-382>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": [
              {
                "weight": 16.666667,
                "original_price": 41160.5,
                "price": 41160.5,
                "identifier": "bitfinex",
                "timestamp": 1702465142997,
                "enabled": true
              },
              {
                "weight": 16.666667,
                "original_price": 41119,
                "price": 41119,
                "identifier": "binance",
                "timestamp": 1702465143045,
                "enabled": true
              },
              {
                "weight": 16.666667,
                "original_price": 41115.53,
                "price": 41115.53,
                "identifier": "coinbase",
                "timestamp": 1702465139000,
                "enabled": true
              },
              {
                "weight": 16.666667,
                "original_price": 41116.42,
                "price": 41116.42,
                "identifier": "gemini",
                "timestamp": 1702465142921,
                "enabled": true
              },
              {
                "weight": 16.666667,
                "original_price": 41108.88,
                "price": 41108.88,
                "identifier": "itbit",
                "timestamp": 1702465141954,
                "enabled": true
              },
              {
                "weight": 16.666667,
                "original_price": 41108.35,
                "price": 41108.35,
                "identifier": "kraken",
                "timestamp": 1702465142906,
                "enabled": true
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
        value: deribit_price_ranking.(index_name)
  - &ref_1
    id: receive_deribit_price_ranking_index_name_updates
    title: Receive deribit_price_ranking updates
    description: Client receives deribit_price_ranking update notifications
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
              x-parser-schema-id: <anonymous-schema-376>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-377>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-378>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-381>
                  x-parser-schema-id: <anonymous-schema-380>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-379>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-375>
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
                "deribit_price_ranking.btc_usd"
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
    value: deribit_price_ranking.(index_name)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [deribit_price_index.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_indexindex_name.md)
- [deribit_price_statistics.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_statisticsindex_name.md)
- [estimated_expiration_price.(index_name) ](https://docs.deribit.com/subscriptions/market-data/estimated_expiration_priceindex_name.md)