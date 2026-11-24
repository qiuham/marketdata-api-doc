---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/trades/tradesinstrument_nameinterval
api_type: WebSocket
updated_at: 2026-11-24 18:59:42.809806
---

# trades.(instrument_name).(interval)

> Trade notifications for a specific instrument.

Use this channel to receive executed trades as they happen for the given instrument. The `interval` controls how frequently trade events are aggregated.

**Note:** Block RFQ trades with delayed publication are sent when they are published (`block_delayed`), with their original `timestamp` and `trade_seq`, so they can arrive out of sequence.

**Note:** For spot instruments routed to Coinbase Exchange, this channel is not supported. Use the [`matches` channel](https://docs.cdp.coinbase.com/exchange/websocket-feed/channels) for the full trade tape. For user trades, orders and changes, use the `user` channels.

**📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json trades.(instrument_name).(interval)
id: trades.(instrument_name).(interval)
title: 'trades.(instrument_name).(interval) '
description: >
  Trade notifications for a specific instrument.


  Use this channel to receive executed trades as they happen for the given
  instrument. The `interval` controls how frequently trade events are
  aggregated.


  **Note:** Block RFQ trades with delayed publication are sent when they are
  published (`block_delayed`), with their original `timestamp` and `trade_seq`,
  so they can arrive out of sequence.


  **Note:** For spot instruments routed to Coinbase Exchange, this channel is
  not supported. Use the [`matches`
  channel](https://docs.cdp.coinbase.com/exchange/websocket-feed/channels) for
  the full trade tape. For user trades, orders and changes, use the `user`
  channels.


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
address: trades.(instrument_name).(interval)
parameters:
  - id: instrument_name
    jsonSchema:
      type: string
      description: Instrument name
    description: Instrument name
    type: string
    required: true
    deprecated: false
  - id: interval
    jsonSchema:
      type: string
      description: >-
        Notification interval. The raw interval selects unaggregated updates and
        is available only to authorized users.
      enum:
        - agg2
        - 100ms
        - raw
    description: >-
      Notification interval. The raw interval selects unaggregated updates and
      is available only to authorized users.
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_3
    id: send_subscribe_trades_instrument_name_interval
    title: Send subscribe request for trades
    description: Client sends subscription request for trades updates
    type: send
    messages:
      - &ref_5
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
                  - name: trade_id
                    type: string
                    description: Unique (per currency) trade identifier
                    required: true
                  - name: trade_seq
                    type: integer
                    description: The sequence number of the trade within instrument
                    required: true
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: true
                  - name: timestamp
                    type: integer
                    description: >-
                      The timestamp of the trade (milliseconds since the UNIX
                      epoch)
                    required: true
                  - name: starbase_timestamp
                    type: integer
                    description: >-
                      Optional field: the Starbase causal timestamp of the
                      trade, in nanoseconds since the UNIX epoch (present only
                      for trades matched in Starbase)
                    required: false
                  - name: direction
                    type: string
                    description: Trade direction of the taker
                    enumValues:
                      - buy
                      - sell
                    required: true
                  - name: tick_direction
                    type: integer
                    description: >-
                      Direction of the "tick" (`0` = Plus Tick, `1` = Zero-Plus
                      Tick, `2` = Minus Tick, `3` = Zero-Minus Tick).
                    enumValues:
                      - 0
                      - 1
                      - 2
                      - 3
                    required: true
                  - name: index_price
                    type: number
                    description: Index Price at the moment of trade
                    required: true
                  - name: price
                    type: number
                    description: The price of the trade
                    required: true
                  - name: amount
                    type: number
                    description: >-
                      Trade amount. For perpetual and inverse futures the amount
                      is in USD units. For options and linear futures it is the
                      underlying base currency coin.
                    required: true
                  - name: contracts
                    type: number
                    description: >-
                      Trade size in contract units (optional, may be absent in
                      historical trades)
                    required: false
                  - name: iv
                    type: number
                    description: Option implied volatility for the price (Option only)
                    required: false
                  - name: liquidation
                    type: string
                    description: >-
                      Optional field (only for trades caused by liquidation):
                      `"M"` when maker side of trade was under liquidation,
                      `"T"` when taker side was under liquidation, `"MT"` when
                      both sides of trade were under liquidation
                    enumValues:
                      - M
                      - T
                      - MT
                    required: false
                  - name: mark_price
                    type: &ref_0
                      - number
                      - 'null'
                    description: Mark Price at the moment of trade
                    required: true
                  - name: block_trade_id
                    type: string
                    description: >-
                      ID of the Block Trade or Block RFQ trade, when the trade
                      was part of one
                    required: false
                  - name: block_trade_leg_count
                    type: integer
                    description: >-
                      Number of legs in the Block Trade or Block RFQ trade, when
                      the trade was part of one
                    required: false
                  - name: block_delayed
                    type: integer
                    description: >-
                      Optional field (only for Block RFQ trades with delayed
                      publication): the time the trade is published to public
                      data feeds, in milliseconds since the UNIX epoch. Until
                      then, the trade is returned only to its counterparties and
                      is not included in public trades or the Block RFQ trade
                      tape. The trade never updates the ticker `last_price` or
                      tick direction, or the 24-hour `high`, `low` and
                      `price_change`; its volume is reported in
                      `volume_delayed`.
                    required: false
                  - name: combo_id
                    type: string
                    description: >-
                      Optional field containing combo instrument name if the
                      trade is a combo trade
                    required: false
                  - name: combo_trade_id
                    type: string
                    description: >-
                      Optional field containing combo trade identifier if the
                      trade is a combo trade
                    required: false
                  - name: starbase_match_id
                    type: integer
                    description: >-
                      Optional field containing the Starbase match identifier
                      (present only for trades matched via Starbase)
                    required: false
                  - name: block_rfq_id
                    type: integer
                    description: ID of the Block RFQ - when trade was part of the Block RFQ
                    required: false
                  - name: legs
                    type: array
                    description: Leg trades, present when querying only combo trades.
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                trade_id:
                  type: string
                  description: Unique (per currency) trade identifier
                  x-parser-schema-id: <anonymous-schema-241>
                trade_seq:
                  description: The sequence number of the trade within instrument
                  type: integer
                  x-parser-schema-id: <anonymous-schema-242>
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-243>
                timestamp:
                  description: >-
                    The timestamp of the trade (milliseconds since the UNIX
                    epoch)
                  example: 1517329113791
                  type: integer
                  x-parser-schema-id: <anonymous-schema-244>
                starbase_timestamp:
                  type: integer
                  example: 1536569522277000000
                  description: >-
                    Optional field: the Starbase causal timestamp of the trade,
                    in nanoseconds since the UNIX epoch (present only for trades
                    matched in Starbase)
                  x-parser-schema-id: <anonymous-schema-245>
                direction:
                  type: string
                  description: Trade direction of the taker
                  enum:
                    - buy
                    - sell
                  x-parser-schema-id: <anonymous-schema-246>
                tick_direction:
                  type: integer
                  enum:
                    - 0
                    - 1
                    - 2
                    - 3
                  description: >-
                    Direction of the "tick" (`0` = Plus Tick, `1` = Zero-Plus
                    Tick, `2` = Minus Tick, `3` = Zero-Minus Tick).
                  x-parser-schema-id: <anonymous-schema-247>
                index_price:
                  description: Index Price at the moment of trade
                  type: number
                  x-parser-schema-id: <anonymous-schema-248>
                price:
                  description: The price of the trade
                  type: number
                  x-parser-schema-id: <anonymous-schema-249>
                amount:
                  description: >-
                    Trade amount. For perpetual and inverse futures the amount
                    is in USD units. For options and linear futures it is the
                    underlying base currency coin.
                  type: number
                  x-parser-schema-id: <anonymous-schema-250>
                contracts:
                  description: >-
                    Trade size in contract units (optional, may be absent in
                    historical trades)
                  type: number
                  x-parser-schema-id: <anonymous-schema-251>
                iv:
                  description: Option implied volatility for the price (Option only)
                  type: number
                  x-parser-schema-id: <anonymous-schema-252>
                liquidation:
                  description: >-
                    Optional field (only for trades caused by liquidation):
                    `"M"` when maker side of trade was under liquidation, `"T"`
                    when taker side was under liquidation, `"MT"` when both
                    sides of trade were under liquidation
                  type: string
                  enum:
                    - M
                    - T
                    - MT
                  x-parser-schema-id: <anonymous-schema-253>
                mark_price:
                  description: Mark Price at the moment of trade
                  type: *ref_0
                  x-parser-schema-id: <anonymous-schema-254>
                block_trade_id:
                  description: >-
                    ID of the Block Trade or Block RFQ trade, when the trade was
                    part of one
                  type: string
                  example: '154'
                  x-parser-schema-id: <anonymous-schema-255>
                block_trade_leg_count:
                  description: >-
                    Number of legs in the Block Trade or Block RFQ trade, when
                    the trade was part of one
                  type: integer
                  example: 3
                  x-parser-schema-id: <anonymous-schema-256>
                block_delayed:
                  description: >-
                    Optional field (only for Block RFQ trades with delayed
                    publication): the time the trade is published to public data
                    feeds, in milliseconds since the UNIX epoch. Until then, the
                    trade is returned only to its counterparties and is not
                    included in public trades or the Block RFQ trade tape. The
                    trade never updates the ticker `last_price` or tick
                    direction, or the 24-hour `high`, `low` and `price_change`;
                    its volume is reported in `volume_delayed`.
                  type: integer
                  example: 1730827181502
                  x-parser-schema-id: <anonymous-schema-257>
                combo_id:
                  description: >-
                    Optional field containing combo instrument name if the trade
                    is a combo trade
                  type: string
                  x-parser-schema-id: <anonymous-schema-258>
                combo_trade_id:
                  description: >-
                    Optional field containing combo trade identifier if the
                    trade is a combo trade
                  type: string
                  x-parser-schema-id: <anonymous-schema-259>
                starbase_match_id:
                  description: >-
                    Optional field containing the Starbase match identifier
                    (present only for trades matched via Starbase)
                  type: integer
                  x-parser-schema-id: <anonymous-schema-260>
                block_rfq_id:
                  type: integer
                  description: ID of the Block RFQ - when trade was part of the Block RFQ
                  x-parser-schema-id: <anonymous-schema-261>
                legs:
                  type: array
                  description: Leg trades, present when querying only combo trades.
                  items:
                    x-parser-schema-id: <anonymous-schema-263>
                  x-parser-schema-id: <anonymous-schema-262>
              required:
                - trade_id
                - instrument_name
                - timestamp
                - trade_seq
                - direction
                - tick_direction
                - index_price
                - price
                - amount
                - mark_price
              type: object
              x-parser-schema-id: <anonymous-schema-240>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-239>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": [
              {
                "trade_seq": 30289442,
                "trade_id": "48079269",
                "timestamp": 1590484512188,
                "tick_direction": 2,
                "price": 8950,
                "mark_price": 8948.9,
                "instrument_name": "BTC-PERPETUAL",
                "index_price": 8955.88,
                "direction": "sell",
                "amount": 10,
                "contracts": 1
              },
              {
                "trade_seq": 30289443,
                "trade_id": "48079270",
                "timestamp": 1590484513004,
                "tick_direction": 0,
                "price": 8960,
                "mark_price": 8948.9,
                "instrument_name": "BTC-PERPETUAL",
                "index_price": 8955.88,
                "direction": "buy",
                "amount": 20,
                "contracts": 2,
                "liquidation": "T"
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_1
      - id: x-parser-unique-object-id
        value: trades.(instrument_name).(interval)
  - &ref_2
    id: receive_trades_instrument_name_interval_updates
    title: Receive trades updates
    description: Client receives trades update notifications
    type: receive
    messages:
      - &ref_4
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
              x-parser-schema-id: <anonymous-schema-233>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-234>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-235>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-238>
                  x-parser-schema-id: <anonymous-schema-237>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-236>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-232>
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
                "trades.BTC-PERPETUAL.100ms"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_1
sendOperations:
  - *ref_2
receiveOperations:
  - *ref_3
sendMessages:
  - *ref_4
receiveMessages:
  - *ref_5
extensions:
  - id: x-parser-unique-object-id
    value: trades.(instrument_name).(interval)
securitySchemes: []

````

## Related topics

- [user.trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/usertradesinstrument_nameinterval.md)
- [user.combo_trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/usercombo_tradesinstrument_nameinterval.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [user.trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/usertradeskindcurrencyinterval.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)