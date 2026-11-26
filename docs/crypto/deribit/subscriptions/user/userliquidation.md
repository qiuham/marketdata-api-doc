---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/user/userliquidation
api_type: WebSocket
updated_at: 2026-11-26 19:02:02.423972
---

# user.liquidation

> Notifications about the authenticated account's own liquidation, auto-deleveraging (ADL), and LSP (Liquidity Support Program) activity — both as the account being liquidated/deleveraged and, for ADL, as a counterparty receiving a deleveraged position.

This includes the liquidated account's own transfer events (`lsp_transfer`, `adl_transfer`) as well as `adl_transfer_received` for any account that absorbs a position via ADL. See `user.lsp` for the additional notifications sent to the LSP participant *receiving* an assigned position (enable/disable and configuration changes).

A successful `lsp_transfer` or `adl_transfer` is also delivered on the [Starbase FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api) session of the Starbase Member that owns that portfolio, as a TradeCaptureReport (`35=AE`) with TradeType (828) `3`. On that report TransferReason (830) is `LIQUIDATED`. The receiving side's report has TransferReason (830) `ASSIGNED` and LiquidationMechanism (8002) `LSP` or `ADL`. Started/completed states and failed assignment attempts are WebSocket-only. Only a position move whose reason is admin is omitted from Drop Copy.

Every notification includes a `state` field identifying the stage of the process — see the notification schema for the full list of states and which fields accompany each.

