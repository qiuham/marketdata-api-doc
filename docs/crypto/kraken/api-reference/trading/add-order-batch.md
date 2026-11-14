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
source_url: 'https://docs.kraken.com/api-reference/trading/add-order-batch'
updated_at: 2026-11-13
---

# Add Order Batch

> Sends a collection of orders (minimum of 2 and maximum 15): 
* Validation is performed on the whole batch prior to submission to the engine. If an order fails validation, the whole batch will be rejected.
* On submission to the engine, if an order fails pre-match checks (i.e. funding), then the individual order will be rejected and remainder of the batch will be processed. 
* All orders in batch are limited to a single pair.

**Note**: See the [AssetPairs](/docs/rest-api/get-tradable-asset-pairs) endpoint for details on the available trading pairs, their price and quantity precisions, order minimums, available leverage, etc.

**API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and trades - Cancel & close orders`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/AddOrderBatch
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
  /private/AddOrderBatch:
    post:
      tags:
        - Trading
      summary: Add Order Batch
      description: >
        Sends a collection of orders (minimum of 2 and maximum 15): 

        * Validation is performed on the whole batch prior to submission to the
        engine. If an order fails validation, the whole batch will be rejected.

        * On submission to the engine, if an order fails pre-match checks (i.e.
        funding), then the individual order will be rejected and remainder of
        the batch will be processed. 

        * All orders in batch are limited to a single pair.


        **Note**: See the [AssetPairs](/docs/rest-api/get-tradable-asset-pairs)
        endpoint for details on the available trading pairs, their price and
        quantity precisions, order minimums, available leverage, etc.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders` and `Orders and trades - Cancel & close orders`
      operationId: addOrderBatch
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/batchadd'
      responses:
        '200':
          description: >-
            The order of returned `orders` in the response array is the same as
            the order of the order list sent in request.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/batchadd-2'
              examples:
                Limits, one with conditional stop-loss:
                  value:
                    error: []
                    result:
                      orders:
                        - txid: O5OR23-ADFAD-Y2G61C
                          descr:
                            order: buy 0.80300000 XBTUSD @ limit 28300.0
                            close: >-
                              close position @ stop loss 27000.0 -> limit
                              26000.0
                        - txid: 9K6KFS-5H3PL-XBRC7A
                          descr:
                            order: sell 0.10500000 XBTUSD @ limit 36000.0
