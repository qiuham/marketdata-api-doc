---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/trading/private-get_order_margin_by_ids
api_type: JSON-RPC
updated_at: 2026-11-18 18:59:20.134298
---

# private/get_order_margin_by_ids

> Retrieves the initial margin requirements for one or more orders identified by their order IDs. Initial margin is the amount of funds required to open a position with these orders.

This method is useful for calculating margin requirements before placing orders, helping to ensure sufficient funds are available.

**Scope:** `trade:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_order_margin_by_ids)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_order_margin_by_ids
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
  /private/get_order_margin_by_ids:
    get:
      tags:
        - Trading
        - Private
      description: >+
        Retrieves the initial margin requirements for one or more orders
        identified by their order IDs. Initial margin is the amount of funds
        required to open a position with these orders.


        This method is useful for calculating margin requirements before placing
        orders, helping to ensure sufficient funds are available.


        **Scope:** `trade:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_order_margin_by_ids)

      parameters:
        - name: ids
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
              example: '123456'
            example:
              - ETH-349280
              - ETH-349279
              - ETH-349278
          description: Ids of orders
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
                  id: 5625
                  method: private/get_order_margin_by_ids
                  params:
                    ids:
                      - ETH-349280
                      - ETH-349279
                      - ETH-349278
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetOrderMarginByIdsResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 5625
                    result:
                      - order_id: ETH-349278
                        initial_margin: 0.00091156
                        initial_margin_currency: ETH
                      - order_id: ETH-349279
                        initial_margin: 0
                        initial_margin_currency: ETH
                      - order_id: ETH-349280
                        initial_margin: 0
                        initial_margin_currency: ETH
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_order_margin_by_ids \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 5625,
              "method": "private/get_order_margin_by_ids",
              "params": {
                "ids": [
                  "ETH-349280",
                  "ETH-349279",
                  "ETH-349278"
                ]
              }
            }'
components:
  schemas:
    PrivateGetOrderMarginByIdsResponse:
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
            $ref: '#/components/schemas/order_id_initial_margin_pair'
      required:
        - result
        - jsonrpc
      type: object
    order_id_initial_margin_pair:
      properties:
        order_id:
          $ref: '#/components/schemas/order_id'
        initial_margin:
          type: number
          description: Initial margin of order
        initial_margin_currency:
          type: string
          description: Currency of initial margin
      required:
        - order_id
        - initial_margin
      type: object
    order_id:
      example: ETH-100234
      type: string
      description: Unique order identifier

````

## Related topics

- [private/get_margins](https://docs.deribit.com/api-reference/trading/private-get_margins.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)
- [private/get_subaccounts_details](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts_details.md)
- [private/get_order_state](https://docs.deribit.com/api-reference/trading/private-get_order_state.md)
- [private/get_open_orders](https://docs.deribit.com/api-reference/trading/private-get_open_orders.md)