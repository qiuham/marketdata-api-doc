---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/session-management/public-set_heartbeat
api_type: JSON-RPC
updated_at: 2026-11-24 18:59:52.691176
---

# public/set_heartbeat

> Signals the WebSocket connection to send and request heartbeats. Heartbeats are used to detect stale or broken connections.

**Heartbeat & Disconnect Lifecycle:**

- When no message has been sent to the client for `interval` seconds, the server sends a `heartbeat` notification (`"params": {"type": "heartbeat"}`).
- When no message has been received from the client for `interval` seconds (plus 500 ms), the server sends a `heartbeat` notification with `"params": {"type": "test_request"}`. Respond by sending a `/api/v2/public/test` request.
- Any JSON text message from the client counts as activity and restarts this timer; WebSocket-level ping/pong frames and the plain-text `ping` / `PING` messages do not.
- If the connection stays silent until `(2 * interval) + 500 ms` after the last client message, the server closes the WebSocket with **close code 4000** (`heartbeat close`).
- If Cancel on Disconnect is enabled for the connection (connection or account scope), orders created over this connection are cancelled when it is closed.
- Calling this method again replaces the previous interval.

**Validation:** `interval` must be an integer between 10 and 300 seconds inclusive. Any other value (including fractional numbers) returns JSON-RPC error `-32602`.

**WebSocket Only:** This method is designed exclusively for WebSocket connections. Calling it over REST/HTTP returns error `10030` (`must_be_websocket_request`).

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fset_heartbeat)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/set_heartbeat
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
  /public/set_heartbeat:
    get:
      tags:
        - Session Management
        - Public
        - WebSocket Only
      description: >+
        Signals the WebSocket connection to send and request heartbeats.
        Heartbeats are used to detect stale or broken connections.


        **Heartbeat & Disconnect Lifecycle:**


        - When no message has been sent to the client for `interval` seconds,
        the server sends a `heartbeat` notification (`"params": {"type":
        "heartbeat"}`).

        - When no message has been received from the client for `interval`
        seconds (plus 500 ms), the server sends a `heartbeat` notification with
        `"params": {"type": "test_request"}`. Respond by sending a
        `/api/v2/public/test` request.

        - Any JSON text message from the client counts as activity and restarts
        this timer; WebSocket-level ping/pong frames and the plain-text `ping` /
        `PING` messages do not.

        - If the connection stays silent until `(2 * interval) + 500 ms` after
        the last client message, the server closes the WebSocket with **close
        code 4000** (`heartbeat close`).

        - If Cancel on Disconnect is enabled for the connection (connection or
        account scope), orders created over this connection are cancelled when
        it is closed.

        - Calling this method again replaces the previous interval.


        **Validation:** `interval` must be an integer between 10 and 300 seconds
        inclusive. Any other value (including fractional numbers) returns
        JSON-RPC error `-32602`.


        **WebSocket Only:** This method is designed exclusively for WebSocket
        connections. Calling it over REST/HTTP returns error `10030`
        (`must_be_websocket_request`).


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fset_heartbeat)

      parameters:
        - in: query
          name: interval
          required: true
          schema:
            example: 30
            type: integer
            minimum: 10
            maximum: 300
          description: 'The heartbeat interval in seconds (allowed range: 10 to 300)'
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 9098
                  method: public/set_heartbeat
                  params:
                    interval: 30
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
                    id: 9098
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: json
          label: WebSocket
          source: |-
            {
              "jsonrpc": "2.0",
              "id": 9098,
              "method": "public/set_heartbeat",
              "params": {
                "interval": 30
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

- [public/disable_heartbeat](https://docs.deribit.com/api-reference/session-management/public-disable_heartbeat.md)
- [Connection Management](https://docs.deribit.com/articles/connection-management-best-practices.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [private/enable_cancel_on_disconnect](https://docs.deribit.com/api-reference/session-management/private-enable_cancel_on_disconnect.md)
- [public/test](https://docs.deribit.com/api-reference/supporting/public-test.md)