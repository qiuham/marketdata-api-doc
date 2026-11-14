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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-extended-balance'
updated_at: 2026-11-13
---

# Get Extended Balance

> Retrieve all extended account balances, including credits and held amounts. Balance available for trading is calculated as: `available balance = balance + credit - credit_used - hold_trade`

Note that held amounts only include spot non margin orders.

**Note on Staking/Earn assets:** We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our [Support article](https://support.kraken.com/hc/en-us/articles/360039879471-What-is-Asset-S-and-Asset-M-) for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g. `USDT` to transact with your `USDT` and `USDT.F` balances).

**Symbol Extensions**:
* `.B`: balances in new yield-bearing products, similar to `.S` (staked) and `.M` (opt-in rewards) balances
* `.F`: balances earning automatically in Kraken Rewards
* `.T`: tokenized assets.

**API Key Permissions Required:** `Funds permissions - Query`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/BalanceEx
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
  /private/BalanceEx:
    post:
      tags:
        - Account Data
      summary: Get Extended Balance
      description: >
        Retrieve all extended account balances, including credits and held
        amounts. Balance available for trading is calculated as: `available
        balance = balance + credit - credit_used - hold_trade`


        Note that held amounts only include spot non margin orders.


        **Note on Staking/Earn assets:** We have begun to migrate assets from
        our legacy Staking system over to a new Earn system. As such, the
        following assets may appear in your balances and ledger. Please see our
        [Support
        article](https://support.kraken.com/hc/en-us/articles/360039879471-What-is-Asset-S-and-Asset-M-)
        for more details. Note that these assets are "read-only", to interact
        with your balances in them please use the base asset (e.g. `USDT` to
        transact with your `USDT` and `USDT.F` balances).


        **Symbol Extensions**:

        * `.B`: balances in new yield-bearing products, similar to `.S` (staked)
        and `.M` (opt-in rewards) balances

        * `.F`: balances earning automatically in Kraken Rewards

        * `.T`: tokenized assets.


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: getExtendedBalance
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
          description: Extended account balances retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/balanceex-2'
                example:
                  error: []
                  result:
                    ZUSD:
                      balance: 25435.21
                      hold_trade: 8249.76
                    XXBT:
                      balance: 1.2435
                      hold_trade: 0.8423
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
    balanceex-2:
      type: object
      properties:
        result:
          title: ExtendedBalance
          description: >-
            Extended balances keyed by asset. An empty object is returned when
            the account holds no assets.
          type: object
          additionalProperties:
            $ref: '#/components/schemas/balanceex'
            x-additionalPropertiesName: asset
        error:
          $ref: '#/components/schemas/error'
    balanceex:
      title: ExtendedBalance
      description: Extended Balance
      type: object
      required:
        - balance
        - hold_trade
      properties:
        balance:
          description: Total balance amount for an asset
          type: string
          example: '3.46840030'
        credit:
          description: Total credit amount. Only present if the account has a credit line.
          type: string
          example: '1.26844502'
        credit_used:
          description: Used credit amount. Only present if the account has a credit line.
          type: string
          example: '0.10002300'
        hold_trade:
          description: Total held amount for an asset
          type: string
          example: '2.14560458'
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
