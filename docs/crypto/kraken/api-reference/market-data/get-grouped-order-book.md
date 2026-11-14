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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-grouped-order-book'
updated_at: 2026-11-13
---

# Get Grouped Order Book

> The GroupedBook endpoint aggregates the volume in the order book over a specified tick range. 
It provides a summary of liquidity deep into the book, useful for user interface display.

Bids and asks between grouped price levels are accumulated to the nearest passive level (asks rounded up, bids down).




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/GroupedBook
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
  /public/GroupedBook:
    get:
      tags:
        - Market Data
      summary: Get Grouped Order Book
      description: >
        The GroupedBook endpoint aggregates the volume in the order book over a
        specified tick range. 

        It provides a summary of liquidity deep into the book, useful for user
        interface display.


        Bids and asks between grouped price levels are accumulated to the
        nearest passive level (asks rounded up, bids down).
      operationId: getGroupedOrderBook
      parameters:
        - in: query
          name: pair
          required: true
          schema:
            type: string
          description: Asset pair to get order book for
          example: BTC/USD
        - in: query
          name: depth
          schema:
            type: integer
            enum:
              - 10
              - 25
              - 100
              - 250
              - 1000
            default: 10
          description: The number of price levels to return per side (bids/asks).
          example: 10
        - in: query
          name: grouping
          schema:
            type: integer
            format: int32
            nullable: true
            enum:
              - 1
              - 5
              - 10
              - 25
              - 50
              - 100
              - 250
              - 500
              - 1000
            default: 1
          description: >-
            Specifies how many tick levels should be within each price level.
            Bids and asks between grouped price levels are accumulated to the
            nearest passive level (asks rounded up, bids down).
          example: 1000
      responses:
        '200':
          description: Grouped order book data retrieved.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: object
                    properties:
                      pair:
                        description: Asset pair
                        type: string
                      grouping:
                        type: integer
                        description: The grouping value used
                      bids:
                        type: array
                        description: Aggregated bid levels
                        items:
                          type: object
                          properties:
                            price:
                              type: string
                              description: Grouped price level
                            qty:
                              type: string
                              description: Aggregated quantity at this price level
                      asks:
                        type: array
                        description: Aggregated ask levels
                        items:
                          type: object
                          properties:
                            price:
                              type: string
                              description: Grouped price level
                            qty:
                              type: string
                              description: Aggregated quantity at this price level
                  error:
                    type: array
                    items:
                      $ref: '#/components/schemas/error'
              example:
                error: []
                result:
                  pair: BTC/USD
                  grouping: 1000
                  bids:
                    - price: '90400.00000'
                      qty: '19.83057746'
                    - price: '90300.00000'
                      qty: '45.35073006'
                    - price: '90200.00000'
                      qty: '35.33199856'
                    - price: '90100.00000'
                      qty: '32.40807838'
                    - price: '90000.00000'
                      qty: '46.00445468'
                    - price: '89900.00000'
                      qty: '22.71486458'
                    - price: '89800.00000'
                      qty: '11.55482018'
                    - price: '89700.00000'
                      qty: '13.77715743'
                    - price: '89600.00000'
                      qty: '27.72185770'
                    - price: '89500.00000'
                      qty: '14.09383330'
                  asks:
                    - price: '90500.00000'
                      qty: '38.96185061'
                    - price: '90600.00000'
                      qty: '55.96402032'
                    - price: '90700.00000'
                      qty: '34.64783055'
                    - price: '90800.00000'
                      qty: '25.26797469'
                    - price: '90900.00000'
                      qty: '20.48922196'
                    - price: '91000.00000'
                      qty: '14.87773628'
                    - price: '91100.00000'
                      qty: '18.99740224'
                    - price: '91200.00000'
                      qty: '19.00592802'
                    - price: '91300.00000'
                      qty: '4.05573682'
                    - price: '91400.00000'
                      qty: '1.60667017'
      security: []
components:
  schemas:
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
