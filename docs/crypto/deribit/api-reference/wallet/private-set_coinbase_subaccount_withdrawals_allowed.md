---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-set_coinbase_subaccount_withdrawals_allowed
api_type: JSON-RPC
updated_at: 2026-11-27 19:01:01.219171
---

# private/set_coinbase_subaccount_withdrawals_allowed

> Allows or disallows withdrawals from subaccounts. Can be called only by the main account; subaccounts receive a `forbidden` error. The setting applies to Coinbase wallet type withdrawals — when disabled, `private/withdraw` requests from subaccounts of a Coinbase wallet type account are rejected.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fset_coinbase_subaccount_withdrawals_allowed)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/set_coinbase_subaccount_withdrawals_allowed
openapi: 3.0.0
info:
  title: Deribit API
  version: 2.1.1
servers:
  - url: https://test.deribit.com/api/v2
security: []
tags:
  - name: WebSocket Only
    description: Can only be used over websockets.
  - name: Public
    description: Public methods can be used without authentication.
  - name: Private
    description: >-
      <p>Private methods require authentication. All requests must include a
      valid OAuth2 token.</p>

      <p>A token can be requested using the <a
      href="#public-auth">/public/auth</a> method.</p>

      <p>When using the websockets protocol, the token must be included as a
      parameter <code>access_token</code> in the message. When using REST (HTTP
      GET), the token may also be passed in the <code>Authorization</code>
      header.</p>
  - name: Authentication
  - name: Session Management
  - name: Subscription Management
    description: >-
      Subscription works as [notifications](#notifications), so users will
      automatically (after subscribing) receive messages from the server.
      Overview for each channel response format is described in
      [subscriptions](#subscriptions) section.
  - name: Account Management
  - name: Trading
  - name: Market Data
  - name: Wallet
  - name: Chat
  - name: lsp
    description: >-
      Methods and notifications for the Liquidity Support Program (LSP), the
      mechanism that assigns risk from liquidated positions to designated LSP
      participant subaccounts before falling back to auto-deleveraging (ADL).
paths:
  /private/set_coinbase_subaccount_withdrawals_allowed:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Allows or disallows withdrawals from subaccounts. Can be called only by
        the main account; subaccounts receive a `forbidden` error. The setting
        applies to Coinbase wallet type withdrawals — when disabled,
        `private/withdraw` requests from subaccounts of a Coinbase wallet type
        account are rejected.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fset_coinbase_subaccount_withdrawals_allowed)

      parameters:
        - name: enabled
          in: query
          required: true
          schema:
            type: boolean
            example: true
          description: If `true`, subaccounts of the account are allowed to withdraw
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 42
                  method: private/set_coinbase_subaccount_withdrawals_allowed
                  params:
                    enabled: true
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/PrivateSetCoinbaseSubaccountWithdrawalsAllowedResponse
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 42
                    result:
                      enabled: true
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/set_coinbase_subaccount_withdrawals_allowed \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 42,
              "method": "private/set_coinbase_subaccount_withdrawals_allowed",
              "params": {
                "enabled": true
              }
            }'
components:
  schemas:
    PrivateSetCoinbaseSubaccountWithdrawalsAllowedResponse:
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
          type: object
          properties:
            enabled:
              type: boolean
              example: true
              description: Whether subaccount withdrawals are allowed
          required:
            - enabled
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [private/withdraw](https://docs.deribit.com/api-reference/wallet/private-withdraw.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [private/set_self_trading_config](https://docs.deribit.com/api-reference/account-management/private-set_self_trading_config.md)
- [private/set_address_requires_security_key](https://docs.deribit.com/api-reference/wallet/private-set_address_requires_security_key.md)