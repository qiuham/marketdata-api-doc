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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-credit-lines'
updated_at: 2026-11-13
---

# Get Credit Lines

> Retrieve all credit line details for VIPs with this functionality.

**API Key Permissions Required:** `Funds permissions - Query`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/CreditLines
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
  /private/CreditLines:
    post:
      tags:
        - Account Data
      summary: Get Credit Lines
      description: |
        Retrieve all credit line details for VIPs with this functionality.

        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: getCreditLines
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                rebase_multiplier:
                  $ref: '#/components/schemas/rebase_multiplier'
              required:
                - nonce
      responses:
        '200':
          description: Credit line details retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/creditlines-2'
                example:
                  error: []
                  result:
                    asset_details:
                      USD:
                        balance: '1000.5000'
                        hold_trade: '0.0000'
                        credit: '50000.0000'
                        credit_used: '12500.0000'
                      EUR:
                        balance: '500.2500'
                        hold_trade: '100.0000'
                        credit: '25000.0000'
                        credit_used: '5000.0000'
                    limits_monitor:
                      total_credit_usd: '100000.0000'
                      total_credit_used_usd: '25000.0000'
                      total_collateral_value_usd: '150000.0000'
                      equity_usd: '125000.0000'
                      ongoing_balance: '1.5000'
                      debt_to_equity: '0.2000'
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
  schemas:
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
    creditlines-2:
      type: object
      properties:
        result:
          $ref: '#/components/schemas/creditlines'
          nullable: true
        error:
          $ref: '#/components/schemas/error'
    creditlines:
      title: CreditLines
      description: Credit Line Details
      type: object
      required:
        - asset_details
        - limits_monitor
      properties:
        asset_details:
          description: Balances by asset
          type: object
          additionalProperties:
            $ref: '#/components/schemas/creditlines-asset'
        limits_monitor:
          $ref: '#/components/schemas/creditlines-monitor'
          description: Credit monitor
          type: object
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
    creditlines-asset:
      title: CreditLinesAsset
      description: Credit line details for a specific asset
      type: object
      required:
        - balance
        - hold_trade
      properties:
        balance:
          description: Current balance for the asset
          type: string
          example: '1000.5000'
        hold_trade:
          description: Amount on hold for open orders
          type: string
          example: '0.0000'
        credit:
          description: >-
            Credit limit for the asset (present only for accounts with a credit
            line)
          type: string
          example: '50000.0000'
        credit_used:
          description: >-
            Currently used credit for the asset (present only for accounts with
            a credit line)
          type: string
          example: '12500.0000'
        collateral_value:
          description: >-
            Collateral value factor for this asset, from `0` to `1` (present for
            eligible collateral assets)
          type: number
          example: 0.99
        rollover_fees:
          description: >-
            Rollover rate charged on drawn credit, in percent per rollover
            period (present only for assets with a credit line)
          type: string
          example: '0.0055'
        reserve_fees:
          description: >-
            Reserve rate charged on undrawn credit, in percent per rollover
            period (present only for assets with a credit line)
          type: string
          example: '0.0038'
    creditlines-monitor:
      title: CreditLinesMonitor
      description: Credit monitor with summary information across all assets
      type: object
      properties:
        total_credit_usd:
          description: Total credit across all assets represented in USD
          type: string
          nullable: true
          example: '100000.0000'
        total_credit_used_usd:
          description: Total credit used across all assets represented in USD
          type: string
          nullable: true
          example: '25000.0000'
        total_collateral_value_usd:
          description: Sum of asset balance in USD * collateral
          type: string
          nullable: true
          example: '150000.0000'
        equity_usd:
          description: Total collateral - total credit (in USD)
          type: string
          nullable: true
          example: '125000.0000'
        ongoing_balance:
          description: Total collateral / total credit (in USD)
          type: string
          nullable: true
          example: '1.5000'
        debt_to_equity:
          description: Total credit used / equity (in USD)
          type: string
          nullable: true
          example: '0.2000'
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
