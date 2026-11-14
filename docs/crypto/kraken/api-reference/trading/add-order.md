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
source_url: 'https://docs.kraken.com/api-reference/trading/add-order'
updated_at: 2026-11-13
---

# Add Order

> Place a new order.

**Note**: See the [AssetPairs](/docs/rest-api/get-tradable-asset-pairs) endpoint for details on the available trading pairs, their price and quantity precisions, order minimums, available leverage, etc.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/AddOrder
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
  /private/AddOrder:
    post:
      tags:
        - Trading
      summary: Add Order
      description: >
        Place a new order.


        **Note**: See the [AssetPairs](/docs/rest-api/get-tradable-asset-pairs)
        endpoint for details on the available trading pairs, their price and
        quantity precisions, order minimums, available leverage, etc.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`
      operationId: addOrder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/add'
      responses:
        '200':
          description: Order added.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/add-2'
              examples:
                Limit with conditional stop-loss:
                  value:
                    error: []
                    result:
                      descr:
                        order: >-
                          buy 2.12340000 XBTUSD @ limit 25000.1 with 2:1
                          leverage
                        close: close position @ stop loss 22000.0 -> limit 21000.0
                      txid:
                        - OUF4EM-FRGI2-MQMWZD
components:
  schemas:
    add:
      example:
        nonce: 163245617
        ordertype: limit
        type: buy
        volume: '1.25'
        pair: XBTUSD
        price: '27500'
        cl_ord_id: 6d1b345e-2821-40e2-ad83-4ecb18a06876
      title: Add Standard Order Request Body
      required:
        - nonce
        - pair
        - type
        - ordertype
        - volume
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/nonce'
        userref:
          description: >
            This is an optional non-unique, numeric identifier which can
            associated with a number of orders by the client. This field is
            mutually exclusive with <code>cl_ord_id</code> parameter.


            `userref` is an optional user-specified integer id that can be
            associated with any number of orders. Many clients choose a
            `userref` corresponding to a unique integer id generated by their
            systems (e.g. a timestamp). However, because we don't enforce
            uniqueness on our side, it can also be used to easily group orders
            by pair, side, strategy, etc. This allows clients to more readily
            cancel or query information about orders in a particular group, with
            fewer API calls by using `userref` instead of our `txid`, where
            supported.
          type: integer
          format: int32
        cl_ord_id:
          description: >
            Adds an alphanumeric client order identifier which uniquely
            identifies an open order for each client. This field is mutually
            exclusive with <code>userref</code> parameter.


            The <code>cl_ord_id</code> parameter can be one of the following
            formats:
              * &bull; Long UUID: <code>6d1b345e-2821-40e2-ad83-4ecb18a06876</code> 32 hex characters separated with 4 dashes.
              * &bull; Short UUID: <code>da8e4ad59b78481c93e589746b0cf91f</code> 32 hex characters with no dashes.
              * &bull; Free text: <code>arb-20240509-00010</code> Free format ascii text up to 18 characters.
          type: string
        ordertype:
          $ref: '#/components/schemas/ordertype'
        type:
          description: Order direction (buy/sell)
          type: string
          enum:
            - buy
            - sell
        volume:
          description: >
            Order quantity in terms of the base asset

            > Note: Volume can be specified as `0` for closing margin orders to
            automatically fill the requisite quantity.
          type: string
          example: '1.25'
        displayvol:
          description: >
            For `iceberg` orders only, it defines the quantity to show in the
            book while the rest of order quantity remains hidden. Minimum value
            is 1 / 15 of `volume`.
          type: string
        pair:
          description: Asset pair `id` or `altname`
          type: string
          example: XBTUSD
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

            * &bull; Limit price for `limit` and `iceberg` orders

            * &bull; Trigger price for `stop-loss`, `stop-loss-limit`,
            `take-profit`, `take-profit-limit`, `trailing-stop` and
            `trailing-stop-limit` orders


            Notes:

            * &bull; Relative Prices: Either `price` or `price2` can be preceded
            by `+`, `-`, or `#` to specify the order price as an offset relative
            to the last traded price. `+` adds the amount to, and `-` subtracts
            the amount from the last traded price. `#` will either add or
            subtract the amount to the last traded price, depending on the
            direction and order type used. Prices can also be suffixed with a
            `%` to signify the relative amount as a percentage, rather than an
            absolute price difference.

            * &bull; Trailing Stops: Must use a relative price for this field,
            namely the `+` prefix, from which the direction will be automatic
            based on if the original order is a buy or sell (no need to use `-`
            or `#`). The `%` suffix also works for these order types to use a
            relative percentage price.
          type: string
          example: '40000.0'
        price2:
          description: >
            Secondary Price:

            * &bull; Limit price for `stop-loss-limit`, `take-profit-limit` and
            `trailing-stop-limit` orders


            Note:

            * &bull; Trailing Stops: Must use a relative price for this field,
            namely one of the `+` or `-` prefixes. This will provide the offset
            from the trigger price to the limit price, i.e. +0 would set the
            limit price equal to the trigger price. The `%` suffix also works
            for this field to use a relative percentage limit price.
          type: string
        trigger:
          description: >
            Price signal used to trigger `stop-loss`, `stop-loss-limit`,
            `take-profit`, `take-profit-limit`, `trailing-stop` and
            `trailing-stop-limit` orders


            Notes:

            * &bull; This `trigger` type will also be used for any associated
            conditional close orders.

            * &bull; To keep triggers serviceable, the last price will be used
            as fallback reference price during connectivity issues with external
            index feeds.
          type: string
          enum:
            - index
            - last
          default: last
        leverage:
          description: 'Amount of leverage desired (default: none)'
          type: string
          example: 5
        reduce_only:
          description: >-
            If `true`, order will only reduce a currently open position, not
            increase it or open a new position.
          type: boolean
          default: false
          example: true
        stptype:
          description: >
            Self Trade Prevention (STP) is a protection feature to prevent users
            from inadvertently or deliberately trading against themselves. To
            prevent a self-match, one of the following STP modes can be used to
            define which order(s) will be expired:

            * &bull; `cancel-newest`: arriving order will be canceled

            * &bull; `cancel-oldest`: resting order will be canceled

            * &bull; `cancel-both`: both arriving and resting orders will be
            canceled
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
            Time-in-force of the order to specify how long it should remain in
            the order book before being cancelled. GTC (Good-'til-cancelled) is
            default if the parameter is omitted. IOC (immediate-or-cancel) will
            immediately execute the amount possible and cancel any remaining
            balance rather than resting in the book. GTD (good-'til-date), if
            specified, must coincide with a desired `expiretm`. FOK
            (fill-or-kill) will execute the full order immediately or cancel it
            entirely.
          type: string
          enum:
            - GTC
            - IOC
            - GTD
            - FOK
          default: GTC
        starttm:
          description: >
            Scheduled start time, can be specified as an absolute timestamp or
            as a number of seconds in the future:
              * &bull; `0` now (default)
              * &bull; `<n>` = unix timestamp of start time
              * &bull; `+<n>` = schedule start time `<n>` seconds from now
                * Note that URL encoding of the `+` character changes it to a space, so please use `%2b` followed by the number of seconds instead of `+`
          type: string
        expiretm:
          description: >
            Expiry time on GTD orders can be set up to one month in future, it
            is specified as an absolute timestamp or as a number of seconds from
            now:
              * &bull; `0` no expiration (default)
              * &bull; `<n>` = unix timestamp of expiration time
              * &bull; `+<n>` = expire `<n>` seconds from now, minimum 5 seconds
                * Note that URL encoding of the `+` character changes it to a space, so please use `%2b` followed by the number of seconds instead of `+`
          type: string
        close[ordertype]:
          description: >
            Conditional close order type 

            > Note: [Conditional close
            orders](https://support.kraken.com/hc/en-us/articles/360038640052-Conditional-Close)
            are triggered by execution of the primary order in the same quantity
            and opposite direction, but once triggered are __independent
            orders__ that may reduce or increase net position
          type: string
          enum:
            - limit
            - iceberg
            - stop-loss
            - take-profit
            - stop-loss-limit
            - take-profit-limit
            - trailing-stop
            - trailing-stop-limit
        close[price]:
          description: |
            Conditional close order `price`
          type: string
          example: '50000.0'
        close[price2]:
          description: |
            Conditional close order `price2`
          type: string
        deadline:
          type: string
          description: >
            RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the
            matching engine should reject the new order request, in presence of
            latency or order queueing: min now() + 2 seconds, max now() + 60
            seconds.
        validate:
          type: boolean
          description: >-
            If set to `true` the order will be validated only, it will not trade
            in the matching engine.
          default: false
        broker:
          description: Broker IIBAN (Partner's Kraken IIBAN)
          type: string
          nullable: true
    add-2:
      type: object
      properties:
        result:
          title: OrderAdded
          type: object
          properties:
            descr:
              description: Order description info
              type: object
              properties:
                order:
                  description: Order description
                  type: string
                close:
                  description: Conditional close order description, if applicable
                  type: string
            txid:
              description: |
                Transaction IDs for order
                <br><sup><sub>(if order was added successfully)</sup></sub>
              type: array
              items:
                type: string
        error:
          type: array
          items:
            $ref: '#/components/schemas/error'
      example:
        error: []
        result:
          descr:
            order: buy 1.45 XBTUSD @ limit 27500.0
          txid:
            - OU22CG-KLAF2-FWUDD7
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    ordertype:
      description: |
        The execution model of the order.
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
      example: limit
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
