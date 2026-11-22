---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-get_ctn_id
api_type: JSON-RPC
updated_at: 2026-11-22 18:59:30.711035
---

# private/get_ctn_id

> Returns the Coinbase Transfer Network (CTN) ID of the account. Share this ID with a sending party so they can add the account as a CTN counterparty and send funds to it.

**Coinbase wallet type only.** The method is available to institutional Coinbase accounts and takes no parameters. Other accounts receive an error.

**Scope:** `wallet:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_ctn_id)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_ctn_id
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
  /private/get_ctn_id:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Returns the Coinbase Transfer Network (CTN) ID of the account. Share
        this ID with a sending party so they can add the account as a CTN
        counterparty and send funds to it.


        **Coinbase wallet type only.** The method is available to institutional
        Coinbase accounts and takes no parameters. Other accounts receive an
        error.


        **Scope:** `wallet:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_ctn_id)

      parameters: []
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 4721
                  method: private/get_ctn_id
                  params: {}
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetCtnIdResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 4721
                    result:
                      ctn_id: 6a1f2c3d-4b5e-4f60-8a71-9b0c1d2e3f40
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_ctn_id \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 4721,
              "method": "private/get_ctn_id",
              "params": {}
            }'
components:
  schemas:
    PrivateGetCtnIdResponse:
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
            ctn_id:
              type: string
              example: 6a1f2c3d-4b5e-4f60-8a71-9b0c1d2e3f40
              description: Coinbase Transfer Network (CTN) ID of the account
          required:
            - ctn_id
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [private/withdraw](https://docs.deribit.com/api-reference/wallet/private-withdraw.md)
- [private/get_address_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book.md)
- [private/get_current_deposit_address](https://docs.deribit.com/api-reference/wallet/private-get_current_deposit_address.md)
- [private/get_members](https://docs.deribit.com/api-reference/account-management/private-get_members.md)
- [private/get_deposits](https://docs.deribit.com/api-reference/wallet/private-get_deposits.md)