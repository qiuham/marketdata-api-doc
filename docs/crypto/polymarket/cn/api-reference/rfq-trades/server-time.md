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
source_url: 'https://docs.polymarket.com/cn/api-reference/rfq-trades/server-time'
updated_at: 2026-11-13
---

# 获取服务器时间

> 读取用于校验请求时间戳的服务器时钟。无需身份验证。

完整的交易流程请参阅 [RFQ 交易合作伙伴 API 指南](https://docs.polymarket.com/partners/rfq-trades.md)。


## OpenAPI

````yaml api-spec/rfq-partner-openapi.yaml GET /v1/time
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
  /v1/time:
    get:
      tags:
        - Status
      summary: Get the server clock
      description: >-
        Public, so a partner whose clock has drifted can still read the time it
        is judged against.
      operationId: getServerTime
      responses:
        '200':
          description: The server's current time.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServerTime'
      security: []
components:
  schemas:
    ServerTime:
      type: object
      required:
        - serverTime
        - timestamp
      properties:
        serverTime:
          type: string
          format: date-time
        timestamp:
          type: integer
          format: int64
          description: The same instant in Unix seconds, ready to use as `RFQ-Timestamp`.
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
