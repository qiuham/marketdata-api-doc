---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakercurrency
api_type: WebSocket
updated_at: 2026-11-20 19:00:10.807829
---

# block_rfq.maker.(currency)

> Real-time notifications for Block RFQs (Request for Quotes) that are available for the subscribed maker to respond to.

This subscription notifies makers when new Block RFQs are created in the specified currency (or all currencies if `any` is used) that they can potentially quote on. Each notification includes:

- **RFQ identification:** Unique Block RFQ ID, creation timestamp, and expiration timestamp
- **RFQ structure:** Multi-leg trade structure with instrument names, directions (buy/sell), and ratios for each leg
- **Trade parameters:** Total amount (multiplied by leg ratios determines trade size), minimum trade amount, and optional combo identifier
- **Hedge information:** Optional hedge leg details including instrument, direction, amount, and price
- **RFQ state:** Current state (open, filled, cancelled, or expired)
- **Counterparty information:** Taker rating, taker alias (if disclosed), and disclosure status
- **Execution details:** For filled RFQs, includes trade information with prices, amounts, directions, and maker aliases
- **Index prices:** List of index prices for underlying instruments at trade execution time (for filled RFQs)
- **Rating information:** Whether the RFQ is included in taker rating calculation (for closed RFQs)

Makers can subscribe to specific currencies (BTC, ETH, USDC, USDT) or use `any` to receive notifications for all supported currencies. This enables makers to monitor incoming RFQ opportunities and respond with competitive quotes in a timely manner.

**Scope required:** `block_rfq:read`

**Trade cross-posting:** When a Block RFQ is filled, the resulting trades are also delivered through the `user.trades.{instrument_name}.{interval}` and `user.trades.{kind}.{currency}.{interval}` channels. Those notifications include `block_rfq_id`, `block_trade_id`, and — for the maker side — `block_rfq_quote_id`.

