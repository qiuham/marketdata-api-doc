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
source_url: 'https://docs.kraken.com/api-reference/trading/amend-order'
updated_at: 2026-11-13
---

# Amend Order

> The amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one.

* The order identifiers assigned by Kraken and/or client will stay the same.
* Queue priority in the order book will be maintained where possible. 
* If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see [amend transaction guide](/docs/guides/spot-amends).

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/AmendOrder
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
  /private/AmendOrder:
    post:
      tags:
        - Trading
      summary: Amend Order
      description: >
        The amend request enables clients to modify the order parameters
        in-place without the need to cancel the existing order and create a new
        one.


        * The order identifiers assigned by Kraken and/or client will stay the
        same.

        * Queue priority in the order book will be maintained where possible. 

        * If an amend request will reduce the order quantity below the existing
        filled quantity, the remaining quantity will be cancelled.


        For more detail, see [amend transaction
        guide](/docs/guides/spot-amends).


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders` or `Orders and trades - Cancel & close orders`
      operationId: amendOrder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/amend'
      responses:
        '200':
          description: >
            A successful amend request will return the unique Kraken amend
            identifier.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/amend-2'
components:
  schemas:
    amend:
      title: Amend Order Request Body
      required:
        - nonce
      type: object
      properties:
        txid:
          description: >-
            The Kraken identifier for the order to be amended. Either `txid` or
            `cl_ord_id` is required.
          type: string
        cl_ord_id:
          description: >-
            The client identifier for the order to be amended. Either `txid` or
            `cl_ord_id` is required.
          type: string
        order_qty:
          description: The new order quantity in terms of the base asset.
          type: string
        display_qty:
          description: >-
            For `iceberg` orders only, it defines the new quantity to show in
            the book while the rest of order quantity remains hidden. Minimum
            value is 1 / 15 of remaining order quantity.
          type: string
        limit_price:
          description: >
            The new limit price restriction on the order (for order types that
            support limit price only).


            The relative pricing can be set by using the `+`, `-` prefixes
            and/or `%` suffix. 

            * &bull; `+` adds the amount from the reference price, i.e. market
            rises 50 USD `"+50"`.

            * &bull; `-` subtracts the amount from the reference price, i.e.
            market drops 100 USD `"-100"`.
          type: string
        trigger_price:
          description: >
            The new trigger price to activate the order (for triggered order
            types only). 


            The relative pricing can be set by using the `+`, `-` prefixes
            and/or `%` suffix. 

            * &bull; `+` adds the amount from the reference price, i.e. market
            rises 50 USD `"+50"`.

            * &bull; `-` subtracts the amount from the reference price, i.e.
            market drops 100 USD `"-100"`.
          type: string
        pair:
          description: >-
            The `pair` is required on amends for non-crypto pairs, i.e. provide
            the pair symbol for xStocks.
          type: string
        post_only:
          description: >
            An optional flag for `limit_price` amends. If `true`, the limit
            price change will be rejected if the order cannot be posted
            passively in the book.
          type: boolean
          default: false
        deadline:
          type: string
          description: >-
            RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the
            matching engine should reject the new order request, in presence of
            latency or order queueing. min now() + 2 seconds, max now() + 60
            seconds.
        nonce:
          $ref: '#/components/schemas/nonce'
      example:
        nonce: 1695828490
        cl_ord_id: 6d1b345e-2821-40e2-ad83-4ecb18a06876
        order_qty: '1.25'
    amend-2:
      type: object
      properties:
        result:
          title: OrderAmended
          type: object
          properties:
            amend_id:
              description: >
                The unique Kraken identifier generated for this amend
                transaction.
              type: string
        error:
          type: array
          items:
            $ref: '#/components/schemas/error'
      example:
        error: []
        result:
          amend_id: TEZA4R-DSDGT-IJBOJK
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
