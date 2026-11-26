---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/session-management/private-disable_cancel_on_disconnect
api_type: JSON-RPC
updated_at: 2026-11-26 19:02:05.653751
---

# private/disable_cancel_on_disconnect

> Disable Cancel On Disconnect for the connection.

When change is applied for the account, then every newly opened connection will start with **inactive** Cancel on Disconnect.

**Scope & transport:**

- `scope=connection` (the default) applies to the current WebSocket connection only and is available over WebSocket only. Over REST/HTTP it fails with `10030` (`must_be_websocket_request`), so HTTP clients must pass `scope=account`.
- `scope=account` changes the account setting, works over both WebSocket and REST/HTTP, and requires the `account:read_write` scope. Connection scope only requires an authenticated connection.

**Scope:** `account:read_write` (only for `scope=account`)

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fdisable_cancel_on_disconnect)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/disable_cancel_on_disconnect
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
  /private/disable_cancel_on_disconnect:
    get:
      tags:
        - Session Management
        - Private
      description: >+
        Disable Cancel On Disconnect for the connection.


        When change is applied for the account, then every newly opened
        connection will start with **inactive** Cancel on Disconnect.


        **Scope & transport:**


        - `scope=connection` (the default) applies to the current WebSocket
        connection only and is available over WebSocket only. Over REST/HTTP it
        fails with `10030` (`must_be_websocket_request`), so HTTP clients must
        pass `scope=account`.

        - `scope=account` changes the account setting, works over both WebSocket
        and REST/HTTP, and requires the `account:read_write` scope. Connection
        scope only requires an authenticated connection.


        **Scope:** `account:read_write` (only for `scope=account`)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fdisable_cancel_on_disconnect)

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
                  id: 1569
                  method: private/disable_cancel_on_disconnect
                  params:
                    scope: account
              connectionRequest:
                summary: Connection Request
                value:
                  jsonrpc: '2.0'
                  id: 1570
                  method: private/disable_cancel_on_disconnect
                  params:
                    scope: connection
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
                    id: 1569
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/disable_cancel_on_disconnect \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 1569,
              "method": "private/disable_cancel_on_disconnect",
              "params": {
                "scope": "account"
              }
            }'
        - lang: json
          label: WebSocket (Connection)
          source: |-
            {
              "jsonrpc": "2.0",
              "id": 1570,
              "method": "private/disable_cancel_on_disconnect",
              "params": {
                "scope": "connection"
              }
            }
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

- [private/enable_cancel_on_disconnect](https://docs.deribit.com/api-reference/session-management/private-enable_cancel_on_disconnect.md)
- [private/get_cancel_on_disconnect](https://docs.deribit.com/api-reference/session-management/private-get_cancel_on_disconnect.md)
- [private/cancel](https://docs.deribit.com/api-reference/trading/private-cancel.md)
- [private/logout](https://docs.deribit.com/api-reference/authentication/private-logout.md)
- [Cancel on Disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md)