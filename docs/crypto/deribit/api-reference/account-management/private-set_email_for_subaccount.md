---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-set_email_for_subaccount
api_type: JSON-RPC
updated_at: 2026-11-18 18:59:14.672531
---

# private/set_email_for_subaccount

> Assigns an email address to a subaccount. This email can be used for direct login to the subaccount and for receiving notifications.

The email address owner will receive a confirmation email with a link to verify the email address. The email must be confirmed before it can be used for login.

**[TFA required](https://docs.deribit.com/articles/security-keys)**

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fset_email_for_subaccount)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/set_email_for_subaccount
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
  /private/set_email_for_subaccount:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Assigns an email address to a subaccount. This email can be used for
        direct login to the subaccount and for receiving notifications.


        The email address owner will receive a confirmation email with a link to
        verify the email address. The email must be confirmed before it can be
        used for login.


        **[TFA required](https://docs.deribit.com/articles/security-keys)**


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fset_email_for_subaccount)

      parameters:
        - name: sid
          in: query
          schema:
            type: integer
            example: 7
          required: true
          description: The user id for the subaccount
        - name: email
          in: query
          schema:
            type: string
            example: user_1_1@email.com
          required: true
          description: The email address for the subaccount
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 1667
                  method: private/set_email_for_subaccount
                  params:
                    sid: 7
                    email: user_1_1@email.com
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OkResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 1667
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/set_email_for_subaccount \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 1667,
              "method": "private/set_email_for_subaccount",
              "params": {
                "sid": 7,
                "email": "user_1_1@email.com"
              }
            }'
components:
  schemas:
    OkResponse:
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
          type: string
          enum:
            - ok
          description: Result of method execution. `ok` in case of success
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api.md)
- [private/set_email_language](https://docs.deribit.com/api-reference/account-management/private-set_email_language.md)
- [private/set_coinbase_subaccount_withdrawals_allowed](https://docs.deribit.com/api-reference/wallet/private-set_coinbase_subaccount_withdrawals_allowed.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/get_account_summaries](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries.md)