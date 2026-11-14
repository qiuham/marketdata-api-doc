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
source_url: 'https://docs.kraken.com/api-reference/algo-trading/add-strategy'
updated_at: 2026-11-13
---

# Add Strategy

> Create a new algorithmic strategy. The only supported `strategy_type` today is `twap`.

A TWAP executes the total `volume` evenly between `starttm` and `expiretm`, as `market` or `limit` child orders. The response returns the `strategy_id`. Use it with `CancelStrategy` and `QueryStrategies`.

**Validation rules**

- The resolved time horizon (`expiretm` − `starttm`) must be at least **60 seconds**. Both `starttm` and `expiretm` must be no more than **30 days from now**.
- `expiretm` must be in the future.
- `price` is required when `ordertype` is `limit`, and must be omitted when `ordertype` is `market`.
- `symbol`, `volume` and `price` follow the same pair, precision and order minimum rules as [Add Order](/api-reference/trading/add-order).
- xStocks pairs are not supported.

Set `validate` to `true` to validate the request without creating or submitting the strategy to the execution engine. The response returns an empty `strategy_id`. This does not run the creation-time balance check or guarantee that a subsequent creation request will succeed.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/AddStrategy
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
  /private/AddStrategy:
    post:
      tags:
        - Algo Trading
      summary: Add Strategy
      description: >
        Create a new algorithmic strategy. The only supported `strategy_type`
        today is `twap`.


        A TWAP executes the total `volume` evenly between `starttm` and
        `expiretm`, as `market` or `limit` child orders. The response returns
        the `strategy_id`. Use it with `CancelStrategy` and `QueryStrategies`.


        **Validation rules**


        - The resolved time horizon (`expiretm` − `starttm`) must be at least
        **60 seconds**. Both `starttm` and `expiretm` must be no more than **30
        days from now**.

        - `expiretm` must be in the future.

        - `price` is required when `ordertype` is `limit`, and must be omitted
        when `ordertype` is `market`.

        - `symbol`, `volume` and `price` follow the same pair, precision and
        order minimum rules as [Add Order](/api-reference/trading/add-order).

        - xStocks pairs are not supported.


        Set `validate` to `true` to validate the request without creating or
        submitting the strategy to the execution engine. The response returns an
        empty `strategy_id`. This does not run the creation-time balance check
        or guarantee that a subsequent creation request will succeed.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`
      operationId: addStrategy
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/addStrategy'
            examples:
              TWAP limit buy over 1 hour:
                value:
                  nonce: 1781169958000
                  symbol: BTC/USD
                  asset_class: forex
                  strategy_type: twap
                  side: buy
                  volume: '1.5'
                  ordertype: limit
                  price: '67000.0'
                  expiretm: '+3600'
              TWAP market sell starting in 5 minutes:
                value:
                  nonce: 1781169958000
                  symbol: ETH/USD
                  asset_class: forex
                  strategy_type: twap
                  side: sell
                  volume: '10'
                  ordertype: market
                  starttm: '+300'
                  expiretm: '+7500'
              Validate only:
                value:
                  nonce: 1781169958000
                  symbol: BTC/USD
                  asset_class: forex
                  validate: true
                  strategy_type: twap
                  side: buy
                  volume: '0.01'
                  ordertype: market
                  expiretm: '+600'
      responses:
        '200':
          description: Strategy accepted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/addStrategy-2'
              examples:
                Strategy created:
                  value:
                    error: []
                    result:
                      strategy_id: ASMBA64-R23M2-J7JRJV
                Validate only:
                  value:
                    error: []
                    result:
                      strategy_id: ''
components:
  schemas:
    addStrategy:
      title: Add Strategy Request Body
      required:
        - nonce
        - strategy_type
        - symbol
        - asset_class
        - side
        - volume
        - ordertype
        - expiretm
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        strategy_type:
          $ref: '#/components/schemas/algoStrategyType'
        symbol:
          description: Asset pair `id` or `altname`, e.g. `BTC/USD` or `XBTUSD`.
          type: string
        asset_class:
          description: >-
            Standard spot pairs. Tokenized assets and synthetic pairs are not
            supported for Spot TWAP creation.
          type: string
          enum:
            - forex
        validate:
          description: >-
            If `true`, validate the request without creating or submitting the
            strategy. The response returns an empty `strategy_id`. The
            creation-time balance check is not run.
          type: boolean
          default: false
        side:
          description: Direction of the strategy.
          type: string
          enum:
            - buy
            - sell
        volume:
          description: >-
            Total quantity to execute over the strategy horizon, in base
            currency.
          type: string
        ordertype:
          description: |
            Order type of the child orders:
              * `market` = child orders execute at the market price
              * `limit` = child orders are limited by `price`
          type: string
          enum:
            - market
            - limit
        price:
          description: >-
            Limit price of the child orders. Required when `ordertype` is
            `limit`. Must be omitted when `ordertype` is `market`.
          type: string
        starttm:
          description: >
            Strategy start time. Defaults to now. Must be no more than 30 days
            from now.
              * `0` = now (default)
              * `+<n>` = start `<n>` seconds from now
              * `<n>` = unix timestamp (seconds) of the start time
          type: string
          default: '0'
        expiretm:
          description: >
            Strategy end time. Must be in the future, at least 60 seconds after
            the resolved `starttm`, and no more than 30 days from now.
              * `+<n>` = end `<n>` seconds from now
              * `<n>` = unix timestamp (seconds) of the end time
          type: string
    addStrategy-2:
      type: object
      properties:
        result:
          title: StrategyAdded
          type: object
          properties:
            strategy_id:
              description: >-
                Identifier of the new strategy. Empty string when `validate` is
                `true`.
              type: string
        error:
          $ref: '#/components/schemas/error'
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    algoStrategyType:
      description: Strategy type. `twap` is the only supported value today.
      type: string
      enum:
        - twap
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
