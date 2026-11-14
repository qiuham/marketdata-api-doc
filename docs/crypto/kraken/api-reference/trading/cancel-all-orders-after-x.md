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
source_url: 'https://docs.kraken.com/api-reference/trading/cancel-all-orders-after-x'
updated_at: 2026-11-13
---

# Cancel All Orders After X

> CancelAllOrdersAfter provides a "Dead Man's Switch" mechanism to protect the client from network malfunction, extreme latency or unexpected matching engine downtime. The client can send a request with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders when the timer expires. The client has to keep sending new requests to push back the trigger time, or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds. This allows the client to keep the orders in place in case of a brief disconnection or transient delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders will be cancelled when the trading engine comes back from downtime - planned or otherwise).

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/CancelAllOrdersAfter
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
  /private/CancelAllOrdersAfter:
    post:
      tags:
        - Trading
      summary: Cancel All Orders After X
      description: >
        CancelAllOrdersAfter provides a "Dead Man's Switch" mechanism to protect
        the client from network malfunction, extreme latency or unexpected
        matching engine downtime. The client can send a request with a timeout
        (in seconds), that will start a countdown timer which will cancel *all*
        client orders when the timer expires. The client has to keep sending new
        requests to push back the trigger time, or deactivate the mechanism by
        specifying a timeout of 0. If the timer expires, all orders are
        cancelled and then the timer remains disabled until the client provides
        a new (non-zero) timeout.


        The recommended use is to make a call every 15 to 30 seconds, providing
        a timeout of 60 seconds. This allows the client to keep the orders in
        place in case of a brief disconnection or transient delay, while keeping
        them safe in case of a network breakdown. It is also recommended to
        disable the timer ahead of regularly scheduled trading engine
        maintenance (if the timer is enabled, all orders will be cancelled when
        the trading engine comes back from downtime - planned or otherwise).


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders` or `Orders and trades - Cancel & close orders`
      operationId: cancelAllOrdersAfter
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - nonce
                - timeout
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                timeout:
                  type: integer
                  description: >-
                    Duration (in seconds) to set/extend the timer, it should be
                    less than 86400 seconds.
              example:
                nonce: 1695828490
                timeout: 120
      responses:
        '200':
          description: Dead man's switch timer reset or disabled.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: object
                    properties:
                      currentTime:
                        description: >-
                          Timestamp (RFC3339 format) at which the request was
                          received
                        type: string
                      triggerTime:
                        description: >-
                          Timestamp (RFC3339 format) after which all orders will
                          be cancelled, unless the timer is extended or disabled
                        type: string
                  error:
                    $ref: '#/components/schemas/error'
                example:
                  error: []
                  result:
                    currentTime: '2023-03-24T17:41:56Z'
                    triggerTime: '2023-03-24T17:42:56Z'
components:
  schemas:
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
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
