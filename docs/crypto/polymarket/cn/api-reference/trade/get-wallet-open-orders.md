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
source_url: 'https://docs.polymarket.com/cn/api-reference/trade/get-wallet-open-orders'
updated_at: 2026-11-13
---

# 获取钱包未完成订单

> Lists every live order on the caller's deposit wallet, regardless of which signer or API key placed it.
Authenticate with L2 headers or `POLY_READONLY_API_KEY` and `POLY_ADDRESS`.
`POLY_ADDRESS` must be the wallet owner or one of its non-revoked session signers.

Results are newest first, in pages of about 500. A page can be short or empty while
`next_cursor` is still set. Keep paging with `cursor` until `next_cursor` is empty.

A deposit wallet supports at most 15 non-revoked session signers. Expired signers
count toward this limit; revoke them to free a slot. Authorizing or revoking a signer
can take up to about 5 seconds to appear in this endpoint and wallet-wide cancellation.
Revoking a signer immediately triggers cancellation of all its open orders by the relayer;
those orders no longer appear here after cancellation.




## OpenAPI

````yaml api-spec/clob-openapi.yaml GET /data/wallet-open-orders
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
  /data/wallet-open-orders:
    get:
      tags:
        - Trade
      summary: Get wallet open orders
      description: >
        Lists every live order on the caller's deposit wallet, regardless of
        which signer or API key placed it.

        Authenticate with L2 headers or `POLY_READONLY_API_KEY` and
        `POLY_ADDRESS`.

        `POLY_ADDRESS` must be the wallet owner or one of its non-revoked
        session signers.


        Results are newest first, in pages of about 500. A page can be short or
        empty while

        `next_cursor` is still set. Keep paging with `cursor` until
        `next_cursor` is empty.


        A deposit wallet supports at most 15 non-revoked session signers.
        Expired signers

        count toward this limit; revoke them to free a slot. Authorizing or
        revoking a signer

        can take up to about 5 seconds to appear in this endpoint and
        wallet-wide cancellation.

        Revoking a signer immediately triggers cancellation of all its open
        orders by the relayer;

        those orders no longer appear here after cancellation.
      operationId: getWalletOpenOrders
      parameters:
        - name: market
          in: query
          description: Exact-match filter on the condition ID
          schema:
            type: string
        - name: asset_id
          in: query
          description: Exact-match filter on the token ID
          schema:
            type: string
        - name: session_keys
          in: query
          description: >
            Filter to orders placed by these signer addresses (maximum 50).

            Accepts comma-separated or repeated values. Addresses outside the
            wallet match nothing.
          style: form
          explode: true
          schema:
            type: array
            maxItems: 50
            items:
              type: string
              pattern: ^0x[a-fA-F0-9]{40}$
        - name: cursor
          in: query
          description: The next_cursor returned by the previous page
          schema:
            type: string
      responses:
        '200':
          description: Wallet open orders, newest first
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WalletOpenOrdersResponse'
        '400':
          description: >-
            Invalid POLY_ADDRESS, cursor or session_keys, or the signer belongs
            to more than one wallet
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
          description: The caller has no deposit wallet or is not a signer of it
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: >-
            The selected signers hold more than 50 API keys; narrow the request
            with session_keys
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '503':
          description: A dependency is unavailable or timed out; safe to retry
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
        - polyReadonlyApiKey: []
          polyAddress: []
components:
  schemas:
    WalletOpenOrdersResponse:
      type: object
      required:
        - data
        - next_cursor
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/WalletOpenOrder'
        next_cursor:
          type: string
          description: >-
            Pass as cursor on the next request. Keep paging until empty, even if
            data is empty.
          example: ''
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
    WalletOpenOrder:
      type: object
      required:
        - id
        - status
        - signer_address
        - maker_address
        - market
        - asset_id
        - side
        - original_size
        - size_matched
        - price
        - expiration
        - order_type
        - created_at
        - outcome
      properties:
        id:
          type: string
          description: Order ID (order hash)
          example: '0xabcdef1234567890abcdef1234567890abcdef12'
        status:
          type: string
          description: Order status
          enum:
            - LIVE
        owner:
          type: string
          description: API key, only filled in for orders placed with the caller's own key
          example: f4f247b7-4ac7-ff29-a152-04fda0a8755a
        signer_address:
          type: string
          description: >-
            EOA whose key placed the order, either the wallet owner or a session
            signer
          example: '0x1234567890123456789012345678901234567890'
        maker_address:
          type: string
          description: Ethereum address of the maker
          example: '0x1234567890123456789012345678901234567890'
        market:
          type: string
          description: Market (condition ID)
          example: '0x0000000000000000000000000000000000000000000000000000000000000001'
        asset_id:
          type: string
          description: Asset ID (token ID)
          example: 0xabc123def456...
        side:
          type: string
          description: Order side
          enum:
            - BUY
            - SELL
          example: BUY
        original_size:
          type: string
          description: Original order size
          example: '10'
        size_matched:
          type: string
          description: Size that has been matched
          example: '5'
        price:
          type: string
          description: Order price
          example: '0.5'
        outcome:
          type: string
          description: Market outcome (YES/NO)
          example: 'YES'
        expiration:
          type: string
          description: Unix timestamp when the order expires
          example: '1735689600'
        order_type:
          type: string
          description: Order type
          enum:
            - GTC
            - FOK
            - GTD
            - FAK
          example: GTC
        created_at:
          type: integer
          description: Unix timestamp when the order was created
          example: 1700000000
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
    polyReadonlyApiKey:
      type: apiKey
      in: header
      name: POLY_READONLY_API_KEY
      description: Read-only API key for wallet open orders; also requires POLY_ADDRESS

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
