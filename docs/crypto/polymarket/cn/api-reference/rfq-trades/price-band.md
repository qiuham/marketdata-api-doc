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
source_url: 'https://docs.polymarket.com/cn/api-reference/rfq-trades/price-band'
updated_at: 2026-11-13
---

# 获取市场价格区间

> 读取此市场上 RFQ 交易价格必须落入的价格区间，涵盖两个结果代币。

完整的交易流程请参阅 [RFQ 交易合作伙伴 API 指南](https://docs.polymarket.com/partners/rfq-trades.md)。


## OpenAPI

````yaml api-spec/rfq-partner-openapi.yaml GET /v1/markets/{marketId}/price-band
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
  /v1/markets/{marketId}/price-band:
    get:
      tags:
        - Markets
      summary: Get a market's price band
      description: >
        The window around each outcome token's CLOB midpoint that an RFQ trade's
        price must fall

        inside, at the default tolerance. A submission can tighten it with
        `priceTolerance`.
      operationId: getMarketPriceBand
      parameters:
        - name: marketId
          in: path
          required: true
          description: A gamma market id.
          schema:
            type: string
      responses:
        '200':
          description: The band for each outcome token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PriceBand'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
        '500':
          $ref: '#/components/responses/InternalError'
        '502':
          $ref: '#/components/responses/DependencyUnavailable'
components:
  schemas:
    PriceBand:
      type: object
      required:
        - marketId
        - tolerance
        - outcomes
        - readAt
      properties:
        marketId:
          type: string
        tolerance:
          type: string
          description: The fraction of each mark the band spans.
        outcomes:
          type: object
          required:
            - 'yes'
            - 'no'
          properties:
            'yes':
              $ref: '#/components/schemas/OutcomeBand'
            'no':
              $ref: '#/components/schemas/OutcomeBand'
        readAt:
          type: string
          format: date-time
    OutcomeBand:
      type: object
      required:
        - tokenId
        - source
      properties:
        tokenId:
          $ref: '#/components/schemas/Uint256'
        mark:
          type: string
        lower:
          type: string
        upper:
          type: string
        source:
          type: string
          enum:
            - clob_midpoint
            - unavailable
          description: >-
            `unavailable` when no midpoint could be read; `mark`, `lower` and
            `upper` are then omitted.
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
