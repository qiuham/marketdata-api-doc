---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/authentication/public-auth
api_type: JSON-RPC
updated_at: 2026-11-25 19:00:47.003598
---

# public/auth

> Retrieve an OAuth access token, to be used for authentication of 'private' requests.

**📖 Related Article:** [Authentication](https://docs.deribit.com/articles/authentication)

**Authentication Methods:**

Three methods of authentication are supported (selected with `grant_type`):

- `client_credentials` - Using the client id and client secret that can be found on the API page on the website. This is the simplest method, suitable for server-to-server applications and quick setup.

- `client_signature` - Enhanced security method using a cryptographic signature instead of sending the client secret directly. The signature is calculated over `<timestamp>\n<nonce>\n<data>` (the three values joined with line-feed characters, `timestamp` exactly as sent). Keys with a shared secret use an HMAC-SHA256 signature encoded as hexadecimal; asymmetric (RSA / Ed25519) keys use a digital signature over the same string encoded as URL-safe base64 without padding. This method requires `client_id`, `timestamp` and `signature`; `nonce` and `data` are optional (`nonce` is strongly recommended for replay protection). See the [Client Signature (WebSocket) guide](https://docs.deribit.com/articles/authentication#client-signature-websocket) for detailed signature calculation instructions.

- `refresh_token` - Using a refresh token that was received from an earlier invocation. This allows you to obtain a new access token without re-supplying your Client ID and Client Secret. Best for long-lived sessions, token renewal, and avoiding re-authentication.

**Refresh token behavior:**

- Every successful refresh issues a **new** access token **and** a new refresh token, and invalidates the previously issued token pair. Always store the newest `refresh_token`; reusing an older one fails with `-32602` (`invalid token`), which also affects concurrent refreshes with the same token.
- The `scope` parameter is ignored for this grant type: the new tokens keep the scope, session and lifetime of the original token.
- A token with `connection` scope is bound to the connection it was issued on and cannot be refreshed or used from another connection.

**Scope behavior (`client_credentials` and `client_signature`):**

- Without a `session:` or `connection` scope item, a WebSocket request gets a `connection` scope token. An HTTP (REST) request gets a `session` scope token with a generated `rest-...` session name, unless `connection` was requested explicitly.
- `connection` and `session:name` cannot be combined (`-32602`).
- Requested permission scopes (`trade`, `wallet`, `account`, `block_trade`, `block_rfq`) never exceed the permissions of the API key: higher levels are silently reduced to the key's level, and permission scopes that are not requested inherit the key's permissions. This is not reported as an error.

**Response:**

The response will contain an access token, expiration period (number of seconds that the token is valid) and a refresh token that can be used to get a new set of tokens. Over WebSocket, a successful call also authenticates the current connection, so later private requests on it need no `access_token`.

**Errors** (JSON-RPC `error.code`):

- `13004` `invalid_credentials` - unknown `client_id`, wrong `client_secret`, invalid `signature`, or `client_id` longer than 16 bytes.
- `13009` `unauthorized` - `timestamp` outside the allowed window, `nonce` longer than 128 bytes or already used, connecting IP not in the key's IP whitelist (`reason: bad_ip`).
- `-32602` `Invalid params` - missing required parameter for the chosen `grant_type`, unknown `grant_type`, invalid `scope`, or an invalid / expired / already-replaced `refresh_token` (including `session_not_found`).

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fauth)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/auth
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
  /public/auth:
    get:
      tags:
        - Authentication
        - Public
      description: >+
        Retrieve an OAuth access token, to be used for authentication of
        'private' requests.


        **📖 Related Article:**
        [Authentication](https://docs.deribit.com/articles/authentication)


        **Authentication Methods:**


        Three methods of authentication are supported (selected with
        `grant_type`):


        - `client_credentials` - Using the client id and client secret that can
        be found on the API page on the website. This is the simplest method,
        suitable for server-to-server applications and quick setup.


        - `client_signature` - Enhanced security method using a cryptographic
        signature instead of sending the client secret directly. The signature
        is calculated over `<timestamp>\n<nonce>\n<data>` (the three values
        joined with line-feed characters, `timestamp` exactly as sent). Keys
        with a shared secret use an HMAC-SHA256 signature encoded as
        hexadecimal; asymmetric (RSA / Ed25519) keys use a digital signature
        over the same string encoded as URL-safe base64 without padding. This
        method requires `client_id`, `timestamp` and `signature`; `nonce` and
        `data` are optional (`nonce` is strongly recommended for replay
        protection). See the [Client Signature (WebSocket)
        guide](https://docs.deribit.com/articles/authentication#client-signature-websocket)
        for detailed signature calculation instructions.


        - `refresh_token` - Using a refresh token that was received from an
        earlier invocation. This allows you to obtain a new access token without
        re-supplying your Client ID and Client Secret. Best for long-lived
        sessions, token renewal, and avoiding re-authentication.


        **Refresh token behavior:**


        - Every successful refresh issues a **new** access token **and** a new
        refresh token, and invalidates the previously issued token pair. Always
        store the newest `refresh_token`; reusing an older one fails with
        `-32602` (`invalid token`), which also affects concurrent refreshes with
        the same token.

        - The `scope` parameter is ignored for this grant type: the new tokens
        keep the scope, session and lifetime of the original token.

        - A token with `connection` scope is bound to the connection it was
        issued on and cannot be refreshed or used from another connection.


        **Scope behavior (`client_credentials` and `client_signature`):**


        - Without a `session:` or `connection` scope item, a WebSocket request
        gets a `connection` scope token. An HTTP (REST) request gets a `session`
        scope token with a generated `rest-...` session name, unless
        `connection` was requested explicitly.

        - `connection` and `session:name` cannot be combined (`-32602`).

        - Requested permission scopes (`trade`, `wallet`, `account`,
        `block_trade`, `block_rfq`) never exceed the permissions of the API key:
        higher levels are silently reduced to the key's level, and permission
        scopes that are not requested inherit the key's permissions. This is not
        reported as an error.


        **Response:**


        The response will contain an access token, expiration period (number of
        seconds that the token is valid) and a refresh token that can be used to
        get a new set of tokens. Over WebSocket, a successful call also
        authenticates the current connection, so later private requests on it
        need no `access_token`.


        **Errors** (JSON-RPC `error.code`):


        - `13004` `invalid_credentials` - unknown `client_id`, wrong
        `client_secret`, invalid `signature`, or `client_id` longer than 16
        bytes.

        - `13009` `unauthorized` - `timestamp` outside the allowed window,
        `nonce` longer than 128 bytes or already used, connecting IP not in the
        key's IP whitelist (`reason: bad_ip`).

        - `-32602` `Invalid params` - missing required parameter for the chosen
        `grant_type`, unknown `grant_type`, invalid `scope`, or an invalid /
        expired / already-replaced `refresh_token` (including
        `session_not_found`).


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fauth)

      parameters:
        - name: grant_type
          in: query
          schema:
            type: string
            enum:
              - client_credentials
              - client_signature
              - refresh_token
            example: client_credentials
          required: true
          description: Method of authentication
        - name: client_id
          in: query
          schema:
            type: string
            example: fo7WAPRm4P
          description: >-
            Required for grant types `client_credentials` and
            `client_signature`. Maximum length is 16 bytes.
          required: false
        - name: client_secret
          in: query
          schema:
            type: string
            example: W0H6FJW4IRPZ1MOQ8FP6KMC5RZDUUKXS
          description: Required for grant type `client_credentials`.
          required: false
        - name: refresh_token
          in: query
          schema:
            type: string
          description: >-
            Required for grant type `refresh_token`. The token pair it belongs
            to is replaced by the new tokens returned (see above).
          required: false
        - name: timestamp
          in: query
          schema:
            type: integer
          description: >
            Required for grant type `client_signature`.


            Time when the request was generated, in milliseconds since the UNIX
            epoch. Must be within ±60 seconds (±60,000 ms) of the server time,
            otherwise the request is rejected with error `13009`
            (`unauthorized`).
          required: false
        - name: signature
          in: query
          schema:
            type: string
          description: >
            Required for grant type `client_signature`.


            Signature calculated over `<timestamp>\n<nonce>\n<data>`:

            - **Shared-secret API keys:** HMAC-SHA256 with the client secret as
            key, encoded as hexadecimal (letter case is ignored).

            - **Asymmetric (RSA / Ed25519) API keys:** digital signature made
            with your private key (SHA-256), encoded as URL-safe base64 without
            padding.


            An invalid signature is rejected with error `13004`
            (`invalid_credentials`).
          required: false
        - name: nonce
          in: query
          schema:
            type: string
          description: >
            Optional for grant type `client_signature`, but strongly
            recommended. Defaults to an empty string.


            User-generated random string, up to 128 bytes. A non-empty nonce can
            be used only once for the same `client_id` and `timestamp` (a repeat
            is rejected with `13009`). With an empty or omitted nonce the
            timestamp window is still enforced but replay detection is not.
          required: false
        - name: data
          in: query
          schema:
            type: string
          description: >
            Optional for grant type `client_signature`. Defaults to an empty
            string.


            Contains any user specific value; it is part of the signed string.
          required: false
        - name: state
          in: query
          schema:
            type: string
          description: Will be passed back in the response.
          required: false
        - name: scope
          in: query
          schema:
            type: string
            example: connection
          description: >
            Describes type of the access for assigned token. Ignored for grant
            type `refresh_token`.


            **Possible values:**


            - `connection`

            - `session:name` (names longer than 64 bytes are truncated)

            - `trade:[read, read_write, none]`

            - `wallet:[read, read_write, none]`

            - `account:[read, read_write, none]`

            - `block_trade:[read, read_write, none]`

            - `block_rfq:[read, read_write, none]`

            - `expires:NUMBER`

            - `ip:ADDR`


            `connection` and `session:name` are mutually exclusive. Permission
            scopes cannot exceed the permissions of the API key.


            Details are elucidated in [Access
            scope](https://docs.deribit.com/articles/access-scope)
          required: false
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 9929
                  method: public/auth
                  params:
                    grant_type: client_credentials
                    client_id: fo7WAPRm4P
                    client_secret: W0H6FJW4IRPZ1MOQ8FP6KMC5RZDUUKXS
              client_signatureRequest:
                summary: Client signature Request
                value:
                  jsonrpc: '2.0'
                  id: 9930
                  method: public/auth
                  params:
                    grant_type: client_signature
                    client_id: fo7WAPRm4P
                    timestamp: 1582628593469
                    signature: >-
                      f22e7089f592213ca51ad051b26fe835bce7edd284bc5eb9fe6e7d7ed3cb4430
                    nonce: fm8Kq3xPd2
              refresh_tokenRequest:
                summary: Refresh token Request
                value:
                  jsonrpc: '2.0'
                  id: 9931
                  method: public/auth
                  params:
                    grant_type: refresh_token
                    refresh_token: >-
                      1582628593469.1GP4rQd0.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM
              sessionRequest:
                summary: Session Request
                value:
                  jsonrpc: '2.0'
                  id: 9932
                  method: public/auth
                  params:
                    grant_type: client_credentials
                    client_id: fo7WAPRm4P
                    client_secret: W0H6FJW4IRPZ1MOQ8FP6KMC5RZDUUKXS
                    scope: session:my_bot trade:read
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicAuthResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 9929
                    result:
                      access_token: >-
                        1582628593469.1MbQ-J_4.CBP-OqOwm_FBdMYj4cRK2dMXyHPfBtXGpzLxhWg31nHu3H_Q60FpE5_vqUBEQGSiMrIGzw3nC37NMb9d1tpBNqBOM_Ql9pXOmgtV9Yj3Pq1c6BqC6dU6eTxHMFO67x8GpJxqw_QcKP5IepwGBD-gfKSHfAv9AEnLJkNu3JkMJBdLToY1lrBnuedF3dU_uARm
                      expires_in: 31536000
                      refresh_token: >-
                        1582628593469.1GP4rQd0.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM
                      scope: connection mainaccount
                      enabled_features: []
                      token_type: bearer
                client_signatureResponse:
                  summary: Client_signature response example
                  value:
                    jsonrpc: '2.0'
                    id: 9930
                    result:
                      access_token: >-
                        1582628593469.1MbQ-J_4.CBP-OqOwm_FBdMYj4cRK2dMXyHPfBtXGpzLxhWg31nHu3H_Q60FpE5_vqUBEQGSiMrIGzw3nC37NMb9d1tpBNqBOM_Ql9pXOmgtV9Yj3Pq1c6BqC6dU6eTxHMFO67x8GpJxqw_QcKP5IepwGBD-gfKSHfAv9AEnLJkNu3JkMJBdLToY1lrBnuedF3dU_uARm
                      expires_in: 31536000
                      refresh_token: >-
                        1582628593469.1GP4rQd0.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM
                      scope: connection mainaccount
                      enabled_features: []
                      token_type: bearer
                refresh_tokenResponse:
                  summary: Refresh_token response example
                  value:
                    jsonrpc: '2.0'
                    id: 9931
                    result:
                      access_token: >-
                        1582628593470.2NcR-K_5.DBQ-PrPxn_GCeNZk5dSL3eNYzIQgCuYHyMyMxiXh42oIv4I_R71GqF6_wrVCFRIjNsJH0x4oDc48ONc0e2uqCOrCPN_Rm0qYPnhtW0Zk4Qr2d7CrD7eV7fUyINFP78y9HqKyrc_RdLQ6JfqxHCE-hgLTIfBw0BFmMLkOv4KlNKCeMUoZ2msCovfeG4eV_vBSn
                      expires_in: 31536000
                      refresh_token: >-
                        1582628593470.2HQ5sRe1.B0Xb89p6lGSJVQ50nTdbE2DrIhjL61IPm3WB7lDuXb9CRaV6Es14CidbYQOwFi4J_NWjyLZozyCPeLKxMmL9MYogp291dlQjQk0zPmdlVv50lYvG4OOQ4tUQdEg24D2DxNLlK2OPdg2zQnScsteeichR-iMb51ugy7Pb-96znn_4a76MadnDfMsnmk_B0kN
                      scope: connection mainaccount
                      enabled_features: []
                      token_type: bearer
                sessionResponse:
                  summary: Session response example
                  value:
                    jsonrpc: '2.0'
                    id: 9932
                    result:
                      access_token: >-
                        1582628600120.3PdS-L_6.CBP-OqOwm_FBdMYj4cRK2dMXyHPfBtXGpzLxhWg31nHu3H_Q60FpE5_vqUBEQGSiMrIGzw3nC37NMb9d1tpBNqBOM_Ql9pXOmgtV9Yj3Pq1c6BqC6dU6eTxHMFO67x8GpJxqw_QcKP5IepwGBD-gfKSHfAv9AEnLJkNu3JkMJBdLToY1lrBnuedF3dU_uARm
                      expires_in: 900
                      refresh_token: >-
                        1582628600120.3IR6tSf2.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM
                      scope: session:my_bot trade:read mainaccount
                      enabled_features: []
                      token_type: bearer
                      sid: 3571.fo7WAPRm4P.my_bot
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/auth \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 9929,
              "method": "public/auth",
              "params": {
                "grant_type": "client_credentials",
                "client_id": "fo7WAPRm4P",
                "client_secret": "W0H6FJW4IRPZ1MOQ8FP6KMC5RZDUUKXS"
              }
            }'
        - lang: bash
          label: cURL (Client signature)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/auth \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 9930,
              "method": "public/auth",
              "params": {
                "grant_type": "client_signature",
                "client_id": "fo7WAPRm4P",
                "timestamp": 1582628593469,
                "signature": "f22e7089f592213ca51ad051b26fe835bce7edd284bc5eb9fe6e7d7ed3cb4430",
                "nonce": "fm8Kq3xPd2"
              }
            }'
        - lang: bash
          label: cURL (Refresh token)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/auth \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 9931,
              "method": "public/auth",
              "params": {
                "grant_type": "refresh_token",
                "refresh_token": "1582628593469.1GP4rQd0.A9Wa78o5kFRIUP49mScaD1CqHgiK50HOl2VA6kCtWa8BQZU5Dr03BhcbXPNvEh3I_MVixKZXnyoBeKJwLl8LXnfo180ckAiPj3zOclcUu4zkXuF3NNP3sTPcDf1B3C1CwMKkJ1NOcf1yPmRbsrd7hbgQ-hLa40tfx6Oa-85ymm_3Z65LZcnCeLrqlj_A9jM"
              }
            }'
        - lang: bash
          label: cURL (Session)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/auth \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 9932,
              "method": "public/auth",
              "params": {
                "grant_type": "client_credentials",
                "client_id": "fo7WAPRm4P",
                "client_secret": "W0H6FJW4IRPZ1MOQ8FP6KMC5RZDUUKXS",
                "scope": "session:my_bot trade:read"
              }
            }'