components:
  schemas:
    batchadd:
      title: Add Standard Order Request Body
      required:
        - nonce
        - orders
        - pair
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        orders:
          type: array
          items:
            required:
              - ordertype
              - type
              - volume
            type: object
            properties:
              userref:
                description: >
                  User reference id

                  `userref` is an optional user-specified integer id that can be
                  associated with any number of orders. Many clients choose a
                  `userref` corresponding to a unique integer id generated by
                  their systems (e.g. a timestamp). However, because we don't
                  enforce uniqueness on our side, it can also be used to easily
                  group orders by pair, side, strategy, etc. This allows clients
                  to more readily cancel or query information about orders in a
                  particular group, with fewer API calls by using `userref`
                  instead of our `txid`, where supported.
                type: integer
                format: int32
              cl_ord_id:
                description: >
                  Adds an alphanumeric client order identifier which uniquely
                  identifies an open order for each client. This field is
                  mutually exclusive with <code>userref</code> parameter.


                  The <code>cl_ord_id</code> parameter can be one of the
                  following formats:
                    * Long UUID: <code>6d1b345e-2821-40e2-ad83-4ecb18a06876</code> 32 hex characters separated with 4 dashes.
                    * Short UUID: <code>da8e4ad59b78481c93e589746b0cf91f</code> 32 hex characters with no dashes.
                    * Free text: <code>arb-20240509-00010</code> Free format ascii text up to 18 characters.
                type: string
              ordertype:
                description: |
                  Order type
                type: string
                enum:
                  - market
                  - limit
                  - iceberg
                  - stop-loss
                  - take-profit
                  - stop-loss-limit
                  - take-profit-limit
                  - trailing-stop
                  - trailing-stop-limit
                  - settle-position
              type:
                description: Order direction (buy/sell)
                type: string
                enum:
                  - buy
                  - sell
              volume:
                description: >
                  Order quantity in terms of the base asset

                  > Note: Volume can be specified as `0` for closing margin
                  orders to automatically fill the requisite quantity.
                type: string
              displayvol:
                description: >
                  For `iceberg` orders only, it defines the quantity to show in
                  the book while the rest of order quantity remains hidden.
                  Minimum value is 1 / 15 of `volume`.
                type: string
              price:
                description: >
                  Price:

                  * Limit price for `limit` and `iceberg` orders

                  * Trigger price for `stop-loss`, `stop-loss-limit`,
                  `take-profit`, and `take-profit-limit` orders


                  Notes:

                  * Relative Prices: Either `price` or `price2` can be preceded
                  by `+`, `-`, or `#` to specify the order price as an offset
                  relative to the last traded price. `+` adds the amount to, and
                  `-` subtracts the amount from the last traded price. `#` will
                  either add or subtract the amount to the last traded price,
                  depending on the direction and order type used. Prices can
                  also be suffixed with a `%` to signify the relative amount as
                  a percentage, rather than an absolute price difference.
                type: string
              price2:
                description: |
                  Secondary Price:
                  * Limit price for `stop-loss-limit` and `take-profit-limit`
                type: string
              trigger:
                description: >
                  Price signal used to trigger `stop-loss`, `stop-loss-limit`,
                  `take-profit`, and `take-profit-limit` orders

                  Notes:

                  * To keep triggers serviceable, the last price will be used as
                  fallback reference price during connectivity issues with
                  external index feeds.
                type: string
                enum:
                  - index
                  - last
                default: last
              leverage:
                description: |
                  Amount of leverage desired (default: none)
                type: string
              reduce_only:
                description: >-
                  If `true`, order will only reduce a currently open position,
                  not increase it or open a new position.
                type: boolean
                default: false
              stptype:
                description: >
                  Self trade prevention behaviour definition:

                  * `cancel-newest` - if self trade is triggered, arriving order
                  will be canceled

                  * `cancel-oldest` - if self trade is triggered, resting order
                  will be canceled

                  * `cancel-both` - if self trade is triggered, both arriving
                  and resting orders will be canceled
                type: string
                enum:
                  - cancel-newest
                  - cancel-oldest
                  - cancel-both
                default: cancel-newest
              oflags:
                $ref: '#/components/schemas/oflags'
              timeinforce:
                description: >
                  Time-in-force of the order to specify how long it should
                  remain in the order book before being cancelled. GTC
                  (Good-'til-cancelled) is default if the parameter is omitted.
                  IOC (immediate-or-cancel) will immediately execute the amount
                  possible and cancel any remaining balance rather than resting
                  in the book. GTD (good-'til-date), if specified, must coincide
                  with a desired `expiretm`.
                type: string
                enum:
                  - GTC
                  - IOC
                  - GTD
                default: GTC
              starttm:
                description: >
                  Scheduled start time, can be specified as an absolute
                  timestamp or as a number of seconds in the future:
                   * `0` now (default)
                   * `+<n>` schedule start time <n> seconds from now
                   * `<n>` = unix timestamp of start time
                type: string
              expiretm:
                description: >
                  Expiry time on GTD orders can be set up to one month in
                  future, it is specified as an absolute timestamp or as a
                  number of seconds from now:
                   * `0` no expiration (default)
                   * `+<n>` = expire <n> seconds from now, minimum 5 seconds
                   * `<n>` = unix timestamp of expiration time
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
        deadline:
          type: string
          description: >
            RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the
            matching engine should reject the new order request, in presence of
            latency or order queueing. min now() + 2 seconds, max now() + 60
            seconds. 
        validate:
          type: boolean
          description: Validate inputs only. Do not submit order.
          default: false
        broker:
          description: Broker IIBAN (Partner's Kraken IIBAN)
          type: string
          nullable: true
      example:
        nonce: 1695828490
        orders:
          - close:
              ordertype: stop-loss-limit
              price: '37000'
              price2: '36000'
            ordertype: limit
            price: '40000'
            price2: string
            timeinforce: GTC
            type: buy
            cl_ord_id: 6d1b345e-2821-40e2-ad83-4ecb18a06876
            volume: '1.2'
          - ordertype: limit
            price: '42000'
            starttm: string
            timeinforce: GTC
            type: sell
            cl_ord_id: da8e4ad59b78481c93e589746b0cf91
            volume: '1.2'
        pair: BTC/USD
        validate: false
        deadline: '2023-09-24T14:15:22Z'
    batchadd-2:
      type: object
      properties:
        result:
          title: Result
          type: object
          properties:
            orders:
              title: Orders
              type: array
              items:
                type: object
                properties:
                  descr:
                    description: Order description info
                    type: object
                    properties:
                      order:
                        type: string
                  error:
                    description: Error description from individual order processing
                    type: string
                  txid:
                    description: >
                      Transaction ID for order

                      <br><sup><sub>(if order was added
                      successfully)</sup></sub>
                    type: string
        error:
          type: array
          items:
            $ref: '#/components/schemas/error'
      example:
        error: []
        result:
          orders:
            - txid: 65LRD3-AHGRA-YAH8E5
              descr:
                order: buy 1.02010000 XBTUSD @ limit 29000.0
            - txid: OK8HFF-5J2PL-XLR17S
              descr:
                order: sell 0.14000000 XBTUSD @ limit 40000.0
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    oflags:
      description: |
        Comma delimited list of order flags

          * &bull; `post` post-only order (available when ordertype = limit)
          * &bull; `fcib` prefer fee in base currency (default if selling)
          * &bull; `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
          * &bull; `nompp` (DEPRECATED) — disabling Market Price Protection for market orders is no longer supported. If supplied, the flag is accepted but ignored.
          * &bull; `viqc`  order volume expressed in quote currency. This option is supported only for buy market orders. Also not available on margin orders.
      type: string
      example: post
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
