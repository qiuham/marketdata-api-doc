---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/session-management/public-disable_heartbeat
api_type: JSON-RPC
updated_at: 2026-11-23 19:00:38.819785
---

# public/disable_heartbeat

> Stop sending heartbeat messages. This method takes no parameters.

It also stops the server-side monitoring of client activity configured by [public/set_heartbeat](https://docs.deribit.com/api-reference/session-management/public-set_heartbeat): after this call the server neither sends `test_request` messages nor closes the connection with code 4000. The regular WebSocket idle timeout (10 minutes without incoming data) still applies.

**WebSocket Only:** This method is designed exclusively for WebSocket connections. Calling it over REST/HTTP returns error `10030` (`must_be_websocket_request`).

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fdisable_heartbeat)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/disable_heartbeat
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
  /public/disable_heartbeat:
    get:
      tags:
        - Session Management
        - WebSocket Only
        - Public
      description: >+
        Stop sending heartbeat messages. This method takes no parameters.


        It also stops the server-side monitoring of client activity configured
        by
        [public/set_heartbeat](https://docs.deribit.com/api-reference/session-management/public-set_heartbeat):
        after this call the server neither sends `test_request` messages nor
        closes the connection with code 4000. The regular WebSocket idle timeout
        (10 minutes without incoming data) still applies.


        **WebSocket Only:** This method is designed exclusively for WebSocket
        connections. Calling it over REST/HTTP returns error `10030`
        (`must_be_websocket_request`).


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fdisable_heartbeat)

      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 3562
                  method: public/disable_heartbeat
                  params: {}
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
                    id: 3562
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: json
          label: WebSocket
          source: |-
            {
              "jsonrpc": "2.0",
              "id": 3562,
              "method": "public/disable_heartbeat",
              "params": {}
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

- [Connection Management](https://docs.deribit.com/articles/connection-management-best-practices.md)
- [public/set_heartbeat](https://docs.deribit.com/api-reference/session-management/public-set_heartbeat.md)
- [private/disable_api_key](https://docs.deribit.com/api-reference/account-management/private-disable_api_key.md)
- [Asymmetric API Keys](https://docs.deribit.com/articles/asymmetric-api-keys.md)
- [public/status](https://docs.deribit.com/api-reference/supporting/public-status.md)