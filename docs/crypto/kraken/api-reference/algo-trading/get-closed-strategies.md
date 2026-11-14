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
source_url: 'https://docs.kraken.com/api-reference/algo-trading/get-closed-strategies'
updated_at: 2026-11-13
---

# Get Closed Strategies

> Retrieve strategies in a terminal state (`closed`, `expired` or `cancelled`) as an ordered array in `result.closed`. Strategies are returned newest first by closing time, or by opening time when `query_time_mode` is `open`.

This endpoint uses cursor-based pagination. Each page holds up to `limit` strategies (default and maximum `100`). While more results are available, the response includes `next_cursor`. Send it as `cursor` to fetch the next page. `next_cursor` is absent on the last page. Offset paging (`ofs`) and a total `count` are not supported. The cursor stores a sort position, not the filters, so repeat the original filters (`asset_class`, `strategy_type`, `status`, `start`, `end` and `query_time_mode`) on every page.

**API Key Permissions Required:** `Orders and trades - Query closed orders & trades`. Results are limited to the key's own account.




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/GetClosedStrategies
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
  /private/GetClosedStrategies:
    post:
      tags:
        - Algo Trading
      summary: Get Closed Strategies
      description: >
        Retrieve strategies in a terminal state (`closed`, `expired` or
        `cancelled`) as an ordered array in `result.closed`. Strategies are
        returned newest first by closing time, or by opening time when
        `query_time_mode` is `open`.


        This endpoint uses cursor-based pagination. Each page holds up to
        `limit` strategies (default and maximum `100`). While more results are
        available, the response includes `next_cursor`. Send it as `cursor` to
        fetch the next page. `next_cursor` is absent on the last page. Offset
        paging (`ofs`) and a total `count` are not supported. The cursor stores
        a sort position, not the filters, so repeat the original filters
        (`asset_class`, `strategy_type`, `status`, `start`, `end` and
        `query_time_mode`) on every page.


        **API Key Permissions Required:** `Orders and trades - Query closed
        orders & trades`. Results are limited to the key's own account.
      operationId: getClosedStrategies
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/getClosedStrategies'
            examples:
              Cancelled TWAPs in a time range:
                value:
                  nonce: 1781169958000
                  strategy_type: twap
                  status: cancelled
                  start: 1781100000
                  end: 1781200000
                  query_time_mode: close
                  limit: 50
              Next page:
                value:
                  nonce: 1781169958001
                  strategy_type: twap
                  status: cancelled
                  start: 1781100000
                  end: 1781200000
                  query_time_mode: close
                  limit: 50
                  cursor: Q0xPU0VEOjE3ODExNzAwMDA6QVNNQkE2NA
      responses:
        '200':
          description: Closed strategies retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/getClosedStrategies-2'
              examples:
                Page with more results:
                  value:
                    error: []
                    result:
                      closed:
                        - strategy_id: ASPBVCI-6MKBA-QE4VF6
                          status: cancelled
                          reason: userRequested
                          details:
                            strategy_type: twap
                            side: buy
                            volume: '1.50000000'
                            filled_volume: '0.80000000'
                            avg_price: '67098.42'
                            total_cost: '53678.74'
                            total_fee: '85.89'
                            starttm: '1781169958'
                            expiretm: '1781173558'
                            symbol: BTC/USD
                            asset_class: forex
                            ordertype: market
                        - strategy_id: ASMBA64-R23M2-J7JRJV
                          status: closed
                          details:
                            strategy_type: twap
                            side: sell
                            volume: '2.00000000'
                            filled_volume: '2.00000000'
                            avg_price: '67050.10'
                            total_cost: '134100.20'
                            total_fee: '214.56'
                            starttm: '1781166400'
                            expiretm: '1781170000'
                            symbol: BTC/USD
                            asset_class: forex
                            ordertype: limit
                            price: '67000.00'
                      next_cursor: Q0xPU0VEOjE3ODExNzAwMDA6QVNNQkE2NA
