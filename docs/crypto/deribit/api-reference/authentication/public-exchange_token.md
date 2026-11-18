---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/authentication/public-exchange_token
api_type: JSON-RPC
updated_at: 2026-11-18 18:59:12.206754
---

# public/exchange_token

> Generates a token for a new subject id. This method can be used to switch between subaccounts.

**Rules:**

- `subject_id` must differ from the subject of the supplied refresh token (otherwise `-32602`) and must identify an active user (otherwise `-32602`).
- Regular clients can only switch within their own account family (the main account and its subaccounts). A token issued directly for a subaccount cannot switch to the main account or to sibling subaccounts (`-32602` on `subject_id`). Vault subaccounts are rejected with `14049` (`vault_subaccount_not_allowed`).
- Without `scope`, the new token inherits the scope of the supplied refresh token. A supplied `scope` **replaces** it (it is not merged), and cannot exceed the scope of the refresh token (`13403` `scope_exceeded`). If it contains neither `session:` nor `connection`, a session with a generated name is created.
- The new access token's lifetime is counted from the issue time of the supplied refresh token.
- Over WebSocket, the returned access token is also installed on the current connection, so subsequent private requests act as the new subject.
- An invalid, expired or already-replaced refresh token (or one bound to another connection) returns `-32602` on `refresh_token`; `session_not_found` means the session of the token no longer exists.

**📖 Related Articles:** 
- [Fork and Exchange Tokens](https://docs.deribit.com/articles/authentication#fork-and-exchange-tokens)
- [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fexchange_token)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/exchange_token
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
  /public/exchange_token:
    get:
      tags:
        - Authentication
        - Public
      description: >+
        Generates a token for a new subject id. This method can be used to
        switch between subaccounts.


        **Rules:**


        - `subject_id` must differ from the subject of the supplied refresh
        token (otherwise `-32602`) and must identify an active user (otherwise
        `-32602`).

        - Regular clients can only switch within their own account family (the
        main account and its subaccounts). A token issued directly for a
        subaccount cannot switch to the main account or to sibling subaccounts
        (`-32602` on `subject_id`). Vault subaccounts are rejected with `14049`
        (`vault_subaccount_not_allowed`).

        - Without `scope`, the new token inherits the scope of the supplied
        refresh token. A supplied `scope` **replaces** it (it is not merged),
        and cannot exceed the scope of the refresh token (`13403`
        `scope_exceeded`). If it contains neither `session:` nor `connection`, a
        session with a generated name is created.

        - The new access token's lifetime is counted from the issue time of the
        supplied refresh token.

        - Over WebSocket, the returned access token is also installed on the
        current connection, so subsequent private requests act as the new
        subject.

        - An invalid, expired or already-replaced refresh token (or one bound to
        another connection) returns `-32602` on `refresh_token`;
        `session_not_found` means the session of the token no longer exists.


        **📖 Related Articles:** 

        - [Fork and Exchange
        Tokens](https://docs.deribit.com/articles/authentication#fork-and-exchange-tokens)

        - [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fexchange_token)

      parameters:
        - name: refresh_token
          in: query
          schema:
            type: string
            example: >-
              1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ
          required: true
          description: Refresh token
        - name: subject_id
          in: query
          schema:
            example: 10
            type: integer
          required: true
          description: >-
            Id of the user (main account or subaccount) to switch to. Must
            differ from the current subject.
        - name: scope
          in: query
          schema:
            type: string
          required: false
          description: >-
            Optional scope for the new token. Replaces (does not merge with) the
            scope of the refresh token and cannot exceed it (`13403`
            `scope_exceeded`). Supports `session:name` for direct session
            creation. If omitted, the scope of the refresh token is kept.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 7619
                  method: public/exchange_token
                  params:
                    refresh_token: >-
                      1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ
                    subject_id: 10
              scopeRequest:
                summary: Scope Request
                value:
                  jsonrpc: '2.0'
                  id: 7621
                  method: public/exchange_token
                  params:
                    refresh_token: >-
                      1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ
                    subject_id: 10
                    scope: session:accounting_view trade:read account:read
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicTokenResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 7619
                    result:
                      access_token: >-
                        1582628593469.1MbQ-J_4.CBP-OqOwm_FBdMYj4cRK2dMXyHPfBtXGpzLxhWg31nHu3H_Q60FpE5_vqUBEQGSiMrIGzw3nC37NMb9d1tpBNqBOM_Ql9pXOmgtV9Yj3Pq1c6BqC6dU6eTxHMFO67x8GpJxqw_QcKP5IepwGBD-gfKSHfAv9AEnLJkNu3JkMJBdLToY1lrBnuedF3dU_uARm
                      expires_in: 900
                      refresh_token: >-
                        1582628593469.1GP4rQd0.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM
                      scope: session:named_session mainaccount
                      sid: 3571.fo7WAPRm4P.named_session
                      token_type: bearer
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/exchange_token \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 7619,
              "method": "public/exchange_token",
              "params": {
                "refresh_token": "1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ",
                "subject_id": 10
              }
            }'
        - lang: bash
          label: cURL (Scope)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/exchange_token \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 7621,
              "method": "public/exchange_token",
              "params": {
                "refresh_token": "1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ",
                "subject_id": 10,
                "scope": "session:accounting_view trade:read account:read"
              }
            }'
components:
  schemas:
    PublicTokenResponse:
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
            access_token:
              type: string
              example: 843SehgeX5n6XxEU4XbABx4Cny5Akai5iHiJePTsvUw7
            token_type:
              type: string
              enum:
                - bearer
              description: Authorization type, allowed value - `bearer`
            expires_in:
              type: integer
              example: 900
              description: Remaining token lifetime in seconds
            refresh_token:
              type: string
              example: 6faf8L36JdaSqsjCEEiwqifPpj6JB18RWwiWHrsGTZ91
              description: Can be used to request a new token (with a new lifetime)
            scope:
              type: string
              description: Type of the access for assigned token
            sid:
              type: string
              description: Session id (present for session scope tokens)
          required:
            - access_token
            - token_type
            - expires_in
            - refresh_token
            - scope
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [public/fork_token](https://docs.deribit.com/api-reference/authentication/public-fork_token.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Managing Transfers](https://docs.deribit.com/articles/managing-transfers-api.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [API Authentication with OAuth 2.0 and Signatures](https://docs.deribit.com/articles/authentication.md)