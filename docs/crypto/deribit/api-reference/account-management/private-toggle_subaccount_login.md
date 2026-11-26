---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-toggle_subaccount_login
api_type: JSON-RPC
updated_at: 2026-11-26 19:02:04.631816
---

# private/toggle_subaccount_login

> Enables or disables direct login access for a subaccount. When login is disabled, the subaccount cannot be accessed directly using email and password authentication, but can still be accessed through the main account.

If login is disabled while an active session exists for the subaccount, that session will be immediately terminated (all sessions of the subaccount are dropped). Requesting the state the subaccount already has is accepted and returns `ok`.

**Access & Restrictions:**
- Must be called by the main account that owns the subaccount (`sid`). Any other account is rejected with `13009` (`unauthorized`); a removed subaccount returns `13009` with `data.reason` = `already_removed`.
- Vault subaccounts are rejected with `14049` (`vault_subaccount_not_allowed`).
- Also rejected for accounts without subaccount management (`13009`), retail brokers (`14021`) and locked accounts (`11098`).
- `state` must be `enable` or `disable`; any other value returns `11043` (`bad_argument`) with `data` = `state`.

**Enabling login** additionally requires:
- no email change pending for the subaccount;
- an email address different from the main account's email;
- a password configured for the subaccount.

**Known limitation:** if one of these conditions is not met, the call currently returns `ok` but login stays disabled. Check `login_enabled` in `private/get_subaccounts` to confirm the change.

**[TFA required](https://docs.deribit.com/articles/security-keys)**

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Ftoggle_subaccount_login)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/toggle_subaccount_login
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
  /private/toggle_subaccount_login:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Enables or disables direct login access for a subaccount. When login is
        disabled, the subaccount cannot be accessed directly using email and
        password authentication, but can still be accessed through the main
        account.


        If login is disabled while an active session exists for the subaccount,
        that session will be immediately terminated (all sessions of the
        subaccount are dropped). Requesting the state the subaccount already has
        is accepted and returns `ok`.


        **Access & Restrictions:**

        - Must be called by the main account that owns the subaccount (`sid`).
        Any other account is rejected with `13009` (`unauthorized`); a removed
        subaccount returns `13009` with `data.reason` = `already_removed`.

        - Vault subaccounts are rejected with `14049`
        (`vault_subaccount_not_allowed`).

        - Also rejected for accounts without subaccount management (`13009`),
        retail brokers (`14021`) and locked accounts (`11098`).

        - `state` must be `enable` or `disable`; any other value returns `11043`
        (`bad_argument`) with `data` = `state`.


        **Enabling login** additionally requires:

        - no email change pending for the subaccount;

        - an email address different from the main account's email;

        - a password configured for the subaccount.


        **Known limitation:** if one of these conditions is not met, the call
        currently returns `ok` but login stays disabled. Check `login_enabled`
        in `private/get_subaccounts` to confirm the change.


        **[TFA required](https://docs.deribit.com/articles/security-keys)**


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Ftoggle_subaccount_login)

      parameters:
        - name: sid
          in: query
          schema:
            type: integer
            example: 7
          required: true
          description: >-
            The user id of the subaccount (must belong to the authenticated main
            account)
        - name: state
          in: query
          schema:
            type: string
            enum:
              - enable
              - disable
            example: enable
          required: true
          description: >-
            `enable` or `disable` direct login. Disabling terminates the
            subaccount's active sessions
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 938
                  method: private/toggle_subaccount_login
                  params:
                    sid: 7
                    state: enable
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
                    id: 938
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/toggle_subaccount_login \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 938,
              "method": "private/toggle_subaccount_login",
              "params": {
                "sid": 7,
                "state": "enable"
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
- [private/toggle_notifications_from_subaccount](https://docs.deribit.com/api-reference/account-management/private-toggle_notifications_from_subaccount.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/create_subaccount](https://docs.deribit.com/api-reference/account-management/private-create_subaccount.md)
- [private/set_email_for_subaccount](https://docs.deribit.com/api-reference/account-management/private-set_email_for_subaccount.md)