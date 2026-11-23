---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/user/usertradeskindcurrencyinterval
api_type: WebSocket
updated_at: 2026-11-23 19:00:30.963144
---

# user.trades.(kind).(currency).(interval)

> User trade notifications across all instruments for a given kind and currency.

Receive a consolidated stream of your private trades across all instruments matching the specified `kind` and `currency`. The `interval` controls aggregation frequency.

**Block RFQ trades:** Trades resulting from Block RFQ execution are included in this channel. See `user.trades.{instrument_name}.{interval}` for the complete list of Block RFQ-specific fields.


## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.trades.(kind).(currency).(interval)
id: user.trades.(kind).(currency).(interval)
title: 'user.trades.(kind).(currency).(interval) '
description: >
  User trade notifications across all instruments for a given kind and currency.


  Receive a consolidated stream of your private trades across all instruments
  matching the specified `kind` and `currency`. The `interval` controls
  aggregation frequency.


  **Block RFQ trades:** Trades resulting from Block RFQ execution are included
  in this channel. See `user.trades.{instrument_name}.{interval}` for the
  complete list of Block RFQ-specific fields.
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
address: user.trades.(kind).(currency).(interval)
parameters:
  - id: kind
    jsonSchema:
      type: string
      description: Instrument kind, `"combo"` for any combo or `"any"` for all
      enum:
        - future
        - option
        - spot
        - future_combo
        - option_combo
        - combo
        - any
    description: Instrument kind, `"combo"` for any combo or `"any"` for all
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
  - &ref_5
    id: send_subscribe_user_trades_kind_currency_interval
    title: Send subscribe request for user
    description: Client sends subscription request for user updates
    type: send
    messages:
      - &ref_7
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
                  - name: starbase_order_id
                    type: integer
                    description: >-
                      Raw Starbase order id of the user's order, in Starbase's
                      own (non currency-prefixed) id namespace (present only for
                      trades matched in Starbase)
                    required: false
                  - name: starbase_client_order_id
                    type: string
                    description: >-
                      Client order id of the user's own order (maker or taker
                      side) submitted directly to
                      [Starbase](https://docs.deribit.com/starbase/overview) via
                      direct access; not returned for orders placed through the
                      Deribit API; for self-trades this is the taker order's
                      client order id
                    required: false
                  - name: order_type
                    type: string
                    description: 'Order type: `"limit"`, `"market"`, or `"liquidation"`'
                    enumValues:
                      - limit
                      - market
                      - liquidation
                    required: false
                  - name: original_order_type
                    type: string
                    description: >-
                      Original API order type when an order is represented
                      internally as a limit order. For example, Starbase market
                      orders use `"limit"` as `order_type` with `"market"` in
                      this optional field.
                    enumValues:
                      - market
                      - market_limit
                    required: false
                  - name: advanced
                    type: string
                    description: >-
                      Advanced type of user order: `"usd"` or `"implv"` (only
                      for options; omitted if not applicable)
                    enumValues:
                      - usd
                      - implv
                    required: false
                  - name: order_id
                    type: &ref_0
                      - string
                      - 'null'
                    description: >-
                      Id of the user order (maker or taker), i.e. subscriber's
                      order id that took part in the trade
                    required: true
                  - name: matching_id
                    type: &ref_1
                      - string
                      - 'null'
                    description: Matched order id for self-trades; null otherwise.
                    required: true
                  - name: direction
                    type: string
                    description: Trade direction of the user
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
                  - name: underlying_price
                    type: number
                    description: >-
                      Underlying price for implied volatility calculations
                      (Options only)
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
                  - name: liquidity
                    type: string
                    description: >-
                      Describes what was role of users order: `"M"` when it was
                      maker order, `"T"` when it was taker order
                    enumValues:
                      - M
                      - T
                    required: false
                  - name: fee
                    type: number
                    description: User's fee in units of the specified `fee_currency`
                    required: true
                  - name: fee_currency
                    type: string
                    description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
                    enumValues:
                      - BTC
                      - ETH
                      - USDC
                      - USDT
                      - EURR
                    required: true
                  - name: label
                    type: string
                    description: >-
                      User defined label (presented only when previously set for
                      order by user)
                    required: false
                  - name: state
                    type: string
                    description: >-
                      Order state: `"open"`, `"filled"`, `"rejected"`,
                      `"cancelled"`, `"untriggered"` or `"archive"` (if order
                      was archived)
                    enumValues:
                      - open
                      - filled
                      - rejected
                      - cancelled
                      - untriggered
                      - archive
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
                  - name: block_rfq_id
                    type: integer
                    description: ID of the Block RFQ - when trade was part of the Block RFQ
                    required: false
                  - name: block_rfq_quote_id
                    type: integer
                    description: >-
                      ID of the Block RFQ quote - when trade was part of the
                      Block RFQ
                    required: false
                  - name: reduce_only
                    type: boolean
                    description: >-
                      `true` if user order is reduce-only; omitted for spot
                      trades.
                    required: false
                  - name: post_only
                    type: boolean
                    description: '`true` if user order is post-only'
                    required: false
                  - name: mmp
                    type: boolean
                    description: '`true` if user order is MMP'
                    required: false
                  - name: risk_reducing
                    type: boolean
                    description: >-
                      `true` if user order is marked by the platform as a risk
                      reducing order (can apply only to orders placed by PM
                      users)
                    required: false
                  - name: api
                    type: boolean
                    description: '`true` if user order was created with API'
                    required: false
                  - name: profit_loss
                    type: number
                    description: Profit and loss in base currency.
                    required: false
                  - name: mark_price
                    type: &ref_2
                      - number
                      - 'null'
                    description: Mark Price at the moment of trade
                    required: true
                  - name: legs
                    type: array
                    description: >-
                      Optional field containing leg trades if trade is a combo
                      trade (present when querying for **only** combo trades and
                      in `combo_trades` events). Each leg trade has the same
                      fields as a top-level user trade, including
                      `starbase_match_id`, `starbase_order_id`, and
                      `starbase_timestamp` when matched in Starbase, and
                      `starbase_client_order_id` for orders submitted via
                      [Starbase](https://docs.deribit.com/starbase/overview)
                      direct access.
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
                  - name: quote_set_id
                    type: string
                    description: >-
                      QuoteSet of the user order (optional, present only for
                      orders placed with `private/mass_quote`)
                    required: false
                  - name: quote_id
                    type: string
                    description: >-
                      QuoteID of the user order (optional, present only for
                      orders placed with `private/mass_quote`)
                    required: false
                  - name: trade_allocations
                    type: array
                    description: >-
                      List of allocations for Block RFQ pre-allocation. Each
                      allocation specifies `user_id`, `amount`, and `fee` for
                      the allocated part of the trade. For broker client
                      allocations, a `client_info` object will be included.
                    required: false
                    properties:
                      - name: user_id
                        type: integer
                        description: >-
                          User ID to which part of the trade is allocated. For
                          brokers the User ID is obstructed.
                        required: false
                      - name: amount
                        type: number
                        description: Amount allocated to this user.
                        required: true
                      - name: fee
                        type: number
                        description: Fee for the allocated part of the trade.
                        required: true
                      - name: client_info
                        type: object
                        description: Optional client allocation info for brokers.
                        required: false
                        properties:
                          - name: client_id
                            type: integer
                            description: >-
                              ID of a client; available to broker. Represents a
                              group of users under a common name.
                            required: false
                          - name: client_link_id
                            type: integer
                            description: >-
                              ID assigned to a single user in a client;
                              available to broker.
                            required: false
                          - name: name
                            type: string
                            description: >-
                              Name of the linked user within the client;
                              available to broker.
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
                  trade_id:
                    type: string
                    description: Unique (per currency) trade identifier
                    x-parser-schema-id: <anonymous-schema-613>
                  trade_seq:
                    description: The sequence number of the trade within instrument
                    type: integer
                    x-parser-schema-id: <anonymous-schema-614>
                  instrument_name:
                    type: string
                    description: Unique instrument identifier
                    example: BTC-PERPETUAL
                    x-parser-schema-id: <anonymous-schema-615>
                  timestamp:
                    description: >-
                      The timestamp of the trade (milliseconds since the UNIX
                      epoch)
                    example: 1517329113791
                    type: integer
                    x-parser-schema-id: <anonymous-schema-616>
                  starbase_timestamp:
                    type: integer
                    example: 1536569522277000000
                    description: >-
                      Optional field: the Starbase causal timestamp of the
                      trade, in nanoseconds since the UNIX epoch (present only
                      for trades matched in Starbase)
                    x-parser-schema-id: <anonymous-schema-617>
                  starbase_order_id:
                    description: >-
                      Raw Starbase order id of the user's order, in Starbase's
                      own (non currency-prefixed) id namespace (present only for
                      trades matched in Starbase)
                    type: integer
                    example: 103148386170
                    x-parser-schema-id: <anonymous-schema-618>
                  starbase_client_order_id:
                    description: >-
                      Client order id of the user's own order (maker or taker
                      side) submitted directly to
                      [Starbase](https://docs.deribit.com/starbase/overview) via
                      direct access; not returned for orders placed through the
                      Deribit API; for self-trades this is the taker order's
                      client order id
                    type: string
                    x-parser-schema-id: <anonymous-schema-619>
                  order_type:
                    description: 'Order type: `"limit"`, `"market"`, or `"liquidation"`'
                    type: string
                    enum:
                      - limit
                      - market
                      - liquidation
                    x-parser-schema-id: <anonymous-schema-620>
                  original_order_type:
                    type: string
                    description: >-
                      Original API order type when an order is represented
                      internally as a limit order. For example, Starbase market
                      orders use `"limit"` as `order_type` with `"market"` in
                      this optional field.
                    enum:
                      - market
                      - market_limit
                    x-parser-schema-id: <anonymous-schema-621>
                  advanced:
                    type: string
                    description: >-
                      Advanced type of user order: `"usd"` or `"implv"` (only
                      for options; omitted if not applicable)
                    enum:
                      - usd
                      - implv
                    x-parser-schema-id: <anonymous-schema-622>
                  order_id:
                    description: >-
                      Id of the user order (maker or taker), i.e. subscriber's
                      order id that took part in the trade
                    type: *ref_0
                    x-parser-schema-id: <anonymous-schema-623>
                  matching_id:
                    description: Matched order id for self-trades; null otherwise.
                    type: *ref_1
                    x-parser-schema-id: <anonymous-schema-624>
                  direction:
                    type: string
                    description: Trade direction of the user
                    enum:
                      - buy
                      - sell
                    x-parser-schema-id: <anonymous-schema-625>
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
                    x-parser-schema-id: <anonymous-schema-626>
                  index_price:
                    description: Index Price at the moment of trade
                    type: number
                    x-parser-schema-id: <anonymous-schema-627>
                  price:
                    description: The price of the trade
                    type: number
                    x-parser-schema-id: <anonymous-schema-628>
                  amount:
                    description: >-
                      Trade amount. For perpetual and inverse futures the amount
                      is in USD units. For options and linear futures it is the
                      underlying base currency coin.
                    type: number
                    x-parser-schema-id: <anonymous-schema-629>
                  contracts:
                    description: >-
                      Trade size in contract units (optional, may be absent in
                      historical trades)
                    type: number
                    x-parser-schema-id: <anonymous-schema-630>
                  iv:
                    description: Option implied volatility for the price (Option only)
                    type: number
                    x-parser-schema-id: <anonymous-schema-631>
                  underlying_price:
                    description: >-
                      Underlying price for implied volatility calculations
                      (Options only)
                    type: number
                    x-parser-schema-id: <anonymous-schema-632>
                  liquidation:
                    description: >-
                      Optional field (only for trades caused by liquidation):
                      `"M"` when maker side of trade was under liquidation,
                      `"T"` when taker side was under liquidation, `"MT"` when
                      both sides of trade were under liquidation
                    type: string
                    enum:
                      - M
                      - T
                      - MT
                    x-parser-schema-id: <anonymous-schema-633>
                  liquidity:
                    description: >-
                      Describes what was role of users order: `"M"` when it was
                      maker order, `"T"` when it was taker order
                    type: string
                    enum:
                      - M
                      - T
                    x-parser-schema-id: <anonymous-schema-634>
                  fee:
                    description: User's fee in units of the specified `fee_currency`
                    type: number
                    x-parser-schema-id: <anonymous-schema-635>
                  fee_currency:
                    type: string
                    description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
                    enum:
                      - BTC
                      - ETH
                      - USDC
                      - USDT
                      - EURR
                    x-parser-schema-id: <anonymous-schema-636>
                  label:
                    type: string
                    description: >-
                      User defined label (presented only when previously set for
                      order by user)
                    x-parser-schema-id: <anonymous-schema-637>
                  state:
                    type: string
                    description: >-
                      Order state: `"open"`, `"filled"`, `"rejected"`,
                      `"cancelled"`, `"untriggered"` or `"archive"` (if order
                      was archived)
                    enum:
                      - open
                      - filled
                      - rejected
                      - cancelled
                      - untriggered
                      - archive
                    x-parser-schema-id: <anonymous-schema-638>
                  block_trade_id:
                    description: >-
                      ID of the Block Trade or Block RFQ trade, when the trade
                      was part of one
                    type: string
                    example: '154'
                    x-parser-schema-id: <anonymous-schema-639>
                  block_trade_leg_count:
                    description: >-
                      Number of legs in the Block Trade or Block RFQ trade, when
                      the trade was part of one
                    type: integer
                    example: 3
                    x-parser-schema-id: <anonymous-schema-640>
                  block_delayed:
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
                    type: integer
                    example: 1730827181502
                    x-parser-schema-id: <anonymous-schema-641>
                  block_rfq_id:
                    type: integer
                    description: ID of the Block RFQ - when trade was part of the Block RFQ
                    x-parser-schema-id: <anonymous-schema-642>
                  block_rfq_quote_id:
                    type: integer
                    description: >-
                      ID of the Block RFQ quote - when trade was part of the
                      Block RFQ
                    x-parser-schema-id: <anonymous-schema-643>
                  reduce_only:
                    description: >-
                      `true` if user order is reduce-only; omitted for spot
                      trades.
                    type: boolean
                    x-parser-schema-id: <anonymous-schema-644>
                  post_only:
                    description: '`true` if user order is post-only'
                    type: boolean
                    x-parser-schema-id: <anonymous-schema-645>
                  mmp:
                    type: boolean
                    description: '`true` if user order is MMP'
                    x-parser-schema-id: <anonymous-schema-646>
                  risk_reducing:
                    type: boolean
                    description: >-
                      `true` if user order is marked by the platform as a risk
                      reducing order (can apply only to orders placed by PM
                      users)
                    x-parser-schema-id: <anonymous-schema-647>
                  api:
                    type: boolean
                    description: '`true` if user order was created with API'
                    x-parser-schema-id: <anonymous-schema-648>
                  profit_loss:
                    type: number
                    description: Profit and loss in base currency.
                    x-parser-schema-id: <anonymous-schema-649>
                  mark_price:
                    description: Mark Price at the moment of trade
                    type: *ref_2
                    x-parser-schema-id: <anonymous-schema-650>
                  legs:
                    description: >-
                      Optional field containing leg trades if trade is a combo
                      trade (present when querying for **only** combo trades and
                      in `combo_trades` events). Each leg trade has the same
                      fields as a top-level user trade, including
                      `starbase_match_id`, `starbase_order_id`, and
                      `starbase_timestamp` when matched in Starbase, and
                      `starbase_client_order_id` for orders submitted via
                      [Starbase](https://docs.deribit.com/starbase/overview)
                      direct access.
                    type: array
                    x-parser-schema-id: <anonymous-schema-651>
                  combo_id:
                    description: >-
                      Optional field containing combo instrument name if the
                      trade is a combo trade
                    type: string
                    x-parser-schema-id: <anonymous-schema-652>
                  combo_trade_id:
                    description: >-
                      Optional field containing combo trade identifier if the
                      trade is a combo trade
                    type: string
                    x-parser-schema-id: <anonymous-schema-653>
                  starbase_match_id:
                    description: >-
                      Optional field containing the Starbase match identifier
                      (present only for trades matched via Starbase)
                    type: integer
                    x-parser-schema-id: <anonymous-schema-654>
                  quote_set_id:
                    type: string
                    description: >-
                      QuoteSet of the user order (optional, present only for
                      orders placed with `private/mass_quote`)
                    x-parser-schema-id: <anonymous-schema-655>
                  quote_id:
                    type: string
                    description: >-
                      QuoteID of the user order (optional, present only for
                      orders placed with `private/mass_quote`)
                    x-parser-schema-id: <anonymous-schema-656>
                  trade_allocations:
                    description: >-
                      List of allocations for Block RFQ pre-allocation. Each
                      allocation specifies `user_id`, `amount`, and `fee` for
                      the allocated part of the trade. For broker client
                      allocations, a `client_info` object will be included.
                    type: array
                    items:
                      type: object
                      properties:
                        user_id:
                          description: >-
                            User ID to which part of the trade is allocated. For
                            brokers the User ID is obstructed.
                          type: integer
                          x-parser-schema-id: <anonymous-schema-659>
                        amount:
                          description: Amount allocated to this user.
                          type: number
                          x-parser-schema-id: <anonymous-schema-660>
                        fee:
                          description: Fee for the allocated part of the trade.
                          type: number
                          x-parser-schema-id: <anonymous-schema-661>
                        client_info:
                          description: Optional client allocation info for brokers.
                          type: object
                          properties:
                            client_id:
                              description: >-
                                ID of a client; available to broker. Represents
                                a group of users under a common name.
                              type: integer
                              x-parser-schema-id: <anonymous-schema-663>
                            client_link_id:
                              description: >-
                                ID assigned to a single user in a client;
                                available to broker.
                              type: integer
                              x-parser-schema-id: <anonymous-schema-664>
                            name:
                              description: >-
                                Name of the linked user within the client;
                                available to broker.
                              type: string
                              x-parser-schema-id: <anonymous-schema-665>
                          x-parser-schema-id: <anonymous-schema-662>
                      required:
                        - amount
                        - fee
                      x-parser-schema-id: <anonymous-schema-658>
                    x-parser-schema-id: <anonymous-schema-657>
                required:
                  - trade_id
                  - trade_seq
                  - instrument_name
                  - timestamp
                  - order_id
                  - matching_id
                  - direction
                  - tick_direction
                  - index_price
                  - price
                  - amount
                  - fee
                  - fee_currency
                  - state
                  - mark_price
                type: object
                x-parser-schema-id: <anonymous-schema-612>
              x-parser-schema-id: <anonymous-schema-611>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-610>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": [
              {
                "trade_seq": 74405,
                "trade_id": "48079262",
                "timestamp": 1590484255886,
                "tick_direction": 2,
                "state": "filled",
                "reduce_only": false,
                "price": 8947,
                "post_only": false,
                "order_type": "limit",
                "order_id": "4008978075",
                "matching_id": null,
                "mark_price": 8970.03,
                "liquidity": "T",
                "instrument_name": "BTC-25SEP20",
                "index_price": 8953.53,
                "fee_currency": "BTC",
                "fee": 0.00049961,
                "direction": "sell",
                "amount": 8940
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_3
      - id: x-parser-unique-object-id
        value: user.trades.(kind).(currency).(interval)
  - &ref_4
    id: receive_user_trades_kind_currency_interval_updates
    title: Receive user updates
    description: Client receives user update notifications
    type: receive
    messages:
      - &ref_6
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
              x-parser-schema-id: <anonymous-schema-604>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-605>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-606>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-609>
                  x-parser-schema-id: <anonymous-schema-608>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-607>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-603>
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
                "user.trades.future.BTC.100ms"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_3
sendOperations:
  - *ref_4
receiveOperations:
  - *ref_5
sendMessages:
  - *ref_6
receiveMessages:
  - *ref_7
extensions:
  - id: x-parser-unique-object-id
    value: user.trades.(kind).(currency).(interval)
securitySchemes: []

````

## Related topics

- [block_rfq.maker.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakercurrency.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [user.combo_trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/usercombo_tradeskindcurrencyinterval.md)
- [user.changes.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/userchangeskindcurrencyinterval.md)
- [trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/trades/tradeskindcurrencyinterval.md)