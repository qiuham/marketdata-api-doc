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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-trade-volume'
updated_at: 2026-11-13
---

# Get Trade Volume

> Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided. Fees will not be included if `pair` is not specified as Kraken fees differ by asset pair.
Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

`pair` accepts either a comma-delimited list of pair names or a list of `{ asset, aclass }` objects (the latter is required for non-forex classes such as `derivatives` or `equity_pair`). Set `fee_schedule` to `true` to additionally receive the full fee schedule per trading pair in the `schedules` field.

**API Key Permissions Required:** `Funds permissions - Query`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/TradeVolume
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
  /private/TradeVolume:
    post:
      tags:
        - Account Data
      summary: Get Trade Volume
      description: >
        Returns 30 day USD trading volume and resulting fee schedule for any
        asset pair(s) provided. Fees will not be included if `pair` is not
        specified as Kraken fees differ by asset pair.

        Note: If an asset pair is on a maker/taker fee schedule, the taker side
        is given in `fees` and maker side in `fees_maker`. For pairs not on
        maker/taker, they will only be given in `fees`.


        `pair` accepts either a comma-delimited list of pair names or a list of
        `{ asset, aclass }` objects (the latter is required for non-forex
        classes such as `derivatives` or `equity_pair`). Set `fee_schedule` to
        `true` to additionally receive the full fee schedule per trading pair in
        the `schedules` field.


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: getTradeVolume
      requestBody:
        $ref: '#/components/requestBodies/volume'
      responses:
        '200':
          description: Trade Volume retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/volume'
                example:
                  error: []
                  result:
                    currency: ZUSD
                    asset_class: currency
                    volume: '200709587.4223'
                    inputs:
                      domain_spot_volume_30d: '200709587.4223'
                      domain_futures_volume_30d: '0.0000'
                      domain_assets_on_platform: '0.0000'
                    fees:
                      XXBTZUSD:
                        fee: '0.1000'
                        minfee: '0.1000'
                        maxfee: '0.2600'
                        nextfee: null
                        tiervolume: '10000000.0000'
                        nextvolume: null
                    fees_maker:
                      XXBTZUSD:
                        fee: '0.0000'
                        minfee: '0.0000'
                        maxfee: '0.1600'
                        nextfee: null
                        tiervolume: '10000000.0000'
                        nextvolume: null