components:
  schemas:
    PublicAuthResponse:
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
              description: >-
                OAuth access token to be used for authentication of 'private'
                requests
            token_type:
              type: string
              enum:
                - bearer
              description: Authorization type, allowed value - `bearer`
            expires_in:
              type: integer
              example: 31536000
              description: Token lifetime in seconds
            refresh_token:
              type: string
              example: 6faf8L36JdaSqsjCEEiwqifPpj6JB18RWwiWHrsGTZ91
              description: Can be used to request a new token (with a new lifetime)
            scope:
              type: string
              description: Type of the access for assigned token
            state:
              type: string
              description: Copied from the input (if applicable)
            sid:
              type: string
              description: Optional Session id
            enabled_features:
              $ref: '#/components/schemas/api_key_features'
            mandatory_tfa_status:
              type: string
              example: enabled
              description: 2FA is required for privileged methods
            google_login:
              type: boolean
              description: The access token was acquired by logging in through Google.
            apple_login:
              type: boolean
              description: The access token was acquired by logging in through Apple.
            coinbase_login:
              type: boolean
              description: The access token was acquired by logging in through Coinbase.
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
    api_key_features:
      items:
        type: string
      type: array
      description: >-
        List of enabled advanced on-key features.<br><br><b>Available
        options:</b><br>- <code>restricted_block_trades</code>: Limit the
        block_trade read scope of the API key to Block Trades that have been
        made using this specific API key<br>- <code>block_trade_approval</code>:
        Block Trades created using this API key require additional user
        approval. Methods that use <code>block_rfq</code> scope are not affected
        by Block Trade approval feature

````

## Related topics

- [public/fork_token](https://docs.deribit.com/api-reference/authentication/public-fork_token.md)
- [API Authentication with OAuth 2.0 and Signatures](https://docs.deribit.com/articles/authentication.md)
- [Managing Transfers](https://docs.deribit.com/articles/managing-transfers-api.md)
- [Creating new API key](https://docs.deribit.com/articles/creating-api-key.md)
- [Asymmetric API Keys](https://docs.deribit.com/articles/asymmetric-api-keys.md)