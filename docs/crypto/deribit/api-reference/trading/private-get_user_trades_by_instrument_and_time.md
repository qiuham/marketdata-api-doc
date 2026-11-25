---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_instrument_and_time
api_type: JSON-RPC
updated_at: 2026-11-25 19:00:50.352626
---

# private/get_user_trades_by_instrument_and_time

> Retrieves the latest user trades that have occurred for a specific instrument within a specified time range. Returns trade details including price, amount, direction, timestamp, trade ID, and order ID.

Use the `count` parameter to limit the number of trades returned, and `sorting` to control the order (ascending or descending by trade ID). Use `historical` to retrieve historical trade data. This method is useful for analyzing trading activity over specific time periods.

Main accounts may use the `subaccount_id` parameter to retrieve trade data for a specific subaccount (requires `mainaccount` scope).

**📖 Related Article:** [Accessing Historical Trades and Orders Using API](https://docs.deribit.com/articles/accessing-historical-trades-orders)

**Scope:** `trade:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_user_trades_by_instrument_and_time)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_user_trades_by_instrument_and_time
openapi: 3.0.0
info:
  title: Deribit API
  version: 2.1.1
servers:
  - url: https://test.deribit.com/api/v2
security: []
tags:
  - name: WebSocket Only
    description: Can only be used over websockets.
  - name: Public
    description: Public methods can be used without authentication.
  - name: Private
    description: >-
      <p>Private methods require authentication. All requests must include a
      valid OAuth2 token.</p>

      <p>A token can be requested using the <a
      href="#public-auth">/public/auth</a> method.</p>

      <p>When using the websockets protocol, the token must be included as a
      parameter <code>access_token</code> in the message. When using REST (HTTP
      GET), the token may also be passed in the <code>Authorization</code>
      header.</p>
  - name: Authentication
  - name: Session Management
  - name: Subscription Management
    description: >-
      Subscription works as [notifications](#notifications), so users will
      automatically (after subscribing) receive messages from the server.
      Overview for each channel response format is described in
      [subscriptions](#subscriptions) section.
  - name: Account Management
  - name: Trading
  - name: Market Data
  - name: Wallet
  - name: Chat
  - name: lsp
    description: >-
      Methods and notifications for the Liquidity Support Program (LSP), the
      mechanism that assigns risk from liquidated positions to designated LSP
      participant subaccounts before falling back to auto-deleveraging (ADL).
paths:
  /private/get_user_trades_by_instrument_and_time:
    get:
      tags:
        - Trading
        - Private
      description: >+
        Retrieves the latest user trades that have occurred for a specific
        instrument within a specified time range. Returns trade details
        including price, amount, direction, timestamp, trade ID, and order ID.


        Use the `count` parameter to limit the number of trades returned, and
        `sorting` to control the order (ascending or descending by trade ID).
        Use `historical` to retrieve historical trade data. This method is
        useful for analyzing trading activity over specific time periods.


        Main accounts may use the `subaccount_id` parameter to retrieve trade
        data for a specific subaccount (requires `mainaccount` scope).


        **📖 Related Article:** [Accessing Historical Trades and Orders Using
        API](https://docs.deribit.com/articles/accessing-historical-trades-orders)


        **Scope:** `trade:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_user_trades_by_instrument_and_time)

      parameters:
        - name: instrument_name
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/instrument_name'
          description: Instrument name
        - name: start_timestamp
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/timestamp'
          description: >-
            Inclusive earliest timestamp (milliseconds since the Unix epoch).
            Time-based methods require at least one of start_timestamp or
            end_timestamp.
        - name: end_timestamp
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/timestamp'
          description: >-
            Inclusive latest timestamp (milliseconds since the Unix epoch).
            Time-based methods require at least one of start_timestamp or
            end_timestamp.
        - name: count
          required: false
          in: query
          schema:
            type: integer
            maximum: 1000
            minimum: 1
          description: Number of requested items, default - `10`, maximum - `1000`
        - name: sorting
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/sorting'
          description: 'Result ordering: asc, desc, or the method-specific default.'
        - name: historical
          in: query
          required: false
          schema:
            type: boolean
          description: >
            Determines whether historical trade and order records should be
            retrieved.


            - `false` (default): Returns recent records: orders for 30 min,
            trades for 24h.

            - `true`: Fetches historical records, available after a short delay
            due to indexing. Recent data is not included.


            **📖 Related Article:** [Accessing Historical Trades and Orders
            Using
            API](https://docs.deribit.com/articles/accessing-historical-trades-orders)
        - name: subaccount_id
          in: query
          required: false
          schema:
            type: integer
            example: 9
          description: Id of a subaccount
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 276
                  method: private/get_user_trades_by_instrument_and_time
                  params:
                    instrument_name: BTC-PERPETUAL
                    start_timestamp: 1590470872894
                    end_timestamp: 1590480872894
                    count: 2
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetUserTradesHistoryResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 276
                    result:
                      trades:
                        - trade_seq: 30289127
                          trade_id: '48078944'
                          timestamp: 1590480866924
                          tick_direction: 2
                          state: filled
                          reduce_only: false
                          price: 8988.5
                          post_only: false
                          order_type: limit
                          order_id: '4008716877'
                          matching_id: null
                          mark_price: 8990.52
                          liquidity: T
                          instrument_name: BTC-PERPETUAL
                          index_price: 8995.15
                          fee_currency: BTC
                          fee: 0.00037465
                          direction: sell
                          amount: 4490
                        - trade_seq: 30289128
                          trade_id: '48078945'
                          timestamp: 1590480866924
                          tick_direction: 2
                          state: filled
                          reduce_only: false
                          price: 8983.5
                          post_only: false
                          order_type: limit
                          order_id: '4008716877'
                          matching_id: null
                          mark_price: 8990.52
                          liquidity: T
                          instrument_name: BTC-PERPETUAL
                          index_price: 8995.15
                          fee_currency: BTC
                          fee: 0.00001503
                          direction: sell
                          amount: 180
                      has_more: true
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_user_trades_by_instrument_and_time \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 276,
              "method": "private/get_user_trades_by_instrument_and_time",
              "params": {
                "instrument_name": "BTC-PERPETUAL",
                "start_timestamp": 1590470872894,
                "end_timestamp": 1590480872894,
                "count": 2
              }
            }'
