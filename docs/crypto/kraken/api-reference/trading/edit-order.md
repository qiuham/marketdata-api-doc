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
source_url: 'https://docs.kraken.com/api-reference/trading/edit-order'
updated_at: 2026-11-13
---

# Edit Order

> Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be 
created with the adjusted parameters a new `txid` will be returned in the response.

**Note:** The new [AmendOrder](/exchange/guides/general/amends) endpoint resolves the caveats listed below and has additional performance gains.

Caveats for `EditOrder`:
* Triggered stop loss or take profit orders are not supported.
* Orders with conditional close terms attached are not supported.
* Orders where the executed volume is greater than the newly supplied volume will be rejected.
* `cl_ord_id` is not supported.
* Existing executions are associated with the original order and not copied to the amended order.
* Queue position will not be maintained.

**API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and trades - Cancel & close orders`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/EditOrder
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
  /private/EditOrder:
    post:
      tags:
        - Trading
      summary: Edit Order
      description: >
        Sends a request to edit the order parameters of a live order. When an
        order has been successfully modified, the original order will be
        cancelled and a new order will be 

        created with the adjusted parameters a new `txid` will be returned in
        the response.


        **Note:** The new [AmendOrder](/exchange/guides/general/amends) endpoint
        resolves the caveats listed below and has additional performance gains.


        Caveats for `EditOrder`:

        * Triggered stop loss or take profit orders are not supported.

        * Orders with conditional close terms attached are not supported.

        * Orders where the executed volume is greater than the newly supplied
        volume will be rejected.

        * `cl_ord_id` is not supported.

        * Existing executions are associated with the original order and not
        copied to the amended order.

        * Queue position will not be maintained.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders` and `Orders and trades - Cancel & close orders`
      operationId: editOrder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/edit'
      responses:
        '200':
          description: Order edited.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/edit-2'
              examples:
                Limit with conditional stop-loss:
                  value:
                    error: []
                    result:
                      status: ok
                      txid: OFVXHJ-KPQ3B-VS7ELA
                      originaltxid: OHYO67-6LP66-HMQ437
                      volume: '0.00030000'
                      price: '19500.0'
                      price2: '32500.0'
                      orders_cancelled: 1
                      descr:
                        order: buy 0.00030000 XXBTZGBP @ limit 19500.0
components:
  schemas:
    edit:
      title: Edit Standard Order Request Body
      required:
        - nonce
        - pair
        - txid
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        userref:
          description: >
            User reference id


            `userref` is an optional user-specified integer id associated with
            edit request. 
             >  Note: userref from parent order will not be retained on the new order after edit.
          type: integer
          format: int32
        txid:
          description: >-
            Original Order ID or User Reference Id (userref) which is
            user-specified integer id used with the original order. If userref
            is not unique and was used with multiple order, edit request is
            denied with an error.
          oneOf:
            - type: string
              title: string
            - type: integer
              title: integer
        volume:
          description: |
            Order quantity in terms of the base asset.
          type: string
        displayvol:
          description: >
            For `iceberg` orders only, it defines the quantity to show in the
            book while the rest of order quantity remains hidden. Minimum value
            is 1 / 15 of `volume`.
          type: string
        pair:
          description: Asset pair `id` or `altname`
          type: string
        asset_class:
          description: >-
            This parameter is required on requests for non-crypto pairs, i.e.
            use `tokenized_asset` for xStocks.
          type: string
          enum:
            - tokenized_asset
        price:
          description: >
            Price:

            * Limit price for `limit` and `iceberg` orders

            * Trigger price for `stop-loss`, `stop-loss-limit`, `take-profit`,
            `take-profit-limit`, `trailing-stop` and `trailing-stop-limit`
            orders


            Notes:

            * Relative Prices: Either `price` or `price2` can be preceded by
            `+`, `-`, or `#` to specify the order price as an offset relative to
            the last traded price. `+` adds the amount to, and `-` subtracts the
            amount from the last traded price. `#` will either add or subtract
            the amount to the last traded price, depending on the direction and
            order type used. Prices can also be suffixed with a `%` to signify
            the relative amount as a percentage, rather than an absolute price
            difference.

            * Trailing Stops: Must use a relative price for this field, namely
            the `+` prefix, from which the direction will be automatic based on
            if the original order is a buy or sell (no need to use `-` or `#`).
            The `%` suffix also works for these order types to use a relative
            percentage price.
          type: string
        price2:
          description: >
            Secondary Price:

            * Limit price for `stop-loss-limit`, `take-profit-limit` and
            `trailing-stop-limit` orders

            Note:

            * Trailing Stops: Must use a relative price for this field, namely
            one of the `+` or `-` prefixes. This will provide the offset from
            the trigger price to the limit price, i.e. +0 would set the limit
            price equal to the trigger price. The `%` suffix also works for this
            field to use a relative percentage limit price.
          type: string
        oflags:
          description: >
            Comma delimited list of order flags. Only these flags can be
            changed: - post post-only order (available when ordertype = limit).
            All the flags from the parent order are retained except post-only.
            post-only needs to be explicitly mentioned on edit request.
        deadline:
          type: string
          description: >
            RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the
            matching engine should reject the new order request, in presence of
            latency or order queueing. min now() + 2 seconds, max now() + 60
            seconds.  
        cancel_response:
          description: >
            Used to interpret if client wants to receive pending replace, before
            the order is completely replaced
          type: boolean
        validate:
          type: boolean
          description: Validate inputs only. Do not submit order.
          default: false
      example:
        nonce: 1695828490
        pair: XBTUSD
        txid: OHYO67-6LP66-HMQ437
        volume: '1.25'
        price: '27500'
        price2: '26500'
    edit-2:
      type: object
      properties:
        result:
          title: OrderEdited
          type: object
          properties:
            descr:
              description: Order description info
              type: object
              properties:
                order:
                  description: Order description
                  type: string
            txid:
              description: |
                New Transaction ID
                <br><sup><sub>(if order was added successfully)</sup></sub>
              type: string
            newuserref:
              description: |
                Original userref if passed with the request
              type: string
            olduserref:
              description: |
                Original userref if passed with the request
              type: string
            orders_cancelled:
              description: |
                Number of orders cancelled (either 0 or 1)
              type: integer
            originaltxid:
              description: |
                Original transaction ID
              type: string
            status:
              description: |
                Status of the order: Ok or Err
              type: string
            volume:
              description: |
                Updated volume
              type: string
            price:
              description: |
                Updated price
              type: string
            price2:
              description: |
                Updated price2
              type: string
            error_message:
              description: |
                Error message if unsuccessful
              type: string
        error:
          type: array
          items:
            $ref: '#/components/schemas/error'
      example:
        error: []
        result:
          descr:
            order: buy 1.25000000 XBTUSD @ limit 27500.0
          txid: OU22CG-KLAF2-FWUDD7
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
