---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-get_subaccounts
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:43.048244
---

# private/get_subaccounts

> Retrieves the main account and its subaccounts, with identifiers, names, email, login and security status. The list always includes the main account itself (`type: main`); removed subaccounts are not listed.

**Visibility:**
- Main account access is available when the authenticated account is the main account, or its token grants access to that main account (`mainaccount` scope or impersonated access). The response lists the main account and its eligible subaccounts.
- Without main account access, a subaccount caller receives only the main account, with limited details (login, password and security-key related fields and `disabled_trading_products` are omitted), and the calling subaccount with full details.
- Vault subaccounts are excluded from ordinary public listings. Isolated-margin subaccounts are not listed.
- Not available for retail brokers (`14021`).

**Portfolio:** set `with_portfolio` to `true` to include per-currency balance and margin summaries (equity, balance, available funds, margin; no positions or orders). With main account access, each returned account has a `portfolio` object. Without it, only the calling subaccount has `portfolio`; the main account entry omits it. The flag also adds `referrals_count` and, while an email change is awaiting confirmation, `not_confirmed_email`. By default only account metadata is returned.

**Examples:** response values are illustrative, not live account data. The examples show all trading products enabled, with no subaccount consent requirements.

**📖 Related Article:** [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)

**Scope:** `account:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_subaccounts)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_subaccounts
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
  /private/get_subaccounts:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Retrieves the main account and its subaccounts, with identifiers, names,
        email, login and security status. The list always includes the main
        account itself (`type: main`); removed subaccounts are not listed.


        **Visibility:**

        - Main account access is available when the authenticated account is the
        main account, or its token grants access to that main account
        (`mainaccount` scope or impersonated access). The response lists the
        main account and its eligible subaccounts.

        - Without main account access, a subaccount caller receives only the
        main account, with limited details (login, password and security-key
        related fields and `disabled_trading_products` are omitted), and the
        calling subaccount with full details.

        - Vault subaccounts are excluded from ordinary public listings.
        Isolated-margin subaccounts are not listed.

        - Not available for retail brokers (`14021`).


        **Portfolio:** set `with_portfolio` to `true` to include per-currency
        balance and margin summaries (equity, balance, available funds, margin;
        no positions or orders). With main account access, each returned account
        has a `portfolio` object. Without it, only the calling subaccount has
        `portfolio`; the main account entry omits it. The flag also adds
        `referrals_count` and, while an email change is awaiting confirmation,
        `not_confirmed_email`. By default only account metadata is returned.


        **Examples:** response values are illustrative, not live account data.
        The examples show all trading products enabled, with no subaccount
        consent requirements.


        **📖 Related Article:** [Managing
        Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api)


        **Scope:** `account:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_subaccounts)

      parameters:
        - name: with_portfolio
          in: query
          schema:
            default: false
            example: true
            type: boolean
          description: >-
            Portfolio flag: `true` to include per-currency balance and margin
            summaries (no positions), `false` for account metadata only
          required: false
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 4947
                  method: private/get_subaccounts
                  params:
                    with_portfolio: true
              metadataRequest:
                summary: Metadata Request
                value:
                  jsonrpc: '2.0'
                  id: 4948
                  method: private/get_subaccounts
                  params:
                    with_portfolio: false
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetSubaccountsResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 4947
                    result:
                      - email: user_AAA@example.com
                        id: 2
                        is_password: true
                        margin_model: segregated_sm
                        login_enabled: true
                        disabled_trading_products: []
                        trading_products_details:
                          - product: perpetual
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: futures
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: options
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: future_combos
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: option_combos
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: spots
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                        referrals_count: 0
                        portfolio:
                          eth:
                            additional_reserve: 0
                            spot_reserve: 0
                            available_funds: 5
                            available_withdrawal_funds: 5
                            balance: 5
                            locked_balance: 0
                            currency: eth
                            equity: 5
                            initial_margin: 0
                            maintenance_margin: 0
                            margin_balance: 5
                          btc:
                            additional_reserve: 0
                            spot_reserve: 0
                            available_funds: 5.000413075
                            available_withdrawal_funds: 5.000413075
                            balance: 5.000593987
                            locked_balance: 0
                            currency: btc
                            equity: 5.000571846
                            initial_margin: 0.000158771
                            maintenance_margin: 0.000115715
                            margin_balance: 5.000571846
                        receive_notifications: false
                        system_name: user_1
                        security_keys_enabled: false
                        security_keys_assignments: []
                        type: main
                        username: user_1
                      - email: user_AAA@example.com
                        id: 7
                        is_password: true
                        margin_model: cross_pm
                        login_enabled: false
                        disabled_trading_products: []
                        trading_products_details:
                          - product: perpetual
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: futures
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: options
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: future_combos
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: option_combos
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: spots
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                        referrals_count: 0
                        portfolio:
                          eth:
                            additional_reserve: 0
                            spot_reserve: 0
                            available_funds: 0
                            available_withdrawal_funds: 0
                            balance: 0
                            locked_balance: 0
                            currency: eth
                            equity: 0
                            initial_margin: 0
                            maintenance_margin: 0
                            margin_balance: 0
                          btc:
                            additional_reserve: 0
                            spot_reserve: 0
                            available_funds: 0
                            available_withdrawal_funds: 0
                            balance: 0
                            locked_balance: 0
                            currency: btc
                            equity: 0
                            initial_margin: 0
                            maintenance_margin: 0
                            margin_balance: 0
                        receive_notifications: false
                        system_name: user_1_1
                        security_keys_enabled: false
                        security_keys_assignments: []
                        type: subaccount
                        username: user_1_1
                metadataResponse:
                  summary: Metadata response example
                  value:
                    jsonrpc: '2.0'
                    id: 4948
                    result:
                      - email: user_AAA@example.com
                        id: 2
                        is_password: true
                        margin_model: segregated_sm
                        login_enabled: true
                        disabled_trading_products: []
                        trading_products_details:
                          - product: perpetual
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: futures
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: options
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: future_combos
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: option_combos
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                          - product: spots
                            enabled: true
                            overwriteable: false
                            requires_consent: false
                        receive_notifications: false
                        system_name: user_1
                        security_keys_enabled: false
                        security_keys_assignments: []
                        type: main
                        username: user_1
                      - email: user_AAA@example.com
                        id: 7
                        is_password: true
                        margin_model: cross_pm
                        login_enabled: false
                        disabled_trading_products: []
                        trading_products_details:
                          - product: perpetual
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: futures
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: options
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: future_combos
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: option_combos
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                          - product: spots
                            enabled: true
                            overwriteable: true
                            requires_consent: false
                        receive_notifications: false
                        system_name: user_1_1
                        security_keys_enabled: false
                        security_keys_assignments: []
                        type: subaccount
                        username: user_1_1
          description: Success response
        '401':
          $ref: '#/components/responses/ErrorMessageResponse'
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_subaccounts \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 4947,
              "method": "private/get_subaccounts",
              "params": {
                "with_portfolio": true
              }
            }'
        - lang: bash
          label: cURL (Metadata)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_subaccounts \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 4948,
              "method": "private/get_subaccounts",
              "params": {
                "with_portfolio": false
              }
            }'
