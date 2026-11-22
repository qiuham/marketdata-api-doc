---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/user/userlsp
api_type: WebSocket
updated_at: 2026-11-22 18:59:23.116574
---

# user.lsp

> Notifications for an LSP (Liquidity Support Program) participant subaccount: assignment attempts (successful or failed), enable/disable state changes, and effective configuration changes.

Subscribe to this channel with an API key belonging to the LSP participant subaccount itself. See `user.liquidation` for the notification sent to the liquidated (source) user whose position was transferred.

A **successful** assignment is also delivered on the [Starbase FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api) session of the Starbase Member that owns that portfolio: a TradeCaptureReport (`35=AE`) with TradeType (828) `3` (position move), TransferReason (830) `ASSIGNED`, and LiquidationMechanism (8002) `LSP`. TrdMatchID (880) on that report is `starbase_match_id` on the successful `transfer` notification. You do not need this WebSocket channel to receive successful assignments if that Member's Drop Copy session already covers the portfolio.

This channel is still required for what Drop Copy does not send: a failed assignment attempt (`success: false`), and `enabled`, `disabled`, and `configuration_changed`. Only a position move whose reason is admin is omitted from Drop Copy. LSP and ADL assignments are sent.

Every notification includes a `type` field identifying the event kind — see the notification schema for the full list of types and which fields accompany each.

