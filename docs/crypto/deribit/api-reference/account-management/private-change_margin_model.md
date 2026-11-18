---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-change_margin_model
api_type: JSON-RPC
updated_at: 2026-11-18 05:08:40.915278
---

# private/change_margin_model

> Changes the margin model for the authenticated account or a specified subaccount. Margin models determine how margin requirements are calculated (e.g., Standard Margin vs. Portfolio Margin).

Changing the margin model may affect margin requirements, available funds, and trading capabilities. Use the `dry_run` parameter to preview the impact of the change before applying it. A dry run runs the same checks as the actual change.

Returns an error if a currency would be left with negative equity, an unfunded long option position, or insufficient funds.

**📖 Related Article:** [Margin types and usage](https://support.deribit.com/hc/en-us/articles/25944811317149-Margin-types-and-usage)

**Scope:** `account:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fchange_margin_model)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/change_margin_model
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
  /private/change_margin_model:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Changes the margin model for the authenticated account or a specified
        subaccount. Margin models determine how margin requirements are
        calculated (e.g., Standard Margin vs. Portfolio Margin).


        Changing the margin model may affect margin requirements, available
        funds, and trading capabilities. Use the `dry_run` parameter to preview
        the impact of the change before applying it. A dry run runs the same
        checks as the actual change.


        Returns an error if a currency would be left with negative equity, an
        unfunded long option position, or insufficient funds.


        **📖 Related Article:** [Margin types and
        usage](https://support.deribit.com/hc/en-us/articles/25944811317149-Margin-types-and-usage)


        **Scope:** `account:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fchange_margin_model)

      parameters:
        - name: user_id
          in: query
          schema:
            type: integer
            example: 1
          required: false
          description: Id of a (sub)account - by default current user id is used
        - name: margin_model
          in: query
          schema:
            type: string
            enum:
              - cross_pm
              - cross_sm
              - segregated_pm
              - segregated_sm
          required: true
          description: Margin model
        - name: dry_run
          in: query
          schema:
            example: true
            type: boolean
          required: false
          description: >-
            If `true` request returns the result without switching the margining
            model. Default: `false`
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 1
                  method: private/change_margin_model
                  params:
                    user_id: 3
                    margin_model: cross_pm
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateChangeMarginModelResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 1
                    result:
                      - old_state:
                          maintenance_margin_rate: 0
                          initial_margin_rate: 0
                          available_balance: 0
                        new_state:
                          maintenance_margin_rate: 0
                          initial_margin_rate: 0
                          available_balance: 0
                        currency: eth
                      - old_state:
                          maintenance_margin_rate: 0.02862727
                          initial_margin_rate: 0.45407615
                          available_balance: 0.553590509
                        new_state:
                          maintenance_margin_rate: 0.02710204
                          initial_margin_rate: 0.03252245
                          available_balance: 0.98106428
                        currency: btc
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/change_margin_model \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 1,
              "method": "private/change_margin_model",
              "params": {
                "user_id": 3,
                "margin_model": "cross_pm"
              }
            }'
components:
  schemas:
    PrivateChangeMarginModelResponse:
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
              old_state:
                type: object
                properties:
                  maintenance_margin_rate:
                    type: number
                    description: Maintenance margin rate before change
                  initial_margin_rate:
                    type: number
                    description: Initial margin rate before change
                  available_balance:
                    type: number
                    description: Available balance before change
                required:
                  - maintenance_margin_rate
                  - initial_margin_rate
                  - available_balance
                description: Represents portfolio state before change
              new_state:
                type: object
                properties:
                  maintenance_margin_rate:
                    type: number
                    description: Maintenance margin rate after change
                  initial_margin_rate:
                    type: number
                    description: Initial margin rate after change
                  available_balance:
                    type: number
                    description: Available balance after change
                required:
                  - maintenance_margin_rate
                  - initial_margin_rate
                  - available_balance
                description: Represents portfolio state after change
              currency:
                $ref: '#/components/schemas/currency'
            required:
              - old_state
              - new_state
              - currency
      required:
        - result
        - jsonrpc
      type: object
    currency:
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
      type: string
      description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`

````

## Related topics

- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/simulate_portfolio](https://docs.deribit.com/api-reference/account-management/private-simulate_portfolio.md)
- [Account Model](https://docs.deribit.com/starbase/account-model.md)