components:
  schemas:
    PrivateGetSubaccountsResponse:
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
          type: array
          items:
            type: object
            properties:
              username:
                type: string
              type:
                enum:
                  - main
                  - subaccount
                type: string
              id:
                type: integer
                description: Account/Subaccount identifier
              email:
                type: string
                description: User email
              not_confirmed_email:
                type: string
                description: >-
                  New email address that has not yet been confirmed. This field
                  is only included if `with_portfolio` == `true`.
              security_keys_enabled:
                type: boolean
                description: >-
                  Whether Security Keys authentication is enabled. Omitted from
                  the main account entry when the caller lacks main account
                  access
              security_keys_assignments:
                type: array
                items:
                  type: string
                description: >-
                  Names of assignments with Security Keys assigned. Omitted from
                  the main account entry when the caller lacks main account
                  access
              system_name:
                type: string
                description: System generated user nickname
              receive_notifications:
                type: boolean
                description: >-
                  Email-forwarding flag reported for the account. It does not
                  reflect changes made with
                  `private/toggle_notifications_from_subaccount`; see the known
                  limitation there
              is_password:
                type: boolean
                description: >-
                  `true` when password for the subaccount has been configured.
                  Omitted from the main account entry when the caller lacks main
                  account access
              disabled_trading_products:
                type: array
                items:
                  type: string
                description: >-
                  List of disabled trading products. Omitted from the main
                  account entry when the caller lacks main account access
              trading_products_details:
                type: array
                items:
                  type: object
                  properties:
                    product:
                      type: string
                    enabled:
                      type: boolean
                    overwriteable:
                      type: boolean
                    requires_consent:
                      type: boolean
                description: >-
                  Per trading product, whether it is enabled and can be
                  overwritten for the account
              referrals_count:
                type: integer
                description: >-
                  Number of referrals of the account. Only included if
                  `with_portfolio` == `true`.
              margin_model:
                type: string
                description: Margin model
              login_enabled:
                type: boolean
                description: >-
                  Informs whether login to the subaccount is enabled. Omitted
                  from the main account entry when the caller lacks main account
                  access
              portfolio:
                $ref: '#/components/schemas/portfolio'
                description: >-
                  Present only when `with_portfolio` is true and the caller has
                  portfolio access to this entry. Without main account access,
                  omitted from the main account entry
            required:
              - username
              - email
              - type
              - receive_notifications
              - system_name
              - id
      required:
        - result
        - jsonrpc
      type: object
    portfolio:
      additionalProperties:
        $ref: '#/components/schemas/currency_portfolio'
      type: object
      description: Portfolio entries keyed by lowercase currency code.
    ErrorMessageResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
            data:
              description: Optional error details.
          required:
            - code
            - message
      required:
        - error
        - jsonrpc
      type: object
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
  responses:
    ErrorMessageResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorMessageResponse'
      description: Success response

````

## Related topics

- [private/toggle_notifications_from_subaccount](https://docs.deribit.com/api-reference/account-management/private-toggle_notifications_from_subaccount.md)
- [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api.md)
- [Moving Positions](https://docs.deribit.com/articles/moving-positions-api.md)
- [private/remove_subaccount](https://docs.deribit.com/api-reference/account-management/private-remove_subaccount.md)
- [private/toggle_subaccount_login](https://docs.deribit.com/api-reference/account-management/private-toggle_subaccount_login.md)