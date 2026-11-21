---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-create_api_key
api_type: JSON-RPC
updated_at: 2026-11-21 19:01:39.041609
---

# private/create_api_key

> Creates a new API key with the specified scope and permissions. API keys are used for programmatic access to the Deribit API and can be restricted to specific operations and IP addresses.

The response includes both the API key ID and the secret key. Store the secret securely as it will not be displayed again. You can view the API key details (without the secret) using the `list_api_keys` method.

**Note:** The new API key cannot be granted higher scopes than the API key used for authentication. Attempting to assign a scope that exceeds the authenticating key's permissions will result in an error.

**[TFA required](https://docs.deribit.com/articles/security-keys)**

**📖 Related Articles:** 
- [Creating new API key on Deribit](https://docs.deribit.com/articles/creating-api-key)
- [Access Scope](https://docs.deribit.com/articles/access-scope)

**Scope:** `account:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcreate_api_key)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/create_api_key
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
  /private/create_api_key:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Creates a new API key with the specified scope and permissions. API keys
        are used for programmatic access to the Deribit API and can be
        restricted to specific operations and IP addresses.


        The response includes both the API key ID and the secret key. Store the
        secret securely as it will not be displayed again. You can view the API
        key details (without the secret) using the `list_api_keys` method.


        **Note:** The new API key cannot be granted higher scopes than the API
        key used for authentication. Attempting to assign a scope that exceeds
        the authenticating key's permissions will result in an error.


        **[TFA required](https://docs.deribit.com/articles/security-keys)**


        **📖 Related Articles:** 

        - [Creating new API key on
        Deribit](https://docs.deribit.com/articles/creating-api-key)

        - [Access Scope](https://docs.deribit.com/articles/access-scope)


        **Scope:** `account:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcreate_api_key)

      parameters:
        - name: max_scope
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/max_scope'
          description: >
            Describes maximal access for tokens generated with given key. If
            scope is not provided, its value is set as none.


            **📖 Related Article:** [Access
            Scope](https://docs.deribit.com/articles/access-scope)
        - name: name
          in: query
          schema:
            type: string
            example: TestName
          description: >-
            Name of key (only letters, numbers and underscores allowed; maximum
            length - 16 characters)
          required: false
        - name: public_key
          in: query
          required: false
          schema:
            type: string
            example: |-
              -----BEGIN PUBLIC KEY-----
              MCowBQYDK2VwAyEAM7FWhKquNqLmTOV4hfYT5r3AjrYiORTT6Tn5HIfFNV8=
              -----END PUBLIC KEY-----
          description: >-
            ED25519 or RSA PEM Encoded public key that should be used to create
            asymmetric API Key for signing requests/authentication requests with
            user's private key.<br></br> **📖 Related Article:** [Asymmetric API
            keys](https://docs.deribit.com/articles/asymmetric-api-keys)
        - name: enabled_features
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
              enum:
                - restricted_block_trades
                - block_trade_approval
          description: >-
            List of enabled advanced on-key features. Available options:<br> -
            `restricted_block_trades`: Limit the block_trade read scope of the
            API key to Block Trades that have been made using this specific API
            key<br> - `block_trade_approval`: Block Trades created using this
            API key require additional user approval. Methods that use
            `block_rfq` scope are not affected by Block Trade approval
            feature<br> 
          style: form
          explode: true
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 8974
                  method: private/create_api_key
                  params:
                    name: Public key 1
                    max_scope: account:read trade:read block_trade:read_write wallet:none
                    public_key: >-
                      -----BEGIN PUBLIC KEY-----

                      MCowBQYDK2VwAyEAM7FWhKquNqLmTOV4hfYT5r3AjrYiORTT6Tn5HIfFNV8=

                      -----END PUBLIC KEY-----
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateApiKeyResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 8974
                    result:
                      timestamp: 1560238048714
                      max_scope: >-
                        account:read block_trade:read_write trade:read
                        wallet:none
                      id: 5
                      enabled: true
                      enabled_features: []
                      default: false
                      public_key: >-
                        -----BEGIN PUBLIC KEY-----

                        MCowBQYDK2VwAyEAM7FWhKquNqLmTOV4hfYT5r3AjrYiORTT6Tn5HIfFNV8=

                        -----END PUBLIC KEY-----
                      client_secret: 9c:6d:c9:02:fd:9f:75:6e:14:bb:71:c5:74:95:86:c8
                      client_id: wcVoQGam
                      name: ''
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/create_api_key \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 8974,
              "method": "private/create_api_key",
              "params": {
                "name": "Public key 1",
                "max_scope": "account:read trade:read block_trade:read_write wallet:none",
                "public_key": "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAM7FWhKquNqLmTOV4hfYT5r3AjrYiORTT6Tn5HIfFNV8=\n-----END PUBLIC KEY-----"
              }
            }'
components:
  schemas:
    max_scope:
      items:
        type: string
      example:
        - account:read
        - trade:read
        - block_trade:read_write
        - wallet:none
      type: array
      description: >
        Describes maximal access for tokens generated with given key. If scope
        is not provided, its value is set as none.


        **📖 Related Article:** [Access
        Scope](https://docs.deribit.com/articles/access-scope)
    PrivateApiKeyResponse:
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
          $ref: '#/components/schemas/api_key'
      required:
        - result
        - jsonrpc
      type: object
    api_key:
      properties:
        id:
          $ref: '#/components/schemas/key_id'
        timestamp:
          $ref: '#/components/schemas/timestamp'
        client_id:
          $ref: '#/components/schemas/client_id'
        client_secret:
          $ref: '#/components/schemas/client_secret'
        public_key:
          $ref: '#/components/schemas/public_key'
        max_scope:
          $ref: '#/components/schemas/max_scope'
        enabled:
          $ref: '#/components/schemas/api_key_enabled'
        default:
          $ref: '#/components/schemas/api_key_default'
        name:
          $ref: '#/components/schemas/api_key_name'
        enabled_features:
          $ref: '#/components/schemas/api_key_features'
        ip_whitelist:
          type: array
          description: List of IP addresses whitelisted for a selected key
      required:
        - id
        - timestamp
        - client_id
        - client_secret
        - max_scope
        - default
      type: object
    key_id:
      example: 1
      type: integer
      description: Key identifier
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    client_id:
      example: IY2D68DS
      type: string
      description: Client identifier used for authentication
    client_secret:
      example: P9Z_c73KaBPwpoTVfsXzehAhjhdJn5kM7Zlz_hhDhE8
      type: string
      description: Client secret or MD5 fingerprint of public key used for authentication
    public_key:
      example: >-
        -----BEGIN PUBLIC KEY-----
        MCowBQYDK2VwAyEApajFN0CSwIaaiIRPiFbiYYvpsLQLSccSLLsKPe984sc= -----END
        PUBLIC KEY-----
      type: string
      description: >-
        PEM encoded public key (Ed25519/RSA) used for asymmetric signatures
        (optional)
    api_key_enabled:
      example: true
      type: boolean
      description: Informs whether api key is enabled and can be used for authentication
    api_key_default:
      example: false
      type: boolean
      description: >-
        Informs whether this api key is default (field is deprecated and will be
        removed in the future)
    api_key_name:
      example: TestName
      type: string
      description: Api key name that can be displayed in transaction log
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

- [Creating new API key](https://docs.deribit.com/articles/creating-api-key.md)
- [Asymmetric API Keys](https://docs.deribit.com/articles/asymmetric-api-keys.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [private/remove_api_key](https://docs.deribit.com/api-reference/account-management/private-remove_api_key.md)
- [private/enable_api_key](https://docs.deribit.com/api-reference/account-management/private-enable_api_key.md)