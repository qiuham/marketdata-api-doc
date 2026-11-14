---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/api-reference/transparency/post-trade-data'
updated_at: 2026-11-13
---

# Post-Trade Data

> Returns a list of trades on the spot exchange. 
If no filter parameters are specified, the last 1000 trades for all pairs are received.




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/PostTrade
openapi: 3.0.0
info:
  title: REST API
  version: 1.1.0
  description: ''
servers:
  - url: https://api.kraken.com/0
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Market Data
  - name: Account Data
  - name: Trading
  - name: Algo Trading
    description: >
      Algo Trading endpoints create and manage **strategies**: parent
      instructions that Kraken executes on your behalf as a series of regular
      child orders.


      The only strategy available today is **TWAP** (time-weighted average
      price). A TWAP buys or sells a total `volume` evenly between `starttm` and
      `expiretm`. How child orders are sized, timed and placed is managed by
      Kraken and may change as execution improves.


      An algo runs as a strategy. In Kraken Pro, TWAP strategies show under
      Bots.


      ### Strategy lifecycle


      `pending` → `open` → `closed` | `expired` | `cancelled`


      - `pending`: accepted, waiting for `starttm`.

      - `open`: running, child orders are being placed.

      - `closed`: the full `volume` was filled before `expiretm`.

      - `expired`: `expiretm` was reached before the full `volume` was filled.

      - `cancelled`: cancelled with `CancelStrategy`.


      TWAP child orders are immediate-or-cancel limit orders and do not rest on
      the book. Completed child orders appear in `ClosedOrders`, and fills
      appear in trade history. Use the strategy endpoints to monitor overall
      progress.
  - name: funding-beta
    x-group: Funding (Beta)
    x-displayName: Funding (Beta)
  - name: Funding
    x-group: Funding (Legacy)
    x-displayName: Funding (Legacy)
  - name: Subaccounts
    description: >-
      Subaccounts are currently only available to institutional clients. Please
      contact your Account Manager for more details.
  - name: Earn
    description: >
      The earn API allows interacting with all of Kraken's yield generating
      products. It replaces the old `/staking` part of the API.


      The different available earn products are represented by earn strategies.
      This corresponds to the legacy `Staking/Assets`. `Stake`/`Unstake` are
      replaced by `Allocate`/`Deallocate`.


      ### Overview of the available endpoints under `/Earn`:


      - `Strategies` - list all earn strategies for which you are eligible or
      have a balance.

      - `Allocations` - lists the balance in your earn account for each
      strategy. Requires the `Query Funds` API key permission.

      - `Allocate`/`Deallocate` - allocate/deallocate to an earn strategy
      through an async operation. Requires the `Earn Funds` API key permission.

      - `AllocateStatus`/`DeallocateStatus` - verifies the state of the last
      allocation/deallocation. Requires the `Earn Funds` or `Query Funds` API
      key permission.


      ### Example usage:


      ### Determine which funds are earning rewards:


      1. Call `Strategies` to obtain information about the relevant strategy.
      The `lock_type` field shows whether bonding/unbonding funds are earning
      yield. The relevant fields are `bonding_rewards`/`unbonding_rewards`.

      2. Call `Allocations` for the relevant strategy. From the previous step,
      for strategies where bonding/unbonding does not earn yield, substract
      these balances from `amount_allocated.total` to determine which balances
      are currently earning.


      ### Get allocatable balance:


      Call `/0/private/BalanceEx`, subtract `hold_trading` amount. Remaining
      balance is available for allocation to a strategy.


      ### Geo restrictions:


      Some earn strategies are not available in all geographic regions.
      `Strategies` will return only strategies available to the caller.
  - name: Transparency
