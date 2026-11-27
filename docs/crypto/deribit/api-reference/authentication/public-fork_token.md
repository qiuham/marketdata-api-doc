---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/authentication/public-fork_token
api_type: JSON-RPC
updated_at: 2026-11-27 19:00:54.457412
---

# public/fork_token

> Generates a token for a new named session. This method can be used only with session scoped tokens.

**Rules:**

- The refresh token must have `session` scope; a `connection` scope refresh token is rejected with `-32602` on `refresh_token`.
- `session_name` longer than 64 bytes is truncated (not rejected). The truncated name must differ from the current session name, otherwise the call fails with `-32602` on `session_name`.
- The forked session keeps the scope of the original token with only the session name replaced, and receives a fresh access token and refresh token.
- Unlike `public/auth` and `public/exchange_token`, the forked access token is **not** installed on the current WebSocket connection: the connection keeps its current authentication until you authenticate it with the new token.
- An invalid, expired or already-replaced refresh token returns `-32602` on `refresh_token`; `session_not_found` means the session of the token no longer exists.

**📖 More Details:** [Fork and Exchange Tokens](https://docs.deribit.com/articles/authentication#fork-and-exchange-tokens)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Ffork_token)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/fork_token
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
  /public/fork_token:
    get:
      tags:
        - Authentication
        - Public
      description: >+
        Generates a token for a new named session. This method can be used only
        with session scoped tokens.


        **Rules:**


        - The refresh token must have `session` scope; a `connection` scope
        refresh token is rejected with `-32602` on `refresh_token`.

        - `session_name` longer than 64 bytes is truncated (not rejected). The
        truncated name must differ from the current session name, otherwise the
        call fails with `-32602` on `session_name`.

        - The forked session keeps the scope of the original token with only the
        session name replaced, and receives a fresh access token and refresh
        token.

        - Unlike `public/auth` and `public/exchange_token`, the forked access
        token is **not** installed on the current WebSocket connection: the
        connection keeps its current authentication until you authenticate it
        with the new token.

        - An invalid, expired or already-replaced refresh token returns `-32602`
        on `refresh_token`; `session_not_found` means the session of the token
        no longer exists.


        **📖 More Details:** [Fork and Exchange
        Tokens](https://docs.deribit.com/articles/authentication#fork-and-exchange-tokens)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Ffork_token)

      parameters:
        - name: refresh_token
          in: query
          schema:
            type: string
            example: >-
              1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ
          required: true
          description: Refresh token
        - name: session_name
          in: query
          schema:
            type: string
            example: forked_session_name
          required: true
          description: >-
            Name of the new session (truncated to 64 bytes). Must differ from
            the current session name.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 7620
                  method: public/fork_token
                  params:
                    refresh_token: >-
                      1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ
                    session_name: forked_session_name
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
                    id: 7620
                    result:
                      access_token: >-
                        1582628593469.1MbQ-J_4.CBP-OqOwm_FBdMYj4cRK2dMXyHPfBtXGpzLxhWg31nHu3H_Q60FpE5_vqUBEQGSiMrIGzw3nC37NMb9d1tpBNqBOM_Ql9pXOmgtV9Yj3Pq1c6BqC6dU6eTxHMFO67x8GpJxqw_QcKP5IepwGBD-gfKSHfAv9AEnLJkNu3JkMJBdLToY1lrBnuedF3dU_uARm
                      expires_in: 900
                      refresh_token: >-
                        1582628593469.1GP4rQd0.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM
                      scope: session:forked_session_name mainaccount
                      sid: 3571.fo7WAPRm4P.forked_session_name
                      token_type: bearer
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/fork_token \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 7620,
              "method": "public/fork_token",
              "params": {
                "refresh_token": "1568800656974.1CWcuzUS.MGy49NK4hpTwvR1OYWfpqMEkH4T4oDg4tNIcrM7KdeyxXRcSFqiGzA_D4Cn7mqWocHmlS89FFmUYcmaN2H7lNKKTnhRg5EtrzsFCCiuyN0Wv9y-LbGLV3-Ojv_kbD50FoScQ8BDXS5b_w6Ir1MqEdQ3qFZ3MLcvlPiIgG2BqyJX3ybYnVpIlrVrrdYD1-lkjLcjxOBNJvvUKNUAzkQ",
                "session_name": "forked_session_name"
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

- [API Authentication with OAuth 2.0 and Signatures](https://docs.deribit.com/articles/authentication.md)
- [Managing Transfers](https://docs.deribit.com/articles/managing-transfers-api.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [public/exchange_token](https://docs.deribit.com/api-reference/authentication/public-exchange_token.md)
- [public/auth](https://docs.deribit.com/api-reference/authentication/public-auth.md)