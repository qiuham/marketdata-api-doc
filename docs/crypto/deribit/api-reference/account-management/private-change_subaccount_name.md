---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-change_subaccount_name
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:42.481061
---

# private/change_subaccount_name

> Changes the display name (alias) of a subaccount, or of the authenticated main account itself (pass the main account's own id as `sid`). The alias is returned as `username` in account responses; the system-generated name (`system_name`), login credentials and account functionality are not affected.

**Access & Restrictions:**
- Requires scope `account:read_write` and `mainaccount`, i.e. a main account token.
- `sid` must be the main account itself or one of its own subaccounts. Any other account is rejected with `13009` (`unauthorized`); a removed subaccount returns `13009` with `data.reason` = `already_removed`.
- Vault subaccounts are rejected with `14049` (`vault_subaccount_not_allowed`).
- Also rejected for accounts without subaccount management (`13009`), retail brokers (`14021`) and locked accounts (`11098`).

**Name rules** (applied after trimming leading and trailing whitespace):
- 5 to 80 characters.
- Only Latin-1 (ISO 8859-1) characters; control characters and the soft hyphen are rejected.
- Must be unique among the main account and its active subaccounts. This includes the target's current name, so re-submitting it fails with `already_taken`.
- Must not match the reserved auto-generated pattern `<main_username>_<number>` (or `<main_username>_vault_<number>`).
- Setting the name to the account's own `system_name` clears a previously set alias.

**Errors:** an invalid name returns `12002` (`wrong_subaccount_name`) with `data` = `already_taken`, `wrong_format` (invalid characters or reserved pattern), or `{"msg": "too_short" | "too_long", "size": <limit>}`. `12002` may also be returned without `data`.

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read_write` and mainaccount

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fchange_subaccount_name)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/change_subaccount_name
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
  /private/change_subaccount_name:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Changes the display name (alias) of a subaccount, or of the
        authenticated main account itself (pass the main account's own id as
        `sid`). The alias is returned as `username` in account responses; the
        system-generated name (`system_name`), login credentials and account
        functionality are not affected.


        **Access & Restrictions:**

        - Requires scope `account:read_write` and `mainaccount`, i.e. a main
        account token.

        - `sid` must be the main account itself or one of its own subaccounts.
        Any other account is rejected with `13009` (`unauthorized`); a removed
        subaccount returns `13009` with `data.reason` = `already_removed`.

        - Vault subaccounts are rejected with `14049`
        (`vault_subaccount_not_allowed`).

        - Also rejected for accounts without subaccount management (`13009`),
        retail brokers (`14021`) and locked accounts (`11098`).


        **Name rules** (applied after trimming leading and trailing whitespace):

        - 5 to 80 characters.

        - Only Latin-1 (ISO 8859-1) characters; control characters and the soft
        hyphen are rejected.

        - Must be unique among the main account and its active subaccounts. This
        includes the target's current name, so re-submitting it fails with
        `already_taken`.

        - Must not match the reserved auto-generated pattern
        `<main_username>_<number>` (or `<main_username>_vault_<number>`).

        - Setting the name to the account's own `system_name` clears a
        previously set alias.


        **Errors:** an invalid name returns `12002` (`wrong_subaccount_name`)
        with `data` = `already_taken`, `wrong_format` (invalid characters or
        reserved pattern), or `{"msg": "too_short" | "too_long", "size":
        <limit>}`. `12002` may also be returned without `data`.


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read_write` and mainaccount


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fchange_subaccount_name)

      parameters:
        - name: sid
          in: query
          schema:
            type: integer
            example: 7
          required: true
          description: >-
            The user id of the subaccount to rename, or the id of the
            authenticated main account to rename the main account itself
        - name: name
          in: query
          schema:
            type: string
            example: new_user_1_1
          required: true
          description: >-
            The new display name, 5-80 characters after trimming whitespace,
            unique within the main account and its subaccounts. See name rules
            above
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 3964
                  method: private/change_subaccount_name
                  params:
                    sid: 7
                    name: new_user_1_1
              main_accountRequest:
                summary: Main account Request
                value:
                  jsonrpc: '2.0'
                  id: 3965
                  method: private/change_subaccount_name
                  params:
                    sid: 2
                    name: main_trading_desk
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
                    id: 3964
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/change_subaccount_name \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 3964,
              "method": "private/change_subaccount_name",
              "params": {
                "sid": 7,
                "name": "new_user_1_1"
              }
            }'
        - lang: bash
          label: cURL (Main account)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/change_subaccount_name \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 3965,
              "method": "private/change_subaccount_name",
              "params": {
                "sid": 2,
                "name": "main_trading_desk"
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
- [private/change_api_key_name](https://docs.deribit.com/api-reference/account-management/private-change_api_key_name.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/toggle_notifications_from_subaccount](https://docs.deribit.com/api-reference/account-management/private-toggle_notifications_from_subaccount.md)
- [private/create_subaccount](https://docs.deribit.com/api-reference/account-management/private-create_subaccount.md)