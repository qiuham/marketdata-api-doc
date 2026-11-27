---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/portfolio-management/mass-cancel
api_type: JSON-RPC
updated_at: 2026-11-27 19:00:53.391651
---

# Mass Cancel

> Cancels all open orders and quotes belonging to the authenticated portfolio. No filter parameters are accepted. The cancel applies to every instrument and every side.


## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/private/cancel_all
openapi: 3.0.3
info:
  title: Starbase REST API
  version: '2.0'
  description: Portfolio-scoped REST API for the Starbase direct-access trading platform.
servers:
  - url: http://195.138.37.5:4410
    description: Production (Gateway A, rest-order)
  - url: http://195.138.37.6:4410
    description: Production (Gateway B, rest-order)
  - url: http://195.138.37.137:4410
    description: Test (Gateway A, rest-order)
  - url: http://195.138.37.138:4410
    description: Test (Gateway B, rest-order)
security: []
tags:
  - name: Portfolio Management
    description: Endpoints that operate on the authenticated portfolio.
  - name: Trading
    description: Authenticated trading endpoints scoped to the caller's portfolio.
  - name: Market Data
    description: >-
      Unauthenticated Starbase reference and market data endpoints. No API
      credentials are required, but the Starbase REST gateway is reachable only
      through private Starbase connectivity.
paths:
  /api/v2/private/cancel_all:
    get:
      tags:
        - Portfolio Management
      summary: Mass Cancel
      description: >-
        Cancels all open orders and quotes belonging to the authenticated
        portfolio. No filter parameters are accepted. The cancel applies to
        every instrument and every side.
      operationId: cancel_all
      responses:
        '200':
          description: All open orders and quotes cancelled successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CancelAllResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result: 42
        '429':
          description: >-
            Per-portfolio rate limit for this endpoint exceeded. Default is 1
            request per minute (`portfolio-rate-limit.cancel_all`). The response
            includes `Retry-After` (seconds until the next one-minute window).
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
      security:
        - BearerAuth: []
components:
  schemas:
    CancelAllResponse:
      type: object
      required:
        - jsonrpc
        - result
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          type: number
          example: 7
          description: Total number of successfully cancelled orders
    JsonRpcError:
      type: object
      required:
        - jsonrpc
        - error
      description: JSON-RPC 2.0 error envelope returned for failed requests.
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
        id:
          type: integer
          nullable: true
          description: The id that was sent in the request, if any.
        error:
          type: object
          required:
            - code
            - message
          properties:
            code:
              type: integer
              description: Numeric JSON-RPC error code.
            message:
              type: string
              description: Human-readable error description.
            data:
              description: Optional additional error details.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        API key passed as a Bearer token. The authenticated session determines
        the portfolio that operations are applied to.

````

## Related topics

- [Portfolio Management](https://docs.deribit.com/starbase/portfolio-management.md)
- [Starbase Mass Cancel Messages](https://docs.deribit.com/starbase/mass-cancel.md)
- [Mass Quotes Specifications](https://docs.deribit.com/articles/mass-quotes-specifications.md)
- [Order Mass Cancel Report(r) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-cancel-report.md)
- [Order Mass Cancel Request(q) (Production FIX API)](https://docs.deribit.com/fix-api/production/order-mass-cancel-request.md)