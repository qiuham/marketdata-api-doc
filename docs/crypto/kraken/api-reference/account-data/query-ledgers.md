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
source_url: 'https://docs.kraken.com/api-reference/account-data/query-ledgers'
updated_at: 2026-11-13
---

# Query Ledgers

> Retrieve information about specific ledger entries. 

> **Note on Staking/Earn assets:** We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our [Support article](https://support.kraken.com/hc/en-us/articles/360039879471-What-is-Asset-S-and-Asset-M-) for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g. `USDT` to transact with your `USDT` and `USDT.F` balances).
> * `.B`, which represents balances in new yield-bearing products, similar to `.S` (staked) and `.M` (opt-in rewards) balances
> * `.F`, which represents balances earning automatically in Kraken Rewards

**API Key Permissions Required:** `Data - Query ledger entries`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/QueryLedgers
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
  /private/QueryLedgers:
    post:
      tags:
        - Account Data
      summary: Query Ledgers
      description: >
        Retrieve information about specific ledger entries. 


        > **Note on Staking/Earn assets:** We have begun to migrate assets from
        our legacy Staking system over to a new Earn system. As such, the
        following assets may appear in your balances and ledger. Please see our
        [Support
        article](https://support.kraken.com/hc/en-us/articles/360039879471-What-is-Asset-S-and-Asset-M-)
        for more details. Note that these assets are "read-only", to interact
        with your balances in them please use the base asset (e.g. `USDT` to
        transact with your `USDT` and `USDT.F` balances).

        > * `.B`, which represents balances in new yield-bearing products,
        similar to `.S` (staked) and `.M` (opt-in rewards) balances

        > * `.F`, which represents balances earning automatically in Kraken
        Rewards


        **API Key Permissions Required:** `Data - Query ledger entries`
      operationId: getLedgersInfo
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        $ref: '#/components/requestBodies/query-2'
      responses:
        '200':
          description: Ledgers info retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/query-3'
                example:
                  error: []
                  result:
                    L4UESK-KG3EQ-UFO4T5:
                      refid: TJKLXF-PGMUI-4NTLXU
                      time: 1688464484.1787
                      type: trade
                      subtype: ''
                      aclass: currency
                      asset: ZGBP
                      amount: '-24.5000'
                      fee: '0.0490'
                      balance: '459567.9171'
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
    query-2:
      required: true
      content:
        application/json:
          schema:
            title: Get Ledger Info Request Body
            required:
              - nonce
              - id
            type: object
            properties:
              nonce:
                $ref: '#/components/schemas/nonce'
              id:
                description: >-
                  Comma delimited list of ledger IDs to query info about (20
                  maximum)
                type: string
              trades:
                description: >-
                  Whether or not to include trades related to position in
                  output. Deprecated, do not rely on this parameter.
                type: boolean
                default: false
                deprecated: true
              rebase_multiplier:
                $ref: '#/components/schemas/rebase_multiplier'
            example:
              nonce: 1695828490
              id: LUI2RA-CJFLB-EN5I4P, L2QE42-IGSZ3-WEVTLK
  schemas:
    query-3:
      type: object
      properties:
        result:
          type: object
          additionalProperties:
            x-additionalPropertiesName: ledger_id
            allOf:
              - $ref: '#/components/schemas/ledger'
              - type: object
                properties:
                  amount_token:
                    description: >-
                      Transaction amount in the token's raw base units. Only
                      present for tokenized assets.
                    type: string
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
    ledger:
      title: LedgerEntry
      description: Ledger Entry
      type: object
      required:
        - refid
        - time
        - type
        - subtype
        - aclass
        - asset
        - amount
        - fee
        - balance
      properties:
        refid:
          description: >-
            Reference Id of the parent transaction (trade, deposit, withdrawal,
            etc.) that caused the ledger entry.
          type: string
        time:
          description: Unix timestamp of ledger
          type: number
        type:
          description: Type of ledger entry
          type: string
          enum:
            - none
            - trade
            - deposit
            - withdrawal
            - transfer
            - margin
            - adjustment
            - rollover
            - spend
            - receive
            - settled
            - credit
            - staking
            - reward
            - dividend
            - sale
            - conversion
            - nfttrade
            - nftcreatorfee
            - nftrebate
            - custodytransfer
        subtype:
          description: Additional info relating to the ledger entry type, where applicable
          type: string
        aclass:
          description: Asset class
          type: string
        asset:
          description: Asset
          type: string
        amount:
          description: Transaction amount
          type: string
        fee:
          description: Transaction fee
          type: string
        balance:
          description: Resulting balance
          type: string
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
