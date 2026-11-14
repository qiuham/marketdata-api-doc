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
source_url: 'https://docs.kraken.com/api-reference/funding/get-status-of-recent-deposits'
updated_at: 2026-11-13
---

# Get Status of Recent Deposits

> This endpoint will remain active but will no longer receive updates. It's highly recommended to migrate to the Funding (Beta) API — see the [Funding guide](/exchange/guides/rest/funding) and [API reference](/api-reference/funding-beta/list-funding-methods).

Retrieve information about recent deposits. Results are sorted by recency, use the `cursor` parameter to iterate through list of deposits (page size equal to value of `limit`) from newest to oldest.
**API Key Permissions Required:** `Funds permissions - Query`


> [!WARNING]
>
> This endpoint will remain active but will no longer receive updates. It's highly recommended to migrate to the Funding (Beta) API — see the [Funding guide](https://docs.kraken.com/exchange/guides/rest/funding.md) and [API reference](https://docs.kraken.com/api-reference/funding-beta/list-funding-methods.md).


## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/DepositStatus
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
  /private/DepositStatus:
    post:
      tags:
        - Funding
      summary: Get Status of Recent Deposits
      description: >
        This endpoint will remain active but will no longer receive updates.
        It's highly recommended to migrate to the Funding (Beta) API — see the
        [Funding guide](/exchange/guides/rest/funding) and [API
        reference](/api-reference/funding-beta/list-funding-methods).


        Retrieve information about recent deposits. Results are sorted by
        recency, use the `cursor` parameter to iterate through list of deposits
        (page size equal to value of `limit`) from newest to oldest.

        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: getStatusRecentDeposits
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/recent'
      responses:
        '200':
          description: Recent deposits retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/recent-2'
      deprecated: true
components:
  schemas:
    recent:
      title: Get Status of Recent Deposits Request Body
      required:
        - nonce
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        asset:
          description: Filter for specific asset being deposited
          type: string
        aclass:
          description: Filter for specific asset class being deposited
          type: string
          enum:
            - currency
            - tokenized_asset
          default: currency
        method:
          description: Filter for specific name of deposit method
          type: string
        start:
          description: >-
            Start timestamp, deposits created strictly before will not be
            included in the response
          type: string
        end:
          description: >-
            End timestamp, deposits created strictly after will be not be
            included in the response
          type: string
        cursor:
          description: >-
            true/false to enable/disable paginated response (boolean) or cursor
            for next page of results (string)
          default: false
          anyOf:
            - type: boolean
              description: Enable/disable paginated response
            - type: string
              description: Cursor for next page of results
        limit:
          description: Number of results to include per page
          type: integer
          default: 25
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
      example:
        nonce: 1695828271
        asset: XBT
        method: Bitcoin
    recent-2:
      type: object
      properties:
        result:
          anyOf:
            - $ref: '#/components/schemas/deposit'
            - properties:
                deposit:
                  $ref: '#/components/schemas/deposit'
                next_cursor:
                  description: >-
                    If pagination is set via `cursor` parameter, provides next
                    input to use for `cursor` in pagination
                  type: string
        error:
          $ref: '#/components/schemas/error'
      example:
        error: []
        result:
          - method: Bitcoin
            aclass: currency
            asset: XXBT
            refid: FTQcuak-V6Za8qrWnhzTx67yYHz8Tg
            txid: 6544b41b607d8b2512baf801755a3a87b6890eacdb451be8a94059fb11f0a8d9
            info: 2Myd4eaAW96ojk38A2uDK4FbioCayvkEgVq
            amount: '0.78125000'
            fee: '0.0000000000'
            time: 1688992722
            status: Success
            status-prop: return
          - method: Ether (Hex)
            aclass: currency
            asset: XETH
            refid: FTQcuak-V6Za8qrPnhsTx47yYLz8Tg
            txid: '0x339c505eba389bf2c6bebb982cc30c6d82d0bd6a37521fa292890b6b180affc0'
            info: '0xca210f4121dc891c9154026c3ae3d1832a005048'
            amount: '0.1383862742'
            time: 1688992722
            status: Settled
            status-prop: onhold
            originators:
              - >-
                0x70b6343b104785574db2c1474b3acb3937ab5de7346a5b857a78ee26954e0e2d
              - >-
                0x5b32f6f792904a446226b17f607850d0f2f7533cdc35845bfe432b5b99f55b66
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    deposit:
      title: deposit
      description: deposit
      type: object
      properties:
        method:
          description: Name of deposit method
          type: string
        aclass:
          description: Asset class
          type: string
        asset:
          description: Asset
          type: string
        refid:
          description: Reference ID
          type: string
        txid:
          description: Method transaction ID
          type: string
        info:
          description: Method transaction information
          type: string
        amount:
          description: Amount deposited
          type: string
        fee:
          description: Fees paid
        time:
          description: Unix timestamp when request was made
          type: integer
          format: int32
        status:
          description: >
            Status of deposit<br>

            <sup><sub>For additional information about the status, please refer
            to the [IFEX financial transaction
            states](https://github.com/globalcitizen/ifex-protocol/blob/master/draft-ifex-00.txt#L837).</sup></sub>
          type: string
          enum:
            - Initial
            - Pending
            - EarlyConfirmed
            - Settled
            - Success
            - Failure
        status-prop:
          description: |
            Addition status properties <sup><sub>(if available)</sup></sub><br>
              * `return` A return transaction initiated by Kraken
              * `onhold` Deposit is on hold pending review
          type: string
          enum:
            - return
            - onhold
        originators:
          description: >
            Client sending transaction id(s) for deposits that credit with a
            sweeping transaction
          type: array
          items:
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
