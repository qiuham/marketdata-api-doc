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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-maintenance-schedule'
updated_at: 2026-11-13
---

# Get Maintenance Schedule

> Get all scheduled maintenance events in the next 7-day window, ordered by
`expected_start_utc` ascending.

This is the planning view. It differs from the `upcoming_maintenance` array
on [Get System Status](/api/spot/rest/operation/operation-get-system-status),
which covers only the next 72 hours.

Each entry carries the same fields as an `upcoming_maintenance` entry,
including the derived `phase` and the `order_submission` /
`recommended_action` guidance for that phase.

Emergency incidents are not scheduled and therefore never appear here — read
the `emergency` array on Get System Status instead.




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/MaintenanceSchedule
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
  /public/MaintenanceSchedule:
    get:
      tags:
        - Market Data
      summary: Get Maintenance Schedule
      description: >
        Get all scheduled maintenance events in the next 7-day window, ordered
        by

        `expected_start_utc` ascending.


        This is the planning view. It differs from the `upcoming_maintenance`
        array

        on [Get System
        Status](/api/spot/rest/operation/operation-get-system-status),

        which covers only the next 72 hours.


        Each entry carries the same fields as an `upcoming_maintenance` entry,

        including the derived `phase` and the `order_submission` /

        `recommended_action` guidance for that phase.


        Emergency incidents are not scheduled and therefore never appear here —
        read

        the `emergency` array on Get System Status instead.
      operationId: getMaintenanceSchedule
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: object
                    properties:
                      events:
                        description: >
                          Scheduled maintenance events in the next 7 days,
                          ordered by

                          `expected_start_utc` ascending. Empty when nothing is
                          scheduled.
                        type: array
                        items:
                          $ref: '#/components/schemas/scheduledMaintenanceEvent'
                  error:
                    $ref: '#/components/schemas/error'
              examples:
                nominal:
                  summary: Two events scheduled
                  value:
                    error: []
                    result:
                      events:
                        - event_id: 21
                          title: Scheduled Maintenance - Website
                          expected_start_utc: '2026-05-11T09:00:00Z'
                          expected_end_utc: '2026-05-11T10:00:00Z'
                          time_to_start_s: 1740
                          phase: approaching_30m
                          affected_services:
                            - spot_trading
                          order_submission: allowed
                          recommended_action: reduce_activity
                          cancel_before_utc: '2026-05-11T08:55:00Z'
                          source_url: https://status.kraken.com/incidents/b7k2r9wqmn41
                        - event_id: 34
                          title: REST API infrastructure upgrade
                          expected_start_utc: '2026-05-14T02:00:00Z'
                          expected_end_utc: '2026-05-14T02:30:00Z'
                          time_to_start_s: 236940
                          phase: announced
                          affected_services:
                            - spot_rest
                            - spot_ws
                          order_submission: allowed
                          recommended_action: continue
                          cancel_before_utc: '2026-05-14T01:55:00Z'
                          source_url: https://status.kraken.com/incidents/d3f8h1xpqv62
                empty:
                  summary: Nothing scheduled
                  value:
                    error: []
                    result:
                      events: []
      security: []
components:
  schemas:
    scheduledMaintenanceEvent:
      description: Scheduled maintenance event.
      type: object
      properties:
        event_id:
          description: Identifier for the event, stable across phase transitions.
          type: integer
        title:
          description: Human-readable event title, as published on the status page.
          type: string
        expected_start_utc:
          description: Start of the maintenance window.
          type: string
          format: date-time
        expected_end_utc:
          description: Expected end of the maintenance window.
          type: string
          format: date-time
        time_to_start_s:
          description: >
            Seconds until `expected_start_utc`, evaluated when the response is
            served.

            Responses are cacheable, so clients needing a live countdown should
            derive

            it from `expected_start_utc` rather than re-reading this field.
          type: integer
        phase:
          description: |
            Approach phase, derived from `expected_start_utc - now()`:
            * `announced`  event first published
            * `reminder_24h`  24 hours out
            * `approaching_30m`  30 minutes out
            * `imminent_5m`  5 minutes out
            * `final_warning_30s`  30 seconds out
          type: string
          enum:
            - announced
            - reminder_24h
            - approaching_30m
            - imminent_5m
            - final_warning_30s
        affected_services:
          description: Kraken surfaces covered by this event.
          type: array
          items:
            $ref: '#/components/schemas/affectedService'
        order_submission:
          description: >
            Whether order submission is advisable in the current phase. Guidance

            only — the engine's own state is carried by the top-level `status`
            field.


            `allowed` in `announced`, `reminder_24h` and `approaching_30m`;

            `discouraged` in `imminent_5m`; `blocked` in `final_warning_30s`.
          type: string
          enum:
            - allowed
            - discouraged
            - blocked
        recommended_action:
          description: |
            Suggested client behaviour for the current phase.

            `continue` in `announced` and `reminder_24h`; `reduce_activity` in
            `approaching_30m`; `cancel_open_orders` in `imminent_5m`;
            `stop_new_orders` in `final_warning_30s`.
          type: string
          enum:
            - continue
            - reduce_activity
            - cancel_open_orders
            - stop_new_orders
        cancel_before_utc:
          description: >
            Deadline by which open orders should be cancelled:
            `expected_start_utc`

            minus 5 minutes while the event is scheduled; absent otherwise.
          type: string
          format: date-time
        source_url:
          description: Permalink to the event on the Kraken status page.
          type: string
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
    affectedService:
      description: >
        Kraken surface affected by a maintenance or emergency advisory. Derived
        from

        the status page components attached to the event.
      type: string
      enum:
        - spot_ws
        - spot_rest
        - spot_fix
        - spot_trading
        - futures_ws
        - futures_rest
        - futures_fix
        - futures_trading
        - all
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
