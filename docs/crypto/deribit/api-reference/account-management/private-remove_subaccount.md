---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-remove_subaccount
api_type: JSON-RPC
updated_at: 2026-11-25 19:00:47.673597
---

# private/remove_subaccount

> Removes a subaccount from the main account. The subaccount must be empty before it can be removed.

Removal cannot be undone through the API. The subaccount can no longer be used or logged in to, it disappears from `private/get_subaccounts`, all of its active sessions are terminated, and its deposit addresses are moved to the main account.

**Access & Restrictions:**
- Must be called by the main account that owns the subaccount. Any other account is rejected with `13009` (`unauthorized`); an already removed subaccount returns `13009` with `data.reason` = `already_removed`.
- Also rejected for accounts without subaccount management (`13009`), retail brokers (`14021`) and locked accounts (`11098`).
- Vault subaccounts are rejected during access validation with `14049` (`vault_subaccount_not_allowed`).
- Only one subaccount can be removed per main account every 5 minutes. A repeated call earlier returns `12006` (`remove_subaccount_over_limit`) with the remaining time in `data.wait` (seconds).

**Removal is refused with `12007` (`subaccount_not_removable`)**; `data.reason` is one of:
- `"has not zero equity"`: open positions, a position closed since the last daily settlement (08:00 UTC) whose realized profit/loss is not settled yet (the subaccount becomes removable after that settlement), non-zero initial or maintenance margin, or absolute equity or balance at or above the currency's minimum balance (only dust whose absolute value is below the threshold is allowed);
- `"has opened trigger orders"`: untriggered trigger orders;
- `"has pending deposits"`;
- `"is owner of app"`: the subaccount owns an API application;
- `"has active block rfq"` or `"is part of block rfq allocation"`;
- `"is linked to a voice broker"`;
- `"is an LSP participant"`;
- `"has a locked portfolio, reason: <reasons>"`, where `<reasons>` is a comma-separated list such as `liquidation running`, `negative equity`, `locked by admin`, `locked on user request` or `legacy lock`.

Other reason strings may be returned in rare cases.

If the subaccount's portfolio could not be cleaned up or verified, or the change could not be saved, the call fails with `13008` (`request_failed`).

**[TFA required](https://docs.deribit.com/articles/security-keys)**

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fremove_subaccount)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/remove_subaccount
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
  /private/remove_subaccount:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Removes a subaccount from the main account. The subaccount must be empty
        before it can be removed.


        Removal cannot be undone through the API. The subaccount can no longer
        be used or logged in to, it disappears from `private/get_subaccounts`,
        all of its active sessions are terminated, and its deposit addresses are
        moved to the main account.


        **Access & Restrictions:**

        - Must be called by the main account that owns the subaccount. Any other
        account is rejected with `13009` (`unauthorized`); an already removed
        subaccount returns `13009` with `data.reason` = `already_removed`.

        - Also rejected for accounts without subaccount management (`13009`),
        retail brokers (`14021`) and locked accounts (`11098`).

        - Vault subaccounts are rejected during access validation with `14049`
        (`vault_subaccount_not_allowed`).

        - Only one subaccount can be removed per main account every 5 minutes. A
        repeated call earlier returns `12006` (`remove_subaccount_over_limit`)
        with the remaining time in `data.wait` (seconds).


        **Removal is refused with `12007` (`subaccount_not_removable`)**;
        `data.reason` is one of:

        - `"has not zero equity"`: open positions, a position closed since the
        last daily settlement (08:00 UTC) whose realized profit/loss is not
        settled yet (the subaccount becomes removable after that settlement),
        non-zero initial or maintenance margin, or absolute equity or balance at
        or above the currency's minimum balance (only dust whose absolute value
        is below the threshold is allowed);

        - `"has opened trigger orders"`: untriggered trigger orders;

        - `"has pending deposits"`;

        - `"is owner of app"`: the subaccount owns an API application;

        - `"has active block rfq"` or `"is part of block rfq allocation"`;

        - `"is linked to a voice broker"`;

        - `"is an LSP participant"`;

        - `"has a locked portfolio, reason: <reasons>"`, where `<reasons>` is a
        comma-separated list such as `liquidation running`, `negative equity`,
        `locked by admin`, `locked on user request` or `legacy lock`.


        Other reason strings may be returned in rare cases.


        If the subaccount's portfolio could not be cleaned up or verified, or
        the change could not be saved, the call fails with `13008`
        (`request_failed`).


        **[TFA required](https://docs.deribit.com/articles/security-keys)**


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fremove_subaccount)

      parameters:
        - name: subaccount_id
          in: query
          schema:
            type: integer
            minimum: 1
            example: 120
          required: true
          description: >-
            The user id of the subaccount to remove (must belong to the
            authenticated main account)
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 6
                  method: private/remove_subaccount
                  params:
                    subaccount_id: 120
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
                    id: 6
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/remove_subaccount \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 6,
              "method": "private/remove_subaccount",
              "params": {
                "subaccount_id": 120
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
- [private/create_subaccount](https://docs.deribit.com/api-reference/account-management/private-create_subaccount.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/toggle_subaccount_login](https://docs.deribit.com/api-reference/account-management/private-toggle_subaccount_login.md)
- [private/change_subaccount_name](https://docs.deribit.com/api-reference/account-management/private-change_subaccount_name.md)