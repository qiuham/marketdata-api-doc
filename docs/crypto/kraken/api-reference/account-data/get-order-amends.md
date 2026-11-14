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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-order-amends'
updated_at: 2026-11-13
---

# Get Order Amends

> Retrieves an audit trail of amend transactions on the specified order. The list is ordered by ascending amend timestamp.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and trades - Query closed orders & trades`, depending on status of order.




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/OrderAmends
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
  /private/OrderAmends:
    post:
      tags:
        - Account Data
      summary: Get Order Amends
      description: >
        Retrieves an audit trail of amend transactions on the specified order.
        The list is ordered by ascending amend timestamp.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades` or `Orders and trades - Query closed orders & trades`,
        depending on status of order.
      operationId: getOrderAmends
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/amends'
      responses:
        '200':
          description: >-
            The first entry contains the original order parameters and has
            amend_type of `original`.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/amends-2'
                example:
                  response:
                    error: []
                    result:
                      amends:
                        - amend_id: TSUN4B-EX2XN-WQ6GKG
                          amend_type: original
                          order_qty: '0.01000000'
                          remaining_qty: '0.01000000'
                          limit_price: '61032.8'
                          timestamp: 1724158070287558000
                        - amend_id: TF6VAW-VUWMX-6SXTCH
                          amend_type: user
                          order_qty: '0.01000000'
                          remaining_qty: '0.01000000'
                          limit_price: '61032.7'
                          timestamp: 1724158076936755700
                        - amend_id: TUMY4K-E4MPE-CSL2N3
                          amend_type: user
                          order_qty: '0.01000000'
                          remaining_qty: '0.01000000'
                          limit_price: '61032.6'
                          timestamp: 1724158214879660000
                      count: 3
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
    amends:
      title: Get Order Amends Request Body
      required:
        - nonce
        - order_id
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        order_id:
          description: The Kraken order identifier for the amended order.
          type: string
        rebase_multiplier:
          $ref: '#/components/schemas/rebase_multiplier'
      example:
        nonce: 1695828490
        order_id: OVITN3-BFK3H-63K37C
    amends-2:
      type: object
      properties:
        result:
          type: object
          description: The amend transaction history.
          title: Amend transactions.
          properties:
            count:
              type: integer
              description: >-
                The total count of new and amend transactions (i.e. includes the
                original order).
            amends:
              type: array
              items:
                type: object
                properties:
                  amend_id:
                    description: Kraken amend identifier
                    type: string
                  amend_type:
                    description: |
                      The type of amend transaction:
                        * &bull; `original`: original order values on order entry.
                        * &bull; `user`: user requested amendment.
                        * &bull; `restated`: engine order maintenance amendment.
                    type: string
                    enum:
                      - original
                      - user
                      - restated
                  order_qty:
                    description: Order quantity in terms of the base asset.
                    type: string
                  display_qty:
                    description: The quantity show in the book for iceberg orders.
                    type: string
                  remaining_qty:
                    description: Remaining un-traded quantity on the order.
                    type: string
                  limit_price:
                    description: The limit price restriction on the order.
                    type: string
                  trigger_price:
                    description: The trigger price on trigger order types.
                    type: string
                  reason:
                    description: Description of the reason for this amend.
                    type: string
                  post_only:
                    description: >-
                      Indicates if the transaction was restricted from taking
                      liquidity.
                    type: boolean
                  timestamp:
                    description: The UNIX timestamp for the amend transaction.
                    type: integer
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
