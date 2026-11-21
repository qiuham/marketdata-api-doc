---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/charttradesinstrument_nameresolution
api_type: WebSocket
updated_at: 2026-11-21 19:01:35.089907
---

# chart.trades.(instrument_name).(resolution)

> Publicly available market data used to generate a TradingView trade candle chart.

During a single resolution period, many events can be sent, each with updated values for the recent period.

**Notice:** When there is no trade during the requested resolution period (e.g. 1 minute), a filling sample is generated which uses data from the last available trade candle (open and close values).

**Note:** For spot instruments routed to Coinbase Exchange, this channel is not supported. Use [Get product candles](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles) instead.

**📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json chart.trades.(instrument_name).(resolution)
id: chart.trades.(instrument_name).(resolution)
title: 'chart.trades.(instrument_name).(resolution) '
description: >
  Publicly available market data used to generate a TradingView trade candle
  chart.


  During a single resolution period, many events can be sent, each with updated
  values for the recent period.


  **Notice:** When there is no trade during the requested resolution period
  (e.g. 1 minute), a filling sample is generated which uses data from the last
  available trade candle (open and close values).


  **Note:** For spot instruments routed to Coinbase Exchange, this channel is
  not supported. Use [Get product
  candles](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles)
  instead.


  **📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed
  Instruments](https://docs.deribit.com/articles/spot-trading-venues)
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
address: chart.trades.(instrument_name).(resolution)
parameters:
  - id: instrument_name
    jsonSchema:
      type: string
      description: Instrument name
    description: Instrument name
    type: string
    required: true
    deprecated: false
  - id: resolution
    jsonSchema:
      type: string
      description: Chart bars resolution in minutes, or `1D` / `D` for daily bars.
      enum:
        - '1'
        - '3'
        - '5'
        - '10'
        - '15'
        - '30'
        - '60'
        - '120'
        - '180'
        - '360'
        - '720'
        - 1D
        - D
    description: Chart bars resolution in minutes, or `1D` / `D` for daily bars.
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_chart_trades_instrument_name_resolution
    title: Send subscribe request for chart
    description: Client sends subscription request for chart updates
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
                  - name: tick
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
                  - name: volume
                    type: number
                    description: Volume data for the candle
                    required: true
                  - name: cost
                    type: number
                    description: Cost data for the candle
                    required: true
                  - name: open
                    type: number
                    description: The open price for the candle'
                    required: true
                  - name: close
                    type: number
                    description: The close price for the candle
                    required: true
                  - name: high
                    type: number
                    description: The highest price level for the candle
                    required: true
                  - name: low
                    type: number
                    description: The lowest price level for the candle
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                tick:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-460>
                volume:
                  description: Volume data for the candle
                  type: number
                  x-parser-schema-id: <anonymous-schema-461>
                cost:
                  description: Cost data for the candle
                  type: number
                  x-parser-schema-id: <anonymous-schema-462>
                open:
                  description: The open price for the candle'
                  type: number
                  x-parser-schema-id: <anonymous-schema-463>
                close:
                  description: The close price for the candle
                  type: number
                  x-parser-schema-id: <anonymous-schema-464>
                high:
                  description: The highest price level for the candle
                  type: number
                  x-parser-schema-id: <anonymous-schema-465>
                low:
                  description: The lowest price level for the candle
                  type: number
                  x-parser-schema-id: <anonymous-schema-466>
              required:
                - tick
                - volume
                - cost
                - open
                - close
                - high
                - low
              type: object
              x-parser-schema-id: <anonymous-schema-459>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-458>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "volume": 0.05219351,
              "tick": 1573645080000,
              "open": 8869.79,
              "low": 8788.25,
              "high": 8870.31,
              "cost": 460,
              "close": 8791.25
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: chart.trades.(instrument_name).(resolution)
  - &ref_1
    id: receive_chart_trades_instrument_name_resolution_updates
    title: Receive chart updates
    description: Client receives chart update notifications
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
              x-parser-schema-id: <anonymous-schema-452>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-453>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-454>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-457>
                  x-parser-schema-id: <anonymous-schema-456>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-455>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-451>
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
                "chart.trades.BTC-PERPETUAL.60"
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
    value: chart.trades.(instrument_name).(resolution)
securitySchemes: []

````

## Related topics

- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/trades/tradesinstrument_nameinterval.md)