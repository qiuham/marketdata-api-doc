---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/wss/rfq-trades'
updated_at: 2026-11-13
---

# Trade Status Stream

> WebSocket stream of your RFQ trades' status changes, authenticated once on the upgrade request.

See the [RFQ Trades Partner API guide](https://docs.polymarket.com/partners/rfq-trades.md) for the full trade flow.


## AsyncAPI

````yaml asyncapi-rfq-partner.json rfqTrades
id: rfqTrades
title: Rfq trades
description: ''
servers:
  - id: production
    protocol: wss
    host: external-rfq-partner.polymarket.com
    bindings: []
    variables: []
address: /v1/ws/rfq-trades
parameters: []
bindings:
  - protocol: ws
    version: latest
    value:
      method: GET
    schemaProperties:
      - name: method
        type: string
        description: GET
        required: false
operations:
  - &ref_1
    id: sendTradeUpdates
    title: Send trade updates
    description: >-
      The server sends each in-flight trade on connect, then every status
      change.
    type: send
    messages:
      - &ref_2
        id: tradeUpdate
        contentType: application/json
        payload:
          - name: trade_update
            description: >-
              A trade's current status, the same object `GET
              /v1/rfq-trades/{tradeId}` returns.
            type: object
            properties:
              - name: type
                type: string
                enumValues:
                  - trade_update
                required: true
              - name: trade
                type: object
                required: true
                properties:
                  - name: tradeId
                    type: string
                    required: true
                  - name: combo
                    type: object
                    description: A combo's on-chain identity. Present on combo trades only.
                    required: false
                    properties:
                      - name: conditionId
                        type: string
                        required: true
                      - name: tokenIdYes
                        type: string
                        description: A base-10 uint256.
                        required: true
                      - name: tokenIdNo
                        type: string
                        description: A base-10 uint256.
                        required: true
                      - name: legs
                        type: array
                        required: true
                        properties:
                          - name: marketId
                            type: string
                            description: A gamma market id.
                            required: true
                          - name: outcome
                            type: string
                            enumValues:
                              - 'yes'
                              - 'no'
                            required: true
                  - name: idempotencyKey
                    type: string
                    required: true
                  - name: status
                    type: string
                    description: >-
                      `PENDING` until the trade lands on-chain (`FILLED`) or is
                      refused or fails (`REJECTED`).
                    enumValues:
                      - PENDING
                      - FILLED
                      - REJECTED
                    required: true
                  - name: transactionHash
                    type: string
                    required: false
                  - name: failureReason
                    type: string
                    description: >-
                      Why a `REJECTED` trade failed. `execution_failed` is a
                      failure after submission to the exchange.
                    required: false
                  - name: createdAt
                    type: string
                    required: true
                  - name: filledAt
                    type: string
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: One message on the trade status stream.
          required:
            - type
            - trade
          properties:
            type:
              type: string
              enum:
                - trade_update
              x-parser-schema-id: <anonymous-schema-1>
            trade:
              type: object
              required:
                - tradeId
                - idempotencyKey
                - status
                - createdAt
              properties:
                tradeId:
                  type: string
                  format: uuid
                  x-parser-schema-id: <anonymous-schema-2>
                combo:
                  type: object
                  description: A combo's on-chain identity. Present on combo trades only.
                  required:
                    - conditionId
                    - tokenIdYes
                    - tokenIdNo
                    - legs
                  properties:
                    conditionId:
                      type: string
                      x-parser-schema-id: <anonymous-schema-3>
                    tokenIdYes: &ref_0
                      type: string
                      pattern: ^[0-9]+$
                      description: A base-10 uint256.
                      x-parser-schema-id: Uint256
                    tokenIdNo: *ref_0
                    legs:
                      type: array
                      items:
                        type: object
                        required:
                          - marketId
                          - outcome
                        properties:
                          marketId:
                            type: string
                            description: A gamma market id.
                            x-parser-schema-id: <anonymous-schema-5>
                          outcome:
                            type: string
                            enum:
                              - 'yes'
                              - 'no'
                            x-parser-schema-id: <anonymous-schema-6>
                        x-parser-schema-id: ComboLeg
                      x-parser-schema-id: <anonymous-schema-4>
                  x-parser-schema-id: Combo
                idempotencyKey:
                  type: string
                  x-parser-schema-id: <anonymous-schema-7>
                status:
                  type: string
                  enum:
                    - PENDING
                    - FILLED
                    - REJECTED
                  description: >-
                    `PENDING` until the trade lands on-chain (`FILLED`) or is
                    refused or fails (`REJECTED`).
                  x-parser-schema-id: TradeState
                transactionHash:
                  type: string
                  x-parser-schema-id: <anonymous-schema-8>
                failureReason:
                  description: >-
                    Why a `REJECTED` trade failed. `execution_failed` is a
                    failure after submission to the exchange.
                  anyOf:
                    - type: string
                      description: >
                        The machine-readable reason a check failed or a request
                        was rejected. New values may be

                        added. See the guardrail and validation guides for each
                        one.
                      enum:
                        - unknown_account
                        - account_restricted
                        - ofac_blocked
                        - insufficient_balance
                        - insufficient_allowance
                        - dependency_unavailable
                        - invalid_order
                        - token_market_mismatch
                        - stale_order
                        - fee_not_accepted
                        - market_not_tradable
                        - price_out_of_band
                        - price_deviation_exceeded
                        - price_mark_missing
                        - transaction_notional_exceeded
                        - taker_notional_below_minimum
                        - counterparty_notional_exceeded
                      x-parser-schema-id: RejectionReason
                    - type: string
                      enum:
                        - execution_failed
                      x-parser-schema-id: <anonymous-schema-10>
                  x-parser-schema-id: <anonymous-schema-9>
                createdAt:
                  type: string
                  format: date-time
                  x-parser-schema-id: <anonymous-schema-11>
                filledAt:
                  type: string
                  format: date-time
                  x-parser-schema-id: <anonymous-schema-12>
              x-parser-schema-id: TradeStatus
          x-parser-schema-id: TradeUpdateFrame
        title: trade_update
        description: >-
          A trade's current status, the same object `GET
          /v1/rfq-trades/{tradeId}` returns.
        example: |-
          {
            "type": "trade_update",
            "trade": {
              "tradeId": "6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
              "idempotencyKey": "partner-ref-123",
              "status": "FILLED",
              "transactionHash": "0x5e1c0b2a9f8d7c6b5a4e3d2c1b0a9f8e7d6c5b4a3e2d1c0b9a8f7e6d5c4b3a2e",
              "createdAt": "2026-07-24T12:34:56Z",
              "filledAt": "2026-07-24T12:35:12Z"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: tradeUpdate
    bindings: []
    extensions:
      - id: x-parser-unique-object-id
        value: rfqTrades
sendOperations: []
receiveOperations:
  - *ref_1
sendMessages: []
receiveMessages:
  - *ref_2
extensions:
  - id: x-parser-unique-object-id
    value: rfqTrades
securitySchemes:
  - id: RfqKeyId
    name: RFQ-Key-Id
    type: httpApiKey
    description: The public half of the partner's API key.
    in: header
    extensions: []
  - id: RfqTimestamp
    name: RFQ-Timestamp
    type: httpApiKey
    description: Unix seconds, within 30 seconds of server time.
    in: header
    extensions: []
  - id: RfqSignature
    name: RFQ-Signature
    type: httpApiKey
    description: base64url(HMAC-SHA256(secret, timestamp + method + path + body)), padded.
    in: header
    extensions: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