paths:
  /public/PostTrade:
    get:
      tags:
        - Transparency
      summary: Post-Trade Data
      description: >
        Returns a list of trades on the spot exchange. 

        If no filter parameters are specified, the last 1000 trades for all
        pairs are received.
      operationId: getPostTrade
      parameters:
        - name: symbol
          in: query
          required: false
          description: Filter the results to the currency pair.
          example: BTC/USD
          schema:
            type: string
        - name: from_ts
          in: query
          description: Filter the results to include the trades *after* this timestamp.
          required: false
          example: '2024-05-30T12:34:56.123456789Z'
          schema:
            type: string
            format: ISO 8601
        - name: to_ts
          in: query
          description: >-
            Filter the results to include the trades *before or at* this
            timestamp.
          required: false
          example: '2024-05-30T12:34:56.123456789Z'
          schema:
            type: string
            format: ISO 8601
        - name: count
          in: query
          required: false
          description: The maximum number of trades to return.
          schema:
            type: integer
            minimum: 1
            maximum: 1000
            default: 1000
      responses:
        '200':
          description: Post-trade data retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/post-trade'
      security: []
components:
  schemas:
    post-trade:
      title: PostTradeResponse
      description: >-
        A list of trades. A maximum of `count` trades will be returned in a
        single query, as specified in the query parameters.
      type: object
      properties:
        result:
          type: object
          properties:
            last_ts:
              type: string
              format: ISO 8601
              description: >
                Timestamp of the latest trade in the list. 

                This field can be used as the `from_ts` parameter when
                requesting the next batch of trades.
              example: '2024-05-30T12:34:56.123456789Z'
            count:
              type: integer
              description: The number of trades returned.
              minimum: 0
              maximum: 1000
            trades:
              type: array
              description: A list of trades in ascending timestamp order.
              items:
                type: object
                format: Trade
                minItems: 0
                maxItems: 1000
                properties:
                  trade_id:
                    type: string
                    maxLength: 19
                    description: Kraken unique trade identifier.
                    example: TGBB7L-HT5LX-J3BZ4A
                  price:
                    type: string
                    description: Trade price excluding fees and commissions.
                    example: '102002.1'
                  quantity:
                    type: string
                    description: Unconsolidated trade quantity from execution.
                    example: '1.24'
                  symbol:
                    type: string
                    maxLength: 32
                    description: The symbol of the currency pair.
                    example: BTC/USD
                  description:
                    type: string
                    maxLength: 350
                    description: The full description of the currency pair.
                    example: Bitcoin / US Dollars
                  base_asset:
                    type: string
                    format: ISO 4217
                    description: Currency code for the base asset.
                    example: BTC
                  base_notation:
                    type: string
                    description: Indicates that the quantity is expressed in nominal value.
                    enum:
                      - UNIT
                  quote_asset:
                    type: string
                    format: ISO 4217
                    description: Currency in which the trading price is expressed.
                    example: USD
                  quote_notation:
                    type: string
                    description: Indicates that the price is expressed in monetary value.
                    enum:
                      - MONE
                  trade_venue:
                    type: string
                    format: ISO 10383
                    maxLength: 12
                    description: >-
                      Market Identifier Code (MIC) of the trading platform where
                      the trade was executed.
                    example: PGSL
                  trade_ts:
                    type: string
                    format: ISO 8601
                    description: >-
                      Timestamp the trade was matched in the engine to
                      microsecond precision.
                    example: '2024-05-30T12:34:56.123456789Z'
                  publication_venue:
                    type: string
                    format: ISO 10383
                    maxLength: 12
                    description: >-
                      Market Identifier Code (MIC) of the trading platform where
                      the trade was published.
                    example: PGSL
                  publication_ts:
                    type: string
                    format: ISO 8601
                    description: Timestamp the trade was published to market data streams.
                    example: '2024-05-30T12:34:56.123456789Z'
        error:
          $ref: '#/components/schemas/error'
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
  securitySchemes:
    API-Key:
      type: apiKey
      description: The "API-Key" header should contain your API key.
      name: API-Key
      in: header
    API-Sign:
      type: apiKey
      description: >-
        Authenticated requests should be signed with the "API-Sign" header,
        using a signature generated with your private key, nonce, encoded
        payload, and URI path.
      name: API-Sign
      in: header

````
