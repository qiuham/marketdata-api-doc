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
source_url: 'https://docs.kraken.com/api-reference/market-data/query-l3-order-book'
updated_at: 2026-11-13
---

# Query L3 Order Book

> Retrieve Level3 order book data, which provides individual order information at each price level.
This includes order IDs and timestamps for each order in the book. 

The Level3 endpoint requires authentication.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/Level3
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
  /private/Level3:
    post:
      tags:
        - Market Data
      summary: Query L3 Order Book
      description: >
        Retrieve Level3 order book data, which provides individual order
        information at each price level.

        This includes order IDs and timestamps for each order in the book. 


        The Level3 endpoint requires authentication.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getLevel3OrderBook
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                pair:
                  type: string
                  description: Asset pair to get order book for
                  example: YFI/EUR
                depth:
                  type: integer
                  description: >-
                    Number of price levels to return per side (bids/asks). Use 0
                    to return the full book.
                  enum:
                    - 0
                    - 10
                    - 25
                    - 100
                    - 250
                    - 1000
                  default: 100
                  example: 10
              required:
                - nonce
                - pair
      responses:
        '200':
          description: Level 3 order book data retrieved.
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
                      bids:
                        type: array
                        description: Bid orders
                        items:
                          type: object
                          properties:
                            price:
                              type: string
                              description: Bid price
                            qty:
                              type: string
                              description: Bid quantity
                            order_id:
                              type: string
                              description: Order ID
                            timestamp:
                              type: integer
                              description: Order timestamp (nanoseconds)
                      asks:
                        type: array
                        description: Ask orders
                        items:
                          type: object
                          properties:
                            price:
                              type: string
                              description: Ask price
                            qty:
                              type: string
                              description: Ask quantity
                            order_id:
                              type: string
                              description: Order ID
                            timestamp:
                              type: integer
                              description: Order timestamp (nanoseconds)
                  error:
                    type: array
                    items:
                      $ref: '#/components/schemas/error'
              example:
                error: []
                result:
                  pair: YFI/EUR
                  bids:
                    - price: '3062.00000'
                      qty: '0.29665800'
                      order_id: O5KJU4-IEQTM-NDMS6W
                      timestamp: 1765622008594292000
                    - price: '3062.00000'
                      qty: '0.13917400'
                      order_id: OERRY6-MXYER-6EQKNY
                      timestamp: 1765622011396903000
                  asks:
                    - price: '3066.00000'
                      qty: '0.00278335'
                      order_id: ORAWGV-N5L4J-LBA3WH
                      timestamp: 1765622008499456000
                    - price: '3067.00000'
                      qty: '0.13902210'
                      order_id: OZWNZS-QE3G6-ZPKZUT
                      timestamp: 1765622021013826600
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
