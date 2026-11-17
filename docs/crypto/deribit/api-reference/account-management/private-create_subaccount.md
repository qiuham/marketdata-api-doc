---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-create_subaccount
api_type: JSON-RPC
updated_at: 2026-11-16 20:32:24.285649
---

# private/create_subaccount

> Creates a new subaccount under the authenticated main account. Subaccounts allow you to organize trading activities and manage risk separately from the main account.

This method takes no parameters. The new subaccount will be created with default settings and can be configured using other subaccount management methods.

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read_write` and mainaccount

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcreate_subaccount)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/create_subaccount
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
  /private/create_subaccount:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Creates a new subaccount under the authenticated main account.
        Subaccounts allow you to organize trading activities and manage risk
        separately from the main account.


        This method takes no parameters. The new subaccount will be created with
        default settings and can be configured using other subaccount management
        methods.


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read_write` and mainaccount


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcreate_subaccount)

      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 5414
                  method: private/create_subaccount
                  params: {}
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateCreateSubaccountResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 5414
                    result:
                      email: user_AAA@email.com
                      id: 13
                      is_password: false
                      login_enabled: false
                      portfolio:
                        eth:
                          available_funds: 0
                          available_withdrawal_funds: 0
                          balance: 0
                          currency: eth
                          equity: 0
                          initial_margin: 0
                          maintenance_margin: 0
                          margin_balance: 0
                        btc:
                          available_funds: 0
                          available_withdrawal_funds: 0
                          balance: 0
                          currency: btc
                          equity: 0
                          initial_margin: 0
                          maintenance_margin: 0
                          margin_balance: 0
                      receive_notifications: false
                      system_name: user_1_4
                      security_keys_enabled: false
                      type: subaccount
                      username: user_1_4
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/create_subaccount \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 5414,
              "method": "private/create_subaccount",
              "params": {}
            }'
components:
  schemas:
    PrivateCreateSubaccountResponse:
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
            email:
              example: user@example.com
              type: string
              description: User email
            login_enabled:
              type: boolean
              description: Informs whether login to the subaccount is enabled
            is_password:
              type: boolean
              description: '`true` when password for the subaccount has been configured'
            receive_notifications:
              type: boolean
              description: When `true` - receive all notification emails on the main email
            system_name:
              example: username_1
              type: string
              description: System generated user nickname
            security_keys_enabled:
              type: boolean
              description: Whether the Security Keys authentication is enabled
            security_keys_assignments:
              type: array
              items:
                type: string
              description: Names of assignments with Security Keys assigned
            username:
              type: string
              description: Account name (given by user)
            type:
              enum:
                - subaccount
              type: string
              description: Account type
            id:
              type: integer
              description: Subaccount identifier
            portfolio:
              $ref: '#/components/schemas/portfolio'
              description: Portfolio information for the subaccount
            margin_model:
              type: string
              description: Margin model
            disabled_trading_products:
              type: array
              items:
                type: string
              description: List of disabled trading products
            trading_products_details:
              type: array
              items:
                type: object
                properties:
                  enabled:
                    type: boolean
                  product:
                    type: string
                  overwriteable:
                    type: boolean
                  requires_consent:
                    type: boolean
              description: Details about trading products availability
            referrals_count:
              type: integer
              description: Number of referrals
          required:
            - username
            - type
            - id
            - login_enabled
            - is_password
            - receive_notifications
            - system_name
            - email
            - security_keys_enabled
            - security_keys_assignments
            - margin_model
            - disabled_trading_products
            - trading_products_details
            - referrals_count
      required:
        - result
        - jsonrpc
      type: object
    portfolio:
      additionalProperties:
        $ref: '#/components/schemas/currency_portfolio'
      type: object
      description: Portfolio entries keyed by lowercase currency code.
    currency_portfolio:
      properties:
        margin_balance:
          type: number
          description: >-
            The account's margin balance. When cross collateral is enabled, this
            aggregated value is calculated by converting the sum of each cross
            collateral currency's value to the given currency, using each cross
            collateral currency's index.
        currency:
          type: string
          description: The selected currency
        maintenance_margin:
          type: number
          description: >-
            The maintenance margin. When cross collateral is enabled, this
            aggregated value is calculated by converting the sum of each cross
            collateral currency's value to the given currency, using each cross
            collateral currency's index.
        initial_margin:
          type: number
          description: >-
            The account's initial margin. When cross collateral is enabled, this
            aggregated value is calculated by converting the sum of each cross
            collateral currency's value to the given currency, using each cross
            collateral currency's index.
        equity:
          type: number
          description: The account's current equity
        balance:
          type: number
          description: The account's balance
        available_withdrawal_funds:
          type: number
          description: The account's available to withdrawal funds
        available_funds:
          type: number
          description: >-
            The account's available funds. When cross collateral is enabled,
            this aggregated value is calculated by converting the sum of each
            cross collateral currency's value to the given currency, using each
            cross collateral currency's index.
        additional_reserve:
          $ref: '#/components/schemas/additional_reserve'
        spot_reserve:
          type: number
          description: The account's balance reserved in active spot orders
      required:
        - margin_balance
        - currency
        - maintenance_margin
        - initial_margin
        - equity
        - balance
        - available_withdrawal_funds
        - available_funds
        - additional_reserve
        - spot_reserve
      type: object
    additional_reserve:
      example: 0.3
      type: number
      description: >-
        The account's balance reserved for open buy option orders and option
        combo orders (the premium payable if they fill). Only non-zero on the
        `cross_sm` margin model; balance reserved by spot orders is reported
        separately in `spot_reserve`.

````

## Related topics

- [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api.md)
- [private/submit_transfer_to_subaccount](https://docs.deribit.com/api-reference/wallet/private-submit_transfer_to_subaccount.md)
- [private/submit_transfer_between_subaccounts](https://docs.deribit.com/api-reference/wallet/private-submit_transfer_between_subaccounts.md)
- [private/remove_subaccount](https://docs.deribit.com/api-reference/account-management/private-remove_subaccount.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)