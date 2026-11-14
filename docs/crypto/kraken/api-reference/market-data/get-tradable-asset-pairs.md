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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-tradable-asset-pairs'
updated_at: 2026-11-13
---

# Get Tradable Asset Pairs

> Get tradable asset pairs




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/AssetPairs
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
  /public/AssetPairs:
    get:
      tags:
        - Market Data
      summary: Get Tradable Asset Pairs
      description: |
        Get tradable asset pairs
      operationId: getTradableAssetPairs
      parameters:
        - $ref: '#/components/parameters/assetVersion'
        - in: query
          name: pair
          description: Asset pairs to get data for
          schema:
            type: string
          example: BTC/USD,ETH/BTC
        - in: query
          name: aclass_base
          schema:
            type: string
            enum:
              - currency
              - tokenized_asset
            default: currency
          description: |
            Filters the asset class to retrieve (optional)

              * `currency` = spot currency pairs.
              * `tokenized_asset` = tokenized asset pairs, i.e. xStocks.
        - in: query
          name: info
          schema:
            type: string
            enum:
              - info
              - leverage
              - fees
              - margin
            default: info
          description: |
            Info to retrieve (optional)

              * `info` = all info
              * `leverage` = leverage info
              * `fees` = fees schedule
              * `margin` = margin info
        - in: query
          name: country_code
          description: >-
            Filter for response to only include pairs available in the provided
            country/region (ISO 3166-1 alpha-2 code).
          schema:
            type: string
          example: GB
        - in: query
          name: execution_venue
          schema:
            type: string
            enum:
              - international
              - bitnomial_exchange
            default: international
          description: |
            Comma-separated list of execution venues to filter by (optional)

              * `international` = International exchange
              * `bitnomial_exchange` = Bitnomial exchange
      responses:
        '200':
          description: Tradable asset pairs retrieved.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    description: Pair names and their info
                    type: object
                    additionalProperties:
                      $ref: '#/components/schemas/pairs'
                  error:
                    $ref: '#/components/schemas/error'
                example:
                  error: []
                  result:
                    XETHXXBT:
                      altname: ETHXBT
                      wsname: ETH/XBT
                      aclass_base: currency
                      base: XETH
                      aclass_quote: currency
                      quote: XXBT
                      lot: unit
                      cost_decimals: 6
                      pair_decimals: 5
                      lot_decimals: 8
                      lot_multiplier: 1
                      leverage_buy:
                        - 2
                        - 3
                        - 4
                        - 5
                      leverage_sell:
                        - 2
                        - 3
                        - 4
                        - 5
                      fees: []
                      fees_maker: []
                      fee_volume_currency: ZUSD
                      margin_call: 80
                      margin_stop: 40
                      ordermin: '0.01'
                      costmin: '0.00002'
                      tick_size: '0.00001'
                      status: online
                      long_position_limit: 1100
                      short_position_limit: 400
                    XXBTZUSD:
                      altname: XBTUSD
                      wsname: XBT/USD
                      aclass_base: currency
                      base: XXBT
                      aclass_quote: currency
                      quote: ZUSD
                      lot: unit
                      cost_decimals: 5
                      pair_decimals: 1
                      lot_decimals: 8
                      lot_multiplier: 1
                      leverage_buy:
                        - 2
                        - 3
                        - 4
                        - 5
                      leverage_sell:
                        - 2
                        - 3
                        - 4
                        - 5
                      fees: []
                      fees_maker: []
                      fee_volume_currency: ZUSD
                      margin_call: 80
                      margin_stop: 40
                      ordermin: '0.0001'
                      costmin: '0.5'
                      tick_size: '0.1'
                      status: online
                      long_position_limit: 250
                      short_position_limit: 200
      security: []
components:
  parameters:
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
  schemas:
    pairs:
      title: AssetPair
      description: Trading Asset Pair
      type: object
      x-additionalPropertiesName: pair
      properties:
        altname:
          description: Alternate pair name
          type: string
        wsname:
          description: WebSocket pair name (if available)
          type: string
        aclass_base:
          description: Asset class of base component
          type: string
        base:
          description: Asset ID of base component
          type: string
        aclass_quote:
          description: Asset class of quote component
          type: string
        quote:
          description: Asset ID of quote component
          type: string
        execution_venue:
          description: Execution venue where the order book for this pair is listed
          type: string
          enum:
            - international
            - bitnomial_exchange
        lot:
          description: Volume lot size
          type: string
          deprecated: true
        pair_decimals:
          description: Number of decimal places for prices in this pair
          type: integer
        cost_decimals:
          description: >-
            Number of decimal places for cost of trades in pair (quote asset
            terms)
          type: integer
        lot_decimals:
          description: Number of decimal places for volume (base asset terms)
          type: integer
        lot_multiplier:
          description: Amount to multiply lot volume by to get currency volume
          type: integer
        leverage_buy:
          description: Array of leverage amounts available when buying
          type: array
          items:
            type: integer
        leverage_sell:
          description: Array of leverage amounts available when selling
          type: array
          items:
            type: integer
        fees:
          description: >
            **DEPRECATED** as of 8 September 2026. Always returns an empty array
            (`[]`).


            Previously the taker fee schedule, as an array of `[<volume>,
            <percent fee>]` tuples. The field remains in the response for
            backwards compatibility but no longer carries any fee data.
          deprecated: true
          type: array
          items:
            type: array
            items:
              type: number
          example: []
        fees_maker:
          description: >
            **DEPRECATED** as of 8 September 2026. Always returns an empty array
            (`[]`).


            Previously the maker fee schedule, as an array of `[<volume>,
            <percent fee>]` tuples, for pairs on a maker/taker schedule. The
            field remains in the response for backwards compatibility but no
            longer carries any fee data.
          deprecated: true
          type: array
          items:
            type: array
            items:
              type: number
          example: []
        fee_volume_currency:
          description: Volume discount currency
          type: string
        margin_call:
          description: Margin call level
          type: integer
        margin_stop:
          description: Stop-out/liquidation margin level
          type: integer
        ordermin:
          description: Minimum order size (in terms of base currency)
          type: string
        costmin:
          description: Minimum order cost (in terms of quote currency)
          type: string
        tick_size:
          description: Minimum increment between valid price levels
          type: string
        status:
          description: >-
            Status of asset. Possible values: `online`, `cancel_only`,
            `post_only`, `limit_only`, `reduce_only`.
          type: string
        long_position_limit:
          description: Maximum long margin position size (in terms of base currency)
          type: integer
        short_position_limit:
          description: Maximum short margin position size (in terms of base currency)
          type: integer
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
