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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-open-orders'
updated_at: 2026-11-13
---

# Get Open Orders

> Retrieve information about currently open orders.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/OpenOrders
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
  /private/OpenOrders:
    post:
      tags:
        - Account Data
      summary: Get Open Orders
      description: >
        Retrieve information about currently open orders.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOpenOrders
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        $ref: '#/components/requestBodies/openOrders'
      responses:
        '200':
          description: Open orders info retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/open-2'
                example:
                  error: []
                  result:
                    open:
                      OQCLML-BW3P3-BUCMWZ:
                        refid: None
                        userref: 0
                        status: open
                        opentm: 1688666559.8974
                        starttm: 0
                        expiretm: 0
                        descr:
                          pair: XBTUSD
                          type: buy
                          ordertype: limit
                          price: '30010.0'
                          price2: '0'
                          leverage: none
                          order: buy 1.25000000 XBTUSD @ limit 30010.0
                          close: ''
                        vol: '1.25000000'
                        vol_exec: '0.37500000'
                        cost: '11253.7'
                        fee: '0.00000'
                        price: '30010.0'
                        stopprice: '0.00000'
                        limitprice: '0.00000'
                        misc: ''
                        oflags: fciq
                        trades:
                          - TCCCTY-WE2O6-P3NB37
                      OB5VMB-B4U2U-DK2WRW:
                        refid: None
                        userref: 45326
                        status: open
                        opentm: 1688665899.5699
                        starttm: 0
                        expiretm: 0
                        descr:
                          pair: XBTUSD
                          type: buy
                          ordertype: limit
                          price: '14500.0'
                          price2: '0'
                          leverage: '5:1'
                          order: >-
                            buy 0.27500000 XBTUSD @ limit 14500.0 with 5:1
                            leverage
                          close: ''
                        vol: '0.27500000'
                        vol_exec: '0.00000000'
                        cost: '0.00000'
                        fee: '0.00000'
                        price: '0.00000'
                        stopprice: '0.00000'
                        limitprice: '0.00000'
                        misc: ''
                        oflags: fciq
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
    openOrders:
      required: true
      content:
        application/json:
          schema:
            title: Get Open Orders Request Body
            required:
              - nonce
            type: object
            properties:
              nonce:
                $ref: '#/components/schemas/nonce'
              trades:
                description: Whether or not to include trades related to position in output
                type: boolean
                default: false
              userref:
                description: Restrict results to given user reference
                type: integer
                format: int32
              cl_ord_id:
                description: Restrict results to given client order id
                type: string
              consolidate_taker:
                description: >-
                  Whether or not to consolidate trades by individual taker
                  trades
                type: boolean
                default: true
              with_cursor:
                description: >-
                  Use cursor-based pagination. Each page then holds at most
                  `limit` orders, and the response includes `cursor.next` when
                  more orders are available.
                type: boolean
                default: false
              limit:
                description: >-
                  Maximum number of orders to return. When `with_cursor` is
                  `true`, defaults to `50` and values above `100` are rejected.
                  Otherwise all open orders are returned unless `limit` is set
                  (capped at `1000`).
                type: integer
                minimum: 1
              cursor:
                description: >-
                  Opaque pagination token from `cursor.next` of the previous
                  page. Requires `with_cursor`.
                type: string
              rebase_multiplier:
                $ref: '#/components/schemas/rebase_multiplier'
            example:
              nonce: 1234567
              trades: true
              cl_ord_id: 9cc788d8-9c00-4b25-94d3-26d93603948d
  schemas:
    open-2:
      type: object
      properties:
        result:
          title: OpenOrders
          description: Open Orders
          type: object
          properties:
            open:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/open'
                x-additionalPropertiesName: txid
            cursor:
              $ref: '#/components/schemas/cursor'
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
    open:
      title: OpenOrder
      description: Open Order
      type: object
      properties:
        refid:
          description: Referral order transaction ID that created this order
          type: string
          nullable: true
        userref:
          description: >-
            Optional numeric, client identifier associated with one or more
            orders.
          type: integer
          nullable: true
        cl_ord_id:
          description: Optional alphanumeric, client identifier associated with the order.
          type: string
          nullable: true
        status:
          description: |
            Status of order
              * pending = order pending book entry
              * open = open order
              * closed = closed order
              * canceled = order canceled
              * expired = order expired
          type: string
          enum:
            - pending
            - open
            - closed
            - canceled
            - expired
        opentm:
          description: Unix timestamp of when order was placed
          type: number
        starttm:
          description: Unix timestamp of order start time (or 0 if not set)
          type: number
        expiretm:
          description: Unix timestamp of order end time (or 0 if not set)
          type: number
        descr:
          title: OrderDescription
          description: Order description info
          type: object
          properties:
            pair:
              description: Asset pair
              type: string
            type:
              description: Type of order (buy/sell)
              type: string
              enum:
                - buy
                - sell
            ordertype:
              $ref: '#/components/schemas/ordertype'
            price:
              description: primary price
              type: string
            price2:
              description: Secondary price
              type: string
            leverage:
              description: Amount of leverage
              type: string
            order:
              description: Order description
              type: string
            close:
              description: Conditional close order description (if conditional close set)
              type: string
            aclass:
              description: Asset class of the pair
              type: string
        time_in_force:
          description: |
            Time-in-force of the order:
              * `gtc` = good till cancelled
              * `ioc` = immediate or cancel
              * `gtd` = good till date
              * `fok` = fill or kill
          type: string
          enum:
            - gtc
            - ioc
            - gtd
            - fok
        vol:
          description: Volume of order (base currency)
          type: string
        vol_exec:
          description: Volume executed (base currency)
          type: string
        cost:
          description: Total cost (quote currency unless)
          type: string
        fee:
          description: Total fee (quote currency)
          type: string
        price:
          description: Average price (quote currency)
          type: string
        stopprice:
          description: Stop price (quote currency)
          type: string
        limitprice:
          description: >-
            Triggered limit price (quote currency, when limit based order type
            triggered)
          type: string
        displayvol:
          description: >-
            For iceberg orders, the visible quantity shown in the book (base
            currency)
          type: string
        displayvolremain:
          description: >-
            For iceberg orders, the remaining visible quantity currently shown
            in the book (base currency)
          type: string
        ext_ord_id:
          description: External order ID
          type: string
        link_id:
          description: Original order ID of an edited order
          type: string
        reduce_only:
          description: Indicates a reduce-only order. Only present if `true`.
          type: boolean
        trigger:
          description: >
            Price signal used to trigger "stop-loss" "take-profit"
            "stop-loss-limit" "take-profit-limit" orders.
              * `last` is the implied trigger if this field is not set.
          type: string
          enum:
            - last
            - index
          default: last
        margin:
          description: Indicates if the order is funded on margin.
          type: boolean
        misc:
          description: |
            Comma delimited list of miscellaneous info

              * `stopped` triggered by stop price
              * `touched` triggered by touch price
              * `liquidated` liquidation
              * `partial` partial fill
              * `amended` order parameters modified
          type: string
        sender_sub_id:
          description: >-
            For institutional accounts, identifies underlying sub-account/trader
            for Self Trade Prevention (STP).
          type: string
          nullable: true
        oflags:
          $ref: '#/components/schemas/oflags'
        trades:
          description: >-
            List of trade IDs related to order (if trades info requested and
            data available)
          type: array
          items:
            type: string
    cursor:
      title: Cursor
      description: >-
        Pagination cursor. Only present when `with_cursor` is `true` and more
        results are available.
      type: object
      nullable: true
      properties:
        next:
          description: Pass as `cursor` in the next request to fetch the following page.
          type: string
          nullable: true
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
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