**📖 Related Article:** [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.lsp
id: user.lsp
title: 'user.lsp '
description: >
  Notifications for an LSP (Liquidity Support Program) participant subaccount:
  assignment attempts (successful or failed), enable/disable state changes, and
  effective configuration changes.


  Subscribe to this channel with an API key belonging to the LSP participant
  subaccount itself. See `user.liquidation` for the notification sent to the
  liquidated (source) user whose position was transferred.


  A **successful** assignment is also delivered on the [Starbase FIX Drop
  Copy](https://docs.deribit.com/starbase/fix-drop-copy-api) session of the
  Starbase Member that owns that portfolio: a TradeCaptureReport (`35=AE`) with
  TradeType (828) `3` (position move), TransferReason (830) `ASSIGNED`, and
  LiquidationMechanism (8002) `LSP`. TrdMatchID (880) on that report is
  `starbase_match_id` on the successful `transfer` notification. You do not need
  this WebSocket channel to receive successful assignments if that Member's Drop
  Copy session already covers the portfolio.


  This channel is still required for what Drop Copy does not send: a failed
  assignment attempt (`success: false`), and `enabled`, `disabled`, and
  `configuration_changed`. Only a position move whose reason is admin is omitted
  from Drop Copy. LSP and ADL assignments are sent.


  Every notification includes a `type` field identifying the event kind — see
  the notification schema for the full list of types and which fields accompany
  each.


  **📖 Related Article:** [Liquidity Support Program (LSP) API
  Guide](https://docs.deribit.com/articles/lsp-api-guide)
servers:
  - id: production
    protocol: wss
    host: deribit.com/ws/api/v2
    bindings: []
    variables: []
  - id: testnet
    protocol: wss
    host: test.deribit.com/ws/api/v2
    bindings: []
    variables: []
address: user.lsp
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_lsp
    title: Send subscribe request
    description: Client sends subscription request for user
    type: send
    messages:
      - &ref_4
        id: subscription_message
        contentType: application/json
        payload:
          - name: Subscription Notification Data
            description: Server sends subscription notification data
            type: object
            properties:
              - name: data
                type: object
                required: true
                properties:
                  - name: type
                    type: string
                    description: >
                      The kind of LSP (Liquidity Support Program) event this
                      notification represents:

                      - `transfer`: An assignment attempt to this participant
                      completed — check `success` to see whether it succeeded
                      (fully or partially) or failed and was redistributed to
                      other participants (or fell through to ADL).

                      - `enabled`: This participant's LSP configuration
                      transitioned from disabled to enabled.

                      - `disabled`: This participant's LSP configuration
                      transitioned from enabled to disabled — check `automatic`
                      to see whether this was a manual change or an automatic
                      disable after repeated transfer failures.

                      - `configuration_changed`: This participant's effective
                      configuration changed (enable state and/or any group
                      limit, including a change to the platform-wide default
                      that affects this participant). Fired on every
                      configuration write, including no-op enable/disable
                      transitions.
                    enumValues:
                      - transfer
                      - enabled
                      - disabled
                      - configuration_changed
                    required: true
                  - name: instrument_name
                    type: string
                    description: Present for `transfer` only.
                    required: false
                  - name: direction
                    type: string
                    description: Present for `transfer` only.
                    enumValues:
                      - buy
                      - sell
                    required: false
                  - name: amount
                    type: number
                    description: >-
                      Present for `transfer` only. Size of the position assigned
                      (or attempted).
                    required: false
                  - name: price
                    type: number
                    description: >-
                      Present for `transfer` only. The transfer price applied to
                      this assignment attempt.
                    required: false
                  - name: currency
                    type: string
                    description: Present for `transfer` only.
                    enumValues:
                      - BTC
                      - ETH
                      - USDC
                      - USDT
                      - EURR
                    required: false
                  - name: success
                    type: boolean
                    description: >-
                      Present for `transfer` only. `true` if the assignment
                      succeeded, `false` if it failed (see `error_reason`). A
                      successful transfer is also sent on Starbase FIX Drop Copy
                      as a TradeCaptureReport (`35=AE`, TradeType (828) `3`)
                      when the portfolio belongs to a Starbase Member; a failed
                      one is not.
                    required: false
                  - name: starbase_match_id
                    type: integer
                    description: >-
                      Present for a successful `transfer` executed on Starbase.
                      Equals `TrdMatchID` (tag 880) on the matching FIX Drop
                      Copy TradeCaptureReport.
                    required: false
                  - name: error_reason
                    type: string
                    description: >-
                      Present for `transfer` only, and only when `success` is
                      `false`. Machine-readable failure reason.
                    enumValues:
                      - platform_locked
                      - lock_count_exceeded
                      - timeout
                      - temporarily_unavailable
                      - not_enough_funds
                      - internal_error
                    required: false
                  - name: automatic
                    type: boolean
                    description: >-
                      Present for `disabled` only. `true` if this was an
                      automatic disable after repeated transfer failures,
                      `false` if a manual configuration change.
                    required: false
                  - name: failure_count
                    type: integer
                    description: >-
                      Present for `disabled` only, and only when `automatic` is
                      `true`. Number of transfer failures that triggered the
                      auto-disable.
                    required: false
                  - name: window_minutes
                    type: integer
                    description: >-
                      Present for `disabled` only, and only when `automatic` is
                      `true`. Length of the failure-counting window, in minutes.
                    required: false
                  - name: configuration
                    type: object
                    description: >-
                      Present for `configuration_changed` only. The
                      participant's resolved effective configuration: `enabled`,
                      plus every cooldown group's effective limit percentage
                      (`group_limits`, keyed by group) — per-participant
                      overrides are already resolved against the platform-wide
                      defaults, so every group appears here regardless of
                      whether this participant has an explicit override.
                    required: false
                    properties:
                      - name: enabled
                        type: boolean
                        description: >-
                          Whether this subaccount is currently an active LSP
                          participant eligible to receive assignments.
                        required: true
                      - name: group_limits
                        type: object
                        description: >
                          The effective assignment limit for each cooldown
                          group, expressed as a percentage of the participant's
                          own equity. Keyed by group: `"1"` through `"6"`
                          (crypto tiers, `"6"` is the catch-all tier) or `"rwa"`
                          (real-world-asset instruments, e.g. tokenized
                          equities/commodities).


                          Every group appears here — per-participant overrides
                          are already resolved against the platform-wide
                          defaults. A value of `0` means assignments for that
                          group are disabled entirely.
                        required: true
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                type:
                  description: >
                    The kind of LSP (Liquidity Support Program) event this
                    notification represents:

                    - `transfer`: An assignment attempt to this participant
                    completed — check `success` to see whether it succeeded
                    (fully or partially) or failed and was redistributed to
                    other participants (or fell through to ADL).

                    - `enabled`: This participant's LSP configuration
                    transitioned from disabled to enabled.

                    - `disabled`: This participant's LSP configuration
                    transitioned from enabled to disabled — check `automatic` to
                    see whether this was a manual change or an automatic disable
                    after repeated transfer failures.

                    - `configuration_changed`: This participant's effective
                    configuration changed (enable state and/or any group limit,
                    including a change to the platform-wide default that affects
                    this participant). Fired on every configuration write,
                    including no-op enable/disable transitions.
                  type: string
                  enum:
                    - transfer
                    - enabled
                    - disabled
                    - configuration_changed
                  x-parser-schema-id: <anonymous-schema-1546>
                instrument_name:
                  type: string
                  description: Present for `transfer` only.
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-1547>
                direction:
                  description: Present for `transfer` only.
                  type: string
                  enum:
                    - buy
                    - sell
                  x-parser-schema-id: <anonymous-schema-1548>
                amount:
                  description: >-
                    Present for `transfer` only. Size of the position assigned
                    (or attempted).
                  type: number
                  x-parser-schema-id: <anonymous-schema-1549>
                price:
                  description: >-
                    Present for `transfer` only. The transfer price applied to
                    this assignment attempt.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1550>
                currency:
                  type: string
                  description: Present for `transfer` only.
                  enum:
                    - BTC
                    - ETH
                    - USDC
                    - USDT
                    - EURR
                  x-parser-schema-id: <anonymous-schema-1551>
                success:
                  description: >-
                    Present for `transfer` only. `true` if the assignment
                    succeeded, `false` if it failed (see `error_reason`). A
                    successful transfer is also sent on Starbase FIX Drop Copy
                    as a TradeCaptureReport (`35=AE`, TradeType (828) `3`) when
                    the portfolio belongs to a Starbase Member; a failed one is
                    not.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1552>
                starbase_match_id:
                  description: >-
                    Present for a successful `transfer` executed on Starbase.
                    Equals `TrdMatchID` (tag 880) on the matching FIX Drop Copy
                    TradeCaptureReport.
                  type: integer
                  x-parser-schema-id: <anonymous-schema-1553>
                error_reason:
                  description: >-
                    Present for `transfer` only, and only when `success` is
                    `false`. Machine-readable failure reason.
                  type: string
                  enum:
                    - platform_locked
                    - lock_count_exceeded
                    - timeout
                    - temporarily_unavailable
                    - not_enough_funds
                    - internal_error
                  x-parser-schema-id: <anonymous-schema-1554>
                automatic:
                  description: >-
                    Present for `disabled` only. `true` if this was an automatic
                    disable after repeated transfer failures, `false` if a
                    manual configuration change.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1555>
                failure_count:
                  description: >-
                    Present for `disabled` only, and only when `automatic` is
                    `true`. Number of transfer failures that triggered the
                    auto-disable.
                  type: integer
                  x-parser-schema-id: <anonymous-schema-1556>
                window_minutes:
                  description: >-
                    Present for `disabled` only, and only when `automatic` is
                    `true`. Length of the failure-counting window, in minutes.
                  type: integer
                  x-parser-schema-id: <anonymous-schema-1557>
                configuration:
                  description: >-
                    Present for `configuration_changed` only. The participant's
                    resolved effective configuration: `enabled`, plus every
                    cooldown group's effective limit percentage (`group_limits`,
                    keyed by group) — per-participant overrides are already
                    resolved against the platform-wide defaults, so every group
                    appears here regardless of whether this participant has an
                    explicit override.
                  type: object
                  properties:
                    enabled:
                      description: >-
                        Whether this subaccount is currently an active LSP
                        participant eligible to receive assignments.
                      type: boolean
                      x-parser-schema-id: <anonymous-schema-1559>
                    group_limits:
                      description: >
                        The effective assignment limit for each cooldown group,
                        expressed as a percentage of the participant's own
                        equity. Keyed by group: `"1"` through `"6"` (crypto
                        tiers, `"6"` is the catch-all tier) or `"rwa"`
                        (real-world-asset instruments, e.g. tokenized
                        equities/commodities).


                        Every group appears here — per-participant overrides are
                        already resolved against the platform-wide defaults. A
                        value of `0` means assignments for that group are
                        disabled entirely.
                      type: object
                      additionalProperties:
                        type: number
                        x-parser-schema-id: <anonymous-schema-1561>
                      x-parser-schema-id: <anonymous-schema-1560>
                  required:
                    - enabled
                    - group_limits
                  x-parser-schema-id: <anonymous-schema-1558>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-1562>
              required:
                - type
                - timestamp
              type: object
              x-parser-schema-id: <anonymous-schema-1545>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1544>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "type": "transfer",
              "instrument_name": "BTC-PERPETUAL",
              "direction": "sell",
              "amount": 5000,
              "price": 63481.75,
              "currency": "BTC",
              "success": true,
              "starbase_match_id": 987654321,
              "timestamp": 1750000400000
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: user.lsp
  - &ref_1
    id: receive_user_lsp
    title: Receive user
    description: Client receives user notifications
    type: receive
    messages:
      - &ref_3
        id: subscribe_request
        contentType: application/json
        payload:
          - name: Subscription Request
            description: >-
              Client sends subscription request to subscribe to notification
              channel. Please refer to [Notification
              page](https://docs.deribit.com/articles/notifications) for more
              information.
            type: object
            properties:
              - name: jsonrpc
                type: string
                description: '2.0'
                required: true
              - name: id
                type: integer
                required: true
              - name: method
                type: string
                enumValues:
                  - public/subscribe
                  - private/subscribe
                required: true
              - name: params
                type: object
                required: true
                properties:
                  - name: channels
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: string
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            jsonrpc:
              type: string
              const: '2.0'
              x-parser-schema-id: <anonymous-schema-1538>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1539>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1540>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1543>
                  x-parser-schema-id: <anonymous-schema-1542>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1541>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1537>
        title: Subscription Request
        description: >-
          Client sends subscription request to subscribe to notification
          channel. Please refer to [Notification
          page](https://docs.deribit.com/articles/notifications) for more
          information.
        example: |-
          {
            "jsonrpc": "2.0",
            "method": "private/subscribe",
            "id": 42,
            "params": {
              "channels": [
                "user.lsp"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
receiveOperations:
  - *ref_2
sendMessages:
  - *ref_3
receiveMessages:
  - *ref_4
extensions:
  - id: x-parser-unique-object-id
    value: user.lsp
securitySchemes: []

````

## Related topics

- [user.liquidation ](https://docs.deribit.com/subscriptions/user/userliquidation.md)
- [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide.md)
- [Starbase FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md)
- [user.isolated.liquidation ](https://docs.deribit.com/subscriptions/user/userisolatedliquidation.md)
- [private/get_lsp_participants_usage](https://docs.deribit.com/api-reference/lsp/private-get_lsp_participants_usage.md)