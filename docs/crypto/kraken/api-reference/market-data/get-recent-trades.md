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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-recent-trades'
updated_at: 2026-11-13
---

# Get Recent Trades

> Returns the last 1000 trades by default




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/Trades
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
  /public/Trades:
    get:
      tags:
        - Market Data
      summary: Get Recent Trades
      description: |
        Returns the last 1000 trades by default
      operationId: getRecentTrades
      parameters:
        - $ref: '#/components/parameters/pair'
        - $ref: '#/components/parameters/assetVersion'
        - name: since
          in: query
          description: Return trade data since given timestamp
          schema:
            type: string
          example: '1616663618'
        - name: count
          in: query
          description: Return specific number of trades, up to 1000
          schema:
            type: integer
            minimum: 1
            maximum: 1000
            default: 1000
          example: 2
        - $ref: '#/components/parameters/asset_class'
      responses:
        '200':
          description: Trade data retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/trades'
                example:
                  error: []
                  result:
                    XXBTZUSD:
                      - - '30243.40000'
                        - '0.34507674'
                        - 1688669597.8277369
                        - b
                        - m
                        - ''
                        - 61044952
                      - - '30243.30000'
                        - '0.00376960'
                        - 1688669598.2804112
                        - s
                        - l
                        - ''
                        - 61044953
                      - - '30243.30000'
                        - '0.01235716'
                        - 1688669602.698379
                        - s
                        - m
                        - ''
                        - 61044956
                    last: '1688671969993150842'
      security: []
components:
  parameters:
    pair:
      in: query
      name: pair
      description: Asset pair to get data for
      required: true
      schema:
        type: string
      example: XBTUSD
    assetVersion:
      in: query
      name: assetVersion
      required: false
      schema:
        type: integer
        enum:
          - 1
      description: >
        Controls whether response keys and asset identifier fields use Kraken's
        internal names or display names.


        * Omitted (default): internal names are used. Asset keys use legacy
        `X`/`Z`-prefixed format (`XXBT`, `ZUSD`). Pair keys use the internal
        format (`XXBTZUSD`). Asset identifier fields (`base`, `quote`,
        `fee_volume_currency`) also use internal names.

        * `assetVersion=1`: display names are used. Asset keys become their
        canonical display names (`BTC`, `USD`). Pair keys become the
        slash-separated display format (`BTC/USD`). On `/public/AssetPairs`, the
        `base`, `quote`, and `fee_volume_currency` fields also switch to display
        names.


        Only `assetVersion=1` is currently supported. The `altname` and `wsname`
        fields are not affected by this parameter.
    asset_class:
      name: asset_class
      in: query
      description: >-
        This parameter is required on requests for non-crypto pairs, i.e. use
        `tokenized_asset` for xStocks.
      required: false
      schema:
        type: string
        enum:
          - tokenized_asset
  schemas:
    trades:
      type: object
      properties:
        result:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/trade'
            x-additionalPropertiesName: pair
          properties:
            last:
              type: string
              description: ID to be used as since when polling for new trade data
        error:
          $ref: '#/components/schemas/error'
    trade:
      title: TickData
      description: >
        Array of trade entries

        `[<price>, <volume>, <time>, <buy/sell>, <market/limit>,
        <miscellaneous>, <trade_id>]`
      type: array
      items:
        type: array
        items:
          oneOf:
            - type: string
              title: string
            - type: number
              title: number
          example:
            - '1205.00000'
            - '2.28253070'
            - 1668714225.5189962
            - b
            - l
            - ''
            - 41557503
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
