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
source_url: 'https://docs.kraken.com/api-reference/algo-trading/get-open-strategies'
updated_at: 2026-11-13
---

# Get Open Strategies

> Retrieve the account's active strategies, i.e. those with status `pending` or `open`. Strategies in a terminal state are returned by `GetClosedStrategies`.

When the request acts on a selected sub-account, only that sub-account's strategies are returned.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`. Results are limited to the key's own account.




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/GetOpenStrategies
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
  /private/GetOpenStrategies:
    post:
      tags:
        - Algo Trading
      summary: Get Open Strategies
      description: >
        Retrieve the account's active strategies, i.e. those with status
        `pending` or `open`. Strategies in a terminal state are returned by
        `GetClosedStrategies`.


        When the request acts on a selected sub-account, only that sub-account's
        strategies are returned.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`. Results are limited to the key's own account.
      operationId: getOpenStrategies
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/getOpenStrategies'
      responses:
        '200':
          description: Open strategies retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/getOpenStrategies-2'
              examples:
                One pending TWAP:
                  value:
                    error: []
                    result:
                      open:
                        ASPBVCI-6MKBA-QE4VF6:
                          strategy_id: ASPBVCI-6MKBA-QE4VF6
                          status: pending
                          details:
                            strategy_type: twap
                            side: buy
                            volume: '0.01000000'
                            filled_volume: '0'
                            avg_price: ''
                            total_cost: '0'
                            total_fee: '0'
                            starttm: '1781169958'
                            expiretm: '1781173558'
                            symbol: BTC/USD
                            asset_class: forex
                            ordertype: market
components:
  schemas:
    getOpenStrategies:
      title: Get Open Strategies Request Body
      required:
        - nonce
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        strategy_type:
          description: Restrict results to one strategy type. Omit to return all types.
          type: string
          enum:
            - twap
      example:
        nonce: 1781169958000
        strategy_type: twap
    getOpenStrategies-2:
      type: object
      properties:
        result:
          title: OpenStrategies
          type: object
          properties:
            open:
              description: >-
                Open strategies, keyed by `strategy_id`. Always present, may be
                empty.
              type: object
              additionalProperties:
                $ref: '#/components/schemas/algoStrategy'
                x-additionalPropertiesName: strategy_id
        error:
          $ref: '#/components/schemas/error'
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
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
