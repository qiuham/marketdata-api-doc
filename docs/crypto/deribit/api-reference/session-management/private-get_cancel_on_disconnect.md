---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/session-management/private-get_cancel_on_disconnect
api_type: JSON-RPC
updated_at: 2026-11-27 19:00:58.492643
---

# private/get_cancel_on_disconnect

> Read the current Cancel On Disconnect configuration.

- `scope=connection` (the default) returns the state for the current WebSocket connection and is available over WebSocket only. Over REST/HTTP it fails with `10030` (`must_be_websocket_request`), so HTTP clients must pass `scope=account`.
- `scope=account` returns the account setting, works over both WebSocket and REST/HTTP, and requires the `account:read` scope.

**Scope:** `account:read` (only for `scope=account`)

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_cancel_on_disconnect)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_cancel_on_disconnect
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
  /private/get_cancel_on_disconnect:
    get:
      tags:
        - Session Management
        - Private
      description: >+
        Read the current Cancel On Disconnect configuration.


        - `scope=connection` (the default) returns the state for the current
        WebSocket connection and is available over WebSocket only. Over
        REST/HTTP it fails with `10030` (`must_be_websocket_request`), so HTTP
        clients must pass `scope=account`.

        - `scope=account` returns the account setting, works over both WebSocket
        and REST/HTTP, and requires the `account:read` scope.


        **Scope:** `account:read` (only for `scope=account`)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_cancel_on_disconnect)

      parameters:
        - name: scope
          in: query
          required: false
          schema:
            type: string
            enum:
              - connection
              - account
            default: connection
          description: >-
            Specifies if Cancel On Disconnect change should be applied/checked
            for the current connection or the account (default -
            `connection`)<br/><br/> **NOTICE:** Scope `connection` can be used
            only when working via Websocket.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 220
                  method: private/get_cancel_on_disconnect
                  params:
                    scope: account
              connectionRequest:
                summary: Connection Request
                value:
                  jsonrpc: '2.0'
                  id: 221
                  method: private/get_cancel_on_disconnect
                  params:
                    scope: connection
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetCancelOnDisconnectResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 220
                    result:
                      scope: account
                      enabled: false
                connectionResponse:
                  summary: Connection response example
                  value:
                    jsonrpc: '2.0'
                    id: 221
                    result:
                      scope: connection
                      enabled: true
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_cancel_on_disconnect \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 220,
              "method": "private/get_cancel_on_disconnect",
              "params": {
                "scope": "account"
              }
            }'
        - lang: json
          label: WebSocket (Connection)
          source: |-
            {
              "jsonrpc": "2.0",
              "id": 221,
              "method": "private/get_cancel_on_disconnect",
              "params": {
                "scope": "connection"
              }
            }
components:
  schemas:
    PrivateGetCancelOnDisconnectResponse:
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
            scope:
              $ref: '#/components/schemas/cod_scope'
            enabled:
              $ref: '#/components/schemas/enabled_field'
          required:
            - scope
            - enabled
      required:
        - result
        - jsonrpc
      type: object
    cod_scope:
      enum:
        - connection
        - account
      type: string
      description: >-
        Informs if Cancel on Disconnect was checked for the current connection
        or the account
    enabled_field:
      example: true
      type: boolean
      description: Current configuration status

````

## Related topics

- [private/disable_cancel_on_disconnect](https://docs.deribit.com/api-reference/session-management/private-disable_cancel_on_disconnect.md)
- [private/enable_cancel_on_disconnect](https://docs.deribit.com/api-reference/session-management/private-enable_cancel_on_disconnect.md)
- [private/logout](https://docs.deribit.com/api-reference/authentication/private-logout.md)
- [private/get_open_orders](https://docs.deribit.com/api-reference/trading/private-get_open_orders.md)
- [private/get_order_state](https://docs.deribit.com/api-reference/trading/private-get_order_state.md)