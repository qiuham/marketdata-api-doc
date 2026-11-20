---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_instrument_and_time
api_type: JSON-RPC
updated_at: 2026-11-20 19:00:14.284759
---

# public/get_last_trades_by_instrument_and_time

> Retrieves the latest trades that have occurred for a specific instrument within a specified time range. Returns trade details including price, amount, direction, timestamp, and trade ID.

Use the `count` parameter to limit the number of trades returned, and `sorting` to control the order (ascending or descending by trade ID). This method is useful for analyzing trading activity over specific time periods.

**Note:** Block RFQ trades with delayed publication are returned only after their publication time (`block_delayed`). They keep their original `timestamp` and `trade_seq`, so results for a past time or sequence range can gain trades after publication.

**Note:** For spot instruments routed to Coinbase Exchange, this call is not supported. Use [Get product trades](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-trades) directly for full trade history.

**📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_last_trades_by_instrument_and_time)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_last_trades_by_instrument_and_time
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
  /public/get_last_trades_by_instrument_and_time:
    get:
      tags:
        - Market Data
        - Public
      description: >+
        Retrieves the latest trades that have occurred for a specific instrument
        within a specified time range. Returns trade details including price,
        amount, direction, timestamp, and trade ID.


        Use the `count` parameter to limit the number of trades returned, and
        `sorting` to control the order (ascending or descending by trade ID).
        This method is useful for analyzing trading activity over specific time
        periods.


        **Note:** Block RFQ trades with delayed publication are returned only
        after their publication time (`block_delayed`). They keep their original
        `timestamp` and `trade_seq`, so results for a past time or sequence
        range can gain trades after publication.


        **Note:** For spot instruments routed to Coinbase Exchange, this call is
        not supported. Use [Get product
        trades](https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-trades)
        directly for full trade history.


        **📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed
        Instruments](https://docs.deribit.com/articles/spot-trading-venues)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_last_trades_by_instrument_and_time)

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
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 3983
                  method: public/get_last_trades_by_instrument_and_time
                  params:
                    instrument_name: ETH-PERPETUAL
                    end_timestamp: 1590480022768
                    count: 1
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicTradesHistoryResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 3983
                    result:
                      trades:
                        - trade_seq: 1966031
                          trade_id: ETH-2696055
                          timestamp: 1590479408216
                          tick_direction: 0
                          price: 203.6
                          mark_price: 203.41
                          instrument_name: ETH-PERPETUAL
                          index_price: 203.45
                          direction: buy
                          amount: 10
                      has_more: true
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_last_trades_by_instrument_and_time \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 3983,
              "method": "public/get_last_trades_by_instrument_and_time",
              "params": {
                "instrument_name": "ETH-PERPETUAL",
                "end_timestamp": 1590480022768,
                "count": 1
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
    PublicTradesHistoryResponse:
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
                $ref: '#/components/schemas/public_trade'
            has_more:
              type: boolean
          required:
            - trades
            - has_more
      required:
        - result
        - jsonrpc
      type: object
    public_trade:
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
        direction:
          $ref: '#/components/schemas/direction'
          description: Trade direction of the taker
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
        mark_price:
          type: number
          nullable: true
          description: Mark Price at the moment of trade
        block_trade_id:
          $ref: '#/components/schemas/block_trade_id_in_result'
        block_trade_leg_count:
          $ref: '#/components/schemas/block_trade_leg_count'
        block_delayed:
          $ref: '#/components/schemas/block_delayed'
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
        block_rfq_id:
          type: integer
          description: ID of the Block RFQ - when trade was part of the Block RFQ
        legs:
          type: array
          items:
            $ref: '#/components/schemas/public_trade'
          description: Leg trades, present when querying only combo trades.
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

````

## Related topics

- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Market Data Collection](https://docs.deribit.com/articles/market-data-collection-best-practices.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [public/get_last_trades_by_instrument](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_instrument.md)