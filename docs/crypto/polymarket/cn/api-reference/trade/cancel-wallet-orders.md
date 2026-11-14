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
source_url: 'https://docs.polymarket.com/cn/api-reference/trade/cancel-wallet-orders'
updated_at: 2026-11-13
---

# 取消钱包订单

> Cancels orders on the deposit wallet across all API keys, including orders from expired session signers.
Also served at `/v1/gateway/cancel-wallet-orders`.

Only the wallet owner can call this endpoint. Send L2 headers with `POLY_ADDRESS`
set to the owner EOA and the owner's API key. Session signers receive 403 and must use
`DELETE /order`, `DELETE /orders` or `DELETE /cancel-all`, which only cancel orders
placed with their own API key.

Set exactly one of `order_ids` or `all`. Unknown orders, orders from another maker,
and already canceled orders are returned in `not_canceled` with the reason
`order not found on the caller's deposit wallet`.

Shares the cancel rate-limit bucket with `DELETE /orders` and `DELETE /cancel-all`.
With `order_ids`, each ID costs one token up front. With `all`, the request costs
one token up front and is then charged for the number of orders actually canceled.

Revoking a session signer immediately triggers the relayer to cancel its open orders.
After cancellation, canceling those IDs returns them in `not_canceled`.
Authorization and revocation changes can take up to about 5 seconds to appear here.

Production rollout: this route currently returns an nginx 404 page until load-balancer
routing is enabled. The production feature flag must also be enabled. A disabled
application endpoint returns a JSON 404 response instead.




## OpenAPI

````yaml api-spec/clob-openapi.yaml DELETE /cancel-wallet-orders
openapi: 3.1.0
info:
  title: Polymarket CLOB API
  description: Polymarket CLOB API Reference
  license:
    name: MIT
    identifier: MIT
  version: 1.0.0
servers:
  - url: https://clob.polymarket.com
    description: Production CLOB API
  - url: https://clob-staging.polymarket.com
    description: Staging CLOB API
security: []
tags:
  - name: Trade
    description: Trade endpoints
  - name: Markets
    description: Market data endpoints
  - name: Account
    description: Account and authentication endpoints
  - name: Notifications
    description: User notification endpoints
  - name: Rewards
    description: Rewards and earnings endpoints
  - name: Rebates
    description: Maker rebate endpoints
paths:
  /cancel-wallet-orders:
    delete:
      tags:
        - Trade
      summary: Cancel wallet orders
      description: >
        Cancels orders on the deposit wallet across all API keys, including
        orders from expired session signers.

        Also served at `/v1/gateway/cancel-wallet-orders`.


        Only the wallet owner can call this endpoint. Send L2 headers with
        `POLY_ADDRESS`

        set to the owner EOA and the owner's API key. Session signers receive
        403 and must use

        `DELETE /order`, `DELETE /orders` or `DELETE /cancel-all`, which only
        cancel orders

        placed with their own API key.


        Set exactly one of `order_ids` or `all`. Unknown orders, orders from
        another maker,

        and already canceled orders are returned in `not_canceled` with the
        reason

        `order not found on the caller's deposit wallet`.


        Shares the cancel rate-limit bucket with `DELETE /orders` and `DELETE
        /cancel-all`.

        With `order_ids`, each ID costs one token up front. With `all`, the
        request costs

        one token up front and is then charged for the number of orders actually
        canceled.


        Revoking a session signer immediately triggers the relayer to cancel its
        open orders.

        After cancellation, canceling those IDs returns them in `not_canceled`.

        Authorization and revocation changes can take up to about 5 seconds to
        appear here.


        Production rollout: this route currently returns an nginx 404 page until
        load-balancer

        routing is enabled. The production feature flag must also be enabled. A
        disabled

        application endpoint returns a JSON 404 response instead.
      operationId: cancelWalletOrders
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CancelWalletOrdersPayload'
            examples:
              by_id:
                value:
                  order_ids:
                    - >-
                      0xabababababababababababababababababababababababababababababababab
              all_orders:
                value:
                  all: true
      responses:
        '200':
          description: Wallet cancellation results
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CancelOrdersResponse'
              example:
                canceled:
                  - >-
                    0xabababababababababababababababababababababababababababababababab
                not_canceled:
                  '0x0000000000000000000000000000000000000000000000000000000000000000': order not found on the caller's deposit wallet
        '400':
          description: >-
            Both or neither of order_ids/all set, more than 1000 IDs, or an
            invalid order ID
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Authentication failed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: >-
            The address does not own a deposit wallet; session signers also
            receive this response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: >-
            Endpoint disabled in this environment, or production load-balancer
            routing not yet enabled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: not found
            text/html:
              schema:
                type: string
              example: <html><body><h1>404 Not Found</h1></body></html>
        '429':
          description: Cancel rate limit exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '503':
          description: Deposit-wallet lookup failed; retry
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - polyApiKey: []
          polyAddress: []
          polySignature: []
          polyPassphrase: []
          polyTimestamp: []
components:
  schemas:
    CancelWalletOrdersPayload:
      description: Set exactly one field. The server deduplicates order_ids.
      oneOf:
        - type: object
          additionalProperties: false
          required:
            - order_ids
          properties:
            order_ids:
              type: array
              maxItems: 1000
              items:
                type: string
                pattern: ^0x[a-fA-F0-9]{64}$
        - type: object
          additionalProperties: false
          required:
            - all
          properties:
            all:
              type: boolean
              const: true
              description: Cancel every order resting on the wallet
    CancelOrdersResponse:
      type: object
      required:
        - canceled
        - not_canceled
      properties:
        canceled:
          type: array
          description: Array of order IDs that were successfully canceled
          items:
            type: string
          example:
            - '0xabcdef1234567890abcdef1234567890abcdef12'
        not_canceled:
          type: object
          description: Map of order IDs that could not be canceled with error messages
          additionalProperties:
            type: string
          example:
            '0xabcdef1234567890abcdef1234567890abcdef12': Order not found or already canceled
    ErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Machine-readable error code, when provided
        retry_after_seconds:
          type: integer
          description: Number of seconds to wait before retrying, when provided
  securitySchemes:
    polyApiKey:
      type: apiKey
      in: header
      name: POLY_API_KEY
      description: Your API key
    polyAddress:
      type: apiKey
      in: header
      name: POLY_ADDRESS
      description: Ethereum address associated with the API key
    polySignature:
      type: apiKey
      in: header
      name: POLY_SIGNATURE
      description: HMAC signature of the request
    polyPassphrase:
      type: apiKey
      in: header
      name: POLY_PASSPHRASE
      description: API key passphrase
    polyTimestamp:
      type: apiKey
      in: header
      name: POLY_TIMESTAMP
      description: Unix timestamp of the request

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