components:
  schemas:
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    sorting:
      enum:
        - asc
        - desc
        - default
      type: string
    PrivateGetUserTradesHistoryResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          type: object
          properties:
            trades:
              type: array
              items:
                $ref: '#/components/schemas/user_trade'
            has_more:
              type: boolean
          required:
            - trades
            - has_more
      required:
        - result
        - jsonrpc
      type: object
    user_trade:
      properties:
        trade_id:
          $ref: '#/components/schemas/trade_id'
        trade_seq:
          $ref: '#/components/schemas/trade_seq'
        instrument_name:
          $ref: '#/components/schemas/instrument_name'
        timestamp:
          $ref: '#/components/schemas/trade_timestamp'
        starbase_timestamp:
          $ref: '#/components/schemas/starbase_timestamp'
          description: >-
            Optional field: the Starbase causal timestamp of the trade, in
            nanoseconds since the UNIX epoch (present only for trades matched in
            Starbase)
        starbase_order_id:
          type: integer
          example: 103148386170
          description: >-
            Raw Starbase order id of the user's order, in Starbase's own (non
            currency-prefixed) id namespace (present only for trades matched in
            Starbase)
        starbase_client_order_id:
          type: string
          description: >-
            Client order id of the user's own order (maker or taker side)
            submitted directly to
            [Starbase](https://docs.deribit.com/starbase/overview) via direct
            access; not returned for orders placed through the Deribit API; for
            self-trades this is the taker order's client order id
        order_type:
          type: string
          enum:
            - limit
            - market
            - liquidation
          description: 'Order type: `"limit"`, `"market"`, or `"liquidation"`'
        original_order_type:
          $ref: '#/components/schemas/original_order_type'
        advanced:
          type: string
          enum:
            - usd
            - implv
          description: >-
            Advanced type of user order: `"usd"` or `"implv"` (only for options;
            omitted if not applicable)
        order_id:
          type: string
          nullable: true
          description: >-
            Id of the user order (maker or taker), i.e. subscriber's order id
            that took part in the trade
        matching_id:
          type: string
          nullable: true
          description: Matched order id for self-trades; null otherwise.
        direction:
          $ref: '#/components/schemas/direction'
          description: Trade direction of the user
        tick_direction:
          $ref: '#/components/schemas/tick_direction'
        index_price:
          type: number
          description: Index Price at the moment of trade
        price:
          $ref: '#/components/schemas/price'
          description: The price of the trade
        amount:
          type: number
          description: >-
            Trade amount. For perpetual and inverse futures the amount is in USD
            units. For options and linear futures it is the underlying base
            currency coin.
        contracts:
          type: number
          description: >-
            Trade size in contract units (optional, may be absent in historical
            trades)
        iv:
          type: number
          description: Option implied volatility for the price (Option only)
        underlying_price:
          type: number
          description: Underlying price for implied volatility calculations (Options only)
        liquidation:
          type: string
          enum:
            - M
            - T
            - MT
          description: >-
            Optional field (only for trades caused by liquidation): `"M"` when
            maker side of trade was under liquidation, `"T"` when taker side was
            under liquidation, `"MT"` when both sides of trade were under
            liquidation
        liquidity:
          type: string
          enum:
            - M
            - T
          description: >-
            Describes what was role of users order: `"M"` when it was maker
            order, `"T"` when it was taker order
        fee:
          type: number
          description: User's fee in units of the specified `fee_currency`
        fee_currency:
          $ref: '#/components/schemas/currency'
        label:
          $ref: '#/components/schemas/label_presentation'
        state:
          $ref: '#/components/schemas/order_state_in_user_trade'
        block_trade_id:
          $ref: '#/components/schemas/block_trade_id_in_result'
        block_trade_leg_count:
          $ref: '#/components/schemas/block_trade_leg_count'
        block_delayed:
          $ref: '#/components/schemas/block_delayed'
        block_rfq_id:
          type: integer
          description: ID of the Block RFQ - when trade was part of the Block RFQ
        block_rfq_quote_id:
          type: integer
          description: ID of the Block RFQ quote - when trade was part of the Block RFQ
        reduce_only:
          type: boolean
          description: '`true` if user order is reduce-only; omitted for spot trades.'
        post_only:
          type: boolean
          description: '`true` if user order is post-only'
        mmp:
          type: boolean
          description: '`true` if user order is MMP'
        risk_reducing:
          type: boolean
          description: >-
            `true` if user order is marked by the platform as a risk reducing
            order (can apply only to orders placed by PM users)
        api:
          type: boolean
          description: '`true` if user order was created with API'
        profit_loss:
          $ref: '#/components/schemas/profit_loss'
        mark_price:
          type: number
          nullable: true
          description: Mark Price at the moment of trade
        legs:
          type: array
          description: >-
            Optional field containing leg trades if trade is a combo trade
            (present when querying for **only** combo trades and in
            `combo_trades` events). Each leg trade has the same fields as a
            top-level user trade, including `starbase_match_id`,
            `starbase_order_id`, and `starbase_timestamp` when matched in
            Starbase, and `starbase_client_order_id` for orders submitted via
            [Starbase](https://docs.deribit.com/starbase/overview) direct
            access.
        combo_id:
          type: string
          description: >-
            Optional field containing combo instrument name if the trade is a
            combo trade
        combo_trade_id:
          type: string
          description: >-
            Optional field containing combo trade identifier if the trade is a
            combo trade
        starbase_match_id:
          type: integer
          description: >-
            Optional field containing the Starbase match identifier (present
            only for trades matched via Starbase)
        quote_set_id:
          type: string
          description: >-
            QuoteSet of the user order (optional, present only for orders placed
            with `private/mass_quote`)
        quote_id:
          type: string
          description: >-
            QuoteID of the user order (optional, present only for orders placed
            with `private/mass_quote`)
        trade_allocations:
          type: array
          items:
            type: object
            properties:
              user_id:
                type: integer
                description: >-
                  User ID to which part of the trade is allocated. For brokers
                  the User ID is obstructed.
              amount:
                type: number
                description: Amount allocated to this user.
              fee:
                type: number
                description: Fee for the allocated part of the trade.
              client_info:
                type: object
                properties:
                  client_id:
                    type: integer
                    description: >-
                      ID of a client; available to broker. Represents a group of
                      users under a common name.
                  client_link_id:
                    type: integer
                    description: >-
                      ID assigned to a single user in a client; available to
                      broker.
                  name:
                    type: string
                    description: >-
                      Name of the linked user within the client; available to
                      broker.
                description: Optional client allocation info for brokers.
            required:
              - amount
              - fee
          description: >-
            List of allocations for Block RFQ pre-allocation. Each allocation
            specifies `user_id`, `amount`, and `fee` for the allocated part of
            the trade. For broker client allocations, a `client_info` object
            will be included.
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
    trade_id:
      type: string
      description: Unique (per currency) trade identifier
    trade_seq:
      type: integer
      description: The sequence number of the trade within instrument
    trade_timestamp:
      example: 1517329113791
      type: integer
      description: The timestamp of the trade (milliseconds since the UNIX epoch)
    starbase_timestamp:
      example: 1536569522277000000
      type: integer
      description: >-
        The Starbase causal timestamp of the trade (nanoseconds since the Unix
        epoch)
    original_order_type:
      enum:
        - market
        - market_limit
      type: string
      description: >-
        Original API order type when an order is represented internally as a
        limit order. For example, Starbase market orders use `"limit"` as
        `order_type` with `"market"` in this optional field.
    direction:
      enum:
        - buy
        - sell
      type: string
      description: 'Direction: `buy`, or `sell`'
    tick_direction:
      enum:
        - 0
        - 1
        - 2
        - 3
      type: integer
      description: >-
        Direction of the "tick" (`0` = Plus Tick, `1` = Zero-Plus Tick, `2` =
        Minus Tick, `3` = Zero-Minus Tick).
    price:
      type: number
      description: >-
        Price in the instrument's price units (quote currency for futures and
        spot).
    currency:
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
      type: string
      description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
    label_presentation:
      type: string
      description: >-
        User defined label (presented only when previously set for order by
        user)
    order_state_in_user_trade:
      enum:
        - open
        - filled
        - rejected
        - cancelled
        - untriggered
        - archive
      type: string
      description: >-
        Order state: `"open"`, `"filled"`, `"rejected"`, `"cancelled"`,
        `"untriggered"` or `"archive"` (if order was archived)
    block_trade_id_in_result:
      example: '154'
      type: string
      description: ID of the Block Trade or Block RFQ trade, when the trade was part of one
    block_trade_leg_count:
      example: 3
      type: integer
      description: >-
        Number of legs in the Block Trade or Block RFQ trade, when the trade was
        part of one
    block_delayed:
      example: 1730827181502
      type: integer
      description: >-
        Optional field (only for Block RFQ trades with delayed publication): the
        time the trade is published to public data feeds, in milliseconds since
        the UNIX epoch. Until then, the trade is returned only to its
        counterparties and is not included in public trades or the Block RFQ
        trade tape. The trade never updates the ticker `last_price` or tick
        direction, or the 24-hour `high`, `low` and `price_change`; its volume
        is reported in `volume_delayed`.
    profit_loss:
      type: number
      description: Profit and loss in base currency.

````

## Related topics

- [Accessing Historical Trades and Orders Using API](https://docs.deribit.com/articles/accessing-historical-trades-orders.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [private/get_user_trades_by_instrument](https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_instrument.md)
- [private/get_user_trades_by_currency_and_time](https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_currency_and_time.md)
- [private/get_user_trades_by_currency](https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_currency.md)