**📖 Related Article:** [Deribit Block RFQ API walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json block_rfq.maker.(currency)
id: block_rfq.maker.(currency)
title: 'block_rfq.maker.(currency) '
description: >
  Real-time notifications for Block RFQs (Request for Quotes) that are available
  for the subscribed maker to respond to.


  This subscription notifies makers when new Block RFQs are created in the
  specified currency (or all currencies if `any` is used) that they can
  potentially quote on. Each notification includes:


  - **RFQ identification:** Unique Block RFQ ID, creation timestamp, and
  expiration timestamp

  - **RFQ structure:** Multi-leg trade structure with instrument names,
  directions (buy/sell), and ratios for each leg

  - **Trade parameters:** Total amount (multiplied by leg ratios determines
  trade size), minimum trade amount, and optional combo identifier

  - **Hedge information:** Optional hedge leg details including instrument,
  direction, amount, and price

  - **RFQ state:** Current state (open, filled, cancelled, or expired)

  - **Counterparty information:** Taker rating, taker alias (if disclosed), and
  disclosure status

  - **Execution details:** For filled RFQs, includes trade information with
  prices, amounts, directions, and maker aliases

  - **Index prices:** List of index prices for underlying instruments at trade
  execution time (for filled RFQs)

  - **Rating information:** Whether the RFQ is included in taker rating
  calculation (for closed RFQs)


  Makers can subscribe to specific currencies (BTC, ETH, USDC, USDT) or use
  `any` to receive notifications for all supported currencies. This enables
  makers to monitor incoming RFQ opportunities and respond with competitive
  quotes in a timely manner.


  **Scope required:** `block_rfq:read`


  **Trade cross-posting:** When a Block RFQ is filled, the resulting trades are
  also delivered through the `user.trades.{instrument_name}.{interval}` and
  `user.trades.{kind}.{currency}.{interval}` channels. Those notifications
  include `block_rfq_id`, `block_trade_id`, and — for the maker side —
  `block_rfq_quote_id`.


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
address: block_rfq.maker.(currency)
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
    id: send_subscribe_block_rfq_maker_currency
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
                type: object
                required: true
                properties:
                  - name: creation_timestamp
                    type: integer
                    description: >-
                      The timestamp when Block RFQ was created (milliseconds
                      since the Unix epoch)
                    required: false
                  - name: expiration_timestamp
                    type: integer
                    description: >-
                      The timestamp when the Block RFQ will expire (milliseconds
                      since the UNIX epoch)
                    required: false
                  - name: block_rfq_id
                    type: integer
                    description: ID of the Block RFQ
                    required: false
                  - name: role
                    type: string
                    description: Role of the user in Block RFQ
                    enumValues:
                      - taker
                      - maker
                    required: false
                  - name: state
                    type: string
                    description: State of the Block RFQ
                    enumValues:
                      - open
                      - filled
                      - cancelled
                      - expired
                    required: false
                  - name: taker_rating
                    type: string
                    description: Rating of the taker
                    required: false
                  - name: amount
                    type: number
                    description: >-
                      This value multiplied by the ratio of a leg gives trade
                      size on that leg.
                    required: false
                  - name: min_trade_amount
                    type: number
                    description: Minimum amount for trading
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
                  - name: combo_id
                    type: string
                    description: Unique combo identifier
                    required: false
                  - name: disclosed
                    type: boolean
                    description: >-
                      Indicates whether the RFQ was created as non-anonymous,
                      meaning taker and maker aliases are visible to
                      counterparties.
                    required: false
                  - name: taker
                    type: string
                    description: Taker alias. Present only when `disclosed` is `true`.
                    required: false
                  - name: index_prices
                    type: array
                    required: false
                    properties:
                      - name: item
                        type: number
                        description: >-
                          A list of index prices for the underlying
                          instrument(s) at the time of trade execution.
                        required: false
                  - name: included_in_taker_rating
                    type: boolean
                    description: >-
                      Indicates whether the RFQ is included in the taker's
                      rating calculation. Present only for closed RFQs created
                      by the requesting taker.
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
                      - name: maker
                        type: string
                        description: Alias of the maker (optional)
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
              type: object
              properties:
                creation_timestamp:
                  description: >-
                    The timestamp when Block RFQ was created (milliseconds since
                    the Unix epoch)
                  type: integer
                  example: 1536569522277
                  x-parser-schema-id: <anonymous-schema-1573>
                expiration_timestamp:
                  type: integer
                  example: 1536569522277
                  description: >-
                    The timestamp when the Block RFQ will expire (milliseconds
                    since the UNIX epoch)
                  x-parser-schema-id: <anonymous-schema-1574>
                block_rfq_id:
                  type: integer
                  description: ID of the Block RFQ
                  x-parser-schema-id: <anonymous-schema-1575>
                role:
                  description: Role of the user in Block RFQ
                  type: string
                  enum:
                    - taker
                    - maker
                  x-parser-schema-id: <anonymous-schema-1576>
                state:
                  description: State of the Block RFQ
                  type: string
                  enum:
                    - open
                    - filled
                    - cancelled
                    - expired
                  x-parser-schema-id: <anonymous-schema-1577>
                taker_rating:
                  description: Rating of the taker
                  type: string
                  x-parser-schema-id: <anonymous-schema-1578>
                amount:
                  description: >-
                    This value multiplied by the ratio of a leg gives trade size
                    on that leg.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1579>
                min_trade_amount:
                  description: Minimum amount for trading
                  type: number
                  x-parser-schema-id: <anonymous-schema-1580>
                legs:
                  type: array
                  items:
                    type: object
                    properties:
                      ratio:
                        description: Ratio of amount between legs
                        type: integer
                        x-parser-schema-id: <anonymous-schema-1583>
                      instrument_name:
                        type: string
                        description: Unique instrument identifier
                        example: BTC-PERPETUAL
                        x-parser-schema-id: <anonymous-schema-1584>
                      direction:
                        type: string
                        description: 'Direction: `buy`, or `sell`'
                        enum:
                          - buy
                          - sell
                        x-parser-schema-id: <anonymous-schema-1585>
                    x-parser-schema-id: <anonymous-schema-1582>
                  x-parser-schema-id: <anonymous-schema-1581>
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
                      x-parser-schema-id: <anonymous-schema-1587>
                    instrument_name:
                      type: string
                      description: Unique instrument identifier
                      example: BTC-PERPETUAL
                      x-parser-schema-id: <anonymous-schema-1588>
                    direction:
                      type: string
                      description: 'Direction: `buy`, or `sell`'
                      enum:
                        - buy
                        - sell
                      x-parser-schema-id: <anonymous-schema-1589>
                    price:
                      description: Price for a hedge leg
                      type: number
                      x-parser-schema-id: <anonymous-schema-1590>
                  x-parser-schema-id: <anonymous-schema-1586>
                combo_id:
                  type: string
                  description: Unique combo identifier
                  example: BTC-FS-31DEC21-PERP
                  x-parser-schema-id: <anonymous-schema-1591>
                disclosed:
                  description: >-
                    Indicates whether the RFQ was created as non-anonymous,
                    meaning taker and maker aliases are visible to
                    counterparties.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1592>
                taker:
                  description: Taker alias. Present only when `disclosed` is `true`.
                  type: string
                  example: TAKER1
                  x-parser-schema-id: <anonymous-schema-1593>
                index_prices:
                  type: array
                  items:
                    type: number
                    description: >-
                      A list of index prices for the underlying instrument(s) at
                      the time of trade execution.
                    x-parser-schema-id: <anonymous-schema-1595>
                  x-parser-schema-id: <anonymous-schema-1594>
                included_in_taker_rating:
                  description: >-
                    Indicates whether the RFQ is included in the taker's rating
                    calculation. Present only for closed RFQs created by the
                    requesting taker.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1596>
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
                        x-parser-schema-id: <anonymous-schema-1599>
                      price:
                        description: >-
                          Price in the instrument's price units (quote currency
                          for futures and spot).
                        type: number
                        x-parser-schema-id: <anonymous-schema-1600>
                      amount:
                        description: >-
                          Trade amount. For options, linear futures, linear
                          perpetuals and spots the amount is denominated in the
                          underlying base currency coin. The inverse perpetuals
                          and inverse futures are denominated in USD units.
                        type: number
                        x-parser-schema-id: <anonymous-schema-1601>
                      maker:
                        type: string
                        description: Alias of the maker (optional)
                        x-parser-schema-id: <anonymous-schema-1602>
                      hedge_amount:
                        type: number
                        description: >-
                          Amount of the hedge leg. For linear futures, linear
                          perpetuals and spots the amount is denominated in the
                          underlying base currency coin. The inverse perpetuals
                          and inverse futures are denominated in USD units.
                        x-parser-schema-id: <anonymous-schema-1603>
                    x-parser-schema-id: <anonymous-schema-1598>
                  x-parser-schema-id: <anonymous-schema-1597>
              x-parser-schema-id: <anonymous-schema-1572>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1571>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "state": "open",
              "combo_id": "BTC-18NOV24-82000-C",
              "legs": [
                {
                  "direction": "buy",
                  "instrument_name": "BTC-18NOV24-82000-C",
                  "ratio": 1
                }
              ],
              "amount": 25,
              "role": "maker",
              "expiration_timestamp": 1731664976443,
              "block_rfq_id": 722,
              "creation_timestamp": 1731664676443,
              "taker_rating": "1-2",
              "disclosed": true,
              "taker": "TAKER1"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: block_rfq.maker.(currency)
  - &ref_1
    id: receive_block_rfq_maker_currency_updates
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
              x-parser-schema-id: <anonymous-schema-1565>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1566>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1567>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1570>
                  x-parser-schema-id: <anonymous-schema-1569>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1568>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1564>
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
                "block_rfq.maker.BTC"
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
    value: block_rfq.maker.(currency)
securitySchemes: []

````

## Related topics

- [Deribit Block RFQ API Walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough.md)
- [block_rfq.maker.quotes.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakerquotescurrency.md)
- [block_rfq.taker.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqtakercurrency.md)
- [block_rfq.trades.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqtradescurrency.md)
- [private/get_block_rfq_makers](https://docs.deribit.com/api-reference/block-rfq/private-get_block_rfq_makers.md)