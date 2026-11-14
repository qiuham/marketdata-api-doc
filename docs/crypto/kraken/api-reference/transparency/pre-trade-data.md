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
source_url: 'https://docs.kraken.com/api-reference/transparency/pre-trade-data'
updated_at: 2026-11-13
---

# Pre-Trade Data

> Returns the price levels in the order book with aggregated order quantities at each price level. 
The top 10 levels are returned for each trading pair.




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/PreTrade
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
  /public/PreTrade:
    get:
      tags:
        - Transparency
      summary: Pre-Trade Data
      description: >
        Returns the price levels in the order book with aggregated order
        quantities at each price level. 

        The top 10 levels are returned for each trading pair.
      operationId: getPreTrade
      parameters:
        - name: symbol
          in: query
          required: true
          description: A list of symbols for the currency pairs.
          example: BTC/USD
          schema:
            type: string
            minLength: 3
            maxLength: 32
      responses:
        '200':
          description: The top price levels of the aggregated order book.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/pre-trade'
      security: []
components:
  schemas:
    pre-trade:
      title: PreTradeResponse
      type: object
      properties:
        result:
          description: An aggregated order book.
          type: object
          properties:
            symbol:
              type: string
              maxLength: 32
              description: The symbol of the currency pair.
              example: BTC/USD
            description:
              type: string
              maxLength: 350
              description: The full description of the currency pair.
              example: Bitcoin / US Dollars
            base_asset:
              type: string
              format: ISO 4217
              description: Currency code for the base asset.
              example: BTC
            base_dti_code:
              type: string
              description: Digital Token Identifier (DTI) code for the base asset.
            base_dti_short_name:
              type: string
              description: DTI short name for the base asset.
            quote_dti_code:
              type: string
              description: Digital Token Identifier (DTI) code for the quote asset.
            quote_dti_short_name:
              type: string
              description: DTI short name for the quote asset.
            base_notation:
              type: string
              description: Indicates how the quantity is expressed.
              enum:
                - UNIT
                - NOML
            quote_asset:
              type: string
              format: ISO 4217
              description: Currency in which the trading price is expressed.
              example: USD
            quote_notation:
              type: string
              description: Indicates that the price is expressed in monetary value.
              enum:
                - MONE
            venue:
              type: string
              format: ISO 10383
              description: >-
                Market Identifier Code (MIC) of the trading platform where the
                order was submitted.
              enum:
                - PGSL
            system:
              type: string
              description: Indicates the order system is a Central Limit Order Book.
              enum:
                - CLOB
            bids:
              type: array
              items:
                type: object
                properties:
                  side:
                    type: string
                    description: >-
                      Indicates whether the price level is a bid (BUY) or offer
                      (SELL).
                    enum:
                      - BUY
                  price:
                    type: string
                    description: Price level in the Central Limit Order Book (CLOB).
                    example: '102002.1'
                  qty:
                    type: string
                    description: The aggregated quantity at the price level.
                    example: '102002.1'
                  count:
                    type: integer
                    description: The number of orders in the price level.
                    minLength: 1
                  submission_ts:
                    type: string
                    format: ISO 8601
                    description: Timestamp the order at this price level was submitted.
                    example: '2024-05-30T12:34:56.123456Z'
                  publication_ts:
                    type: string
                    format: ISO 8601
                    description: Timestamp the price level was last updated and published.
                    example: '2024-05-30T12:34:56.123456Z'
            asks:
              type: array
              items:
                type: object
                properties:
                  side:
                    type: string
                    description: >-
                      Indicates whether the price level is a bid (BUY) or offer
                      (SELL).
                    enum:
                      - SELL
                  price:
                    type: string
                    description: Price level in the Central Limit Order Book (CLOB).
                    example: '102002.1'
                  qty:
                    type: string
                    description: The aggregated quantity at the price level.
                    example: '102002.1'
                  count:
                    type: integer
                    description: The number of orders in the price level.
                    minLength: 1
                  submission_ts:
                    type: string
                    format: ISO 8601
                    description: Timestamp the order at this price level was submitted.
                    example: '2024-05-30T12:34:56.123456Z'
                  publication_ts:
                    type: string
                    format: ISO 8601
                    description: Timestamp the price level was last updated and published.
                    example: '2024-05-30T12:34:56.123456Z'
        error:
          $ref: '#/components/schemas/error'
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
