---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-fills'
updated_at: 2026-11-13
---

# Fills

> Perps WebSocket private fill updates.



## AsyncAPI

````yaml asyncapi-perps.json fills
id: fills
title: Fills
description: Real-time fill updates. Requires authentication, see [Auth](/ws/auth).
servers:
  - id: production
    protocol: wss
    host: ws.perpetuals.polymarket.com
    bindings: []
    variables: []
address: /v1/ws
parameters: []
bindings: []
operations:
  - &ref_1
    id: FillsSubscribe
    title: Fills subscribe
    description: Subscribe to fills
    type: receive
    messages:
      - &ref_6
        id: SubscribeRequest
        contentType: application/json
        payload:
          - name: Subscribe
            description: Subscribe to private fill updates (requires prior auth)
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: req
                type: string
                description: Request type
                enumValues:
                  - post
                  - sub
                  - unsub
                required: true
              - name: chs
                type: array
                description: 'Fills private channel: "fills"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - fills
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-473>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-474>
            chs:
              type: array
              description: 'Fills private channel: "fills"'
              items:
                type: string
                enum:
                  - fills
                x-parser-schema-id: <anonymous-schema-476>
              example:
                - fills
              x-parser-schema-id: <anonymous-schema-475>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-472>
        title: Subscribe
        description: Subscribe to private fill updates (requires prior auth)
        example: |-
          {
            "req": "sub",
            "chs": [
              "fills"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeRequest
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: fills
  - &ref_3
    id: FillsSubscribeResponse
    title: Fills subscribe response
    description: Fills subscribe response
    type: send
    messages:
      - &ref_8
        id: SubscribeResponse
        contentType: application/json
        payload:
          - name: Subscribe Response
            description: Response to fills subscribe request
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: array
                title: Subscribe Response
                required: true
                properties:
                  - name: item
                    type: object
                    required: false
                    properties:
                      - name: status
                        type: string
                        enumValues:
                          - ok
                        required: true
                      - name: status
                        type: string
                        enumValues:
                          - err
                        required: true
                      - name: error
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Response
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-478>
            data:
              title: Subscribe Response
              type: array
              items:
                oneOf:
                  - type: object
                    required:
                      - status
                    properties:
                      status:
                        type: string
                        enum:
                          - ok
                        x-parser-schema-id: <anonymous-schema-482>
                    x-parser-schema-id: <anonymous-schema-481>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-484>
                      error:
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        example: insufficient_margin
                        x-parser-schema-id: <anonymous-schema-485>
                    x-parser-schema-id: <anonymous-schema-483>
                x-parser-schema-id: <anonymous-schema-480>
              x-parser-schema-id: <anonymous-schema-479>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-477>
        title: Subscribe Response
        description: Response to fills subscribe request
        example: |-
          {
            "data": []
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: SubscribeResponse
    bindings: []
    extensions: *ref_0
  - &ref_2
    id: FillsUnsubscribe
    title: Fills unsubscribe
    description: Unsubscribe from fills
    type: receive
    messages:
      - &ref_7
        id: UnsubscribeRequest
        contentType: application/json
        payload:
          - name: Unsubscribe
            description: Unsubscribe from private fill updates
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: req
                type: string
                description: Request type
                enumValues:
                  - post
                  - sub
                  - unsub
                required: true
              - name: chs
                type: array
                description: 'Fills private channel: "fills"'
                required: true
                properties:
                  - name: item
                    type: string
                    enumValues:
                      - fills
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-487>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-488>
            chs:
              type: array
              description: 'Fills private channel: "fills"'
              items:
                type: string
                enum:
                  - fills
                x-parser-schema-id: <anonymous-schema-490>
              example:
                - fills
              x-parser-schema-id: <anonymous-schema-489>
          required:
            - req
            - chs
          x-parser-schema-id: <anonymous-schema-486>
        title: Unsubscribe
        description: Unsubscribe from private fill updates
        example: |-
          {
            "req": "unsub",
            "chs": [
              "fills"
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeRequest
    bindings: []
    extensions: *ref_0
  - &ref_4
    id: FillsUnsubscribeResponse
    title: Fills unsubscribe response
    description: Fills unsubscribe response
    type: send
    messages:
      - &ref_9
        id: UnsubscribeResponse
        contentType: application/json
        payload:
          - name: Unsubscribe Response
            description: Response to fills unsubscribe request
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: array
                title: Subscribe Response
                required: true
                properties:
                  - name: item
                    type: object
                    required: false
                    properties:
                      - name: status
                        type: string
                        enumValues:
                          - ok
                        required: true
                      - name: status
                        type: string
                        enumValues:
                          - err
                        required: true
                      - name: error
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Response
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-492>
            data:
              title: Subscribe Response
              type: array
              items:
                oneOf:
                  - type: object
                    required:
                      - status
                    properties:
                      status:
                        type: string
                        enum:
                          - ok
                        x-parser-schema-id: <anonymous-schema-496>
                    x-parser-schema-id: <anonymous-schema-495>
                  - type: object
                    required:
                      - status
                      - error
                    properties:
                      status:
                        type: string
                        enum:
                          - err
                        x-parser-schema-id: <anonymous-schema-498>
                      error:
                        type: string
                        description: >-
                          Error identifier. For domain rejections and transport
                          errors (`401`/`404`/`429`/`500`) this is a stable,
                          machine-readable snake_case identifier that is part of
                          the API contract and safe to branch on, e.g.
                          `insufficient_margin`, `insufficient_balance`,
                          `order_not_found`, `reduce_only_invalid`,
                          `price_outside_bounds`, `position_not_found`,
                          `position_exists`, `open_orders_exist`,
                          `invalid_margin_mode`, `invalid_margin_amount`,
                          `margin_below_required_initial`,
                          `account_liquidating`, `instrument_close_only`,
                          `instrument_settled`, `settlement_price_unavailable`,
                          `settlement_insurance_insufficient`,
                          `settlement_invalid_state`, `unauthorized`,
                          `not_found`. `instrument_close_only` means user orders
                          must reduce an existing position; `instrument_settled`
                          is permanent. Settlement readiness errors leave the
                          instrument and accounts unchanged. For `400` it is a
                          human-readable validation detail whose wording may
                          change. See the Error handling guide for the domain
                          identifiers. (Post-only / Fill-or-Kill outcomes are
                          order statuses such as `post_only_rejected`, not
                          rejections.)
                        example: insufficient_margin
                        x-parser-schema-id: <anonymous-schema-499>
                    x-parser-schema-id: <anonymous-schema-497>
                x-parser-schema-id: <anonymous-schema-494>
              x-parser-schema-id: <anonymous-schema-493>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-491>
        title: Unsubscribe Response
        description: Response to fills unsubscribe request
        example: |-
          {
            "data": []
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: UnsubscribeResponse
    bindings: []
    extensions: *ref_0
  - &ref_5
    id: FillsUpdate
    title: Fills update
    description: Receive fill updates
    type: send
    messages:
      - &ref_10
        id: Update
        contentType: application/json
        payload:
          - name: Update
            description: Real-time fill updates for authenticated users
            type: object
            properties:
              - name: ch
                type: string
                description: >-
                  Channel name for push data. Parameterized channels include the
                  instrument ID (e.g. "trades::1", "book::1", "klines::1::1m",
                  "tickers::all"). Most private channels use plain names (e.g.
                  "fills", "orders"). TP/SL updates are the exception: they are
                  suffixed with the authenticated account's numeric ID (e.g.
                  "tpsl::12345"), so match them on the "tpsl::" prefix.
                  Subscribe and unsubscribe requests still use the bare "tpsl".
                required: true
              - name: ts
                type: integer
                description: >-
                  Request timestamp. Unix milliseconds for most operations; Unix
                  seconds for withdrawals (must match the on-chain EIP-712
                  struct verified against block.timestamp).
                required: true
              - name: sq
                type: integer
                description: Sequence number
                required: true
              - name: data
                type: array
                description: Array of fill objects
                required: true
                properties:
                  - name: tid
                    type: integer
                    description: Trade ID
                    required: true
                  - name: oid
                    type: integer
                    description: Order ID
                    required: true
                  - name: iid
                    type: integer
                    description: Instrument ID
                    required: true
                  - name: side
                    type: string
                    description: Side
                    enumValues:
                      - long
                      - short
                    required: true
                  - name: p
                    type: string
                    description: Price
                    required: true
                  - name: qty
                    type: string
                    description: Quantity in no. of contracts
                    required: true
                  - name: taker
                    type: boolean
                    description: Whether this side was the taker
                    required: true
                  - name: fee
                    type: string
                    description: >-
                      Signed exchange fee for this trade side, excluding
                      builder_fee. Negative values are rebates
                    required: true
                  - name: builder_fee
                    type: string
                    description: >-
                      Actual additional builder fee in the same asset as fee,
                      floored independently for each execution to that asset's
                      token decimals (six for pUSD), with discarded dust and no
                      carry. The fee is non-negative and is zero for older or
                      untagged fills and excluded forced liquidation legs.
                    required: true
                  - name: total_fee
                    type: string
                    description: >-
                      Exact signed sum of exchange fee and builder_fee in the
                      same asset. May be negative when exchange rebates exceed
                      the builder charge.
                    required: true
                  - name: builder
                    type: object
                    description: >-
                      Saved builder terms. Address is the registered Perps
                      account, and fee_rate is an additional fraction of
                      executed notional. Terms survive approval revocation for
                      existing orders.
                    required: false
                    properties:
                      - name: address
                        type: string
                        description: Address
                        required: true
                      - name: fee_rate
                        type: string
                        description: >-
                          Additional builder fee as a decimal fraction of
                          executed notional, from 0 through 0.001 (10 basis
                          points). Zero approval revokes future admission. Never
                          a percentage string.
                        required: true
                  - name: fea
                    type: string
                    description: Fee asset name
                    required: true
                  - name: psz
                    type: string
                    description: Position size before the fill
                    required: true
                  - name: pep
                    type: string
                    description: Position entry price before the fill
                    required: true
                  - name: pnl
                    type: string
                    description: >-
                      Realized trading PnL before exchange and builder fees.
                      Subtract total_fee once to calculate this fill's net
                      trading result.
                    required: true
                  - name: liq
                    type: boolean
                    description: >-
                      Whether this fill was part of a liquidation of the
                      account's position — true on forced closes and on any fill
                      executed while the account was under liquidation on the
                      instrument, maker or taker. False on the counterparty leg
                      of an auto-deleveraging or backstop match — its fill is
                      part of someone else's liquidation, flagged by `adl` where
                      applicable
                    required: true
                  - name: adl
                    type: boolean
                    description: Whether the fill came from auto-deleveraging
                    required: true
                  - name: ts
                    type: integer
                    description: >-
                      Request timestamp. Unix milliseconds for most operations;
                      Unix seconds for withdrawals (must match the on-chain
                      EIP-712 struct verified against block.timestamp).
                    required: true
                  - name: settlement
                    type: boolean
                    description: >-
                      Whether this fill closes a position during permanent
                      instrument settlement. Settlement fills use the final
                      settlement price and have no fees or liquidation
                      penalties; they are not normal market trades or ADL.
                    required: true
                  - name: coid
                    type: string
                    description: Client order ID
                    required: false
                  - name: liquidation_details
                    type: object
                    required: false
                    properties:
                      - name: liquidated_user
                        type: string
                        description: >-
                          Checksummed address of the liquidated account. Present
                          on authenticated fill surfaces and, on public
                          account-scoped routes, only on the liquidated
                          account's own rows. It is absent on fund-side public
                          rows and the anonymous trade tape.
                        required: false
                      - name: mark
                        type: string
                        description: >-
                          Mark price captured when the liquidation command was
                          issued. The fill price itself stays the accounting
                          price.
                        required: true
                      - name: method
                        type: string
                        description: >-
                          How the position was liquidated. Only backstop is
                          emitted today. The market value is reserved for
                          order-book liquidations, which currently carry no
                          liquidation_details.
                        enumValues:
                          - market
                          - backstop
                        required: true
        headers: []
        jsonPayloadSchema:
          title: Fills Update
          type: object
          properties:
            ch:
              type: string
              description: >-
                Channel name for push data. Parameterized channels include the
                instrument ID (e.g. "trades::1", "book::1", "klines::1::1m",
                "tickers::all"). Most private channels use plain names (e.g.
                "fills", "orders"). TP/SL updates are the exception: they are
                suffixed with the authenticated account's numeric ID (e.g.
                "tpsl::12345"), so match them on the "tpsl::" prefix. Subscribe
                and unsubscribe requests still use the bare "tpsl".
              example: trades::1
              x-parser-schema-id: <anonymous-schema-501>
            ts:
              type: integer
              description: >-
                Request timestamp. Unix milliseconds for most operations; Unix
                seconds for withdrawals (must match the on-chain EIP-712 struct
                verified against block.timestamp).
              example: 1767225600000
              x-parser-schema-id: <anonymous-schema-502>
            sq:
              type: integer
              description: Sequence number
              example: 1234567890
              x-parser-schema-id: <anonymous-schema-503>
            data:
              type: array
              description: Array of fill objects
              items:
                type: object
                required:
                  - tid
                  - oid
                  - iid
                  - side
                  - p
                  - qty
                  - taker
                  - fee
                  - builder_fee
                  - total_fee
                  - fea
                  - psz
                  - pep
                  - pnl
                  - ts
                  - settlement
                  - liq
                  - adl
                properties:
                  tid:
                    type: integer
                    description: Trade ID
                    example: 1
                    x-parser-schema-id: <anonymous-schema-506>
                  oid:
                    type: integer
                    description: Order ID
                    example: 1234567890
                    x-parser-schema-id: <anonymous-schema-507>
                  iid:
                    type: integer
                    description: Instrument ID
                    example: 1
                    x-parser-schema-id: <anonymous-schema-508>
                  side:
                    type: string
                    description: Side
                    enum:
                      - long
                      - short
                    x-parser-schema-id: <anonymous-schema-509>
                  p:
                    type: string
                    description: Price
                    example: '100.00'
                    x-parser-schema-id: <anonymous-schema-510>
                  qty:
                    type: string
                    description: Quantity in no. of contracts
                    example: '10.00'
                    x-parser-schema-id: <anonymous-schema-511>
                  taker:
                    type: boolean
                    description: Whether this side was the taker
                    x-parser-schema-id: <anonymous-schema-512>
                  fee:
                    type: string
                    description: >-
                      Signed exchange fee for this trade side, excluding
                      builder_fee. Negative values are rebates
                    example: '1.25'
                    x-parser-schema-id: <anonymous-schema-513>
                  builder_fee:
                    type: string
                    description: >-
                      Actual additional builder fee in the same asset as fee,
                      floored independently for each execution to that asset's
                      token decimals (six for pUSD), with discarded dust and no
                      carry. The fee is non-negative and is zero for older or
                      untagged fills and excluded forced liquidation legs.
                    example: '1.00'
                    x-parser-schema-id: <anonymous-schema-514>
                  total_fee:
                    type: string
                    description: >-
                      Exact signed sum of exchange fee and builder_fee in the
                      same asset. May be negative when exchange rebates exceed
                      the builder charge.
                    example: '2.25'
                    x-parser-schema-id: <anonymous-schema-515>
                  builder:
                    type: object
                    description: >-
                      Saved builder terms. Address is the registered Perps
                      account, and fee_rate is an additional fraction of
                      executed notional. Terms survive approval revocation for
                      existing orders.
                    required:
                      - address
                      - fee_rate
                    properties:
                      address:
                        type: string
                        description: Address
                        example: '0x1234567890abcdef1234567890abcdef12345678'
                        x-parser-schema-id: <anonymous-schema-517>
                      fee_rate:
                        type: string
                        description: >-
                          Additional builder fee as a decimal fraction of
                          executed notional, from 0 through 0.001 (10 basis
                          points). Zero approval revokes future admission. Never
                          a percentage string.
                        example: '0.001'
                        x-parser-schema-id: <anonymous-schema-518>
                    x-parser-schema-id: <anonymous-schema-516>
                  fea:
                    type: string
                    description: Fee asset name
                    example: USDC
                    x-parser-schema-id: <anonymous-schema-519>
                  psz:
                    type: string
                    description: Position size before the fill
                    example: '26.86'
                    x-parser-schema-id: <anonymous-schema-520>
                  pep:
                    type: string
                    description: Position entry price before the fill
                    example: '100.00'
                    x-parser-schema-id: <anonymous-schema-521>
                  pnl:
                    description: >-
                      Realized trading PnL before exchange and builder fees.
                      Subtract total_fee once to calculate this fill's net
                      trading result.
                    type: string
                    example: '100.00'
                    x-parser-schema-id: <anonymous-schema-522>
                  liq:
                    type: boolean
                    description: >-
                      Whether this fill was part of a liquidation of the
                      account's position — true on forced closes and on any fill
                      executed while the account was under liquidation on the
                      instrument, maker or taker. False on the counterparty leg
                      of an auto-deleveraging or backstop match — its fill is
                      part of someone else's liquidation, flagged by `adl` where
                      applicable
                    x-parser-schema-id: <anonymous-schema-523>
                  adl:
                    type: boolean
                    description: Whether the fill came from auto-deleveraging
                    x-parser-schema-id: <anonymous-schema-524>
                  ts:
                    type: integer
                    description: >-
                      Request timestamp. Unix milliseconds for most operations;
                      Unix seconds for withdrawals (must match the on-chain
                      EIP-712 struct verified against block.timestamp).
                    example: 1767225600000
                    x-parser-schema-id: <anonymous-schema-525>
                  settlement:
                    type: boolean
                    description: >-
                      Whether this fill closes a position during permanent
                      instrument settlement. Settlement fills use the final
                      settlement price and have no fees or liquidation
                      penalties; they are not normal market trades or ADL.
                    x-parser-schema-id: <anonymous-schema-526>
                  coid:
                    type: string
                    description: Client order ID
                    minLength: 32
                    maxLength: 32
                    pattern: ^[0-9a-f]{32}$
                    example: 550e8400e29b41d4a716446655440000
                    x-parser-schema-id: <anonymous-schema-527>
                  liquidation_details:
                    type: object
                    required:
                      - mark
                      - method
                    properties:
                      liquidated_user:
                        type: string
                        description: >-
                          Checksummed address of the liquidated account. Present
                          on authenticated fill surfaces and, on public
                          account-scoped routes, only on the liquidated
                          account's own rows. It is absent on fund-side public
                          rows and the anonymous trade tape.
                        x-parser-schema-id: <anonymous-schema-529>
                      mark:
                        type: string
                        description: >-
                          Mark price captured when the liquidation command was
                          issued. The fill price itself stays the accounting
                          price.
                        x-parser-schema-id: <anonymous-schema-530>
                      method:
                        type: string
                        enum:
                          - market
                          - backstop
                        description: >-
                          How the position was liquidated. Only backstop is
                          emitted today. The market value is reserved for
                          order-book liquidations, which currently carry no
                          liquidation_details.
                        x-parser-schema-id: <anonymous-schema-531>
                    x-parser-schema-id: <anonymous-schema-528>
                x-parser-schema-id: <anonymous-schema-505>
              x-parser-schema-id: <anonymous-schema-504>
          required:
            - ch
            - ts
            - sq
            - data
          x-parser-schema-id: <anonymous-schema-500>
        title: Update
        description: Real-time fill updates for authenticated users
        example: |-
          {
            "ch": "fills",
            "ts": 1767225600000,
            "ets": 1767225600000,
            "sq": 1234567890,
            "data": [
              {
                "tid": 1,
                "oid": 1234567890,
                "iid": 1,
                "side": "long",
                "p": "100.00",
                "qty": "10.00",
                "fee": "1.25",
                "builder_fee": "1.00",
                "total_fee": "2.25",
                "builder": {
                  "address": "0x1234567890abcdef1234567890abcdef12345678",
                  "fee_rate": "0.001"
                },
                "fea": "USDC",
                "psz": "26.86",
                "pep": "100.00",
                "pnl": "100.00",
                "ts": 1767225600000,
                "coid": "550e8400e29b41d4a716446655440000",
                "liquidation_details": {
                  "method": "market"
                }
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Update
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
  - *ref_2
receiveOperations:
  - *ref_3
  - *ref_4
  - *ref_5
sendMessages:
  - *ref_6
  - *ref_7
receiveMessages:
  - *ref_8
  - *ref_9
  - *ref_10
extensions:
  - id: x-parser-unique-object-id
    value: fills
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
