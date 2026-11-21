---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-set_email_for_subaccount
api_type: JSON-RPC
updated_at: 2026-11-21 19:01:40.028578
---

# private/set_email_for_subaccount

> Assigns an email address to a subaccount. This email is used for direct login to the subaccount and for receiving notifications.

**Behavior:**
- Normally the address is not applied immediately: a verification email with a confirmation link is sent to it, and it can be used for login only after it is confirmed.
- Two changes are applied immediately, without a verification email: setting the main account's own email (the subaccount returns to the main email and its direct login is disabled), and setting the subaccount's current confirmed email while another change is pending (the pending change is cancelled).
- Every successful change terminates all active sessions of the subaccount.
- An address that is already registered to another account does not produce an error: the call returns `ok` without revealing whether the address exists, and the address is not assigned.
- An address already used by another subaccount of the same main account returns `-32602` (`Invalid params`) with `data.subaccount_id` of that subaccount.

**Access & Restrictions:**
- Must be called by the main account that owns the subaccount (`sid`). Any other account is rejected with `13009` (`unauthorized`); a removed subaccount returns `13009` with `data.reason` = `already_removed`. Vault subaccounts are rejected with `14049`.
- Also rejected for accounts without subaccount management (`13009`), retail brokers (`14021`) and locked accounts (`11098`).

**Validation & Limits:**
- Maximum email length is 64 characters; a longer address returns `-32602` with `max_length`.
- `11043` (`bad_argument`) with `data` = `email_wrong_format`, `email_blocked`, `empty_email_address`, `invalid_email_domain` or `same_email` (the address equals the current email and no change is pending).
- Changes are rate limited per subaccount: `10028` (`too_many_requests`) with the time to wait in `data.wait` (seconds).

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
        Assigns an email address to a subaccount. This email is used for direct
        login to the subaccount and for receiving notifications.


        **Behavior:**

        - Normally the address is not applied immediately: a verification email
        with a confirmation link is sent to it, and it can be used for login
        only after it is confirmed.

        - Two changes are applied immediately, without a verification email:
        setting the main account's own email (the subaccount returns to the main
        email and its direct login is disabled), and setting the subaccount's
        current confirmed email while another change is pending (the pending
        change is cancelled).

        - Every successful change terminates all active sessions of the
        subaccount.

        - An address that is already registered to another account does not
        produce an error: the call returns `ok` without revealing whether the
        address exists, and the address is not assigned.

        - An address already used by another subaccount of the same main account
        returns `-32602` (`Invalid params`) with `data.subaccount_id` of that
        subaccount.


        **Access & Restrictions:**

        - Must be called by the main account that owns the subaccount (`sid`).
        Any other account is rejected with `13009` (`unauthorized`); a removed
        subaccount returns `13009` with `data.reason` = `already_removed`. Vault
        subaccounts are rejected with `14049`.

        - Also rejected for accounts without subaccount management (`13009`),
        retail brokers (`14021`) and locked accounts (`11098`).


        **Validation & Limits:**

        - Maximum email length is 64 characters; a longer address returns
        `-32602` with `max_length`.

        - `11043` (`bad_argument`) with `data` = `email_wrong_format`,
        `email_blocked`, `empty_email_address`, `invalid_email_domain` or
        `same_email` (the address equals the current email and no change is
        pending).

        - Changes are rate limited per subaccount: `10028` (`too_many_requests`)
        with the time to wait in `data.wait` (seconds).


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
          description: >-
            The user id of the subaccount (must belong to the authenticated main
            account)
        - name: email
          in: query
          schema:
            type: string
            example: user_1_1@email.com
          required: true
          description: The new email address for the subaccount, up to 64 characters
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
- [private/create_subaccount](https://docs.deribit.com/api-reference/account-management/private-create_subaccount.md)