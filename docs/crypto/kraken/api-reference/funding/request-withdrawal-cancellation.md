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
source_url: 'https://docs.kraken.com/api-reference/funding/request-withdrawal-cancellation'
updated_at: 2026-11-13
---

# Request Withdrawal Cancellation

> This endpoint will remain active but will no longer receive updates. It's highly recommended to migrate to the Funding (Beta) API — see the [Funding guide](/exchange/guides/rest/funding) and [API reference](/api-reference/funding-beta/list-funding-methods).

Cancel a recently requested withdrawal, if it has not already been successfully processed.

**API Key Permissions Required:** `Funds permissions - Withdraw`, unless withdrawal is a `WalletTransfer`, then no permissions are required.


> [!WARNING]
>
> This endpoint will remain active but will no longer receive updates. It's highly recommended to migrate to the Funding (Beta) API — see the [Funding guide](https://docs.kraken.com/exchange/guides/rest/funding.md) and [API reference](https://docs.kraken.com/api-reference/funding-beta/list-funding-methods.md).


## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/WithdrawCancel
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
  /private/WithdrawCancel:
    post:
      tags:
        - Funding
      summary: Request Withdrawal Cancellation
      description: >
        This endpoint will remain active but will no longer receive updates.
        It's highly recommended to migrate to the Funding (Beta) API — see the
        [Funding guide](/exchange/guides/rest/funding) and [API
        reference](/api-reference/funding-beta/list-funding-methods).


        Cancel a recently requested withdrawal, if it has not already been
        successfully processed.


        **API Key Permissions Required:** `Funds permissions - Withdraw`, unless
        withdrawal is a `WalletTransfer`, then no permissions are required.
      operationId: cancelWithdrawal
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/cancel-3'
      responses:
        '200':
          description: Withdrawal cancellation requested.
          content:
            application/json:
              schema:
                properties:
                  result:
                    type: boolean
                    description: Whether cancellation was successful or not.
                  error:
                    $ref: '#/components/schemas/error'
                example:
                  error: []
                  result: true
      deprecated: true
components:
  schemas:
    cancel-3:
      title: Request Withdrawal Cancelation Request Body
      required:
        - nonce
        - asset
        - refid
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        asset:
          description: Asset being withdrawn
          type: string
        refid:
          description: Withdrawal reference ID
          type: string
      example:
        nonce: 1695828271
        asset: XBT
        refid: FTQcuak-V6Za8qrWnhzTx67yYHz8Tg
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
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
