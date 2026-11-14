---
api_type: spec
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-spec/rfq-partner-openapi.yaml'
updated_at: 2026-11-13
---

# rfq-partner-openapi.yaml

Source: https://docs.polymarket.com/api-spec/rfq-partner-openapi.yaml

```yaml
openapi: 3.0.3
info:
  title: Polymarket RFQ Trades — Partner API
  version: 1.0.0
  description: |
    Trades two counterparties agreed through an RFQ, settled on Polymarket's CTF Exchange as one
    matched pair of orders. A partner pre-flights the agreed terms (`validate`), has the service
    build both orders (`prepare`), collects each side's signature, submits the signed pair, and
    follows the trade by polling or over the WebSocket stream (`asyncapi.yaml`).

    ## Authentication

    Every request except `/v1/time`, `/health` and `/ready` carries three headers:

    - `RFQ-Key-Id`: the public half of the partner's API key.
    - `RFQ-Timestamp`: Unix seconds. It must be within 30 seconds of server time either way;
      `GET /v1/time` returns the server clock.
    - `RFQ-Signature`: `base64url(HMAC-SHA256(secret, timestamp + method + path + body))`, padded
      (RFC 4648 §5), where `method` is uppercase, `path` is the URL path without the query string,
      and `body` is the exact bytes sent (empty for a `GET`).

    The partner is resolved from the key, never from the body. Another partner's trade is a `404`.

    ## Conventions

    - Amounts (`shares`, `makerAmount`, `takerAmount`, fees) are base-10 integer strings in 6-decimal
      units: `"1000000"` is one share or one pUSD. Prices and tolerances are decimal strings.
    - Request bodies are decoded strictly: an unknown field is a `400`.
    - Every error uses the `Error` envelope. `details.reason` is the machine-readable rejection, and
      new reasons may be added: treat an unknown one as a rejection.
    - Fees are set by the service and returned by `prepare`. A submission never quotes its own.
servers:
  - url: https://external-rfq-partner.polymarket.com
    description: Production
tags:
  - name: RFQ trades
  - name: Markets
  - name: Status
security:
  - RfqKeyId: []
    RfqTimestamp: []
    RfqSignature: []
paths:
  /v1/rfq-trades/validate:
    post:
      tags: [RFQ trades]
      operationId: validateRfqTrade
      summary: Pre-flight proposed terms
      description: |
        Runs every check a submission of these terms would run and reports them all. Advisory:
        nothing is stored, and the same checks run again at submission. A completed validation is
        always a `200`; a failed check is a verdict in the body, not an error status.
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
  /v1/rfq-trades/prepare:
    post:
      tags: [RFQ trades]
      operationId: prepareRfqTrade
      summary: Build both orders to sign
      description: |
        Expands the agreed terms into both unsigned orders, with fresh salts and timestamps, and
        returns each side's signing payload and the fee it will be charged. Stateless: submit the
        orders unchanged, each with its signature, to `POST /v1/rfq-trades`.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PrepareRequest'
      responses:
        '200':
          description: Both orders, keyed like the request's `parties`.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrepareResult'
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
  /v1/rfq-trades:
    post:
      tags: [RFQ trades]
      operationId: submitRfqTrade
      summary: Submit a signed RFQ trade
      description: |
        Submits both signed orders. The trade is accepted as `PENDING` and executes asynchronously.
        `idempotencyKey` is the partner's own trade reference: a repeat of a known key returns the
        original trade, with its current status, and sets `Idempotency-Replayed: true`.
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
              description: '`true` when the response replays an earlier submission of the same key.'
              schema:
                type: string
                enum: ['true']
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
  /v1/rfq-trades/{tradeId}:
    get:
      tags: [RFQ trades]
      operationId: getRfqTrade
      summary: Get a trade's status
      description: The source of truth for a trade's outcome, and the reconciliation path for the stream.
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
  /v1/markets/{marketId}/price-band:
    get:
      tags: [Markets]
      operationId: getMarketPriceBand
      summary: Get a market's price band
      description: |
        The window around each outcome token's CLOB midpoint that an RFQ trade's price must fall
        inside, at the default tolerance. A submission can tighten it with `priceTolerance`.
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
  /v1/ws/rfq-trades:
    get:
      tags: [RFQ trades]
      operationId: streamRfqTrades
      summary: Open the trade status stream
      description: |
        Upgrades to a WebSocket that sends a snapshot of the partner's in-flight trades, then each
        status change. The upgrade request is signed like any `GET` (empty body). Messages are
        described in `asyncapi.yaml`. Delivery is lossy by design: `GET /v1/rfq-trades/{tradeId}`
        is the source of truth. The server pings every 45 seconds and closes a connection that has
        not answered within 60.
      responses:
        '101':
          description: Switched to the WebSocket protocol.
        '401':
          $ref: '#/components/responses/Unauthorized'
        '503':
          description: The stream is not enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /v1/time:
    get:
      tags: [Status]
      operationId: getServerTime
      summary: Get the server clock
      description: Public, so a partner whose clock has drifted can still read the time it is judged against.
      security: []
      responses:
        '200':
          description: The server's current time.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServerTime'
  /health:
    get:
      tags: [Status]
      operationId: getHealth
      summary: Liveness probe
      security: []
      responses:
        '200':
          description: The service is up.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Probe'
  /ready:
    get:
      tags: [Status]
      operationId: getReady
      summary: Readiness probe
      security: []
      responses:
        '200':
          description: The service is ready.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Probe'
components:
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
      description: base64url(HMAC-SHA256(secret, timestamp + method + path + body)), padded.
  responses:
    BadRequest:
      description: A malformed body, an unknown field, or a malformed path parameter.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    Unauthorized:
      description: Missing or invalid authentication headers, or a timestamp outside the window.
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
      description: A dependency failed. Retry when `retryable` is true, with the same `idempotencyKey` for a submission.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
  schemas:
    Address:
      type: string
      pattern: '^0x[0-9a-fA-F]{40}$'
      example: '0x4444444444444444444444444444444444444444'
    Amount:
      type: string
      pattern: '^[0-9]+$'
      description: A base-10 integer in 6-decimal units.
      example: '65000000'
    Uint256:
      type: string
      pattern: '^[0-9]+$'
      description: A base-10 uint256.
    Role:
      type: string
      enum: [maker, taker]
      description: |
        Which fee rate a side pays. Set it on both sides or on neither; omitted, the `yes` side of a
        split or merge and the `buyer` of a trade are the taker.
    MarketSource:
      type: string
      enum: [gamma, bespoke, combo]
      default: gamma
      description: '`gamma` for a Polymarket market id, `bespoke` for a bespoke market, `combo` for a market defined by its `legs`.'
    Combination:
      type: string
      enum: [and]
      description: The combo operator. Omitted means `and`.
    ComboLeg:
      type: object
      required: [marketId, outcome]
      properties:
        marketId:
          type: string
          description: A gamma market id.
        outcome:
          type: string
          enum: ['yes', 'no']
    RejectionReason:
      type: string
      description: |
        The machine-readable reason a check failed or a request was rejected. New values may be
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
      required: [error]
      properties:
        error:
          type: object
          required: [code, message, retryable, details]
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
                  description: The side the rejection is attributable to, when there is one.
                field:
                  type: string
                  description: The request field at fault, when there is one, e.g. `orders[0].salt`.
      example:
        error:
          code: validation_failed
          message: 'stale_order (taker): order timestamp is 12m0s old (max 10m0s)'
          retryable: false
          details:
            reason: stale_order
            party: taker
    PrepareParty:
      type: object
      required: [maker, signatureType]
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
          description: The order signature type. `3` (deposit wallet) is the type partner trades use.
          example: 3
        role:
          $ref: '#/components/schemas/Role'
    PrepareRequest:
      type: object
      required: [operation, price, shares, parties]
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
          enum: [split, merge, trade]
          description: |
            `split`: both sides buy, one YES and one NO. `merge`: both sides sell, one YES and one NO.
            `trade`: one side buys an outcome token from the other.
        token:
          type: string
          enum: ['yes', 'no']
          description: The outcome token that changes hands, for `trade` only.
        price:
          type: string
          description: The agreed price in (0, 1). The YES price for a split or merge, the traded token's price for a trade.
          example: '0.65'
        shares:
          $ref: '#/components/schemas/Amount'
        parties:
          type: object
          description: Keyed `yes` and `no` for a split or merge, `buyer` and `seller` for a trade.
          additionalProperties:
            $ref: '#/components/schemas/PrepareParty'
        priceTolerance:
          type: string
          description: Tightens the price band to this fraction of the mark, e.g. `0.05` for ±5%. Wider than the default is refused.
    Check:
      type: object
      required: [status]
      properties:
        status:
          type: string
          enum: [pass, fail, missing]
          description: '`missing` is a check that could not run. It is not a pass.'
        reason:
          $ref: '#/components/schemas/RejectionReason'
        detail:
          type: string
    PriceCheck:
      type: object
      required: [status]
      properties:
        status:
          type: string
          enum: [pass, fail, missing]
        reason:
          $ref: '#/components/schemas/RejectionReason'
        detail:
          type: string
        band:
          type: object
          description: The band the price was judged against, for the token the request priced.
          required: [mark, lower, upper]
          properties:
            mark:
              type: string
            lower:
              type: string
            upper:
              type: string
    GuardrailCheck:
      type: object
      required: [id, status]
      properties:
        id:
          type: string
          enum: [taker_notional, price_deviation, transaction_notional, counterparty_notional]
          description: |
            `taker_notional`: the taker's own collateral leg is below the minimum trade size.
            `price_deviation`: a leg's price is too far from its token's CLOB midpoint.
            `transaction_notional`: the trade is above the maximum trade size.
            `counterparty_notional`: a wallet, or the partner, would pass its trading volume limit.
        status:
          type: string
          enum: [pass, fail, missing]
        reason:
          $ref: '#/components/schemas/RejectionReason'
        detail:
          type: string
        party:
          type: string
          description: The side the verdict is about, when it is about one.
    ValidationResult:
      type: object
      required: [valid, checks, checkedAt]
      properties:
        valid:
          type: boolean
          description: Whether a submission of these terms would be accepted now.
        checks:
          type: object
          required: [market]
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
              description: One entry per guardrail, in the order they run. The first failure is the one a submission returns.
              items:
                $ref: '#/components/schemas/GuardrailCheck'
        checkedAt:
          type: string
          format: date-time
    Order:
      type: object
      description: A CTF Exchange v2 order, in the field order and encoding it is signed in.
      required: [salt, maker, signer, tokenId, makerAmount, takerAmount, side, signatureType, timestamp, metadata, builder]
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
          enum: [0, 1]
          description: '`0` buy, `1` sell.'
        signatureType:
          type: integer
        timestamp:
          type: string
          description: Unix seconds the order was built at.
        metadata:
          type: string
          description: bytes32 hex.
        builder:
          type: string
          description: bytes32 hex. The partner's builder code, set by the service.
    PreparedOrder:
      type: object
      required: [order, typedData, role, digest, signatureSuffix]
      properties:
        order:
          $ref: '#/components/schemas/Order'
        typedData:
          type: object
          additionalProperties: true
          description: The nested ERC-7739 payload to pass to `eth_signTypedData_v4`.
        role:
          $ref: '#/components/schemas/Role'
        digest:
          type: string
          description: The hash the raw ECDSA signature verifies against.
        signatureSuffix:
          type: string
          description: Appended to the raw signature to form the submitted one (`rawSignature || signatureSuffix`).
    PrepareResult:
      type: object
      required: [orders, fees, expiresAt]
      properties:
        orders:
          type: object
          description: Keyed like the request's `parties`.
          additionalProperties:
            $ref: '#/components/schemas/PreparedOrder'
        fees:
          type: object
          description: The fee each side will be charged, keyed like `orders`.
          additionalProperties:
            $ref: '#/components/schemas/Amount'
        expiresAt:
          type: string
          format: date-time
          description: After this, a submission of these orders is refused as stale.
    SignedOrder:
      type: object
      description: An `Order` exactly as prepared, with its signature.
      required: [salt, maker, signer, tokenId, makerAmount, takerAmount, side, signatureType, timestamp, metadata, builder, signature]
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
          enum: [0, 1]
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
    SubmitRequest:
      type: object
      required: [orders, idempotencyKey]
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
          enum: ['0']
          description: Not an input. Omit it; anything but `0` is rejected with `fee_not_accepted`.
        makerFeeAmount:
          type: string
          enum: ['0']
          description: Not an input. Omit it; anything but `0` is rejected with `fee_not_accepted`.
    TradeState:
      type: string
      enum: [PENDING, FILLED, REJECTED]
      description: '`PENDING` until the trade lands on-chain (`FILLED`) or is refused or fails (`REJECTED`).'
    Combo:
      type: object
      description: A combo's on-chain identity. Present on combo trades only.
      required: [conditionId, tokenIdYes, tokenIdNo, legs]
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
    SubmitResult:
      type: object
      required: [tradeId, status, createdAt]
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
    TradeStatus:
      type: object
      required: [tradeId, idempotencyKey, status, createdAt]
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
          description: Why a `REJECTED` trade failed. `execution_failed` is a failure after submission to the exchange.
          anyOf:
            - $ref: '#/components/schemas/RejectionReason'
            - type: string
              enum: [execution_failed]
        createdAt:
          type: string
          format: date-time
        filledAt:
          type: string
          format: date-time
    TradeUpdateFrame:
      type: object
      description: One message on the trade status stream.
      required: [type, trade]
      properties:
        type:
          type: string
          enum: [trade_update]
        trade:
          $ref: '#/components/schemas/TradeStatus'
    OutcomeBand:
      type: object
      required: [tokenId, source]
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
          enum: [clob_midpoint, unavailable]
          description: '`unavailable` when no midpoint could be read; `mark`, `lower` and `upper` are then omitted.'
    PriceBand:
      type: object
      required: [marketId, tolerance, outcomes, readAt]
      properties:
        marketId:
          type: string
        tolerance:
          type: string
          description: The fraction of each mark the band spans.
        outcomes:
          type: object
          required: ['yes', 'no']
          properties:
            'yes':
              $ref: '#/components/schemas/OutcomeBand'
            'no':
              $ref: '#/components/schemas/OutcomeBand'
        readAt:
          type: string
          format: date-time
    ServerTime:
      type: object
      required: [serverTime, timestamp]
      properties:
        serverTime:
          type: string
          format: date-time
        timestamp:
          type: integer
          format: int64
          description: The same instant in Unix seconds, ready to use as `RFQ-Timestamp`.
    Probe:
      type: object
      required: [data]
      properties:
        data:
          type: string
```
