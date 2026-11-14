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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-trades-history'
updated_at: 2026-11-13
---

# Get Trades History

> Retrieve information about trades/fills. By default, the most recent trades are returned.
* Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the asset pair (`pair_decimals` and `lot_decimals`), not the individual assets' precision (`decimals`).

**API Key Permissions Required:** `Orders and trades - Query closed orders & trades`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/TradesHistory
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
  /private/TradesHistory:
    post:
      tags:
        - Account Data
      summary: Get Trades History
      description: >
        Retrieve information about trades/fills. By default, the most recent
        trades are returned.

        * Unless otherwise stated, costs, fees, prices, and volumes are
        specified with the precision for the asset pair (`pair_decimals` and
        `lot_decimals`), not the individual assets' precision (`decimals`).


        **API Key Permissions Required:** `Orders and trades - Query closed
        orders & trades`
      operationId: getTradeHistory
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        $ref: '#/components/requestBodies/history'
      responses:
        '200':
          description: Trade history retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/history-2'
                example:
                  error: []
                  result:
                    trades:
                      THVRQM-33VKH-UCI7BS:
                        ordertxid: OQCLML-BW3P3-BUCMWZ
                        postxid: TKH2SE-M7IF5-CFI7LT
                        pair: XXBTZUSD
                        time: 1688667796.8802
                        type: buy
                        ordertype: limit
                        price: '30010.00000'
                        cost: '600.20000'
                        fee: '0.00000'
                        vol: '0.02000000'
                        margin: '0.00000'
                        misc: ''
                        trade_id: 40274859
                        maker: true
                      TCWJEG-FL4SZ-3FKGH6:
                        ordertxid: OQCLML-BW3P3-BUCMWZ
                        postxid: TKH2SE-M7IF5-CFI7LT
                        pair: XXBTZUSD
                        time: 1688667769.6396
                        type: buy
                        ordertype: limit
                        price: '30010.00000'
                        cost: '300.10000'
                        fee: '0.00000'
                        vol: '0.01000000'
                        margin: '0.00000'
                        misc: ''
                        trade_id: 39482674
                        maker: true
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
    history:
      required: true
      content:
        application/json:
          schema:
            title: Get Trades History Request Body
            required:
              - nonce
            type: object
            properties:
              nonce:
                $ref: '#/components/schemas/nonce'
              type:
                description: Type of trade
                type: string
                default: all
                enum:
                  - all
                  - any position
                  - closed position
                  - closing position
                  - no position
              trades:
                description: Whether or not to include trades related to position in output
                type: boolean
                default: false
              start:
                description: Starting unix timestamp or trade tx ID of results (exclusive)
                type: integer
              end:
                description: Ending unix timestamp or trade tx ID of results (inclusive)
                type: integer
              ofs:
                description: >-
                  Result offset for pagination. Deprecated, use `with_cursor`
                  and `cursor` instead. Must be absent or `0` when `with_cursor`
                  is `true`.
                type: integer
                deprecated: true
              without_count:
                description: >-
                  If true, does not retrieve count of trades. Request can be
                  noticeably faster for users with many trades as this avoids an
                  extra database query.
                type: boolean
                default: false
              consolidate_taker:
                description: >-
                  Whether or not to consolidate trades by individual taker
                  trades
                type: boolean
                default: true
              ledgers:
                description: >
                  Whether or not to include related ledger ids for given trade

                  <br><sub><sup>Note that setting this to true will slow request
                  performance</sub></sup>
                type: boolean
                default: false
              rebase_multiplier:
                $ref: '#/components/schemas/rebase_multiplier'
              aclass:
                description: Asset class of the `pair` filter.
                type: string
                default: forex
                enum:
                  - forex
                  - equity_pair
                  - futures_contract
                  - synthetic_pair
                  - external_pair
              pair:
                description: >-
                  Filter results to a single trading pair. An unrecognized pair
                  returns `EQuery:Unknown asset pair`.
                type: string
              limit:
                description: >-
                  Number of trades returned per page (1–100). Values above 100
                  get clamped to 100.
                type: integer
                default: 50
                minimum: 1
                maximum: 100
              with_cursor:
                description: >-
                  Use cursor-based pagination instead of `ofs`. The response
                  then includes `cursor.next` when more trades are available.
                type: boolean
                default: false
              cursor:
                description: >-
                  Opaque pagination token from `cursor.next` of the previous
                  page. Requires `with_cursor`.
                type: string
            example:
              nonce: 1695828490
              type: all
              trades: false
              consolidate_taker: true
              pair: BTC/USD
              limit: 75
  schemas:
    history-2:
      type: object
      properties:
        result:
          $ref: '#/components/schemas/history'
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
    history:
      title: TradeHistory
      description: Trade History
      type: object
      properties:
        count:
          description: >-
            Amount of available trades matching criteria. `0` is returned when
            `without_count` or `with_cursor` is `true`.
          type: integer
        trades:
          description: Trade info
          type: object
          additionalProperties:
            $ref: '#/components/schemas/trade-2'
            x-additionalPropertiesName: txid
        cursor:
          $ref: '#/components/schemas/cursor'
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
    trade-2:
      title: Trade
      description: Trade Info
      type: object
      properties:
        ordertxid:
          description: Order responsible for execution of trade
          type: string
        postxid:
          description: Position responsible for execution of trade
          type: string
        pair:
          description: Asset pair
          type: string
        time:
          description: Unix timestamp of trade
          type: number
        type:
          description: Type of order (buy/sell)
          type: string
          enum:
            - buy
            - sell
        ordertype:
          description: Order type
          type: string
        price:
          description: Average price order was executed at (quote currency)
          type: string
        cost:
          description: Total cost of order (quote currency)
          type: string
        fee:
          description: Total fee (quote currency)
          type: string
        vol:
          description: Volume (base currency)
          type: string
        margin:
          description: Initial margin (quote currency)
          type: string
        leverage:
          description: Amount of leverage used in trade
          type: string
        misc:
          description: |
            Comma delimited list of miscellaneous info:
            * `closing` &mdash; Trade closes all or part of a position
          type: string
        ledgers:
          description: |
            List of ledger ids for entries associated with trade
          type: array
          items:
            type: string
        trade_id:
          description: Unique identifier of trade executed
          type: integer
        maker:
          description: >
            `true` if trade was executed with user as the maker, `false` if
            taker
          type: boolean
        aclass:
          description: Asset class of the traded pair
          type: string
        ext_exec_id:
          description: External execution identifier (if any)
          type: string
        tradeordertype:
          description: >-
            Order type of the trade (e.g. `market`, `limit`). May differ from
            `ordertype` when the order type was converted on execution.
          type: string
        posstatus:
          description: |
            Position status (open/closed)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
          enum:
            - open
            - closed
        cprice:
          description: |
            Average price of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
        ccost:
          description: |
            Total cost of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
        cfee:
          description: |
            Total fee of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
        cvol:
          description: |
            Total volume of closed portion of position (base currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
        cmargin:
          description: |
            Total margin freed in closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
        net:
          description: >
            Net profit/loss of closed portion of position (quote currency, quote
            currency scale)

            <br><sub><sup>Only present if trade opened a position</sub></sup>
          type: string
        trades:
          description: |
            List of closing trades for position (if available)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
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
