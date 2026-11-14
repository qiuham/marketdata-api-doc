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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-open-positions'
updated_at: 2026-11-13
---

# Get Open Positions

> Get information about open margin positions.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/OpenPositions
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
  /private/OpenPositions:
    post:
      tags:
        - Account Data
      summary: Get Open Positions
      description: >
        Get information about open margin positions.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades`
      operationId: getOpenPositions
      parameters:
        - $ref: '#/components/parameters/account_id'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - nonce
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                txid:
                  type: string
                  description: Comma delimited list of txids to limit output to
                docalcs:
                  type: boolean
                  description: Whether to include P&L calculations
                  default: false
                consolidation:
                  type: string
                  description: Consolidate positions by market/pair
                  enum:
                    - market
                rebase_multiplier:
                  $ref: '#/components/schemas/rebase_multiplier'
            examples:
              get Open Position:
                value:
                  nonce: 1695828490
                  docalcs: false
                  consolidation: market
                  txid: STMH53C-C54CG-4SO42I, ST4USDQ-ZQBMB-FGET2G
      responses:
        '200':
          description: Open positions info retrieved.
          content:
            application/json:
              schema:
                properties:
                  result:
                    description: >-
                      Open positions keyed by trade txid. When `consolidation`
                      is `market`, a list of positions consolidated by pair is
                      returned instead.
                    oneOf:
                      - type: object
                        title: Positions
                        additionalProperties:
                          x-additionalPropertiesName: txid
                          title: txid
                          type: object
                          properties:
                            ordertxid:
                              type: string
                              description: Order ID responsible for the position
                            class:
                              type: string
                              description: Asset class of the position
                            posstatus:
                              type: string
                              description: Position status
                              enum:
                                - open
                                - closed
                            pair:
                              description: Asset pair
                              type: string
                            time:
                              description: Unix timestamp of trade
                              type: number
                            type:
                              type: string
                              description: Direction (buy/sell) of position
                              enum:
                                - buy
                                - sell
                            ordertype:
                              type: string
                              description: Order type used to open position
                              enum:
                                - limit
                                - market
                            cost:
                              type: string
                              description: Opening cost of position (in quote currency)
                            fee:
                              type: string
                              description: Opening fee of position (in quote currency)
                            vol:
                              type: string
                              description: Position opening size (in base currency)
                            vol_closed:
                              type: string
                              description: Quantity closed (in base currency)
                            margin:
                              type: string
                              description: Initial margin consumed (in quote currency)
                            value:
                              type: string
                              description: >-
                                Current value of remaining position (if
                                `docalcs` requested)
                            net:
                              type: string
                              description: >-
                                Unrealised P&L of remaining position (if
                                `docalcs` requested)
                            terms:
                              type: string
                              description: Funding cost and term of position
                            rollovertm:
                              type: string
                              description: Timestamp of next margin rollover fee
                            misc:
                              type: string
                              description: Comma delimited list of add'l info
                            oflags:
                              type: string
                              description: Comma delimited list of opening order flags
                      - type: array
                        title: Consolidated positions
                        items:
                          type: object
                          title: ConsolidatedPosition
                          description: Open margin positions consolidated by pair.
                          required:
                            - pair
                            - class
                            - positions
                            - type
                            - leverage
                            - cost
                            - fee
                            - vol
                            - vol_closed
                            - margin
                          properties:
                            pair:
                              description: Asset pair
                              type: string
                            class:
                              type: string
                              description: Asset class of the positions
                            positions:
                              type: string
                              description: Number of positions consolidated into this entry
                            type:
                              type: string
                              description: Direction (buy/sell) of the positions
                              enum:
                                - buy
                                - sell
                            leverage:
                              type: string
                              description: >-
                                Average leverage of the consolidated positions,
                                or `n/a`
                            cost:
                              type: string
                              description: >-
                                Opening cost of the positions (in quote
                                currency)
                            fee:
                              type: string
                              description: Opening fee of the positions (in quote currency)
                            vol:
                              type: string
                              description: Opening size of the positions (in base currency)
                            vol_closed:
                              type: string
                              description: Quantity closed (in base currency)
                            margin:
                              type: string
                              description: Initial margin consumed (in quote currency)
                            value:
                              type: string
                              description: >-
                                Current value of remaining positions (if
                                `docalcs` requested)
                            net:
                              type: string
                              description: >-
                                Unrealised P&L of remaining positions (if
                                `docalcs` requested)
                  error:
                    $ref: '#/components/schemas/error'
                example:
                  error: []
                  result:
                    TF5GVO-T7ZZ2-6NBKBI:
                      ordertxid: OLWNFG-LLH4R-D6SFFP
                      posstatus: open
                      pair: XXBTZUSD
                      time: 1605280097.8294
                      type: buy
                      ordertype: limit
                      cost: '104610.52842'
                      fee: '289.06565'
                      vol: '8.82412861'
                      vol_closed: '0.20200000'
                      margin: '20922.10568'
                      value: '258797.5'
                      net: '+154186.9728'
                      terms: 0.0100% per 4 hours
                      rollovertm: '1616672637'
                      misc: ''
                      oflags: ''
                    T24DOR-TAFLM-ID3NYP:
                      ordertxid: OIVYGZ-M5EHU-ZRUQXX
                      posstatus: open
                      pair: XXBTZUSD
                      time: 1607943827.3172
                      type: buy
                      ordertype: limit
                      cost: '145756.76856'
                      fee: '335.24057'
                      vol: '8.00000000'
                      vol_closed: '0.00000000'
                      margin: '29151.35371'
                      value: '240124.0'
                      net: '+94367.2314'
                      terms: 0.0100% per 4 hours
                      rollovertm: '1616672637'
                      misc: ''
                      oflags: ''
                    TYMRFG-URRG5-2ZTQSD:
                      ordertxid: OF5WFH-V57DP-QANDAC
                      posstatus: open
                      pair: XXBTZUSD
                      time: 1610448039.8374
                      type: buy
                      ordertype: limit
                      cost: '0.00240'
                      fee: '0.00000'
                      vol: '0.00000010'
                      vol_closed: '0.00000000'
                      margin: '0.00048'
                      value: '0'
                      net: '+0.0006'
                      terms: 0.0100% per 4 hours
                      rollovertm: '1616672637'
                      misc: ''
                      oflags: ''
                    TAFGBN-TZNFC-7CCYIM:
                      ordertxid: OF5WFH-V57DP-QANDAC
                      posstatus: open
                      pair: XXBTZUSD
                      time: 1610448039.8448
                      type: buy
                      ordertype: limit
                      cost: '2.40000'
                      fee: '0.00264'
                      vol: '0.00010000'
                      vol_closed: '0.00000000'
                      margin: '0.48000'
                      value: '3.0'
                      net: '+0.6015'
                      terms: 0.0100% per 4 hours
                      rollovertm: '1616672637'
                      misc: ''
                      oflags: ''
                    T4O5L3-4VGS4-IRU2UL:
                      ordertxid: OF5WFH-V57DP-QANDAC
                      posstatus: open
                      pair: XXBTZUSD
                      time: 1610448040.7722
                      type: buy
                      ordertype: limit
                      cost: '21.59760'
                      fee: '0.02376'
                      vol: '0.00089990'
                      vol_closed: '0.00000000'
                      margin: '4.31952'
                      value: '27.0'
                      net: '+5.4133'
                      terms: 0.0100% per 4 hours
                      rollovertm: '1616672637'
                      misc: ''
                      oflags: ''
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
  schemas:
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
