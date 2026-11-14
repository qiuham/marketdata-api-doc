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
source_url: 'https://docs.kraken.com/api-reference/earn/list-earn-allocations'
updated_at: 2026-11-13
---

# List Earn Allocations

> List all allocations for the user.

Requires the `Query Funds` API key permission.

By default all allocations are returned, even for strategies that have been
used in the past and have zero balance now. That is so that the user can see
how much was earned with given strategy in the past.
`hide_zero_allocations` parameter can be used to remove zero balance entries
from the output.  Paging hasn't been implemented for this method as we don't
expect the result for a particular user to be overwhelmingly large.

All amounts in the output can be denominated in a currency of user's choice
(the `converted_asset` parameter).

Information about when the next reward will be paid to the client is also
provided in the output.

Allocated funds can be in up to 4 states:
- bonding
- allocated
- exit_queue (ETH only)
- unbonding

Any funds in `total` not in `bonding`/`unbonding` are simply allocated and
earning rewards. Depending on the strategy funds in the other 3 states can
also be earning rewards. Consult the output of `/Earn/Strategies` to know
whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still
earns rewards.

Note that for `ETH`, when the funds are in the `exit_queue` state, the
`expires` time given is the time when the funds will have finished
unbonding, not when they go from exit queue to unbonding.

(Un)bonding time estimate can be inaccurate right after having (de)allocated the
funds. Wait 1-2 minutes after (de)allocating to get an accurate result.



## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/Earn/Allocations
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
  /private/Earn/Allocations:
    post:
      tags:
        - Earn
      summary: List Earn Allocations
      description: >-
        List all allocations for the user.


        Requires the `Query Funds` API key permission.


        By default all allocations are returned, even for strategies that have
        been

        used in the past and have zero balance now. That is so that the user can
        see

        how much was earned with given strategy in the past.

        `hide_zero_allocations` parameter can be used to remove zero balance
        entries

        from the output.  Paging hasn't been implemented for this method as we
        don't

        expect the result for a particular user to be overwhelmingly large.


        All amounts in the output can be denominated in a currency of user's
        choice

        (the `converted_asset` parameter).


        Information about when the next reward will be paid to the client is
        also

        provided in the output.


        Allocated funds can be in up to 4 states:

        - bonding

        - allocated

        - exit_queue (ETH only)

        - unbonding


        Any funds in `total` not in `bonding`/`unbonding` are simply allocated
        and

        earning rewards. Depending on the strategy funds in the other 3 states
        can

        also be earning rewards. Consult the output of `/Earn/Strategies` to
        know

        whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still

        earns rewards.


        Note that for `ETH`, when the funds are in the `exit_queue` state, the

        `expires` time given is the time when the funds will have finished

        unbonding, not when they go from exit queue to unbonding.


        (Un)bonding time estimate can be inaccurate right after having
        (de)allocated the

        funds. Wait 1-2 minutes after (de)allocating to get an accurate result.
      operationId: listAllocations
      requestBody:
        content:
          application/json:
            schema:
              description: Page request
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
                converted_asset:
                  nullable: true
                  description: >-
                    A secondary currency to express the value of your
                    allocations (the default is USD).
                  type: string
                hide_zero_allocations:
                  nullable: true
                  description: >-
                    Omit entries for strategies that were used in the past but
                    now they don't hold any allocation (the default is `false`)
                  type: boolean
              required:
                - nonce
              example:
                nonce: 30295839
                converted_asset: EUR
                hide_zero_allocations: true
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
                    description: Page response
                    type: object
                    properties:
                      converted_asset:
                        description: >-
                          A secondary asset to show the value of allocations.
                          (Eg. you also want to

                          see the value of your allocations in USD). Choose this
                          in the request

                          parameters.
                        type: string
                      items:
                        type: array
                        items:
                          type: object
                          properties:
                            amount_allocated:
                              description: Amounts allocated to this Earn strategy
                              type: object
                              properties:
                                bonding:
                                  nullable: true
                                  description: >-
                                    Amount allocated in bonding status. Only
                                    present when there are bonding allocations.
                                  type: object
                                  properties:
                                    allocation_count:
                                      description: >-
                                        The total number of allocations in this
                                        state for this asset
                                      type: integer
                                      format: uint
                                    allocations:
                                      description: >-
                                        Details about when each allocation will
                                        expire and move to the next state
                                      type: array
                                      items:
                                        description: >-
                                          Additional information about the
                                          allocation describing the amount
                                          contained within the allocation and when
                                          it will transition to the next state
                                        type: object
                                        properties:
                                          converted:
                                            description: >-
                                              Amount converted into the requested
                                              asset
                                            type: string
                                          created_at:
                                            description: >-
                                              The date and time which a request to
                                              either allocate was received and

                                              the funds started bonding.
                                            type: string
                                            format: date-time
                                          expires:
                                            description: >-
                                              The date at which the `Bonded`
                                              allocation will move to the `Earning`
                                              state.
                                            type: string
                                            format: date-time
                                          native:
                                            description: Amount in the native asset
                                            type: string
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                                exit_queue:
                                  nullable: true
                                  description: >-
                                    Amount allocated in the exit-queue status.
                                    Only present when there are exit_queue
                                    allocations.
                                  type: object
                                  properties:
                                    allocation_count:
                                      description: >-
                                        The total number of allocations in this
                                        state for this asset
                                      type: integer
                                      format: uint
                                    allocations:
                                      description: >-
                                        Details about when each allocation will
                                        expire and move to the next state
                                      type: array
                                      items:
                                        description: >-
                                          Additional information about the
                                          allocation describing the amount
                                          contained within the allocation and when
                                          it will transition to the next state
                                        type: object
                                        properties:
                                          converted:
                                            description: >-
                                              Amount converted into the requested
                                              asset
                                            type: string
                                          created_at:
                                            description: >-
                                              The date and time which a request to
                                              deallocate was received and processed.

                                              For a deallocation request to a strategy
                                              with an `exit-queue`, this will be the
                                              time the funds joined the exit queue.
                                            type: string
                                            format: date-time
                                          expires:
                                            description: >-
                                              The date/time when the funds will be
                                              unbonded.
                                            type: string
                                            format: date-time
                                          native:
                                            description: Amount in the native asset
                                            type: string
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                                pending:
                                  nullable: true
                                  description: >-
                                    Pending allocation amount - can be negative
                                    if the pending operation is deallocation.
                                    Only present when there are pending
                                    allocations.
                                  type: object
                                  properties:
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                                total:
                                  description: Total amount allocated to this Earn strategy
                                  type: object
                                  properties:
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                                unbonding:
                                  nullable: true
                                  description: >-
                                    Amount allocated in unbonding status. Only
                                    present when there are unbonding
                                    allocations.
                                  type: object
                                  properties:
                                    allocation_count:
                                      description: >-
                                        The total number of allocations in this
                                        state for this asset
                                      type: integer
                                      format: uint
                                    allocations:
                                      description: >-
                                        Details about when each allocation will
                                        expire and move to the next state
                                      type: array
                                      items:
                                        description: >-
                                          Additional information about the
                                          allocation describing the amount
                                          contained within the allocation and when
                                          it will transition to the next state
                                        type: object
                                        properties:
                                          converted:
                                            description: >-
                                              Amount converted into the requested
                                              asset
                                            type: string
                                          created_at:
                                            description: >-
                                              The date and time which a request to
                                              either allocate or deallocate was
                                              received and processed.


                                              For a deallocation request to a strategy
                                              with an `exit-queue`, this will be the
                                              time the funds joined the exit queue.
                                              For a deallocation request to a strategy
                                              without exit queue, this will be the
                                              time the funds started unbonding
                                            type: string
                                            format: date-time
                                          expires:
                                            description: >-
                                              The date/time the funds will be
                                              unbonded.
                                            type: string
                                            format: date-time
                                          native:
                                            description: Amount in the native asset
                                            type: string
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                            native_asset:
                              description: >-
                                The asset of the native currency of this
                                allocation
                              type: string
                            payout:
                              nullable: true
                              description: >-
                                Information about the current payout period,
                                absent if when there is no current payout
                                period.
                              type: object
                              properties:
                                accumulated_reward:
                                  description: >-
                                    Reward accumulated in the payout period
                                    until now
                                  type: object
                                  properties:
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                                estimated_reward:
                                  description: Estimated reward from now until the payout
                                  type: object
                                  properties:
                                    converted:
                                      description: >-
                                        Amount converted into the requested
                                        asset
                                      type: string
                                    native:
                                      description: Amount in the native asset
                                      type: string
                                period_end:
                                  description: Tentative date of the next reward payout.
                                  type: string
                                  format: date-time
                                period_start:
                                  description: >-
                                    When the current payout period started.
                                    Either the date of the last payout or when
                                    it was enabled.
                                  type: string
                                  format: date-time
                            strategy_id:
                              description: Unique ID for Earn Strategy
                              type: string
                            total_rewarded:
                              description: >-
                                Amount earned using the strategy during the
                                whole lifetime of user account
                              type: object
                              properties:
                                converted:
                                  description: Amount converted into the requested asset
                                  type: string
                                native:
                                  description: Amount in the native asset
                                  type: string
                      total_allocated:
                        description: >-
                          The total amount allocated across all strategies,
                          denominated in the `converted_asset` currency
                        type: string
                      total_rewarded:
                        description: >-
                          Amount earned across all strategies during the whole
                          lifetime of user account, denominated in
                          `converted_asset` currency
                        type: string
                example:
                  error: []
                  result:
                    converted_asset: USD
                    total_allocated: '49.2398'
                    total_rewarded: '0.0675'
                    next_cursor: '2'
                    items:
                      - strategy_id: ESDQCOL-WTZEU-NU55QF
                        native_asset: ETH
                        amount_allocated:
                          bonding:
                            native: '0.0210000000'
                            converted: '39.0645'
                            allocation_count: 2
                            allocations:
                              - created_at: '2023-07-06T10:52:05Z'
                                expires: '2023-08-19T02:34:05.807Z'
                                native: '0.0010000000'
                                converted: '1.8602'
                              - created_at: '2023-08-01T11:25:52Z'
                                expires: '2023-09-06T07:55:52.648Z'
                                native: '0.0200000000'
                                converted: '37.2043'
                          total:
                            native: '0.0210000000'
                            converted: '39.0645'
                        total_rewarded:
                          native: '0'
                          converted: '0.0000'
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
