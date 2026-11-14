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
source_url: 'https://docs.polymarket.com/api-reference/rfq-trades/get-trade'
updated_at: 2026-11-13
---

# Get an RFQ Trade

> Read a trade's current status, the source of truth for its outcome.

See the [RFQ Trades Partner API guide](https://docs.polymarket.com/partners/rfq-trades.md) for the full trade flow.


## OpenAPI

````yaml api-spec/rfq-partner-openapi.yaml GET /v1/rfq-trades/{tradeId}
openapi: 3.0.3
info:
  title: Polymarket RFQ Trades — Partner API
  version: 1.0.0
  description: >
    Trades two counterparties agreed through an RFQ, settled on Polymarket's CTF
    Exchange as one

    matched pair of orders. A partner pre-flights the agreed terms (`validate`),
    has the service

    build both orders (`prepare`), collects each side's signature, submits the
    signed pair, and

    follows the trade by polling or over the WebSocket stream (`asyncapi.yaml`).


    ## Authentication


    Every request except `/v1/time`, `/health` and `/ready` carries three
    headers:


    - `RFQ-Key-Id`: the public half of the partner's API key.

    - `RFQ-Timestamp`: Unix seconds. It must be within 30 seconds of server time
    either way;
      `GET /v1/time` returns the server clock.
    - `RFQ-Signature`: `base64url(HMAC-SHA256(secret, timestamp + method + path
    + body))`, padded
      (RFC 4648 §5), where `method` is uppercase, `path` is the URL path without the query string,
      and `body` is the exact bytes sent (empty for a `GET`).

    The partner is resolved from the key, never from the body. Another partner's
    trade is a `404`.


    ## Conventions


    - Amounts (`shares`, `makerAmount`, `takerAmount`, fees) are base-10 integer
    strings in 6-decimal
      units: `"1000000"` is one share or one pUSD. Prices and tolerances are decimal strings.
    - Request bodies are decoded strictly: an unknown field is a `400`.

    - Every error uses the `Error` envelope. `details.reason` is the
    machine-readable rejection, and
      new reasons may be added: treat an unknown one as a rejection.
    - Fees are set by the service and returned by `prepare`. A submission never
    quotes its own.
servers:
  - url: https://external-rfq-partner.polymarket.com
    description: Production
security:
  - RfqKeyId: []
    RfqTimestamp: []
    RfqSignature: []
tags:
  - name: RFQ trades
  - name: Markets
  - name: Status
paths:
  /v1/rfq-trades/{tradeId}:
    get:
      tags:
        - RFQ trades
      summary: Get a trade's status
      description: >-
        The source of truth for a trade's outcome, and the reconciliation path
        for the stream.
      operationId: getRfqTrade
      parameters:
        - name: tradeId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: The trade's current status.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TradeStatus'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  schemas:
    TradeStatus:
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
        combo:
          $ref: '#/components/schemas/Combo'
        idempotencyKey:
          type: string
        status:
          $ref: '#/components/schemas/TradeState'
        transactionHash:
          type: string
        failureReason:
          description: >-
            Why a `REJECTED` trade failed. `execution_failed` is a failure after
            submission to the exchange.
          anyOf:
            - $ref: '#/components/schemas/RejectionReason'
            - type: string
              enum:
                - execution_failed
        createdAt:
          type: string
          format: date-time
        filledAt:
          type: string
          format: date-time
    Combo:
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
        tokenIdYes:
          $ref: '#/components/schemas/Uint256'
        tokenIdNo:
          $ref: '#/components/schemas/Uint256'
        legs:
          type: array
          items:
            $ref: '#/components/schemas/ComboLeg'
    TradeState:
      type: string
      enum:
        - PENDING
        - FILLED
        - REJECTED
      description: >-
        `PENDING` until the trade lands on-chain (`FILLED`) or is refused or
        fails (`REJECTED`).
    RejectionReason:
      type: string
      description: >
        The machine-readable reason a check failed or a request was rejected.
        New values may be

        added. See the guardrail and validation guides for each one.
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
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          required:
            - code
            - message
            - retryable
            - details
          properties:
            code:
              type: string
              enum:
                - validation_failed
                - authentication_failed
                - not_found
                - stale_state
                - invalid_state
                - dependency_unavailable
                - internal
              description: Maps one to one to the HTTP status.
            message:
              type: string
              description: Human-readable, for logs.
            retryable:
              type: boolean
              description: Whether the same request may be sent again as is.
            details:
              type: object
              properties:
                reason:
                  $ref: '#/components/schemas/RejectionReason'
                party:
                  type: string
                  description: >-
                    The side the rejection is attributable to, when there is
                    one.
                field:
                  type: string
                  description: >-
                    The request field at fault, when there is one, e.g.
                    `orders[0].salt`.
      example:
        error:
          code: validation_failed
          message: 'stale_order (taker): order timestamp is 12m0s old (max 10m0s)'
          retryable: false
          details:
            reason: stale_order
            party: taker
    Uint256:
      type: string
      pattern: ^[0-9]+$
      description: A base-10 uint256.
    ComboLeg:
      type: object
      required:
        - marketId
        - outcome
      properties:
        marketId:
          type: string
          description: A gamma market id.
        outcome:
          type: string
          enum:
            - 'yes'
            - 'no'
  responses:
    BadRequest:
      description: A malformed body, an unknown field, or a malformed path parameter.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    Unauthorized:
      description: >-
        Missing or invalid authentication headers, or a timestamp outside the
        window.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    NotFound:
      description: No such resource for this partner.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    InternalError:
      description: An unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
  securitySchemes:
    RfqKeyId:
      type: apiKey
      in: header
      name: RFQ-Key-Id
      description: The public half of the partner's API key.
    RfqTimestamp:
      type: apiKey
      in: header
      name: RFQ-Timestamp
      description: Unix seconds, within 30 seconds of server time.
    RfqSignature:
      type: apiKey
      in: header
      name: RFQ-Signature
      description: >-
        base64url(HMAC-SHA256(secret, timestamp + method + path + body)),
        padded.

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
