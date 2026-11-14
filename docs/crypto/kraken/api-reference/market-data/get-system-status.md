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
source_url: 'https://docs.kraken.com/api-reference/market-data/get-system-status'
updated_at: 2026-11-13
---

# Get System Status

> Get the current system status or trading mode, along with any scheduled
maintenance or ongoing emergency advisories.

The `upcoming_maintenance` and `emergency` fields are additive — clients that do not read them are unaffected. Both are arrays; empty or absent when no advisory is active.

* `upcoming_maintenance` carries scheduled events that are within 72 hours. An event is removed once its maintenance window starts.
* `emergency` carries unresolved status page incidents. An incident is removed when it reaches `resolved`.

The top-level `status` field remains driven by the trading engine and is
independent of both arrays: an advisory describes *why* a state is happening
or coming — it does not dictate engine state.




## OpenAPI

````yaml /openapi/spot-rest.yaml get /public/SystemStatus
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
  /public/SystemStatus:
    get:
      tags:
        - Market Data
      summary: Get System Status
      description: >
        Get the current system status or trading mode, along with any scheduled

        maintenance or ongoing emergency advisories.


        The `upcoming_maintenance` and `emergency` fields are additive — clients
        that do not read them are unaffected. Both are arrays; empty or absent
        when no advisory is active.


        * `upcoming_maintenance` carries scheduled events that are within 72
        hours. An event is removed once its maintenance window starts.

        * `emergency` carries unresolved status page incidents. An incident is
        removed when it reaches `resolved`.


        The top-level `status` field remains driven by the trading engine and is

        independent of both arrays: an advisory describes *why* a state is
        happening

        or coming — it does not dictate engine state.
      operationId: getSystemStatus
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    properties:
                      status:
                        type: string
                        enum:
                          - online
                          - maintenance
                          - cancel_only
                          - post_only
                        description: >
                          Current system status:

                          * `online`  Kraken is operating normally. All order
                          types may be submitted and trades can occur.

                          * `maintenance`  The exchange is offline. No new
                          orders or cancellations may be submitted.

                          * `cancel_only`  Resting (open) orders can be
                          cancelled but no new orders may be submitted. No
                          trades will occur.

                          * `post_only`  Only post-only limit orders can be
                          submitted. Existing orders may still be cancelled. No
                          trades will occur.
                      timestamp:
                        type: string
                        description: Current timestamp (RFC3339)
                      upcoming_maintenance:
                        description: >
                          Scheduled maintenance advisories within the next 72
                          hours,

                          ordered by `expected_start_utc` ascending. Empty or
                          absent

                          when no scheduled event is active.
                        type: array
                        items:
                          $ref: '#/components/schemas/scheduledMaintenanceEvent'
                      emergency:
                        description: >
                          Unresolved incident advisories. Empty or absent when
                          no

                          incident is active.
                        type: array
                        items:
                          $ref: '#/components/schemas/emergencyEvent'
                  error:
                    $ref: '#/components/schemas/error'
              examples:
                nominal:
                  summary: No advisory active
                  value:
                    error: []
                    result:
                      status: online
                      timestamp: '2023-07-06T18:52:00Z'
                      upcoming_maintenance: []
                      emergency: []
                scheduledMaintenanceApproaching:
                  summary: Scheduled maintenance approaching
                  value:
                    error: []
                    result:
                      status: online
                      timestamp: '2026-05-11T08:30:00Z'
                      upcoming_maintenance:
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
                      emergency: []
                emergencyInProgress:
                  summary: Emergency in progress
                  value:
                    error: []
                    result:
                      status: cancel_only
                      timestamp: '2026-05-08T14:28:00Z'
                      upcoming_maintenance: []
                      emergency:
                        - event_id: 4821
                          title: Elevated API error rates
                          incident_status: identified
                          impact: critical
                          affected_services:
                            - spot_ws
                            - spot_rest
                            - spot_fix
                          started_at_utc: '2026-05-08T14:23:11Z'
                          next_steps:
                            - applies_to:
                                - spot_trading
                              type: expected_restart
                              expected_at_utc: '2026-05-08T14:30:00Z'
                          source_url: https://stspg.io/c378t4f7rh0n
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
    emergencyEvent:
      description: >
        Unplanned incident advisory, relayed from the Kraken status page.


        The object explains why a state is happening or coming — the engine's
        own

        state is carried by the top-level `status` field. Emergencies carry no

        `order_submission` or `recommended_action`: derive guidance from

        `incident_status`, `next_steps` and `status`.
      type: object
      properties:
        event_id:
          description: Identifier for the incident, stable for its lifetime.
          type: integer
        title:
          description: Human-readable incident title, as published on the status page.
          type: string
        incident_status:
          description: |
            Incident lifecycle state, relayed 1:1 from the status page:
            * `investigating`  cause not yet known
            * `identified`  cause known, remediation under way
            * `monitoring`  remediation applied, under observation
          type: string
          enum:
            - investigating
            - identified
            - monitoring
        impact:
          description: Severity as published on the status page.
          type: string
          enum:
            - none
            - minor
            - major
            - critical
        affected_services:
          description: Kraken surfaces covered by this incident.
          type: array
          items:
            $ref: '#/components/schemas/affectedService'
        started_at_utc:
          description: When the incident was opened.
          type: string
          format: date-time
        next_steps:
          description: >
            Forecast operational actions, ordered by `expected_at_utc`
            ascending.

            Empty when no forecast has been published.
          type: array
          items:
            $ref: '#/components/schemas/nextStep'
        source_url:
          description: Permalink to the incident on the Kraken status page.
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
    nextStep:
      description: |
        Forecast operational action during an emergency, published by Kraken
        operations. Absent when no reliable forecast exists.
      type: object
      properties:
        applies_to:
          description: Kraken surfaces this step applies to.
          type: array
          items:
            $ref: '#/components/schemas/affectedService'
        type:
          description: |
            Nature of the forecast action:
            * `expected_restart`  service restart
            * `expected_cancel_only`  transition to cancel-only
            * `expected_post_only`  transition to post-only
            * `expected_online`  return to normal operation
          type: string
          enum:
            - expected_restart
            - expected_cancel_only
            - expected_post_only
            - expected_online
        expected_at_utc:
          description: Forecast time of the action.
          type: string
          format: date-time
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
