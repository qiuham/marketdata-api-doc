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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-trade-balance'
updated_at: 2026-11-13
---

# Get Trade Balance

> Retrieve a summary of collateral balances, margin position valuations, equity and margin level.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/TradeBalance
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
  /private/TradeBalance:
    post:
      tags:
        - Account Data
      summary: Get Trade Balance
      description: >
        Retrieve a summary of collateral balances, margin position valuations,
        equity and margin level.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getTradeBalance
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        $ref: '#/components/requestBodies/balance'
      responses:
        '200':
          description: Trade balances retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/balance-4'
                example:
                  error: []
                  result:
                    eb: '1101.3425'
                    tb: '392.2264'
                    m: '7.0354'
                    'n': '-10.0232'
                    c: '21.1063'
                    v: '31.1297'
                    e: '382.2032'
                    mf: '375.1678'
                    ml: '5432.57'
components:
  parameters:
    account_id:
      in: query
      name: account_id
      description: >-
        Public wallet account ID. Omit to use the authenticated user's default
        wallet. See [List Wallet
        Accounts](/api-reference/account-data/list-wallet-accounts).
      schema:
        type: string
      example: WX6V-JUKW-KKPB-QE36
      x-selected-account: true
      style: form
  requestBodies:
    balance:
      required: true
      content:
        application/json:
          schema:
            title: Update Account Profile Request
            description: Update Account Profile Request Body
            required:
              - nonce
            type: object
            properties:
              nonce:
                $ref: '#/components/schemas/nonce'
              asset:
                description: Base asset used to determine balance
                type: string
                default: ZUSD
              rebase_multiplier:
                $ref: '#/components/schemas/rebase_multiplier'
            example:
              nonce: 1695828490
              asset: ZUSD
  schemas:
    balance-4:
      type: object
      properties:
        result:
          $ref: '#/components/schemas/balance-3'
        error:
          $ref: '#/components/schemas/error'
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    rebase_multiplier:
      type: string
      enum:
        - rebased
        - base
      default: rebased
      nullable: true
      description: |
        Optional parameter for viewing xStocks data. 
        - `rebased`: Display in terms of underlying equity.
        - `base`: Display in terms of SPV tokens.
    balance-3:
      title: AccountBalance
      description: Account Balance
      type: object
      required:
        - eb
        - tb
        - m
        - uv
        - 'n'
        - c
        - v
        - e
        - mf
      properties:
        eb:
          description: Equivalent balance (combined balance of all currencies)
          type: string
          example: '3224744.0162'
        tb:
          description: Trade balance (combined balance of all equity currencies)
          type: string
          example: '3224744.0162'
        m:
          description: Margin amount of open positions
          type: string
          example: '0.0000'
        'n':
          description: Unrealized net profit/loss of open positions
          type: string
          example: '0.0000'
        c:
          description: Cost basis of open positions
          type: string
          example: '0.0000'
        v:
          description: Current floating valuation of open positions
          type: string
          example: '0.0000'
        e:
          description: 'Equity: `trade balance + unrealized net profit/loss`'
          type: string
          example: '3224744.0162'
        mf:
          description: >-
            Free margin: `Equity - initial margin (maximum margin available to
            open new positions)`
          type: string
          example: '3224744.0162'
        mfo:
          description: >-
            Margin free for orders: available margin that can be used for new
            orders
          type: string
          example: '3224744.0162'
        ml:
          description: >-
            Margin level: `(equity / initial margin) * 100`. Only present when
            margin positions are open.
          type: string
          nullable: true
          example: '0.0000'
        uv:
          description: 'Unexecuted value: Value of unfilled and partially filled orders'
          type: string
          example: '0.0000'
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
