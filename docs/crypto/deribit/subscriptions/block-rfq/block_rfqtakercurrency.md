---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/block-rfq/block_rfqtakercurrency
api_type: WebSocket
updated_at: 2026-11-26 19:02:02.492115
---

# block_rfq.taker.(currency)

> Get notifications about the state of your Block RFQ. `trades` are only visible if the Block RFQ was filled.

**Note:** After Block RFQ creation, a grace period of 5 seconds begins, during which the taker cannot see quotes or trade the Block RFQ.

**📖 Related Article:** [Deribit Block RFQ API walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json block_rfq.taker.(currency)
id: block_rfq.taker.(currency)
title: 'block_rfq.taker.(currency) '
description: >
  Get notifications about the state of your Block RFQ. `trades` are only visible
  if the Block RFQ was filled.


  **Note:** After Block RFQ creation, a grace period of 5 seconds begins, during
  which the taker cannot see quotes or trade the Block RFQ.


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
address: block_rfq.taker.(currency)
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
    id: send_subscribe_block_rfq_taker_currency
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
                  - name: makers
                    type: array
                    required: false
                    properties:
                      - name: item
                        type: string
                        description: List of targeted Block RFQ makers
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
                  - name: asks
                    type: array
                    required: false
                    properties:
                      - name: makers
                        type: array
                        required: false
                        properties:
                          - name: item
                            type: string
                            description: Maker of the quote
                            required: false
                      - name: price
                        type: number
                        description: Price of a quote
                        required: false
                      - name: last_update_timestamp
                        type: integer
                        description: >-
                          Timestamp of the last update of the quote
                          (milliseconds since the UNIX epoch)
                        required: false
                      - name: execution_instruction
                        type: string
                        description: >-
                          Execution instruction of the quote. Default -
                          `any_part_of`


                          - `"all_or_none (AON)"` - The quote can only be filled
                          entirely or not at all, ensuring that its amount
                          matches the amount specified in the Block RFQ.
                          Additionally, 'all_or_none' quotes have priority over
                          'any_part_of' quotes at the same price level.

                          - `"any_part_of (APO)"` - The quote can be filled
                          either partially or fully, with the filled amount
                          potentially being less than the Block RFQ amount.
                        enumValues:
                          - any_part_of
                          - all_or_none
                        required: false
                      - name: amount
                        type: number
                        description: >-
                          This value multiplied by the ratio of a leg gives
                          trade size on that leg.
                        required: false
                      - name: expires_at
                        type: integer
                        description: >-
                          The timestamp when the quote expires (milliseconds
                          since the Unix epoch), equal to the earliest expiry of
                          placed quotes
                        required: false
                  - name: bids
                    type: array
                    required: false
                    properties:
                      - name: makers
                        type: array
                        required: false
                        properties:
                          - name: item
                            type: string
                            description: Maker of the quote
                            required: false
                      - name: price
                        type: number
                        description: Price of a quote
                        required: false
                      - name: last_update_timestamp
                        type: integer
                        description: >-
                          Timestamp of the last update of the quote
                          (milliseconds since the UNIX epoch)
                        required: false
                      - name: execution_instruction
                        type: string
                        description: >-
                          Execution instruction of the quote. Default -
                          `any_part_of`


                          - `"all_or_none (AON)"` - The quote can only be filled
                          entirely or not at all, ensuring that its amount
                          matches the amount specified in the Block RFQ.
                          Additionally, 'all_or_none' quotes have priority over
                          'any_part_of' quotes at the same price level.

                          - `"any_part_of (APO)"` - The quote can be filled
                          either partially or fully, with the filled amount
                          potentially being less than the Block RFQ amount.
                        enumValues:
                          - any_part_of
                          - all_or_none
                        required: false
                      - name: amount
                        type: number
                        description: >-
                          This value multiplied by the ratio of a leg gives
                          trade size on that leg.
                        required: false
                      - name: expires_at
                        type: integer
                        description: >-
                          The timestamp when the quote expires (milliseconds
                          since the Unix epoch), equal to the earliest expiry of
                          placed quotes
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
                  - name: label
                    type: string
                    description: >-
                      User defined label for the Block RFQ (maximum 64
                      characters)
                    required: false
                  - name: app_name
                    type: string
                    description: >-
                      The name of the application that created the Block RFQ on
                      behalf of the user (optional, visible only to taker).
                    required: false
                  - name: mark_price
                    type: number
                    description: The mark price for the instrument
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
                  - name: trade_trigger
                    type: object
                    description: >-
                      Present only if a trade trigger was placed by the taker
                      and only visible to taker. Only for cases: `cancelled`
                      (contains the reason for cancellation) and `untriggered`
                      (contains the information about the trade trigger).
                    required: false
                    properties:
                      - name: state
                        type: string
                        description: 'Trade trigger state: `"untriggered"` or `"cancelled"`'
                        enumValues:
                          - triggered
                          - untriggered
                          - cancelled
                        required: true
                      - name: price
                        type: number
                        description: Price of the trade trigger
                        required: true
                      - name: direction
                        type: string
                        description: Direction of the trade trigger
                        enumValues:
                          - buy
                          - sell
                        required: true
                      - name: cancel_reason
                        type: string
                        description: >-
                          Reason for cancellation, present only when state is
                          cancelled
                        required: false
                  - name: trade_allocations
                    type: array
                    description: >-
                      List of allocations for Block RFQ pre-allocation. Allows
                      to split amount between different (sub)accounts. The taker
                      can also allocate to himself. Visible only to the taker.
                    required: false
                    properties:
                      - name: user_id
                        type: integer
                        description: >-
                          User ID to allocate part of the RFQ amount. For
                          brokers the User ID is obstructed.
                        required: false
                      - name: client_info
                        type: object
                        description: Client allocation info for brokers.
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
                      - name: amount
                        type: number
                        description: Amount allocated to this user or client.
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
                  x-parser-schema-id: <anonymous-schema-1614>
                expiration_timestamp:
                  type: integer
                  example: 1536569522277
                  description: >-
                    The timestamp when the Block RFQ will expire (milliseconds
                    since the UNIX epoch)
                  x-parser-schema-id: <anonymous-schema-1615>
                block_rfq_id:
                  type: integer
                  description: ID of the Block RFQ
                  x-parser-schema-id: <anonymous-schema-1616>
                role:
                  description: Role of the user in Block RFQ
                  type: string
                  enum:
                    - taker
                    - maker
                  x-parser-schema-id: <anonymous-schema-1617>
                state:
                  description: State of the Block RFQ
                  type: string
                  enum:
                    - open
                    - filled
                    - cancelled
                    - expired
                  x-parser-schema-id: <anonymous-schema-1618>
                taker_rating:
                  description: Rating of the taker
                  type: string
                  x-parser-schema-id: <anonymous-schema-1619>
                makers:
                  type: array
                  items:
                    type: string
                    description: List of targeted Block RFQ makers
                    x-parser-schema-id: <anonymous-schema-1621>
                  x-parser-schema-id: <anonymous-schema-1620>
                amount:
                  description: >-
                    This value multiplied by the ratio of a leg gives trade size
                    on that leg.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1622>
                min_trade_amount:
                  description: Minimum amount for trading
                  type: number
                  x-parser-schema-id: <anonymous-schema-1623>
                asks:
                  type: array
                  items:
                    type: object
                    properties:
                      makers:
                        type: array
                        items:
                          type: string
                          description: Maker of the quote
                          x-parser-schema-id: <anonymous-schema-1627>
                        x-parser-schema-id: <anonymous-schema-1626>
                      price:
                        description: Price of a quote
                        type: number
                        x-parser-schema-id: <anonymous-schema-1628>
                      last_update_timestamp:
                        type: integer
                        example: 1536569522277
                        description: >-
                          Timestamp of the last update of the quote
                          (milliseconds since the UNIX epoch)
                        x-parser-schema-id: <anonymous-schema-1629>
                      execution_instruction:
                        type: string
                        description: >-
                          Execution instruction of the quote. Default -
                          `any_part_of`


                          - `"all_or_none (AON)"` - The quote can only be filled
                          entirely or not at all, ensuring that its amount
                          matches the amount specified in the Block RFQ.
                          Additionally, 'all_or_none' quotes have priority over
                          'any_part_of' quotes at the same price level.

                          - `"any_part_of (APO)"` - The quote can be filled
                          either partially or fully, with the filled amount
                          potentially being less than the Block RFQ amount.
                        enum:
                          - any_part_of
                          - all_or_none
                        x-parser-schema-id: <anonymous-schema-1630>
                      amount:
                        description: >-
                          This value multiplied by the ratio of a leg gives
                          trade size on that leg.
                        type: number
                        x-parser-schema-id: <anonymous-schema-1631>
                      expires_at:
                        type: integer
                        example: 1745312540321
                        description: >-
                          The timestamp when the quote expires (milliseconds
                          since the Unix epoch), equal to the earliest expiry of
                          placed quotes
                        x-parser-schema-id: <anonymous-schema-1632>
                    x-parser-schema-id: <anonymous-schema-1625>
                  x-parser-schema-id: <anonymous-schema-1624>
                bids:
                  type: array
                  items:
                    type: object
                    properties:
                      makers:
                        type: array
                        items:
                          type: string
                          description: Maker of the quote
                          x-parser-schema-id: <anonymous-schema-1636>
                        x-parser-schema-id: <anonymous-schema-1635>
                      price:
                        description: Price of a quote
                        type: number
                        x-parser-schema-id: <anonymous-schema-1637>
                      last_update_timestamp:
                        type: integer
                        example: 1536569522277
                        description: >-
                          Timestamp of the last update of the quote
                          (milliseconds since the UNIX epoch)
                        x-parser-schema-id: <anonymous-schema-1638>
                      execution_instruction:
                        type: string
                        description: >-
                          Execution instruction of the quote. Default -
                          `any_part_of`


                          - `"all_or_none (AON)"` - The quote can only be filled
                          entirely or not at all, ensuring that its amount
                          matches the amount specified in the Block RFQ.
                          Additionally, 'all_or_none' quotes have priority over
                          'any_part_of' quotes at the same price level.

                          - `"any_part_of (APO)"` - The quote can be filled
                          either partially or fully, with the filled amount
                          potentially being less than the Block RFQ amount.
                        enum:
                          - any_part_of
                          - all_or_none
                        x-parser-schema-id: <anonymous-schema-1639>
                      amount:
                        description: >-
                          This value multiplied by the ratio of a leg gives
                          trade size on that leg.
                        type: number
                        x-parser-schema-id: <anonymous-schema-1640>
                      expires_at:
                        type: integer
                        example: 1745312540321
                        description: >-
                          The timestamp when the quote expires (milliseconds
                          since the Unix epoch), equal to the earliest expiry of
                          placed quotes
                        x-parser-schema-id: <anonymous-schema-1641>
                    x-parser-schema-id: <anonymous-schema-1634>
                  x-parser-schema-id: <anonymous-schema-1633>
                legs:
                  type: array
                  items:
                    type: object
                    properties:
                      ratio:
                        description: Ratio of amount between legs
                        type: integer
                        x-parser-schema-id: <anonymous-schema-1644>
                      instrument_name:
                        type: string
                        description: Unique instrument identifier
                        example: BTC-PERPETUAL
                        x-parser-schema-id: <anonymous-schema-1645>
                      direction:
                        type: string
                        description: 'Direction: `buy`, or `sell`'
                        enum:
                          - buy
                          - sell
                        x-parser-schema-id: <anonymous-schema-1646>
                    x-parser-schema-id: <anonymous-schema-1643>
                  x-parser-schema-id: <anonymous-schema-1642>
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
                      x-parser-schema-id: <anonymous-schema-1648>
                    instrument_name:
                      type: string
                      description: Unique instrument identifier
                      example: BTC-PERPETUAL
                      x-parser-schema-id: <anonymous-schema-1649>
                    direction:
                      type: string
                      description: 'Direction: `buy`, or `sell`'
                      enum:
                        - buy
                        - sell
                      x-parser-schema-id: <anonymous-schema-1650>
                    price:
                      description: Price for a hedge leg
                      type: number
                      x-parser-schema-id: <anonymous-schema-1651>
                  x-parser-schema-id: <anonymous-schema-1647>
                combo_id:
                  type: string
                  description: Unique combo identifier
                  example: BTC-FS-31DEC21-PERP
                  x-parser-schema-id: <anonymous-schema-1652>
                label:
                  type: string
                  description: User defined label for the Block RFQ (maximum 64 characters)
                  x-parser-schema-id: <anonymous-schema-1653>
                app_name:
                  description: >-
                    The name of the application that created the Block RFQ on
                    behalf of the user (optional, visible only to taker).
                  type: string
                  example: Example Application
                  x-parser-schema-id: <anonymous-schema-1654>
                mark_price:
                  description: The mark price for the instrument
                  type: number
                  x-parser-schema-id: <anonymous-schema-1655>
                disclosed:
                  description: >-
                    Indicates whether the RFQ was created as non-anonymous,
                    meaning taker and maker aliases are visible to
                    counterparties.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1656>
                taker:
                  description: Taker alias. Present only when `disclosed` is `true`.
                  type: string
                  example: TAKER1
                  x-parser-schema-id: <anonymous-schema-1657>
                index_prices:
                  type: array
                  items:
                    type: number
                    description: >-
                      A list of index prices for the underlying instrument(s) at
                      the time of trade execution.
                    x-parser-schema-id: <anonymous-schema-1659>
                  x-parser-schema-id: <anonymous-schema-1658>
                included_in_taker_rating:
                  description: >-
                    Indicates whether the RFQ is included in the taker's rating
                    calculation. Present only for closed RFQs created by the
                    requesting taker.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1660>
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
                        x-parser-schema-id: <anonymous-schema-1663>
                      price:
                        description: >-
                          Price in the instrument's price units (quote currency
                          for futures and spot).
                        type: number
                        x-parser-schema-id: <anonymous-schema-1664>
                      amount:
                        description: >-
                          Trade amount. For options, linear futures, linear
                          perpetuals and spots the amount is denominated in the
                          underlying base currency coin. The inverse perpetuals
                          and inverse futures are denominated in USD units.
                        type: number
                        x-parser-schema-id: <anonymous-schema-1665>
                      maker:
                        type: string
                        description: Alias of the maker (optional)
                        x-parser-schema-id: <anonymous-schema-1666>
                      hedge_amount:
                        type: number
                        description: >-
                          Amount of the hedge leg. For linear futures, linear
                          perpetuals and spots the amount is denominated in the
                          underlying base currency coin. The inverse perpetuals
                          and inverse futures are denominated in USD units.
                        x-parser-schema-id: <anonymous-schema-1667>
                    x-parser-schema-id: <anonymous-schema-1662>
                  x-parser-schema-id: <anonymous-schema-1661>
                trade_trigger:
                  type: object
                  description: >-
                    Present only if a trade trigger was placed by the taker and
                    only visible to taker. Only for cases: `cancelled` (contains
                    the reason for cancellation) and `untriggered` (contains the
                    information about the trade trigger).
                  properties:
                    state:
                      type: string
                      description: 'Trade trigger state: `"untriggered"` or `"cancelled"`'
                      enum:
                        - triggered
                        - untriggered
                        - cancelled
                      x-parser-schema-id: <anonymous-schema-1669>
                    price:
                      description: Price of the trade trigger
                      type: number
                      x-parser-schema-id: <anonymous-schema-1670>
                    direction:
                      description: Direction of the trade trigger
                      type: string
                      enum:
                        - buy
                        - sell
                      x-parser-schema-id: <anonymous-schema-1671>
                    cancel_reason:
                      description: >-
                        Reason for cancellation, present only when state is
                        cancelled
                      type: string
                      x-parser-schema-id: <anonymous-schema-1672>
                  required:
                    - state
                    - price
                    - direction
                  x-parser-schema-id: <anonymous-schema-1668>
                trade_allocations:
                  type: array
                  description: >-
                    List of allocations for Block RFQ pre-allocation. Allows to
                    split amount between different (sub)accounts. The taker can
                    also allocate to himself. Visible only to the taker.
                  items:
                    type: object
                    properties:
                      user_id:
                        description: >-
                          User ID to allocate part of the RFQ amount. For
                          brokers the User ID is obstructed.
                        type: integer
                        x-parser-schema-id: <anonymous-schema-1675>
                      client_info:
                        description: Client allocation info for brokers.
                        type: object
                        properties:
                          client_id:
                            description: >-
                              ID of a client; available to broker. Represents a
                              group of users under a common name.
                            type: integer
                            x-parser-schema-id: <anonymous-schema-1677>
                          client_link_id:
                            description: >-
                              ID assigned to a single user in a client;
                              available to broker.
                            type: integer
                            x-parser-schema-id: <anonymous-schema-1678>
                          name:
                            description: >-
                              Name of the linked user within the client;
                              available to broker.
                            type: string
                            x-parser-schema-id: <anonymous-schema-1679>
                        x-parser-schema-id: <anonymous-schema-1676>
                      amount:
                        description: Amount allocated to this user or client.
                        type: number
                        x-parser-schema-id: <anonymous-schema-1680>
                    x-parser-schema-id: <anonymous-schema-1674>
                  x-parser-schema-id: <anonymous-schema-1673>
              x-parser-schema-id: <anonymous-schema-1613>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1612>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "label": "example",
              "state": "open",
              "amount": 10000,
              "role": "taker",
              "bids": [
                {
                  "amount": 10000,
                  "price": 291664.14,
                  "makers": [
                    "ANONYMOUS"
                  ],
                  "last_update_timestamp": 1740047910507,
                  "execution_instruction": "any_part_of"
                }
              ],
              "asks": [],
              "combo_id": null,
              "legs": [
                {
                  "direction": "buy",
                  "instrument_name": "BTC-21FEB25",
                  "ratio": 1
                },
                {
                  "direction": "buy",
                  "instrument_name": "BTC-28FEB25",
                  "ratio": 1
                },
                {
                  "direction": "buy",
                  "instrument_name": "BTC-PERPETUAL",
                  "ratio": 1
                }
              ],
              "min_trade_amount": 10,
              "makers": [
                "MAKER1",
                "MAKER2"
              ],
              "creation_timestamp": 1740047910438,
              "block_rfq_id": 321,
              "expiration_timestamp": 1740048210438,
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
        value: block_rfq.taker.(currency)
  - &ref_1
    id: receive_block_rfq_taker_currency_updates
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
              x-parser-schema-id: <anonymous-schema-1606>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1607>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1608>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1611>
                  x-parser-schema-id: <anonymous-schema-1610>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1609>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1605>
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
                "block_rfq.taker.BTC"
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
    value: block_rfq.taker.(currency)
securitySchemes: []

````

## Related topics

- [Deribit Block RFQ API Walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough.md)
- [block_rfq.maker.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakercurrency.md)
- [block_rfq.maker.quotes.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakerquotescurrency.md)
- [block_rfq.trades.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqtradescurrency.md)
- [private/get_block_rfqs](https://docs.deribit.com/api-reference/block-rfq/private-get_block_rfqs.md)