**📖 Related Article:** [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.liquidation
id: user.liquidation
title: 'user.liquidation '
description: >
  Notifications about the authenticated account's own liquidation,
  auto-deleveraging (ADL), and LSP (Liquidity Support Program) activity — both
  as the account being liquidated/deleveraged and, for ADL, as a counterparty
  receiving a deleveraged position.


  This includes the liquidated account's own transfer events (`lsp_transfer`,
  `adl_transfer`) as well as `adl_transfer_received` for any account that
  absorbs a position via ADL. See `user.lsp` for the additional notifications
  sent to the LSP participant *receiving* an assigned position (enable/disable
  and configuration changes).


  A successful `lsp_transfer` or `adl_transfer` is also delivered on the
  [Starbase FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api)
  session of the Starbase Member that owns that portfolio, as a
  TradeCaptureReport (`35=AE`) with TradeType (828) `3`. On that report
  TransferReason (830) is `LIQUIDATED`. The receiving side's report has
  TransferReason (830) `ASSIGNED` and LiquidationMechanism (8002) `LSP` or
  `ADL`. Started/completed states and failed assignment attempts are
  WebSocket-only. Only a position move whose reason is admin is omitted from
  Drop Copy.


  Every notification includes a `state` field identifying the stage of the
  process — see the notification schema for the full list of states and which
  fields accompany each.


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
address: user.liquidation
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_liquidation
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
                  - name: state
                    type: string
                    description: >
                      The stage of the liquidation/ADL/LSP process this
                      notification represents:

                      - `liquidation_started` / `liquidation_completed`: The
                      standard (order-book) liquidation process has started or
                      completed for this account.

                      - `close_out_liquidation_started` /
                      `close_out_liquidation_completed`: The LSP/ADL close-out
                      process has started or completed for this account. An
                      account can go through this pair, the
                      `liquidation_started`/`liquidation_completed` pair, or
                      both in sequence (e.g. LSP/ADL close-out first, handed off
                      to standard liquidation if it can't fully resolve the
                      breach).

                      - `lsp_transfer`: A position was transferred off this
                      account to an LSP participant. Sent to the liquidated
                      (source) account — see the `user.lsp` channel for the
                      notification sent to the receiving participant.

                      - `adl_transfer`: A position was auto-deleveraged off this
                      account. Sent to the account being deleveraged (source).

                      - `adl_transfer_received`: A position was auto-deleveraged
                      onto this account from a counterparty. Sent to the
                      receiving (counterparty) account.
                    enumValues:
                      - liquidation_started
                      - liquidation_completed
                      - close_out_liquidation_started
                      - close_out_liquidation_completed
                      - lsp_transfer
                      - adl_transfer
                      - adl_transfer_received
                    required: true
                  - name: user_id
                    type: integer
                    description: Unique user identifier
                    required: true
                  - name: isolated
                    type: boolean
                    description: >-
                      Present and `true` only when this event applies to an
                      isolated-margin subaccount.
                    required: false
                  - name: currency
                    type: string
                    description: >-
                      Present on every state: the margin currency
                      (`liquidation_started`/`liquidation_completed`/`close_out_liquidation_started`/`close_out_liquidation_completed`)
                      or the transfer currency
                      (`lsp_transfer`/`adl_transfer`/`adl_transfer_received`).
                    enumValues:
                      - BTC
                      - ETH
                      - USDC
                      - USDT
                      - EURR
                    required: false
                  - name: margin_balance
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: maintenance_margin
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: initial_margin
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: close_out_margin
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: equity
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: instrument_name
                    type: string
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`.
                    required: false
                  - name: direction
                    type: string
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`. This account's own resulting
                      position side.
                    enumValues:
                      - buy
                      - sell
                    required: false
                  - name: amount
                    type: number
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`.
                    required: false
                  - name: price
                    type: number
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`. The transfer price applied.
                    required: false
                  - name: commission
                    type: number
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`. The commission charged (on
                      `lsp_transfer`/`adl_transfer`) or this account's share of
                      the commission (on `adl_transfer_received`, proportional
                      to the position this account absorbed). Intra-account
                      subaccount ADL moves are commissioned the same way as
                      moves onto another user's account.
                    required: false
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
                state:
                  description: >
                    The stage of the liquidation/ADL/LSP process this
                    notification represents:

                    - `liquidation_started` / `liquidation_completed`: The
                    standard (order-book) liquidation process has started or
                    completed for this account.

                    - `close_out_liquidation_started` /
                    `close_out_liquidation_completed`: The LSP/ADL close-out
                    process has started or completed for this account. An
                    account can go through this pair, the
                    `liquidation_started`/`liquidation_completed` pair, or both
                    in sequence (e.g. LSP/ADL close-out first, handed off to
                    standard liquidation if it can't fully resolve the breach).

                    - `lsp_transfer`: A position was transferred off this
                    account to an LSP participant. Sent to the liquidated
                    (source) account — see the `user.lsp` channel for the
                    notification sent to the receiving participant.

                    - `adl_transfer`: A position was auto-deleveraged off this
                    account. Sent to the account being deleveraged (source).

                    - `adl_transfer_received`: A position was auto-deleveraged
                    onto this account from a counterparty. Sent to the receiving
                    (counterparty) account.
                  type: string
                  enum:
                    - liquidation_started
                    - liquidation_completed
                    - close_out_liquidation_started
                    - close_out_liquidation_completed
                    - lsp_transfer
                    - adl_transfer
                    - adl_transfer_received
                  x-parser-schema-id: <anonymous-schema-1498>
                user_id:
                  description: Unique user identifier
                  type: integer
                  example: 57874
                  x-parser-schema-id: <anonymous-schema-1499>
                isolated:
                  description: >-
                    Present and `true` only when this event applies to an
                    isolated-margin subaccount.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-1500>
                currency:
                  type: string
                  description: >-
                    Present on every state: the margin currency
                    (`liquidation_started`/`liquidation_completed`/`close_out_liquidation_started`/`close_out_liquidation_completed`)
                    or the transfer currency
                    (`lsp_transfer`/`adl_transfer`/`adl_transfer_received`).
                  enum:
                    - BTC
                    - ETH
                    - USDC
                    - USDT
                    - EURR
                  x-parser-schema-id: <anonymous-schema-1501>
                margin_balance:
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1502>
                maintenance_margin:
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1503>
                initial_margin:
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1504>
                close_out_margin:
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1505>
                equity:
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1506>
                instrument_name:
                  type: string
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`.
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-1507>
                direction:
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`. This account's own resulting
                    position side.
                  type: string
                  enum:
                    - buy
                    - sell
                  x-parser-schema-id: <anonymous-schema-1508>
                amount:
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1509>
                price:
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`. The transfer price applied.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1510>
                commission:
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`. The commission charged (on
                    `lsp_transfer`/`adl_transfer`) or this account's share of
                    the commission (on `adl_transfer_received`, proportional to
                    the position this account absorbed). Intra-account
                    subaccount ADL moves are commissioned the same way as moves
                    onto another user's account.
                  type: number
                  x-parser-schema-id: <anonymous-schema-1511>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-1512>
              required:
                - state
                - user_id
                - timestamp
              type: object
              x-parser-schema-id: <anonymous-schema-1497>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1496>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "state": "lsp_transfer",
              "user_id": 7,
              "instrument_name": "BTC-PERPETUAL",
              "direction": "sell",
              "amount": 5000,
              "price": 63481.75,
              "currency": "BTC",
              "commission": 1.25,
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
        value: user.liquidation
  - &ref_1
    id: receive_user_liquidation
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
              x-parser-schema-id: <anonymous-schema-1490>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-1491>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-1492>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-1495>
                  x-parser-schema-id: <anonymous-schema-1494>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-1493>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1489>
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
                "user.liquidation"
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
    value: user.liquidation
securitySchemes: []

````

## Related topics

- [user.isolated.liquidation ](https://docs.deribit.com/subscriptions/user/userisolatedliquidation.md)
- [user.lsp ](https://docs.deribit.com/subscriptions/user/userlsp.md)
- [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [private/get_user_trades_by_order](https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_order.md)