components:
  requestBodies:
    volume:
      required: true
      content:
        application/json:
          schema:
            title: Get Trade Volume
            required:
              - nonce
            type: object
            properties:
              nonce:
                $ref: '#/components/schemas/nonce'
              pair:
                description: >
                  Asset pair(s) for which to retrieve fee info (optional, but
                  required if any fee info is desired). Accepts one of the
                  following formats:

                  * A comma-delimited list of pair names — each is looked up as
                  a forex pair.

                  * A list of `{ asset, aclass }` objects (`pairs_with_class`).
                  Required to request fees for non-forex classes such as
                  `equity_pair`, `derivatives`, or `futures_contract`.
                anyOf:
                  - type: string
                    title: Comma-delimited list
                    description: >-
                      Comma-delimited list of pair names, each looked up as a
                      forex pair.
                  - type: array
                    title: List of pairs with class
                    description: >-
                      List of `{ asset, aclass }` objects. Required for
                      non-forex classes.
                    items:
                      type: object
                      required:
                        - asset
                        - aclass
                      properties:
                        asset:
                          description: >-
                            The pair name. All result amounts will be expressed
                            in units of this asset.
                          type: string
                        aclass:
                          description: The asset class of the pair.
                          type: string
                          enum:
                            - currency
                            - forex
                            - equity
                            - equity_pair
                            - nft
                            - derivatives
                            - tokenized_asset
                            - futures_contract
              fee-info:
                description: >-
                  Whether or not to include fee info in the results (legacy
                  parameter, accepted for backwards compatibility).
                default: false
                oneOf:
                  - type: string
                    title: string
                  - type: boolean
                    title: boolean
                  - type: number
                    title: number
              fee_schedule:
                description: >-
                  Whether to include the full fee schedule per trading pair in
                  the response (returned in `schedules`).
                type: boolean
                nullable: true
              rebase_multiplier:
                $ref: '#/components/schemas/rebase_multiplier'
            example:
              nonce: 1695828490
              pair:
                - asset: BTC/USD
                  aclass: forex
                - asset: PF_XBTUSD
                  aclass: derivatives
  schemas:
    volume:
      type: object
      properties:
        result:
          title: TradeVolume
          description: Trade Volume
          type: object
          required:
            - currency
            - volume
            - inputs
          properties:
            currency:
              description: >
                The asset used to express the trade volume value. The value in
                `volume` is expressed in units of this asset.
              type: string
            asset_class:
              description: The class of the asset used to express the trade volume value.
              type: string
              nullable: true
              enum:
                - currency
                - forex
                - equity
                - equity_pair
                - nft
                - derivatives
                - tokenized_asset
                - futures_contract
            volume:
              description: The total trading volume value.
              type: string
            inputs:
              description: >-
                Domain-aggregated input values evaluated against fee-schedule
                tier conditions.
              type: object
              required:
                - domain_assets_on_platform
                - domain_futures_volume_30d
                - domain_spot_volume_30d
              properties:
                domain_spot_volume_30d:
                  description: 30-day rolling spot trading volume.
                  type: string
                domain_futures_volume_30d:
                  description: 30-day rolling futures trading volume.
                  type: string
                domain_assets_on_platform:
                  description: Assets on platform.
                  type: string
            fees:
              description: >-
                A map describing the taker fees applicable to each trading pair
                (one entry per pair). `null` if `pair` is not requested.
              type: object
              nullable: true
              additionalProperties:
                $ref: '#/components/schemas/fees'
                x-additionalPropertiesName: pair
            fees_maker:
              description: >-
                A map describing the maker fees applicable to each trading pair
                (one entry per pair). `null` if `pair` is not requested.
              type: object
              nullable: true
              additionalProperties:
                $ref: '#/components/schemas/fees'
                x-additionalPropertiesName: pair
            volume_subaccounts:
              description: >
                Trade volume breakdown by subaccount. Only present when the
                requester is the domain's master account.
              type: array
              items:
                title: SubaccountVolume
                description: Trade volume for one subaccount in a domain.
                type: object
                required:
                  - iiban
                  - volume
                properties:
                  iiban:
                    description: The subaccount IIBAN.
                    type: string
                  volume:
                    description: The subaccount trade volume.
                    type: string
            schedules:
              description: >-
                Full fee schedule per trading pair. Present only when
                `fee_schedule` is requested.
              type: array
              nullable: true
              items:
                title: FeeSchedule
                description: Full fee schedule for a trading pair.
                type: object
                required:
                  - pair
                  - class
                  - tiers
                properties:
                  pair:
                    description: The trading pair to which the fee schedule applies.
                    type: string
                  class:
                    description: Trading pair class.
                    type: string
                    enum:
                      - currency
                      - forex
                      - equity
                      - equity_pair
                      - nft
                      - derivatives
                      - tokenized_asset
                      - futures_contract
                      - volume
                  tiers:
                    description: The tiers of the fee schedule.
                    type: array
                    items:
                      title: FeeScheduleTier
                      description: A single tier in a fee schedule.
                      type: object
                      required:
                        - maker_fee
                        - taker_fee
                      properties:
                        maker_fee:
                          description: Maker fee percentage for this tier.
                          type: string
                        taker_fee:
                          description: Taker fee percentage for this tier.
                          type: string
                        min_spot_volume:
                          description: >-
                            Minimum spot volume threshold for this tier, if
                            applicable.
                          type: string
                          nullable: true
                        min_futures_volume:
                          description: >-
                            Minimum 30-day futures volume threshold for this
                            tier, if applicable.
                          type: string
                          nullable: true
                        min_assets_on_platform:
                          description: >-
                            Minimum assets on platform threshold for this tier,
                            if applicable.
                          type: string
                          nullable: true
                        active:
                          description: >-
                            Whether this is the currently active tier for the
                            user.
                          type: boolean
                          nullable: true
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
    fees:
      title: FeeTierInfo
      description: >
        Fee and volume tier information. Fees are expressed as percentages, and
        volumes as absolute values.
      type: object
      required:
        - fee
        - minfee
        - maxfee
        - tiervolume
      properties:
        fee:
          description: Current trading fee.
          type: string
        minfee:
          description: Minimum trading fee (corresponding to the highest volume tier).
          type: string
        maxfee:
          description: Maximum trading fee (corresponding to the lowest volume tier).
          type: string
        nextfee:
          description: >-
            Next fee (applicable once the next volume tier is reached). `null`
            at the lowest fee tier.
          type: string
          nullable: true
        tiervolume:
          description: Current spot-volume tier threshold.
          type: string
        tierfuturesvolume:
          description: Current futures-volume tier threshold, when visible in the schedule.
          type: string
          nullable: true
        nextvolume:
          description: Next spot-volume tier threshold. `null` at the highest volume tier.
          type: string
          nullable: true
        nextfuturesvolume:
          description: Next futures-volume tier threshold, when visible in the schedule.
          type: string
          nullable: true
        volumeoffset:
          description: Volume adjustment (added to the trade volume when computing fees).
          type: string
          nullable: true
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
