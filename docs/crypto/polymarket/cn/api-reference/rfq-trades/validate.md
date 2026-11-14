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
source_url: 'https://docs.polymarket.com/cn/api-reference/rfq-trades/validate'
updated_at: 2026-11-13
---

# 验证 RFQ 交易

> 运行提交这些条款时会执行的所有检查，不存储任何内容。

完整的交易流程请参阅 [RFQ 交易合作伙伴 API 指南](https://docs.polymarket.com/partners/rfq-trades.md)。


## OpenAPI

````yaml api-spec/rfq-partner-openapi.yaml POST /v1/rfq-trades/validate
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
  /v1/rfq-trades/validate:
    post:
      tags:
        - RFQ trades
      summary: Pre-flight proposed terms
      description: >
        Runs every check a submission of these terms would run and reports them
        all. Advisory:

        nothing is stored, and the same checks run again at submission. A
        completed validation is

        always a `200`; a failed check is a verdict in the body, not an error
        status.
      operationId: validateRfqTrade
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PrepareRequest'
      responses:
        '200':
          description: The verdict on each check.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationResult'
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
    PrepareRequest:
      type: object
      required:
        - operation
        - price
        - shares
        - parties
      additionalProperties: false
      properties:
        marketId:
          type: string
          description: Required unless `marketSource` is `combo`.
        marketSource:
          $ref: '#/components/schemas/MarketSource'
        legs:
          type: array
          description: The combo's legs, for `marketSource` `combo` only.
          items:
            $ref: '#/components/schemas/ComboLeg'
        combination:
          $ref: '#/components/schemas/Combination'
        operation:
          type: string
          enum:
            - split
            - merge
            - trade
          description: >
            `split`: both sides buy, one YES and one NO. `merge`: both sides
            sell, one YES and one NO.

            `trade`: one side buys an outcome token from the other.
        token:
          type: string
          enum:
            - 'yes'
            - 'no'
          description: The outcome token that changes hands, for `trade` only.
        price:
          type: string
          description: >-
            The agreed price in (0, 1). The YES price for a split or merge, the
            traded token's price for a trade.
          example: '0.65'
        shares:
          $ref: '#/components/schemas/Amount'
        parties:
          type: object
          description: >-
            Keyed `yes` and `no` for a split or merge, `buyer` and `seller` for
            a trade.
          additionalProperties:
            $ref: '#/components/schemas/PrepareParty'
        priceTolerance:
          type: string
          description: >-
            Tightens the price band to this fraction of the mark, e.g. `0.05`
            for ±5%. Wider than the default is refused.
    ValidationResult:
      type: object
      required:
        - valid
        - checks
        - checkedAt
      properties:
        valid:
          type: boolean
          description: Whether a submission of these terms would be accepted now.
        checks:
          type: object
          required:
            - market
          properties:
            market:
              $ref: '#/components/schemas/Check'
            price:
              $ref: '#/components/schemas/PriceCheck'
            parties:
              type: object
              description: Keyed like the request's `parties`.
              additionalProperties:
                $ref: '#/components/schemas/Check'
            guardrails:
              type: array
              description: >-
                One entry per guardrail, in the order they run. The first
                failure is the one a submission returns.
              items:
                $ref: '#/components/schemas/GuardrailCheck'
        checkedAt:
          type: string
          format: date-time
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
    Amount:
      type: string
      pattern: ^[0-9]+$
      description: A base-10 integer in 6-decimal units.
      example: '65000000'
    PrepareParty:
      type: object
      required:
        - maker
        - signatureType
      additionalProperties: false
      properties:
        maker:
          $ref: '#/components/schemas/Address'
        signer:
          allOf:
            - $ref: '#/components/schemas/Address'
          description: Defaults to `maker`.
        signatureType:
          type: integer
          description: >-
            The order signature type. `3` (deposit wallet) is the type partner
            trades use.
          example: 3
        role:
          $ref: '#/components/schemas/Role'
    Check:
      type: object
      required:
        - status
      properties:
        status:
          type: string
          enum:
            - pass
            - fail
            - missing
          description: '`missing` is a check that could not run. It is not a pass.'
        reason:
          $ref: '#/components/schemas/RejectionReason'
        detail:
          type: string
    PriceCheck:
      type: object
      required:
        - status
      properties:
        status:
          type: string
          enum:
            - pass
            - fail
            - missing
        reason:
          $ref: '#/components/schemas/RejectionReason'
        detail:
          type: string
        band:
          type: object
          description: >-
            The band the price was judged against, for the token the request
            priced.
          required:
            - mark
            - lower
            - upper
          properties:
            mark:
              type: string
            lower:
              type: string
            upper:
              type: string
    GuardrailCheck:
      type: object
      required:
        - id
        - status
      properties:
        id:
          type: string
          enum:
            - taker_notional
            - price_deviation
            - transaction_notional
            - counterparty_notional
          description: >
            `taker_notional`: the taker's own collateral leg is below the
            minimum trade size.

            `price_deviation`: a leg's price is too far from its token's CLOB
            midpoint.

            `transaction_notional`: the trade is above the maximum trade size.

            `counterparty_notional`: a wallet, or the partner, would pass its
            trading volume limit.
        status:
          type: string
          enum:
            - pass
            - fail
            - missing
        reason:
          $ref: '#/components/schemas/RejectionReason'
        detail:
          type: string
        party:
          type: string
          description: The side the verdict is about, when it is about one.
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
