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
source_url: 'https://docs.polymarket.com/cn/api-reference/rfq-trades/submit'
updated_at: 2026-11-13
---

# 提交 RFQ 交易

> 提交双方已签名的订单。交易以 PENDING 状态被接受，并异步执行。

完整的交易流程请参阅 [RFQ 交易合作伙伴 API 指南](https://docs.polymarket.com/partners/rfq-trades.md)。


## OpenAPI

````yaml api-spec/rfq-partner-openapi.yaml POST /v1/rfq-trades
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
  /v1/rfq-trades:
    post:
      tags:
        - RFQ trades
      summary: Submit a signed RFQ trade
      description: >
        Submits both signed orders. The trade is accepted as `PENDING` and
        executes asynchronously.

        `idempotencyKey` is the partner's own trade reference: a repeat of a
        known key returns the

        original trade, with its current status, and sets `Idempotency-Replayed:
        true`.
      operationId: submitRfqTrade
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SubmitRequest'
      responses:
        '201':
          description: The accepted trade, or the original one on an idempotent replay.
          headers:
            Idempotency-Replayed:
              description: >-
                `true` when the response replays an earlier submission of the
                same key.
              schema:
                type: string
                enum:
                  - 'true'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmitResult'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '413':
          $ref: '#/components/responses/PayloadTooLarge'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
        '500':
          $ref: '#/components/responses/InternalError'
        '502':
          $ref: '#/components/responses/DependencyUnavailable'
components:
  schemas:
    SubmitRequest:
      type: object
      required:
        - orders
        - idempotencyKey
      additionalProperties: false
      properties:
        marketId:
          type: string
          description: Required unless `marketSource` is `combo`.
        marketSource:
          $ref: '#/components/schemas/MarketSource'
        legs:
          type: array
          items:
            $ref: '#/components/schemas/ComboLeg'
        combination:
          $ref: '#/components/schemas/Combination'
        orders:
          type: array
          minItems: 2
          maxItems: 2
          description: Both signed orders, in any order.
          items:
            $ref: '#/components/schemas/SignedOrder'
        idempotencyKey:
          type: string
          maxLength: 128
          description: The partner's own reference for the trade.
        priceTolerance:
          type: string
          description: As on `PrepareRequest`.
        takerFeeAmount:
          type: string
          enum:
            - '0'
          description: >-
            Not an input. Omit it; anything but `0` is rejected with
            `fee_not_accepted`.
        makerFeeAmount:
          type: string
          enum:
            - '0'
          description: >-
            Not an input. Omit it; anything but `0` is rejected with
            `fee_not_accepted`.
    SubmitResult:
      type: object
      required:
        - tradeId
        - status
        - createdAt
      properties:
        tradeId:
          type: string
          format: uuid
        status:
          $ref: '#/components/schemas/TradeState'
        fees:
          type: object
          description: The fee each side is charged, keyed like the trade's parties.
          additionalProperties:
            $ref: '#/components/schemas/Amount'
        transactionHash:
          type: string
          description: Set once the trade has executed, so only on a replay.
        createdAt:
          type: string
          format: date-time
        combo:
          $ref: '#/components/schemas/Combo'
    MarketSource:
      type: string
      enum:
        - gamma
        - bespoke
        - combo
      default: gamma
      description: >-
        `gamma` for a Polymarket market id, `bespoke` for a bespoke market,
        `combo` for a market defined by its `legs`.
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
    Combination:
      type: string
      enum:
        - and
      description: The combo operator. Omitted means `and`.
    SignedOrder:
      type: object
      description: An `Order` exactly as prepared, with its signature.
      required:
        - salt
        - maker
        - signer
        - tokenId
        - makerAmount
        - takerAmount
        - side
        - signatureType
        - timestamp
        - metadata
        - builder
        - signature
      additionalProperties: false
      properties:
        salt:
          $ref: '#/components/schemas/Uint256'
        maker:
          $ref: '#/components/schemas/Address'
        signer:
          $ref: '#/components/schemas/Address'
        tokenId:
          $ref: '#/components/schemas/Uint256'
        makerAmount:
          $ref: '#/components/schemas/Amount'
        takerAmount:
          $ref: '#/components/schemas/Amount'
        side:
          type: integer
          enum:
            - 0
            - 1
        signatureType:
          type: integer
        timestamp:
          type: string
        metadata:
          type: string
        builder:
          type: string
        signature:
          type: string
          description: 0x hex.
        role:
          $ref: '#/components/schemas/Role'
    TradeState:
      type: string
      enum:
        - PENDING
        - FILLED
        - REJECTED
      description: >-
        `PENDING` until the trade lands on-chain (`FILLED`) or is refused or
        fails (`REJECTED`).
    Amount:
      type: string
      pattern: ^[0-9]+$
      description: A base-10 integer in 6-decimal units.
      example: '65000000'
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
    Address:
      type: string
      pattern: ^0x[0-9a-fA-F]{40}$
      example: '0x4444444444444444444444444444444444444444'
    Role:
      type: string
      enum:
        - maker
        - taker
      description: >
        Which fee rate a side pays. Set it on both sides or on neither; omitted,
        the `yes` side of a

        split or merge and the `buyer` of a trade are the taker.
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
    PayloadTooLarge:
      description: The body is over 64 KiB.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    UnprocessableEntity:
      description: The request is well-formed but rejected; `details.reason` says why.
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
    DependencyUnavailable:
      description: >-
        A dependency failed. Retry when `retryable` is true, with the same
        `idempotencyKey` for a submission.
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
