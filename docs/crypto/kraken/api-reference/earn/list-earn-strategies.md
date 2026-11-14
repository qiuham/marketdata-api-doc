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
source_url: 'https://docs.kraken.com/api-reference/earn/list-earn-strategies'
updated_at: 2026-11-13
---

# List Earn Strategies

> List earn strategies along with their parameters.

Requires a valid API key but not specific permission is required.

Returns only strategies that are available to the user
based on geographic region.

When the user does not meet the tier restriction, `can_allocate` will be
false and `allocation_restriction_info` indicates `Tier` as the restriction
reason. Earn products generally require Intermediate tier. Get your account verified
to access earn.

A note about `lock_type`:
- `instant`: can be deallocated without an unbonding period. This is called flexible in the UI.
- `bonded`: has an unbonding period. Deallocation will not happen until this period has passed.
- `flex`: "Kraken rewards". This is earning on your spot balances where eligible. It's turned on account wide
  from the UI and you cannot manually allocate to these strategies.

Paging isn't yet implemented, so the endpoint always returns all
data in the first page.



## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/Earn/Strategies
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
  /private/Earn/Strategies:
    post:
      tags:
        - Earn
      summary: List Earn Strategies
      description: >-
        List earn strategies along with their parameters.


        Requires a valid API key but not specific permission is required.


        Returns only strategies that are available to the user

        based on geographic region.


        When the user does not meet the tier restriction, `can_allocate` will be

        false and `allocation_restriction_info` indicates `Tier` as the
        restriction

        reason. Earn products generally require Intermediate tier. Get your
        account verified

        to access earn.


        A note about `lock_type`:

        - `instant`: can be deallocated without an unbonding period. This is
        called flexible in the UI.

        - `bonded`: has an unbonding period. Deallocation will not happen until
        this period has passed.

        - `flex`: "Kraken rewards". This is earning on your spot balances where
        eligible. It's turned on account wide
          from the UI and you cannot manually allocate to these strategies.

        Paging isn't yet implemented, so the endpoint always returns all

        data in the first page.
      operationId: listStrategies
      requestBody:
        content:
          application/json:
            schema:
              description: List strategies parameters
              type: object
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                ascending:
                  nullable: true
                  description: >-
                    `true` to sort ascending, `false` (the default) for
                    descending.
                  type: boolean
                asset:
                  nullable: true
                  description: Filter strategies by asset name
                  type: string
                cursor:
                  nullable: true
                  description: None to start at beginning/end, otherwise next page ID
                  type: string
                limit:
                  nullable: true
                  description: >-
                    How many items to return per page. Note that the limit may
                    be cap'd to lower value in the application code.
                  type: integer
                  format: uint16
                lock_type:
                  nullable: true
                  description: Filter strategies by lock type
                  type: array
                  items:
                    description: Type of a strategy
                    type: string
                    enum:
                      - flex
                      - bonded
                      - timed
                      - instant
              required:
                - nonce
              example:
                nonce: 30295839
                asset: DOT
        required: true
      responses:
        '200':
          description: Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/error'
                  result:
                    nullable: true
                    type: object
                    properties:
                      items:
                        type: array
                        items:
                          description: Parameters for a single strategy
                          type: object
                          properties:
                            allocation_fee:
                              description: Fee applied when allocating to this strategy
                              oneOf:
                                - type: string
                                  title: string
                                - type: integer
                                  title: integer
                                - type: number
                                  title: number
                            allocation_restriction_info:
                              description: >-
                                Reason list why user is not eligible for
                                allocating to the strategy
                              type: array
                              items:
                                description: >-
                                  Recoverable strategy restriction reasons,
                                  which are no preventing strategy from being
                                  returned by [`ListStrategiesResponse`].
                                type: string
                                enum:
                                  - tier
                            apr_estimate:
                              nullable: true
                              description: >-
                                The estimate is based on previous revenues from
                                the strategy. Optional hint, not always present.
                              type: object
                              properties:
                                high:
                                  description: Maximal yield percentage for one year
                                  type: string
                                low:
                                  description: Minimal yield percentage for one year
                                  type: string
                            asset:
                              description: The asset to invest for this earn strategy
                              type: string
                            auto_compound:
                              description: Auto compound choices for the earn strategy
                              oneOf:
                                - title: disabled
                                  description: >-
                                    Auto compound is not possible for any
                                    allocation
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - disabled
                                - title: enabled
                                  description: Auto compound is forced for all allocations
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - enabled
                                - title: optional
                                  description: >-
                                    Auto compound depends on user's preference
                                    and it comes with default value
                                  type: object
                                  properties:
                                    default:
                                      type: boolean
                                    type:
                                      type: string
                                      enum:
                                        - optional
                            can_allocate:
                              description: Is allocation available for this strategy
                              type: boolean
                            can_deallocate:
                              description: Is deallocation available for this strategy
                              type: boolean
                            deallocation_fee:
                              description: Fee applied when deallocating from this strategy
                              oneOf:
                                - type: string
                                  title: string
                                - type: integer
                                  title: integer
                                - type: number
                                  title: number
                            id:
                              description: The unique identifier for this strategy
                              type: string
                            lock_type:
                              description: Type of the strategy
                              oneOf:
                                - title: flex
                                  description: >-
                                    Either the whole asset balance or part of it
                                    is allocated to earn strategy and users are
                                    free to deallocate it anytime and most
                                    importantly the deallocation can be implicit
                                    (triggered by a trade, withdrawal from
                                    exchange, etc.).
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - flex
                                - title: bonded
                                  description: >-
                                    Explicit allocate and deallocate action by
                                    user is required and bonding/unbonding
                                    parameters apply.
                                  type: object
                                  properties:
                                    bonding_period:
                                      description: >-
                                        Duration of the bonding period, in
                                        seconds
                                      type: integer
                                    bonding_period_variable:
                                      description: >-
                                        Is the bonding period length variable
                                        (`true`) or static (`false`)
                                      type: boolean
                                    bonding_rewards:
                                      description: >-
                                        Whether rewards are earned during the
                                        bonding period (payouts occur after
                                        bonding is complete)
                                      type: boolean
                                    exit_queue_period:
                                      description: >-
                                        In order to remove funds, if this value
                                        is greater than 0, funds will first have
                                        to enter an exit queue and will have to
                                        wait for the exit queue period to end.
                                        Once ended, her funds will then follow
                                        and respect the `unbonding_period`.


                                        If the value of the exit queue period is
                                        0, then no waiting will have to occur
                                        and the exit queue will be skipped


                                        Rewards are always paid out for the exit
                                        queue
                                      type: integer
                                    payout_frequency:
                                      description: >-
                                        At what intervals are rewards
                                        distributed and credited to the user's
                                        ledger, in seconds
                                      type: integer
                                    type:
                                      type: string
                                      enum:
                                        - bonded
                                    unbonding_period:
                                      description: >-
                                        Duration of the unbonding period in
                                        seconds. In order to remove funds, you
                                        must wait for the unbonding period to
                                        pass after requesting removal before
                                        funds become available in her spot
                                        wallet
                                      type: integer
                                    unbonding_period_variable:
                                      description: >-
                                        Is the unbonding period length variable
                                        (`true`) or static (`false`)
                                      type: boolean
                                    unbonding_rewards:
                                      description: >-
                                        Whether rewards are earned and payouts
                                        are done during the unbonding period
                                      type: boolean
                                - title: instant
                                  description: >-
                                    Instant strategy lock type is a special case
                                    of bonded strategy with no bonding/unbonding
                                    period. It is equivalent of what used to be
                                    called "flex" in legacy staking system (not
                                    to be confused with Flex defined above).
                                    Explicit allocate/deallocate action is
                                    required.
                                  type: object
                                  properties:
                                    payout_frequency:
                                      description: >-
                                        At what intervals are rewards
                                        distributed and credited to the user's
                                        ledger, in seconds
                                      type: integer
                                    type:
                                      type: string
                                      enum:
                                        - instant
                            user_cap:
                              nullable: true
                              type: string
                              description: >-
                                The maximum amount of funds that any given user
                                may allocate to an account. Absence of value
                                means there is no limit. Zero means that all new
                                allocations will return an error (though
                                auto-compound is unaffected).
                            user_min_allocation:
                              nullable: true
                              type: string
                              description: >-
                                Minimum amount (in USD) for an allocation or
                                deallocation. Absence means no minimum.
                            yield_source:
                              description: Yield generation mechanism of this strategy
                              oneOf:
                                - description: >-
                                    Funds are staked on-chain, PoS is the source
                                    of yield.
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - staking
                                - description: >-
                                    Funds are put at work in another
                                    yield-generation financial mechanism.
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - off_chain
                      next_cursor:
                        nullable: true
                        description: >-
                          index to send into PageRequest for next page, None
                          means you've reached the end.
                        type: string
                example:
                  error: []
                  result:
                    next_cursor: '2'
                    items:
                      - id: ESRFUO3-Q62XD-WIOIL7
                        asset: DOT
                        lock_type:
                          type: instant
                          payout_frequency: 604800
                        apr_estimate:
                          low: '8.0000'
                          high: '12.0000'
                        user_min_allocation: '0.01'
                        allocation_fee: '0.0000'
                        deallocation_fee: '0.0000'
                        auto_compound:
                          type: enabled
                        yield_source:
                          type: staking
                        can_allocate: true
                        can_deallocate: true
                        allocation_restriction_info: []
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
