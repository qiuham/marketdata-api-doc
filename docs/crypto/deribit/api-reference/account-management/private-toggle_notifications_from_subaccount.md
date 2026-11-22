---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-toggle_notifications_from_subaccount
api_type: JSON-RPC
updated_at: 2026-11-22 18:59:26.919257
---

# private/toggle_notifications_from_subaccount

> Saves a subaccount's preference for forwarding copies of its notification emails to the main account's email address. It does not stop the subaccount from receiving its own emails.

When forwarding is active, forwarded copies exclude the registration welcome email and mask activation and password-change links. Their title is `Notification for subaccount: <name> - <original title>`.

**Known limitation:** changing this setting currently has no effect on forwarding, and `receive_notifications` (returned by `private/get_subaccounts`, `private/create_subaccount`, and by `private/get_account_summary` / `private/get_account_summaries` with `extended` = `true`) does not reflect it. A successful response only confirms that the request was accepted.

**Access & Restrictions:**
- Must be called by the main account that owns the subaccount (`sid`). The target must be an owned subaccount, not the main account itself. An invalid target is rejected with `13009` (`unauthorized`); a removed subaccount returns `13009` with `data.reason` = `already_removed`. Vault subaccounts are rejected with `14049`.
- Also rejected for accounts without subaccount management (`13009`) and locked accounts (`11098`).
- Send `state` as a JSON boolean. Do not rely on rejection of other types: the current implementation may coerce them to a boolean.

**[TFA required](https://docs.deribit.com/articles/security-keys)**

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Ftoggle_notifications_from_subaccount)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/toggle_notifications_from_subaccount
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
  /private/toggle_notifications_from_subaccount:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Saves a subaccount's preference for forwarding copies of its
        notification emails to the main account's email address. It does not
        stop the subaccount from receiving its own emails.


        When forwarding is active, forwarded copies exclude the registration
        welcome email and mask activation and password-change links. Their title
        is `Notification for subaccount: <name> - <original title>`.


        **Known limitation:** changing this setting currently has no effect on
        forwarding, and `receive_notifications` (returned by
        `private/get_subaccounts`, `private/create_subaccount`, and by
        `private/get_account_summary` / `private/get_account_summaries` with
        `extended` = `true`) does not reflect it. A successful response only
        confirms that the request was accepted.


        **Access & Restrictions:**

        - Must be called by the main account that owns the subaccount (`sid`).
        The target must be an owned subaccount, not the main account itself. An
        invalid target is rejected with `13009` (`unauthorized`); a removed
        subaccount returns `13009` with `data.reason` = `already_removed`. Vault
        subaccounts are rejected with `14049`.

        - Also rejected for accounts without subaccount management (`13009`) and
        locked accounts (`11098`).

        - Send `state` as a JSON boolean. Do not rely on rejection of other
        types: the current implementation may coerce them to a boolean.


        **[TFA required](https://docs.deribit.com/articles/security-keys)**


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Ftoggle_notifications_from_subaccount)

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
            type: boolean
            example: true
          required: true
          description: >-
            Forwarding preference: `true` to request copies at the main account
            email, `false` to request no copies. Currently has no effect; see
            the known limitation above
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 9995
                  method: private/toggle_notifications_from_subaccount
                  params:
                    sid: 7
                    state: true
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
                    id: 9995
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/toggle_notifications_from_subaccount \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 9995,
              "method": "private/toggle_notifications_from_subaccount",
              "params": {
                "sid": 7,
                "state": true
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
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/create_subaccount](https://docs.deribit.com/api-reference/account-management/private-create_subaccount.md)
- [private/get_account_summaries](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries.md)
- [private/get_account_summary](https://docs.deribit.com/api-reference/account-management/private-get_account_summary.md)