components:
  schemas:
    getClosedStrategies:
      title: Get Closed Strategies Request Body
      required:
        - nonce
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        asset_class:
          description: >-
            Restrict results to one asset class. Omit to return all asset
            classes. Repeat the same value on subsequent cursor pages.
          allOf:
            - $ref: '#/components/schemas/algoAssetClass'
        strategy_type:
          description: Restrict results to one strategy type. Omit to return all types.
          type: string
          enum:
            - twap
        status:
          description: Restrict results to one terminal status. Omit to return all three.
          type: string
          enum:
            - closed
            - expired
            - cancelled
        start:
          description: >-
            Inclusive lower bound in Unix seconds, applied according to
            query_time_mode. Omit or use 0 for no lower bound.
          type: integer
        end:
          description: >-
            Inclusive upper bound in Unix seconds, including the entire end
            second. Omit or use 0 for no upper bound.
          type: integer
        query_time_mode:
          description: >
            Which timestamps the bounds apply to:

            - `open`: both bounds apply to the persisted opening time, not the
            scheduled `starttm`.

            - `close`: both bounds apply to the time the strategy reached a
            terminal state.

            - `both`: `start` bounds the opening time and `end` bounds the
            closing time; both conditions must hold.

            Results are ordered newest first by opening time for `open`,
            otherwise by closing time.
          type: string
          enum:
            - open
            - close
            - both
          default: both
        limit:
          description: Maximum number of strategies per page.
          type: integer
          minimum: 1
          maximum: 100
          default: 100
        cursor:
          description: >-
            Opaque pagination token from `next_cursor` of the previous page.
            Omit for the first page. The cursor stores a sort position, not the
            filters, so repeat the original `asset_class`, `strategy_type`,
            `status`, `start`, `end` and `query_time_mode` on every page.
          type: string
    getClosedStrategies-2:
      type: object
      properties:
        result:
          title: ClosedStrategies
          type: object
          properties:
            closed:
              description: >-
                Terminal strategies, newest first by opening time when
                query_time_mode is open, otherwise by closing time.
              type: array
              items:
                $ref: '#/components/schemas/algoStrategy'
            next_cursor:
              description: >-
                Pass as `cursor` in the next request to fetch the following
                page. Only present when more results are available.
              type: string
        error:
          $ref: '#/components/schemas/error'
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    algoAssetClass:
      description: |
        Asset class of `symbol`:
          * `forex` = standard spot pairs, e.g. `BTC/USD`
          * `tokenized_asset` = tokenized asset pairs
          * `synthetic_pair` = synthetic pairs
      type: string
      enum:
        - forex
        - tokenized_asset
        - synthetic_pair
    algoStrategy:
      title: strategy_id
      description: Strategy info
      type: object
      properties:
        strategy_id:
          $ref: '#/components/schemas/algoStrategyId'
        status:
          description: |
            Status of the strategy
              * `pending` = accepted, waiting for `starttm`
              * `open` = running
              * `closed` = fully filled before `expiretm`
              * `expired` = `expiretm` reached before being fully filled
              * `cancelled` = cancelled by the user
          type: string
          enum:
            - pending
            - open
            - closed
            - expired
            - cancelled
        reason:
          description: >-
            Additional explanation of the current status, when applicable, such
            as `insufficientFunds`, `remainingBelowMinimum` or `userRequested`.
            May also qualify an open strategy.
          type: string
        details:
          $ref: '#/components/schemas/twapStrategyInfo'
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
    algoStrategyId:
      description: >-
        Kraken strategy identifier, assigned when the strategy is created.
        Always starts with `AS`.
      type: string
      pattern: ^AS[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{6}$
      example: ASMBA64-R23M2-J7JRJV
    twapStrategyInfo:
      title: TWAP
      description: TWAP strategy details and execution progress.
      type: object
      properties:
        strategy_type:
          $ref: '#/components/schemas/algoStrategyType'
        side:
          description: Direction of the strategy.
          type: string
          enum:
            - buy
            - sell
        volume:
          description: Total quantity of the strategy (base currency).
          type: string
        filled_volume:
          description: Quantity executed so far (base currency).
          type: string
        avg_price:
          description: >-
            Average execution price (`total_cost` / `filled_volume`). Empty
            string until the first fill.
          type: string
        total_cost:
          description: Total cost of the executed quantity (quote currency).
          type: string
        total_fee:
          description: >-
            Aggregate fees charged across fills, in quote currency. '0' before
            any fills.
          type: string
        starttm:
          description: Unix timestamp (seconds) of the strategy start time.
          type: string
        expiretm:
          description: Unix timestamp (seconds) of the strategy end time.
          type: string
        symbol:
          description: Asset pair, e.g. `BTC/USD`.
          type: string
        asset_class:
          $ref: '#/components/schemas/algoAssetClass'
        ordertype:
          description: Order type of the child orders.
          type: string
          enum:
            - market
            - limit
        price:
          description: >-
            Limit price of the child orders. Only present when `ordertype` is
            `limit`.
          type: string
    algoStrategyType:
      description: Strategy type. `twap` is the only supported value today.
      type: string
      enum:
        - twap
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
